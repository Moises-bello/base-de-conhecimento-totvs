---
content_hash: c40f64d3b607c5d6927ac79a75330b5517a4554395609b8a3367092a00dd7852
fetched_at: '2026-06-29T00:08:49.313921+00:00'
page_id: '329036294'
product: rm
source: tdn-rm
title: DT Opção única para atualização de valores de acordo no lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=329036294
version: 98
---

# Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Parâmetros (Etapa 02.01.03.01)* | *Parâmetros.* | | Geração de Acordo | Geração de Acordo | |
| **Cadastros Iniciais:** | *Lançamentos* |
| **Requisito/S****tory/Issue:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-755> |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Oracle e SqlServer* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Criar uma opção única para atualização dos valores do acordo (juros, desconto e acréscimo) nos lançamentos de origem e/ou destino.

## Procedimento para Utilização

1. Foi criado o parâmetro "Detalhar valores do acordo (desconto, acréscimo, juros)", na etapa 02.01.03.01, com as seguintes opções:  
     
   * Lançamento origem: os valores do acordo (desconto, acréscimo, juros) serão gravados apenas no lançamento de origem.
   * Lançamento gerado: os valores do acordo (desconto, acréscimo, juros) serão gravados apenas no lançamento gerado por acordo.
   * Lançamento origem e gerado: os valores do acordo (desconto, acréscimo, juros) serão gravados em ambos os lançamento.
2. Foi criado um campo na tabela de acordo (FACORDO), onde será gravado a opção definida nos parâmetros no momento da geração do acordo. Com isso o comportamento ao cancelar/efetivar o acordo será realizado de acordo com o dado gravado no acordo.

**Importante:** No RM.Atualizador.exe será executado um script onde será atualizado o novo campo criado na tabela de acordo de acordo com a definição do parametrização existente no momento da conversão.

## Vídeo

600400

divs
