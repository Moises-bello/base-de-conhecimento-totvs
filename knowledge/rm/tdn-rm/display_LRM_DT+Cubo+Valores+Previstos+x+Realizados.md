---
content_hash: ef2427c15812ac3da0c20fda068ecd3e7ba34bbaafff052d9e995e13ce6cfe6d
fetched_at: '2026-06-29T00:08:51.693872+00:00'
page_id: '337363240'
product: rm
source: tdn-rm
title: DT Cubo Valores Previstos x Realizados
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Cubo+Valores+Previstos+x+Realizados
version: 4
---

# Cubo Valores Previstos x Realizados - Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cubos | Cubos | | Valores Previstos x Realizados | Valores Previstos x Realizados | |
| **Cadastros Iniciais:** | *Lançamentos* |
| **Requisito/S****tory/Issue:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-4834> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Oracle e SqlServer* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Este cubo tem como objetivo visualizar valores previstos e realizados em um período determinado, sem apresentar a obrigatoriedade de utilizar uma natureza orçamentária financeira e o centro de custo, possibilitando uma visualização mais simples mediante alguns parâmetros.

## Procedimento para Implantação

* O arquivo "FINCUB0002 - Valores Previstos x Realizados" estará disponível na pasta Objetos Gerenciais / Cubos.

Para realizar a importação do mesmo, o usuário deve primeiramente  acessar o módulo "Inteligência de Negócios"

* Neste módulo, fazer a importação do Objeto Gerencial "FINCUB0002 - Valores Previstos x Realizados":

* Após importação, na visão de cubos, selecionar o cubo importado e clicar duas vezes no mesmo. Importante: O usuário que realiza a importação deverá ter seu perfil associado à categoria do cubo.  
  Obs.: O relatório estará disponível no Totvs Gestão Financeira no menu **Gestão | Ferramentas de Análise | Cubos.**

## Procedimento para Utilização

* Acessar o menu **Gestão | Ferramentas de Análise | Cubos.**

* Será apresentada a mensagem informando que o cubo ainda não foi atualizado. Clique em Sim para atualizar o cubo. Caso o cubo já esteja atualizado o mesmo será aberto.
* Após a abertura do cubo, o usuário poderá definir um filtro com os parâmetros abaixo:

* Coligadas - Informe as coligadas desejadas separando as mesmas por vírgula, por exemplo: 1,2,3,4
* Pagar/Receber - Para os lançamentos à receber deve ser informado “R”, para os lançamentos à pagar deve ser informado “P”. Se desejar gerar o cubo para ambos deve-se informar “PR”.
* Data Previsto - Informe a data que deseja realizar o filtro para cálculo dos valores no cubo.
* Data Vencimento Inicial - Informe a data de vencimento inicial que deseja realizar o filtro para cálculo dos valores no cubo.
* Data Vencimento Final - Informe a data de vencimento final que deseja realizar o filtro para cálculo dos valores no cubo.
* Considera Valor de Cheque Emitido – Informe “V” se deseja considerar o valor do cheque emitido no cálculo, e “F” se não deseja considerar.

**Obs.:**

O campo "Valor Previsto Vencimento" apresentará o valor do cálculo na data do vencimento do lançamento;   
O campo "Valor Data Previsto" apresentará o valor na data informada na tela.
