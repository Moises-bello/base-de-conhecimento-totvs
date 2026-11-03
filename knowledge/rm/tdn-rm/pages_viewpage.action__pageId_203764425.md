---
content_hash: 11a1928d73432d06aded58a4432906d5489527b4c87fcf0062dec5124334aa72
fetched_at: '2026-06-29T00:06:10.564359+00:00'
page_id: '203764425'
product: rm
source: tdn-rm
title: ER_Melhorias na Qualificação de Fornecedores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203764425
version: 4
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Gestão de Estoque, Compras e Faturamento | **Módulo** | Compras |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_C&P\_MOV006 | **IRM1** | * [PCREQ-2235](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-2235 "PCREQ-2235") |
| **Requisito1** | * [PCREQ-7757](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-7757 "PCREQ-7757") | **Subtarefa1** | 1. [PDR\_CP\_MOV008-60](http://jira.totvs.com.br/browse/PDR_CP_MOV008-60) |
| **Chamado2** | N/A | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

Implementar melhorias identificadas no processo de qualificação de fornecedores liberado na release 12.1.4.

### (Obrigatório)

## Definição da Regra de Negócio

1. O Nome Fantasia do Cli/For será adicionado nos anexos de qualificação e requisitos do produtos /fornecedor.
2. Incluir as informações de CNPJ e Estado do fornecedor na tela do processo de análise de requisitos.
3. Serão Disponibilizados no relatório detalhado do QCP (Report), e também na exportação de QCP para excel o (Excel de modelo detalhado) a informação de qualificação do fornecedor conforme foi feito na tela do quadro comparativo na visão do mesmo pelo sistema.
4. A qualificação do fornecedor será tratada por coligada. Este comportamento será alterado para tratar por coligada como é feito na qualificação de produtos/fornecedor. Neste caso o campo CODCOLCFO será incluído na tabela TQUALIFICACAOCFO e os tratamentos necessários serão realizados no serviço de qualificação de fornecedores.  
     
   Na conversão de base de dados o campo CODCOLIGADA da tabela TQUALIFICACAOCFO será alterado para CODCOLCFO e o campo CODCOLIGADA será criado e preenchido da seguinte forma:

* Caso a coligada do fornecedor (CODCOLCFO) for global, os dados da qualificação serão replicados para todas as coligadas que estiverem parametrizadas para qualificação de fornecedores.
* Caso contrario (fornecedor não global) o campo CODCOLIGADA será preenchido com a mesma informação do campo CODCOLCFO.
* O campo CODCOLIGADA criado terá uma forengkey com a tabela global GCOLIGADA
* A chave primária da tabela TQUALIFICACAOCFO será alterado para incluir o campo CODCOLCFO

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
