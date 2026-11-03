---
content_hash: 961f7f3ca0c39a01cd7b00cfc84d29162c55c406b22cf3a0ec57471ce1f7c7fe
fetched_at: '2026-06-29T00:06:11.286959+00:00'
page_id: '203767375'
product: rm
source: tdn-rm
title: TTGENR_Inclusao_Seg_Cod_Barras_MDFe
type: documentation
url: https://tdn.totvs.com/display/LRM/TTGENR_Inclusao_Seg_Cod_Barras_MDFe
version: 1
---

# NOME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Totvs Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MDF.003. | MDF-E - REJEIÇÃO | |
| **Chamados relacionados** | TTGENR |
| **Requisito (ISSUE):** | MOV000174 - Manifesto Eletrônico de Documentos Fiscais (MDF-e) |
| **Banco(s) de Dados:** | Sql Server e Oracle |
| **Tabelas utilizadas:** | TCTRC, TMDF-e |
| **Versões/Release:** | 12.1.6 e superiores |

## Descrição

Inclusão do Segundo Código de Barras para MDF-e quando o mesmo é vinculado a CT-e emitido em contingência.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.6 deste chamado

## Procedimento para Utilização

       1.            Preencha os dados de Contingência no registro da aba CTRC Saida do Movimento.

       2.            Informe uma chave de acesso contendo um CT-e enviado em contingência.

       3.            Envie o mdf-e e verifique que o campo SEGcodbarra será preencido.
