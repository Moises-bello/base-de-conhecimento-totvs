---
article_id: 19485903940247
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 922594288eb5862d577d8405f5eaaf603cf62147009a5af81ceddb94e2a2234a
fetched_at: '2026-06-28T22:42:02.333780+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Erro: Código inválido. O campo deverá existir no Registro 0500 com o campo COD_NAT_CC
  = 01.'
type: support-article
updated_at: '2023-12-05T17:32:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19485903940247-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Erro-C%C3%B3digo-inv%C3%A1lido-O-campo-dever%C3%A1-existir-no-Registro-0500-com-o-campo-COD-NAT-CC-01
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19485908380695) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao validar o arquivo **Sped Fiscal**, ocorre o erro abaixo no registro **0300**:

Código inválido. O campo deverá existir no Registro **0500** com o campo **COD\_NAT\_CC = 01**.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Causa**  
Esse incidente ocorre em duas situações:

**1** - Caso não possua registro **0500** para o código gerado no **0300**

**2** - Conteúdo do campo **CT1\_NTSPED** diferente de **1**.  
  
**Solução**

Conforme determinação do Guia Prático, o campo **06** do registro **0300** segue a seguinte validação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19485878530967)

Para corrigir, segue:

1 - Verifique se gerou o registro **0500** para o código apresentado no **0300**, caso não, segue doc:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010379511-MP-FIS-SPED-FISCAL-Como-gerar-os-registros-0500-e-0600?source=search>

2 - Após o registro **0500** gerado, caso o incidente persista, favor verificar o conteúdo do campo **CT1\_NTSPED** (conta contábil) **= 1** e faça um novo teste.
