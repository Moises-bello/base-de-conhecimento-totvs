---
content_hash: 2b603d75fcafd1328b2c00f476b367a4241f46ea87159619ab0d1624b9787c7a
fetched_at: '2026-06-29T00:08:28.993969+00:00'
page_id: '272138828'
product: rm
source: tdn-rm
title: ER EDUCTB002-501 Tamanho Maximo Linha TXT
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+EDUCTB002-501+Tamanho+Maximo+Linha+TXT
version: 103
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | Totvs Gestão Contábil |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | CTB/FIN 2016/2017 | **IRM/EPIC1** | EDUCTB002-494 |
| **Requisito/Story/Issue1** | EDUCTB002-501 | **Subtarefa1** | EDUCTB002-518 |
| **Chamado/Ticket2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

Liberar o tamanho máximo das linhas quando o tipo de saída, dos relatório contábeis, for arquivo texto (TXT).

## Definição da Regra de Negócio

Quando o tipo de saída dos relatórios contábeis for arquivo texto (TXT), o sistema não deverá limitar o tamanho da linha, ou seja, a soma do tamanho das colunas poderá ultrapassar limite de caracteres por linha. Essa melhoria deve ser realizada nos relatórios contábeis fixos, que possuem a aba campos:

* Balancete
* Razão
* Diário
* Balanço Patrimonial
* Acompanhamento Orçamentário
* Listagem de Lançamentos

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
