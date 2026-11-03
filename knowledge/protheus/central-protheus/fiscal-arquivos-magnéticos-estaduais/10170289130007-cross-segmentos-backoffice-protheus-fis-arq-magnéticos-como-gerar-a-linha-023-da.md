---
article_id: 10170289130007
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: a4170eb2baae008cb5fe883a8f474ff8bce6d21217d9872fe05b38355c45d2b9
fetched_at: '2026-06-28T22:42:08.943326+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a linha 023 da DAPIMG?
type: support-article
updated_at: '2024-06-13T17:31:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10170289130007-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-linha-023-da-DAPIMG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar a **linha 023 - Uso e Consumo** da **DAPIMG?**  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A linha **023 - Uso e Consumo** é gerada com base nos valores totais das operações do período  lançadas no livro **Registro de Entradas** com algumas **CFOPs** específicas.

Para que o valor de um documento fiscal componha os valores da **Linha 23**, no campo **Cod. Fiscal - D1\_CF** do lançamento deve conter uma das seguintes**CFOPs**:1407/1556/1557 

ou

O campo **Cod. Fiscal - D1\_CF**  contenha a **CFOP 1653** e no cadastro de  TES utilizado na escrituração, os campos **Credita ICMS - F4\_CREDICM =**  Não e o campo **Material de Consumo - F4\_CONSUMO** = Sim.
