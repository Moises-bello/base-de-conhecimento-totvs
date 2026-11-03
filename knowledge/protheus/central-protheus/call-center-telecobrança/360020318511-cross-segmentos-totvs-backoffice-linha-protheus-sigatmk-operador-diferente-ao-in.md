---
article_id: 360020318511
category: Call Center - Telecobrança
content_hash: 892aa58bc78a1236f935d1eb0c4524e19422b28e9e78d4d54a49561de2e6fedd
fetched_at: '2026-06-28T22:41:28.671872+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Operador diferente
  ao incluir Atendimento Telecobrança '
type: support-article
updated_at: '2022-06-22T17:32:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020318511-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Operador-diferente-ao-incluir-Atendimento-Telecobran%C3%A7a
---

**Dúvida**

Ao incluir um telecobrança no call center e informar o código do cliente, sistema atrela o atendimento a outro operador que não o operador logado, o que fazer ?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-a partir da versão 11.  
  
**Solução**

Esses casos ocorrem quando dentro da tabela **SK1**, ha títulos desse cliente amarados a esse Operador diferente, mesmo não possuindo atendimento em aberto.

Isso ocorre pois ao gerar uma **Lista de Cobrança** para o Operador você amarra todos os títulos da tabela SK1 daqueles clientes que estão na lista de cobrança com esse operador.

E mesmo excluindo a lista ou encerrando ela sem atendimento os títulos da SK1 permanecem amarados ao Operador.

Para tirar essa amarração necessário utilizar a rotina de **Transferência de Cobrança(tmka300).**
