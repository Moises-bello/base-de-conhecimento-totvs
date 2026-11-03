---
content_hash: b51eb662936f601227c664806c883897757e9aa8c7b64cc44fce583abc55e5bb
fetched_at: '2026-06-29T00:06:13.107325+00:00'
page_id: '208339377'
product: rm
source: tdn-rm
title: ER_PCREQ-6023_Relatórios_das_Curvas_ABC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208339377
version: 23
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Relatórios Projetos |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-6022 |
| **Requisito1** | PCREQ-6023 | **Subtarefa1** | PDR\_CP\_TOP008-86 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Upgrade dos relatórios de curvas ABC utilizando o Gerador.NET.

## Definição da Regra de Negócio

O Relatório de curva ABC exibe dados do cálculo das curvas ABC dos insumos e tarefas da planilha de atividades do cenário principal. Haverá três tipos de relatórios que serão disponibilizados em duas versões, sendo uma exibindo e calculando utilizando o pelo preço de venda e outra versão utilizando o preço de custo. Os relatórios são:

* ;
* ;
* ;

Para executar o relatório o usuário deverá acessar a funcionalidade de relatórios da Curva ABC  que conterá as seguintes opções:

* **Relatório:** informação do código do relatório a ser impresso. Nessa pesquisa aparecerão somente relatórios do tipo “CURVAS ABC”.
* **Imprimir direto da impressora:** envia o relatório diretamente para impressora.

A funcionalidade para execução do relatório é acessada através da opção "Relatórios -> Curva ABC".

Os relatórios são dependentes das informações tabuladas pelo cálculo da Curva ABC. Diante disto, esta disponível a opção de realizar o recalculo da curva ABC. Para isto o usuário deve marcar a respectiva opção e o cálculo ocorrer antes da geração do relatório.

**Restrições**

* Estes relatórios serão padrões no sistema e por questão de segurança o usuário não poderá editar ou excluir os mesmos, podendo duplicá-los para criar outros customizados.

**Filtros**

* Por cenário e tipo de planilha.
* Tarefa inicial e final.
* O filtro de disciplina esta implícito e será aplicado somente no relatório da Curva ABC de Serviços.

**Localização dos relatórios:**

Interna: *RM/Documentos/Prj-Projetos/Relatórios/Relatorios Migrados*

Clientes: Pasta "*Objetos Gerenciais*" localizada no diretório de instalação do Produto.

Atenção

Para que um relatório seja gerado pelo Menu Relatórios -> Curva ABC, o mesmo tem que ser do tipo Curva ABC.

Para relatórios relacionados a planilha atividades/serviços () no primeiro detalhe (Banda) do relatório dever conter a tabela de Curva Abc Serviços (MABCSERV).

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Relatórios das Curvas ABC | Criação | Relatórios -> Curva ABC |  |
|  |  |  |  |
|  |  |  |  |

***Tabelas Utilizadas***

* *Não se aplica.*

## Protótipo de Tela

**Protótipo 01 - Tela de Filtro**

**Protótipo 02 - Acompanhamento de curva ABC de serviços**

****Protótipo 03 - Acompanhamento de curva ABC de insumos****

******Protótipo 04 - Acompanhamento de curva ABC de grupo de custos******

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
