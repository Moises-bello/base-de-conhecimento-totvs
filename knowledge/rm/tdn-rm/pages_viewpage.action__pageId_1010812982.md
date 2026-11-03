---
content_hash: 8cd8cb1123887527fcdf201e42c6b70ace641304b99851eb27f4ce257d88446b
fetched_at: '2026-06-29T00:05:47.345418+00:00'
page_id: '1010812982'
product: rm
source: tdn-rm
title: DT - Crédito do Trabalhador - Cálculo conforme competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1010812982
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Crédito do Trabalhador - Cálculo conforme competência |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHCALCRM-9711](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-9711) |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2410.319
  + 12.1.2502.229
  + 12.1.2506.179
  + 12.1.2510.112
  + 12.1.2602 e superiores

## **03. SITUAÇÃO/REQUISITO**

O funcionário já quitou o empréstimo consignado modalidade crédito do trabalhador, mas ele ainda está sendo lançado na folha.  
Implementa no RM uma forma para que esse empréstimo quitado não seja mais considerado no cálculo da folha.

## **04. SOLUÇÃO**

Conforme [DT - Crédito Trabalhador - Novos campos na tabela de Importação do Crédito](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1010257226) foi implementado um campo específico para registrar a competência do arquivo de importação. A partir dessa alteração, o cálculo da folha de pagamento considera este novo campo para determinar a aplicação do desconto referente ao empréstimo na modalidade crédito do trabalhador.

O desconto somente deverá ser aplicado caso o campo de competência esteja preenchido e corresponda exatamente à competência da folha de pagamento em processamento.

Na rescisão também foi feito o tratamento e o desconto deve ser efetuado de acordo com a competência informada no novo campo.

Observação:

1. O Atualizador da base de dados deve ser executado para o cálculo considerar este novo campo para determinar a aplicação do desconto referente ao empréstimo na modalidade crédito do trabalhador.
2. Exceção para férias, a provisão deve ser realizada quando o novo campo corresponder ao mês das férias ou ao mês anterior.
IMPORTANTE:

**01 -** Ao executar o script para a criação do campo deve-se importar o arquivo para o correto preenchimento dessa competência.

Se este campo estiver nulo na base de dados e apresentando valor zerado na visão do cadastro de empréstimo, este valor do empréstimo não será lançado.

**Exemplo:**

No mês de Outubro de 2025 o funcionário quitou o empréstimo.

No inicio do mês de Novembro de 2025 foi executado o atualizador na base de dados criando os campos com valor NULL

* + **PFEMPRT.MESCOMPATUAL**
  + **PFEMPRT.ANOCOMPATUAL**

Ao importar o arquivo disponibilizado no Emprega Brasil e o nome desse funcionário não estará no arquivo de Novembro de 2025, então o campo continuará nulo para este funcionário.

Quando executado o lançamento do desconto do empréstimo, então este funcionário não terá o desconto em folha porque não estava presente no arquivo e com isso este campo não foi atualizado.

Atenção:

**Caso importar o arquivo do Emprega Brasil antes de atualizar a base de dados no mês que deve ter o desconto do empréstimo consignado deve-se importar novamente o arquivo para preenchimento correto destes campos mês e ano da competência atual, sob risco de não ser descontado nenhum dos empréstimos por estarem com o campo Nulo.**

**02 -** Estes campos de mês/ano competência do credito do trabalhador foram tratados no lançamento do desconto pelo Grupo de Eventos e na Rescisão, e também no provisionamento no Adiantamento e no cálculo do recibo de Férias. Se o evento de desconto for lançado diretamente no envelope de pagamento do funcionário será feito o cálculo sem considerar os campos de mês/ano competência do credito do trabalhador, ficando o controle por conta do usuário.

## **05. ASSUNTOS RELACIONADOS**

* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
* [DT - Crédito Trabalhador - Novos campos na tabela de Importação do Crédito](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1010257226)
