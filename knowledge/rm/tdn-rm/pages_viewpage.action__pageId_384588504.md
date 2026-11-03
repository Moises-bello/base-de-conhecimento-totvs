---
content_hash: b9fc960b48c6f949699da066fd74ed70410d6fdfd6777c6a84a5bed1c77ea734
fetched_at: '2026-06-29T00:09:07.712316+00:00'
page_id: '384588504'
product: rm
source: tdn-rm
title: DEDUANALYTICS-361 DT Fast Analytics - Criação da fato Recebido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=384588504
version: 1
---

# TOTVS Fast Analytics - Fato Recebido

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Fast Analytics. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Extração Fato Recebido. | N/A. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parametrização do Business Analytics no RM Integração. | N/A | |  |  | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | SPARAMGERAL.HABILITAFASTANALYTICS |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** | Todos |
| **Banco(s) de Dados:** | Sql Server e Oracle. |
| **Tabelas Utilizadas:** | HCPARAMETROS    SPARAMGERAL |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | N/A |

## Descrição

Foi desenvolvido a consulta que será utilizada pelo agente para realizar a extração dos dados relacionados com a fato Recebido do TOTVS Fast Analytics do Educacional.

Para que seja possível realizar a extração dessa fato é necessário as seguintes parametrizações:

1) Liberar a configuração do Fast Analytics setando o parâmetro "HABILITAFASTANALYTICS" na SPARAMGERAL.

2) Configurar a integração com TOTVS Fast Analytics em RM Integrações | Ferramentas | Configurar | TOTVS Business Analytics  (marcar a flag TOTVS Fast Analytics)

3) Parametrizar o curso e período letivo em RM Integrações | Ferramentas | Parâmetros | TOTVS Business Analytics | Parâmetros por Empresa | Educacional

Depois de configurado/parametrizado o Fast Analytics, será necessário inserir a consulta de Recebido na pasta apropriada e executar o agente. Após a execução as informações estarão disponível no Gooddata para consulta.
