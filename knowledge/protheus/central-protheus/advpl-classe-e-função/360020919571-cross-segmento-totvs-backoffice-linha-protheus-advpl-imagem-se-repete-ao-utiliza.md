---
article_id: 360020919571
category: ADVPL - Classe e Função
content_hash: 3975a167174fcb5dfa0376a6d60d03d537cdc16223d539575e80f623a80c08e8
fetched_at: '2026-06-28T22:40:16.924349+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Imagem se repete
  ao utilizar o SmartClient Web
type: support-article
updated_at: '2022-01-03T20:32:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020919571-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Imagem-se-repete-ao-utilizar-o-SmartClient-Web
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao aplicar **CSS** em um botão customizado, a imagem se repetem por todo o objeto  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
**Causa**Esse erro está relacionado as propriedades do **CSS** e a interpretação do navegador

Por padrão(HTML e CSS), a imagem é inserida no canto superior esquerdo e repetida na vertical e na horizontal até que tenha preenchido 100% do corpo do elemento.   
  
**Solução**  
Podemos especificar que a imagem se repetirá em todos os eixos, apenas no horizontal, apenas no vertical ou não se repetirá.

```
background-repeat: no-repeat;
```

![KCS_CSS.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360017327871/KCS_CSS.gif)
