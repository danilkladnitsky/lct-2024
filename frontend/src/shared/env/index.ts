const { VITE_SHA } = import.meta.env;
export const APP_VERSION = VITE_SHA ? `commit #${VITE_SHA}` : 'local';
export const APP_VERSION_LINK = VITE_SHA ? `https://github.com/danilkladnitsky/lct-2024/commit/${VITE_SHA}` : 'https://github.com/danilkladnitsky/lct-2024';
export const API_HOST = `https://api-lct-2024.kladnitsky.ru`;