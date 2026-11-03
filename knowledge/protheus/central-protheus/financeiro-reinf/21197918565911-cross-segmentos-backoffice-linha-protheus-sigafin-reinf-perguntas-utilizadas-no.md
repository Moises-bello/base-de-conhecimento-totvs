---
article_id: 21197918565911
category: Financeiro - Reinf
content_hash: 2793f60555c1869e138cfca86f536445d4be9bc1148fc86ac15ee87e755a786c
fetched_at: '2026-06-28T22:37:51.729974+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: ' Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Perguntas
  utilizadas no extrator de dados do Financeiro para o TAF'
type: support-article
updated_at: '2024-02-08T15:17:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21197918565911--Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Perguntas-utilizadas-no-extrator-de-dados-do-Financeiro-para-o-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21197906852247) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Perguntas utilizadas no extrator de dados do financeiro para o TAF  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**Para extração dos dados financeiros para o **TAF**, são consideradas apenas as perguntas contidas das seguintes "**abas**" do **extrator**:

* + "**Aba**" **Geração**

![](https://tdn.totvs.com/download/attachments/317302431/image-2023-10-31_16-21-24.png?version=1&modificationDate=1698780084910&api=v2)

* + "**Aba**" **Financeiro**

![](https://tdn.totvs.com/download/attachments/317302431/image-2023-10-31_16-22-25.png?version=1&modificationDate=1698780145353&api=v2)

As perguntas das demais "**abas**" não são consideradas para exportação dos dados financeiros para o **TAF**.

**Importante:**Na "Aba" **Financeiro** o filtro **1- Data de contabilização** ira filtrar as informações do campo   
**(E1\_EMIS1/E2\_EMIS1)**, e o filtro **2 - Data de emissão** ira filtrar as informações do campo   
**(E1\_EMISSAO/E2\_EMISSAO)****![](https://centraldeatendimento.totvs.com/hc/article_attachments/21197906856983)**

**Atenção:** Caso a nota fiscal possua emissão em um mês e entrada em outro mês, por exemplo, emissão 29/01 e entrada 02/02, as perguntas da aba **Financeiro** precisam seguir esse cenário. Neste caso o layout **T154** do titulo só será integrado com sucesso no **TAF** com a opção **2 - Contabilização**, caso contrário irá ocorrer erro ao integrar o **layout T154**.  
  
**Saiba mais:**   
[DT Extrator Financeiro para o TAF - REINF](https://tdn.totvs.com/display/public/PROT/DT+Extrator+Financeiro+para+o+TAF+-+REINF)
