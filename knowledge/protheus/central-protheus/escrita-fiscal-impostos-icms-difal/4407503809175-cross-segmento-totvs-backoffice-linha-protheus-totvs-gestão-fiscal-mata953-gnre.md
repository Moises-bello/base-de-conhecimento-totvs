---
article_id: 4407503809175
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 2ab5ec562720b44793de5d0fb40231562437de65016a30686f89c46b0dd4182a
fetched_at: '2026-06-28T22:39:19.225728+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  MATA953 - GNRE Difal/FECP e Configurações por UF
type: support-article
updated_at: '2025-01-10T20:04:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407503809175-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-MATA953-GNRE-Difal-FECP-e-Configura%C3%A7%C3%B5es-por-UF
---

**Dúvida**Como configurar para que as Guias de Difal (EC 87) e FECP sejam separadas ou unificadas na rotina de apuração do ICMS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**As GNRE's do Difal e do FECP poderão ser geradas em uma única GNRE se necessário, através do parâmetro **MV\_GNREDF**.

O parâmetro **MV\_GNREDF** pode ser preenchido de formas distintas:

1 (Padrão): Serão geradas GNRE's separadas de DIFAL e FECP para todas as UF's.

2: Será gerada GNRE única de DIFAL + FECP para todas as UF's.

Caso seja necessário definir estados específicos para os quais deve ser gerada uma única GNRE basta informar as UF's separadas por barra, da seguinte forma: SP/RJ/MG. Desta forma será gerada uma GNRE única de DIFAL + FECP apenas para as UF's informadas no parâmetro.

Mais informações sobre Apuração do Difal (EC 87):  
<https://tdn.totvs.com/pages/releaseview.action?pageId=224105637>
