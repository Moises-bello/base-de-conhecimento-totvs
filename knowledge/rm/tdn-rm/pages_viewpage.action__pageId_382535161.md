---
content_hash: 8434d01b31948f73ea14ca6ea89603b6eeaedb739cffff9a1c022ea5604215d8
fetched_at: '2026-06-29T00:09:03.648711+00:00'
page_id: '382535161'
product: rm
source: tdn-rm
title: DEDUANALYTICS-257 Fast Analytics - Extração da Fato Alunos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382535161
version: 1
---

# Extração da Fato Alunos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional (Fast Analytics). |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Extração da Fato de Alunos. | Extração da Fato de Alunos. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | IParametrização do Business Analytics no RM Integração. | N/A. | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | SPARAMGERAL.HABILITAFASTANALYTICS. |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | SQL Server e Oracle. |
| **Tabelas Utilizadas:** | HCPARAMETROS    SPARAMGERAL. |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | N/A |

## Descrição

Foi evoluída a consulta que será utilizada pelo agente para realizar a extração dos dados relacionados com a fato Alunos do TOTVS Fast Analytics do Educacional. Agora na configuração do agente pode ser informado um período maior que um mês, evitando assim a necessidade de rodar a extração mês a mês.

Para que seja possível realizar a extração dessa fato é necessário as seguintes parametrizações:

1) Liberar a configuração do Fast Analytics setando o parâmetro "HABILITAFASTANALYTICS" na SPARAMGERAL.

2) Configurar a integração com TOTVS Fast Analytics em RM Integrações | Ferramentas | Configurar | TOTVS Business Analytics  (marcar a flag TOTVS Fast Analytics)

3) Parametrizar as informações relacionadas a alunos: RM Integrações | Ferramentas | Parâmetros | TOTVS Business Analytics

Depois de configurado/parametrizado o Fast Analytics, será necessário inserir a consulta de Alunos na pasta apropriada e executar o agente. Após a execução as informações estarão disponível no Gooddata.
