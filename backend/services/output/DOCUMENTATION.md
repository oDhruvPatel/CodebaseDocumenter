# Shipment & Fleet Tracker

## package.json
Defines backend project metadata, scripts, and dependencies.

**Functions:**

**Dependencies:**
- bcryptjs
- cors
- dotenv
- express
- jsonwebtoken
- mongoose
- nodemon

---

## seed.js
Populates the database with sample admin/viewer users and demo shipments.

**Functions:**
- seedData - populates the database with sample data

**Dependencies:**
- mongoose
- dotenv
- ./models/User
- ./models/Shipment

---

## server.js
Main entry point for the Express backend API, sets up middleware, connects to MongoDB, and defines routes.

**Functions:**

**Dependencies:**
- express
- mongoose
- cors
- dotenv
- ./routes/auth
- ./routes/shipments

---

## auth.js
Provides middleware functions for JWT token verification and role-based access control.

**Functions:**
- verifyToken - verifies a JWT token from the request header
- requireAdmin - checks if the authenticated user has an 'admin' role

**Dependencies:**
- jsonwebtoken

---

## Shipment.js
Defines the Mongoose schema and model for shipment data.

**Functions:**

**Dependencies:**
- mongoose

---

## User.js
Defines the Mongoose schema and model for user data, including password hashing.

**Functions:**
- userSchema.pre('save') - hashes user password before saving
- userSchema.methods.comparePassword - compares a candidate password with the stored hash

**Dependencies:**
- mongoose
- bcryptjs

---

## auth.js
Handles user authentication (registration, login) and provides current user information.

**Functions:**
- router.post('/register') - registers a new user
- router.post('/login') - authenticates a user and returns a JWT
- router.get('/me') - retrieves the current user's profile

**Dependencies:**
- express
- jsonwebtoken
- ../models/User
- ../middleware/auth

---

## shipments.js
Defines API routes for managing shipments, including CRUD operations and filtering.

**Functions:**
- router.get('/') - lists all shipments with optional filters
- router.get('/:id') - retrieves a single shipment by ID
- router.post('/') - creates a new shipment (admin only)
- router.put('/:id') - updates an existing shipment (admin only)
- router.delete('/:id') - deletes a shipment (admin only)

**Dependencies:**
- express
- ../models/Shipment
- ../middleware/auth

---

## angular.json
Angular CLI configuration file for the frontend project.

**Functions:**

**Dependencies:**

---

## package.json
Defines frontend project metadata, scripts, and dependencies.

**Functions:**

**Dependencies:**
- @angular/animations
- @angular/common
- @angular/compiler
- @angular/core
- @angular/forms
- @angular/platform-browser
- @angular/platform-browser-dynamic
- @angular/router
- leaflet
- rxjs
- tslib
- zone.js
- @angular-devkit/build-angular
- @angular/cli
- @angular/compiler-cli
- @types/leaflet
- typescript

---

## tsconfig.app.json
TypeScript configuration for the Angular application compilation.

**Functions:**

**Dependencies:**

---

## tsconfig.json
Base TypeScript configuration for the Angular project.

**Functions:**

**Dependencies:**

---

## index.html
Main HTML file for the Angular frontend, serving as the entry point for the web application.

**Functions:**

**Dependencies:**

---

## main.ts
Entry point for bootstrapping the Angular application.

**Functions:**
- bootstrapApplication - initializes and starts the Angular application

**Dependencies:**
- @angular/platform-browser
- ./app/app.config
- ./app/app.component

---

## styles.css
Defines global CSS styles, variables, and utility classes for the frontend application.

**Functions:**

**Dependencies:**

---

## app.component.ts
Root component of the Angular application, hosting the router outlet.

**Functions:**

**Dependencies:**
- @angular/core
- @angular/router

---

## app.config.ts
Configures the Angular application's providers, including routing and HTTP client with interceptors.

**Functions:**

**Dependencies:**
- @angular/core
- @angular/router
- @angular/common/http
- ./app.routes
- ./interceptors/auth.interceptor

---

## app.routes.ts
Defines the routing configuration for the Angular application.

**Functions:**

**Dependencies:**
- @angular/router
- ./components/login/login.component
- ./components/dashboard/dashboard.component
- ./guards/auth.guard

---

## dashboard.component.css
Styles for the dashboard component layout and elements.

**Functions:**

**Dependencies:**

---

## dashboard.component.html
HTML template for the dashboard component, displaying stats, map, shipment list, and form modal.

**Functions:**
- logout - logs out the user
- onFilterChange - applies shipment status filter
- onAddNew - opens form for new shipment creation
- onEdit - opens form for editing a shipment
- onDelete - deletes a shipment
- onFormClose - closes the shipment form modal
- onFormSaved - handles form saved event to refresh data

