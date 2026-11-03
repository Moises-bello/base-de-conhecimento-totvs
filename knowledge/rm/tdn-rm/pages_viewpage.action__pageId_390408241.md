---
content_hash: 82cc9773870dc662f59cfcd2184c2a92a52b3035e73d707b3cb976a4b86d1595
fetched_at: '2026-06-29T00:09:08.978579+00:00'
page_id: '390408241'
product: rm
source: tdn-rm
title: DT Cálculo IRRF - Pessoa Física sem considerar tabela progressiva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=390408241
version: 11
---

# Cálculo IRRF - Pessoa Física sem considerar tabela progressiva

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira - Fluxus |
| **Rotina:** | Geração de IRRF-PF |
| **Situação/Requisito:** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-7511> |
| **Solução/Implementação:** | Permite a geração de lançamentos IRRF-PF considerando uma alíquota fixa |

**Descrição**

Visando atender situações onde o imposto de renda pessoa física deve ser calculado via alíquota fixa, o sistema foi evoluído para permitir tais situações. A nova classificação de tipo de documento "Gera IRRF-PF Alíquota Fixa" deverá ser utilizada nos lançamentos onde o cálculo do imposto deverá desconsiderar a tabela progressiva.

Nestes casos, o cálculo do imposto de renda pessoa física respeitará a alíquota fixa previamente informada no cadastro do código de receita associado ao cli/for.

Calculo de IRRF-PFtrue1Nova Classificação para o Tipo de Documento

Foi criado com uma nova classificação de tipo de documento, chamada “*Gera IRRF PF – alíquota fixa*”, disponível no cadastro de um novo tipo de documento.

Este documento deverá ser utilizado em todos os lançamentos que deverão gerar IRRF-PF com uma alíquota fixa, determinada no código da receita.

2Inclusão/Baixa de Lançamentos Geradores de IRRF-PF

**Processos de Inclusão e Baixa de lançamentos geradores de IRRF Pessoa Física**

**Inclusão**: Na inclusão de um movimento/lançamento financeiro que possui um Cliente/Fornecedor pessoa física com um tipo de documento financeiro que possua a classificação igual a “**Gera IRFF PF – Alíquota Fixa**” e a data base para geração seja igual a “Emissão/Vencimento/Contab. Inclusão”, o sistema irá verificar qual Código de Receita que está associado/vinculado ao lançamento financeiro e irá realizar o cálculo do IRRF - PF com base na alíquota fixa informada no respectivo código de receita.

**Baixa**: Na baixa de um lançamento financeiro que possui um Cliente/Fornecedor pessoa física com um tipo de documento financeiro que possua a classificação igual a “**Gera IRFF PF – Alíquota Fixa**” e a data base para geração seja igual a “Baixa”, o sistema irá verificar qual o código de Receita que está associado/vinculado ao lançamento financeiro e irá realizar o cálculo do IRRF – PF com base na alíquota fixa informada no respectivo código de receita.
