# Software Requirements Specification (SRS)

**Project:** VJTI Launchpad / Job Hunt Platform

**Version:** 1.0

**Date:** 26 May 2026

---

## 1. Cover Page

VJTI Launchpad — Software Requirements Specification (SRS)

Version: 1.0

Date: 26 May 2026

Prepared for: Academic Submission / Final Year Project

Prepared by: [Student / Team Name]

Supervisor: [Supervisor Name]

Contact: [email@example.com]

Repository path: /Users/rachith/Desktop/mp/jobportal

---

## 2. Certificate

This is to certify that the work presented in this Software Requirements Specification (SRS) document titled "Job Portal — Software Requirements Specification" is the original work of the authors and has been carried out under the guidance of the faculty supervisor. The document is submitted in partial fulfillment of the requirements for the degree of [Degree Name] at [Institution Name].

Signatures:

_________________________  Date: ______________

(Author / Student)

_________________________  Date: ______________

(Supervisor)

---

## 3. Declaration

I hereby declare that the work presented in this SRS document is my own and has not been submitted earlier for any degree or diploma to any university or other institution. All sources of information and references used have been duly cited.

Name: [Student Name]

Signature: ___________________

Date: 26 May 2026

---

## 4. Acknowledgement

We gratefully acknowledge the guidance, support, and constructive feedback of our project supervisor and faculty members who helped refine the objectives and scope of this project. We also acknowledge the open-source projects and libraries used in this work. Thanks to peers and testers who provided valuable insights during early verification and validation of the prototype.

---

## 5. Abstract

This Software Requirements Specification (SRS) documents the functional and non-functional requirements for the Job Portal / Job Hunt Platform. The platform connects students/job-seekers with recruiters/employers, enabling user account management, company registration and editing, job posting and search, application creation and review, and status tracking. The SRS follows IEEE conventions and provides comprehensive system descriptions, features, database and API design, security and validation requirements, testing strategies, risk analysis, future enhancements, and textual descriptions of diagrams required for formal documentation.

---

## 6. Table of Contents

1. Cover Page
2. Certificate
3. Declaration
4. Acknowledgement
5. Abstract
6. Table of Contents
7. List of Figures (textual)
8. List of Tables
9. Introduction
  9.1 Purpose of this Document
  9.2 Intended Audience
  9.3 Document Conventions
10. Purpose
11. Scope
12. Definitions, Acronyms & Abbreviations
13. References
14. Overall Description
  14.1 Product Perspective
  14.2 Product Functions
  14.3 User Classes and Characteristics
  14.4 Operating Environment
  14.5 Design Constraints
  14.6 Assumptions and Dependencies
15. Product Features
16. Functional Requirements
17. Non-Functional Requirements
18. External Interface Requirements
19. System Features
  19.1 Authentication Module
  19.2 Job Management Module
  19.3 Company Management Module
  19.4 Application Management Module
  19.5 Recruiter Dashboard Module
  19.6 Student/User Module
20. Database Design
21. API Design
22. Security Requirements
23. Performance Requirements
24. Software Quality Attributes
25. Error Handling
26. Validation Rules
27. Testing Strategies
28. Test Cases
29. Risk Analysis
30. Feasibility Study
31. Future Enhancements
32. Conclusion
33. Appendix
34. Bibliography
35. References
36. Screenshots placeholders (textual)
37. Diagram textual descriptions
38. Tables

---

## 7. List of Figures (textual)

Note: This SRS version intentionally contains no images. The following is a list of diagrams that are described in textual form later in this document. The diagram descriptions are sufficient to recreate visual diagrams for submission.

- Figure 1: System Architecture — textual description
- Figure 2: Entity-Relationship (ER) Diagram — textual description
- Figure 3: Use Case Diagram — textual description
- Figure 4: Data Flow Diagram (DFD) Level 0 — textual description
- Figure 5: Data Flow Diagram (DFD) Level 1 — textual description
- Figure 6: Activity Diagram — textual description
- Figure 7: Sequence Diagram — textual description
- Figure 8: Component Diagram — textual description
- Figure 9: Deployment Diagram — textual description

---

## 8. List of Tables

- Table 1: Functional Requirements (Identifiers and details)
- Table 2: Non-functional Requirements
- Table 3: User Roles and Permissions
- Table 4: Database Tables and Attributes
- Table 5: API Summary
- Table 6: Test Cases
- Table 7: Hardware Requirements
- Table 8: Software Requirements
- Table 9: Risk Analysis
- Table 10: Validation Rules

