---
article_id: 1500004351361
category: Configurações
content_hash: 9c120ee92accb60036e80e5cd076c2a2906acc5bfe9aa5636017fc78233915fc
fetched_at: '2026-06-28T22:46:49.578372+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: 'RH - RM - FOP - Erro: AfDataFinalAtestado30Dias ou DataIncidenciaAviso da
  classe FopParams e String was not recognized as a valid DateTime'
type: support-article
updated_at: '2025-03-05T18:30:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004351361-RH-RM-FOP-Erro-AfDataFinalAtestado30Dias-ou-DataIncidenciaAviso-da-classe-FopParams-e-String-was-not-recognized-as-a-valid-DateTime
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:04:00 min  
  
Ocorrência**Ao acessar o RM é retornado o erro "A propriedade AfDataFinalAtestado30Dias da classe FopParams não pode ser carregada na base de dados" ou "A propriedade DataIncidenciaAviso da classe FopParams não pode ser carregada na base de dados" ou "String was not recognized as a valid DateTime", que impede o usuário de acessar o sistema ou processar algumas rotinas.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro referente a AfDataFinalAtestado30Dias ocorre devido ao formato incorreto na data informada em Configurações | Parametrizador | Folha Normal | Afastamento 1/2, no campo do **período referente a MP 664**.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005470322/mceclip0.png)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500005569861/mceclip1.png)**

O erro referente a DataIncidenciaAviso ocorre devido ao formato incorreto na data informada em Configurações | Parametrizador | Rescisão | Aviso Prévio, onde a data informada no campo **Verificar incidência CC 62 e CC 99 a partir de:** está em um formato/valor incorreto.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402376903575/mceclip0.png)**

**Solução**Para solucionar a demanda, existem duas possibilidades. A primeira está em alterar a data cadastrada nos dois seguintes campos do parametrizador: Configurações | Parametrizador | Folha Normal | Afastamento 1/2 para um dia a menos, apenas para que esta alteração force a atualização do banco de dados:

**![](https://totvssuporte.zendesk.com/attachments/token/Fg5xVFmq1QWvsV6OId8cpJkE5/?name=inline425115105.png)**

E fazer o mesmo processo em Configurações | Parametrizador | Rescisão | Aviso prévio se o erro exibido for DataIncidenciaAviso:

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402376955927/mceclip1.png)**

Feita a alteração e a conclusão da parametrização, ou seja, avançando-a até o final, basta entrar no parametrizador novamente e voltar à data que estava inserida novamente.  
  
Consulte abaixo o link da Central de Downloads. Orientamos aplicar a última versão disponibilizada caso seja necessário atualizar pois são cumulativas.

**[Central de Downloads e Atualizações](https://suporte.totvs.com/portal/p/10098/download#000023/12.1/all/search/12.1.31)**
