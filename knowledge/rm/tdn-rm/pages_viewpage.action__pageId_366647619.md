---
content_hash: a81c73f9ef03d96415369d767bb2fe4757a91fc6cc62c4bc3c66487237d65101
fetched_at: '2026-06-29T00:09:00.262760+00:00'
page_id: '366647619'
product: rm
source: tdn-rm
title: 976885 MATESTCNTFTOF01-357 DT Alteração de Comportamento do Campo Afetar Orçamento
  no Tipo de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=366647619
version: 6
---

# AFETAR ORÇAMENTO NO TIPO CONTRATO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Orçamento no Contrato. |
| **Situação/Requisito:** | Ao permitir desmarcar o campo **Afetar Orçamento** no **Tipo de Contrato** o sistema não consistia se já havia algum contrato que gerou orçamento para este tipo.  Com essa possibilidade, os valores de orçamento poderiam ficar incorretos dependendo da mudança realizada pelo usuário. |
| **Solução/Implementação:** | Realizado o ajuste para o campo do **Tipo de Contrato** possuir o mesmo comportamento dos campos de parametrização do orçamento do movimento.  A partir da Release 12.1.21, uma vez parametrizado para **Afetar Orçamento**, e realizado a inclusão de parcela de orçamento no item de contrato gerando registro na TCNTORCAMENTORELAC, **não será possível desmarcar**. |
| **Conversores e Parâmetros:** | Contratos | Tabelas de Contrato | Tipos de Contrato | Campo **Afetar Orçamento**. |
| **Tickets relacionados:** | 976885. |
| **Requisito:** | Orçamento no Contrato. |
| **Documento de Referência:** | [Integração Contrato e Orçamento](http://wikihelp.totvs.com.br/WikiHelp/EST/EST.IntegracaoContratoOr%C3%A7amento.aspx). |

## Descrição

1. Tipo de Contrato parametrizado para **Afetar Orçamento**:
2. Contrato incluído utilizando o Tipo de Contrato parametrizado para Afetar Orçamento:
3. Gerado a parcela de orçamento para o Item de Contrato:
4. Registro de Orçamento gerado na TCNTORCAMENTORELAC:
5. Ao acessar o cadastro do **Tipo de Contrato** não será possível alterar a parametrização do efeito de orçamento:

## Observações

* Para habilitar novamente a alteração do campo **Afetar Orçamento** é necessário que não exista nenhum registro de orçamento para o tipo de contrato em questão.
* Em chamadas via serviços, como por exemplo, o WebService, caso exista registro de orçamento, o sistema não permitirá a alteração do efeito de orçamento.
