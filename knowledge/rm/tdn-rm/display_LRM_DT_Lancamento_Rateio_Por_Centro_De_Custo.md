---
content_hash: 06580357b121ad11d6f5069746774a975b4aeb8fa7d4d02686debca139f54982
fetched_at: '2026-06-29T00:06:14.633056+00:00'
page_id: '210048134'
product: rm
source: tdn-rm
title: DT_Lancamento_Rateio_Por_Centro_De_Custo
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Lancamento_Rateio_Por_Centro_De_Custo
version: 3
---

# GERAÇÃO DE LANÇAMENTOS RATEADOS POR CENTRO DE CUSTO - BUSCANDO O CENTRO DE CUSTO DA SEÇÃO

## Características do Requisito

| **Linha de Produto:** | *RM* |
| --- | --- |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | | **Rotina** | **Nome Técnico** | | --- | --- | | *Rateio* | *Centro de Custo* | |
| **Versões/Release:** | *12.1.5* |

## Descrição

O parâmetro “Utilizar centro de custo da seção”, pode ser selecionado quando as opções, “Gerar lançamentos financeiros” e “Ratear lanctos rateados por centro de custo” também estiverem marcados.  
Caso o parâmetro seja marcado é inserido além do lançamento o rateio por centro de custo para o centro custo cadastrado na seção do usuário.

## Procedimento para Utilização

**Considere os 3 funcionários abaixo, para cada um observe a seção, e a configuração do Rateio Tomadores:**

Denise Fraga  
Seção 01.03 DAP – Depto Administrativo

Rateio Tomadores

Adriana Teixeira Lobo  
Seção 01.02 COM – Depto Pessoal

Rateio Tomadores:

Tereza Lima Pereira Soares  
Seção 01.04 PDE – Depto Pesquisa e Desenvolvimento

Rateio Tomadores:

**Detalhamento das seções, de onde é buscado o Centro de Custo.**

Seção 01.03 DAP – Depto Administrativo  
Centro Custo 01 Administrativo

Seção 01.02 COM – Depto Pessoal  
Centro de Custo 05 Representantes

Seção 01.04 PDE – Depto Pesquisa e Desenvolvimento  
Centro de Custo 04 Filial

**Geração do SEFIP, ou Guia de INSS**

Executando o processo “Geração do SEFIP”, ou “Guia de INSS” para cada funcionário individualmente são gerados os lançamentos rateados por Tomador/CEI.

00048 - Denise Fraga

00019 - Adriana Teixeira Lobo

00018 - Tereza Lima Pereira Soares

**Parâmetros**

O parâmetro ‘Usar centro de custo da seção’ nos processos ‘Geração do SEFIP’ e ‘Guia de INSS’ é ativado caso o parâmetro global ‘Usa Centro de Custo’ esteja desmarcado, caso contrário, estará desabilitado.

Executando o processo “Geração do SEFIP” para todos os funcionários, os lançamentos gerados:

Para cada lançamento foi gerado rateio de centro de custo, de acordo com o centro de custo cadastrado na seção do Funcionário:

Lançamento 7273

Lançamento 7274

Lançamento 7275

Lançamento 7276
