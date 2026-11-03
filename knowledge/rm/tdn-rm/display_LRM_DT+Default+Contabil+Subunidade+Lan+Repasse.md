---
content_hash: fd6b58742426cfb5fdf4ada17bcf37325faa02a6f0395b77925464fc28ea4582
fetched_at: '2026-06-29T00:08:33.395871+00:00'
page_id: '274315692'
product: rm
source: tdn-rm
title: DT Default Contabil Subunidade Lan Repasse
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Default+Contabil+Subunidade+Lan+Repasse
version: 6
---

# Buscar default contábil da subunidade para lançamentos de repasse

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Construção e Projetos | | |
| **Módulo:** | Totvs Gestão Financeira | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Default Contábil.* | *Buscar default contábil.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Default contábil no Lote (subunidade)*.* | **Default contábil no Lote*.* | |  |  | | | |
| **Chamado/Ticket:** | TSWHZZ | | |
| **Requisito/Story/Issue:** | FINANCEIRO01-577. | | |
| **País:** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** |  | | |

### Objetivo

Permitir que o usuário defina os defaults contábeis para contabilização na subunidade do empreendimento adquirido no Totvs Incorporação e a contabilização de um lançamento originado de um repasse financeiro busque os defaults da subunidade do lançamento origem quando o evento possui item parametrizado para "Buscar Defaults em" como Subunidade (RM SGI).

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Defaults contábeis Subunidade | Envolvida | Cadastros -> Manutenção de Empreendimentos -> Quadra/Lote -> Lote -> Default Contábil | - |
| Contabilização Lançamento | Alteração | Contas a pagar-receber -> Lançamentos -> Dados Adicionais -> Contabilização | - |
| Contabilização Baixa | Alteração | Contas a pagar-receber -> Lançamentos -> Baixas -> Contabilização | - |

Lançamentos financeiros a receber gerados via Totvs Incorporação estão vinculados a um contrato de venda cujo(s) item(ns) estão vinculados a um loteamento, quadra e lote (subunidade). Na subunidade é possível definir defaults contábeis a serem carregados quando o evento possui item parametrizado para buscar default em "Subunidade (RM SGI)". 

No Totvs Gestão Financeira há um processo de repasse que permite passar para um fornecedor a responsabilidade pela quitação do total ou parcial do valor de um ou mais lançamentos financeiros (o lançamento de origem e aquele criado pelo repasse ficam vinculados). O sistema foi evoluído para quando for executada a contabilização de lançamentos criados por repasse os defaults contábeis, quando o evento contábil parametrizado para isso, sejam buscados da subunidade vinculada ao lançamento origem.

**Tabelas Utilizadas**

* FREPASSE – Repasse de Lançamentos

## **Procedimento para Configuração**

No Totvs Incorporação parametrizar os defaults contábeis na subunidade  em Cadastros -> Manutenção de Empreendimentos -> Quadra/Lote -> Lote -> Default Contábil.

No Totvs Gestão Financeira parametrizar os itens de evento contábil em Cadastros -> Contabiliade -> Eventos Contábeis -> Itens Evento para buscar default em "Subunidade (RM SGI)" .

## Procedimento para Utilização

No Totvs Gestão Financeira aplicar o evento contábil na contabilização do lançamento/baixa do lançamento originado pelo processo de repasse.

OBS: a contabilização do lançamento gerado pelo repasse, para utilizar essa opção, não pode ser feita na inclusão.
