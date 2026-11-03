---
content_hash: 266189050a8a12185e9e502770e8b3fc168b0c84c00be050bb41daa473821e29
fetched_at: '2026-06-29T00:08:19.287818+00:00'
page_id: '266983419'
product: rm
source: tdn-rm
title: TVWKZC_DT_Gerar_Somente_BPA_Individual
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWKZC_DT_Gerar_Somente_BPA_Individual
version: 109
---

# Gerar BPA somente com atendimentos individualizados

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Faturamento SUS | Faturamento de BPA | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | ORACLE®, SQL SERVER® |
| **Tabelas Utilizadas:** | SZPARAMSUS |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado parâmetro para gerar o BPA somente com atendimentos individuais no arquivo de exportação para o programa BPA-Magnético.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.12.130 da biblioteca do RM.

## Procedimento para Utilização

1. Acesse o menu **Opções / Parâmetros / Parâmetros SUS / BPA** e marque a opção “**Prioriza BPA-Individual na geração do arquivo de exportação**”.
2. Cadastre um ou mais atendimento atendimentos externos para qualquer paciente com o convênio SUS.
3. Elabore o BPA para esses atendimentos.
4. Fature a BPA para esses atendimentos.
5. Verifique no arquivo de exportação se todos os atendimentos saíram como atendimento individualizados.

divs
