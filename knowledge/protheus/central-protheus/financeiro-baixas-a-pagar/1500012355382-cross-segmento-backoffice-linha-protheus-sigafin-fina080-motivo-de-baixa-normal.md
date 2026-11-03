---
article_id: 1500012355382
category: Financeiro - Baixas a Pagar
content_hash: 088aba0172dd610852021c6bf18e52ea433684b633aec76d39d51e45bf38265d
fetched_at: '2026-06-28T22:37:24.866409+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA080 - Motivo de
  baixa normal não contabiliza
type: support-article
updated_at: '2026-05-27T19:03:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012355382-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Motivo-de-baixa-normal-n%C3%A3o-contabiliza
---

**Dúvida**  
Por que motivo de baixa normal não contabiliza?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Ocorrência**  
A contabilização ocorre normalmente quando o motivo de baixa utilizado é **Débito CC**. Porém, ao utilizar o motivo de baixa **NOR (Normal)**, não há geração de contabilização.

**Solução**  
No motivo de baixa **NOR (Normal)**, o sistema não gera movimentação bancária e, consequentemente, não realiza a contabilização. O processo contábil ocorre apenas quando existe movimentação bancária vinculada à baixa.

Caso seja necessário que a contabilização também ocorra para baixas com motivo **NOR (Normal)**, o parâmetro **MV\_CTBAIXA** deve estar configurado com o conteúdo **“A”.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019781601)

**Saiba mais**  
[Lançamento Padrão](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)
