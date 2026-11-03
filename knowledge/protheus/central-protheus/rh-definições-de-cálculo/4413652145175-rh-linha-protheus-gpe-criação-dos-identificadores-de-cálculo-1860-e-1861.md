---
article_id: 4413652145175
category: RH - Definições de Cálculo
content_hash: 77d87c7a0d4feae08be154749c28599dc37a584e460f2ebf17d385e146d5be6e
fetched_at: '2026-06-28T22:43:22.235849+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE -  Criação dos identificadores de cálculo 1860 e
  1861
type: support-article
updated_at: '2026-06-26T16:42:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413652145175-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-dos-identificadores-de-c%C3%A1lculo-1860-e-1861
---

**Dúvida**Como realizar o cadastro dos identificadores 1860 e 1861?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O sistema não apura no segundo cálculo de Férias o valor correto da verba ID 0232 (INSS Férias Mês Seguinte para Desconto no Mês Corrente), mesmo após ativação do mnemônico P\_MULTV e Funcionário com dois vínculos, sendo múltiplo vinculo do mesmo Grupo Econômico, Filiais diferentes e Férias partidas.  
  
Dessa forma, foram criados os seguintes ID´s de Cálculos, para apuração correta do segundo cálculo da verba ID 0232:  
**> ID 1860** - Base INSS Férias Mês seguinte outras Empresas  
**> ID 1861** - INSS Férias Mês seguinte outras Empresas  
  
  
**Saiba Mais:**  
[DT Inconsistência no INSS Férias Mês Seguinte do vínculo 02 - Múltiplos Vínculos](https://tdn.totvs.com/pages/viewpage.action?pageId=626145163)  
[Manual do Cálculo de Múltiplos Vínculos](https://tdn.totvs.com/pages/viewpage.action?pageId=552575179)
