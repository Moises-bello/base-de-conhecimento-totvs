---
article_id: 4411306792215
category: Financeiro - Contas a Pagar
content_hash: 5386339b01f19a7557ed3be0e4e6a4d09290803d6443dfcfda136363cc2617bc
fetched_at: '2026-06-28T22:38:08.403713+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento BackOffice Linha Protheus - FINA340 - HELP ADTXPED Adiantamento
  relacionado a um Pedido
type: support-article
updated_at: '2026-01-13T15:05:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411306792215-Cross-Segmento-BackOffice-Linha-Protheus-FINA340-HELP-ADTXPED-Adiantamento-relacionado-a-um-Pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37641276985495) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a compensação de um adiantamento, é apresentado o HELP **ADTXPED - Adiantamento relacionado a um pedido, somente poderá ser utilizado no relacionamento com pedidos**  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Esse incidente ocorre devido o Pagamento Antecipado estar atrelado a um pedido de compras onde não irá permitir a compensação manualmente pelo financeiro, pois a compensação automática ocorrerá quando uma nota de entrada foi incluída com este pedido de compras.   
  
**Solução**

Caso houver a necessidade de desvincular o PA do pedido para compensar, é possível retirando a seleção do PA na tela de adiantamento do Pedido em Outras Ações:

![PEDIDOPA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411311525783)

Caso do tipo:PA foi compensado de forma automática com o tipo:NF assim que for executado a rotina  "**MATA103 - Documento de Entrada**"  (MV\_CMPDEVV = .T.)  deixado um saldo parcial no título do tipo:PA, automaticamente o campo **FIE\_SALDO** da tabela **FIE** ficará zerado, permitindo que o restante do saldo do tipo:PA possa ser utilizado para compensar pela rotina "**FINA340 - Compensação Contas a pagar**"

**Saiba Mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA340 - Configuração dos parâmetros utilizados na Compensação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019492591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Configura%C3%A7%C3%A3o-dos-par%C3%A2metros-utilizados-na-Compensa%C3%A7%C3%A3o-)  
[MP - SIGACOM - Como Incluir ou Excluir o relacionamento do Pagamento Antecipado ( PA ) no Pedido de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015664151-MP-SIGACOM-Como-Incluir-ou-Excluir-o-relacionamento-do-Pagamento-Antecipado-PA-no-Pedido-de-Compras-)
