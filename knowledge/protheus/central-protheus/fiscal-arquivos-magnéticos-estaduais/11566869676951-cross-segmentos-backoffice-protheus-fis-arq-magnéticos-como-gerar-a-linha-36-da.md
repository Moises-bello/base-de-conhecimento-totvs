---
article_id: 11566869676951
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 75c02693b374ec6c1bae4c596d2791e240a1073bf30a53e6bb629b902d89b600
fetched_at: '2026-06-28T22:42:08.997780+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 36 da DAPI?
type: support-article
updated_at: '2023-01-10T18:41:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11566869676951-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-36-da-DAPI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **L****inha 36 - Compras** da **DAPIMG?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A **L****inha 36 - Compras** é  gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** em algumas situações específicas.

O valor de um documento fiscal compõe os valores da **Linha 36**, nos casos em que :

1 - O campo **CFOP** do documento de entrada (**D1\_CF**) contenha: 3101/3102/3126/3127/3651/3652;

2 - O campo **D1\_CF** contenha **3653** e no cadastro da TES o Campo**Credita ICM**S (**F4\_CREDICM** ) esteja diferente de Não;

3 - O cadastro da TES esteja com o Campo **Material de consumo** (**F4\_CONSUMO** diferente de **Sim**)

4 - O campo**D1\_CF** contenha o CFOP **3949**e o campo **Tipo Docto.** (**D1\_TIPO**) Seja **Complemento de ICMS.**
