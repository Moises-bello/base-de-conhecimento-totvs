---
article_id: 8863047146135
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: b9f541a7f38001faa73be7f914e3ac1aa3d644b892ff6787d2bec221bdcb8142
fetched_at: '2026-06-28T22:42:08.912499+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  a coluna 11- Outras da DAPIMG com redução de base de ICMS? '
type: support-article
updated_at: '2022-09-14T12:12:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8863047146135-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-coluna-11-Outras-da-DAPIMG-com-redu%C3%A7%C3%A3o-de-base-de-ICMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:02:00 min** **Dúvida**Como gerar a **Coluna 11- Outras** da **DAPI MG** com **redução de base de ICMS**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12

**Solução**

Para gerar a **Coluna 11 - Outras** da **DAPI MG** com **Redução de Base de Cálculo,** o **Protheus** valida os documentos fiscais escriturados com cadastro de **TES** em que os campos abaixo estejam configurados da seguinte forma:

* **Sit.Trib.ICM (F4\_SITTRIB)** = **20 - Com Redução de Base de Cálculo**
* **%Red. do ICMS (F4\_BASEICM)** = Preenchido
* **Livro Fiscal ICMS (F4\_LFICM)**= **Outras**

O Valor considerado na coluna é o gravado no campo**Vlr Out ICMS (FT\_OUTRICM)**, na tabela **LIVRO FISCAL POR ITEM DE NF (SFT).**
