---
content_hash: baf9100ec574e75c4593b7d3be9d93847cf2d1017fcb09dc4c6e18f1cdaa0f11
fetched_at: '2026-06-29T00:06:28.178694+00:00'
page_id: '233750473'
product: rm
source: tdn-rm
title: TUBRFM_DT_Resultados_Online
type: documentation
url: https://tdn.totvs.com/display/LRM/TUBRFM_DT_Resultados_Online
version: 119
---

# Check Box Resultados Online Removido

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Prontuário Eletrônico | |
| **Parâmetro(s):** | Cadastros / Uso geral / Unidades de Atendimento, aba Outros dados, marcar parâmetro "Utiliza Resultados Online".  Opções / Parâmetros / Parâmetros Gerais, aba Unidade Diagnóstico II, marcar parâmetro "Disponibiliza Resultados Online" e informar um caminho a ser salvo os documentos. |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL SERVER e ORACLE |
| **Tabelas Utilizadas:** | SZUNIDATEND |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Ajuste para criar o pedido de exames com resultados online automaticamente conforme configuração da unidade de atendimento (se emite resultados online ou não). Dessa forma **o checkbox foi retirado** da tela de pedidos de exame via PEP.

## Procedimento para Utilização

1. Acesse o **Prontuário Eletrônico do Paciente** e selecione um paciente.
2. Acesse a aba "**Avaliações Complementares**" e clique em "**Solicitação de Exames**".
3. Informe exames que são realizados em uma unidade de atendimento que emite resultados online, por exemplo, exames de imagem.
4. Para verificar se o resultado será disponibilizado online acesse **Unidades Diagnóstico / Pedidos de Exame para Paciente Interno** (se paciente interno) ou apenas acesse o atendimento do paciente se este for externo.
5. Verifique que na aba "**Pedidos de Exame**" o checkbox "**Resultados Online**" estará marcado e uma senha para visualizá-los na internet foi gerada.

divs
