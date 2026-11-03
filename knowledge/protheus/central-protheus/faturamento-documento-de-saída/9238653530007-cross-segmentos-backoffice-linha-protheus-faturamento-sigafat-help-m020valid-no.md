---
article_id: 9238653530007
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 2d9e8e268ed0cafefc7354c8b0bf3ec46cce06b3f013f8c1694eb0060e585d52
fetched_at: '2026-06-28T22:38:45.299039+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Help:
  M020VALID no faturamento'
type: support-article
updated_at: '2024-03-27T19:15:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9238653530007-Cross-Segmentos-Backoffice-Linha-Protheus-Faturamento-SIGAFAT-Help-M020VALID-no-faturamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min** **Dúvida**Ao preparar um Documento de Saída é apresentado o **Help: M020VALID**

![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5279892864535/imagem1.png)  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Versão 12+.  
  
**Solução**O **Help** é apresentado, pois, o campo **FK2\_NATURE** está sendo buscado na tabela **SED - Naturezas** e não está sendo localizado.

Nesse caso, é necessário confirmar o cadastro da Natureza na rotina **FINA010** e certificar que o registro da natureza não está bloqueado (**ED\_MSBLQL = '2 - Nao'** significa que não está bloqueado).

**Saiba mais:**

[Página do Faturamento: **(https://tdn.totvs.com/x/FreLJg)**](https://tdn.totvs.com/x/FreLJg)
