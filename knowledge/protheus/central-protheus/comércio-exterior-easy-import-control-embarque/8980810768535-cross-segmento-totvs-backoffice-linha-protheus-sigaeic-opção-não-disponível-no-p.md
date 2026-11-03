---
article_id: 8980810768535
category: Comércio Exterior - Easy Import Control - Embarque
content_hash: 3634097d366ada5f186dd11bfbacb6ae343b55662599b45480a49d069208de45
fetched_at: '2026-06-28T22:39:48.747502+00:00'
product: protheus
section_id: 1500001538381
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Opção Não Disponível
  no Protheus Função AP110CBOX
type: support-article
updated_at: '2022-09-19T18:15:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8980810768535-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Op%C3%A7%C3%A3o-N%C3%A3o-Dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-AP110CBOX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao tentar acessar a rotina de controle de cambio (**EICAP100**) apresenta a mensagem

**"HELP: Problema: Opção não disponível no Protheus Função:AP110CBOX Called By X3CBOX".**

"?![AP100CBOX.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8980409073943/AP100CBOX.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*– Todas versões  
  
**Solução**A mensagem na rotina controle de câmbio (**EICAP100**) esta sendo exibida pois no ambiente o dicionário  
 esta atualizado porém a rotina  esta desatualizado .

Para que a mensagem não seja mais exibida será necesário que aplique o patch da expedição contínua do  Comex pois seomente o patch pontual do fonte, pode não resolver 100%.

[Pacotes de Atualizações - Comércio Exterior - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=526987588)
