---
article_id: 360047608493
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 159552ef8594688c601d018f9aba4968313c4e96a47835bd6c867d116bc4aab5
fetched_at: '2026-06-28T22:42:05.191722+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Error.log Unable to GetGlbVars on global variable assigned with PutGlbValue
type: support-article
updated_at: '2023-01-04T17:48:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047608493-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Error-log-Unable-to-GetGlbVars-on-global-variable-assigned-with-PutGlbValue
---

**Dúvida**  
Error.log Unable to GetGlbVars on global variable assigned with PutGlbValue  
  
 **Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Esse erro ocorre por motivo da rotina FISA008 Geração do Arquivo utilizar as funções GetGlbVars e PutGlbValue quando tem uma concorrência de threads usando a função glbvalue o erro é apresentado quando executado a função getglbvalue.

Esse cenário foi corrigido pela equipe de desenvolvimento e disponibilizado nas atualizações contidas de expedição continua contida no link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>
