# Dental Care Clinic - Flask Web Application

A modern, responsive dental clinic website built with Flask, featuring a beautiful glass-morphism design and comprehensive dental services.

## Features

- **Modern Design**: Glass-morphism UI with smooth animations
- **Responsive Layout**: Works perfectly on all devices
- **Professional Pages**: Home, About, Services, Doctors, Appointment, Contact
- **Interactive Forms**: Appointment booking and contact forms with validation
- **Doctor Profiles**: Professional team showcase with images
- **Service Catalog**: Comprehensive dental services with pricing
- **Contact Information**: Multiple ways to get in touch
- **Google Maps Integration**: Location display
- **FAQ Section**: Common questions and answers

## Pages

1. **Home Page**: Hero section, featured services, why choose us
2. **About Page**: Clinic story, mission, values, team highlights
3. **Services Page**: Complete service catalog with pricing
4. **Doctors Page**: Team profiles with specializations
5. **Appointment Page**: Online booking form
6. **Contact Page**: Contact form, information, map, FAQ

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **CSS Framework**: Bootstrap 5.3.3
- **Icons**: Bootstrap Icons
- **Fonts**: Google Fonts (Poppins)
- **Images**: Unsplash (professional dental images)

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd dental_clinic
   ```

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the website**:
   Open your browser and go to `http://localhost:5001`

## Project Structure

```
dental_clinic/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with header/footer
│   ├── index.html        # Home page
│   ├── about.html        # About page
│   ├── services.html     # Services page
│   ├── doctors.html      # Doctors page
│   ├── appointment.html  # Appointment page
│   └── contact.html      # Contact page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Custom styles
    ├── js/
    │   └── main.js       # Custom JavaScript
    └── images/           # Image assets
```

## Features in Detail

### Design Features
- Glass-morphism effect with backdrop blur
- Smooth hover animations
- Gradient backgrounds
- Professional color scheme (teal/cyan theme)
- Responsive grid layouts
- Modern typography

### Interactive Elements
- Form validation with Bootstrap
- Smooth scrolling navigation
- Animated service cards
- Doctor profile hover effects
- Loading states for forms
- Auto-hiding notifications

### Content Features
- Professional dental services
- Doctor profiles with images
- Service pricing information
- Contact details and hours
- Google Maps integration
- FAQ section

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
- Update clinic information in `app.py`
- Modify service details and pricing
- Add/remove doctor profiles
- Update contact information

### Images
- Replace placeholder images with actual clinic photos
- Update doctor profile images
- Add clinic facility images

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge
- Mobile browsers

## License

This project is created for educational and commercial use. Feel free to modify and use for your dental clinic.

## Support

For any questions or issues, please contact the development team.

---

**Dental Care Clinic** - Your Smile, Our Priority 