import React, { useState } from 'react';

interface BaselineComparisonProps {
  currentVeyraProbability?: number | null;
  currentSpreadValue?: number | null;
  variable?: string;
  leadHours?: number;
}

const MiniGauge: React.FC<{ value: number, label: string }> = ({ value, label }) => {
  const radius = 20;
  const circumference = 2 * Math.PI * radius;
  const percent = Math.min(Math.max(value, 0), 100) / 100;
  const strokeDashoffset = circumference - percent * circumference;

  return (
    <div style={{ display: 'flex', alignItems: 'center', gap: '10px' }}>
      <div style={{ position: 'relative', width: '48px', height: '48px' }}>
        <svg width="48" height="48" viewBox="0 0 48 48" style={{ transform: 'rotate(-90deg)' }}>
          <circle cx="24" cy="24" r={radius} stroke="rgba(255,255,255,0.15)" strokeWidth="4" fill="none" />
          <circle 
            cx="24" cy="24" r={radius} 
            stroke="#4ade80" 
            strokeWidth="4" 
            fill="none"
            strokeDasharray={circumference}
            strokeDashoffset={strokeDashoffset}
            strokeLinecap="round"
            style={{ transition: 'stroke-dashoffset 1.5s cubic-bezier(0.4, 0, 0.2, 1)', filter: 'drop-shadow(0 0 6px rgba(74, 222, 128, 0.6))' }}
          />
        </svg>
        <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', fontSize: '0.65rem', fontWeight: 800, color: '#fff' }}>
          +{value}%
        </div>
      </div>
      <div style={{ fontWeight: 800, fontSize: '0.85rem', color: '#fff' }}>{label}</div>
    </div>
  );
};

export const BaselineToggle: React.FC<BaselineComparisonProps> = ({
  currentVeyraProbability = 0.58,
  currentSpreadValue = 4.8,
  variable: _variable = 'temperature_2m',
  leadHours: _leadHours = 48,
}) => {
  const [activeModel, setActiveModel] = useState<'veyra' | 'spread'>('veyra');

  const veyraProbPct =
    currentVeyraProbability != null ? (currentVeyraProbability * 100).toFixed(1) : '58.0';

  return (
    <div
      className="glass-card"
      style={{
        padding: '16px 20px',
        display: 'flex',
        flexDirection: 'column',
        gap: '14px',
      }}
    >
      {/* Header with Segmented Switch */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '10px' }}>
        <div>
          <h4 style={{ fontSize: '0.95rem', fontWeight: 700, color: 'var(--noaa-white)' }}>
            Model vs. Ensemble Spread Baseline (§17, §20, File 090)
          </h4>
          <p style={{ fontSize: '0.78rem', color: 'var(--noaa-muted)', marginTop: '2px' }}>
            Compare Veyra multi-feature calibrated model against the standard ensemble spread-only benchmark.
          </p>
        </div>

        {/* Toggle Switch */}
        <div
          style={{
            display: 'flex',
            background: 'var(--noaa-gray-bg)',
            borderRadius: '6px',
            padding: '3px',
            border: '1px solid var(--noaa-border-subtle)',
          }}
        >
          <button
            onClick={() => setActiveModel('veyra')}
            style={{
              padding: '6px 14px',
              borderRadius: '4px',
              fontSize: '0.78rem',
              fontWeight: 700,
              border: 'none',
              cursor: 'pointer',
              background: activeModel === 'veyra' ? 'var(--noaa-accent)' : 'transparent',
              color: activeModel === 'veyra' ? '#ffffff' : 'var(--noaa-muted)',
              transition: 'all 0.15s ease',
            }}
          >
            Veyra Sentinel (Full)
          </button>
          <button
            onClick={() => setActiveModel('spread')}
            style={{
              padding: '6px 14px',
              borderRadius: '4px',
              fontSize: '0.78rem',
              fontWeight: 700,
              border: 'none',
              cursor: 'pointer',
              background: activeModel === 'spread' ? 'var(--noaa-accent)' : 'transparent',
              color: activeModel === 'spread' ? '#ffffff' : 'var(--noaa-muted)',
              transition: 'all 0.15s ease',
            }}
          >
            Spread-Only Baseline
          </button>
        </div>
      </div>

      {/* Direct Side-by-Side Comparison Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '12px' }}>
        {/* Model Card */}
        <div
          style={{
            padding: '12px 14px',
            borderRadius: '6px',
            border: activeModel === 'veyra' ? '2px solid var(--noaa-accent)' : '1px solid var(--noaa-border-subtle)',
            background: activeModel === 'veyra' ? 'var(--noaa-light-blue)' : 'var(--noaa-card-bg)',
          }}
        >
          <div style={{ fontSize: '0.72rem', fontWeight: 800, color: 'var(--noaa-accent)', textTransform: 'uppercase' }}>
            Veyra V3 LightGBM + Conformal
          </div>
          <div style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--noaa-white)', marginTop: '4px' }}>
            {veyraProbPct}% <span style={{ fontSize: '0.75rem', fontWeight: 600 }}>P(Bust)</span>
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--noaa-muted)', marginTop: '4px' }}>
            Median Alert Lead Time: <strong>48h</strong>
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--noaa-muted)' }}>
            PR-AUC Benchmark: <strong>0.2124</strong> (AP: 0.2047)
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--noaa-muted)' }}>
            Brier Score: <strong>0.0538</strong> (Calibrated)
          </div>
        </div>

        {/* Baseline Card */}
        <div
          style={{
            padding: '12px 14px',
            borderRadius: '6px',
            border: activeModel === 'spread' ? '2px solid var(--noaa-accent)' : '1px solid var(--noaa-border-subtle)',
            background: activeModel === 'spread' ? 'var(--noaa-light-blue)' : 'var(--noaa-card-bg)',
          }}
        >
          <div style={{ fontSize: '0.72rem', fontWeight: 800, color: 'var(--noaa-muted)', textTransform: 'uppercase' }}>
            Ensemble Spread-Only (E1 Baseline)
          </div>
          <div style={{ fontSize: '1.4rem', fontWeight: 800, color: 'var(--noaa-white)', marginTop: '4px' }}>
            ±{currentSpreadValue ?? 4.8} <span style={{ fontSize: '0.75rem', fontWeight: 600 }}>Spread</span>
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--noaa-muted)', marginTop: '4px' }}>
            Median Alert Lead Time: <strong>24h</strong>
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--noaa-muted)' }}>
            PR-AUC Benchmark: <strong>0.0820</strong> (Uncalibrated)
          </div>
          <div style={{ fontSize: '0.75rem', color: 'var(--noaa-muted)' }}>
            Brier Score: <strong>0.0715</strong> (+32.9% Error)
          </div>
        </div>
      </div>

      {/* Advantage Banner */}
      <div
        style={{
          padding: '8px 12px',
          background: 'rgba(34, 197, 94, 0.15)',
          borderLeft: '3px solid #4ade80',
          borderRadius: '0 4px 4px 0',
          fontSize: '0.78rem',
          color: '#86efac',
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          flexWrap: 'wrap',
          gap: '6px',
        }}
      >
        <span>
          <strong style={{ color: '#fff' }}>Early Warning Advantage:</strong> Veyra provides <strong style={{ color: '#fff' }}>+24.0h warning lead-time gain</strong> over spread-only,
          detecting 74.2% of busts at 48h lead vs 38.4% for the spread baseline.
        </span>
        <MiniGauge value={35.8} label="Lead Gain" />
      </div>
    </div>
  );
};

export default BaselineToggle;
