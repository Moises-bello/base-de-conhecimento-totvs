---
content_hash: 2bfa14aabb5046e5a97ac0b265b051d3a4f527e09e29c7422aa4f50ef6a8a910
fetched_at: '2026-06-29T00:06:28.816391+00:00'
page_id: '233762065'
product: rm
source: tdn-rm
title: TTVTMK_DT_Número_Remessa_Composto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=233762065
version: 119
---

# Número de Remessa Composto

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento | |
| **País:** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | SZPARAMCONV |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Realizada melhoria para possibilitar que o número da remessa seja único. O número do lote será composto por unidade de faturamento + código do convênio + sequencial da remessa.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. No **RM Saúde** nova MDI acesse **Cadastro / Condições Contratuais com o convênio / Aba Eletrônico III - TISS**.

|  |  |
| --- | --- |
| **Itens/Pastas** | **Descrição** |
| **Nome:** | Número de remessa composto |
| **Tipo:** | Boleano |
| **Cont. Por.:** | Falso |
| **Descrição:** | Concatena o ID da unidade de faturamento e ID do convênio ao número da remessa. |

## Procedimento para Utilização

**Exemplo:**

1. Em **RM Saúde** (nova MDI), acesse **Faturamento / Faturamento para Convênio.**
2. Clique em **Processos.**
3. Acesse **Faturamento de Convênio**;
4. Execute o processo;

divs
