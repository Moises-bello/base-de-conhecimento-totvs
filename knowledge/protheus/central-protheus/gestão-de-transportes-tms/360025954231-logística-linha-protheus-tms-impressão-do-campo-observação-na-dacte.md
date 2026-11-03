---
article_id: 360025954231
category: Gestão de Transportes (TMS)
content_hash: af45112b7008b028b0692004d0159a44be8516dc6a9e34943c83b93e3a167aab
fetched_at: '2026-06-28T22:45:29.306398+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Impressão do campo observação na DACTE
type: support-article
updated_at: '2024-09-04T13:55:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025954231-Log%C3%ADstica-Linha-Protheus-TMS-Impress%C3%A3o-do-campo-observa%C3%A7%C3%A3o-na-DACTE
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26124112865943)*** Tempo aproximado para leitura: **00:00:35 min****Dúvida**Como imprimir texto no campo de **observação** da **DACTE - Documento Auxiliar do Conhecimento de Transporte Eletrônico**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões.  
  
**Solução**Para a impressão de uma informação no campo de observação da **DACTE**, existe duas opções:

* No campo **Observação - DTC\_OBS,** na **Entrada Documentos de Clientes - TMSA050**- Se o preenchimento ocorrer neste campo apenas o **CT-e - Conhecimento de Transporte eletrônico**, gerado para este lote terá a informação.
* No campo **Msg. Fiscal - DUG\_CODMSG**, na **Regras de Tributação - TMSA410** - Se o preenchimento ocorrer neste campo, todos os **CT-e** que utilizarem essa **TES - Tipos de Entrada e Saída** para o cálculo terão a observação na impressão.

Vale reforçar que a impressão da **DACTE** é feita através do *rdmake* **RTMSR35**, que é customizável, e pode ser alterado para realizar a impressão conforme sua necessidade, seguindo as regras do manual da **SEFAZ - Secretaria da Fazenda**.