---

## 9. Introduction

### 9.1 Purpose of this Document

This Software Requirements Specification (SRS) documents the requirements for the Job Portal web application. It defines the functional and non-functional requirements, system architecture expectations, database schema, API endpoints, validation rules, security expectations, test cases and risk considerations. The document serves as the contract between stakeholders (students, recruiters, supervisors) and the development team.

### 9.2 Intended Audience

- Project Supervisor and Evaluation Committee
- Developers and DevOps Engineers
- Testers and QA Engineers
- Future maintainers and extension teams

### 9.3 Document Conventions

- IEEE-style numbered headings.
- Terminology: “user” is generic; “student” and “recruiter” denote role-specific users.
- Endpoints are in the form /api/v1/... and refer to HTTP methods (GET/POST/PUT).
- Where codebase specifics were absent, reasonable assumptions were documented.

---

## 10. Purpose

The Job Portal provides an online platform for job discovery and application management. Its objectives include:

- Allowing students to register, build profiles, upload resumes and apply to posted jobs.
- Enabling recruiters to register companies, post job listings, review applicant lists and update application statuses.
- Providing secure authentication and role-specific access control.
- Offering a searchable and user-friendly interface for job discovery and administrative workflows.

---

## 11. Scope

**In scope:**

- Web-based front-end (React + Vite) and REST API back-end (Node.js + Express).
- Authentication via JWT and cookie-based storage.
- Core modules: user auth/profile, company management, job posting and search, application management.
- File uploads handled with multer → DataURI → Cloudinary.

**Out of scope (not implemented in current codebase):**

- Email verification & password reset flows.
- Payment or premium features.
- Advanced analytics beyond basic listings and counts.
- Native mobile application (although responsive web is supported).

---

## 12. Definitions, Acronyms & Abbreviations

**Definitions:**
- Applicant: Student applying for a job.
- Recruiter: Employer or recruiter posting jobs.
- Application: Documented instance of a candidate applying to a job.

**Acronyms:**
- SRS — Software Requirements Specification
- API — Application Programming Interface
- SPA — Single Page Application
- DB — Database
- JWT — JSON Web Token
- UI — User Interface
- UX — User Experience

---

## 13. References

- IEEE Std 830-1998 — Recommended Practice for Software Requirements Specifications.
- ReactJS documentation — https://reactjs.org
- Express documentation — https://expressjs.com
- Mongoose documentation — https://mongoosejs.com
- Cloudinary docs — https://cloudinary.com/documentation
- JWT specification — https://jwt.io/introduction

---

## 14. Overall Description

### 14.1 Product Perspective

The Job Portal is a standalone web application featuring a decoupled front-end SPA and a RESTful back-end. It integrates with Cloudinary for file storage and requires a MongoDB instance. The front-end communicates with the back-end over HTTP(S) and authenticates users using JWT stored in cookies.

### 14.2 Product Functions (high level)

- User management: registration, login, logout, profile update.
- Recruiter-specific: company registration/editing, job posting, applicant review.
- Candidate-specific: search jobs, apply for jobs, view applied jobs/status.
- File handling: profile image upload and resume upload to Cloudinary.
- Search: server-side keyword search with client-side filtering.

### 14.3 User Classes and Characteristics

- Student: basic user, less technical; primary goal is to find jobs and apply.
- Recruiter: business user; manages companies and job postings; reviews applicants.
- System Administrator (implicit): responsible for deployment and infrastructure (not a distinct in-app role).

### 14.4 Operating Environment

- Front-end: Modern browsers (Chrome, Firefox, Safari, Edge).
- Back-end: Node.js runtime, Express web server.
- Database: MongoDB accessible via connection string (MONGO_URI).
- External services: Cloudinary (CLOUD_NAME, API_KEY, API_SECRET).
- Development: Vite for frontend; nodemon for backend development.

### 14.5 Design Constraints

- Use of REST API endpoints with existing route patterns (/api/v1/...).
- Files are handled using multer memory storage in current implementation—this affects memory usage on the server.
- JWT tokens stored in cookies; cookie options must be set appropriately for security.

### 14.6 Assumptions and Dependencies

- Cloudinary account exists and credentials are provided via environment variables.
- Production will use HTTPS and environment variables set securely.
- Users provide valid resumes and images; file-type & size validation should be enforced.

---

## 15. Product Features

### 15.1 Authentication & Authorization

- Account creation (student/recruiter), login and logout.
- JWT-based authentication with token stored in cookie.
- Role checks: recruiter or student determines accessible UI and API behaviours.

