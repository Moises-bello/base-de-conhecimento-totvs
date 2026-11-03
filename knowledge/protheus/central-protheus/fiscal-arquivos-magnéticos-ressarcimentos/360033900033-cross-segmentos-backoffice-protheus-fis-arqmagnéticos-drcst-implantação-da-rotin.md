---
article_id: 360033900033
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: 0bffde3daaea2a6ee3366854af39bd902f3e0c4da8992e92e10a2623d3a55e26
fetched_at: '2026-06-28T22:42:12.696781+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DRCST - Implantação
  da rotina para atender a DRCST de SC
type: support-article
updated_at: '2024-06-17T18:16:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033900033-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DRCST-Implanta%C3%A7%C3%A3o-da-rotina-para-atender-a-DRCST-de-SC
---

**Ocorrência**Implantação da rotina para atender a DRCST SC.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para implantar a DRCST no Protheus, realize os seguintes passos:

1. Aplique o patch abaixo de acordo com a release utilizada;  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333-MP-FIS-Atualiza%C3%A7%C3%A3o-do-Ambiente-Fiscal-M%C3%B3dulo-09-para-a-correta-gera%C3%A7%C3%A3o-dos-Arquivos-Magn%C3%A9ticos-fiscais-?source=search>

2. Execute o compatibilizador **UPDDISTR,** após a cópia dos arquivos contidos no pacote de dados diferencial para a pasta **systemload;**Para maiores informações sobre o compatibilizador:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152-MP-FIS-Como-Processar-o-UPDDISTR-para-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rios>

3. Realize a atualização do Menu, incluindo a nova rotina FISA230.  
  
4. Consulte o procedimento para a utilização da rotina no *link*:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=484701377>
