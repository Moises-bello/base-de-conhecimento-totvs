---
content_hash: a8797cadfa475ae0f7aeef2a31f0de90c79d1f0c96973fb59857545954661c4f
fetched_at: '2026-06-29T00:10:57.993415+00:00'
page_id: '602619084'
product: rm
source: tdn-rm
title: FISCAL01-14959 - DT Gerar o Evento R-2055 pelo BackOffice RM (Com tributo Discutido)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=602619084
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS BackOffice |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14959 |

## **02. SITUAÇÃO/REQUISITO**

Gerar o Evento R-2055 para considerar os tributos discutidos.

## **03. SOLUÇÃO**

No registro R-2055 dentro da TAG <detAquis> será gerada a TAG <infoProcJud> referente as informações processo judicial vinculado no lançamento.

Para gerar as informações do processo judicial é necessário ter um Processo Judicial vinculado ao Lançamento (este deve obedecer a geração do R-2055).

Neste Processo Judicial é necessário haver cadastrado Tributo Discutido do tipo FUNRURAL nos itens do Lançamento é necessário ter cadastrado o Tributo FUNRURAL.

A TAG <infoProcJud> possui os seguintes itens:

* nrProcJud -número do processo judicial cadastrado através do evento R-1070
* codSusp - Código do indicativo da suspensão atribuído pelo contribuinte. Este campo
* vlrCPNRet - Valor da contribuição previdenciária que deixou de ser retida pelo declarante em decorrência d e decisão/sentença judicial.
* vlrRatNRet - Valor da contribuição GILRAT incidente sobre a aquisição de produção rural de produtor rural, cuja retenção deixou de ser efetuada em decorrência de decisão/sentença judicial.
* vlrSenarNRet - Valor da contribuição destinada ao Senar, incidente sobre a aquisição de produção rural de produtor rural pessoa física/segurado especial, e que deixou de ser retida em decorrência de decisão/sentença judicial.

O que ocorre na geração da TAG <infoProcJud> desde que obedecido os requisitos anteriores:

1. Lançamento pode possuir um ou mais processos judiciais
   * Caso haja apenas um processo será gerada uma TAG <infoProcJud>;
   * Caso exista mais de um processo será gerada uma TAG <infoProcJud> para cada processo;
2. No Lançamento podem haver vários itens
   * Caso haja apenas um item e um processo vinculado será gerada apenas uma TAG <infoProcJud>
   * Caso exista mais de um item e todos estes itens possuem a flag de Isenção do Funrural **\*** marcada ou todos possuem a flag desmarcada e há apenas um processo vinculado será gerada uma TAG <infoProcJud> agrupando as informações do processo e somando os valores das TAGS <vlrCPNRet>, <vlrRatNRet> e <vlrSenarNRet>
   * Caso existam 3 itens, 2 possuem a flag marcada e o outro não, serão geradas duas TAGs <infoProcJud>
     + a primeira TAG <infoProcJud> será agrupada (os dois lançamentos com a flag marcada) e terá os valores das TAGs<vlrCPNRet>, <vlrRatNRet> e <vlrSenarNRet> somadas,
     + a segunda TAG <infoProcJud> terá seu valor respectivo da retenção do FUNRURAL n
   * A mesma situação pode ocorrer de forma inversa, ex.: 2 itens com flag desmarcada e 1 item com flag marcada

**\*** No cadastro do produto | Aba Detalhes | Aba Outros Dados | Flag Isento Funrural
