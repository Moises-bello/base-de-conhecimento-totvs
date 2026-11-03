---
content_hash: 2a524a67452610286b58ae3e78502c9324a9a7f89b6d2110537d7805463e67c8
fetched_at: '2026-06-29T00:06:19.534558+00:00'
page_id: '219698682'
product: rm
source: tdn-rm
title: DT_EXP#8_Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219698682
version: 3
---

# RM - Experiência 8 - Telas Faturamento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina** | | Faturamento | |
| **Cadastros Iniciais:** | Tipos de Glosa, Tipos de Pré-Glosa, Motivo de Estorno de Fatura, Motivos de Recurso de Glosa, Desconto em Repasse, Empresa, Pendências |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server |
| **Tabelas Utilizadas:** | SZTIPOGLOSA, SZTIPOPREGLOSA, SZMOTIVOESTORNO, SZMOTRECGLOSA, SZDESCONTOREPASSE, SZEMPRESA, SZFATPENDENCIA |
| **Sistema(s) Operacional(is):** | Todos |
| **Versões/Release:** | 12.1.9 |

## Descrição

Foram reescritos os cadastros Tipos de Glosa, Tipos de Pré-Glosa, Motivo de Estorno de Fatura, Motivos de Recurso de Glosa, Desconto em Repasse, Empresa, Pendências, visando adequar à experiência 8, que foi desenvolvida em cima do TOTVS HMTL Framework.

854480

## Procedimento para Implantação

Antes de executar a atualização é recomendável realizar o backup do banco de dados bem como dos arquivos do Sistema (executáveis, dlls e arquivos de configuração):  
Realizar a atualização antes no ambiente de homologação e, posterior a devida validação, no ambiente de produção.

* É necessária a instalação do Totvs Gestão Hospitalar na versão 12.1.9.
* Instalação do fluig versão 1.5.2.

divs