### 15.2 Company Management

- Company registration by recruiters; company details (name, description, website, location, logo) management.

### 15.3 Job Management

- Recruiter creates job posts that include structured fields; job listings are searchable and paginated.

### 15.4 Application Management

- Students can apply to jobs; recruiters can see applicants and change application statuses (pending, accepted, rejected).

### 15.5 Profile Management

- Students and recruiters can update profile fields and upload profile picture/resume.

### 15.6 Search & Filtering

- Server-side keyword search on title & description; client-side filters (location, jobType) in the UI.

---

## 16. Functional Requirements

**Table 1 — Functional Requirements (detailed)**

| ID    | Title                        | Description / Acceptance Criteria |
|-------|------------------------------|-----------------------------------|
| FR-1  | User Registration            | User signs up with required fields; password hashed; user stored; duplicate emails rejected. |
| FR-2  | User Login                   | Authentication with email+password+role; cookie token set; user returned. |
| FR-3  | User Logout                  | Cookie cleared and user logged out. |
| FR-4  | Update Profile               | Authenticated user can update profile info; resume uploaded to Cloudinary; resume original name saved. |
| FR-5  | Company Registration         | Recruiter can register a company with unique name; company associated with recruiter. |
| FR-6  | Get Companies                | Recruiter retrieves companies they created. |
| FR-7  | Update Company               | Recruiter updates company info and uploads logo; only owner allowed to update. |
| FR-8  | Post Job                     | Recruiter posts job with required fields; job persisted; requirements stored as array. |
| FR-9  | Get All Jobs / Search        | Jobs returned based on optional keyword; jobs populated with company. |
| FR-10 | Get Job By ID                | Return job with applications populated. |
| FR-11 | Get Admin Jobs               | Return jobs where created_by == recruiter id. |
| FR-12 | Apply Job                    | Student applies to job; duplicate applications prevented; application created and job.applications updated. |
| FR-13 | Get Applied Jobs             | Student retrieves their applications with job and company details. |
| FR-14 | Get Applicants               | Recruiter retrieves applicants for a job with applicant details populated. |
| FR-15 | Update Application Status    | Recruiter updates application status (pending/accepted/rejected). |
| FR-16 | File Upload Handling         | Files uploaded via multer -> DataURI -> Cloudinary; secure URLs stored in DB. |

Each FR is mapped to controllers and routes in the codebase and must be covered by unit/integration tests.

---

## 17. Non-Functional Requirements

**Table 2 — Non-functional Requirements**

| ID  | Category       | Requirement                                                                 | Metric / Acceptance Criteria |
|-----|----------------|-----------------------------------------------------------------------------|------------------------------|
| NFR1| Performance    | Average GET response < 300 ms under low load                               | Median response < 300 ms     |
| NFR2| Scalability    | Support horizontal scaling; stateless servers; use Cloudinary for assets   | Stateless API; DB scalable   |
| NFR3| Security       | Passwords hashed; cookies httpOnly & secure in production; JWT expiry 24h   | Security controls enforced   |
| NFR4| Reliability    | 99.5% uptime target for production                                          | Monitoring & redundancy     |
| NFR5| Maintainability| Clear MVC separation; modular controllers; documented APIs                 | Documentation included       |
| NFR6| Usability      | Primary flows complete in <= 3 clicks                                       | Usability testing            |
| NFR7| Portability    | Deployable on Node.js-supported hosts; DB as MongoDB                       | Cross-platform               |

---

## 18. External Interface Requirements

### 18.1 User Interfaces

- Front-end SPA pages: Home, Jobs, Job Description, Login, Signup, Profile, Admin pages. Forms use standard HTML controls; UI components include dialogs, tables and selects.

### 18.2 Hardware Interfaces

- No direct hardware interaction; standard server hardware required.

### 18.3 Software Interfaces

- REST API endpoints (see Section 21).
- Cloudinary SDK integration for file uploads.

### 18.4 Communication Interfaces

- HTTP/HTTPS for all client-server communication.
- CORS configured to allow development origin http://localhost:5173 (production origin to be set accordingly).

---

## 19. System Features

### 19.1 Authentication Module

- JWT creation at login, verification middleware, set cookie with secure attributes in production. Password hashing via bcrypt.

### 19.2 Job Management Module

- Job creation with data validation, storage with reference to company; search via $regex on title/description; populate company data in responses.

### 19.3 Company Management Module

- Company creation and updates, with logo upload to Cloudinary and association of company with recruiter.

