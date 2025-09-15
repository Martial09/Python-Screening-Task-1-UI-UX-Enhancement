# UI/UX Enhancement for Workshop Booking Site

This project improves on the user interface (UI) and user experience (UX) of the original FOSSEE Workshop Booking website. The overall aim was a modern, responsive, and intuitive interface for students, since they will primarily use the site on their mobile devices.

The backend logic and general Flask structure has not been changed, the improvements presented are focused on the frontend presentation layer composed of HTML, CSS (with a Bootstrap 5 framework), and a little JavaScript. Reasoning and design choices
The answers to the required questions on design and development process are listed below.

1. What design principles were followed to improve your designs?

The improvements to the designs were driven by the following core design concepts:
Mobile-First Design: The main scenario was mobile usage. The following design decisions were made on tablet and desktop versions only after they were optimized for the mobile experience. The benefit of this approach is that the target user group will experience a somewhat consistence interaction/experience.
Clarity and simplicity: The interface is open and clean. I utilized white space, an easy to read font (defaulted by Bootstrap), and a limited color scope (dark navbar, primary blue for whatever actions would be needed – buttons, links) to decrease cognitive load and simplify menu navigation.
Visual hierarchy: I directed users attention through size, colour, and location of items. For instance, the homepage main heading is large and bold; CTA buttons are easily prominent, and workshop titles on cards are clearly view-able and styled differently than the description text.
Consistency: To help with visual rhythm and ease of navigation, I created a base.html template that will utilize the same navigation bar, footer, and style across the site. It will make the site feel predictable, and subsequently, easier to learn based on visual knowledge.

2. How did you ensure responsive design on all devices?

Making sure that our site was responsive was very important and accomplished by way of several techniques, mainly relying on Bootstrap 5.
Viewport Meta Tag: So, adding  in base.html is really the first thing made sure there is a viewport and the page will scale correctly across devices.
Responsive Grid System: I ultimately used the Bootstrap 5 responsive grid for the workshop list (e.g. row, col-md-2 col-lg-3), which will automatically layout workshop cards in one column (small screens/mobile), two columns (medium screens/tablets) and three columns (large screens/desktop).
Collabsible Navigation:  Our navigation bar within the .navbar will automatically convert to a collapsible hamburger style menu on smaller screens, preserving the screen real-estate while still ultimately keeping all links available to the user.
Responsive Components: All the UI components we used from Bootstrap (Cards, Forms, Buttons, Alerts) are responsive components and made to adjust to fit screens of all sizes.
Responsive Tables: For the bookings page, which contains tabular data, we wrapped the table in a .table-responsive div. That way, when displayed on smaller screens, we do not break the page layout with overflow - the table itself will have a horizontal scroll bar so the user can still see all data from it.

3. What trade-offs did you make regarding design and performance?

The primary trade-off involved using an external UI Framework (Bootstrap) versus writing a minimal amount of custom CSS from scratch.
Design/Development Benefit: Using bootstrap enabled the implementation of a well-tested, professional-grade, and responsive design, almost immediately. Writing custom CSS, media queries, and JavaScript for components like the collapsible navbar would have taken a significant amount of time and effort.
Performance Penalty: The "trade-off" is only a small, initial page load time increase as the browser has to download Bootstrap's CSS (~150kb), and JS (~50kb) files; however, and as you will see below, it was mitigated and justified in several respects.
CDN Hosted: The user’s browser load will sometimes include an already cached version of the same files when loaded via a popular CDN because the user has visited other sites that used bootstrap.
Minimal Impact: For a small app like this example, the performance hit is inconsequential on today's modern internet connection speeds.
Humongous UX Gain: The vastly improved usability, accessibility, and professional appearance far outweighs the minimal performance hit. Overall, the site, (i.e., sites) is a lot more usable than it was before, and that was the intent of the exercise.

4. What was the most difficult part of the task and how did you resolve it?

The hardest part of the task was deciding on the most effective way of displaying the list of available workshops. The original version used a straightforward <table> element. While this is OK on a desktop, it can be a nightmare for developers to render truly responsive and understandable on narrow mobile screens.
I considered a couple options:
Responsive Table: I initially thought of making the original table responsive. Even with horizontal scrolling, a table with content descriptions can feel squished and bouncing back and forth between scrolling can create a poor experience.
List View: I thought about using a simple list of workshops stacked up vertically. That would look good on mobile, but the desktop rendering might look too simplistic and spare and not take up enough space.
Card Based Grid (Best approach eventually decided on): I chose to re-do it as Bootstrap Card-based grid. This worked best because:
It is responsive by default: the grid system is smart enough to start with a singular column on mobile and go to multiple columns on larger views.
It's information modular: Each card contains all the information for a workshop (title, description, call-to-action button) in one place, making it easier to scan and consume.
It's aesthetically pleasing: Cards give the site a modern feel and style that is better than using a table.

This decision involved rewriting the HTML and Jinja2 loop in workshops.html, but the result was the most significant improvement to UX for mobile users on this site.