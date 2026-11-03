---
content_hash: cb9b3f747bedab5abe0317c91bc4f8d7b322fbbf9315e492af9817fac72bbae2
fetched_at: '2026-06-29T00:06:12.165560+00:00'
page_id: '205914176'
product: rm
source: tdn-rm
title: ER_PCREQ-5476_colunas_de_niveis_na_medicao_de_contratos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5476_colunas_de_niveis_na_medicao_de_contratos
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** |  |
| **Requisito1** | PCREQ-5476 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** |  |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  Contratos: <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar que no processo de Medição de Item de Contrato possa ser visualizado toda a hierarquia dos itens associados aos contratos, isto é, exibir as obras e etapas das respectivas tarefas.

## Definição da Regra de Negócio

O processo de Medição de Item de Contrato deverá ser alterado para que possa exibir, além das tarefas associadas ao contrato (itens), toda a hierarquia que as compõe, como obras e etapas (Protótipo 01) , sendo assim algumas regras deverá ser consideradas:

 

* Apenas as tarefas continuarão sendo medidas pois a exibição de obras e etapas será apenas informativa;
* A seleção de obras e etapas não deverá ser considerada na execução do processo;
* As linhas de obras e etapas deverão estar como somente leitura para todas as colunas;
* Um ícone deverá diferenciar obras, etapas e tarefas.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Medição de Item de Contrato | [Alteração] | Contratos/Períodos/Medição de Item de Contrato | - |

## Protótipo de Tela

**Protótipo 01**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
