import { defineConfig } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  use: {
    headless: true,
    baseURL: 'http://127.0.0.1:8000',
    viewport: { width: 1280, height: 720 },
  },
});
