---
content_hash: 92b01300c46dbac59639b2d885db99202b3eadcc9ea428631ff9534864b72bb5
fetched_at: '2026-06-29T00:10:45.882564+00:00'
page_id: '553346113'
product: rm
source: tdn-rm
title: FISCAL01-11504 DT EFD ICMS\IPI - Registro H030
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553346113
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Varejo Gestão Fiscal  TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Gerar arquivo EFD ICMS\IPI |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11504 |

## **02. SITUAÇÃO/REQUISITO**

Implementar a geração do registro H030 referente ao Ressarcimento do ICMS-ST da rotina EFD ICMS\IPI

## **03. SOLUÇÃO**

Implementação do registro H030 da rotina EFD ICMS\IPI.

Para geração do Registro H005 com motivo "06" e filhos automaticamente é necessário a rotina gerar os registros C180, C185 e C870 previamente.

* O H005 será gerado automaticamente com a **Data de Inventário** de 1 dia anterior ao da Data da rotina.

Exemplo: Sped gerado com data 01/01/2020 a 31/01/2020 a data de Inventário será 31/12/2020.

* Na geração do registro H010 foi consumido o serviço do Estoque selecionando somente os produtos que foram gerados nos registros "C180", "C185" e "C870".

Observação: No registro H010 é necessário informar a conta contábil do estoque e está deve ser informada em Parâmetros do Sped Fiscal\ aba Dados Inventário no campo "Código da Conta Contábil do Estoque".

* Para geração do H030 serão selecionados os itens dos lançamentos fiscais de Entrada e a quantidade e valores de tributos serão selecionados até atender a quantidade em Estoque, no período menor ou igual a data do inventário. Os lançamentos de saída com os itens que possuem referência de itens dos lançamentos de entrada não terão seus valores de ICMS e ICMS -ST totalizados como se estivessem no estoque. No registro H030 serão demonstrados os valores unitários ou seja **Valor do Imposto** divido pela **Quantidade** informada no H010.

Exemplo de Calculo:

Foi montando um cenário onde foi escolhido 1 produto “ABC” e feito toda sua movimentação de estoque com inclusão de movimentos que foram escriturados onde se forma o cenário abaixo do produto “ABC”.

Com a saída de 100 unidades do produto "ABC" no dia  o produto "ABC" ficou com apenas 150 unidades em estoque. Valor esperado do produto no registro registro H030 de acordo com sua movimentação até 29/02/2020 gerado na rotina de 01/03/2020 a 31/03/2020

Observação: Os valores da movimentação do dia 01/12/2018 foi proporcional a quantidade em estoque, para que os cálculos fiquem de forma correta.
