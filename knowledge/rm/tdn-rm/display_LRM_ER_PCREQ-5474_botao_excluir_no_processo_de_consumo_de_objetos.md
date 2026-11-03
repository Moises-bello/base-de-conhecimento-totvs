---
content_hash: ef804195adf7ae7e49682c74b2e7b97b4ae7a2248cc98f1b9d1c6c82487bb861
fetched_at: '2026-06-29T00:06:12.131243+00:00'
page_id: '204968756'
product: rm
source: tdn-rm
title: ER_PCREQ-5474_botao_excluir_no_processo_de_consumo_de_objetos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5474_botao_excluir_no_processo_de_consumo_de_objetos
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** |  |
| **Requisito1** | PCREQ-5474 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:  Contratos: <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Contrato.aspx> | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar que no processo de Consumir Objetos do Contrato, os objetos a consumir e objetos consumidos, possam ser excluídos de forma simples.

## Definição da Regra de Negócio

O processo de Consumir Objetos do Contrato deverá ser alterado para que os objetos a consumir e objetos consumidos possam ser excluídos de forma simples. O botão de **Excluir**   deverá ser adicionado na barra de ferramentas existente no painel de **Objetos a Consumir** (Protótipo 01) e na aba **Objetos Consumidos no Período** (Protótipo 02). No primeiro, o usuário deverá selecionar a(s) linha(s) desejada(s) e clicar no botão, sendo assim, as mesmas serão excluídas do grid, já no segundo, ao marcar a(s) linha(s) e clicar no botão, as mesmas deverão ser marcadas como excluídas, e ao executar o processo a ação será efetivada e no caso de o usuário desistir da exclusão, basta desmarcar as linhas selecionadas para que o consumo não seja excluído.  

**Importante:**

* + - **Devido à essa alteração, não será mais possível realizar consumos com quantidade, valor ou percentual igual a 0(zero), pois essa possibilidade apenas permitia que um item já consumido pudesse ser excluído.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Consumir Objetos do Contrato | [Alteração] | Contratos/Períodos/ Consumir Objetos do Contrato | - |

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
