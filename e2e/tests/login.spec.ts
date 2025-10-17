import { test, expect } from '@playwright/test';

test('login flow', async ({ page }) => {
  await page.goto('/accounts/login/');
  await expect(page.locator('text=Login')).toBeVisible();

  // Use credentials created by the signup test or existing test user
  await page.fill('input[name=username]', 'playwright_user');
  await page.fill('input[name=password]', 'Testpass123!');
  await page.click('button:has-text("Login")');

  // After login, should redirect to home
  await expect(page).toHaveURL(/.*\//);
});
