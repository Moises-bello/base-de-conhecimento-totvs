---
article_id: 14055857695511
category: SIGAEST - RELATORIOS
content_hash: 466c449150de0a109dfdba7500e4d72745a2c2410e31911621215660ed50c7bf
fetched_at: '2026-06-28T22:39:06.145540+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR390 - Relatório
  de Divergências é o relatório base para o Refaz Saldos? Qual a finalidade do Relatório?
type: support-article
updated_at: '2023-09-15T14:14:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14055857695511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR390-Relat%C3%B3rio-de-Diverg%C3%AAncias-%C3%A9-o-relat%C3%B3rio-base-para-o-Refaz-Saldos-Qual-a-finalidade-do-Relat%C3%B3rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17552235346327) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual a finalidade do Relatório de **Divergências de Estoque (MATR390)**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**A finalidade do relatório de **DIVERGÊNCIAS DE ESTOQUE (MATR390)** é apresentar se constam saldos errados no Estoque e pontualmente em qual produto, dessa forma permite processar a rotina **REFAZ SALDOS (MATA300)** especificamente para o produto apresentado no relatório.

Como sugestão, também é útil para os cenários em que o processamento da rotina REFAZ SALDOS é muito demorada, pode emitir esse relatório para processar a rotina REFAZ SALDOS apenas para os itens listados no MATR390.

***Observações importantes:*** Esse relatório **não exibe dados de saldos desbalanceados** entre as tabelas SB2xSBFxSB8, nesse caso, **deve utilizar o relatório MATR282**, **[clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF)** e veja a FAQ sobre esse cenário se for o caso.

Veja um exemplo simulado abaixo:

 ***- 1 -*** **Ao emitir o relatório para todos os produtos, apresenta um item com diferenças;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14056540472215)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14056242752151)

 ***- 2 -*** **Processar a rotina REFAZ SALDOS (MATA300) filtrando apenas o produto apresentado no relatório;**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14056783110807)

 ***- 3 -*** **Emitir o relatório novamente para todos os produtos ou apenas para o produto processado anteriormente na rotinas REFAZ SALDOS (MATA300). veja o resultado, o saldo foi ajustado e o relatório retorna sem dados.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14056959164055)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14056964544791)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre RELATÓRIOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)

[SIGAEST - Como descobrir a origem dos saldos na consulta com comando [F4] no Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto-)
