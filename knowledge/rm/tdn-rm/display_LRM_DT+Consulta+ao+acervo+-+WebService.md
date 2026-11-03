---
content_hash: 29ac29ac094363a3b11140aa97eb81e863be758305a48076b665fd6d9947bd0c
fetched_at: '2026-06-29T00:08:46.628587+00:00'
page_id: '317307236'
product: rm
source: tdn-rm
title: DT Consulta ao acervo - WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Consulta+ao+acervo+-+WebService
version: 3
---

# CONSULTA AO ACERVO - WEBSERVICE

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Bibliotecária** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Consulta ao acervo* | *Consulta ao acervo* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Consulta ao acervo** | ***Consulta ao acervo*** | |
| **Cadastros Iniciais:** | *Publicações*  *Exemplares*  *Fascículos*  *Artigos* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *WebService* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *EDUCACIONAL01-1187* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *SQL Server / Oracle* |
| **Tabelas Utilizadas:** | *LPUBLIC, LEXEMPLAR, LARTIGO, LFASCICULO, LUNIDADE* |
| **Sistema(s) Operacional(is):** | *Todos* |

## Descrição

Foi implementado um novo DataServer que irá permitir a consulta ao acervo através de webservices, assim permitindo realizar consultas ao acervo e detalhar um item do acervo semelhante a tela de consulta ao acervo do TOTVS Gestão Bibliotecária.

DataServer: **BibConsultaAcervoDataWS**

## Procedimento para implantação e utilização

O DataServer estará disponível a partir da versão 12.1.19 e para utilizá-lo basta utilizar qualquer meio de consumo de webservices.

Para as orientações de utilização do DataServer acesse o documento de referência. Clique [aqui](http://tdn.totvs.com/display/LRM/Consulta+ao+acervo+-+WebService) para acessar.
