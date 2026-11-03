---
article_id: 8390716138647
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 54bfeae4a5196354ea98cabce034f1ac004254ab1c6b31182dc106dacf103928
fetched_at: '2026-06-28T22:38:45.409241+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Configurar
  NF de entrada para ter controle de numeração pela SD9
type: support-article
updated_at: '2022-11-28T13:12:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8390716138647-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configurar-NF-de-entrada-para-ter-controle-de-numera%C3%A7%C3%A3o-pela-SD9
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como configurar o sistema para considerar Nota Fiscal de Entrada no controle de numeração pela tabela SD9.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento – SIGAFAT - Protheus 12 ou superior.  
  
**Solução**Tenha previamente a numeração que comporte o controle pela **SD9**. [**Ajustes** e parâmetro **MV\_TPNRNFS = 3**]. Veja nosso vídeo sobre como realizar a configuração em: [**Controle de Numeração via SD9**](https://www.youtube.com/watch?v=3CUmcFtV2d4&t=1s)

1 - Incluir um documento de entrada (**Rotina MATA103)**  
2 - No cabeçalho do documento de entrada, deixe o campo **"Form. Prop = "Sim"**  
3 - Ao salvar o documento de entrada, na última etapa, é mostrado a **janela pop-up de numeração**, basta escolher a numeração e a série desejada

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8390567211415/mceclip0.png)

4 - Visualizar na [Rotina MATA012] o documento/registro gerado

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8390638756631/mceclip2.png)

**Saiba mais:** [Controle de Numeração do Documento de Saída no Protheus](https://tdn.totvs.com/x/Q4ScEw)
