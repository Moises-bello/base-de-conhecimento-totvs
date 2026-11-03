---
article_id: 1500007693002
category: Financeiro - Contas a Pagar
content_hash: a43470ad558a0a9a0d2599f04719543adffc89d72d035d340050ea4574def939
fetched_at: '2026-06-28T22:38:07.230751+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN  - FINA050 - HELP: FIN050DDA'
type: support-article
updated_at: '2021-04-28T22:12:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007693002-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-HELP-FIN050DDA
---

**Ocorrência**No módulo Financeiro ao tentar excluir de um título a pagar, apresenta mensagem HELP: FIN050DDA![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011197521/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Esse incidente ocorre, pois o título a pagar teve uma conciliação DDA, portanto para que possa excluir a nota ou o título, será necessário efetuar o cancelamento da conciliação.  
  
Para efetuar o cancelamento, realize os seguintes passos:  
**1.** Acesse o módulo Financeiro e em Em “Atualizações/Comunic. Bancária/Conciliação DDA” (FINA260), posicione o cursor sobre um registro com legenda verde (conciliado). Clique na opção “Cancelar”.  
**2.** Serão apresentados os dados do registro DDA (tabela FIG) e do registro de Contas a Pagar (tabela SE2).  
**3.** Confira os dados e confirme.  
**4**. Realize a exclusão do Título a pagar

**Saiba mais**<https://tdn.totvs.com/display/public/PROT/FIN0001_DDA_DEBITO_DIRETO_AUTORIZADO>
