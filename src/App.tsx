import { useEffect, useRef } from 'react';
import { gsap } from 'gsap';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import RepositoryInput from './components/RepositoryInput';
import './App.css';

function App() {
  const mainRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (mainRef.current) {
      const q = gsap.utils.selector(mainRef.current);

      gsap.fromTo(q('.hero-title'),
        { y: 50, opacity: 0 },
        { y: 0, opacity: 1, duration: 1, ease: 'power3.out', delay: 0.2 }
      );

      gsap.fromTo(q('.hero-description'),
        { y: 30, opacity: 0 },
        { y: 0, opacity: 1, duration: 1, ease: 'power3.out', delay: 0.4 }
      );

      gsap.fromTo(q('.badge'),
        { scale: 0.8, opacity: 0 },
        { scale: 1, opacity: 1, duration: 0.8, ease: 'back.out(1.7)', delay: 0.6 }
      );

      gsap.fromTo(q('.meadow-card'),
        { y: 100, opacity: 0 },
        { y: 0, opacity: 1, duration: 1.2, ease: 'power4.out', delay: 0.8 }
      );
    }
  }, []);

  return (
    <main className="app-container" ref={mainRef}>
      <Navbar />
      <Hero />
      <RepositoryInput />
    </main>
  );
}

export default App;
