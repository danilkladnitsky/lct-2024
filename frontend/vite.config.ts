import react from '@vitejs/plugin-react-swc';
import path from 'path';
import sass from 'sass';
import { defineConfig } from 'vite';

export default defineConfig({
  plugins: [react()],
  define: {
    VITE_API_HOST: `'${process.env.VITE_API_HOST}'`,
    VITE_SHA: `'${process.env.VITE_SHA}'`,
  },
  build: {
    assetsDir: 'public',
  },
  css: {
    preprocessorOptions: {
      scss: {
        implementation: sass,
      },
    },
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@/common': path.resolve(__dirname, './src/common'),
    },
  },
});
