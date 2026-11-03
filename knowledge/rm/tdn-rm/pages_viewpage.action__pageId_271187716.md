---
content_hash: 7ca45b5bfe91e6cf886c16460f2f39c529132cee3cebe2faef1c190c7865a81e
fetched_at: '2026-06-29T00:08:26.646491+00:00'
page_id: '271187716'
product: rm
source: tdn-rm
title: ER SAUHRM02-590 Cronograma de Pagamento do Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271187716
version: 102
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS GESTÃO HOSPITALAR - RM | **Módulo** | Dados de Faturamento |
| **Segmento Executor** | Saúde | | |
| **Projeto** | SAUHRM02 | **IRM/EPIC** | SAUHRM02-596 |
| **Requisito/Story/Issue** | SAUHRM02-590 | **Subtarefa** | SAUHRM02-655 |
| **Chamado** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

## Objetivo

No cadastro de convênios, incluir novas opções de cálculo da data de vencimento da fatura

## Definição da Regra de Negócio

***RN001**- Criar parâmetro "Calcular faturamento à partir da data de entrega", para indicar  que o cálculo é feito para considerar a data de entrega ao invés da data de faturamento*

***RN002**- Incluir na opção “Tipo de entrega”, o  item “Intervalo de datas”, criando dois campos de data para armazenar o intervalo, com dia, mês e ano definidos para a data de entrega*

***RN003** - Incluir na opção “Tipo regra”, o item “Data específica”, e um campo de data para o mesmo, informando dia, mês e ano para o cálculo do pagamento*

****RN004** - Incluir no campo “Mês de controle”, a opção “Próximos meses” e criar um campo “Número de meses”, para a contagem do número de meses à frente**

******RN005** - Ao selecionar a opção "Intervalo de Datas" no Tipo de Entrega, a regra de recebimento deverá ser calculada através do Tipo de Regra "Data Específica"****

********RN006** - O campo "Número de meses" somente estará disponível quando estiver selecionada a opção "Meses á frente" do campo “Mês de controle”******

****RN007** - Incluir na rotina que calcula a data de vencimento da fatura o novo cálculo à partir da data de entrega, caso o parâmetro *"Calcular faturamento à partir da data de entrega" esteja selecionado***

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Convênio -> Dados de Faturamento | [Alteração] | [Cadastros -> Uso Geral -> Convênio] | RN001, RN002, RN003, RN004, RN005, RN006 |
| Faturamento | [Alteração] | [Faturamento] | RN007 |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
