---
content_hash: 6af98e75e9d37444fd689d2f5f5e4b77a0f684b4d8bda9bf388279d58f860ac7
fetched_at: '2026-06-29T00:08:57.155075+00:00'
page_id: '353276241'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-2068 Criar Parametrização para inclusão de movimento de CT-
  e 3.0 - MULTIMODAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353276241
version: 4
---

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | Inclusão de movimento de CT- e 3.0 - MULTIMODAL - (Movimento e parametrização) | | |
| **Ticket:** | N/D | | |
| **Requisito (ISSUE):** | MATFATCMPCRM01-2068 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

Criação de parâmetro no TOTVS Gestão de Estoque, Compras e Faturamento para inclusão de movimento de CT-e 3.0 Multimodal

## Definição da Regra de Negócio

Foi implementado no parâmetro Modal a opção "Multimodal" para a inclusão de um movimento de CT-e 3.0 Multimodal.

O parâmetro está localizado nos parâmetros do tipo de movimento "Etapa 69 - Fis - Conhecimento de Transporte":

Em tipos de movimento definidos como Multimodal, ao incluir um novo movimento, na aba "CTRC | Outros Dados" deverá ser apresentado o campo novo "Indicador Negociável".

Este campo contem 2 tipos de indicadores.

Os tipos de indicadores são:

0 - Não Negociável;  
1 - Negociável.

Na aba CT-e, por se tratar de um CT-e Multimodal, será apresentada a aba Seguro de Carga.

Somente os seguintes campos serão visiveis para preenchimento:  
- Seguradora;  
- Apólice;  
- Averbação.

O campo de Registro do Operador de Transporte Multimodal (COTM) é obrigatório o preenchimento, no cadastro da Filial, aba de Anexos da Filial - Dados Fiscais - Dados Adicionais.

**Consistências:**

* O campo "Indicador Negociável" é de preenchimento obrigatório.

Em tipos de movimento de CT-e parametrizados como "Multimodal" será oibrigatorio o preenchimento do campo "Indicador Negociável" no movimento e caso não seja preenchido, será apresentado a mensagem de consistência abaixo:

**Tabelas Utilizadas**

Para a implementação, foi criado o campo na base na tabela citada abaixo:

* TMOVTRANSP - Dados de Transporte.
* Campo: INDICADORNEGOCIAVEL.TMOVTRANSP

### Procedimento para Utilização

Não se aplica.

**CONFIGURAÇÃO DE PARÂMETROS**

Não se aplica.
