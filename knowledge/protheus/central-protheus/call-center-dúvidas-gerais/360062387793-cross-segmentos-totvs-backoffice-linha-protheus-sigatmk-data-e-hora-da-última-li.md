---
article_id: 360062387793
category: Call Center - Dúvidas Gerais
content_hash: fde2a53ec27fdda3c45c09e42e6312a92fd0b9e3a87ee0a837525b695fc852f9
fetched_at: '2026-06-28T22:41:26.980107+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK - Data e Hora da
  última ligação apresentadas no Rodapé do Atendimento
type: support-article
updated_at: '2022-06-17T19:21:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062387793-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Data-e-Hora-da-%C3%BAltima-liga%C3%A7%C3%A3o-apresentadas-no-Rodap%C3%A9-do-Atendimento
---

**Dúvida**De onde o sistema busca a informação da data e hora da última ligação apresentadas no rodapé do atendimento Call Center?  
  
**Ambiente**Cross Segmentos -TOTVS Backoffice (Linha Protheus)- SIGATMK – Call Center – A partir da versão 12  
  
**Solução**No rodapé do atendimento no módulo Call Center, o sistema apresenta a **data e a hora da última ligação** do cliente, baseando-se no **último** atendimento incluído para este **Código de Cliente e Loja**.

No caso do atendimento de Televendas, o sistema busca a data da ultima ligação do campo "**Data**" (**UA\_EMISSAO**) e a **hora** da ultima ligação do campo "**Termino Lig**." (**UA\_FIM**).
