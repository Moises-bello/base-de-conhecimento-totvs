---
content_hash: f169fee5b0e58d6de24df21801ca40a566716366baf5df85276193e0f29526ad
fetched_at: '2026-06-29T00:10:21.803810+00:00'
page_id: '493646818'
product: rm
source: tdn-rm
title: 4053258 FISCAL01-6895 DT Carregar os tributos INSS e Funrural para o Item do
  lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493646818
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| Ticket: | 4053258 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Lançamento Fiscal |

## **02. SITUAÇÃO/REQUISITO**

Alterar o serviço de inclusão de lançamentos para que o tributo INSS e Funrural, quando estiverem parametrizados como Tributos Defaults da Natureza de Operação sejam carregados para os Tributos do Item e não mais para os Tributos do Lançamento durante o processo de inclusão manual.

## **03. SOLUÇÃO**

Inclusão automática do tributo INSS ou Funrural, quando estiverem parametrizados como Tributos Defaults da Natureza de Operação, nos Tributos do Item e não mais para os Tributos do Lançamento durante o processo de inclusão manual.

De forma que:

Base de cálculo: será o valor de mercadoria do item.

**Busca a alíquota e no Cadastro do INSS/PJ vinculado ao Cli/For do Lançamento Fiscal. Neste sentido, existindo registro cadastrado, o mesmo recuperará as informações:**

Alíquota ← Alíquota de Apuração do INSS

Serviços Especiais

15 anos de contribuição - Alíquota ← Alíquota adicional - 15 anos

20 anos de contribuição - Alíquota ← Alíquota adicional - 20 anos

25 anos de contribuição - Alíquota ← Alíquota adicional - 25 anos

Identificação

Identificador do INSS/PJ ← Identificador

Valor da Retenção ← Base x Alíquota

Valor Tributo ← Base x Alíquota

**Caso o registro de INSS/PJ não exista, as seguintes informações serão recuperadas do Cadastro do Tributo.**

Alíquota ← Alíquota (%)

Valor da Retenção ← Base x Alíquota

Valor Tributo ← Base x Alíquota

Identificador do INSS/PJ ← Código Receita

No caso do GILRAT, a alíquota só será recuperada caso o Cli/For não seja uma entidade executora de PAA.
