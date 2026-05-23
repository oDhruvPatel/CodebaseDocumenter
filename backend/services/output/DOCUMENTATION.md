# speercheck

## components.json
Configures shadcn/ui components and project aliases.

**Functions:**

**Dependencies:**

---

## eslint.config.js
Configures ESLint for the project, including TypeScript, React hooks, and React refresh.

**Functions:**
- defineConfig - sets up ESLint configuration

**Dependencies:**
- @eslint/js
- globals
- eslint-plugin-react-hooks
- eslint-plugin-react-refresh
- typescript-eslint
- eslint/config

---

## index.html
The main HTML entry point for the React application.

**Functions:**

**Dependencies:**

---

## jest.config.ts
Configures Jest for running TypeScript tests using ts-jest.

**Functions:**

**Dependencies:**
- ts-jest

---

## package.json
Defines project metadata, scripts, and manages dependencies for the application.

**Functions:**

**Dependencies:**
- @fontsource-variable/geist
- class-variance-authority
- clsx
- dayjs
- lucide-react
- next-themes
- radix-ui
- react
- react-dom
- react-hot-toast
- shadcn
- sonner
- tailwind-merge
- tw-animate-css
- zustand
- @eslint/js
- @tailwindcss/vite
- @types/jest
- @types/node
- @types/react
- @types/react-dom
- @vitejs/plugin-react
- autoprefixer
- eslint
- eslint-plugin-react-hooks
- eslint-plugin-react-refresh
- globals
- jest
- postcss
- tailwindcss
- ts-jest
- typescript
- typescript-eslint
- vite

---

## README.md
Provides an overview of the project, design decisions, setup instructions, and AI usage.

**Functions:**

**Dependencies:**

---

## tsconfig.app.json
TypeScript configuration specifically for the application source files.

**Functions:**

**Dependencies:**

---

## tsconfig.json
Main TypeScript configuration file, referencing other tsconfig files.

**Functions:**

**Dependencies:**

---

## tsconfig.node.json
TypeScript configuration specifically for Node.js-related files like vite.config.ts.

**Functions:**

**Dependencies:**

---

## vite.config.ts
Configures Vite for development and build processes, including React and Tailwind CSS plugins.

**Functions:**
- defineConfig - configures Vite

**Dependencies:**
- vite
- @vitejs/plugin-react
- @tailwindcss/vite
- path

---

## App.tsx
The root component of the React application, rendering the Home page and a global toast system.

**Functions:**
- App - main application component

**Dependencies:**
- ./index.css
- ./pages/Home
- react-hot-toast

---

## index.css
Global CSS file importing fonts, Tailwind CSS, animations, and defining custom theme variables.

**Functions:**

**Dependencies:**
- tailwindcss
- tw-animate-css
- shadcn/tailwind.css
- @fontsource-variable/geist

---

## main.tsx
Entry point for the React application, rendering the App component into the DOM.

**Functions:**

**Dependencies:**
- react
- react-dom
- ./index.css
- ./App.tsx

---

## Button.tsx
A React component that provides a dropdown for selecting a candidate.

**Functions:**
- Button - renders the candidate selection dropdown

**Dependencies:**
- ../data/availability
- @/store/useSchedulerStore
- @/components/ui/select

---

## Calender.tsx
Displays a calendar grid with time slots, showing engineer and candidate availability, and handles slot selection.

**Functions:**
- Calender - renders the calendar interface

**Dependencies:**
- ../libs/getTime
- ../libs/getDays
- ./ui/scroll-area
- dayjs
- clsx
- ../data/availability
- ./SlotCard
- @/store/useSchedulerStore

---

## ConfirmationScreen.tsx
A modal component that displays interview confirmation details and handles scheduling.

**Functions:**
- ConfirmationModal - renders the interview confirmation modal
- handleConfirm - schedules the interview and shows a toast

**Dependencies:**
- ../store/useSchedulerStore
- dayjs
- clsx
- react-hot-toast

---

## Main.tsx
Orchestrates the main layout of the application, including the top bar, calendar, and confirmation screen.

