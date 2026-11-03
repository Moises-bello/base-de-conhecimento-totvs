---
article_id: 5727719097111
category: Financeiro - Baixas a Receber
content_hash: c746eeeda9dd6ff94a786d400c091ace3fab1165b50ea88e027fd375536d9820
fetched_at: '2026-06-28T22:37:43.781215+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA070 - Como realizar
  o cancelamento de baixa com correção monetária
type: support-article
updated_at: '2025-07-30T17:36:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5727719097111-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Como-realizar-o-cancelamento-de-baixa-com-corre%C3%A7%C3%A3o-monet%C3%A1ria
---

**Dúvida**É possível realizar o cancelamento/estorno de um lançamento de baixa com correção monetária pela rotina FINA070 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA070 - A partir da versão 12  
  
**Solução**No padrão não existe uma rotina de cancelamento/estorno para os lançamentos de variação monetária, apenas a exclusão do título, sendo assim, não será possível estorná-lo.

Deverá ser feito uma nova variação no dia em questão colocando a taxa correta, o sistema irá ajustar para o valor desejado, pois o **E5\_TIPODOC** **= CM** não movimenta saldos bancários.

**Saiba Mais**  
[Descrição E5\_TIPODOC](https://tdn.totvs.com/pages/releaseview.action?pageId=207357394)
