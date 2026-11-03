---
content_hash: 0f6d1af573eae09f6e6d2db4997e5af7f6899e2cee3f060957c8ed7fa524dc8b
fetched_at: '2026-06-28T21:35:28.731014+00:00'
page_id: '684328571'
product: fluig
source: tdn-fluig
title: Temas
type: documentation
url: https://tdn.totvs.com/display/fluig/Temas
version: 5
---

# Índice

trueÍndicenone

Este guia visa orientar os desenvolvedores a como obter que está em uso no TOTVS Fluig Plataforma. Hoje temos 3 formas de obter o tema selecionado em sua empresa. Via **CSS**, via **FTL** e via **JavaScript**.

### **Obtendo o tema via CSS**

---

Hoje, no Fluig Plataforma, será adicionado sempre na tag <body> da página, o código do tema selecionado como uma classe, conforme exemplo abaixo:

Com essa classe sendo aplicada no body, você pode construir o seu CSS como no exemplo abaixo:

### Obtendo o tema via FTL

---

Também é possível obter o tema via FTL através da variável freemarker `*${fluigThemeCode}*` com o código do tema selecionado, como no exemplo abaixo:

Recomendamos que seja feita essa validação para garantir que o código funcione corretamente.

Dessa forma, a variável `*${fluigThemeCode}*` será preenchida com o código do tema selecionado, permitindo que seja utilizada da forma que o desenvolvedor preferir.

### Obtendo o tema via JavaScript

---

Para obter o tema selecionado via JavaScript, é necessário acessar uma API Rest que retorna o código do tema, como no exemplo abaixo:

### Variáveis CSS do tema responsivo

---

As variáveis CSS abaixo são exportadas **somente pelo tema responsivo**. Nos demais temas **não é possível obter essas variáveis**.

Hoje, no tema responsivo, é exportado diversas variáveis CSS para auxiliar na construção do tema da sua empresa.

* Para maiores informações sobre Variáveis CSS, acesse o link de referência: <https://developer.mozilla.org/pt-BR/docs/Web/CSS/Using_CSS_custom_properties>

### Descrição das variáveis

---

| Variável | Descrição |
| --- | --- |
| --themeResponsiveBgColor | Hexadecimal da cor de fundo da página |
| --themeResponsiveBgContrastColor | Hexadecimal da cor contrastante da cor de fundo da página |
| --themeResponsiveMenuBgColor | Hexadecimal da cor de fundo do menu |
| --themeResponsiveMenuBgHoverColor | Hexadecimal da cor de hover dos itens de menu |
| --themeResponsiveMenuActiveColor | Hexadecimal da cor do menu ativo |
| --themeResponsiveMenuActionColor | Hexadecimal da cor do menu de ação |
| --themeResponsiveHeaderBgColor | Hexadecimal da cor de fundo do header |
| --themeResponsiveHeaderActionColor | Hexadecimal da cor das ações no header |
| --themeResponsiveBrandColor | Hexadecimal da cor da marca da empresa |
| --themeResponsiveBgImage | Url da imagem de fundo da página |
| --themeResponsiveHeaderBgImage | Url da imagem de fundo do header |
| --themeResponsiveBgImageRepeat | Propriedade com a informação se a imagem de fundo da página irá se repetir (repeat | no-repeat) |
| --themeResponsiveBgImageCover | Propriedade com a informação se a imagem de fundo da página irá ocupar o espaço todo disponível (cover | unset) |
| --themeResponsiveHeaderBgImageRepeat | Propriedade com a informação se a imagem de fundo do header irá se repetir (repeat | no-repeat) |
| --themeResponsiveHeaderBgImageCover | Propriedade com a informação se a imagem de fundo do header irá ocupar o espaço todo disponível (cover | unset) |

### Como utilizar as variáveis em meu desenvolvimento

---

Para utilizar essas variáveis CSS, pode ser usado o exemplo abaixo:
