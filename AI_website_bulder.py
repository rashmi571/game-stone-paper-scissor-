import React, { useState, useEffect } from 'react';
import { Wand2, Download, Eye, Loader2, Home, Info, Mail, HelpCircle, Menu, X, ArrowRight, MessageCircle, Send, Edit, Plus, Trash2, Clock, LayoutDashboard, Save, User, LogOut, LogIn } from 'lucide-react';

export default function AIWebsiteBuilder() {
  const [currentPage, setCurrentPage] = useState('home');
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [currentUser, setCurrentUser] = useState(null);
  const [showProfileMenu, setShowProfileMenu] = useState(false);
  
  const [formData, setFormData] = useState({
    businessName: '',
    businessType: '',
    description: '',
    colors: '',
    features: '',
    style: '',
    sections: []
  });
  const [generatedHTML, setGeneratedHTML] = useState('');
  const [loading, setLoading] = useState(false);
  const [showLivePreview, setShowLivePreview] = useState(false);
  const [savedWebsites, setSavedWebsites] = useState([]);
  const [editingId, setEditingId] = useState(null);
  
  const [newSectionName, setNewSectionName] = useState('');
  const [newSectionContent, setNewSectionContent] = useState('');
  
  const [chatMessages, setChatMessages] = useState([
    { role: 'assistant', content: 'Hello! I\'m here to help you with any questions about building your website. What would you like to know?' }
  ]);
  const [chatInput, setChatInput] = useState('');
  const [chatLoading, setChatLoading] = useState(false);

  useEffect(() => {
    const user = localStorage.getItem('aibuilder_user');
    if (user) {
      try {
        const userData = JSON.parse(user);
        setCurrentUser(userData);
        setIsAuthenticated(true);
        loadUserWebsites(userData.email);
      } catch (e) {
        console.error('Error loading user:', e);
      }
    }
  }, []);

  const loadUserWebsites = (userEmail) => {
    const allWebsites = localStorage.getItem('aibuilder_all_websites');
    if (allWebsites) {
      try {
        const websites = JSON.parse(allWebsites);
        const userWebsites = websites.filter(w => w.userEmail === userEmail);
        setSavedWebsites(userWebsites);
      } catch (e) {
        setSavedWebsites([]);
      }
    }
  };

  const saveAllWebsites = (websites) => {
    localStorage.setItem('aibuilder_all_websites', JSON.stringify(websites));
  };

  const handleLogin = (provider) => {
    const mockUser = {
      name: `Demo User (${provider})`,
      email: `demo@${provider}.com`,
      provider: provider,
      avatar: `https://ui-avatars.com/api/?name=${provider}&background=random`
    };
    
    localStorage.setItem('aibuilder_user', JSON.stringify(mockUser));
    setCurrentUser(mockUser);
    setIsAuthenticated(true);
    loadUserWebsites(mockUser.email);
    setCurrentPage('home');
  };

  const handleLogout = () => {
    localStorage.removeItem('aibuilder_user');
    setCurrentUser(null);
    setIsAuthenticated(false);
    setSavedWebsites([]);
    setCurrentPage('home');
    setShowProfileMenu(false);
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const addSection = () => {
    if (newSectionName.trim() && newSectionContent.trim()) {
      setFormData({
        ...formData,
        sections: [...formData.sections, { name: newSectionName, content: newSectionContent }]
      });
      setNewSectionName('');
      setNewSectionContent('');
    }
  };

  const removeSection = (index) => {
    setFormData({
      ...formData,
      sections: formData.sections.filter((_, i) => i !== index)
    });
  };

  const saveWebsite = () => {
    if (!isAuthenticated) {
      alert('Please login to save websites');
      return;
    }

    const allWebsites = JSON.parse(localStorage.getItem('aibuilder_all_websites') || '[]');
    
    const website = {
      id: editingId || Date.now(),
      ...formData,
      html: generatedHTML,
      userEmail: currentUser.email,
      userName: currentUser.name,
      createdAt: editingId ? savedWebsites.find(w => w.id === editingId)?.createdAt : new Date().toISOString(),
      updatedAt: new Date().toISOString()
    };

    let updatedWebsites;
    if (editingId) {
      updatedWebsites = allWebsites.map(w => w.id === editingId ? website : w);
    } else {
      updatedWebsites = [...allWebsites, website];
    }

    saveAllWebsites(updatedWebsites);
    loadUserWebsites(currentUser.email);
    alert('✅ Website saved successfully!');
  };

  const loadWebsite = (website) => {
    setFormData({
      businessName: website.businessName,
      businessType: website.businessType,
      description: website.description,
      colors: website.colors,
      features: website.features,
      style: website.style,
      sections: website.sections
    });
    setGeneratedHTML(website.html);
    setShowLivePreview(true);
    setEditingId(website.id);
    setCurrentPage('builder');
  };

  const deleteWebsite = (id) => {
    if (confirm('Are you sure you want to delete this website?')) {
      const allWebsites = JSON.parse(localStorage.getItem('aibuilder_all_websites') || '[]');
      const updatedWebsites = allWebsites.filter(w => w.id !== id);
      saveAllWebsites(updatedWebsites);
      loadUserWebsites(currentUser.email);
    }
  };

  const createNewWebsite = () => {
    if (!isAuthenticated) {
      alert('Please login to create websites');
      setCurrentPage('login');
      return;
    }
    
    setFormData({
      businessName: '',
      businessType: '',
      description: '',
      colors: '',
      features: '',
      style: '',
      sections: []
    });
    setGeneratedHTML('');
    setShowLivePreview(false);
    setEditingId(null);
    setCurrentPage('builder');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const generateWebsite = async () => {
    if (!isAuthenticated) {
      alert('Please login to generate websites');
      setCurrentPage('login');
      return;
    }

    setLoading(true);

    const sectionsText = formData.sections.map(s => `${s.name}: ${s.content}`).join('\n');

    const prompt = `Create a complete, professional, single-page HTML website with embedded CSS and JavaScript based on these requirements:

Business/Project Name: ${formData.businessName}
Type: ${formData.businessType}
Description: ${formData.description}
Preferred Colors: ${formData.colors || 'modern and professional'}
Features Needed: ${formData.features || 'standard sections'}
Style Preference: ${formData.style || 'modern and clean'}

SECTIONS/TABS TO INCLUDE:
${sectionsText || 'Include standard sections: Home, About, Services, Contact'}

Requirements:
- Create a fully functional, beautiful single-page website with navigation
- Include all sections/tabs specified above with the provided content
- Make navigation menu with smooth scrolling to each section
- Include all CSS styles in a <style> tag
- Include any JavaScript in a <script> tag
- Make it responsive and mobile-friendly
- Use modern design principles
- Add smooth animations and interactivity
- Make it production-ready

Return ONLY the complete HTML code, nothing else. No explanations, no markdown formatting, just pure HTML starting with <!DOCTYPE html>.`;

    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 4000,
          messages: [
            {
              role: 'user',
              content: prompt
            }
          ]
        })
      });

      const data = await response.json();
      const htmlCode = data.content
        .filter(block => block.type === 'text')
        .map(block => block.text)
        .join('\n');

      setGeneratedHTML(htmlCode);
      setShowLivePreview(true);
    } catch (error) {
      alert('Error generating website: ' + error.message);
    } finally {
      setLoading(false);
    }
  };

  const downloadHTML = () => {
    const blob = new Blob([generatedHTML], { type: 'text/html' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `${formData.businessName.replace(/\s+/g, '-').toLowerCase() || 'website'}.html`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  const sendChatMessage = async () => {
    if (!chatInput.trim()) return;

    const userMessage = chatInput;
    setChatInput('');
    setChatMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setChatLoading(true);

    try {
      const response = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 1000,
          messages: [
            {
              role: 'user',
              content: `You are a helpful assistant for an AI Website Builder platform. Help users with questions about building websites, web design, features, and troubleshooting. User question: ${userMessage}`
            }
          ]
        })
      });

      const data = await response.json();
      const assistantMessage = data.content
        .filter(block => block.type === 'text')
        .map(block => block.text)
        .join('\n');

      setChatMessages(prev => [...prev, { role: 'assistant', content: assistantMessage }]);
    } catch (error) {
      setChatMessages(prev => [...prev, { role: 'assistant', content: 'Sorry, I encountered an error. Please try again.' }]);
    } finally {
      setChatLoading(false);
    }
  };

  const navItems = [
    { id: 'home', label: 'Home', icon: Home },
    ...(isAuthenticated ? [{ id: 'dashboard', label: 'Dashboard', icon: LayoutDashboard }] : []),
    { id: 'about', label: 'About', icon: Info },
    { id: 'contact', label: 'Contact Us', icon: Mail },
    { id: 'help', label: 'Help', icon: HelpCircle }
  ];

  return (
    <div className="min-h-screen bg-gradient-to-br from-purple-50 via-white to-blue-50">
      <nav className="bg-white shadow-lg sticky top-0 z-50">
        <div className="max-w-7xl mx-auto px-4">
          <div className="flex justify-between items-center h-16">
            <div className="flex items-center gap-2">
              <Wand2 className="w-8 h-8 text-purple-600" />
              <span className="text-xl font-bold bg-gradient-to-r from-purple-600 to-blue-600 bg-clip-text text-transparent">
                AI Website Builder
              </span>
            </div>

            <div className="hidden md:flex items-center gap-1">
              {navItems.map(item => {
                const Icon = item.icon;
                return (
                  <button
                    key={item.id}
                    onClick={() => setCurrentPage(item.id)}
                    className={`flex items-center gap-2 px-4 py-2 rounded-lg transition ${
                      currentPage === item.id
                        ? 'bg-purple-600 text-white'
                        : 'text-gray-700 hover:bg-purple-50'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                    {item.label}
                  </button>
                );
              })}
              
              {isAuthenticated ? (
                <div className="relative ml-4">
                  <button
                    onClick={() => setShowProfileMenu(!showProfileMenu)}
                    className="flex items-center gap-2 px-4 py-2 rounded-lg bg-purple-100 hover:bg-purple-200 transition"
                  >
                    <img 
                      src={currentUser?.avatar} 
                      alt={currentUser?.name}
                      className="w-6 h-6 rounded-full"
                    />
                    <span className="font-semibold text-purple-900">{currentUser?.name}</span>
                  </button>
                  
                  {showProfileMenu && (
                    <div className="absolute right-0 mt-2 w-64 bg-white rounded-lg shadow-xl border border-gray-200 py-2">
                      <div className="px-4 py-3 border-b border-gray-200">
                        <p className="text-sm font-semibold text-gray-900">{currentUser?.name}</p>
                        <p className="text-xs text-gray-500">{currentUser?.email}</p>
                      </div>
                      <button
                        onClick={handleLogout}
                        className="w-full text-left px-4 py-2 text-red-600 hover:bg-red-50 transition flex items-center gap-2"
                      >
                        <LogOut className="w-4 h-4" />
                        Logout
                      </button>
                    </div>
                  )}
                </div>
              ) : (
                <button
                  onClick={() => setCurrentPage('login')}
                  className="ml-4 flex items-center gap-2 px-4 py-2 rounded-lg bg-gradient-to-r from-purple-600 to-blue-600 text-white hover:from-purple-700 hover:to-blue-700 transition"
                >
                  <LogIn className="w-4 h-4" />
                  Login
                </button>
              )}
            </div>

            <button
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              className="md:hidden p-2 text-gray-700"
            >
              {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
            </button>
          </div>

          {mobileMenuOpen && (
            <div className="md:hidden pb-4">
              {navItems.map(item => {
                const Icon = item.icon;
                return (
                  <button
                    key={item.id}
                    onClick={() => {
                      setCurrentPage(item.id);
                      setMobileMenuOpen(false);
                    }}
                    className={`flex items-center gap-2 w-full px-4 py-3 rounded-lg transition ${
                      currentPage === item.id
                        ? 'bg-purple-600 text-white'
                        : 'text-gray-700 hover:bg-purple-50'
                    }`}
                  >
                    <Icon className="w-4 h-4" />
                    {item.label}
                  </button>
                );
              })}
              
              {isAuthenticated ? (
                <>
                  <div className="px-4 py-3 mt-2 border-t border-gray-200">
                    <p className="text-sm font-semibold text-gray-900">{currentUser?.name}</p>
                    <p className="text-xs text-gray-500">{currentUser?.email}</p>
                  </div>
                  <button
                    onClick={() => {
                      handleLogout();
                      setMobileMenuOpen(false);
                    }}
                    className="w-full text-left px-4 py-3 text-red-600 hover:bg-red-50 transition flex items-center gap-2"
                  >
                    <LogOut className="w-4 h-4" />
                    Logout
                  </button>
                </>
              ) : (
                <button
                  onClick={() => {
                    setCurrentPage('login');
                    setMobileMenuOpen(false);
                  }}
                  className="w-full text-left px-4 py-3 bg-purple-600 text-white hover:bg-purple-700 transition flex items-center gap-2 mt-2 rounded-lg"
                >
                  <LogIn className="w-4 h-4" />
                  Login
                </button>
              )}
            </div>
          )}
        </div>
      </nav>

      <div className="max-w-7xl mx-auto px-4 py-8">
        {currentPage === 'login' && (
          <div className="min-h-[80vh] flex items-center justify-center">
            <div className="max-w-md w-full bg-white rounded-2xl shadow-2xl p-8">
              <div className="text-center mb-8">
                <Wand2 className="w-16 h-16 mx-auto mb-4 text-purple-600" />
                <h1 className="text-3xl font-bold text-gray-800 mb-2">Welcome Back!</h1>
                <p className="text-gray-600">Login to create and manage your websites</p>
              </div>

              <div className="space-y-4">
                <button
                  onClick={() => handleLogin('google')}
                  className="w-full flex items-center justify-center gap-3 px-6 py-4 border-2 border-gray-300 rounded-lg hover:border-purple-600 hover:bg-purple-50 transition group"
                >
                  <svg className="w-6 h-6" viewBox="0 0 24 24">
                    <path fill="#4285F4" d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z"/>
                    <path fill="#34A853" d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z"/>
                    <path fill="#FBBC05" d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z"/>
                    <path fill="#EA4335" d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z"/>
                  </svg>
                  <span className="font-semibold text-gray-700 group-hover:text-purple-600">Continue with Google</span>
                </button>

                <button
                  onClick={() => handleLogin('facebook')}
                  className="w-full flex items-center justify-center gap-3 px-6 py-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
                >
                  <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                  </svg>
                  <span className="font-semibold">Continue with Facebook</span>
                </button>

                <button
                  onClick={() => handleLogin('github')}
                  className="w-full flex items-center justify-center gap-3 px-6 py-4 bg-gray-900 text-white rounded-lg hover:bg-gray-800 transition"
                >
                  <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.840 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                  </svg>
                  <span className="font-semibold">Continue with GitHub</span>
                </button>
              </div>

              <p className="text-center text-sm text-gray-500 mt-8">
                By continuing, you agree to our Terms of Service and Privacy Policy
              </p>
            </div>
          </div>
        )}

        {currentPage === 'home' && (
          <div className="min-h-[80vh] flex flex-col items-center justify-center text-center py-12">
            <div className="max-w-4xl mx-auto">
              <h1 className="text-6xl md:text-7xl font-bold mb-6 bg-gradient-to-r from-purple-600 via-blue-600 to-purple-600 bg-clip-text text-transparent animate-pulse">
                Welcome to AI Builder
              </h1>
              <p className="text-2xl md:text-3xl text-gray-700 mb-8 font-light">
                Create stunning, professional websites in minutes with the power of artificial intelligence
              </p>
              <p className="text-lg text-gray-600 mb-12 max-w-2xl mx-auto">
                Just describe your vision, answer a few questions, and watch as AI brings your dream website to life. No coding knowledge required!
              </p>
              
              <button
                onClick={() => isAuthenticated ? setCurrentPage('builder') : setCurrentPage('login')}
                className="group bg-gradient-to-r from-purple-600 to-blue-600 text-white px-12 py-6 rounded-full text-xl font-semibold hover:from-purple-700 hover:to-blue-700 transition shadow-2xl hover:shadow-3xl transform hover:scale-105 flex items-center gap-3 mx-auto"
              >
                Create Your Website
                <ArrowRight className="w-6 h-6 group-hover:translate-x-1 transition" />
              </button>

              <div className="mt-16 flex flex-wrap justify-center gap-8 text-gray-600">
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
                  <span>Live Preview</span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-blue-500 rounded-full animate-pulse"></div>
                  <span>Edit & Save</span>
                </div>
                <div className="flex items-center gap-2">
                  <div className="w-3 h-3 bg-purple-500 rounded-full animate-pulse"></div>
                  <span>Dashboard</span>
                </div>
              </div>
            </div>
          </div>
        )}

        {currentPage === 'dashboard' && (
          <div>
            <div className="mb-8 flex justify-between items-center">
              <div>
                <h1 className="text-4xl font-bold text-gray-800 mb-2">Your Websites</h1>
                <p className="text-gray-600">Manage all your created websites in one place</p>
              </div>
              <button
                onClick={createNewWebsite}
                className="bg-gradient-to-r from-purple-600 to-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:from-purple-700 hover:to-blue-700 transition shadow-lg flex items-center gap-2"
              >
                <Plus className="w-5 h-5" />
                Create New
              </button>
            </div>

            {savedWebsites.length === 0 ? (
              <div className="bg-white rounded-2xl shadow-xl p-12 text-center">
                <LayoutDashboard className="w-16 h-16 mx-auto mb-4 text-gray-400" />
                <h3 className="text-2xl font-bold text-gray-800 mb-2">No websites yet</h3>
                <p className="text-gray-600 mb-6">Start creating your first website now!</p>
                <button
                  onClick={createNewWebsite}
                  className="bg-purple-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-purple-700 transition"
                >
                  Create Your First Website
                </button>
              </div>
            ) : (
              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                {savedWebsites.map(website => (
                  <div key={website.id} className="bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition">
                    <div className="bg-gradient-to-r from-purple-600 to-blue-600 p-4 text-white">
                      <h3 className="font-bold text-lg truncate">{website.businessName}</h3>
                      <p className="text-sm text-purple-100">{website.businessType}</p>
                    </div>
                    <div className="p-4">
                      <p className="text-sm text-gray-600 mb-3 line-clamp-2">{website.description}</p>
                      <div className="flex items-center gap-2 text-xs text-gray-500 mb-4">
                        <Clock className="w-3 h-3" />
                        <span>{new Date(website.updatedAt).toLocaleDateString()}</span>
                      </div>
                      <div className="flex gap-2">
                        <button
                          onClick={() => loadWebsite(website)}
                          className="flex-1 bg-blue-600 text-white px-3 py-2 rounded-lg hover:bg-blue-700 transition flex items-center justify-center gap-1 text-sm font-semibold"
                        >
                          <Edit className="w-4 h-4" />
                          Edit
                        </button>
                        <button
                          onClick={() => {
                            const newWindow = window.open('', '_blank');
                            if (newWindow) {
                              newWindow.document.open();
                              newWindow.document.write(website.html);
                              newWindow.document.close();
                            }
                          }}
                          className="flex-1 bg-green-600 text-white px-3 py-2 rounded-lg hover:bg-green-700 transition flex items-center justify-center gap-1 text-sm font-semibold"
                        >
                          <Eye className="w-4 h-4" />
                          View
                        </button>
                        <button
                          onClick={() => deleteWebsite(website.id)}
                          className="bg-red-600 text-white px-3 py-2 rounded-lg hover:bg-red-700 transition flex items-center justify-center"
                        >
                          <Trash2 className="w-4 h-4" />
                        </button>
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {currentPage === 'builder' && (
          <>
            <div className="text-center mb-8">
              <h1 className="text-4xl font-bold text-gray-800 mb-2">
                {editingId ? 'Edit Your Website' : 'Build Your Website'}
              </h1>
              <p className="text-gray-600">Answer a few questions and let AI create your perfect website</p>
            </div>

            <div className="grid lg:grid-cols-2 gap-8">
              <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
                <h2 className="text-2xl font-bold text-gray-800 mb-6">Website Details</h2>
                
                <div className="space-y-5">
                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">
                      Business/Project Name *
                    </label>
                    <input
                      type="text"
                      name="businessName"
                      value={formData.businessName}
                      onChange={handleChange}
                      placeholder="e.g., Acme Consulting"
                      className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">
                      Business Type *
                    </label>
                    <input
                      type="text"
                      name="businessType"
                      value={formData.businessType}
                      onChange={handleChange}
                      placeholder="e.g., Restaurant, Portfolio"
                      className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">
                      Description *
                    </label>
                    <textarea
                      name="description"
                      value={formData.description}
                      onChange={handleChange}
                      placeholder="Tell us about your business..."
                      rows="4"
                      className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition resize-none"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">
                      Preferred Colors
                    </label>
                    <input
                      type="text"
                      name="colors"
                      value={formData.colors}
                      onChange={handleChange}
                      placeholder="e.g., Blue and white"
                      className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">
                      Features Needed
                    </label>
                    <input
                      type="text"
                      name="features"
                      value={formData.features}
                      onChange={handleChange}
                      placeholder="e.g., Contact form, Gallery"
                      className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition"
                    />
                  </div>

                  <div>
                    <label className="block text-sm font-semibold text-gray-700 mb-2">
                      Style Preference
                    </label>
                    <input
                      type="text"
                      name="style"
                      value={formData.style}
                      onChange={handleChange}
                      placeholder="e.g., Modern and minimal"
                      className="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition"
                    />
                  </div>

                  <div className="border-t pt-6 mt-6">
                    <h3 className="text-xl font-bold text-gray-800 mb-4">Sections/Tabs</h3>
                    
                    {formData.sections.length > 0 && (
                      <div className="space-y-3 mb-4">
                        {formData.sections.map((section, index) => (
                          <div key={index} className="bg-purple-50 border border-purple-200 rounded-lg p-4">
                            <div className="flex justify-between items-start mb-2">
                              <h4 className="font-semibold text-purple-900">{section.name}</h4>
                              <button
                                onClick={() => removeSection(index)}
                                className="text-red-600 hover:text-red-700 text-sm font-semibold"
                              >
                                Remove
                              </button>
                            </div>
                            <p className="text-sm text-gray-700">{section.content}</p>
                          </div>
                        ))}
                      </div>
                    )}

                    <div className="bg-blue-50 border border-blue-200 rounded-lg p-4 space-y-3">
                      <input
                        type="text"
                        value={newSectionName}
                        onChange={(e) => setNewSectionName(e.target.value)}
                        placeholder="Section name (e.g., Home)"
                        className="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition"
                      />
                      <textarea
                        value={newSectionContent}
                        onChange={(e) => setNewSectionContent(e.target.value)}
                        placeholder="Content for this section..."
                        rows="3"
                        className="w-full px-4 py-2 rounded-lg border border-gray-300 focus:ring-2 focus:ring-blue-500 focus:border-transparent transition resize-none"
                      />
                      <button
                        onClick={addSection}
                        disabled={!newSectionName.trim() || !newSectionContent.trim()}
                        className="w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition disabled:opacity-50 flex items-center justify-center gap-2"
                      >
                        <Plus className="w-4 h-4" />
                        Add Section
                      </button>
                    </div>
                  </div>

                  <button
                    onClick={generateWebsite}
                    disabled={loading || !formData.businessName || !formData.businessType || !formData.description}
                    className="w-full bg-gradient-to-r from-purple-600 to-blue-600 text-white py-4 rounded-lg font-semibold hover:from-purple-700 hover:to-blue-700 transition disabled:opacity-50 flex items-center justify-center gap-2 shadow-lg mt-6"
                  >
                    {loading ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        Generating...
                      </>
                    ) : (
                      <>
                        <Wand2 className="w-5 h-5" />
                        {editingId ? 'Regenerate' : 'Generate Website'}
                      </>
                    )}
                  </button>
                </div>
              </div>

              <div className="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
                <div className="flex items-center justify-between mb-6">
                  <h2 className="text-2xl font-bold text-gray-800">Live Preview</h2>
                  {generatedHTML && (
                    <div className="flex gap-2">
                      <button
                        onClick={saveWebsite}
                        className="bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700 transition flex items-center gap-2 text-sm font-semibold"
                      >
                        <Save className="w-4 h-4" />
                        Save
                      </button>
                      <button
                        onClick={downloadHTML}
                        className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition flex items-center gap-2 text-sm font-semibold"
                      >
                        <Download className="w-4 h-4" />
                        Download
                      </button>
                    </div>
                  )}
                </div>

                {loading ? (
                  <div className="flex flex-col items-center justify-center h-[600px] bg-gradient-to-br from-purple-50 to-blue-50 rounded-lg border-2 border-purple-200">
                    <Loader2 className="w-16 h-16 animate-spin mb-4 text-purple-600" />
                    <p className="text-xl font-semibold text-gray-700 mb-2">Creating your website...</p>
                    <div className="space-y-2 text-sm text-gray-600 text-center">
                      <p>✨ Designing layout</p>
                      <p>🎨 Applying colors</p>
                      <p>📱 Mobile optimization</p>
                    </div>
                  </div>
                ) : showLivePreview && generatedHTML ? (
                  <div className="space-y-4">
                    <div className="border-2 border-gray-200 rounded-lg overflow-hidden shadow-lg">
                      <iframe
                        srcDoc={generatedHTML}
                        className="w-full h-[600px] border-0"
                        title="Live Preview"
                        sandbox="allow-scripts allow-forms allow-modals allow-popups allow-same-origin"
                      />
                    </div>
                    <button
                      onClick={() => {
                        if (generatedHTML) {
                          const newWindow = window.open('', '_blank');
                          if (newWindow) {
                            newWindow.document.open();
                            newWindow.document.write(generatedHTML);
                            newWindow.document.close();
                          }
                        }
                      }}
                      className="w-full bg-blue-600 text-white py-3 rounded-lg font-semibold hover:bg-blue-700 transition flex items-center justify-center gap-2"
                    >
                      <Eye className="w-5 h-5" />
                      Open in New Tab
                    </button>
                  </div>
                ) : (
                  <div className="flex flex-col items-center justify-center h-[600px] text-gray-400 bg-gray-50 rounded-lg">
                    <Eye className="w-16 h-16 mb-4" />
                    <p className="text-lg">Preview will appear here</p>
                  </div>
                )}
              </div>
            </div>
          </>
        )}

        {currentPage === 'about' && (
          <div className="max-w-3xl mx-auto">
            <div className="bg-white rounded-2xl shadow-xl p-8 md:p-12">
              <h1 className="text-4xl font-bold text-gray-800 mb-8">About AI Website Builder</h1>
              
              <div className="space-y-6 text-gray-700 text-lg">
                <div className="border-l-4 border-purple-600 pl-6">
                  <h2 className="text-2xl font-semibold text-gray-800 mb-2">Owner</h2>
                  <p className="text-xl">Rashmi</p>
                </div>

                <div className="border-l-4 border-blue-600 pl-6">
                  <h2 className="text-2xl font-semibold text-gray-800 mb-2">Launch Date</h2>
                  <p className="text-xl">January 15, 2026</p>
                </div>

                <div className="mt-8 pt-8 border-t border-gray-200">
                  <p className="text-gray-600 leading-relaxed">
                    AI Website Builder is a revolutionary platform designed to make website creation accessible to everyone.
                  </p>
                </div>
              </div>
            </div>
          </div>
        )}

        {currentPage === 'contact' && (
          <div className="max-w-2xl mx-auto">
            <div className="bg-white rounded-2xl shadow-xl p-8 md:p-12">
              <h1 className="text-4xl font-bold text-gray-800 mb-6">Contact Us</h1>
              
              <div className="bg-gradient-to-r from-purple-50 to-blue-50 rounded-xl p-8 mb-8 border border-purple-200">
                <div className="flex items-center gap-3 mb-4">
                  <Mail className="w-8 h-8 text-purple-600" />
                  <h2 className="text-2xl font-semibold text-gray-800">Email Us</h2>
                </div>
                <a 
                  href="mailto:r9793812@gmail.com" 
                  className="text-2xl font-semibold text-purple-600 hover:text-purple-700 transition underline"
                >
                  r9793812@gmail.com
                </a>
              </div>
            </div>
          </div>
        )}

        {currentPage === 'help' && (
          <div className="max-w-4xl mx-auto">
            <div className="bg-white rounded-2xl shadow-xl overflow-hidden">
              <div className="bg-gradient-to-r from-purple-600 to-blue-600 p-6">
                <div className="flex items-center gap-3 text-white">
                  <MessageCircle className="w-8 h-8" />
                  <div>
                    <h1 className="text-3xl font-bold">AI Help Assistant</h1>
                    <p className="text-purple-100">Ask me anything about building your website</p>
                  </div>
                </div>
              </div>

              <div className="h-[500px] overflow-y-auto p-6 bg-gray-50">
                {chatMessages.map((msg, idx) => (
                  <div
                    key={idx}
                    className={`mb-4 flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
                  >
                    <div
                      className={`max-w-[80%] rounded-2xl px-6 py-3 ${
                        msg.role === 'user'
                          ? 'bg-purple-600 text-white'
                          : 'bg-white text-gray-800 shadow-md border border-gray-200'
                      }`}
                    >
                      <p className="whitespace-pre-wrap">{msg.content}</p>
                    </div>
                  </div>
                ))}
                {chatLoading && (
                  <div className="flex justify-start mb-4">
                    <div className="bg-white text-gray-800 rounded-2xl px-6 py-3 shadow-md border border-gray-200">
                      <Loader2 className="w-5 h-5 animate-spin" />
                    </div>
                  </div>
                )}
              </div>

              <div className="p-6 bg-white border-t border-gray-200">
                <div className="flex gap-3">
                  <input
                    type="text"
                    value={chatInput}
                    onChange={(e) => setChatInput(e.target.value)}
                    onKeyPress={(e) => e.key === 'Enter' && sendChatMessage()}
                    placeholder="Ask me anything..."
                    className="flex-1 px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-purple-500 focus:border-transparent transition"
                  />
                  <button
                    onClick={sendChatMessage}
                    disabled={chatLoading || !chatInput.trim()}
                    className="bg-gradient-to-r from-purple-600 to-blue-600 text-white px-6 py-3 rounded-lg hover:from-purple-700 hover:to-blue-700 transition disabled:opacity-50 flex items-center gap-2"
                  >
                    <Send className="w-5 h-5" />
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}