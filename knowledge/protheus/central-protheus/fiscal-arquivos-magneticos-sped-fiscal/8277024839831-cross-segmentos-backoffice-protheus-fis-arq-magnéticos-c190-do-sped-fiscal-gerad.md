---
article_id: 8277024839831
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 4fb4e612f0c666e787aba1d29bd93a0d7b4c9e9216008450c93d7bb2c692c5b7
fetched_at: '2026-06-28T22:42:00.843073+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos - C190 do
  Sped fiscal gerado com CST incorreto '
type: support-article
updated_at: '2022-08-19T12:16:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8277024839831-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-C190-do-Sped-fiscal-gerado-com-CST-incorreto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No campo **02 - CST\_ICMS** do registro **C190** do **Sped Fiscal** o **CST** apresentado não condiz com o informado no campo **Sit. Trib.ICM - F4\_SITTRIB**  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Causa**O problema ocorre quando a operação realizada envolve cliente/fornecedor optante pelo **Simples Nacional** (campos **Opt Simp Nac - A1\_SIMPNAC/A2\_SIMPNAC = 1)** e o campo **Cod Sit SN - F4\_CSOSN** está preenchido com conteúdo distinto do campo **Sit. Trib.ICM - F4\_SITTRIB.**Neste cenário, o campo **FT\_CSOSN** é alimentado com o conteúdo do  **Cod Sit SN - F4\_CSOSN** e o Protheus carrega o **CST** do campo **FT\_CSOSN** para o campo **02 do C190.**

**Solução**

Para que o **CST** apresentado seja o informado no campo **FT\_CLASFIS** (que é alimentado pelo conteúdo do campo  **Sit. Trib.ICM - F4\_SITTRIB)** a movimentação não pode ser com participante  optante pelo  **Simples Nacional**.

Quando o participante é optante pelo **Simples Nacional** é preciso informar o **CST** correto no campo **Cod Sit SN - F4\_CSOSN.**

Para os novos lançamentos utilize o cadastro de **TES** já com a informação correta no campo e para as documentos já lançados corrija a informação no cadastro de **TES**,  reprocesse as notas e gere novamente o **Sped Fiscal**.
