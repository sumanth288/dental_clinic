# Ramana's Dental & Implant Centre - Website

A static, responsive dental clinic website with a glass-morphism design, deployed on Cloudflare Pages.

## Pages

1. **Home Page**: Hero section, featured services, why choose us
2. **About Page**: Clinic story, mission, values
3. **Services Page**: Complete service catalog
4. **Doctors Page**: Team profiles with specializations
5. **Appointment Page**: Online booking form
6. **Contact Page**: Contact form, information, hours

## Technology Stack

- **Hosting**: Cloudflare Pages (static assets, see `wrangler.jsonc`)
- **Frontend**: HTML5, CSS3, JavaScript
- **CSS Framework**: Bootstrap 5.3.3
- **Icons**: Bootstrap Icons
- **Fonts**: Google Fonts (Poppins)
- **Forms**: Web3Forms (client-side submission, no backend)

## Running locally

No build step or server required — it's a static site.

- **Quickest**: open any `.html` file (e.g. `index.html`) directly in a browser.
- **Production parity**: from this folder, run `npx wrangler pages dev .` and open `http://localhost:8788`.

## Project Structure

```
dental_clinic/
├── index.html
├── about.html
├── services.html
├── doctors.html
├── appointment.html
├── contact.html
├── wrangler.jsonc        # Cloudflare Pages config
└── static/
    ├── css/
    │   └── style.css
    ├── js/
    │   └── main.js
    └── images/
```

## Customization

### Colors
The color scheme can be modified in `static/css/style.css`:
```css
:root {
    --primary-color: #00bcd4;
    --secondary-color: #009688;
    --accent-color: #ff5722;
    /* ... other colors */
}
```

### Content
Edit the relevant `.html` page directly — there's no templating layer.

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers
