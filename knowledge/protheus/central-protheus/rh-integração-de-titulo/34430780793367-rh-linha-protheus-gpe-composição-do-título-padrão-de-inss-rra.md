---
article_id: 34430780793367
category: RH - Integração de Titulo
content_hash: ce961307a5596f346181ba6753cd2834e55a6f24b623178f4a4483f44f597d9c
fetched_at: '2026-06-28T22:43:37.143654+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Composição do Título Padrão de INSS - RRA
type: support-article
updated_at: '2025-08-25T20:12:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34430780793367-RH-Linha-Protheus-GPE-Composi%C3%A7%C3%A3o-do-T%C3%ADtulo-Padr%C3%A3o-de-INSS-RRA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34430805952151) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Quais são as verbas que compõem o Título Padrão de INSS de RRA?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
  
Utilizando a opção Padrão de Título de INSS - RRA, o Protheus gera os valores de Resumo da Folha (tabela SRZ) à partir das tabelas de Movimento do Período (SRC) ou Histórico de Movimentos (SRD), efetuando processamento por tipo de contrato e gera os Títulos com valores dos Identificadores de Cálculo:  
    0148 INSS Empresa  
    0149 Percentual de Terceiros  
    0150 Percentual Acidente Trabalho (e exceto para produtor rural - Código de pagamento GPS 2607)  
    0975 Contr. Previdenciaria RRA      
    0980 Contr. Previdenciaria 13º RRA  
    deduzindo o Id 1412 Devolução INSS (Ferias com aliquota superior)

Para produtor rural, caso informadas na S035 as verbas de ID:  
    0315 Valor Produtor Rural PF  
    0316 Valor Produtor Rural PJ  
    e o percentual de encargo de SENAR (S038)

As deduções são compostas pelos proventos e descontos com Deducao da Guia de INSS=S (RV\_DEDINSS), além dos avos dos Ids abaixo conforme os parâmetros MV\_LIMDMAT e MV\_SALMGRP:  
    0040 Auxílio Maternidade   
    0407 Pagamento de Médias Auxílio Maternidade  
    1338 ATS Maternidade       
    1339 Insalubridade Maternidade  
    1340 Periculosidade Maternidade  
    1341 Adic. Cargo Confiança Maternidade  
    1342 Adic. Transferencia Maternidade

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34430805953303)

**Saiba Mais:**  
[Composição dos Títulos Padrões](https://tdn.totvs.com/pages/releaseview.action?pageId=976128352)   
[RH - Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
