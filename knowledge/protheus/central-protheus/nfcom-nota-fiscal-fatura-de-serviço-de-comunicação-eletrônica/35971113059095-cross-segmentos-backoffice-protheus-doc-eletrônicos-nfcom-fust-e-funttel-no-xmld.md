---
article_id: 35971113059095
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 42c755796ce3b71d6431b78df77b639eb053271627d5114b9f1248175ec858d0
fetched_at: '2026-06-28T22:39:55.138949+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - FUST e FUNTTEL
  no XML/DANFECOM
type: support-article
updated_at: '2025-11-03T12:57:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35971113059095-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-FUST-e-FUNTTEL-no-XML-DANFECOM
---

**Dúvida**  
Como gerar as contribuições de FUST e FUNTTEL no XML e DANFECOM?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Para gerar essas informações tanto no XML quanto no DANFECOM (Impressão), primeiramente precisará ser realizado a configuração e cálculo [**através do Configurador de Tributos (clique aqui)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35985212819991-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-calcular-o-FUST-FUNTTEL-pelo-Configurador-de-Tributos), visto que via legado não é possível por não gerar tabela/campo para ser considerado pelos fontes.  
  
Uma vez configurado, as alíquotas e valores serão gravadas nas tabelas F2D e CJ3, conforme exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35971119324183)

**IMPORTANTE**  
Após isso, precisará se certificar de estar contemplando as atualizações abaixo no Protheus:  
- **Pacote Acumulado:** [download](https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1171486). [12.1.2410]  
- **Rdmake NFCOMSefaz:** [download](https://suporte.totvs.com/portal/p/10098/download?e=1152113). [12.1.2410]  
  
Por último, ao transmitir e imprimir uma NFCOM, os valores deverão ser apresentados:  
  
**XML**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35971113039255)

**DANFECOM**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/35971224468247)**
