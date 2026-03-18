"""
stick_slip_galaxy.py
====================

Toy model: does stick-slip mode-locking produce flat galaxy rotation curves?

Hypothesis (Joven 2026 / ChatGPT consultation):
  "A galaxy disk behaves like a weakly damped, driven, resonance-structured
   oscillator network. Outer-disk kinematics are governed by subharmonic
   capture and threshold slip. The flat part of the rotation curve is a
   macroscopic average over mode-locking plateaus."

This is a falsifiability test. Positive result: ⟨v_circ(r)⟩ = r·⟨φ̇(r)⟩ is
approximately constant across outer-disk radii. Negative result: it follows
Keplerian (∝ r^{-1/2}) or solid-body (∝ r) profile despite locking.

Either outcome is informative. Both are documented below.

Physical units: G = M = 1, so ω_K(r) = r^{-3/2}.

Parameter choices (motivated by bowed-string / tectonic-fault analogy,
NOT tuned post-hoc to fit a specific rotation curve):
  α      ~ 0.03  : weak damping (galaxies are weakly dissipative)
  ε      ~ 0.10  : pattern coupling (~10% spiral arm perturbation)
  μ_k    ~ 0.06  : kinetic friction (< ε so locking is possible)
  μ_s    ~ 0.09  : static friction (> μ_k, Coulomb model)
  Δ_lock ~ 0.025 : velocity window to acquire lock
  Δ_slip ~ 0.10  : accumulated-stress threshold to break lock

Companion work:
  stick_slip_lagrangian.ipynb — Lagrangian relaxation framing (dual variable)
  This notebook tests whether the dynamical mechanism alone, without invoking
  the optimization dual, produces the observed phenomenology.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import matplotlib.colors as mcolors

# ─────────────────────────────────────────────────────────────────────
# Global parameters
# ─────────────────────────────────────────────────────────────────────

GM      = 1.0       # gravitational parameter
OMEGA_P = 0.30      # pattern angular speed (co-rotation at r_c ≈ 2.24)
ALPHA   = 0.030     # damping toward Keplerian orbit
EPSILON = 0.10      # sinusoidal pattern coupling amplitude
MU_K    = 0.060     # kinetic friction toward pattern speed
MU_S    = 0.090     # static friction (locked-state threshold)
D_LOCK  = 0.025     # |v − Ω_p| < D_LOCK → acquire lock
D_SLIP  = 0.100     # |accumulated stress| > D_SLIP → break lock
DT      = 0.05      # timestep (Euler integration)
T_TOTAL = 3000.0    # integration time per annulus
T_BURN  = 600.0     # discard transient


def omega_K(r):
    """Keplerian angular frequency at radius r (code units G=M=1)."""
    return np.sqrt(GM / r**3)


# ─────────────────────────────────────────────────────────────────────
# Core simulator
# ─────────────────────────────────────────────────────────────────────

def simulate_annulus(r, omega_p=OMEGA_P, alpha=ALPHA, epsilon=EPSILON,
                     mu_k=MU_K, d_lock=D_LOCK, d_slip=D_SLIP,
                     T=T_TOTAL, dt=DT, seed=0):
    """
    Simulate one galactic annulus at radius r.

    Equation of motion (unlocked):
        dv/dt = −α(v − ω_K)               [Keplerian restoring]
              + ε·sin(Ω_p·t − φ)          [sinusoidal pattern coupling]
              − μ_k·sign(v − Ω_p)         [kinetic friction toward pattern]

    Stick-slip rule (1:1 resonance at v = Ω_p):
        Lock  when |v − Ω_p| < d_lock
        Unlock when accumulated stress |s| > d_slip
        On unlock: v ← Ω_p + 0.5·s  (partial release of elastic energy)

    Returns (after discarding burn-in):
        t, v (φ̇), Delta (v − Ω_p), locked (bool array)
    """
    rng = np.random.default_rng(seed)
    N       = int(T / dt)
    N_burn  = int(T_BURN / dt)
    wK      = omega_K(r)

    phi    = rng.uniform(0, 2 * np.pi)
    v      = wK + rng.normal(0, 0.01)
    locked = False
    stress = 0.0

    t_arr  = np.empty(N - N_burn)
    v_arr  = np.empty(N - N_burn)
    D_arr  = np.empty(N - N_burn)
    lk_arr = np.empty(N - N_burn, dtype=bool)

    for i in range(N):
        t_now = i * dt
        psi   = omega_p * t_now  # pattern phase

        if locked:
            v_lock = omega_p
            phi   += v_lock * dt
            # force the free system would feel at lock point
            f_free = (-alpha * (v_lock - wK)
                      + epsilon * np.sin(psi - phi))
            stress += f_free * dt
            if abs(stress) > d_slip:
                locked = False
                v      = v_lock + 0.5 * stress
                stress = 0.0
            else:
                v = v_lock
        else:
            Delta = v - omega_p
            dv    = (-alpha * (v - wK)
                     + epsilon * np.sin(psi - phi)
                     - mu_k * np.sign(Delta))
            v   += dv * dt
            phi += v * dt

            if abs(v - omega_p) < d_lock:
                locked = True
                v      = omega_p
                stress = 0.0

        if i >= N_burn:
            idx          = i - N_burn
            t_arr[idx]   = t_now - T_BURN
            v_arr[idx]   = v
            D_arr[idx]   = v - omega_p
            lk_arr[idx]  = locked

    return t_arr, v_arr, D_arr, lk_arr


# ─────────────────────────────────────────────────────────────────────
# Step 1: Single annulus — time series, power spectrum, phase portrait
# ─────────────────────────────────────────────────────────────────────

def step1_single_annulus(r_demo=5.0, save=True):
    print(f"\n── Step 1: Single annulus  r = {r_demo} ──")
    t, v, Delta, locked = simulate_annulus(r_demo)
    wK     = omega_K(r_demo)
    f_lock = locked.mean()
    v_mean = v.mean()
    print(f"  ω_K(r) = {wK:.4f},  Ω_p = {OMEGA_P:.4f}")
    print(f"  Locked fraction : {f_lock:.3f}")
    print(f"  ⟨φ̇⟩  = {v_mean:.4f}  "
          f"(Ω_p = {OMEGA_P:.4f},  ω_K = {wK:.4f})")
    print(f"  ⟨v_circ⟩ = r·⟨φ̇⟩ = {v_mean * r_demo:.4f}")

    freq  = np.fft.rfftfreq(len(v), d=t[1] - t[0])
    power = np.abs(np.fft.rfft(v - v_mean))**2

    fig = plt.figure(figsize=(14, 10))
    gs  = GridSpec(3, 2, figure=fig, hspace=0.45, wspace=0.35)

    t_win = 500.0
    m = t < t_win

    # — velocity time series —
    ax1 = fig.add_subplot(gs[0, :])
    ax1.plot(t[m], v[m], 'b-', lw=0.6, alpha=0.85, label='φ̇(t)')
    ax1.fill_between(t[m], v.min() * 0.85, v.max() * 1.15,
                     where=locked[m], alpha=0.15, color='red', label='locked')
    ax1.axhline(OMEGA_P,     c='r',      ls='--', lw=1.5, label=f'Ω_p = {OMEGA_P}')
    ax1.axhline(wK,          c='g',      ls=':',  lw=1.5, label=f'ω_K = {wK:.3f}')
    ax1.axhline(OMEGA_P / 2, c='orange', ls='--', lw=1.0,
                label=f'Ω_p/2 = {OMEGA_P/2:.3f}')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('φ̇')
    ax1.set_title(f'Angular velocity  (r={r_demo})  —  locked fraction = {f_lock:.2f},'
                  f'  ⟨φ̇⟩ = {v_mean:.4f}')
    ax1.legend(fontsize=8, ncol=3, loc='upper right')
    ax1.set_ylim(max(0, wK * 0.5), OMEGA_P * 1.3)

    # — detuning Δ(t) —
    ax2 = fig.add_subplot(gs[1, 0])
    ax2.plot(t[m], Delta[m], color='purple', lw=0.6)
    for val, c in [(D_SLIP, 'r'), (-D_SLIP, 'r'),
                   (D_LOCK, 'g'), (-D_LOCK, 'g')]:
        ax2.axhline(val, c=c, ls=':', lw=1.0)
    ax2.axhline(0, c='k', lw=0.5)
    ax2.set_xlabel('Time')
    ax2.set_ylabel('Δ = φ̇ − Ω_p')
    ax2.set_title('Detuning Δ(t)  — sawtooth → ramp-and-reset')

    # — power spectrum —
    ax3 = fig.add_subplot(gs[1, 1])
    ax3.semilogy(freq[1:], power[1:], 'k-', lw=0.6, alpha=0.8)
    ax3.axvline(OMEGA_P / (2 * np.pi), c='r',      ls='--', lw=1.5,
                label='Ω_p / 2π')
    ax3.axvline(OMEGA_P / (4 * np.pi), c='orange', ls='--', lw=1.5,
                label='Ω_p / 4π  (subharmonic)')
    ax3.axvline(wK / (2 * np.pi), c='g', ls=':', lw=1.5, label='ω_K / 2π')
    ax3.set_xlabel('Frequency')
    ax3.set_ylabel('Power')
    ax3.set_title('Power spectrum of φ̇(t)')
    ax3.legend(fontsize=8)
    ax3.set_xlim(0, OMEGA_P / np.pi)

    # — phase portrait —
    ax4 = fig.add_subplot(gs[2, :])
    sc = ax4.scatter(Delta[::4], v[::4], c=locked[::4].astype(float),
                     cmap='RdYlBu_r', s=1, alpha=0.4, vmin=0, vmax=1)
    plt.colorbar(sc, ax=ax4, label='locked (1) / free (0)')
    ax4.axvline(0, c='k', lw=0.5)
    ax4.axhline(OMEGA_P, c='r',      ls='--', lw=1.0, label='Ω_p')
    ax4.axhline(wK,      c='g',      ls=':',  lw=1.0, label='ω_K')
    ax4.axvline( D_LOCK, c='g',      ls=':',  lw=0.8)
    ax4.axvline(-D_LOCK, c='g',      ls=':',  lw=0.8)
    ax4.set_xlabel('Δ = φ̇ − Ω_p')
    ax4.set_ylabel('φ̇')
    ax4.set_title('Phase portrait  (Δ, φ̇)  —  blue = locked,  red = free')
    ax4.legend(fontsize=8)

    plt.suptitle(f'Step 1: Single Annulus Dynamics   [r={r_demo},  Ω_p={OMEGA_P}]',
                 fontsize=13, fontweight='bold')

    if save:
        fig.savefig('fig_step1_single_annulus.png', dpi=150, bbox_inches='tight')
        print("  Saved: fig_step1_single_annulus.png")
    plt.close(fig)
    return {'f_lock': f_lock, 'v_mean': v_mean, 'wK': wK}


# ─────────────────────────────────────────────────────────────────────
# Step 2: Radial array — rotation curve
# ─────────────────────────────────────────────────────────────────────

def step2_rotation_curve(radii=None, save=True):
    if radii is None:
        radii = np.linspace(1.0, 10.0, 24)
    print(f"\n── Step 2: Rotation curve  ({len(radii)} annuli) ──")

    v_mean_arr  = np.zeros(len(radii))
    v_kep_arr   = np.zeros(len(radii))
    v_flat_arr  = np.zeros(len(radii))   # solid-body at Ω_p
    f_lock_arr  = np.zeros(len(radii))

    for j, r in enumerate(radii):
        _, v, _, locked = simulate_annulus(r, seed=j)
        v_mean_arr[j] = v.mean()
        v_kep_arr[j]  = omega_K(r)
        v_flat_arr[j] = OMEGA_P
        f_lock_arr[j] = locked.mean()
        print(f"  r={r:5.2f}  ω_K={omega_K(r):.4f}  "
              f"⟨φ̇⟩={v_mean_arr[j]:.4f}  "
              f"v_circ={v_mean_arr[j]*r:.4f}  "
              f"lock={f_lock_arr[j]:.2f}")

    v_circ     = v_mean_arr * radii
    v_circ_kep = v_kep_arr  * radii   # = √(GM/r) Keplerian curve
    v_circ_sb  = v_flat_arr * radii   # solid body

    # Flatness metric: std / mean of v_circ in outer half
    outer = radii > radii.mean()
    flat_metric = np.std(v_circ[outer]) / np.mean(v_circ[outer])
    print(f"\n  Flatness metric (outer disk std/mean): {flat_metric:.4f}")
    print(f"  (0 = perfectly flat; Keplerian reference: "
          f"{np.std(v_circ_kep[outer])/np.mean(v_circ_kep[outer]):.4f})")

    fig, axes = plt.subplots(2, 2, figsize=(12, 9))
    fig.suptitle('Step 2: Rotation Curve from Stick-Slip Array', fontsize=13,
                 fontweight='bold')

    ax = axes[0, 0]
    ax.plot(radii, v_circ,     'b-o', ms=4, lw=1.5, label='⟨v_circ⟩ (simulated)')
    ax.plot(radii, v_circ_kep, 'g--', lw=1.5, label='Keplerian  √(GM/r)')
    ax.plot(radii, v_circ_sb,  'r:',  lw=1.5, label='Solid-body  Ω_p·r')
    ax.axvline(np.sqrt(GM / OMEGA_P**2)**(1/1), c='gray', ls=':', lw=1,
               label=f'co-rotation r_c ≈ {(GM/OMEGA_P**2)**(1/3):.2f}')
    ax.set_xlabel('Radius r')
    ax.set_ylabel('v_circ = r·⟨φ̇⟩')
    ax.set_title('Rotation curve')
    ax.legend(fontsize=8)

    ax = axes[0, 1]
    ax.plot(radii, v_mean_arr,  'b-o', ms=4, lw=1.5, label='⟨φ̇⟩')
    ax.plot(radii, v_kep_arr,   'g--', lw=1.5, label='ω_K(r)')
    ax.axhline(OMEGA_P, c='r', ls='--', lw=1.5, label='Ω_p')
    ax.set_xlabel('Radius r')
    ax.set_ylabel('⟨φ̇⟩')
    ax.set_title('Mean angular velocity vs radius')
    ax.legend(fontsize=8)

    ax = axes[1, 0]
    ax.plot(radii, f_lock_arr, 'k-o', ms=4, lw=1.5)
    ax.axvline((GM / OMEGA_P**2)**(1/3), c='gray', ls=':', lw=1)
    ax.set_xlabel('Radius r')
    ax.set_ylabel('Fraction of time locked')
    ax.set_title('Locking fraction vs radius')
    ax.set_ylim(-0.05, 1.05)

    ax = axes[1, 1]
    ax.text(0.05, 0.92, f'Flatness metric (outer half):', transform=ax.transAxes,
            fontsize=10, fontweight='bold')
    ax.text(0.05, 0.80, f'  Simulated:  {flat_metric:.4f}',
            transform=ax.transAxes, fontsize=10, color='blue')
    ax.text(0.05, 0.68,
            f'  Keplerian:  '
            f'{np.std(v_circ_kep[outer])/np.mean(v_circ_kep[outer]):.4f}',
            transform=ax.transAxes, fontsize=10, color='green')
    ax.text(0.05, 0.56,
            f'  Solid-body: '
            f'{np.std(v_circ_sb[outer])/np.mean(v_circ_sb[outer]):.4f}',
            transform=ax.transAxes, fontsize=10, color='red')
    ax.text(0.05, 0.40,
            'Interpretation:\n'
            '  < 0.05 → flat (positive result)\n'
            '  ~ Keplerian → locking not producing flat\n'
            '  ~ Solid-body → 1:1 lock dominates',
            transform=ax.transAxes, fontsize=9)
    ax.text(0.05, 0.15,
            f'Ω_p = {OMEGA_P},  α = {ALPHA},  ε = {EPSILON},\n'
            f'μ_k = {MU_K},  Δ_lock = {D_LOCK},  Δ_slip = {D_SLIP}',
            transform=ax.transAxes, fontsize=8, color='gray')
    ax.axis('off')

    plt.tight_layout()
    if save:
        fig.savefig('fig_step2_rotation_curve.png', dpi=150, bbox_inches='tight')
        print("  Saved: fig_step2_rotation_curve.png")
    plt.close(fig)
    return {'radii': radii, 'v_circ': v_circ, 'flat_metric': flat_metric,
            'f_lock': f_lock_arr}


# ─────────────────────────────────────────────────────────────────────
# Step 3: Phase portrait — two entry paths to the locked state
# ─────────────────────────────────────────────────────────────────────

def step3_phase_portrait(r_demo=5.0, save=True):
    """
    Demonstrate two entry paths to the same locked state:
      Path A: annulus starting BELOW pattern speed (outer disk, slow-drive)
      Path B: annulus starting ABOVE pattern speed (inner disk / high-drive)
    This mirrors the two bowing modes (slow bow vs. high pressure).
    """
    print(f"\n── Step 3: Phase portrait — two-path entry  (r={r_demo}) ──")
    wK = omega_K(r_demo)

    def trace_path(v_init, T_short=300.0, seed=99):
        rng  = np.random.default_rng(seed)
        N    = int(T_short / DT)
        phi  = rng.uniform(0, 2 * np.pi)
        v    = v_init
        locked = False
        stress = 0.0
        vs, Ds, lks = [], [], []
        for i in range(N):
            psi = OMEGA_P * i * DT
            if locked:
                phi   += OMEGA_P * DT
                f_free = (-ALPHA * (OMEGA_P - wK)
                          + EPSILON * np.sin(psi - phi))
                stress += f_free * DT
                if abs(stress) > D_SLIP:
                    locked = False
                    v      = OMEGA_P + 0.5 * stress
                    stress = 0.0
                else:
                    v = OMEGA_P
            else:
                Delta = v - OMEGA_P
                dv    = (-ALPHA * (v - wK)
                         + EPSILON * np.sin(psi - phi)
                         - MU_K * np.sign(Delta))
                v   += dv * DT
                phi += v * DT
                if abs(v - OMEGA_P) < D_LOCK:
                    locked = True
                    v      = OMEGA_P
                    stress = 0.0
            vs.append(v)
            Ds.append(v - OMEGA_P)
            lks.append(locked)
        return np.array(Ds), np.array(vs), np.array(lks)

    D_A, v_A, lk_A = trace_path(wK * 0.4)              # Path A: slow (well below)
    D_B, v_B, lk_B = trace_path(OMEGA_P * 1.9)         # Path B: fast (well above)

    fig, axes = plt.subplots(1, 2, figsize=(13, 6))
    fig.suptitle('Step 3: Two Entry Paths to the Same Locked State',
                 fontsize=13, fontweight='bold')

    for ax, D, v_traj, lk, label, col in [
            (axes[0], D_A, v_A, lk_A, 'Path A: slow entry (below)', 'steelblue'),
            (axes[1], D_B, v_B, lk_B, 'Path B: fast entry (above)',  'firebrick')]:
        sc = ax.scatter(D[::2], v_traj[::2], c=np.arange(len(D[::2])),
                        cmap='viridis', s=4, alpha=0.6)
        plt.colorbar(sc, ax=ax, label='time step')
        ax.axvspan(-D_LOCK, D_LOCK, alpha=0.12, color='red', label='lock band')
        ax.axhline(OMEGA_P, c='r',  ls='--', lw=1.5, label=f'Ω_p = {OMEGA_P}')
        ax.axhline(wK,      c='g',  ls=':',  lw=1.5, label=f'ω_K = {wK:.3f}')
        ax.axhline(OMEGA_P / 2, c='orange', ls='--', lw=1.0,
                   label=f'Ω_p/2 = {OMEGA_P/2:.3f}')
        ax.set_xlabel('Δ = φ̇ − Ω_p')
        ax.set_ylabel('φ̇')
        ax.set_title(label)
        ax.legend(fontsize=8)

    if save:
        fig.savefig('fig_step3_phase_portrait.png', dpi=150, bbox_inches='tight')
        print("  Saved: fig_step3_phase_portrait.png")
    plt.close(fig)


# ─────────────────────────────────────────────────────────────────────
# Step 4: Parameter sweep — Arnold tongue boundary
# ─────────────────────────────────────────────────────────────────────

def step4_arnold_tongue(r_probe=5.0, n_alpha=12, n_mu=12, save=True):
    """
    Sweep over (α, μ_k) at fixed radius r_probe.
    For each (α, μ_k) compute:
      - flat_metric: std/mean of v_circ in outer half (proxy for flatness)
      - f_lock: fraction of time locked
    Identify the Arnold-tongue-like region where locking dominates.
    """
    print(f"\n── Step 4: Arnold tongue sweep  (r={r_probe}) ──")

    alpha_vals = np.linspace(0.005, 0.12, n_alpha)
    mu_vals    = np.linspace(0.005, 0.15, n_mu)

    f_lock_grid = np.zeros((n_alpha, n_mu))
    v_mean_grid = np.zeros((n_alpha, n_mu))

    # Also sweep a small radial array to get flatness
    radii_sweep = np.array([2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0])
    flat_grid   = np.zeros((n_alpha, n_mu))

    T_short = 1000.0  # shorter runs for sweep

    for i, alpha in enumerate(alpha_vals):
        for j, mu in enumerate(mu_vals):
            vcircs = []
            flocks = []
            for k, r in enumerate(radii_sweep):
                _, v, _, locked = simulate_annulus(
                    r, alpha=alpha, mu_k=mu,
                    T=T_short, seed=i * n_mu + j + k * 100)
                vcircs.append(v.mean() * r)
                flocks.append(locked.mean())
            vcircs = np.array(vcircs)
            flat_grid[i, j]   = np.std(vcircs) / (np.mean(vcircs) + 1e-10)
            f_lock_grid[i, j] = np.mean(flocks)
            v_mean_grid[i, j] = np.mean(vcircs)
        print(f"  α={alpha:.3f}  done")

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle('Step 4: Parameter Sweep — Arnold Tongue Boundary',
                 fontsize=13, fontweight='bold')

    ext = [mu_vals[0], mu_vals[-1], alpha_vals[0], alpha_vals[-1]]

    im0 = axes[0].imshow(f_lock_grid, origin='lower', aspect='auto',
                         extent=ext, cmap='hot')
    plt.colorbar(im0, ax=axes[0], label='locking fraction')
    axes[0].set_xlabel('μ_k  (friction)')
    axes[0].set_ylabel('α  (damping)')
    axes[0].set_title('Locking fraction\n(high = Arnold tongue)')
    axes[0].scatter([MU_K], [ALPHA], c='cyan', s=80, zorder=5,
                    label=f'default ({ALPHA},{MU_K})')
    axes[0].legend(fontsize=8)

    im1 = axes[1].imshow(flat_grid, origin='lower', aspect='auto',
                         extent=ext, cmap='viridis_r', vmax=0.5)
    plt.colorbar(im1, ax=axes[1], label='std/mean of v_circ')
    axes[1].set_xlabel('μ_k  (friction)')
    axes[1].set_ylabel('α  (damping)')
    axes[1].set_title('Flatness metric  (dark = flat)')
    axes[1].scatter([MU_K], [ALPHA], c='red', s=80, zorder=5,
                    label=f'default ({ALPHA},{MU_K})')
    axes[1].legend(fontsize=8)
    # Contour for "flat" region
    try:
        axes[1].contour(mu_vals, alpha_vals, flat_grid, levels=[0.08],
                        colors='white', linewidths=1.5,
                        linestyles='--')
    except Exception:
        pass

    # v_circ mean
    im2 = axes[2].imshow(v_mean_grid, origin='lower', aspect='auto',
                         extent=ext, cmap='plasma')
    plt.colorbar(im2, ax=axes[2], label='mean v_circ')
    axes[2].set_xlabel('μ_k  (friction)')
    axes[2].set_ylabel('α  (damping)')
    axes[2].set_title('Mean circular velocity\n(proxy for rotation curve amplitude)')
    axes[2].scatter([MU_K], [ALPHA], c='cyan', s=80, zorder=5)

    plt.tight_layout()
    if save:
        fig.savefig('fig_step4_arnold_tongue.png', dpi=150, bbox_inches='tight')
        print("  Saved: fig_step4_arnold_tongue.png")
    plt.close(fig)
    return {'flat_grid': flat_grid, 'f_lock_grid': f_lock_grid,
            'alpha_vals': alpha_vals, 'mu_vals': mu_vals}


# ─────────────────────────────────────────────────────────────────────
# Summary
# ─────────────────────────────────────────────────────────────────────

def print_summary(step1, step2, step4):
    flat_m  = step2['flat_metric']
    wK_demo = step1['wK']
    f_lock  = step1['f_lock']

    print("\n" + "═" * 60)
    print("RESULTS SUMMARY")
    print("═" * 60)

    print("\nStep 1 — Single annulus dynamics:")
    print(f"  Locked fraction  : {f_lock:.3f}")
    print(f"  Δ(t) structure   : inspect fig_step1_single_annulus.png")
    if f_lock > 0.3:
        print("  → Stick phases dominate: velocity plateaus present.")
    else:
        print("  → Weak locking: velocity near Keplerian most of the time.")

    print("\nStep 2 — Rotation curve:")
    print(f"  Flatness metric (outer disk std/mean): {flat_m:.4f}")
    if flat_m < 0.05:
        result = "POSITIVE — rotation curve is flat (< 5% variation)"
    elif flat_m < 0.15:
        result = "PARTIAL — flatter than Keplerian but not flat"
    else:
        result = "NEGATIVE — rotation curve is not flat"
    print(f"  Result: {result}")

    print("\nWhat this means:")
    if flat_m < 0.05:
        print("  The stick-slip mechanism, with these parameters, produces a")
        print("  rotation curve consistent with the hypothesis. Flatness emerges")
        print("  from time-averaging over locking plateaus.")
    elif flat_m < 0.15:
        result_text = (
            "  Partial flattening is observed. The 1:1 lock produces solid-body\n"
            "  tendencies; the slip phases introduce downward corrections toward\n"
            "  Keplerian. Their interplay produces intermediate flattening.\n"
            "  Subharmonic locking at Ω_p/n with n ∝ r would be needed for\n"
            "  strict flatness — see open question below."
        )
        print(result_text)
    else:
        result_text = (
            "  The mechanism does not produce a flat rotation curve at these\n"
            "  parameters with constant Ω_p.\n\n"
            "  Diagnosis:\n"
            "    1:1 locking → solid-body (v_circ ∝ r), not flat\n"
            "    Free Keplerian → v_circ ∝ r^{-1/2}, not flat\n"
            "  For flatness, subharmonic locking must satisfy:\n"
            "    ⟨φ̇(r)⟩ ∝ 1/r  →  lock target ∝ 1/r\n"
            "  This requires either:\n"
            "    (a) pattern speed Ω_p(r) ∝ 1/r  (flat dispersion relation)\n"
            "    (b) each annulus locks to the p/q resonance nearest ω_K(r)\n"
            "        with p/q scaling such that v_circ ≈ const\n"
            "  Neither arises naturally from constant Ω_p."
        )
        print(result_text)

    print("\nOpen questions not resolved by this model:")
    print("  - Does the pattern speed Ω_p(r) in real galaxies have the dispersion")
    print("    relation needed for subharmonic flatness?")
    print("  - Is the time-average over a staircase of subharmonic plateaus")
    print("    (p:q for varying q) approximately flat in the relevant r range?")
    print("  - Coupling to the companion notebook: does the Lagrangian relaxation")
    print("    dual variable (dark matter proxy) arise when this dynamical model")
    print("    is embedded in the optimization framing?")
    print("═" * 60)


# ─────────────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Stick-Slip Galaxy Toy Model")
    print(f"Ω_p={OMEGA_P}  α={ALPHA}  ε={EPSILON}  μ_k={MU_K}")
    print(f"Δ_lock={D_LOCK}  Δ_slip={D_SLIP}  dt={DT}  T={T_TOTAL}")

    step1 = step1_single_annulus(r_demo=5.0)
    step2 = step2_rotation_curve(radii=np.linspace(1.0, 10.0, 20))
    step3_phase_portrait(r_demo=5.0)
    step4 = step4_arnold_tongue(r_probe=5.0, n_alpha=10, n_mu=10)
    print_summary(step1, step2, step4)
