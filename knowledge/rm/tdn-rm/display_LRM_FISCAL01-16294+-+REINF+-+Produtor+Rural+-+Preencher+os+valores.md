---
content_hash: bdcaf1f5a4a7657115f5727740782b9f29416e5b0552d9a90731d8f45b306d0a
fetched_at: '2026-06-29T00:11:06.306889+00:00'
page_id: '633542647'
product: rm
source: tdn-rm
title: FISCAL01-16294 - REINF - Produtor Rural - Preencher os valores
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16294+-+REINF+-+Produtor+Rural+-+Preencher+os+valores
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16294 |

## **02. SITUAÇÃO/REQUISITO**

 Ao gerar o evento R-2055 as tags de <vlrCPDescPR> <vlrRatDescPR> <vlrSenarDescPR>, foram gerados com o valor zerado.

Mesmo com os campos GILTAT/SENAR preenchidos.

## **03. SOLUÇÃO.**

Implementamos o campo “Indicativo da opção pelo produtor rural pela forma de tributação da contribuição previdenciária**”** no Cadastro da Cli/For – Anexo – eSocial.

* Se o Campo igual a "**1 - Sobre a Comercialização da sua produção" ou "Vazio"**:

Então a Tag **<indOpcCP>** **não deve** ser gerada.

          {vlrBruto} com o valor bruto do Lançamento Fiscal;

          {vlrCPDescPR} com o valor real informado no Lançamento Fiscal;

          {vlrRatDescPR} com o valor real informado no Lançamento Fiscal;

         {vlrSenarDesc} com o valor real informado no Lançamento Fiscal.

* Se o Campo igual a **2 - Sobre a Folha de Pagamento:**

**Então a Tag **<indOpcCP>**  deve ser gerada.**

          {vlrBruto} com o valor bruto do Lançamento Fiscal;

          {vlrCPDescPR} com valor zero;

          {vlrRatDescPR} com valor zero;

          {vlrSenarDesc} com o valor real informado no Item do Lançamento Fiscal\Outros Tributos.
