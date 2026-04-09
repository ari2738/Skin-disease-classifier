/* ── Reset & Variables ──────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg:        #0d0f14;
  --bg2:       #13161e;
  --bg3:       #1a1e29;
  --border:    rgba(255,255,255,0.08);
  --border2:   rgba(255,255,255,0.14);
  --text:      #e8eaf0;
  --muted:     #7a8099;
  --accent:    #4ecca3;
  --accent2:   #2bb38a;
  --danger:    #f06060;
  --warn:      #f0b060;
  --low:       #4ecca3;
  --radius:    16px;
  --font-head: 'DM Serif Display', serif;
  --font-body: 'DM Sans', sans-serif;
}

html { font-size: 16px; }
body {
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-body);
  font-weight: 400;
  min-height: 100vh;
  line-height: 1.6;
}

/* ── Nav ────────────────────────────────────────────────────── */
.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.2rem 2rem;
  border-bottom: 1px solid var(--border);
  background: var(--bg);
  position: sticky;
  top: 0;
  z-index: 100;
}

.nav-brand {
  font-family: var(--font-head);
  font-size: 1.4rem;
  color: var(--text);
  letter-spacing: -0.02em;
}
.nav-brand span { color: var(--accent); }

.nav-tabs { display: flex; gap: 4px; background: var(--bg3); border-radius: 10px; padding: 4px; }
.nav-tab {
  background: none;
  border: none;
  color: var(--muted);
  font-family: var(--font-body);
  font-size: 0.875rem;
  font-weight: 500;
  padding: 6px 18px;
  border-radius: 7px;
  cursor: pointer;
  transition: all 0.2s;
}
.nav-tab.active { background: var(--bg2); color: var(--text); }
.nav-tab:hover:not(.active) { color: var(--text); }

/* ── Tabs ───────────────────────────────────────────────────── */
.tab { display: none; }
.tab.active { display: block; }

/* ── Hero ───────────────────────────────────────────────────── */
.hero {
  padding: 3rem 2rem 2rem;
  max-width: 480px;
  margin: 0 auto;
  text-align: center;
}
.hero h1 {
  font-family: var(--font-head);
  font-size: 2.8rem;
  line-height: 1.15;
  color: var(--text);
  margin-bottom: 1rem;
  letter-spacing: -0.03em;
}
.hero h1 em { color: var(--accent); font-style: italic; }
.hero p { color: var(--muted); font-size: 0.95rem; line-height: 1.7; }

/* ── Main Grid ──────────────────────────────────────────────── */
.main-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1.5rem;
  max-width: 900px;
  margin: 0 auto 3rem;
  padding: 0 2rem;
}
@media (max-width: 700px) { .main-grid { grid-template-columns: 1fr; } }

/* ── Card ───────────────────────────────────────────────────── */
.card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
}

/* ── Upload Card ────────────────────────────────────────────── */
.upload-zone {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3rem 2rem;
  border: 2px dashed var(--border2);
  border-radius: var(--radius);
  margin: 1rem;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
  min-height: 260px;
}
.upload-zone:hover { border-color: var(--accent); background: rgba(78,204,163,0.04); }
.upload-zone.drag-over { border-color: var(--accent); background: rgba(78,204,163,0.08); }

.upload-icon { color: var(--accent); margin-bottom: 1rem; opacity: 0.8; }
.upload-label { font-size: 0.95rem; color: var(--text); margin-bottom: 4px; }
.upload-sub { font-size: 0.8rem; color: var(--muted); margin-bottom: 1rem; }

#preview {
  width: 100%;
  max-height: 280px;
  object-fit: cover;
  display: block;
}

.upload-actions {
  display: flex;
  gap: 10px;
  padding: 1rem;
  border-top: 1px solid var(--border);
}

/* ── Buttons ────────────────────────────────────────────────── */
.btn-primary {
  flex: 1;
  background: var(--accent);
  color: #0d1a14;
  border: none;
  border-radius: 10px;
  padding: 10px 20px;
  font-family: var(--font-body);
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
}
.btn-primary:hover { background: var(--accent2); }
.btn-primary:active { transform: scale(0.98); }
.btn-primary:disabled { opacity: 0.5; cursor: not-allowed; }

.btn-outline {
  background: none;
  border: 1px solid var(--border2);
  color: var(--text);
  border-radius: 10px;
  padding: 8px 20px;
  font-family: var(--font-body);
  font-size: 0.875rem;
  cursor: pointer;
  transition: border-color 0.2s;
}
.btn-outline:hover { border-color: var(--accent); color: var(--accent); }

