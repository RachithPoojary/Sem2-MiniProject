# Project Inventory & API Summary

Repository root: `/Users/rachith/Desktop/mp/jobportal`

This document is an automatically generated, structured inventory of the project — useful for generating an IEEE-style SRS. It covers directories, important files, models, routes, data flows and recommended fixes.

---

## Overview

- Backend: Node.js + Express + Mongoose (MongoDB)
- Frontend: React (Vite) + Redux Toolkit
- File storage: Cloudinary (via DataURI uploads)
- Authentication: JWT stored in cookie
- Main backend entry: `backend/index.js`
- Main frontend entry: `frontend/src/main.jsx` / `frontend/src/App.jsx`

Site Name: VJTI Launchpad

---

## Backend — /backend

### `backend/index.js`
- Purpose: Express server bootstrap, middleware registration, route mounting, DB connect.
- Key behavior:
  - Uses `express.json`, `express.urlencoded`, `cookie-parser`, `cors`
  - CORS origin set to `http://localhost:5173`, credentials enabled
  - Registers routes under `/api/v1/user`, `/api/v1/company`, `/api/v1/job`, `/api/v1/application`
  - Calls `connectDB()` on startup

### `backend/utils/db.js`
- Purpose: Connect to MongoDB using `mongoose.connect(process.env.MONGO_URI)`.

### `backend/utils/cloudinary.js`
- Purpose: Configure Cloudinary (`cloudinary.v2`) using environment variables `CLOUD_NAME`, `API_KEY`, `API_SECRET`.

### `backend/utils/datauri.js`
- Purpose: Convert multer file buffer into DataURI for Cloudinary upload.
- Exports: `getDataUri(file)`

### `backend/middlewares/mutler.js`
- Purpose: Multer middleware using memoryStorage; exports `singleUpload` configured with `.single('file')`.
- Note: using memoryStorage keeps file buffers in memory (consider size limits).

### `backend/middlewares/isAuthenticated.js`
- Purpose: JWT verification middleware. Reads JWT from cookie `token`, verifies with `process.env.SECRET_KEY`, sets `req.id = decode.userId`.
- Failure: returns 401 with JSON error.

---

## Backend Models — `backend/models`

### User (`backend/models/user.model.js`)
- Purpose: Persist platform users (students & recruiters) and profile data.
- Fields:
  - `fullname` (String, required)
  - `email` (String, required, unique)
  - `phoneNumber` (Number, required)
  - `password` (String, required) // hashed
  - `role` (String enum: 'student' | 'recruiter')
  - `profile`:
    - `bio` (String)
    - `skills` ([String])
    - `resume` (String) // Cloudinary URL
    - `resumeOriginalName` (String)
    - `company` (ObjectId -> Company)
    - `profilePhoto` (String URL)
  - timestamps

### Company (`backend/models/company.model.js`)
- Purpose: Persist recruiter-created company entities.
- Fields:
  - `name` (String, required, unique)
  - `description`, `website`, `location` (String)
  - `logo` (String URL)
  - `userId` (ObjectId -> User, required)
  - timestamps

### Job (`backend/models/job.model.js`)
- Purpose: Job postings.
- Fields:
  - `title`, `description` (String, required)
  - `requirements` ([String])
  - `salary` (String, required)
  - `experienceLevel` (String required)
  - `location` (String required)
  - `jobType` (String required)
  - `position` (Number required)
  - `company` (ObjectId -> Company, required)
  - `created_by` (ObjectId -> User, required)
  - `applications` ([ObjectId -> Application])
  - timestamps

### Application (`backend/models/application.model.js`)
- Purpose: Job application records.
- Fields:
  - `job` (ObjectId -> Job, required)
  - `applicant` (ObjectId -> User, required)
  - `status` (String enum: 'pending' | 'accepted' | 'rejected', default 'pending')
  - timestamps

Relationships (summary):
- User (recruiter) 1..* -> Company
- Company 1..* -> Job
- Job 1..* -> Application
- User (student) 1..* -> Application

---

## Backend Controllers (behavior summary)

### `backend/controllers/user.controller.js`
- Functions:
  - `register(req, res)`
    - Validates fields, optionally uploads profile photo (`req.file`) via DataURI -> Cloudinary
    - Hashes password with `bcrypt.hash(..., 10)`
    - Creates User document
  - `login(req, res)`
    - Validates credentials, compares password using `bcrypt.compare`
    - Checks role matches
    - Generates JWT `jwt.sign({ userId }, SECRET_KEY, { expiresIn:'1d' })`
    - Sets cookie `token` with options (note: uses `httpsOnly: true` which is a typo; should be `httpOnly: true`)
    - Returns user (sans password)
  - `logout(req, res)`
    - Clears cookie by setting `token` to empty and `maxAge: 0`
  - `updateProfile(req, res)`
    - Authenticated route; can accept resume upload (uses `resource_type: "raw"` for Cloudinary)
    - Accepts `fullname`, `email`, `phoneNumber`, `bio`, `skills` (CSV -> array)
    - Updates `user.profile.resume` and `resumeOriginalName` when file uploaded