### 19.4 Application Management Module

- Create Application documents; prevent duplicates; recruiter view applicants and update statuses.

### 19.5 Recruiter Dashboard Module

- Aggregate recruiter-specific views: companies, posted jobs, applicants and relevant operations.

### 19.6 Student/User Module

- Profile editing, resume upload, view applied jobs.

---

## 20. Database Design

### 20.1 Collections and Attributes (detailed)

**Users Collection**
- _id: ObjectId (PK)
- fullname: String (required)
- email: String (required, unique)
- phoneNumber: Number (required)
- password: String (hashed)
- role: String (enum: 'student','recruiter')
- profile: Object { bio, skills: [String], resume: String (URL), resumeOriginalName: String, company: ObjectId (ref), profilePhoto: String }
- timestamps: createdAt, updatedAt

**Companies Collection**
- _id: ObjectId (PK)
- name: String (required, unique)
- description: String
- website: String
- location: String
- logo: String (Cloudinary URL)
- userId: ObjectId (ref User)
- timestamps

**Jobs Collection**
- _id: ObjectId (PK)
- title: String (required)
- description: String (required)
- requirements: [String]
- salary: String (required)
- experienceLevel: String (required)
- location: String (required)
- jobType: String (required)
- position: Number (required)
- company: ObjectId (ref Company)
- created_by: ObjectId (ref User)
- applications: [ObjectId] (ref Application)
- timestamps

**Applications Collection**
- _id: ObjectId (PK)
- job: ObjectId (ref Job)
- applicant: ObjectId (ref User)
- status: String (enum: ['pending','accepted','rejected'], default 'pending')
- timestamps

### 20.2 Relationships

- One User (recruiter) → many Companies (via Company.userId).
- One Company → many Jobs (via Job.company).
- One Job → many Applications (via Application.job and Job.applications array).
- One User (student) → many Applications (via Application.applicant).

---

## 21. API Design

### 21.1 Endpoint Summary (Table 5)

| Endpoint                                  | Method | Auth | Purpose / Body Summary |
|-------------------------------------------|--------|------|------------------------|
| /api/v1/user/register                     | POST   | No   | multipart/form-data: fullname, email, phoneNumber, password, role, file (profile photo optional) |
| /api/v1/user/login                        | POST   | No   | JSON: { email, password, role } |
| /api/v1/user/logout                       | GET    | No   | Clear cookie |
| /api/v1/user/profile/update               | POST   | Yes  | multipart/form-data: profile fields, resume file (optional) |
| /api/v1/company/register                  | POST   | Yes  | JSON: { companyName } |
| /api/v1/company/get                       | GET    | Yes  | Get companies created by authenticated user |
| /api/v1/company/get/:id                   | GET    | Yes  | Get company by id |
| /api/v1/company/update/:id                | PUT    | Yes  | multipart/form-data: name, description, website, location, file (logo) |
| /api/v1/job/post                          | POST   | Yes  | JSON: job fields (title, description, requirements, salary, location, jobType, experience, position, companyId) |
| /api/v1/job/get                           | GET    | Yes  | Optional ?keyword= |
| /api/v1/job/getadminjobs                  | GET    | Yes  | Get jobs created by authenticated recruiter |
| /api/v1/job/get/:id                       | GET    | Yes  | Get job details with applications |
| /api/v1/application/apply/:id             | POST*  | Yes  | Apply to job (must be POST instead of GET for side-effects) |
| /api/v1/application/get                   | GET    | Yes  | Get applied jobs for authenticated user |
| /api/v1/application/:id/applicants        | GET    | Yes  | Get applicants for job id |
| /api/v1/application/status/:id/update     | POST   | Yes  | Body: { status } |

*Note: The codebase used GET for the apply route. This SRS mandates changing it to POST to align with HTTP semantics and security (prevent CSRF/pre-fetch issues).

### 21.2 Request and Response Formats

- JSON responses follow structure: { success: boolean, message: string, data?: {...} }
- Error responses use appropriate HTTP status codes and include message and success: false.

### 21.3 Authentication and Middleware

- `isAuthenticated` middleware reads cookie `token`, verifies with SECRET_KEY and sets `req.id` = decoded.userId. Controllers rely on req.id to scope operations.

### 21.4 Error Codes

- 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Internal Server Error.

---

## 22. Security Requirements

### 22.1 Authentication and Session Management

- Use JWT tokens signed with a strong secret (SECRET_KEY env var). Tokens expire after 24 hours. Cookies storing the token must be set with `httpOnly: true`, `secure: true` in production, and `SameSite: 'Strict'`. The current code contains a typo `httpsOnly` and must be corrected to `httpOnly`.

