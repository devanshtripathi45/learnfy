import { test, expect } from '@playwright/test';

test('home page loads', async ({ page }) => {
  await page.goto('/');
  await expect(page).toHaveTitle(/Learnify/);
  await expect(page.locator('text=Latest Courses')).toBeVisible();
});
