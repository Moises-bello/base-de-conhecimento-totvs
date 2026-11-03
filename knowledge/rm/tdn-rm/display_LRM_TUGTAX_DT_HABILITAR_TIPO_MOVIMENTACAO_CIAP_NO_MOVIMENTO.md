---
content_hash: e3e0673bb8555e509d5f4a6a0e1bfec14d8e0afc5c3f937f764720d17955e8d6
fetched_at: '2026-06-29T00:06:28.542106+00:00'
page_id: '233754290'
product: rm
source: tdn-rm
title: TUGTAX_DT_HABILITAR_TIPO_MOVIMENTACAO_CIAP_NO_MOVIMENTO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUGTAX_DT_HABILITAR_TIPO_MOVIMENTACAO_CIAP_NO_MOVIMENTO
version: 117
---

# ME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=219695506) |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | PAR.014 | PARAMETRIZACAO - TIPO DE MOVIMENTO. | |
| **Chamados Relacionados** | TUGTAX |
| **Requisito (ISSUE):** | MOV000003 - Movimento |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Tabelas Utilizadas:** | *TITMMOVFISCAL* |

## Descrição

Implementação do campo "Tipo Movimentação CIAP" no Tipo de Movimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado.

1. Aplique o patch do chamado 11.82.42.133 ou superior.

## Procedimento para Utilização

O campo será habilitado com as seguintes parametrizações:

1) Nos parâmetros fiscais da Filial, marque a opção "Controla Ativo permanente"

2) Ainda nos parâmetros fiscais da Filial, marque o Tipo do livro como diferente de "ISS / Outros"

3) Na natureza de operação vinculada ao item de Movimento deve estar marcada a opção "Ativo Imobilizado" no grupo "Tipo Operação"

Caso essa opção "Ativo imobilizado" não esteja marcada, o campo também será exibido caso a Natureza de operação seja 6.600 ou  6.603

4 ) Após essas parametrizações, verifique a aba fiscal do item de Movimento e verifique o campo "Tipo de Movimentação do Bem ou Componente".

divs
