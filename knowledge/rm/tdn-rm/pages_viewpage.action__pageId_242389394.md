---
content_hash: 6c6355f688150d4759afebc076130615d4a0d7b188c6e15495d6080a50a991ba
fetched_at: '2026-06-29T00:08:11.299238+00:00'
page_id: '242389394'
product: rm
source: tdn-rm
title: TVAWUB_DT_Não_Gerar_Tipo_Atendimento_DMED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242389394
version: 111
---

# Não gerar tipo de atendimento na DMED

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Utilitários | Gerar DMED | |
| **País(es):** | Brasil |

## Descrição

Criado parâmetro para informar os tipos de atendimentos que não devem aparecer no arquivo da DMED em Opções / Parâmetros / Parâmetros de integração Nucleos/ Aba Geral II, parâmetro “Não gera DMED para tipo de atendimento”.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações 12.1.12 da biblioteca do RM Saúde.

## Procedimento para Utilização

1. Acesse o menu **Opções / Parâmetros / Parâmetros de integração Nucleos**.
2. Aba Geral II e configure um tipo de atendimento no campo “Não gera DMED para tipo de atendimento”.
3. Em seguida, cadastre um registro de atendimento externo com o tipo de atendimento selecionado no passo anterior.
4. Encerre o atendimento e dê baixa no fluxus e nucleus.
5. Em seguida gere a DMED para o ano selecionado.
6. No arquivo não serão listados os atendimentos que possuem o tipo configurado no parâmetro.

divs
