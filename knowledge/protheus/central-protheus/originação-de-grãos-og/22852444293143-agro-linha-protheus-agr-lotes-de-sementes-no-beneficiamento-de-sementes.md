---
article_id: 22852444293143
category: Originação de Grãos (OG)
content_hash: f9ba571daa2e067fc7b72ba80aef8f52868799d96db98d8df8d30f18afb952e1
fetched_at: '2026-06-28T22:45:40.976363+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Lotes de Sementes no Beneficiamento de Sementes
type: support-article
updated_at: '2025-06-20T11:43:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22852444293143-Agro-Linha-Protheus-AGR-Lotes-de-Sementes-no-Beneficiamento-de-Sementes
---

Características do Requisito:

|  |  |
| --- | --- |
| **Linha de Produto:** | Microsiga Prothues. |
| **Segmento:** | Agroindústria. |
| **Módulo:** | SIGAAGR. |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | AGRA840 | Beneficiamento de Sementes | |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | DAGROINDUSTRIA-5665 |
| **País(es):** | Brasil. |
| **Tabelas Utilizadas:** | NP9. |
| **Pacote:** | [12.1.17](https://suporte.totvs.com/totvs-tdi-files-maps/mapeamentos/portal-anexos/anexos/zendesk/20191014/TTVFLGP1J001-1571083687329-592152.ZIP), |

**Descrição**Foi adicionado na tabela **"NP9"** um novo campo para contemplar o tipo de ordem de produção, campo foi denominado com **"NP9\_TPPR"**.

**Atualizações do Compatibilizador**Criação de **Campos** no arquivo**SX3 – Campos****:**

|  |  |
| --- | --- |
| **Campo** | NP9\_TPPR |
| **Tipo** | Caractere |
| **Tamanho** | 1 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | Tp. Produção |
| **Descrição** | Tipo de Produção |
| **Usado** | Sim |
| **Obrigatório** | Não |
| **Browse** | Não |
| **Opções** | I=Interna;E=Externa;R=Retrabalho;O=Outros |
| **Relação** | "I" |
| **Help** | Tipo de ordem de produção a ser gerada. |
