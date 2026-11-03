---
article_id: 6923644526743
category: Financeiro - Contas a Pagar
content_hash: 0dfac83a7a1ce6aafb75c6b02f889b51da2f10bfbfbf824f1fc4afd689648cf2
fetched_at: '2026-06-28T22:38:09.725955+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Banco não
  aparece na configuração de Layout do Boleto
type: support-article
updated_at: '2025-05-29T21:16:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6923644526743-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Banco-n%C3%A3o-aparece-na-configura%C3%A7%C3%A3o-de-Layout-do-Boleto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32462713264919) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a configuração do Layout de Banco, o banco não está aparecendo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6923228152983)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o cadastro de bancos não contem a informação de Banco Oficial - **A6\_BCOOFI**  
  
**Solução**Verifique se o identificador está cadastrado no banco, caso não esteja se faz necessário informar o código no campo ( **A6\_BCOOFI** ) conforme código do banco. 

Saiba mais:   
[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=611007335)
