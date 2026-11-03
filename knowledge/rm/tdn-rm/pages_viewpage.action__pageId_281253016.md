---
content_hash: 3cd368ddd008fb80f080da540b7038468a05bb2854328b9d990927b6270fb7d8
fetched_at: '2026-06-29T00:08:35.511663+00:00'
page_id: '281253016'
product: rm
source: tdn-rm
title: Calculo de recorrência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=281253016
version: 109
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Snowden | **Módulo** | Incidents |
| **Segmento Executor** |  | | |
| **Projeto** | Snowden | **IRM/EPIC** |  |
| **Requisito/Story/Issue** | 1. [FRW\_FRW004-52](http://jiraproducao.totvs.com.br/browse/FRW_FRW004-52 "Lógica de armazenamento do stack de dados") | **Subtarefa** | 1. [FRW\_FRW004-53](http://jiraproducao.totvs.com.br/browse/FRW_FRW004-53) |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 

Realizar o calculo de quantas vezes o mesmo incidente ocorreu, com detalhamento de grupo de incidente, versão e cliente

### Definição da Regra de Negócio

Quando novos incidentes são cadastrados, uma rotina garante que os cálculos de recorrência estejam corretos.

Isso é feito fazendo filtros por incidente, cliente e versão nas ocorrências do incidente. com o total de registros em mãos temos o valor da recorrência de cada grupo.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
