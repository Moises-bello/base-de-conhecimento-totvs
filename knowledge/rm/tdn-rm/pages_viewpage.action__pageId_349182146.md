---
content_hash: 5d06e1e6db6564da7d7bd8a942ded92f3a1b584162bb2aaa83c1a4ed31e27c80
fetched_at: '2026-06-29T00:08:55.398900+00:00'
page_id: '349182146'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-3018 Criar Parametrização para inclusão de movimento de repasse
  - R-2030 e R-2040 da EFD Reinf
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=349182146
version: 3
---

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | Inclusão de movimento de repasse - R-2030 e R-2040 da EFD Reinf. | | |
| **Ticket:** | N/D | | |
| **Requisito (ISSUE):** | MATFATCMPCRM01-3018 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

Criação de parâmetro no TOTVS Gestão de Estoque, Compras e Faturamento para inclusão de movimento de repasse - R-2030 e R-2040 da EFD Reinf.

## Definição da Regra de Negócio

Foi implementado o parâmetro "Movimento de Repasse EFD Reinf" que será visível em todos os tipos de movimentos.

O parâmetro está localizado nos parametros do tipo de movimento "Etapa 61 - Fiscal - Dados Fiscais":

Em tipos de movimento onde o parametro esteja marcado, ao incluir um novo movimento, na aba "Integrações | Fiscal" do Item de movimento deverá ser apresentado o campo "Tipo Repasse EFD Reinf".

Este campo contem 5 tipos de repasse EFD Reinf que após definido no item de movimento serão utilizados pelo TOTVS Gestão Fiscal para a rotina de Reinf.

Os tipos de repasse são:

1 - Patrocínio;  
2 - Licenciamento de marcas e símbolos;  
3 - Publicidade;  
4 - Propaganda;  
5 - Transmissão de espetáculos.

**Consistências:**

* O campo Tipo de Repasse deve ter preenchimento obrigatório.

Em tipos de movimento parametrizados como Repasse EFD Reinf será oibrigatorio o preenchimento do tipo de repasse no item de movimento e caso não seja preenchido, será apresentado a mensagem de consistência abaixo:

* Somente um tipo de repasse poderá ser selecionado por item de movimento.
* Itens de movimentos distintos poderão ter tipos de repasses distintos.
* Quando o parâmetro de repasse estiver habilitado, no movimento desse tipo, em Integrações, deve ser apresentada a opção Processo Judiciais, que deverá ser preeenchido para ser utilizado posteriormente pelo TOTVS Gestão Fiscal para a rotina de Reinf.

**Tabelas Utilizadas**

Para a implementação, foram criados dois campos na base nas tabelas citadas abaixo:

* TTMVEXT- Tipos de Movimentos.
* Campo: TTMVEXT.MOVIMENTOREPASSEREINF
* TITMMOVFISCAL - Dados Fiscais do Item de Movimento
* Campo: TITMMOVFISCAL.TIPOREPASSEREINF

### Procedimento para Utilização

Não se aplica.

**CONFIGURAÇÃO DE PARÂMETROS**

Não se aplica.
