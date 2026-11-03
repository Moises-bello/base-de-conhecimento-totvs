---
content_hash: e9a686bde943a817d812dcd9171f9b9fc5150d667cef5fc33c1527ecec637e03
fetched_at: '2026-06-29T00:08:27.545917+00:00'
page_id: '271415631'
product: rm
source: tdn-rm
title: 119017 MCP-1036 DT Faturamento de Medições do Item de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271415631
version: 111
---

# FATURAMENTO DE MEDIÇÕES DO ITEM DE CONTRATO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Totvs Gestão de Estoque Compras e Faturamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *MOV006* | *PROCESSAR MOVIMENTO* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Informe a(s) rotina(s) envolvidas*.* | *Informe o nome técnico da(s) rotina(s) envolvidas.* | |  |  | |
| **Cadastros Iniciais:** | *Não se aplica.* |
| **Parâmetro(s):** | *Não se aplica.* |
| **Ponto de Entrada:** | *Não se aplica.* |
| **Tickets relacionados** | *119017* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MCP-1036 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL e Oracle.* |
| **Tabelas Utilizadas:** | *Não se aplica.* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Implementação para incluir os movimentos de acordo com o sequencial das Medições do Item de Contrato faturadas.

Esse procedimento somente afeta o processo de faturamento de medição do item de contrato.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.16*deste chamado.

## Procedimento para Utilização

1. Entrar no Menu Contratos - Manutencão de Contratos e escolher o filtro desejado.
2. Selecionar o contrato a faturar, clicar em anexos - Visualizar Medições do Contrato.
3. Selecionar as medições a serem faturadas e clicar em Faturar Medições.
4. Verificar que os movimentos criados respeitam a ordem das Medições do Item de Contrato.

Movimentos criados pelo Faturamento das Medições.

divs
