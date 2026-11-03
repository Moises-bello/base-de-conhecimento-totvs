---
article_id: 360020372631
category: Materiais - Compras (SIGACOM)
content_hash: d677793cad6fe84d12c21bfb4f33da1b97264ab04159ab2d5101b1ba98cfdd1d
fetched_at: '2026-06-28T22:41:07.457633+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao tentar excluir um
  documento de entrada de retorno pela MATA103  é apresentado o help A520NPODER.
type: support-article
updated_at: '2024-12-06T13:13:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020372631-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-tentar-excluir-um-documento-de-entrada-de-retorno-pela-MATA103-%C3%A9-apresentado-o-help-A520NPODER
---

**Dúvida**Ao tentar excluir um documento de entrada de retorno pela MATA103  é apresentado o help A520NPODER.

**Ambiente**  
Protheus – Compras – A partir da versão 12.1.17   
  
  
**Solução**  
Valide se existe a diferença de casas decimais conforme abaixo:

O sistema apresenta o help **A520NPODER**, pois o sistema esta efetuando a Comparação de campos, se sua estrutura esta exatamente igual.

Verifique em sua base o campo **B6\_QUANT** = exemplo se estiver com 3 Casas Decimais e o Campo **B6\_SALDO** = 2 Casas Decimais dá diferença.

Segue um exemplo em números:

**16358,454**  
**16358,45**

*Desta forma, se B6\_QUANT for diferente B6\_SALDO, sistema apresentará o help.*

*![KCS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016271351)*

*Com isso é necessário em sua base efetuar o acerto de de Casas Decimais equalizando os campos, para que sistema se comporte de forma esperada.*

***Saiba Mais:***

[Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
