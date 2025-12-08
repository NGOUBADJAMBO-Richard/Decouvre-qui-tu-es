#!/usr/bin/env python3
import os
import re

navbar_pattern = r'<!-- Barre de menu -->[\s\S]*?<!-- End Navbar -->'

navbar_replacement = '''<!-- Barre de menu améliorée -->
      <nav
        class="bg-white shadow-sm sticky top-0 z-50 border-b border-gray-100"
        x-data="{ open: false }"
      >
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div class="relative flex h-16 items-center justify-between">
            <!-- Logo -->
            <div class="flex flex-shrink-0 items-center">
              <img
                class="h-10 w-auto"
                src="./logo/logo2.png"
                alt="Découvre qui tu es"
              />
            </div>

            <!-- Desktop Menu -->
            <div class="hidden sm:flex sm:items-center sm:space-x-1">
              <a
                href="index.html"
                class="rounded-lg px-4 py-2 text-sm font-medium text-white bg-[#2B6EF6] hover:bg-[#06B6D4] transition-colors duration-200"
              >
                Qui es-tu ?
              </a>
              <a
                href="propos.html"
                class="rounded-lg px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
              >
                Propos
              </a>
              <div class="relative group">
                <button
                  class="rounded-lg px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 transition-colors duration-200 flex items-center gap-1"
                >
                  Plus
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                  </svg>
                </button>
                <div class="absolute left-0 mt-0 w-48 rounded-lg shadow-lg bg-white border border-gray-100 opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-10">
                  <a href="test.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-[#2B6EF6] first:rounded-t-lg">
                    Faire des tests
                  </a>
                  <a href="ressources.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-[#2B6EF6]">
                    Ressources
                  </a>
                  <a href="langues.html" class="block px-4 py-2 text-sm text-gray-700 hover:bg-blue-50 hover:text-[#2B6EF6] last:rounded-b-lg">
                    Langues
                  </a>
                </div>
              </div>
              <a
                href="experiences.html"
                class="rounded-lg px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
              >
                Experiences
              </a>
              <a
                href="contact.html"
                class="rounded-lg px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
              >
                Contact
              </a>
              <a
                href="inscription.html"
                class="rounded-lg px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
              >
                S'inscrire
              </a>
            </div>

            <!-- Mobile menu button -->
            <div class="sm:hidden">
              <button
                @click="open = !open"
                type="button"
                class="inline-flex items-center justify-center rounded-lg p-2 text-gray-600 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
                aria-controls="mobile-menu"
                :aria-expanded="open"
              >
                <span class="sr-only">Menu principal</span>
                <svg x-show="!open" class="block h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                </svg>
                <svg x-show="open" class="hidden h-6 w-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- Mobile menu -->
        <div
          x-show="open"
          x-transition
          class="sm:hidden border-t border-gray-100 bg-white"
          id="mobile-menu"
        >
          <div class="space-y-1 px-4 pt-2 pb-3">
            <a
              href="index.html"
              class="block rounded-lg px-4 py-2 text-base font-medium text-white bg-[#2B6EF6] hover:bg-[#06B6D4] transition-colors duration-200"
            >
              Qui es-tu ?
            </a>
            <a
              href="propos.html"
              class="block rounded-lg px-4 py-2 text-base font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
            >
              Propos
            </a>
            <button
              @click="$el.nextElementSibling.classList.toggle('hidden')"
              class="w-full text-left block rounded-lg px-4 py-2 text-base font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
            >
              Plus
            </button>
            <div class="hidden pl-4 space-y-1">
              <a href="test.html" class="block rounded-lg px-4 py-2 text-sm text-gray-600 hover:bg-blue-50 hover:text-[#2B6EF6] transition-colors duration-200">
                Faire des tests
              </a>
              <a href="ressources.html" class="block rounded-lg px-4 py-2 text-sm text-gray-600 hover:bg-blue-50 hover:text-[#2B6EF6] transition-colors duration-200">
                Ressources
              </a>
              <a href="langues.html" class="block rounded-lg px-4 py-2 text-sm text-gray-600 hover:bg-blue-50 hover:text-[#2B6EF6] transition-colors duration-200">
                Langues
              </a>
            </div>
            <a
              href="experiences.html"
              class="block rounded-lg px-4 py-2 text-base font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
            >
              Experiences
            </a>
            <a
              href="contact.html"
              class="block rounded-lg px-4 py-2 text-base font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
            >
              Contact
            </a>
            <a
              href="inscription.html"
              class="block rounded-lg px-4 py-2 text-base font-medium text-gray-700 hover:bg-gray-100 hover:text-[#2B6EF6] transition-colors duration-200"
            >
              S'inscrire
            </a>
          </div>
        </div>
      </nav>
      <!-- End Navbar -->'''

directory = r"c:\Users\hp\Desktop\Projets_Sites_Web\Decouvre_qui_tu_es_2"
count = 0

for filename in os.listdir(directory):
    if filename.endswith(".html") and filename != "index.html":
        filepath = os.path.join(directory, filename)
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if "<!-- Barre de menu -->" in content:
                new_content = re.sub(navbar_pattern, navbar_replacement, content, flags=re.DOTALL)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✓ {filename}")
                count += 1
            else:
                print(f"⚠ {filename} - navbar non trouvée")
        except Exception as e:
            print(f"✗ {filename} - Erreur: {e}")

print(f"\n{count} fichiers mises à jour")
