---
article_id: 4421528636055
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: e512c01e04e43a05d61fd70abda4f1b8da5f4aeabd05f51dddaf10cad60036a6
fetched_at: '2026-06-28T22:39:36.797963+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - ERROR.LOG - type mismatch on
  compare  on FISXCOFINS(FISXCOFINS.PRW) line : 292'
type: support-article
updated_at: '2022-02-04T17:46:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421528636055-Cross-Segmentos-Backoffice-Protheus-FIS-ERROR-LOG-type-mismatch-on-compare-on-FISXCOFINS-FISXCOFINS-PRW-line-292
---

**Dúvida**

ERROR.LOG - type mismatch on compare on FISXCOFINS(FISXCOFINS.PRW) line : 292  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - a partir da versão 12  
  
**Solução**

Verificar para a Filial na qual esta realizando a operação existe os parâmetros abaixo:

**MV\_DEDBCOF, MV\_ICMDSDT, e MV\_DICMISE**

Caso não tenha deve incluir e configurar de acordo com sua necessidade:

**MV\_DEDBCOF**

**Finalidade: Para deduzir o ICMS na base do Pis/Cofins**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421545206935/mceclip0.png)

**Informação adicional :**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Valor de ICMS na Base de Cálculo do PIS COFINS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020917572-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Valor-de-ICMS-na-Base-de-C%C3%A1lculo-do-PIS-COFINS?source=search)

**MV\_ICMDSDT**

**Finalidade: Define a partir de que data os valores de ICMS deduzidos da base de PIS e COFINS serão apresentados no campo 08 do registro C170 da EFD Contribuições**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421551462039/mceclip1.png)

**Informação adicional:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=633335034>

**MV\_DICMISE**

**Finalidade :CST's de ICMS que não devem ser deduzidos da Base de Cálculo do PIS e COFINS.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421545227543/mceclip2.png)

**Informação adicional:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Dedução apenas do ICMS tributado da base de cálculo do PIS e COFINS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053374314-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Dedu%C3%A7%C3%A3o-apenas-do-ICMS-tributado-da-base-de-c%C3%A1lculo-do-PIS-e-COFINS?source=search)
