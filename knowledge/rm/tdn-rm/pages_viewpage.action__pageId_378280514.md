---
content_hash: 9730731a1612eed0f4eac2e1ff42349f74fb14de6b4b5e30c2716a3bea4b6c60
fetched_at: '2026-06-29T00:09:01.819418+00:00'
page_id: '378280514'
product: rm
source: tdn-rm
title: DEDUANALYTICS-326 DT Fast Analytics - Parâmetro da Fato de Inadimplência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=378280514
version: 1
---

# Fast Analytics - Fato Inadimplência

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Fast Analytics. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parametrização. | Parametrização para fato de inadimplência. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Configuração da integração com o Fast Analytics. | Configuração da integração com o Fast Analytics. | |  |  | |
| **Cadastros Iniciais:** | N/A. |
| **Parâmetro(s):** | SPARAMGERAL.HABILITAFASTANALYTICS  EDUKPI\_EDUINADDIASAPOSVENC.ID |
| **Ponto de Entrada:** | N/A. |
| **Tickets relacionados** | N/A. |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** |  |
| **País(es):** | Todos. |
| **Banco(s) de Dados:** | Sql Server e Oracle. |
| **Tabelas Utilizadas:** | HCPARAMETROS    SPARAMGERAL |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | N/A |

## Descrição

Criado o parâmetro "Número de dias após o vencimento para ser considerado como inadimplente" nos parâmetros da integração (RM Integração | Ferrasmentas | Parâmetros | TOTVS Business Analytics | Edu-Inadimplência).

Para que seja possível realizar essa parametrização é necessário configurar o TOTVS Fast Analytics:

1) Liberar a configuração do Fast Analytics setando o parâmetro "HABILITAFASTANALYTICS" na SPARAMGERAL.

2) Configurar a integração com TOTVS Fast Analytics em RM Integrações | Ferramentas | Configurar | TOTVS Business Analytics  (marcar a flag TOTVS Fast Analytics)

Depois de configurado/parametrizado o Fast Analytics, será possível realizar a extração da fato de Inadimplência.
