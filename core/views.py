def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # For demo, if username contains 'org', set as organizer, else attendee
        if 'org' in username.lower():
            role = 'organizer'
        else:
            role = 'attendee'
        request.session['role'] = role
        request.session['username'] = username
        return redirect('home-page')
    return render(request, 'login.html')
from django.shortcuts import redirect
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        role = request.POST.get('role')
        # Simulate registration by saving role in session
        request.session['role'] = role
        request.session['username'] = username
        return redirect('login-page')
    return render(request, 'register.html')
def events_view(request):
    events = [
        {
            'name': 'Tech Conference 2025',
            'description': 'A gathering of tech enthusiasts and professionals featuring keynote speakers, workshops, and networking opportunities.',
            'venue': 'Grand Conference Center',
            'date': '2025-08-15',
            'time': '9:00 AM - 6:00 PM',
            'capacity': 500,
            'price': '$299',
            'image': 'https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80',
            'tags': ['Technology', 'Networking', 'Professional'],
            'organizer': 'TechEvents Inc.',
        },
        {
            'name': 'Startup Pitch Night',
            'description': 'An evening of innovative startup pitches to angel investors and venture capitalists.',
            'venue': 'Innovation Hub',
            'date': '2025-08-20',
            'time': '6:00 PM - 9:00 PM',
            'capacity': 200,
            'price': '$50',
            'image': 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=400&q=80',
            'tags': ['Startup', 'Business', 'Investment'],
            'organizer': 'StartupLaunch',
        },
        {
            'name': 'Art Expo 2025',
            'description': 'A showcase of contemporary art featuring local and international artists.',
            'venue': 'Metropolitan Art Gallery',
            'date': '2025-08-25',
            'time': '10:00 AM - 8:00 PM',
            'capacity': 300,
            'price': '$25',
            'image': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80',
            'tags': ['Art', 'Culture', 'Exhibition'],
            'organizer': 'ArtCurators Ltd.',
        },
        {
            'name': 'Food & Wine Festival',
            'description': 'A culinary journey featuring top chefs, wine tastings, and gourmet food stalls.',
            'venue': 'Riverside Gardens',
            'date': '2025-09-01',
            'time': '12:00 PM - 10:00 PM',
            'capacity': 1000,
            'price': '$75',
            'image': 'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=400&q=80',
            'tags': ['Food', 'Wine', 'Festival'],
            'organizer': 'Culinary Events Co.',
        },
        {
            'name': 'Music Festival 2025',
            'description': 'A three-day music extravaganza featuring top artists across multiple genres.',
            'venue': 'City Arena',
            'date': '2025-09-15',
            'time': '2:00 PM - 11:00 PM',
            'capacity': 5000,
            'price': '$150',
            'image': 'https://images.unsplash.com/photo-1514525253161-7a46d19cd819?auto=format&fit=crop&w=400&q=80',
            'tags': ['Music', 'Festival', 'Entertainment'],
            'organizer': 'SoundWave Productions',
        },
    ]
    return render(request, 'events.html', {'events': events})
def space_detail_view(request):
    role = request.session.get('role', None)
    # Dummy data for spaces
    spaces = [
        {
            'name': 'Conference Room A',
            'location': 'First Floor',
            'capacity': 50,
            'image': 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80',
            'description': 'A modern conference room with projector and whiteboard.',
            'booked': False
        },
        {
            'name': 'Banquet Hall',
            'location': 'Second Floor',
            'capacity': 200,
            'image': 'https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80',
            'description': 'Spacious hall for weddings, parties, and large events.',
            'booked': True
        },
        {
            'name': 'Meeting Room 1',
            'location': 'Third Floor',
            'capacity': 20,
            'image': 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=400&q=80',
            'description': 'Cozy room for small team meetings.',
            'booked': False
        },
    ]
    space_name = request.GET.get('space', '')
    space = next((s for s in spaces if s['name'] == space_name), None)
    return render(request, 'space_detail.html', {'space': space, 'role': role})
from django.shortcuts import render, redirect


def home_view(request):
    return render(request, 'home.html')

def logout_view(request):
    # Clear all session data
    request.session.flush()
    return redirect('home-page')

