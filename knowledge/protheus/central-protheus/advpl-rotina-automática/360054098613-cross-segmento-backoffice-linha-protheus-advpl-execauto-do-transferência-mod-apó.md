---
article_id: 360054098613
category: ADVPL - Rotina Automática
content_hash: 6760c21fb1ef5a6fcefbf5d45a77cb3ea87e267c44acfb8035d116a0fc5ce086
fetched_at: '2026-06-28T22:40:24.004397+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - ExecAuto do Transferência
  Mod ||:Após a execução não posiciona no registro
type: support-article
updated_at: '2021-12-29T14:08:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054098613-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-ExecAuto-do-Transfer%C3%AAncia-Mod-Ap%C3%B3s-a-execu%C3%A7%C3%A3o-n%C3%A3o-posiciona-no-registro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Porque o ExecAuto(0 do Transferência Mod || não posiciona no registro gerado?

**Ambiente**Protheus – ADVPL – A partir da versão P12

**Solução**Diferentemente do uso em tela, onde a *Browse* na maioria dos casos posiciona no ultimo registro incluído, no **Execauto** a *Browse* não tem atuação e o posicionamento de registros pode ser qualquer um, dependendo do fluxo de rotinas envolvidas no processo.  
O **Execauto** é indicado para desenvolvedores que querem automatizar um processo como se fosse feito pela tela seguindo os conceitos e regras padrão, mas as boas praticas de desenvolvimento ainda devem ser seguidas, como posicionar corretamente o dado que vai usar ou atualizar.
