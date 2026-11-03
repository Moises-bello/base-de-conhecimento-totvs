---
article_id: 39658520755735
category: Meu RH - Ponto
content_hash: b71bdfbaaf2a475a7a9d6708bed72d17c92a184fcc6a59c0669a918f44db5c70
fetched_at: '2026-06-28T22:47:30.218223+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Como bloquear o registro de ponto para funcionários de Férias
  ou Afastados no Meu RH?
type: support-article
updated_at: '2026-04-27T11:39:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39658520755735-RH-RM-Meu-RH-Como-bloquear-o-registro-de-ponto-para-funcion%C3%A1rios-de-F%C3%A9rias-ou-Afastados-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39658537290135) Tempo aproximado para leitura: **00:01:35min**  
  
**Dúvida**  
Como realizar o bloqueio de acesso ao espelho de ponto e impedir a marcação de batidas manuais e por geolocalização no Meu RH para colaboradores de férias ou afastados?

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**  
Para impedir que o colaborador visualize o espelho de ponto durante o período de férias ou afastamento, é necessário ajustar as permissões no Grupo de Acesso ao Quiosque.

Acesse o módulo de **Automação de Ponto >** **Configurações > Parametrizador > RM Portal >** edite o **Grupo de acesso ao quiosque** e desmarque a opção "**Permite acesso ao RM Portal para funcionários de férias / em afastamento"**;  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39658537290391)

Caso utilize batidas por **geolocalização**, este parâmetro acima não bloqueia as batidas remotas. Para impedir efetivamente o registro do ponto por geolocalização, deve-se realizar o **bloqueio do movimento** do espelho de ponto para os funcionários nestas situações. Acesse **Automação de Ponto** > **Movimento** > clique no item **Bloqueia.** Crie um filtro de seção para estes funcionários que deverão ser impedidos de registrar ponto e execute a rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39658537290519)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39658520740759)

Após desmarcar o parâmetro "**Permite acesso ao RM Portal para funcionários de férias...**" e executar o **Bloqueio do movimento**, o Meu RH irá impedir o registro de batidas de ponto destes funcionários.

**Saiba Mais**  
[RH - RM - PTO - Bloquear/Desbloquear alterações no movimento do espelho de ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008578091-RH-RM-PTO-Bloquear-Desbloquear-altera%C3%A7%C3%B5es-no-movimento-do-espelho-de-ponto)
