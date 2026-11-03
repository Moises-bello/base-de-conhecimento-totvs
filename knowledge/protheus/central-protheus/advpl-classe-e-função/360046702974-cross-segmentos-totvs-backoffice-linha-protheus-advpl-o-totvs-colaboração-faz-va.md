---
article_id: 360046702974
category: ADVPL - Classe e Função
content_hash: ce5ee742ed06322d456788c98b7e11e60798ae3b27fb79f2ad41fb691e600dbe
fetched_at: '2026-06-28T22:40:20.541996+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - O Totvs Colaboração
  faz validação na sefaz com os códigos de chaves
type: support-article
updated_at: '2022-06-01T18:15:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046702974-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-O-Totvs-Colabora%C3%A7%C3%A3o-faz-valida%C3%A7%C3%A3o-na-sefaz-com-os-c%C3%B3digos-de-chaves
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**O Totvs Colaboração faz validação na Sefaz com os códigos de chaves?  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**A validação é realizada previamente pela **Neogrid**, que valida o **XML** antes de ser encaminhado ao Protheus.   
Quando o **XML** está cancelado ou rejeitado na **Sefaz**, é encaminhado para o **Protheus**, porém não é importado para as tabelas do Colaboração (**SDS e SDT**).  
É importado apenas para que seja enviado um e-mail avisando que o **XML** está cancelado ou rejeitado.  
Agora se a **Neogrid** encaminhou um **XML** válido não haverá nova consulta a **SEFAZ** por parte do **Totvs Colaboração**. Não existe essa validação posterior.  
  
**Saiba mais**  
**[P12 - TOTVS Colaboração 2.0](https://tdn.totvs.com/pages/releaseview.action?pageId=187534008)**