**Dependencies:**

---

## dashboard.component.ts
Manages the dashboard view, including fetching and displaying shipments, stats, filtering, and CRUD operations.

**Functions:**
- ngOnInit - initializes component data by loading shipments
- loadShipments - fetches shipments from the service and updates stats
- calculateStats - computes shipment statistics based on current data
- onFilterChange - updates filtered shipments based on selected status
- onAddNew - prepares the form for creating a new shipment
- onEdit - prepares the form for editing an existing shipment
- onDelete - handles shipment deletion via the service
- onFormClose - closes the shipment form modal
- onFormSaved - reloads shipments after a form submission (create/update)
- logout - calls the authentication service to log out the user

**Dependencies:**
- @angular/core
- @angular/common
- @angular/forms
- ../../services/auth.service
- ../../services/shipment.service
- ../shipment-list/shipment-list.component
- ../map/map.component
- ../shipment-form/shipment-form.component

---

## login.component.css
Styles for the login and registration page.

**Functions:**

**Dependencies:**

---

## login.component.html
HTML template for the login and registration component.

**Functions:**
- onSubmit - handles form submission for login or registration
- toggleMode - switches between login and registration forms

**Dependencies:**

---

## login.component.ts
Handles user login and registration logic, interacting with the authentication service.

**Functions:**
- constructor - redirects to dashboard if already logged in
- toggleMode - switches between login and registration forms
- onSubmit - performs user login or registration

**Dependencies:**
- @angular/core
- @angular/common
- @angular/forms
- @angular/router
- ../../services/auth.service

---

## map.component.ts
Displays shipment locations on an interactive Leaflet map.

**Functions:**
- ngAfterViewInit - initializes the map after the view is rendered
- ngOnChanges - updates map markers when shipments input changes
- initMap - sets up the Leaflet map instance
- updateMarkers - clears existing markers and adds new ones for shipments

**Dependencies:**
- @angular/core
- @angular/common
- ../../services/shipment.service
- leaflet

---

## shipment-form.component.css
Styles for the shipment creation and editing modal form.

**Functions:**

**Dependencies:**

---

## shipment-form.component.html
HTML template for the shipment creation and editing form modal.

**Functions:**
- onClose - closes the modal
- onSubmit - submits the shipment form

**Dependencies:**

---

## shipment-form.component.ts
Manages the form for creating or editing shipment details.

**Functions:**
- ngOnInit - initializes form data if editing an existing shipment
- onSubmit - handles form submission to create or update a shipment
- onClose - emits a close event for the modal

**Dependencies:**
- @angular/core
- @angular/common
- @angular/forms
- ../../services/shipment.service

---

## shipment-list.component.css
Styles for the shipment list table.

**Functions:**

**Dependencies:**

---

## shipment-list.component.html
HTML template for displaying a list of shipments in a table.

**Functions:**
- onEdit - emits an event to edit a specific shipment
- onDelete - emits an event to delete a specific shipment

**Dependencies:**

---

## shipment-list.component.ts
Displays a table of shipments and allows editing/deleting for admin users.

**Functions:**
- onEdit - emits an event to edit a shipment
- onDelete - emits an event to delete a shipment

**Dependencies:**
- @angular/core
- @angular/common
- ../../services/shipment.service

---

## auth.guard.ts
Angular route guard to protect routes that require authentication.

**Functions:**
- authGuard - checks if a user is logged in before allowing route activation

**Dependencies:**
- @angular/core
- @angular/router
- ../services/auth.service

---

## auth.interceptor.ts
Angular HTTP interceptor to add JWT authorization token to outgoing requests.

**Functions:**
- authInterceptor - intercepts HTTP requests to add an Authorization header

**Dependencies:**
- @angular/common/http

---

## auth.service.ts
Provides authentication functionalities including login, registration, logout, and managing user state.

**Functions:**
- constructor - restores user from local storage on app start
- login - authenticates a user with the backend
- register - registers a new user with the backend
- logout - clears user session and navigates to login
- isLoggedIn - checks if a user token exists
- currentUser - gets the current authenticated user object
- isAdmin - checks if the current user has 'admin' role

**Dependencies:**
- @angular/core
- @angular/common/http
- rxjs
- @angular/router

---

## shipment.service.ts
Provides methods for interacting with the backend API for shipment-related operations.

**Functions:**
- getShipments - fetches a list of shipments with optional filters
- getShipment - fetches a single shipment by ID
- createShipment - creates a new shipment
- updateShipment - updates an existing shipment
- deleteShipment - deletes a shipment

**Dependencies:**
- @angular/core
- @angular/common/http
- rxjs

---

