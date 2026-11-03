---
content_hash: 6d25a69f0c72ae143c1e0605805772077a2c9d7cce0deedf4612621e9dd3a542
fetched_at: '2026-06-29T00:06:30.102260+00:00'
page_id: '235312693'
product: rm
source: tdn-rm
title: TULI91_DT_BASE_DE_CALCULO_DIFAL
type: documentation
url: https://tdn.totvs.com/display/LRM/TULI91_DT_BASE_DE_CALCULO_DIFAL
version: 2
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MOV.001 | INCLUSAO DE MOVIMENTO | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-.* |
| **Chamados Relacionados** | *TULI91, TTYHIN, TUMVAF, TUNZIA* |
| **Requisito (ISSUE):** | MOV000038 - Cálculo do movimento |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *-* |
| **Tabelas Utilizadas:** | *TMOV, TITMMOV,TTRBMOV* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Criado novo campo na tabela de tributos (TTRBMOV.BaseICMSDifAliq) para armazenar o calculo da Base de Calculo do Diferencial de Alíquota do ICMS.

As informações completas sobre a Legislação e a forma como o cálculo é realizado podem ser encontradas na página do  que implementou o cálculo em si.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.42.140 ou superior.*

*Também estará disponível nas versões 11.82.43 e 11.83*

## Procedimento para Utilização

       1.            Crie e salve um movimento.

       2.           O campo será calculado sempre que a Natureza do item de Movimento for uma natureza fiscal e o Tipo de Operação Tributária dessa natureza for igual a "Diferencial de Alíquota". Além disso deve haver os tributos ICMS e IPI para que o processo funcione.
