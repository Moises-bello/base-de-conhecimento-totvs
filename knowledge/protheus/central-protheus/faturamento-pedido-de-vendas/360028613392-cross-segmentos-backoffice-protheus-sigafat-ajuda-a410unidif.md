---
article_id: 360028613392
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: e15f66c66ccd08f737603d5e9a3ac2dd37f4548bce3db4462c2f31f0e8754dea
fetched_at: '2026-06-28T22:38:39.625010+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFAT - Ajuda: A410UNIDIF'
type: support-article
updated_at: '2024-09-23T20:57:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028613392-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Ajuda-A410UNIDIF
---

**Ocorrência**

O que fazer quando gera o Help **A410UNIDIF**  ou Ajuda: A410UNIDIF no Faturamento?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 11.80.

**Causa**

Esse incidente ocorre devido a inconsistência nas configurações da Base de Dados. Diferenças de Tamanho e Casas Decimais entre os campos das Tabelas utilizadas no processo e no recálculo.

Pois quando o sistema faz o cálculo do valor de um campo **X** (**C6\_PRCVEN**, por exemplo), ele utiliza vários outros campos no cálculo, e se não estiverem padronizados, as últimas casas decimais serão perdidas em alguma das tabelas, impactando no valor final considerado e levado para o campo de destino.

**Solução**

Verifique se os campos de **quantidade** e **valor** das tabelas **SC6**, **SD1** e **SB6** estão com a quantidade de **decimais iguais**, conforme a documentação:

* [Aumento de Casas Decimais no ambiente Faturamento (SIGAFAT)](https://tdn.totvs.com/x/twEmDg)

Para garantir que todos os campos relacionados estejam padronizados, utilize os [**Grupos de campos Numéricos**](https://youtu.be/BXPL4BPr668?si=ZcVvWgMGujYV1ap5). Assim todos os campos de **quantidade** ficarão com as mesmas configurações, assim como todos os campo de **valor** dependendo do Grupo que utilizar para o ajuste.

**Após** **ajustar** os campos, verifique a possibilidade de **executar**algumas rotinas de recálculos disponibilizados pelo sistema, que podem ajustar os campos que possuem dados incorretos:

* FATURAMENTO > Miscelanea > Ajustes > **Refazer Acumulados** (**MATA215**)
* FATURAMENTO > Miscelanea > Ajustes > **Refazer Poder de Terceiros** (**MATA216**)
* FINANCEIRO > Miscelanea > Recalculos > **Refaz Dados Clientes e Fornecedores** (**FINA410**)
* ESTOQUE/CUSTOS > Miscelanea > Processamentos > **Refaz Saldos** (**MATA300**)

Saiba mais sobre outros Helps no pedido:

**[MP-FAT-Help-A410TOTAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007798262-MP-FAT-Help-A410TOTAL)**

**[MP-FAT-Help-A100VALOR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004315022-MP-FAT-Help-A100VALOR)**
