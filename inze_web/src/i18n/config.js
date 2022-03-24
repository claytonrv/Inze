import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import { format as formatDate, isDate } from "date-fns";

// the translations
// (tip move them in a JSON file and import them,
// or even better, manage them separated from your code: https://react.i18next.com/guides/multiple-translation-files)
const resources = {
  "en-US": {
    translation: require('./locales/en-US.json')
  },
  "pt-BR": {
    translation: require('./locales/pt-BR.json')
  }
};

const locales = ['en-US', 'pt-BR']

i18n
  .use(initReactI18next) // passes i18n down to react-i18next
  .init({
    fallbackLng: 'en-US',
    resources,
    lng: "en-US", // language to use, more information here: https://www.i18next.com/overview/configuration-options#languages-namespaces-resources
    // you can use the i18n.changeLanguage function to change the language manually: https://www.i18next.com/overview/api#changelanguage
    // if you're using a language detector, do not define the lng option
    interpolation: {
      escapeValue: false, // react already safes from xss
        format: (value, rawFormat, lng) => {
          const [format, ...additionalValues] = rawFormat.split(',').map((v) => v.trim());
          console.log(additionalValues[0])
          switch(format){
            case 'currency': {
              return Intl.NumberFormat(lng, {
                style: 'currency',
                currency: additionalValues[0]
              }).format(value);
            }
            default: {
              if (isDate(value)) {
                const locale = locales[lng];
                return formatDate(value, rawFormat, { locale });
              }
            }
          }
      }
    },
  });

  i18n.languages = locales;
  

  export default i18n;