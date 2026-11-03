---
article_id: 360045913513
category: Escrita Fiscal - Impostos - ISS
content_hash: 6332dcf0e46ad143a6657698f13a73804d36050feed434b3bac2bbbcf4e24f28
fetched_at: '2026-06-28T22:39:35.251491+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS BackOffice Linha Protheus - FIS - Rotina FISA052 Para
  Notas Fiscais de Saída
type: support-article
updated_at: '2022-09-15T12:02:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045913513-CROSS-Segmentos-TOTVS-BackOffice-Linha-Protheus-FIS-Rotina-FISA052-Para-Notas-Fiscais-de-Sa%C3%ADda
---

**Dúvida**Como configurar a alíquota de ISS na rotina **FISA052** para notas fiscais de saída, de acordo o local de execução do serviço?

**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**Para configurar a alíquota de ISS pela rotina **FISA052** para notas ficais de saída, utilizando o local de execução do serviço, realize os seguintes passos;

1. Configure o **Parâmetros:** **MV\_ISSXMUN** = .T.;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360063260154/mceclip1.png)

2. Configure o **produto**, campo  **Exe. Serviço** **(B1\_MEPLES) = 2 LES;**

3. Configure a alíquota de **ISS** na rotina **FISA052**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064198373/mceclip0.png)

4. Realize o pedido de venda preenchendo os campos **UF PREST. (C5\_ESTPRES)** = SP, **Forn. ISS (C5\_FORNISS)** (Com o código do Fornecedor do ISS (Prefeitura) e **MUN PREST ( C5\_MUNPRES)** = 18800, informe o mesmo produto que foi cadastrado na rotina **FISA052;**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360064203633/mceclip2.png)Mais informações no link do tdn abaixo;

<https://tdn.totvs.com/pages/releaseview.action?pageId=654295834>
