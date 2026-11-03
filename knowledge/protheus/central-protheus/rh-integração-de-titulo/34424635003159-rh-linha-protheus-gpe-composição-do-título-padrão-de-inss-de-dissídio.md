---
article_id: 34424635003159
category: RH - Integração de Titulo
content_hash: 1bfb9251231c2519aadff400bbcbc243bd043cf7a0031e9fef332b6063ecb567
fetched_at: '2026-06-28T22:43:37.150731+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Composição do Título Padrão de INSS de Dissídio
type: support-article
updated_at: '2025-08-25T20:10:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34424635003159-RH-Linha-Protheus-GPE-Composi%C3%A7%C3%A3o-do-T%C3%ADtulo-Padr%C3%A3o-de-INSS-de-Diss%C3%ADdio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34424634982935) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Quais são as verbas que compõem o Título Padrão de INSS de Dissídio?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Utilizando a opção Padrão de Título de INSS de Dissídio, o Protheus verifica a existência de rescisão complementar por dissídio, buscando no Histórico de Movimentos (SRD) e Itens de Férias e Rescisões (SRR) do período, e não havendo, segue a busca com os valores do Acumulado Dissídio (tabela RHH) nos IDs:  
    0340 Valor INSS Diferenca Dissidio    
    0401 Valor INSS Diferenca Dissidio 13º  
    0943 INSS Empresa Dissidio  
    0944 Contr. Terceiros Dissidio  
    0945 Contr. Acidente Trabalho Dissidio                  
    e a Verba para Pagto.Dissidio (RV\_CODCOM\_) do Id 0040-Auxílio Maternidade caso informada.

As deduções são compostas pelos proventos e descontos com Deducao da Guia de INSS=S (RV\_DEDINSS),  
ou cuja Verba Origem (RHH\_VB) seja a do Id 0670-Deducao Salario Maternidade de 13o salario na GPS,  
além dos avos dos Ids abaixo conforme os parâmetros MV\_LIMDMAT e MV\_SALMGRP:  
    0040 Auxílio Maternidade   
    0407 Pagamento de Médias Auxílio Maternidade  
    1338 ATS Maternidade       
    1339 Insalubridade Maternidade  
    1340 Periculosidade Maternidade  
    1341 Adic. Cargo Confiança Maternidade  
    1342 Adic. Transferencia Maternidade

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34424651342615)

**Saiba Mais:**  
[Composição dos Títulos Padrões](https://tdn.totvs.com/pages/releaseview.action?pageId=976128352)   
[RH - Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
