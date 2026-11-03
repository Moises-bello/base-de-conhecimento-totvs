---
content_hash: 3cb1e4052eec9133760a2c52749bee7987f5e4b95e6f89884ecb4dd9e82ff08d
fetched_at: '2026-06-29T00:08:46.387068+00:00'
page_id: '317293362'
product: rm
source: tdn-rm
title: DT GoodData - Ficha Financeira por Centro de Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+GoodData+-+Ficha+Financeira+por+Centro+de+Custo
version: 94
---

# GOODDATA - FATO - FOLHA DE PAGAMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Integração - GoodData* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Processo do Plano de Extração* | **Processo do Plano de Extração** | |
| **Parâmetro(s):** | *"Levar ficha financeira do funcionário rateada por centro de custo (se houver)"* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | FOPROTINAS01-2268 |
| **País(es):** | *Brasil* |

## Descrição

Foi criado um parâmetro "Levar ficha financeira do funcionário rateada por centro de custo (se houver)" que leva as informações da folha de pagamento do funcionário rateada pelo centro de custo (PFMOVCC). Caso os eventos não tenham sido rateados, o comportamento normal de ler os dados da PFFINANC continua sendo executado.

## Procedimento para Configuração

*(Estes procedimentos devem ser feitos quando for necessário configurar parâmetros e/ou  rotinas no menu).*

**CONFIGURAÇÃO DE PARÂMETROS**

1. No módulo **Integração**, acesse o menu **Ferramentas | Parâmetros**. Dentro do item "50.08 - TOTVS Business Analytics" selecione o item "50.08.01 - Parâmetros Globais":
2. Em seguida habilite a checkbox **"Levar ficha financeira do funcionário rateada por centro de custo (se houver)"**:

divs
