---
article_id: 360029026611
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: be090ac11c314462b459dc3e3f4e7c7726aefdeb1f5eb39757c36fa9c41b89fb
fetched_at: '2026-06-28T22:37:23.999602+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Parâmetro MV_CNFCOMP
  - Como validar para realizar medição somente na competência que está logado no sistema
  ?
type: support-article
updated_at: '2026-02-12T14:54:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029026611-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Par%C3%A2metro-MV-CNFCOMP-Como-validar-para-realizar-medi%C3%A7%C3%A3o-somente-na-compet%C3%AAncia-que-est%C3%A1-logado-no-sistema
---

**Dúvida**  
Parâmetro MV\_CNFCOMP - Como validar para realizar medição somente na competência que está logado no sistema ?

**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Solução**

Como impedir a realizacão da medicão de competências posteriores a data logada no sistema? Para poder apenas realizar medicão na competência atual a data logada?

**Resposta:**

Com o parâmetro MV\_CNFCOMP Habilitado conteúdo .T. só será possível efetuar a medição com a competência do mês de acesso da data base do sistema.

Segue exemplo com parâmetro habilitado.

Neste exemplo foi logado no sistema com a data 31/05/2019. Observe que só é possível selecionar a competência do mês 05.

***Medição(CNTA121)***

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029894332)

Para que possa realizar a medição com competência de outros meses desabilite o parâmetro preenchendo seu conteúdo .F.

Segue exemplo do mesmo contrato com parâmetro desabilitado, observe foi permitido selecionar a competência de outros meses.

***Medição CNTA121***

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029880911)

**IMPORTANTE:**

Esse parâmetro se aplica apenas a contratos **com Cronograma Financeiro**.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
