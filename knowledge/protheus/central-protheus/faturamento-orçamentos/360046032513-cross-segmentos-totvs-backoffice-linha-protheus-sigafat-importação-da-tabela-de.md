---
article_id: 360046032513
category: Faturamento - Orçamentos
content_hash: 398fc99c7e571fae75e44d343ec39fa4b84ff31b6033a3ef71abf2359f208b2a
fetched_at: '2026-06-28T22:38:24.976043+00:00'
product: protheus
section_id: 1500001539281
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Importação
  da Tabela de Preços (OMSA010) via Mile
type: support-article
updated_at: '2023-05-19T19:32:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046032513-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Importa%C3%A7%C3%A3o-da-Tabela-de-Pre%C3%A7os-OMSA010-via-Mile
---

**Dúvida**

Ao importar o **layout** **mile** da **tabela de preço** (**OMSA010**), gera a mensagem: Erro Fatal: Não há dados de cabeçalho.

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - todas as versões.  
  
**Solução**

Na importação da Tabela de Preços (OMSA010) é necessário utilizar como separador o **pipe** ( **|**) conforme exemplo abaixo:  
  
**Layout com erro:**  
A;TESTE01;20191215;  
B;0001;FAT000000000000000000000000002;1000.00;AC,20191215;  
B;0002;FAT000000000000000000000000002;1500.00;SP,20191215;

Veja que neste layout de txt, as informações estão separadas por ponto e vírgula, gerando inconsistência na leitura.

**Layout correto**:  
|A|TESTE01|20191215|  
|B|0001|FAT000000000000000000000000002|1000.00|AC|20191215|  
|B|0002|FAT000000000000000000000000002|1500.00|SP|20191215|  
  
Desta forma, corrija o layout seguindo o modelo acima e efetue o processo com o **adapter MVC ou MSEXECAUTO.**

**Saiba mais:**

**[MP - FAT - Uso da Integração Mile no Modulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043730774-MP-FAT-Uso-da-Integra%C3%A7%C3%A3o-Mile-no-Modulo-Faturamento)**

[**Mile Importação e Exportação do Layout**](https://tdn.totvs.com/x/KrJEGQ)

[**MILE - Model Integrator Layout Engine**](https://tdn.totvs.com/x/kYQbCQ)
