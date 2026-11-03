---
article_id: 11496971262103
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: a99b4743db2658acfa400bd1925cfc149ba9fa01f3bf625294a32b92115abdae
fetched_at: '2026-06-28T22:42:08.960629+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 26 da DAPI?
type: support-article
updated_at: '2023-01-09T13:05:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11496971262103-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-26-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar a **linha 26 - Compras** da **DAPI?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A linha **linha 26 - Compras**é gerada com base nos valores totais das operações do período lançadas no livro **Registro de Entradas** quando:

1. O campo **CFOP** do documento de entrada  **D1\_CF** contenha alguma das **CFOPS** abaixo: **2101/2102/2111/2113/2116/2117/2118/2120/2121/2122/2124/2125/2126/2401/2403/2501/2651/2652**  
  
2. O campo **D1\_CF** contenha = **2653** e no cadastro da **TES** o Campo **Credita ICMS (F4\_CREDICM)** esteja **diferente de Não**.

3. No cadastro da **TES** o Campo **Material de consumo (F4\_CONSUMO)** estiver diferente de **Sim**  
  
4. No campo **D1\_CF** contenha o **CFOP 2949** e o campo **Tipo Docto.** **(D1\_TIPO)** Seja **Complemento de  ICMS.**
