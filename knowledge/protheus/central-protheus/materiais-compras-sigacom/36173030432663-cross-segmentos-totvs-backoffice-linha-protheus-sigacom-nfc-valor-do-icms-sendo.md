---
article_id: 36173030432663
category: Materiais - Compras (SIGACOM)
content_hash: 3b1c4b4939aa7479369e9565eec8e22db837ea93b96f51e25c136bc6cb8b7526
fetched_at: '2026-06-28T22:41:12.807722+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Linha Protheus - SIGACOM - NFC - Valor do
  ICMS sendo somado no valor total da Cotação incorretamente
type: support-article
updated_at: '2025-12-29T19:26:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36173030432663-Cross-Segmentos-Totvs-Backoffice-Linha-Protheus-SIGACOM-NFC-Valor-do-ICMS-sendo-somado-no-valor-total-da-Cota%C3%A7%C3%A3o-incorretamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36172967974423) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
No Novo Fluxo de Compras, valor do ICMS está sendo somado no valor total da Cotação incorretamente. Como corrigir essa ocorrência.  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
Realmente, o valor do ICMS não deve ser acrescido no valor total da cotação no Novo Fluxo de Compras. Apenas os valores dos impostos**IPI (C8\_VALIPI)**e **ICMS Solidário (C8\_VALSOL)** serão somados no valor total da cotação.

Os impostos **ICMS, ICMS Complementar, ISS e ICMS DIFAL**não serão incluídos nem descontados do Valor Total da Cotação, ou seja, eles não farão parte da composição do valor total da Cotação. Se trata do conceito de funcionamento da rotina. O valor desses impostos serão preenchidos **apenas a título de conhecimento**, não surtirá efeito no valor total da cotação.

Para solucionar esta ocorrência, é necessário aplicar o pacote abaixo. Aplique inicialmente em base de teste / homologação e efetue todos os devidos backups corretamente.

12.1.2410:<https://r.totvs.io/p/1221957> ;

12.1.2510:<https://r.totvs.io/p/1221958> ;

***Saiba Mais:***

[DMANMAT02-53639 DT NFC Implementar a apresentação dos tributos CBS / IBS na tela de análise da cotação](https://tdn.totvs.com/pages/viewpage.action?pageId=981002683)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como incluir ou deduzir o valor dos impostos no total da Cotação no NFC?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35791880461463-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-incluir-ou-deduzir-o-valor-dos-impostos-no-total-da-Cota%C3%A7%C3%A3o-no-NFC)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
