---
article_id: 22740964083607
category: Materiais - Compras (SIGACOM)
content_hash: 3a6e946a5a2c054d808b8a119f51c088234fec05ea38b386e5418aa93f271e47
fetched_at: '2026-06-28T22:41:18.976635+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP- SN1MASTER N1_LOJA
  REGNOIS em Nota de Entrada do Tipo Devolução com Ativo
type: support-article
updated_at: '2024-04-11T19:28:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22740964083607-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-SN1MASTER-N1-LOJA-REGNOIS-em-Nota-de-Entrada-do-Tipo-Devolu%C3%A7%C3%A3o-com-Ativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22740937016343) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**  
HELP- SN1MASTER N1\_LOJA REGNOIS em Nota de Entrada do Tipo Devolução com Ativo  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

Por padrão, operações envolvendo a saída de um ativo pelo módulo de Faturamento e clientes, não geram movimentações dentro desse ativo no módulo 01.  
Logo, mesmo que a saída tenha sido utilizado um TES movimentando ativo para um cliente, este ativo não foi movimentado, e por consequência a sua entrada/devolução também não movimentará.  
Por padrão no Documento de Entrada só alimentamos o ativo através das notas de compras, envolvendo fornecedores.

Ajuste o campo F4\_ATUATF para **Não,** para realização de um novo Teste.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22740964048535)

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - HELP SN1MASTER VLDDATA\_OBRIGAT N3\_XXXX OU N1\_XXXX na nota de entrada com ativo fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006565012-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-SN1MASTER-VLDDATA-OBRIGAT-N3-XXXX-OU-N1-XXXX-na-nota-de-entrada-com-ativo-fixo?source=search)

[Ponto de Entrada ATFA006102 - Gravação do Ativo Fixo](http://tdn.totvs.com/pages/releaseview.action?pageId=6085761)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
