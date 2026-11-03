---
content_hash: 5bc8336d8b5f5c1995ab7426c74a513f2c209935413f671a64e4fdcff551a929
fetched_at: '2026-06-29T00:06:11.846014+00:00'
page_id: '204964104'
product: rm
source: tdn-rm
title: ER_PCREQ-7829_Melhorias Abono Funcinário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=204964104
version: 5
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Automação de Ponto | **Módulo** | Abonos do Funcionário |
| **Segmento Executor** | Contrução e Projetos | | |
| **Projeto1** | PDR\_RH\_PTO008-5 | **IRM1** | PCREQ-7829 |
| **Requisito1** | PCREQ-7894 | **Subtarefa1** | PDR\_RH\_PTO008-20 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

 

## Objetivo

*Permitir ao usuário a possibilidade de visualizar abonos fora do período ativo, criar filtros por origem do abono e visualizar a descrição e dia da semana do abono.*

## Definição da Regra de Negócio

*Serão listadas a seguir as evoluções que serão necessárias para atender o requisito. Serão realizadas dentro da nova MDI:*

**1.** **Abono do Funcionário**

O cadastro de abonos do funcionário que pode ser acessado através do caminho [**Automação de Ponto -> Cadastros -> Funcionário -> Anexos -> Automação de Ponto -> Abono funcionário**], irá receber melhorias como a visualização de abonos fora do período ativo, possibilidade de criação de filtros por origem do abono e exibição da descrição e dia da semana do abono.

**1.1.** **Abonos fora do período ativo**

O cadastro de abonos do funcionário passará a exibir abonos que não estejam compreendidos no período ativo do TOTVS Automação de Ponto (***Protótipo Nº 1 – Abonos fora do período ativo***). Para manter a compatibilidade com o funcionamento antigo, será criado uma nova opção de filtro que permitirá ao usuário filtrar abonos que estejam compreendidos apenas no período ativo. Por exemplo, para exibir apenas os abonos que estejam no período atual do TOTVS Automação de Ponto, o usuário poderá criar e utilizar a expressão de filtro “***Período Ativo = Sim***” (***Protótipo Nº 2 – Período Ativo = Sim***);

**1.2.** **Filtro por origem do abono**

O cadastro de abonos do funcionário passará a ter uma nova opção de filtro, esta opção possibilitará criar filtros de abonos por sua origem (***Protótipo Nº 3 – Filtro por origem do abono***). Por exemplo, para exibir apenas os abonos futuros, o usuário poderá criar a expressão de filtro “***Origem do abono = Abono inserido pela AABONOFUTURO***”;

**1.3.** **Descrição do abono e dia da semana**

O cadastro de abonos do funcionário passará a exibir duas novas colunas na visão de abonos do funcionário, será adicionado uma coluna que exibirá a descrição do abono e outra coluna que exibirá o dia da semana que foi abonado. Quando o período do abono compreender mais de um dia, será exibido o dia da semana da data de início do período abonado (***Protótipo Nº 4 – Descrição do abono e dia da semana***).

## Protótipo de Tela

**Protótipo Nº 1 – Abonos fora do período ativo**

**Protótipo Nº 2 – Período Ativo = Sim**

**Protótipo Nº 3 – Filtro por origem do abono**

**Protótipo Nº 4 – Descrição do abono e dia da semana**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
