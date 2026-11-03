---
article_id: 28111633502359
category: Rental by ItUp Business
content_hash: e1b32a4716fe862af561a27106b4f12c2a4996d60e2d3728704e80592667355f
fetched_at: '2026-06-28T22:36:20.680563+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Problema na numeração da
  Nota Fiscal durante a emissão de Nota Fiscal de Remessa pela rotina Orçamento (LOCA001).
type: support-article
updated_at: '2026-04-09T13:00:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28111633502359-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Problema-na-numera%C3%A7%C3%A3o-da-Nota-Fiscal-durante-a-emiss%C3%A3o-de-Nota-Fiscal-de-Remessa-pela-rotina-Or%C3%A7amento-LOCA001
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28111620654359) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Problema na numeração da Nota Fiscal durante a emissão de Nota Fiscal de Remessa pela rotina Orçamento (LOCA001).  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - P12.1.2310  
  
**Causa**  
Ao gerar a Nota Fiscal de Remessa pela rotina de **Orçamento** (**LOCA001**), quando o parâmetro **MV\_GERNFS** está configurado como **".T."**, o sistema exibe a mensagem de erro: "**Problema na Numeração NF"**.  
  
![Captura de tela 2024-11-27 103351.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28111620657047)  
  
**Solução**

Para solucionar essa ocorrência, siga os passos abaixo:

1. **Verifique a configuração do parâmetro MV\_LOCX201 (Série usada para emitir NF REMESSA):** Certifique-se de que uma série válida esteja configurada para emissão da Nota Fiscal de Remessa.
