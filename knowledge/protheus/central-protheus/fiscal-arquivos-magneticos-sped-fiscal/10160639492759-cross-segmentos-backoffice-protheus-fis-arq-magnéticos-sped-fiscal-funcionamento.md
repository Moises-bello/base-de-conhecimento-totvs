---
article_id: 10160639492759
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 421040ad8032b134130568bb760836a3ae57159edc37371c1ec0274c26912c75
fetched_at: '2026-06-28T22:42:02.340816+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Funcionamento da FISA116 para o Bloco H no Sped Fiscal
type: support-article
updated_at: '2022-11-11T15:29:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10160639492759-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Funcionamento-da-FISA116-para-o-Bloco-H-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**  
Como funciona a rotina FISA116 referente ao Bloco H do Sped Fiscal?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

**Parametrizações e critérios relevantes referente a FISA116 no Bloco H do Sped Fiscal:**

**[FISA116 - BLOCO H](https://tdn.totvs.com/pages/releaseview.action?pageId=702825120#SPDFISComposi%C3%A7%C3%A3odevalorespararegistroH020doarquivomagn%C3%A9ticoSPEDFiscal-Passosparaagera%C3%A7%C3%A3oH020viaFISA116)**

**Importante:**

Quando for necessário informar mais de um fechamento de inventário deve ser utilizada rotina de motivo de inventario (FISA120)

[Motivo do Inventário - Sped Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028666152-MP-FIS-Motivo-de-Inventario-Bloco-H-SPED-Fiscal)

**H020 pela FISA116:**

<https://tdn.totvs.com/display/public/PROT/ARQ0013_H020_SPED_FISCAL>

Incluído ponto de entrada SPEDALTH para processamento do registro H010 SPED FISCAL.

Através desde ponto de entrada é possível enviar tabela temporária que será processada pela rotina SPED FISCAL e Composição do registro H020 (FISA116) sem que seja processado Estoque.

[SPEDALTH - Ponto de entrada](https://tdn.totvs.com/display/public/PROT/PE+-+SPEDALTH+-+SPEDFISCAL+-+Registro+H010)
