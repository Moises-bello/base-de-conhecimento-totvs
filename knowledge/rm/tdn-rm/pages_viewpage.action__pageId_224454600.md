---
content_hash: 460882fbd97f77fff4d44dd4cc32d97efff72f58c09c325cc201eef5e84423f4
fetched_at: '2026-06-29T00:06:26.212846+00:00'
page_id: '224454600'
product: rm
source: tdn-rm
title: TUDAOC_DT_Impressao_de_Etiquetas_por_Número_Amostra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224454600
version: 121
---

# Impressão de etiquetas por número de amostra

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Opções | Parâmetros Gerais |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Atendimento | Registro de atendimento externo | | Unidade de Diagnóstico | Controle de pedido de exames | |
| **Parâmetro(s):** | Relatório de Impressão de Etiquetas de identificação do Material Biológico por número de amostra |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle, SQL Server |

## Descrição

Foi necessário possibilitar a impressão do relatório de etiquetas por número de amostra ao invés de imprimir por número do pedido. Realizada criação de parâmetro para que o usuário possa configurar um relatório de etiquetas por número de amostra.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.9.006 do RM Saúde.

## Procedimento para Utilização

Acesse o menu **Opções / Parâmetros / Parâmetros Gerais / Unidade de Diagnóstico** e selecione um relatório no parâmetro "**Relatório de Impressão de Etiquetas de identificação do Material Biológico por número de amostra**".

       Observação: O relatório deve ser criado pelo usuário e deve receber os parâmetros "CODCOLIGADA" e "NUMAMOSTRA".

Após a configuração, esse novo relatório será emitido todas as vezes que for solicitada a emissão de etiquetas de materiais biológicos nas tela de Registro de atendimento externo e controle de pedido de exames.

divs
