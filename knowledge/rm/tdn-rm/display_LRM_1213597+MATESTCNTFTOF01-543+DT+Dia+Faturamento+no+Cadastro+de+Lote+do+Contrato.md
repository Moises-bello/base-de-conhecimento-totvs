---
content_hash: ad3be844d94083ace66e5fbacba6a7569252c443ac9e5bfe03552e0c397d1ae8
fetched_at: '2026-06-29T00:08:41.603813+00:00'
page_id: '286736308'
product: rm
source: tdn-rm
title: 1213597 MATESTCNTFTOF01-543 DT Dia Faturamento no Cadastro de Lote do Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/1213597+MATESTCNTFTOF01-543+DT+Dia+Faturamento+no+Cadastro+de+Lote+do+Contrato
version: 112
---

# DIA FATURAMENTO NO CADASTRO DE LOTE DO CONTRATO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Faturar iten(s) de contrato(s) que possui(em) o Dia Faturamento informado na sub-aba Filtros Opcionais da aba Filtros dos Contratos no Cadastro de Lote de acordo com o Dia do Faturamento informado na aba Condições Gerais do Item de Contrato. |
| **Situação/Requisito:** | Ao realizar o faturamento do Lote de Contrato informando o Dia Faturamento, o sistema estava considerando todos os itens para faturamento definido no filtro dos contratos, não respeitando o Dia informado.  Esta situação ocorria pois o parâmetro **Vencimento em dias fixos** não estava marcado nos parâmetros do contrato. |
| **Solução/Implementação:** | Foi adicionado uma regra de visibilidade do campo Dia Faturamento Cadastro de Lote do Contrato, onde o mesmo somente será apresentado para o usuário caso o parâmetro **Vencimento em dias fixos** esteja marcado. |
| **Conversores e Parâmetros:** | O campo **Dia Faturamento** ficará visível quando nos parâmetros do Contrato estiver marcado a flag **Vencimento em dias fixos**. (Etapa Definições Fat. de Contrato 2/3). |
| **Tickets relacionados:** | 1213597. |
| **Requisito:** | MATESTCNTFTOF01-543. |

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.17*deste chamado.

## Procedimento para Utilização

1. Acesse o Módulo de Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.05 - Contratos | 04.05.04 - Faturamento | Etapa Definições Fat. de Contrato 2/3.  
     
     
     
   Marque o parâmetro **Vencimento em dias fixos**.
2. Acesse Contratos | Faturamento por Lote | Na tela de edição acesse Filtros dos Contratos | Filtros Opcionais | Irá verificar que o campo Dia Faturamento será apresentado.

divs
