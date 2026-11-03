---
content_hash: f701ca7496ae190bc3c680213c835c67874f3612223857616955b53a7d589659
fetched_at: '2026-06-29T00:06:00.360980+00:00'
page_id: '196804739'
product: rm
source: tdn-rm
title: ER_migracao_barra_calculo_projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_migracao_barra_calculo_projeto
version: 37
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação - Migração da** **Barra de Cálculo do Projeto** | | | |
| **Produto** | RM | **Módulo** | TOP (Totvs Obras e Projetos) |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6024 |
| **Requisito1** | PCREQ-6025 | **Subtarefa1** | PDR\_CP\_TOP007-1229 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | não |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  |  | | --- | --- | --- | | 1 | Projeto | **<http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx>** | | 2 | Cálcular Projeto | *<http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.CalcularProjeto.aspx>* | |  |  |  | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

 

 

 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Barra de Cálculo] | [Criação] | [Projetos -> Construção e Projetos -> Exibir Valores da Barra de Cálculo] | - |
|  |  |  |  |

 

## Objetivo

Migrar a barra de cálculo do projeto existente no RMSOLUM.exe aplicando as melhorias sugeridas pela equipe de Design Think, para que assim fique disponível na nova MDI.

## Definição da Regra de Negócio

A barra de cálculo no delphi contém:

* IDPRJ - Rev. [ID DA REVISAO] - NOME DA FASE [Cod fase] - CODAUXPRJ - CODPRJ - DESCRICAO
* Data do Último cálculo do projeto
* Valor Sem BDI
* Valor Com BDI
* BDI
* Total Indireto

A barra de cálculo na nova MDI, terá os mesmos itens, com o **botão de calcular projeto** como facilitador a mais:

* IDPRJ - Rev. [ID DA REVISAO] - NOME DA FASE [Cod fase] - CODAUXPRJ - CODPRJ - DESCRICAO
* Valor Sem BDI
* Valor Com BDI
* BDI
* Total Indireto
* Data do Último cálculo do projeto
* **Botão de Cálculo do Projeto (NOVO)**

## 

## Barra de Cálculo

A visão final da barra de cálculo será conforme ilustra o . 

O botão de Calcular, ou o próprio menu de Calcular projeto, deverá atualizar os valores da barra automaticamente.

## Parâmetros

Os valores da barra de cálculo, devem seguir a quantidade de dígitos após a vírgula, conforme os 

Parâmetros de projeto (f6) >>Exibição >> Geral >> **Monetários**,e o campo BDI %, **Percentuais.** 

## Valores da barra de cálculo

Será adicionado a opção **Exibir Valores da Barra de Cálculo**, em **Construção e Projetos**, e assim ao clicar na opção, 

os campos Valor sem BDI, BDI, Valor com BDI e Total Indireto, ficarão visíveis, conforme ilustra o .

## Segurança

Para que seja possível "Exibir os Valores da Barra de Cálculo", será necessário habilitar o item, conforme ilustra o . 

## Protótipo de Tela

**Protótipo 01 - Barra de cálculo delphi**

****Protótipo 02 - Exibir Valores da Barra de Cálculo****

******Protótipo 03 - Barra de Cálculo******

********Protótipo 04 - Segurança********

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
