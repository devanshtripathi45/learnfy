E2E tests (Playwright)

This project includes a Playwright E2E test scaffold under `e2e/`.

Setup (requires Node.js):

1. Install dependencies:

   npm install

2. Install browsers (Playwright):

   npx playwright install

3. Run the Django dev server in another terminal:

   python manage.py runserver

4. Run the tests:

   npm run test:e2e

Notes:
- Tests expect the dev server at http://127.0.0.1:8000
- Playwright is only a scaffold here; install Node and run the above commands to execute tests locally.
 
Test user setup:
- You can run the `signup` test first which creates `playwright_user` or create a user manually:

   python manage.py createsuperuser --username playwright_user --email you@example.com

   (Then set the password to `Testpass123!` for the test run.)
