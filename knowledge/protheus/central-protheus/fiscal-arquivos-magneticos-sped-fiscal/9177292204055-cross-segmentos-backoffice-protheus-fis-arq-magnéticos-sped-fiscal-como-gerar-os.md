---
article_id: 9177292204055
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: a4a1d85a100164fe9ebe01d872879fb66e92eb20bc0277474a4c05882b02a76d
fetched_at: '2026-06-28T22:42:02.273169+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar os registros E111 e E113 automaticamente do arquivo Sped Fiscal?
type: support-article
updated_at: '2024-06-04T20:25:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9177292204055-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-os-registros-E111-e-E113-automaticamente-do-arquivo-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23952688121751) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar os registros E111 e E113 no arquivo do Sped Fiscal?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

1-       Parâmetros

MV\_ESTADO = SP   -> Deve ser o estado que está sendo gerado apuração

MV\_USASPED = .T.

MV\_P9SPED = .F.

MV\_P9AUTO = F

MV\_STUF=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO

MV\_STUFS=AC/AL/AM/AP/BA/CE/DF/ES/GO/MA/MT/MS/MG/PA/PB/PR/PE/PI/RN/RS/RJ/RO/RR/SC/SP/SE/TO

**MV\_SUBTRIB** = preenchido com estado + inscrição estadual (todos os estados que possuírem inscrição estadual para recolhimento do ICMS ST)

**MV\_ESTE113** informando a UF que gerará o registro E113

**Iremos prosseguir seguindo os passos:**

2 - Inclua uma TES conforme à sua necessidade, porém anexando informações nos campos abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11620831520023)

3 - Após configurar a TES, execute a inclusão da NF que deseja e informando a TES configurada de acordo, automaticamente será alimentado na aba de lançamento de apuração:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11620847760663)

4 - Após a inclusão da nota, verifique na apuração de ICMS se preencheu a tabela CDH com o código de ajuste utilizado na rotina MATA953:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11620873450519)

5 - Rode à apuração e acesse a rotina do Sped Fiscal para geração do registro.

Lembrando que o período apurado na wizard na geração do arquivo deve estar abrangendo o período determinado dos campos CDH\_DTINI e CDH\_DTFIM.

Ao gerar o arquivo do Sped Fiscal será apresentado o registro:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11620878291607)

**Informações****adicionais:**

**Manual Utilização SPEDFISCAL**

<https://tdn.totvs.com/pages/releaseview.action?pageId=238035285#FIS0009_Manual_Utiliza%C3%A7%C3%A3o_SPEDFISCAL-REGISTROE113:INFORMA%C3%87%C3%95ESADICIONAISDOSAJUSTESDAAPURA%C3%87%C3%83ODOICMS%E2%80%93IDENTIFICA%C3%87%C3%83ODOSDOCUMENTOSFISCAIS>.
