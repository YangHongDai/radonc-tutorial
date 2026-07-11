(function () {
  "use strict";

  var STORAGE_KEYS = [
    "radonc-language",
    "radonc_lang",
    "language",
    "lang"
  ];

  var currentLanguage = "zh";
  var isInitialised = false;

  function normaliseLanguage(value) {
    var language = String(value || "").toLowerCase();
    return language === "en" || language === "english" ? "en" : "zh";
  }

  function readStoredLanguage() {
    try {
      for (var i = 0; i < STORAGE_KEYS.length; i += 1) {
        var stored = localStorage.getItem(STORAGE_KEYS[i]);
        if (stored) {
          return normaliseLanguage(stored);
        }
      }
    } catch (error) {
      // Continue with the default language when storage is unavailable.
    }

    var rootLanguage =
      document.documentElement.getAttribute("lang") || "zh-TW";

    return rootLanguage.toLowerCase().indexOf("en") === 0 ? "en" : "zh";
  }

  function saveLanguage(language) {
    try {
      /*
       * Write both the current key and common legacy keys so old and new
       * pages remain synchronized.
       */
      STORAGE_KEYS.forEach(function (key) {
        localStorage.setItem(key, language);
      });
    } catch (error) {
      // The switcher still works when localStorage is unavailable.
    }
  }

  function setElementVisibility(element, shouldShow) {
    element.hidden = !shouldShow;
    element.style.display = shouldShow ? "" : "none";
    element.setAttribute("aria-hidden", shouldShow ? "false" : "true");
  }

  function updateBilingualText(language) {
    document.querySelectorAll("[data-zh][data-en]").forEach(function (element) {
      var value = element.getAttribute(
        language === "zh" ? "data-zh" : "data-en"
      );

      if (value !== null) {
        element.textContent = value;
      }
    });
  }

  function updateLanguageBlocks(language) {
    document.querySelectorAll("[data-lang]").forEach(function (element) {
      setElementVisibility(
        element,
        normaliseLanguage(element.getAttribute("data-lang")) === language
      );
    });

    /*
     * Backward compatibility for older generated pages that use classes
     * rather than data-lang attributes.
     */
    document.querySelectorAll(
      ".lang-zh, .zh-content, .content-zh, [data-language='zh']"
    ).forEach(function (element) {
      setElementVisibility(element, language === "zh");
    });

    document.querySelectorAll(
      ".lang-en, .en-content, .content-en, [data-language='en']"
    ).forEach(function (element) {
      setElementVisibility(element, language === "en");
    });
  }

  function updateButtons(language) {
    var buttons = document.querySelectorAll(
      "#lang-toggle, .lang-toggle, [data-lang-toggle]"
    );

    buttons.forEach(function (button) {
      button.textContent = language === "zh" ? "EN" : "中文";
      button.setAttribute(
        "aria-label",
        language === "zh" ? "Switch to English" : "切換至中文"
      );
      button.setAttribute("data-current-lang", language);
      button.setAttribute("type", button.getAttribute("type") || "button");
    });
  }

  function updateDocumentState(language) {
    var root = document.documentElement;

    root.lang = language === "en" ? "en" : "zh-TW";
    root.setAttribute("data-ui-lang", language);
    root.classList.remove("i18n-pending");

    document.body.classList.toggle("lang-zh", language === "zh");
    document.body.classList.toggle("lang-en", language === "en");
  }

  function applyLanguage(language, persist) {
    currentLanguage = normaliseLanguage(language);

    updateDocumentState(currentLanguage);
    updateBilingualText(currentLanguage);
    updateLanguageBlocks(currentLanguage);
    updateButtons(currentLanguage);

    if (persist !== false) {
      saveLanguage(currentLanguage);
    }

    document.dispatchEvent(
      new CustomEvent("languagechange", {
        detail: { language: currentLanguage }
      })
    );

    return currentLanguage;
  }

  function toggleLanguage() {
    return applyLanguage(
      currentLanguage === "zh" ? "en" : "zh",
      true
    );
  }

  function ensureLanguageButton() {
    if (
      document.querySelector(
        "#lang-toggle, .lang-toggle, [data-lang-toggle]"
      )
    ) {
      return;
    }

    var navInner = document.querySelector(".top-nav-inner");
    if (!navInner) {
      return;
    }

    var button = document.createElement("button");
    button.id = "lang-toggle";
    button.className = "lang-toggle";
    button.type = "button";
    button.setAttribute("data-lang-toggle", "");
    navInner.appendChild(button);
  }

  function ensureLiteratureNavLink() {
    document.querySelectorAll(".top-nav-links").forEach(function (navLinks) {
      if (navLinks.querySelector('a[href="literature/index.html"]')) {
        return;
      }

      var quizLink = navLinks.querySelector('a[href="radonc-quiz/index.html"]');
      var item = document.createElement("li");
      var link = document.createElement("a");

      link.href = "literature/index.html";
      link.setAttribute("data-zh", "📖 文獻");
      link.setAttribute("data-en", "📖 Literature");
      link.textContent = currentLanguage === "en" ? "📖 Literature" : "📖 文獻";

      item.appendChild(link);

      if (quizLink && quizLink.parentElement) {
        navLinks.insertBefore(item, quizLink.parentElement);
      } else {
        navLinks.appendChild(item);
      }
    });
  }

  function ensureBenignNavLink() {
    document.querySelectorAll(".top-nav-links").forEach(function (navLinks) {
      if (navLinks.querySelector('a[href="benign.html"]')) {
        return;
      }

      var palliativeLink = navLinks.querySelector('a[href="palliative.html"]');
      var quizLink = navLinks.querySelector('a[href="radonc-quiz/index.html"]');
      var item = document.createElement("li");
      var link = document.createElement("a");

      link.href = "benign.html";
      link.setAttribute("data-zh", "良性");
      link.setAttribute("data-en", "Benign");
      link.textContent = currentLanguage === "en" ? "Benign" : "良性";

      item.appendChild(link);

      if (palliativeLink && palliativeLink.parentElement) {
        palliativeLink.parentElement.insertAdjacentElement("afterend", item);
      } else if (quizLink && quizLink.parentElement) {
        navLinks.insertBefore(item, quizLink.parentElement);
      } else {
        navLinks.appendChild(item);
      }
    });
  }

  function bindLanguageButtons() {
    document.querySelectorAll(
      "#lang-toggle, .lang-toggle, [data-lang-toggle]"
    ).forEach(function (button) {
      /*
       * Do not add another listener when an older page already uses
       * onclick="toggleLang()", otherwise one click would toggle twice.
       */
      var inlineHandler = button.getAttribute("onclick") || "";
      if (/toggleLang|toggleLanguage/.test(inlineHandler)) {
        return;
      }

      if (button.dataset.i18nBound === "true") {
        return;
      }

      button.addEventListener("click", toggleLanguage);
      button.dataset.i18nBound = "true";
    });
  }

  function initialiseLanguage() {
    if (isInitialised) {
      return;
    }

    isInitialised = true;
    ensureBenignNavLink();
    ensureLiteratureNavLink();
    ensureLanguageButton();
    bindLanguageButtons();
    applyLanguage(readStoredLanguage(), false);
  }

  /*
   * Legacy global functions used by older cancer pages.
   */
  window.toggleLang = toggleLanguage;
  window.toggleLanguage = toggleLanguage;
  window.setLanguage = function (language) {
    return applyLanguage(language, true);
  };
  window.setLang = window.setLanguage;
  window.applyLanguage = function (language) {
    return applyLanguage(language, false);
  };
  window.getCurrentLanguage = function () {
    return currentLanguage;
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialiseLanguage);
  } else {
    initialiseLanguage();
  }
})();
