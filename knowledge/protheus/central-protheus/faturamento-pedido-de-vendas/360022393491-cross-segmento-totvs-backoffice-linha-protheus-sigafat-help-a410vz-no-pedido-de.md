---
article_id: 360022393491
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 6423d57b8f7ce6d48ad8e9aca800a9e3f0e26cfec44dcb58b5d3f6fa02fbf9a5
fetched_at: '2026-06-28T22:38:38.537667+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - HELP: A410VZ
  no Pedido de Venda (MATA410)'
type: support-article
updated_at: '2023-08-15T14:41:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022393491-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-HELP-A410VZ-no-Pedido-de-Venda-MATA410
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16778987858967) Tempo aproximado para leitura: **00:00:30 min****Ocorrência**Ao alterar e manipular um pedido de venda (Rotina MATA410) é exibido o **HELP: A410VZ**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16778973191191)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento – Todas as versões  
  
**Causa**Isso ocorre quando a "Prc Unitario" (C6\_PRCVEN) está igual a "0,00" (zero) e a TES "Tipo Saida" (C6\_TS) colocada não suporta valores zerados (F4\_VLRZERO)   
  
**Solução**Deve-se mudar o preço unitário para um valor maior que zero para que a TES aceite **(Opção 1)**, ou deve-se mudar a TES para aceitar valores zerados **(Opção 2)**. **Opção 1**: Inclua valor no campo "Prc Unitario" (C6\_PRCVEN) no Pedido de Vendas (MATA410)

**Opção 2:** Mude o campo da TES para "Vlr. Zerado" (F4\_VLRZERO) = 1 - Sim. Localizado na aba "Outros" (MATA080)

**Saiba mais:**

* **HELP: A410VZ2:** [MP - FAT - Ao incluir Pedido de Venda do tipo de Complemento de ICMS, apresenta o Help A410VZ2](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiHFlXTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyNzg1NDQ3MS1NUC1GQVQtQW8taW5jbHVpci1QZWRpZG8tZGUtVmVuZGEtZG8tdGlwby1kZS1Db21wbGVtZW50by1kZS1JQ01TLWFwcmVzZW50YS1vLUhlbHAtQTQxMFZaMgY7CFQ6DnNlYXJjaF9pZEkiKWY1MGY5NjI3LTE0ZmMtNGE0Ny05YjU0LWI2MTQ3OWJjNGQzMQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiDEE0MTBWWjIGOwhUOhJyZXN1bHRzX2NvdW50aQs%3D--2c130ed71dc25aa62863fa4ed7ac7480ac11ae82)
* **Caso a descrição do HELP esteja em branco, siga os passos da documentação:** [Framework - Linha Protheus - FRAME - Atualização de Help](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwijG2bTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBgmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyODk2OTg5MS1GcmFtZXdvcmstTGluaGEtUHJvdGhldXMtRlJBTUUtQXR1YWxpemElQzMlQTclQzMlQTNvLWRlLUhlbHAGOwhUOg5zZWFyY2hfaWRJIikwZTI3MjY0MC0wZjdmLTQwZGQtOTJhNi00MmNkNzYxZDA4ZTYGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIj9GcmFtZXdvcmsgLSBMaW5oYSBQcm90aGV1cyAtIEZSQU1FIC0gQXR1YWxpemHDp8OjbyBkZSBIZWxwBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--93015ea0abfb8676bee40562f3b27abad4150a38)