Notes: fix cookie option typo; add validation & consistent error responses.

### `backend/controllers/company.controller.js`
- Functions:
  - `registerCompany(req, res)` — create company associated with `req.id`
  - `getCompany(req, res)` — get companies for logged-in user
  - `getCompanyById(req, res)` — get company by id
  - `updateCompany(req, res)` — updates company fields and logo (uploads `req.file` to Cloudinary)

Notes: updateCompany does not verify ownership explicitly — add owner check.

### `backend/controllers/job.controller.js`
- Functions:
  - `postJob(req, res)` — create job (requirements split by comma)
  - `getAllJobs(req, res)` — optional `?keyword=` search on title/description; populates `company`
  - `getJobById(req, res)` — returns job and populates `applications`
  - `getAdminJobs(req, res)` — returns jobs created by `req.id` and populates `company`

### `backend/controllers/application.controller.js`
- Functions:
  - `applyJob(req, res)` — creates an Application and pushes its id into Job.applications
    - NOTE: route implemented as GET (should be POST)
  - `getAppliedJobs(req, res)` — returns applications for `req.id`, populates job -> company
  - `getApplicants(req, res)` — returns job populated with `applications` and each application populated with `applicant`
  - `updateStatus(req, res)` — updates Application.status

---

## Backend Routes (registered under `/api/v1` in `backend/index.js`)

### User routes (`backend/routes/user.route.js`)
- POST `/api/v1/user/register` — register (singleUpload middleware)
- POST `/api/v1/user/login` — login
- GET `/api/v1/user/logout` — logout
- POST `/api/v1/user/profile/update` — updateProfile (protected: isAuthenticated, singleUpload)

### Company routes (`backend/routes/company.route.js`)
- POST `/api/v1/company/register` — registerCompany (protected)
- GET `/api/v1/company/get` — getCompany (protected)
- GET `/api/v1/company/get/:id` — getCompanyById (protected)
- PUT `/api/v1/company/update/:id` — updateCompany (protected, singleUpload)

### Job routes (`backend/routes/job.route.js`)
- POST `/api/v1/job/post` — postJob (protected)
- GET `/api/v1/job/get` — getAllJobs (protected) with optional `?keyword=`
- GET `/api/v1/job/getadminjobs` — getAdminJobs (protected)
- GET `/api/v1/job/get/:id` — getJobById (protected)

### Application routes (`backend/routes/application.route.js`)
- GET `/api/v1/application/apply/:id` — applyJob (protected) — (should be POST)
- GET `/api/v1/application/get` — getAppliedJobs (protected)
- GET `/api/v1/application/:id/applicants` — getApplicants (protected)
- POST `/api/v1/application/status/:id/update` — updateStatus (protected)

---

## Frontend — `frontend/src`

### API endpoint constants: `frontend/src/utils/constant.js`
- `USER_API_END_POINT = "http://localhost:8000/api/v1/user"`
- `JOB_API_END_POINT = "http://localhost:8000/api/v1/job"`
- `APPLICATION_API_END_POINT = "http://localhost:8000/api/v1/application"`
- `COMPANY_API_END_POINT = "http://localhost:8000/api/v1/company"`

Note: backend default PORT in `backend/index.js` is 3000 if `PORT` not provided; frontend constant uses port 8000 — ensure deployment/pipeline or proxy configuration keeps them consistent.

### Redux store & slices (state used by UI)
- `frontend/src/redux/authSlice.js` — { loading, user }
- `frontend/src/redux/jobSlice.js` — { allJobs, allAdminJobs, singleJob, allAppliedJobs, ... }
- `frontend/src/redux/companySlice.js` — { companies, singleCompany }
- `frontend/src/redux/applicationSlice.js` — { applicants }
- `frontend/src/redux/store.js` — configures redux-persist (localStorage)

### Hooks (data fetching)
- `useGetAllJobs`, `useGetAllAdminJobs`, `useGetAppliedJobs`, `useGetCompanyById`, `useGetAllCompanies`
- All use `axios.get(..., { withCredentials: true })` so they rely on cookie auth being set by backend.

