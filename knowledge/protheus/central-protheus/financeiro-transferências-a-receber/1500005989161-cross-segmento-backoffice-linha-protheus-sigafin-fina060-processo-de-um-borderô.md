---
article_id: 1500005989161
category: Financeiro - Transferências a Receber
content_hash: f14b13745a263abdadcaa9021e1ade9df2b25a9be4679a54865070c1b8c6eb2d
fetched_at: '2026-06-28T22:37:42.957900+00:00'
product: protheus
section_id: 33829950145431
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA060 - Processo de
  um borderô de títulos carteira descontada
type: support-article
updated_at: '2026-05-21T11:01:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005989161-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA060-Processo-de-um-border%C3%B4-de-t%C3%ADtulos-carteira-descontada
---

**Dúvida**  
Processo de um borderô de títulos da carteira descontada?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Financeiro - Todas as versões  
  
**Solução**  
O processo é realizado pela rotina FINA060. Ao efetuar um borderô para cobrança com a situação = **2 - Cobrança Descontada**, o sistema utiliza o banco para efetuar a transferência do título.

Nesta modalidade, a instituição financeira antecipa o crédito na conta da empresa correntista, deduzindo previamente as taxas de desconto negociadas. A partir desse momento, o banco passa a ser o credor do título.

No entanto, a empresa cedente atua como corresponsável pela dívida. Caso o cliente final fique inadimplente e não pague o título no vencimento, a empresa deverá ressarcir a instituição financeira.

No Protheus, ao transferir o título para esse tipo de situação, o campo de situação será atualizado para “Cobrança Descontada” **(E1\_SITUACA = 2)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40633821448087)

Após clicar em “OK” para confirmar a transferência, deverão ser informadas a taxa de desconto e a taxa de IOF aplicadas pela instituição financeira.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40633869380887)

O crédito do valor líquido poderá ser realizado no momento da transferência ou posteriormente, por meio de uma baixa. Para definir esse comportamento, acesse o parâmetro pelo F12 e configure a opção **“Baixar Tit. Descont.?”** como **“Sim”** ou **“Não”.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40633821451671)

No exemplo a seguir, o parâmetro está configurado como **“Sim”**, realizando a baixa do título e preenchendo o campo portador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40633869382295)

**Importante**

A operação somente será permitida caso não exista cheque não devolvido vinculado ao título.

**Saiba mais**  
[Transferências - FINA060 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=271405699)
