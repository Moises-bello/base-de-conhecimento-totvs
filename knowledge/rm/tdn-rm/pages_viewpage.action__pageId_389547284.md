---
content_hash: 2a837ea43246fe23f91bcfd0b70afcd9e0d42dc5d8031e288d42ce1a30b81b11
fetched_at: '2026-06-29T00:09:08.455201+00:00'
page_id: '389547284'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-4932_DT_PARAMETRO_ENVIAR_VALORES_OPCIONAIS_NF_
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=389547284
version: 3
---

# CRIAÇÃO DE PARÂMETROS PARA ENVIAR VALORES OPCIONAIS DA PARCELA NAS NF-E

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | **Totvs Gestão de Estoque, Compras*.e Faturamento*. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *NF-e* | **NOTA FISCAL ELETRÔNICA** | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | Parametro Financeiros do Tipo de Movimento |
| **Ponto de Entrada:** | - |
| **Tickets relacionados** | MATFATCMPCRM01-4932 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-4932 |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | *SQLServer e Oracle.* |
| **Tabelas Utilizadas:** | - |
| **Sistema(s) Operacional(is):** | - |
| **Pacote:** | - |

## Descrição

Criação de parâmetros no tipo de movimento para identificar quais valores opcionais utilizados no tipo de movimento deverão ser considerados para cálculo do valor das parcelas da NF-e.

Assim, essa implementação permitira ao usuário determinar, entre os valores opcionais enviados para os valores opcionais nos lançamentos financeiros, quais devem ser adicionados às parcelas no envio da Nota Fiscal Eletrônica (nas parcelas incluídas na tag "pag" do XML da NF-e )

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações de uma das seguintes versões:

* 12.1.18.338 ou superiores
* 12.1.22 ou superiores

## Procedimento para Utilização

* Para parametrizar essa opção, deve acessar o **Totvs Gestão de Estoque, Compras e Faturamento → Ambiente → Gestão de Estoque Compras e Faturamento** e acessar os Parâmetros do Tipo de Movimento utilizado para envio da NF-e.
* Acessar a etapa **Fin - Faturamento 4/6** e verificar que existe a opção **Enviar Op NFe** em cada um dos Valores Opcionais.
* Além disso na etapa **Fin - Faturamento 5/6**, é importante definir como será a distribuição para cada Valor Opcional.
* Além disso, é importante definir qual a operação que será feita com o valor na parcela. Isso é feito acessando o **Totvs Gestão Financeira → Ambiente → TOTVS Gestão Financeira** e acessar a etapa **02.01.01.01 - Lançamento → Valores Opcionais.** Caso se selecione **Acrescentar**, o valor opcional correspondente será adicionado às parcelas selecionadas na Etapa**Fin - Faturamento 5/6**, descrita acima (na primeira, na ultima ou rateado entre todas). Caso se selecione**Descontar**, o valor opcional correspondente será subtraído às parcelas selecionadas na Etapa**Fin - Faturamento 5/6**, descrita acima (na primeira, na ultima ou rateado entre todas). Caso seja selecionado **Nada**, nenhum valor daquele valor opcional será adicionado a nenhuma parcela.
