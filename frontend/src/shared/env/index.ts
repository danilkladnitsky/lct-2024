const { VITE_SHA, DEV } = import.meta.env;
export const APP_VERSION = VITE_SHA ? `commit #${VITE_SHA}` : "local";
export const APP_VERSION_LINK = VITE_SHA
  ? `https://github.com/danilkladnitsky/lct-2024/commit/${VITE_SHA}`
  : "https://github.com/danilkladnitsky/lct-2024";
export const API_HOST = DEV
  ? `http://localhost:3000`
  : `https://api-lct-2024.kladnitsky.ru`;

export const MAPBOX_TOKEN = `pk.eyJ1IjoiZGFuaWxrbGFkbml0c2t5IiwiYSI6ImNseGg1eTVxOTFidXAycXF6cjJsaHUzMzMifQ.IPzQ5vI0502wjpz0hmAvTQ`;
