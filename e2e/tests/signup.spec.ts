import { test, expect } from '@playwright/test';

// NOTE: These tests assume the Django dev server is running at http://127.0.0.1:8000

test('signup flow', async ({ page }) => {
  await page.goto('/accounts/signup/');
  await expect(page.locator('text=Sign up')).toBeVisible();

  // Fill the default Django UserCreationForm fields
  await page.fill('input[name=username]', 'playwright_user');
  await page.fill('input[name=password1]', 'Testpass123!');
  await page.fill('input[name=password2]', 'Testpass123!');
  await page.click('button:has-text("Create account")');

  // After signup, user should be redirected to login
  await expect(page).toHaveURL(/.*accounts\/login.*/);
});
