---
content_hash: 773b7ce4817359b366ff8260b2be9b0ca8e013bf9e8832377a96d1d612f03643
fetched_at: '2026-06-29T00:08:07.783909+00:00'
page_id: '237390020'
product: rm
source: tdn-rm
title: TGJ953_DT_Resumo_Tributos
type: documentation
url: https://tdn.totvs.com/display/LRM/TGJ953_DT_Resumo_Tributos
version: 117
---

**Resumo de Tributos - Considerar Redução no Cálculo do ICMS Próprio**

**Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Resumo de Tributos.* | MovResumoTributosItemForm | |
| **Cadastros Iniciais:** | *Natureza de Operação, Tributos, Movimento e Item de Movimento.* |
| **Parâmetro(s):** | *O tipo de Movimento deve estar parametrizado para trabalhar com ICMS-ST.* |
| **Ponto de Entrada:** | N/A |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *N/A* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *TTRBMOV, DNATUREZA e DREGRAICMS* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

O Objetivo desta implementação é, fazer com que a rotina responsável por exibir o resumo dos tributos do movimento considere o parâmetro "ICMS S.T. Considera Redução no Cálculo do ICMS Próprio”, contido nas regras de ICMS vinculadas a natureza de operação.

**Parametrização**

* Deverá ser selecionado o parâmetro "ICMS S.T. Considera Redução no Cálculo do ICMS Próprio" na Regra de ICMS-ST vinculado a natureza de operação do movimento.
* Deverá ser informado também o percentual de redução do ICMS S.T. "Redução Base ICMS S.T. / D.A. (%)".

Exemplo:

**Regra de Negócio:**

Na tela de edição do Movimento, ao clicar em "Resumo dos tributos dos Itens" o sistema exibe o extrato dos tributos de todos os itens de movimento, e caso exista o imposto ICMS-ST, uma linha é adicionada informando o valor do mesmo "VALOR ICMSST".

Exemplo:

Esta implementação consiste em alterar a forma do cálculo do "VALOR ICMSST", o mesmo passa a considerar o parâmetro "ICMS S.T. Considera Redução no Cálculo do ICMS Próprio". Com o parâmetro desmarcado o sistema continua se comportando da mesma forma, ou seja, não houve alterações, caso o parâmetro seja marcado,  o cálculo será realizado da seguinte forma:

Informações do Cálculo do ICMS Próprio  
Base de Cálculo Tributada - 1.000,00  
Alíquota – 12%  
Valor do ICMS – 120,00

Informações de Cálculo do ICMS ST  
Base de Cálculo ICMS ST – 1.150,00  
Percentual de Redução – 61.11%  
Alíquota ICMS ST – 18%

Cálculos  
Valor do ICMS Próprio = Base de Cálculo do ICMS – Percentual de Redução x Alíquota do ICMS ST

Valor ICMS Próprio = 70,00 => (1.000,00 – (61,11% = 388,90) x 18%)  
Valor do ICMS ST = 80,50 - 70,00 = 10,50

divs
