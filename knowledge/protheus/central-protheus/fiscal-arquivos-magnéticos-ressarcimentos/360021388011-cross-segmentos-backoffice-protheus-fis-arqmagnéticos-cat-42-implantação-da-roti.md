---
article_id: 360021388011
category: Fiscal Arquivos Magnéticos - Ressarcimentos
content_hash: eb4f9f1256687d36cd16ea3edd98264f60358ff8dfe41555d2f30d9f45f6223c
fetched_at: '2026-06-28T22:42:12.682860+00:00'
product: protheus
section_id: 1500001546642
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - CAT 42 - Implantação
  da rotina para atender a Portaria CAT 42
type: support-article
updated_at: '2022-08-18T17:54:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021388011-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CAT-42-Implanta%C3%A7%C3%A3o-da-rotina-para-atender-a-Portaria-CAT-42
---

**Ocorrência**Implantação da rotina para atender a Portaria CAT 42.  
  
**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**Para implantar a CAT 42 no Protheus, realize os seguintes passos:

1. Aplique o patch abaixo de acordo com a release utilizada;  
  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333-MP-FIS-Atualiza%C3%A7%C3%A3o-do-Ambiente-Fiscal-M%C3%B3dulo-09-para-a-correta-gera%C3%A7%C3%A3o-dos-Arquivos-Magn%C3%A9ticos-fiscais-?source=search>

2. Execute o compatibilizador **UPDDISTR,** após a cópia dos arquivos contidos no pacote de dados diferencial para a pasta **systemload;**Para maiores informações sobre o compatibilizador:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024320152-MP-FIS-Como-Processar-o-UPDDISTR-para-atualiza%C3%A7%C3%A3o-de-dicion%C3%A1rios>

3. Realize a atualização do Menu, incluindo a nova rotina FISA190.  
  
4. Consulte o procedimento para a utilização da rotina no *link*:  
<http://tdn.totvs.com/pages/viewpage.action?pageId=439704784>
