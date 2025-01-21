# Multiple Apps

The project is structured with multiple apps, each responsible for a specific functionality, ensuring a modular and scalable architecture.

# Models

The project features three primary models, each incorporating multiple foreign key relationships to ensure robust data structure and seamless integration between entities.

## Products Model (CRUD functionality):
Full create, read, update, and delete operations are supported.

## Blog Model (CRUD functionality):
**Fully supports create, read, update, and delete operations**, with access granted to both the **admin** and the **user who created the post**.

## Appointments Model :
Handles a different set of data but may not include full CRUD operations.

# "Secure Administrative Functions with Decorators"

**Administrative functions are protected using decorators**, ensuring that only authorized users, such as admins, can access and perform sensitive actions.

# Auto Email Sender

**An automated email system has been integrated into the project**. When users submit an appointment request, a confirmation email is sent to the user to confirm the scheduled time. **The same functionality is also available when a user places an order for a product**, ensuring they receive a confirmation email with the order details.

# Blog for Adoption Stories

The project features a blog where users can read and post adoption stories. This blog allows for easy publishing of content related to adoption, promoting awareness and support for families.

# Dynamic Navigation Bar

A dynamic navigation bar is included that adjusts based on the user’s authentication status and relevant permissions. It provides a smooth and intuitive navigation experience across different pages.

# User-friendly Interface

The project has a clean, responsive, and easy-to-use interface for all users, making it accessible from various devices.
