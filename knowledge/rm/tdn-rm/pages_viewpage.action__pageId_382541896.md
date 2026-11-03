---
content_hash: 609b17f87487c49075c9495fdded0ee7f30fa982e87a8dcd6c7e2f3dff0b56b4
fetched_at: '2026-06-29T00:09:04.009612+00:00'
page_id: '382541896'
product: rm
source: tdn-rm
title: DEDUANALYTICS-347 DT Fast Analytics - Inadimplência acumulada e mensal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382541896
version: 1
---

# TOTVS Fast Analitcs - Fato Inadimplência

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Fast Analytics. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Extração da Fato Inadimplência. | N/A. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parametrização do Business Analytics no RM Integração. |  | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | SPARAMGERAL.HABILITAFASTANALYTICS. |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A. |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | HCPARAMETROS  SPARAMGERAL |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | N/A |

## Descrição

Evolução da consulta para extrair os valores da inadimplência no mês (campo VLINADIMPLENCIAMENSAL) e a acumulada até o mês (VLINADIMPLENCIACUMULADO).

Para que seja possível realizar a extração dessa fato é necessário as seguintes parametrizações:

1) Liberar a configuração do Fast Analytics setando o parâmetro "HABILITAFASTANALYTICS" na SPARAMGERAL.

2) Configurar a integração com TOTVS Fast Analytics em RM Integrações | Ferramentas | Configurar | TOTVS Business Analytics  (marcar a flag TOTVS Fast Analytics)

3) Parametrizar as informações que serão utilizadas na extração RM Integrações | Ferramentas | Parâmetros | TOTVS Business Analytics

Depois de configurado/parametrizado o Fast Analytics, será necessário inserir a consulta de Inadimplência na pasta apropriada e executar o agente. Após a execução as informações estarão disponível no Gooddata para consulta.
