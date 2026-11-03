---
article_id: 40797788851223
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 24eeabc27d769ffe9d7db735a67338c790cd6edd4d128530f23c756ca85d10e5
fetched_at: '2026-06-28T22:39:15.717456+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular IBS/CBS
  para notas de serviço?
type: support-article
updated_at: '2026-05-28T15:11:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40797788851223-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-IBS-CBS-para-notas-de-servi%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788797335) Tempo aproximado para leitura: **10:00 min**  
  
**Dúvida**  
Como calcular IBS/CBS para notas de serviço com calculo do ISS?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2310  
  
**Solução**  
Para o cálculo do IBS e CBS em notas de serviço que contenha o cálculo do ISS no Configurador de Tributos, será necessário realizar a seguinte configuração:

Para o Cálculo do ISS pelo Configurador de Tributos, pode ser utilizada a seguinte configuração:

**Regra de Base de Cálculo:**

* **Cód. Regra (F27\_CODIGO)**: Mercad
* **Descrição (F27\_DESC)**: Valor da Mercadoria
* **Valor Origem (F27\_VALORI)**: 01 - Valor da Mercadoria

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741122199)

**Regra de Alíquota:**

* **Cód. Regra (F28\_CODIGO)**: 000001
* **Descrição (F28\_DESC)**: SERVICO
* **Valor Origem (F28\_VALORI)**: 04 - Alíquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 5,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788800407)

Regra de Escrituração:

* **Incidência (CJ2\_INCIDE):** 1 - Tributado
* **Total da Nota (CJ2\_STOTNF):** 1 - Sem Ação
* **Tabela CST (CJ2\_CSTCAB):** 000004 - CST DO ISS
* **CST (CJ2\_CST):** 01

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788800791)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741125015)

Cadastro dos Perfis devem ser ajustados conforme a necessidade, porém teria a obrigatoriedade de informar o Código de Serviço ISS que estiver preenchido no campo Cód. Serv. ISS (B1\_CODISS) no cadastro do Produto no Perfil de Operação, aba Código de Serviço:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788802839)

**Regra de Cálculo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788803351)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741126551)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741128471)

Para o calculo do IBS e CBS, pode ser realizanda a Carga do IBS/CBS no Configurador de Tributos, desta forma irá trazer a seguinte configuração:

Regra de Base de calculo do IBS/CBS

**Regra de Base de Cálculo:**

* **Cód. Regra (F27\_CODIGO)**: TB0001
* **Descrição (F27\_DESC)**: BASE DE CALCULO: CBS FED/IBS EST
* **Valor Origem (F27\_VALORI)**: 11 - Formula Manual
* Fórmula:   ( O:VAL\_MERCADORIA + O:FRETE + O:SEGURO + O:DESPESAS + O:VAL\_II ) - ( O:DESCONTO + O:VAL\_PS2 + O:VAL\_CF2 + O:VAL\_ICM\_TRIBUTADO + O:VAL\_DIFAL + O:VAL\_FECP + O:VAL\_FCPDIF + O:VAL\_ISS\_TRIBUTADO + O:VAL\_IPI\_TRIBUTADO )

**Regra de Alíquota:**

CBSFED:

* **Cód. Regra (F28\_CODIGO)**: TA0001
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.9%
* **Valor Origem (F28\_VALORI)**: 04 - Alíquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,90

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741130007)

IBSEST

* **Cód. Regra (F28\_CODIGO)**: TA0002
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.1%
* **Valor Origem (F28\_VALORI)**: 04 - Alíquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,10

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788809879)

IBSMUN

* **Cód. Regra (F28\_CODIGO)**: TA0002
* **Descrição (F28\_DESC)**: ALÍQUOTA 0.0%
* **Valor Origem (F28\_VALORI)**: 04 - Alíquota Informada Manualmente
* **Tp. Alíquota (F28\_TPALIQ)**: 1 - Percentual
* **Alíquota (F28\_ALIQ)**: 0,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788811927)

Documentação com instrução de como realizar a Carga automática do IBS/CBS:

* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como realizar carga automática dos Tributos CBS e IBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33147484988823-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-realizar-carga-autom%C3%A1tica-dos-Tributos-CBS-e-IBS-no-Configurador-de-Tributos)

A Regra de Escrituração não será importada junto com a Carga automática do IBS/CBS, sendo necessário a criação manual. Para esta ação, será necessário inicialmente realizar a importação do cClassTrib e IndOp, segue abaixo a documentação:

* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)
* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Importação da Tabela de Indicador de Operação (IndOp) no Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37485247428503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Importa%C3%A7%C3%A3o-da-Tabela-de-Indicador-de-Opera%C3%A7%C3%A3o-IndOp-no-Configurador-de-Tributos)

OBS: O arquivo CSV devem do cClassTrib e IndOp devem ser salvos no formato **CSV (separado por vírgulas)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788812951)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788813463)

**Regra de Cálculo do IBS e CBS:**

CBSFED:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788814103)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788815895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741128471)

IBSEST:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741133847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788815895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741128471)

IBSMUN:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788817175)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788815895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741128471)

Pedido de Venda:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788819735)

Gravação na CJ3 e F2D:

F2D:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788822679)

CJ3:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797741139223)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40797788824343)

**Documentações:**

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como calcular IBS/CBS cClasstrib 000001 na venda Hibrida ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36147453667095-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-IBS-CBS-cClasstrib-000001-na-venda-Hibrida)

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como calcular o ISS utilizando o Configurador de Tributos para notas de entrada e saída?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33675439757335-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-ISS-utilizando-o-Configurador-de-Tributos-para-notas-de-entrada-e-sa%C3%ADda)
