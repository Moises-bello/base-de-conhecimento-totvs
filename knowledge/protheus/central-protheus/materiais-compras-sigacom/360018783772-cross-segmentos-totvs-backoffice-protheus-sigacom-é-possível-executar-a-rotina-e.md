---
article_id: 360018783772
category: Materiais - Compras (SIGACOM)
content_hash: b1b2b0f846767e328ccb0ec78044c414b6c9a416795eac03940183de905a30ed
fetched_at: '2026-06-28T22:41:08.815956+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possível executar
  a rotina Eliminação de Resíduos (MATA235) de forma automática ?
type: support-article
updated_at: '2025-11-07T15:03:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018783772-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-executar-a-rotina-Elimina%C3%A7%C3%A3o-de-Res%C3%ADduos-MATA235-de-forma-autom%C3%A1tica
---

**Dúvida**

É possível executar a rotina Eliminação de Resíduos (MATA235) de forma automática ?  
  
**Ambiente**Microsiga Protheus – Compras – **A partir da versão 24.10 ou superiores**  
  
**Solução  
A rotina Eliminação de Resíduo - MATA235, não possui um execauto.**

**Porém há a possibilidade de ser executada via Smart Schedule. ( Execução em segundo plano ).**

ISSUE que implementou o processo:

**[MATA235 - Eliminação de resíduos - Execução em segundo plano](https://tdn.totvs.com/pages/viewpage.action?pageId=851288593)**

Para configurar e utilizar o Smart Schedule, veja documento abaixo :

**[Configuração Smart Schedule](https://tdn.totvs.com/display/public/framework/Schedule+Protheus)**

**<https://tdn.totvs.com/display/public/framework/tNewProcess>**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35629240504727)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35629240506519)**

Abaixo um exemplo do botão que será apresentado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35629194627607)

Em virtude do Smart Schedule ser uma funcionalidade pertencente ao framework., caso tenha dúvidas em seu configuração, a equipe deve ser acionada mediante ticket.

Este processo irá realizar a eliminação de resíduo de pedidos de compras, autorizações de entrega , contratos de parceria e solicitações de compras. Importante ressaltar que não existe a possibilidade de eliminar resíduo de cotações. Itens que estão em processo de Cotação não serão eliminados o resíduo pela rotina MATA235 , para não perder integridade e histórico com a cotação já gerada.

***Saiba Mais :***

[MP - SIGACOM - Pontos de Entrada para Eliminação de Resíduo (MATA235)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026070274)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