### 22.2 Password Protection

- Use bcrypt with a minimum of 10 salt rounds. Passwords never stored or transmitted in plain text.

### 22.3 Input Validation & Sanitization

- Enforce server-side validation using a library (express-validator). Validate email patterns, password strength, numeric constraints, input lengths, and sanitize text fields to prevent XSS.

### 22.4 File Upload Controls

- Enforce file size caps (images ≤ 5MB, resume docs ≤ 10MB) and whitelist MIME types (image/jpeg, image/png, application/pdf, application/msword, application/vnd.openxmlformats-officedocument.wordprocessingml.document). Use streaming uploads or disk-backed storage to avoid memory exhaustion caused by multer memoryStorage.

### 22.5 Authorization

- Ensure resource modification endpoints (company update, job update, application status update) verify the requesting user is the owner (i.e., company.userId or job.created_by matches req.id). Return 403 Forbidden otherwise.

### 22.6 Transport Layer Security

- Enforce HTTPS in production; set secure cookies and apply HSTS as appropriate.

### 22.7 Operational Security

- Rate-limit authentication endpoints to mitigate brute-force attacks. Log failed login attempts and alert on abnormal patterns.

---

## 23. Performance Requirements

### 23.1 Response Times

- Target median response time for basic GETs under typical loads < 300 ms. POSTs that involve Cloudinary will have longer latencies; asynchronous or background processing may be considered for heavy operations.

### 23.2 Scalability

- Stateless API servers should allow horizontal scaling behind a load balancer. Database scaling via replica sets and sharding as required.

### 23.3 Resource Utilization

- Avoid memory-heavy file handling in production. Use streaming or temporary disk storage for uploads.

---

## 24. Software Quality Attributes

- Maintainability: Modular code, controllers separated from models and routes.
- Testability: Tests defined for critical flows; use of Redux and modular components improves testability.
- Reliability: Graceful error handling expected; ensure DB reconnection logic for production.
- Usability: Intuitive UI components and flows; accessible via modern browsers.
- Security: Follow OWASP Top 10 mitigations (input validation, output encoding, auth controls, file upload checks).

---

## 25. Error Handling

- Use a centralized error-handling middleware in Express to capture synchronous and asynchronous errors. Responses should include status code and JSON with { success: false, message }.
- Do not expose stack traces in production responses. Log detailed errors to server logs but show generic messages to clients.

---

## 26. Validation Rules

**Table 10 — Validation Rules (summary)**

| Field                | Rule |
|----------------------|------|
| fullname             | Required, 2–100 chars, no HTML |
| email                | Required, valid format, unique |
| phoneNumber          | Required, numeric string, 7–15 digits |
| password             | Required, min 8 chars (recommend complexity) |
| role                 | Required, one of ['student','recruiter'] |
| company.name         | Required, unique |
| job.title            | Required, 5–200 chars |
| job.description      | Required, 10–5000 chars |
| job.position         | Integer >= 1 |
| file uploads         | Images: jpeg/png <=5MB; Resumes: pdf/docx <=10MB |
| application.status   | Enum: 'pending','accepted','rejected' |

---

## 27. Testing Strategies

### 27.1 Unit Testing

- Unit tests for controllers, utilities (e.g., data URI conversion) and reducers (frontend). Use Jest for backend; React Testing Library for frontend components.

### 27.2 Integration Testing

- Integration tests for routes using Supertest: ensure DB interactions are correct and middleware works.

### 27.3 End-to-End Testing

- Use Cypress to script user flows: signup/login, profile update, post job (recruiter), apply job (student), recruiter updates status.

### 27.4 Test Data & Environments

- Use a separate test DB (MongoDB test instance) and use mock/stub for Cloudinary (or use a test Cloudinary account). Wipe test DB between run cycles.

### 27.5 Continuous Integration

- Integrate tests in CI pipeline (GitHub Actions or similar) to run unit and integration tests on push.

---

## 28. Test Cases

**Table 6 — Representative Test Cases**