**Functions:**
- Main - composes the main UI components

**Dependencies:**
- ./Calender
- ./TopBar
- ./ConfirmationScreen

---

## Navbar.tsx
Renders a navigation bar with the application logo and title.

**Functions:**
- Navbar - displays the application logo and title

**Dependencies:**
- ../assets/speer_logo_header.fd6ca103 (1).svg

---

## SlotCard.tsx
A reusable component to display individual time slots for engineers, candidates, or overlaps within the calendar.

**Functions:**
- SlotCard - renders an interactive time slot

**Dependencies:**
- clsx

---

## Toast.tsx
A simple React component for displaying a toast message.

**Functions:**
- Toast - renders a toast message

**Dependencies:**

---

## TopBar.tsx
Displays the application header, including the logo, week navigation, engineer legends, and candidate selection.

**Functions:**
- TopBar - renders the application's top navigation and information bar

**Dependencies:**
- @/assets/speer_logo_header.fd6ca103 (1).svg
- ./Button
- ../data/availability
- ../libs/getDays
- dayjs
- clsx

---

## label.tsx
A Shadcn UI component for rendering accessible labels.

**Functions:**
- Label - renders an accessible label

**Dependencies:**
- react
- radix-ui
- @/lib/utils

---

## scroll-area.tsx
A Shadcn UI component for creating scrollable regions with custom scrollbars.

**Functions:**
- ScrollArea - creates a scrollable container
- ScrollBar - renders the custom scrollbar

**Dependencies:**
- react
- radix-ui
- @/lib/utils

---

## select.tsx
A Shadcn UI component providing a highly customizable select dropdown.

**Functions:**
- Select - root select component
- SelectGroup - groups select items
- SelectValue - displays the selected value
- SelectTrigger - the interactive element that opens the select
- SelectContent - the container for select items
- SelectLabel - a label for a group of items
- SelectItem - an individual selectable item
- SelectSeparator - a visual separator between items
- SelectScrollUpButton - button to scroll up in the select content
- SelectScrollDownButton - button to scroll down in the select content

**Dependencies:**
- react
- radix-ui
- @/lib/utils
- lucide-react

---

## separator.tsx
A Shadcn UI component for rendering a visual separator.

**Functions:**
- Separator - renders a visual separator

**Dependencies:**
- react
- radix-ui
- @/lib/utils

---

## sonner.tsx
Wraps the sonner toast library with next-themes integration and custom icons.

**Functions:**
- Toaster - configures and renders the sonner toast system

**Dependencies:**
- next-themes
- sonner
- lucide-react

---

## availability.ts
Defines static dummy data for engineers and candidates, including their availability schedules.

**Functions:**

**Dependencies:**

---

## utils.ts
Provides utility functions, specifically for conditionally joining CSS class names.

**Functions:**
- cn - conditionally joins CSS class names using clsx and tailwind-merge

**Dependencies:**
- clsx
- tailwind-merge

---

## getDays.ts
Generates an array of 5 days starting from the current week's Monday.

**Functions:**
- generateDays - calculates and returns an array of day objects

**Dependencies:**
- dayjs

---

## getTime.ts
Generates an array of 30-minute time slots from 9 AM to 6 PM.

**Functions:**
- generateSlots - calculates and returns an array of time strings

**Dependencies:**
- dayjs

---

## Home.tsx
The main page component that renders the core application layout.

**Functions:**
- Home - renders the Main component

**Dependencies:**
- ../components/Main

---

## useSchedulerStore.ts
Implements Zustand stores for managing global state related to candidate selection, interview confirmation, and booked slots.

**Functions:**
- useCandidateStore - manages the selected candidate state
- useConfirmStore - manages the interview confirmation details state
- useBookedSlotStore - manages the booked interview slots state

**Dependencies:**
- zustand
- ../data/availability

---

## availability.test.ts
Contains unit tests for the interview overlap logic.

**Functions:**
- findOverlap - helper function to simulate overlap logic

**Dependencies:**

---

