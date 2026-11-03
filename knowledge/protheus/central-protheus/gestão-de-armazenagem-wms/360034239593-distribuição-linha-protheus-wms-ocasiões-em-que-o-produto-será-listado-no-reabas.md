---
article_id: 360034239593
category: Gestão de Armazenagem (WMS)
content_hash: 629834dbd95d9c17e28a6604dfa2d56c4e2c5751ef5de199926480f210ac6b34
fetched_at: '2026-06-28T22:45:47.946127+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Distribuição - Linha Protheus - WMS - Ocasiões em que o produto será listado
  no reabastecimento preventivo
type: support-article
updated_at: '2024-07-24T13:57:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034239593-Distribui%C3%A7%C3%A3o-Linha-Protheus-WMS-Ocasi%C3%B5es-em-que-o-produto-ser%C3%A1-listado-no-reabastecimento-preventivo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25131384331543)***Tempo aproximado para leitura:**00:01:06 min**  
**Dúvida**Quais são as ocasiões em que o produto será listado no reabastecimento preventivo?  
  
**Ambiente**TOTVS Distribuição - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - A partir da versão 12  
  
**Solução**O **Reabastecimento Preventivo - WMSA100** não traz automaticamente os produtos que podem entrar no endereço, esta escolha deve ser manual.  
  
As ocasiões em que o produto será listado na rotina **WMSA100** são:  
  
- Quando o endereço de *picking* possuir um saldo menor que a capacidade do endereço, trará o produto para processar, conforme o percentual de reabastecimento indicado no parâmetro inicial;  
  
- Quando existir alguma movimentação pendente para o endereço de *picking*, como entrada prevista para o endereço, completará conforme o percentual de reabastecimento indicado no parâmetro inicial;  
  
- Quando for *picking* fixo, que é o caso em que o endereço só aceita o produto definido no cadastro de **Endereços - MATA015**, então não é preciso informá-lo.  
  
Outra situação diferente destas, informar manualmente o produto que reabastecerá o *picking*, por meio da opção **Alterar**, em **Outras Ações**.