| TC ID | Test Case                                  | Steps | Expected Result |
|-------|--------------------------------------------|-------|-----------------|
| TC-01 | User registration (valid student)          | Submit valid signup form with profile image | 201 Created; user record in DB |
| TC-02 | User registration (duplicate email)        | Submit signup with existing email | 400 with message 'User already exist with this email.' |
| TC-03 | Login success                              | Submit correct credentials | 200; cookie token set; user returned |
| TC-04 | Login wrong password                       | Submit wrong password | 400 'Incorrect email or password.' |
| TC-05 | Post Job (recruiter)                       | Authenticated recruiter posts job | 201 job created; job.created_by == recruiter id |
| TC-06 | Apply Job (student)                        | Authenticated user applies to job | 201 Application created; job.applications length increases |
| TC-07 | Apply Job duplicate                        | Same user applies again | 400 with duplicate message |
| TC-08 | Company update unauthorized                | Non-owner attempts to update company | 403 Forbidden |
| TC-09 | Profile update with resume                 | Upload resume via profile update | 200; profile.resume contains Cloudinary URL |
| TC-10 | Get applicants                             | Recruiter requests applicants of own job | 200; job.applications populated with applicant data |

---

## 29. Risk Analysis

**Table 9 — Risk Analysis**

| Risk ID | Description | Probability | Impact | Mitigation |
|---------|-------------|-------------|--------|------------|
| R1 | Cookie incorrectly configured (`httpsOnly` typo) | Medium | High | Fix cookie option to `httpOnly: true`; set `secure: true` in production |
| R2 | Memory exhaustion due to multer.memoryStorage | Medium | High | Use disk storage or streaming uploads for production |
| R3 | Unauthorized updates to resources | Medium | High | Enforce owner checks in controllers; add unit tests |
| R4 | Malicious file uploads (malware) | Low | High | Enforce MIME/type checks & size limits; virus scanning in production |
| R5 | Brute force on login | Medium | Medium | Rate-limit login endpoint; log & alert suspicious attempts |
| R6 | Regex-based search DoS (ReDoS) | Low | Medium | Escape user input or use text indexes & controlled regex patterns |

---

## 30. Feasibility Study

### 30.1 Technical Feasibility

- The chosen stack (React, Node/Express, MongoDB, Cloudinary) is common and supported, making the project technically feasible.

### 30.2 Economic Feasibility

- For academic deployment, free tiers of MongoDB Atlas and Cloudinary will suffice for development. Production costs are moderate.

### 30.3 Operational Feasibility

- The system requires standard operational capabilities (Node.js hosting, MongoDB). Team can maintain and operate the system.

### 30.4 Schedule Feasibility

- Core features are implementable within a 6–12 week project schedule for a small team, with iterative releases.

---

## 31. Future Enhancements

- Email verification and password reset flows.
- Resume parsing to auto-extract skills and populate profile (NLP).
- Advanced search & filtering (faceted search, geolocation).
- Interview scheduling module with calendar integration.
- Notifications (email and in-app) for application status updates.
- Real-time chat between recruiter and applicant (WebSocket).
- Analytics dashboard for recruiters with visualizations (charts for applicants per job, conversion rates).

---

## 32. Conclusion

This SRS provides an exhaustive, IEEE-aligned description of the Job Portal project. It includes functional and non-functional requirements, data model and API definitions, security constraints, testing requirements and risks, and provides textual descriptions of diagrams to be included in a final submission. It is suitable for use as a project specification for development, testing and academic evaluation.

---

## 33. Appendix

### 33.1 Environment Variables (required)
- MONGO_URI: MongoDB connection string
- SECRET_KEY: JWT secret
- CLOUD_NAME: Cloudinary cloud name
- API_KEY: Cloudinary API key
- API_SECRET: Cloudinary API secret
- PORT: Server port

