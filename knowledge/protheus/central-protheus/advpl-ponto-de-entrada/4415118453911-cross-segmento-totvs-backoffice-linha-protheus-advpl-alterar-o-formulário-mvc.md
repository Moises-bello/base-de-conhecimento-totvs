---
article_id: 4415118453911
category: ADVPL - Ponto de Entrada
content_hash: 550e59c8e7d79275b98dacc2bb6125729f36da572ebc6d736eb53451179a1c87
fetched_at: '2026-06-28T22:40:12.952325+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Alterar o formulário
  MVC
type: support-article
updated_at: '2021-12-06T14:25:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415118453911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Alterar-o-formul%C3%A1rio-MVC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como alterar o formulário MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**A alteração pode ser através do ponto de entrada em MVC, onde você usará o método **FWModelActive**() para pegar o modelo ativo e alterá-lo usando o **oModel:setValue**().  
Em alguns caso, tal alteração pode não ter o comportamento esperado, quando um model sofre uma alteração diretamente a *view* não recebe esse aviso de modificação.  
No caso, a rotina que atualiza o estado de modificação se dá pelo grid existente onde ao realizar um *refresh* na *view* uma modificação na *view* é forçada pelo *goLine* realizado e com isso o estado de modificação da *view* sofre a alteração.  
Para disponibilizarmos um método ou algo do tipo que possa possibilitar uma atualização da *view* ao realizar a alteração diretamente no módulo realize a abertura de uma sugestão de melhoria através da [Central Colaborativa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039467434-Central-Colaborativa-Como-Acessar?source=search).  
  
**Saiba mais**  
[FWModelActive](https://tdn.totvs.com/display/framework/FWModelActive)  
[FWFormModel](https://tdn.totvs.com/display/public/PROT/FWFormModel)  
[Ponto de Entrada Padrão do MVC](https://tdn.totvs.com/pages/releaseview.action?pageId=208345968)
