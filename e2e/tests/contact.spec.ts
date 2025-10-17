import { test, expect } from '@playwright/test';

test('contact form can be submitted', async ({ page }) => {
  await page.goto('/contact/');
  await expect(page.locator('text=Contact Us')).toBeVisible();

  await page.fill('input[name=name]', 'E2E Tester');
  await page.fill('input[name=email]', 'e2e@example.com');
  await page.fill('textarea[name=message]', 'Hello from Playwright');
  await page.click('button:has-text("Send Message")');

  await expect(page.locator('text=Thank you — your message has been sent.')).toBeVisible();
});