### 33.2 Key Source File Mapping (where to find specific behavior)
- Backend entry point: backend/index.js
- Controllers: backend/controllers/*.controller.js
- Models: backend/models/*.model.js
- Routes: backend/routes/*.route.js
- Middlewares: backend/middlewares/isAuthenticated.js, backend/middlewares/mutler.js
- Cloudinary utilities: backend/utils/cloudinary.js, backend/utils/datauri.js
- Frontend: frontend/src/components, frontend/src/hooks, frontend/src/redux

### 33.3 Developer quick-start (local)

Ensure environment variables are set (MONGO_URI, SECRET_KEY, CLOUD_NAME, API_KEY, API_SECRET).

**Backend:**
```bash
cd backend
npm install
npm run dev
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

Note: Cloudinary account required for file uploads.

---

## 34. Bibliography

- Node.js official documentation: https://nodejs.org
- React official documentation: https://reactjs.org
- Express official documentation: https://expressjs.com
- Mongoose documentation: https://mongoosejs.com
- Cloudinary documentation: https://cloudinary.com/documentation
- JWT information: https://jwt.io/introduction
- IEEE Std 830-1998, IEEE Recommended Practice for Software Requirements Specifications

---

## 35. References

(Repeated references used in research and system design)

---

## 36. Screenshots Placeholders (textual)

Below are textual placeholders describing screenshots to be inserted into the final printed report (images omitted per your request). Each placeholder includes a description and suggested file name for later insertion.

- Home Page — placeholder (file: screenshots/home_page.png)
  Description: Hero section, navbar, latest jobs sections, featured categories.

- Login Page — placeholder (file: screenshots/login_page.png)
  Description: Login form with fields for email, password and radio for role selection.

- Signup Page — placeholder (file: screenshots/signup_page.png)
  Description: Registration form with profile upload and role radio selections.

- Profile Page — placeholder (file: screenshots/profile_page.png)
  Description: Candidate profile display with skills badges and resume download link.

- Job Listings Page — placeholder (file: screenshots/job_listings.png)
  Description: Grid or list of job cards with filters in a sidebar.

- Job Description Page — placeholder (file: screenshots/job_description.png)
  Description: Full job details, badges for jobType and salary, Apply button.

- Apply Job Confirmation — placeholder (file: screenshots/apply_job_confirmation.png)
  Description: Success toast or confirmation screen after applying.

- Recruiter Dashboard — placeholder (file: screenshots/recruiter_dashboard.png)
  Description: Links to companies and jobs, counts and quick actions.

- Company Management — placeholder (file: screenshots/company_management.png)
  Description: Company registration and list view.

- Post Job Form — placeholder (file: screenshots/post_job_form.png)
  Description: Form fields for job posting.

- Applicants Management — placeholder (file: screenshots/applicants_management.png)
  Description: Table of applicants for a job with ability to change status.

---

## 37. Diagram Textual Descriptions (no images)

Below are precise textual descriptions of diagrams that would normally be included as images. These descriptions are written to be directly convertible to diagrams by any diagramming tool or by a visual designer.

### 37.1 System Architecture (textual) — (Figure 1)
- Actors: User (Browser).
- Components: React SPA (Vite + Redux) — communicates over HTTPS to REST API (Node.js + Express). REST API interacts with MongoDB (Mongoose) and Cloudinary (asset uploads). Authentication uses JWT stored in cookies. The SPA uses axios with credentials to call the API. The API exposes endpoints: /api/v1/user, /api/v1/company, /api/v1/job, /api/v1/application. This architecture emphasizes decoupling and externalized asset storage.

### 37.2 ER Diagram (textual) — (Figure 2)
- Entities:
  - User: attributes include _id, fullname, email (unique), phoneNumber, password, role (enum), profile object (bio, skills[], resume, resumeOriginalName, company ref, profilePhoto).
  - Company: attributes include _id, name (unique), description, website, location, logo, userId (ref to User).
  - Job: attributes include _id, title, description, requirements[], salary, experienceLevel, location, jobType, position, company (ref), created_by (ref User), applications[] (array of Application refs).
  - Application: attributes include _id, job (ref), applicant (ref), status (enum).
- Relationships: one User -> many Companies; one Company -> many Jobs; one Job -> many Applications; one User -> many Applications.

### 37.3 Use Case Diagram (textual) — (Figure 3)
- Actors: Student, Recruiter.
- Student use cases: Register, Login, Update Profile, Search Jobs, View Job Details, Apply for Job, View Applied Jobs.
- Recruiter use cases: Register, Login, Register Company, Post Job, View Applicants, Update Application Status.

### 37.4 DFD Level 0 (context) — (Figure 4)
- External Entities: User (Browser), Cloudinary, MongoDB.
- System: Job Portal System.
- Data flows: User interacts with System via HTTP requests; System reads/writes data to MongoDB; System uploads and retrieves files from Cloudinary.

### 37.5 DFD Level 1 (detailed) — (Figure 5)
- Processes: Authentication Service, Profile Service, Company Service, Job Service, Application Service.
- Data stores: users, companies, jobs, applications.
- Process flows: Authentication validates credentials → DB lookup; Job Service handles create/search/get; Application Service creates application records and updates job documents.

### 37.6 Activity Diagram — Apply Job (textual) — (Figure 6)
- Steps: User logs in → navigates to job description → system checks if user already applied → if applied → show disabled Apply button; else → user clicks Apply → front-end sends POST /application/apply/:jobId → backend verifies token, checks for existing application, creates Application, appends application id to job → returns success → front-end updates UI and shows confirmation.

### 37.7 Sequence Diagram — Candidate Apply (textual) — (Figure 7)
- Sequence: Student → SPA (click Apply) → SPA → API POST /application/apply/:id (cookie) → API → isAuthenticated middleware (verify JWT) → API → DB: find Job by id → API → DB: check existing Application → API → DB: create Application → API → DB: push application id to Job.applications → API → SPA: 201 success → SPA → Student: display success.

### 37.8 Component Diagram (textual) — (Figure 8)
- Frontend components: Navbar, Jobs, JobDescription, Profile, Admin components, Redux store (slices: auth, job, company, application), Hooks (useGetAllJobs, useGetAllCompanies). 
- Backend components: Routes, Controllers, Middlewares (auth, multer), Utils (cloudinary, datauri). 
- Data flows: Frontend ↔ Backend via REST; Backend ↔ DB via Mongoose; Backend ↔ Cloudinary via SDK.

### 37.9 Deployment Diagram (textual) — (Figure 9)
- Nodes: Client Browser, CDN/Web Server (optional for static assets), App Server (Node.js instances behind load balancer), MongoDB Atlas cluster, Cloudinary. The App Server communicates with DB and Cloudinary; static frontend files served via CDN or static hosting.

---

## 38. Complete Lists (for appendices)

### 38.1 Detected Codebase Modules (concise)
- Backend: index.js, controllers (user/job/company/application), models (user/job/company/application), routes, middlewares, utils.
- Frontend: components (Home, Jobs, JobDescription, Profile, Admin), hooks, redux slices and store, UI primitives.

### 38.2 Pages / Screens
- Home, Jobs list, Job details, Login, Signup, Profile, Recruiter Companies, Post Job, Admin Jobs, Applicants, Applied Jobs.

### 38.3 API list
- See Section 21, full list of endpoints and descriptions.

### 38.4 Database tables (collections)
- users, companies, jobs, applications.

### 38.5 User roles
- student, recruiter.

---

## 39. Recommended Immediate Code Corrections (actionable)

- Fix cookie option `httpsOnly` to `httpOnly` in backend login controller when setting cookie. Add `secure: true` when NODE_ENV === 'production'.
- Change apply endpoint from GET to POST to prevent side-effects from GET and reduce CSRF risk.
- Add owner checks in company update and job update endpoints to ensure only resource owners can modify.
- Add server-side validation (express-validator) and centralize error handling.
- Replace multer memoryStorage with diskStorage or stream to Cloudinary to avoid memory exhaustion.

---

## 40. Try-it / Run Commands (developer)

To run the project locally (assumes environment variables set):

**Backend:**
```bash
cd backend
npm install
npm run dev
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

To run tests (if added):
```bash
# backend
cd backend
npm test
```

---

## 41. Conclusion

This SRS provides an exhaustive, IEEE-aligned description of the Job Portal system. It identifies functional and non-functional requirements, data model and API definitions, security constraints, testing requirements and risks, and provides textual descriptions of diagrams to be included in a final submission. It is suitable for use as a project specification for development, testing and academic evaluation.

---

## 42. Appendix A — Tables (reproduced for quick access)

**Table 3 — User Roles and Permissions**

| Role     | Permissions                                                                 |
|----------|-----------------------------------------------------------------------------|
| Student  | Registration, login, profile update, resume upload, search jobs, apply, view applied jobs |
| Recruiter| Registration, login, register company, update company, post job, view applicants, update application status |

**Table 7 — Hardware Requirements**

| Component      | Minimum                     | Recommended                        |
|----------------|-----------------------------|------------------------------------|
| Developer PC   | 2 CPU cores, 4GB RAM        | 4 CPU cores, 8GB RAM               |
| Server         | 1 vCPU, 1GB RAM             | 2+ vCPU, 4+ GB RAM, SSD            |

**Table 8 — Software Requirements**

| Component | Version / Notes |
|-----------|-----------------|
| Node.js   | v16+ (18 recommended) |
| npm/yarn  | Latest compatible |
| MongoDB   | 4.x/5.x (Atlas supported) |
| Cloudinary| Account + credentials required |
| Browsers  | Modern - Chrome, Firefox, Safari, Edge |

---

## 43. Appendix B — Test Cases (complete list)

(See Section 28 — core test cases provided; full QA team should expand to detailed test scripts.)

---

## 44. Appendix C — Contact

Project Lead: [Student Name] — [email@example.com]

Supervisor: [Supervisor Name] — [supervisor@example.com]

---

End of SRS (Markdown)
