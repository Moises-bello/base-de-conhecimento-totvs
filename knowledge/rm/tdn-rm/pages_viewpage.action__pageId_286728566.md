---
content_hash: 216f8936fc6f5b742be378e1300596305f41c807a99193210894cf321520dcca
fetched_at: '2026-06-29T00:08:41.458334+00:00'
page_id: '286728566'
product: rm
source: tdn-rm
title: 1109471 MSAU-12644 DT Lançamento de Guia de Solicitação de Internação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286728566
version: 106
---

# Lançamento de guia de solicitação de internação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Atendimento | Registro de internação | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |

## Descrição

Realizado ajuste para incluir uma guia de solicitação de internação quando for incluir uma guia de resumo de internação que não possua solicitação de autorização lançada.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.16.26 do RM Saúde.

## Procedimento para Utilização

1. Acesse o registro de internação de qualquer paciente;
2. Na aba "Guias/Autorização", cadastre uma guia de resumo de internação;
3. Ao salvar o registro, o sistema vai verificar se já existe uma guia de autorização de internação com o mesmo número da guia de resumo, e caso não exista, o sistema vai incluir automaticamente a guia de solicitação.

divs
