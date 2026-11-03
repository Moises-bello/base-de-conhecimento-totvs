---
content_hash: c735ca25705aecdd47b50125117a443c321d127305ad740a29b02232dc9403d1
fetched_at: '2026-06-29T00:06:16.197649+00:00'
page_id: '211064744'
product: rm
source: tdn-rm
title: TTDNF3_DT_Impressao_Boleto_WebService_
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=211064744
version: 1
---

# Geração de Boleto através de WebService.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *TOTVS RM* |
| **Segmento:** | *RM* |
| **Módulo:** | **Informe o módulo*.* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *wsEdu* | *WebService contendo serviços do Educacional* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Impressão de boleto do Educacional através do serviço de WebService chamado wsEdu** | ***ImprimeBoletoParam()**.* | |  |  | |
| **Cadastros Iniciais:** | *N/A* |
| **Parâmetro(s):** | *Para que seja realizado a impressão do boleto através do WebService, deve ser parâmetrizado o relatório para a geração de Boleto conforme a geração de boleto existente no Portal do Educacional. O mesmo boleto gerado no Portal Educacional será disponibilizado através deste WebService.* |
| **Ponto de Entrada:** | *N/A.* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *Oracle e SQL Server* |
| **Tabelas Utilizadas:** | *N/A* |
| **Sistema(s) Operacional(is):** | *Windows XP, 7, 8, 8.1 e 10.* |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** | *N/A* |
| **Versão Expedida:** | *N/A* |

## Descrição

Foi criado um novo serviço no webservice wsEdu no qual é disponibilizado o boleto gerado em arquivo PDF. Este serviço retorna um Array de bytes do arquivo gerado e deve ser salvo posteriormente como um novo arquivo no disco.

## Procedimento para Utilização

* *Para consumir este serviço, deverá ser criado uma aplicação externa para chamada do WebService e manipular o conteúdo retornado, criando um novo arquivo em disco.*
* *O serviço ImprimeBoletoParam espera os seguintes parâmetros (Código do Boleto, Código da Coligada, Código da Filial, Código do Nível de Ensino e Usuário. Este usuário é apenas um nome de usuário com permissões para execução do relatório de boleto.*

**Exemplo:**

divs