### Key components that call backend
- `frontend/src/components/auth/Login.jsx` — POST login; dispatch setUser
- `frontend/src/components/auth/Signup.jsx` — POST register (FormData) including file upload
- `frontend/src/components/admin/PostJob.jsx` — POST create job
- `frontend/src/components/JobDescription.jsx` — GET job details; GET apply (non-RESTful)
- `frontend/src/components/Profile.jsx` — shows user info and resume link; uses `useGetAppliedJobs`
- `frontend/src/components/admin/Applicants.jsx` — GET applicants for job

---

## Data Flow Examples (high level)

1. Registration (student/recruiter):
   - Frontend: sends multipart/form-data to POST `/api/v1/user/register` (field `file` optional)
   - Backend: `multer` memoryStorage reads file -> `getDataUri(file)` -> `cloudinary.uploader.upload` -> store secure_url -> create User -> respond

2. Login:
   - Frontend POST `/api/v1/user/login` with credentials
   - Backend verifies password -> signs JWT -> sets cookie `token` -> returns user object
   - Frontend persists user in Redux and uses `withCredentials` on subsequent requests

3. Post Job (recruiter):
   - Frontend POST `/api/v1/job/post` with JSON body; backend `postJob` validates fields, splits `requirements`, sets `created_by = req.id`, stores Job

4. Apply Job (student):
   - Frontend triggers GET `/api/v1/application/apply/:jobId` (note: should be POST)
   - Backend checks existing application -> creates Application -> pushes id to Job.applications -> returns success

---

## Noted Issues & Recommended Fixes (for SRS / Technical Debt)

- Cookie option typo in `login()` (`httpsOnly: true`) — should be `httpOnly: true`. Also set `secure: true` in production.
- `applyJob` exposed as GET route (`/application/apply/:id`) while it modifies state — change to POST.
- Ownership checks missing on `updateCompany` (ensure `req.id === company.userId` before allowing update).
- No explicit file type/size validation on uploads — add middleware checks.
- Inconsistent port between backend default (3000) and frontend constants (8000) — clarify and align.
- Error handling inconsistency: some controllers do not return an error response in catch blocks; introduce centralized error middleware and consistent status codes.
- Multer memory storage may blow server memory on large uploads — consider file size limits or disk storage/temp streams.

---

## Suggested SRS Artifacts you can derive directly from this inventory
- API table (endpoint, method, auth, request schema, response schema, errors)
- ER Diagram (User, Company, Job, Application) — use the Models section
- Sequence diagrams for Register, Login, Post Job, Apply Job, Update Profile
- Data Flow Diagrams highlighting Cloudinary upload and token cookie flow

---

## File List (important files)

- backend/
  - index.js
  - package.json
  - controllers/
    - user.controller.js
    - company.controller.js
    - job.controller.js
    - application.controller.js
  - routes/
    - user.route.js
    - company.route.js
    - job.route.js
    - application.route.js
  - models/
    - user.model.js
    - company.model.js
    - job.model.js
    - application.model.js
  - middlewares/
    - isAuthenticated.js
    - mutler.js
  - utils/
    - cloudinary.js
    - datauri.js
    - db.js

- frontend/
  - src/
    - main.jsx
    - App.jsx
    - utils/constant.js
    - redux/
      - authSlice.js
      - jobSlice.js
      - companySlice.js
      - applicationSlice.js
      - store.js
    - hooks/
      - useGetAllJobs.jsx
      - useGetAllAdminJobs.jsx
      - useGetAppliedJobs.jsx
      - useGetCompanyById.jsx
      - useGetAllCompanies.jsx
    - components/
      - auth/Login.jsx
      - auth/Signup.jsx
      - admin/PostJob.jsx
      - JobDescription.jsx
      - Profile.jsx
      - admin/Applicants.jsx
    - components/ui/* (input, button, badge, table, etc.)

---

## Next steps I can take (pick one or more)
- Generate a fully-documented API table in Markdown with request/response examples for every endpoint.
- Produce PlantUML sources for ER, sequence, component diagrams (I can also try to render them if network allowed or provide instructions to render locally).
- Implement small bug fixes: change apply route to POST and fix cookie option typo; add owner check on company update and add a basic validation for file size.
- Create a `docs/api.md` or extend this markdown into a full SRS-ready section.

---

Generated: 26 May 2026

File saved at: `/Users/rachith/Desktop/mp/jobportal/srs_report/project_inventory.md`

If you want, I can now generate the API table in this same file or create separate files (e.g., `srs_report/api_endpoints.md`, `srs_report/er_diagram.puml`). Which would you like next?