def spaces_view(request):
    role = request.session.get('role', None)
    spaces = [
        {
            'name': 'Grand Ballroom',
            'location': 'Main Floor',
            'capacity': 500,
            'image': 'https://images.unsplash.com/photo-1519167758481-83f550bb49b3?auto=format&fit=crop&w=400&q=80',
            'description': 'Elegant ballroom with crystal chandeliers, perfect for weddings and galas.',
            'price_per_hour': 500,
            'amenities': ['Stage', 'Dance Floor', 'Professional Sound System', 'Lighting', 'Catering Kitchen'],
            'booked': False,
            'rating': 4.9,
            'reviews': 45,
        },
        {
            'name': 'Tech Hub Conference Center',
            'location': 'Innovation District',
            'capacity': 300,
            'image': 'https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=400&q=80',
            'description': 'Modern conference space with state-of-the-art AV equipment and breakout rooms.',
            'price_per_hour': 300,
            'amenities': ['4K Projectors', 'Video Conferencing', 'High-speed WiFi', 'Breakout Rooms', 'Tech Support'],
            'booked': True,
            'rating': 4.8,
            'reviews': 32,
        },
        {
            'name': 'Riverside Garden Pavilion',
            'location': 'Waterfront',
            'capacity': 200,
            'image': 'https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=400&q=80',
            'description': 'Beautiful outdoor venue with panoramic river views and covered areas.',
            'price_per_hour': 400,
            'amenities': ['Garden Setting', 'River View', 'Covered Pavilion', 'Outdoor Lighting', 'Parking'],
            'booked': False,
            'rating': 4.7,
            'reviews': 28,
        },
        {
            'name': 'Creative Studio Loft',
            'location': 'Arts District',
            'capacity': 100,
            'image': 'https://images.unsplash.com/photo-1497366672149-e5e4b4d34eb3?auto=format&fit=crop&w=400&q=80',
            'description': 'Industrial-chic loft space perfect for photo shoots and creative events.',
            'price_per_hour': 200,
            'amenities': ['Natural Light', 'Photography Equipment', 'Makeup Room', 'Props', 'Loading Dock'],
            'booked': True,
            'rating': 4.6,
            'reviews': 23,
        },
        {
            'name': 'Executive Boardroom',
            'location': 'Business Center',
            'capacity': 20,
            'image': 'https://images.unsplash.com/photo-1515378791036-0648a3ef77b2?auto=format&fit=crop&w=400&q=80',
            'description': 'Professional meeting space with executive amenities.',
            'price_per_hour': 150,
            'amenities': ['Video Conference System', 'Interactive Display', 'Coffee Service', 'Catering Available'],
            'booked': False,
            'rating': 4.8,
            'reviews': 15,
        }
    ]
    return render(request, 'spaces.html', {'spaces': spaces, 'role': role})

def bookings_view(request):
    role = request.session.get('role', None)
    bookings = [
        {
            'id': 'BK001',
            'space': 'Grand Ballroom',
            'date': '2025-08-15',
            'time': '6:00 PM - 11:00 PM',
            'purpose': 'Annual Charity Gala',
            'status': 'Confirmed',
            'attendees': 400,
            'total_cost': '$2,500',
            'amenities_requested': ['Catering', 'Sound System', 'Lighting', 'Valet Parking'],
            'organizer': 'City Foundation',
            'contact_email': 'events@cityfoundation.org'
        },
        {
            'id': 'BK002',
            'space': 'Tech Hub Conference Center',
            'date': '2025-08-20',
            'time': '9:00 AM - 5:00 PM',
            'purpose': 'Tech Summit 2025',
            'status': 'Confirmed',
            'attendees': 250,
            'total_cost': '$2,400',
            'amenities_requested': ['Video Conferencing', 'Tech Support', 'Catering', 'Recording'],
            'organizer': 'Tech Innovators Inc.',
            'contact_email': 'events@techinnovators.com'
        },
        {
            'id': 'BK003',
            'space': 'Riverside Garden Pavilion',
            'date': '2025-09-01',
            'time': '4:00 PM - 9:00 PM',
            'purpose': 'Wedding Ceremony & Reception',
            'status': 'Pending',
            'attendees': 150,
            'total_cost': '$2,000',
            'amenities_requested': ['Outdoor Lighting', 'Tent Setup', 'Catering Kitchen', 'Sound System'],
            'organizer': 'Sarah & James',
            'contact_email': 'sarah.james@email.com'
        },
        {
            'id': 'BK004',
            'space': 'Creative Studio Loft',
            'date': '2025-09-05',
            'time': '10:00 AM - 6:00 PM',
            'purpose': 'Fashion Photography Shoot',
            'status': 'Confirmed',
            'attendees': 25,
            'total_cost': '$1,600',
            'amenities_requested': ['Lighting Equipment', 'Makeup Room', 'Props', 'Catering'],
            'organizer': 'Style Magazine',
            'contact_email': 'productions@stylemagazine.com'
        },
        {
            'id': 'BK005',
            'space': 'Executive Boardroom',
            'date': '2025-09-10',
            'time': '1:00 PM - 5:00 PM',
            'purpose': 'Board Meeting',
            'status': 'Pending',
            'attendees': 15,
            'total_cost': '$600',
            'amenities_requested': ['Video Conference System', 'Coffee Service', 'Catering'],
            'organizer': 'Global Corp',
            'contact_email': 'admin@globalcorp.com'
        }
    ]
    selected_space = request.GET.get('space', '')
    return render(request, 'bookings.html', {'bookings': bookings, 'selected_space': selected_space, 'role': role})
