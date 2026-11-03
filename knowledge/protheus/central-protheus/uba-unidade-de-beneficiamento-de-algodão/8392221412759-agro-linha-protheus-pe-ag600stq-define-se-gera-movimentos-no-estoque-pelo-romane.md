---
article_id: 8392221412759
category: UBA - Unidade de Beneficiamento de Algodão
content_hash: 19fafa1d0b5088e72e930f06e9db2477a13bbe123d8dfcb6c6d30eb59b8b147d
fetched_at: '2026-06-28T22:45:35.568271+00:00'
product: protheus
section_id: 360005717853
source: central-protheus
title: Agro - Linha Protheus - PE AG600STQ - Define se gera movimentos no estoque
  pelo romaneio de entrada
type: support-article
updated_at: '2025-06-18T13:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8392221412759-Agro-Linha-Protheus-PE-AG600STQ-Define-se-gera-movimentos-no-estoque-pelo-romaneio-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21968508922263) Tempo aproximado para leitura: **00:00:40 min** **Dúvida**Qual o ponto de entrada que define se gera movimento no estoque?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - UBA - Unidade de Beneficiamento de Algodão - A partir da versão 12.1.17  
  
**Solução**O ponto de entrada **AG600STQ** esta disponível na rotina de **Romaneio de Entrada** - **AGRA600** nas opções de encerramento do romaneio de entrada e no cancelamento do romaneio de entrada, permitindo definir se as movimentações de estoque serão processadas pela rotina do romaneio de entrada.  
Por padrão as **movimentações de estoque** **são processadas pelo** **romaneio de entrada**, porém há cenários em que as movimentações não serão processadas no romaneio de entrada **mas sim por integração, exemplo PIMS**.  
O retorno do ponto de entrada **AG600STQ** deverá ser um valor lógico, verdadeiro **.T.** ou falso **.F.** sendo que se o valor for falso **.F.** as movimentações de estoque não serão processadas pelo romaneio de entrada.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8391912929303)
