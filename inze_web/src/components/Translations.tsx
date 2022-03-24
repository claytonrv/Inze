import { t } from 'i18next';
import { useTranslation } from 'react-i18next';

import BRFlag from "../assets/br_flag.png"
import USFlag from "../assets/us_flag.png"

import {TranslationButton, TranslationImage, TranslationButtonsWrapper, ChangeLanguageText} from '../style/components/Translationbuttons'

export default function Translations(){
    const { i18n } = useTranslation();

    function changeLanguage(language:string) {
        i18n.changeLanguage(language);
    }

    return(
        <TranslationButtonsWrapper>
            <ChangeLanguageText>{t('app.language')}</ChangeLanguageText>
            <TranslationButton onClick={() => changeLanguage('en-US')}>
                <TranslationImage src={USFlag} alt="English"/>
            </TranslationButton>
            <TranslationButton onClick={() => changeLanguage('pt-BR')}>
                <TranslationImage src={BRFlag} alt="Portuguese (BR)" />
            </TranslationButton>
        </TranslationButtonsWrapper>
  )
}