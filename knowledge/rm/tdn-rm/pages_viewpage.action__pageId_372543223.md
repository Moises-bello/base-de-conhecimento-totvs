---
content_hash: 49a888120a4a65705a458229d9dac9ece884fc956ebcb29e905d2db97e8c8694
fetched_at: '2026-06-29T00:09:01.091508+00:00'
page_id: '372543223'
product: rm
source: tdn-rm
title: DEDUANALYTICS-312 DT Fast Analytics - Criação da Fato de Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372543223
version: 1
---

# TOTVS Fast Analytics - Fato de Faturamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Fast Analytics. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Extração Fato Faturamento. | N/A |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parametrização do Business Analytics no RM Integração. | N/A. | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | SPARAMGERAL.HABILITAFASTANALYTICS |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | Sql Server e Oracle. |
| **Tabelas Utilizadas:** | HCPARAMETROS  SPARAMGERAL |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | N/A |

1. [DEDUANALYTICS-312](http://jiraproducao.totvs.com.br/browse/DEDUANALYTICS-312)

## Descrição

Foi desenvolvido a consulta que será utilizada pelo agente para realizar a extração dos dados relacionados com a fato Faturamento do TOTVS Fast Analytics do Educacional.

Para que seja possível realizar a extração dessa fato é necessário as seguintes parametrizações:

1) Liberar a configuração do Fast Analytics setando o parâmetro "HABILITAFASTANALYTICS" na SPARAMGERAL.

2) Configurar a integração com TOTVS Fast Analytics em RM Integrações | Ferramentas | Configurar | TOTVS Business Analytics  (marcar a flag TOTVS Fast Analytics)

3) Parametrizar a data de faturamento em RM Integrações | Ferramentas | Parâmetros | TOTVS Business Analytics | Edu - Data Faturamento

Depois de configurado/parametrizado o Fast Analytics, será necessário inserir a consulta de Faturamento na pasta apropriada e executar o agente. Após a execução as informações estarão disponível no Gooddata para consulta.
