---
article_id: 360000050407
category: Escrita Fiscal - CIAP
content_hash: dad97875f6d0a50a4f07d0f761dc6df758438cf02b377235d09a89c2b8a53e91
fetched_at: '2026-06-28T22:39:33.807217+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - CIAP Valores dos
  Totais de Saídas e Saídas Tributadas
type: support-article
updated_at: '2021-07-29T13:06:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000050407-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-CIAP-Valores-dos-Totais-de-Sa%C3%ADdas-e-Sa%C3%ADdas-Tributadas
---

**Duvida:**

Os valores dos totais de saídas estão incorretos?

**Ambiente:**

Protheus - SIGAFIS - A partir da versão 12.1.17

**Solução:**

Os valores dos totais de saídas estão incorretos?

**1** **-** **Principais parâmetros e campos envolvidos:**

**\*****Parâmetros**

MV\_CIAPTOT

MV\_CIAPVER

MV\_CIAPCFO

MV\_P3CIAP

MV\_CIAPDEV

**\*Cadastro de TES:**

Campo: “Trib. CIAP” (F4\_CIAPTRB) - Considera as saídas tributadas quando o TES estiver configurado como OUTROS ou ISENTO para o cálculo do coeficiente de apropriação do CIAP.

**Solução/Análise:**

**2** **- A regra de composição dos valores, disponível em:**

[http://](http://tdn.totvs.com/pages/releaseview.action?pageId=51251109)[tdn.totvs.com/pages/releaseview.action?pageId=51251109](http://tdn.totvs.com/pages/releaseview.action?pageId=51251109)

Se mesmo com as informações do link acima restar alguma dúvida poderá executar a Query abaixo, assim avaliar as notas que o sistema está considerando.

**3** **- Query executada pela rotina MATA906 para compor os valores dos totais de saídas.**

**Obs.: Este processo de analisar a query deverá ser executado por um profissional capacitado.**

--Parâmetros:

--MV\_CIAPCFO = ' '

--MV\_CIAPVER = F

--MV\_CIAPTOT = F

--MV\_P3CIAP = F

--MV\_CIAPVST = ' '

SELECT D2\_EMISSAO,

D2\_TIPO,

D2\_TES,

D2\_CF,

D2\_DOC,

SUM(D2\_TOTAL) D2\_TOTAL, --(Campos de Total, Seguro, Frete, Despesas, IPI e ST influenciam no VALBRUT).

SUM(D2\_SEGURO) D2\_SEGURO,

SUM(D2\_VALFRE) D2\_VALFRE,

SUM(D2\_DESPESA) D2\_DESPESA,

SUM(D2\_VALIPI) D2\_VALIPI,

SUM(D2\_ICMSRET) D2\_ICMSRET,

SUM(D2\_BASEICM) D2\_BASEICM, -- Coluna "BASEICM" trará os valores do Total de Saídas Tributadas (Somar com Exportação).

SUM(D2\_VALBRUT) D2\_VALBRUT -- Coluna "VALBRUT" trará os valores do Total de Saídas.

FROM SD2990 AS SD2,

SF4990 AS SF4

WHERE D2\_FILIAL = '01'

AND D2\_EMISSAO BETWEEN '20160201' AND '20160229' -- Periodo para análise das notas.

AND D2\_TIPO <> 'I' -- Tipo da Nota deve ser diferente de "Complemento de IPI".

AND ( SD2.D2\_CF LIKE '5%' -- CFOP's iniciados em: "5, 6 e 7".

OR SD2.D2\_CF LIKE '6%'

OR SD2.D2\_CF LIKE '7%' )

AND SD2.D\_E\_L\_E\_T\_ = ' '

AND F4\_FILIAL = '01'

AND F4\_CODIGO = D2\_TES -- Verifica as TES utilizadas.

AND F4\_LFICM NOT IN ( 'N', 'Z' ) -- Desconsidera Livro de ICMS = "Não" e "Zerado".

AND F4\_PODER3 = 'N' -- Não controla Poder de Terceiros. ( Obs - Essa linha será incluída se o Parâmetro: MV\_P3CIAP = .F.)

AND SF4.D\_E\_L\_E\_T\_ = ' '

GROUP BY D2\_EMISSAO,

D2\_TIPO,

D2\_TES,

D2\_CF,

D2\_DOC -- Documento considerado.

ORDER BY D2\_EMISSAO
