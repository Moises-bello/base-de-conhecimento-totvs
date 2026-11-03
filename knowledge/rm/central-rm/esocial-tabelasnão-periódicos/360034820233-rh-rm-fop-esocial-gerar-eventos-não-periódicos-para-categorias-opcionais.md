---
article_id: 360034820233
category: eSocial - Tabelas/Não Periódicos
content_hash: 75aba904ee1e76936363e3c773963c00ba51cc416faaf661212930b2cc0c2442
fetched_at: '2026-06-28T22:47:10.483368+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Gerar eventos não periódicos para categorias opcionais
type: support-article
updated_at: '2024-06-20T16:23:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034820233-RH-RM-FOP-eSocial-Gerar-eventos-n%C3%A3o-peri%C3%B3dicos-para-categorias-opcionais
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24315522483735)****Tempo aproximado para leitura:** **00:03:00 min  
  
Dúvida**É possível gerar eventos não periódicos para categorias eSocial opcionais?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**É possível sim gerar eventos não periódicos para autônomos de categorias opcionais. Para isso é necessário marcar o parâmetro **Gerar gatilho para trabalhador sem vínculo com categorias opcionais** presente no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 4/7.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10650603415959)**

Ao marcar esse parâmetro, serão gerados gatilhos a cada situação que dispare a necessidade de envio de um evento não periódico para os funcionários de categoria 701, 711, 712, 741 e 903. Quando o parâmetro estiver desmarcado, não serão gerados gatilhos para funcionários com as categorias mencionadas.  
  
**Importante**É importante lembrar que os eventos periódicos continuarão sendo gerados normalmente porém, **caso possua** o evento **S-2300** para esses funcionários na fila de eventos, o agrupamento de **informações complementares** no XML dos eventos periódicos, **não será gerado**. Caso **não tenha** enviado o **S-2300** para as categorias opcionais, **será incluso** um grupo de **informações complementares** no XML dos eventos periódicos.

O parâmetro foi migrado da etapa **Autônomos e Externos 1/2** para **Configurações Gerais 4/6** nos *patches* mais recentes dos releases de mercado.  
  
**Saiba Mais**Para maiores informações acesse:  
      • [Configurações Gerais 4/7](https://tdn.totvs.com/pages/releaseview.action?pageId=452719221)