.btn-ghost {
  background: none;
  border: none;
  color: var(--muted);
  font-family: var(--font-body);
  font-size: 0.875rem;
  cursor: pointer;
  padding: 10px 12px;
  border-radius: 8px;
  transition: color 0.2s;
}
.btn-ghost:hover { color: var(--danger); }

/* ── Result Card ────────────────────────────────────────────── */
.result-card { padding: 1.5rem; overflow-y: auto; max-height: 520px; }

.result-placeholder {
  height: 100%;
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--muted);
  font-size: 0.875rem;
  border: 2px dashed var(--border);
  border-radius: 10px;
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;
}
.result-label { font-size: 0.72rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px; }
.result-disease { font-family: var(--font-head); font-size: 1.5rem; color: var(--text); line-height: 1.2; }
.result-code { font-size: 0.8rem; color: var(--accent); margin-top: 2px; }

.severity-badge {
  padding: 4px 12px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 500;
  white-space: nowrap;
}
.severity-High   { background: rgba(240,96,96,0.15);  color: var(--danger); }
.severity-Medium { background: rgba(240,176,96,0.15); color: var(--warn); }
.severity-Low    { background: rgba(78,204,163,0.15); color: var(--low); }

.result-desc { font-size: 0.875rem; color: var(--muted); line-height: 1.7; margin-bottom: 0.75rem; }
.result-action {
  font-size: 0.825rem;
  color: var(--text);
  background: var(--bg3);
  border-left: 3px solid var(--accent);
  padding: 8px 12px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 1.25rem;
}

.conf-main {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}
.conf-label { font-size: 0.8rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; }
.conf-value { font-family: var(--font-head); font-size: 1.8rem; color: var(--accent); }

.bars-title { font-size: 0.72rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 0.75rem; }

.bar-row { display: flex; align-items: center; gap: 8px; margin-bottom: 8px; }
.bar-label { font-size: 0.75rem; color: var(--muted); width: 48px; flex-shrink: 0; }
.bar-track { flex: 1; background: var(--bg3); border-radius: 4px; height: 6px; overflow: hidden; }
.bar-fill { height: 100%; background: var(--accent); border-radius: 4px; transition: width 0.6s ease; }
.bar-fill.top { background: var(--accent); }
.bar-fill.rest { background: rgba(78,204,163,0.35); }
.bar-val { font-size: 0.75rem; color: var(--muted); width: 40px; text-align: right; flex-shrink: 0; }

/* ── History ────────────────────────────────────────────────── */
.history-header { padding: 2.5rem 2rem 1.5rem; max-width: 900px; margin: 0 auto; }
.history-header h2 { font-family: var(--font-head); font-size: 1.8rem; color: var(--text); }
.history-header p  { color: var(--muted); font-size: 0.875rem; margin-top: 4px; }

.history-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
  max-width: 900px;
  margin: 0 auto;
  padding: 0 2rem 3rem;
}

.history-card {
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: var(--radius);
  overflow: hidden;
  transition: border-color 0.2s;
}
.history-card:hover { border-color: var(--border2); }
.history-card img { width: 100%; height: 130px; object-fit: cover; display: block; }
.history-card-body { padding: 12px 14px; }
.hc-name { font-size: 0.875rem; font-weight: 500; color: var(--text); margin-bottom: 2px; }
.hc-code { font-size: 0.75rem; color: var(--accent); margin-bottom: 6px; }
.hc-row  { display: flex; justify-content: space-between; align-items: center; }
.hc-conf { font-size: 0.8rem; color: var(--muted); }
.hc-time { font-size: 0.72rem; color: var(--muted); }
.hc-sev  { font-size: 0.7rem; padding: 2px 8px; border-radius: 10px; }

.history-empty { text-align: center; color: var(--muted); padding: 4rem; }

/* ── Loading spinner ────────────────────────────────────────── */
@keyframes spin { to { transform: rotate(360deg); } }
.spinner {
  width: 18px; height: 18px;
  border: 2px solid rgba(0,0,0,0.2);
  border-top-color: #0d1a14;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
  display: inline-block;
  vertical-align: middle;
  margin-right: 6px;
}

/* ── Fade in ────────────────────────────────────────────────── */
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
.fade-in { animation: fadeIn 0.4s ease forwards; }
