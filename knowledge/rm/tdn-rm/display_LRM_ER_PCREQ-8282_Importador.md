---
content_hash: 50b3128b6bd0e0894f01a1878452fda51fb60a22e07fc11b87b10824f163a896
fetched_at: '2026-06-29T00:06:13.501081+00:00'
page_id: '208342404'
product: rm
source: tdn-rm
title: ER_PCREQ-8282_Importador
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8282_Importador
version: 8
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Totvs Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto** | R\_EDU\_EDU011 | **IRM** | PCREQ-8277 |
| **Requisito** | PCREQ-8282 | **Subtarefa** | PDR\_EDU\_EDU011-600 |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar que sejam importados registros relacionados aos requisitos das disciplinas do Ensino Superior.

## Definição da Regra de Negócio

Através da ferramenta Totvs Educacional - Importador, será possível importar registros relacionados aos requisitos das disciplinas.

Para importar os registros, o arquivo SREQUISITO.TXT deverá ter os valores dos seguintes campos:

* CODCOLIGADA: Código da coligada
* CODCURSO: Código do curso
* CODHABILITACAO: Código da Habilitação
* CODGRADE: Código da Matriz
* CODPERIODO: Código do Período
* CODDISC: Código da Disciplina
* CODDISCREQ: Código da Disciplina Requisito
* TIPO: Tipo do Requisito (Pré-requisito ou Correquisito)

Mais informações no arquivo (RM Classis Net - LayoutsImportação.xls), disponibilizado juntamente com a ferramenta.

***Tabelas Utilizadas***

* SREQUISITO

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
