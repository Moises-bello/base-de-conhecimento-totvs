---
article_id: 360047669333
category: ADVPL - Rotina Automática
content_hash: 89aceaa741385f6e62c29380456a0934f47aa0fd40e7ce407e53112c02f24194
fetched_at: '2026-06-28T22:40:23.937150+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Como considerar o profile
  de usuário no ExecAuto() MATA185.
type: support-article
updated_at: '2021-12-29T13:51:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047669333-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Como-considerar-o-profile-de-usu%C3%A1rio-no-ExecAuto-MATA185
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como considerar o profile de usuário no ExecAuto() MATA185?

**Ambiente**  
Protheus – ADVPL – A partir da versão P12  
  
**Solução**

Para que o **Execauto()** trate corretamente os parâmetros **F12**, o fonte chamador deve ser executado por um menu dentro do modulo ou se de forma ***batch***, deve ter os comandos de inicialização de ambiente **RPCSETENV** com a empresa, filial, **usuário, senha e modulo**, simulando como se fosse um menu.

Deve ser observado também que os parâmetros estarão com o conteúdo default ou o ultimo conteúdo utilizado pelo usuário configurado quando acessou a rotina diretamente.

**Exemplo;**  
**RpcSetEnv( "99","01", "Administrador", " ", "EST", "MATA185",)**

**Saiba Mais;**  
**[PEST06010 - MATA185 - Rotina Automática da Baixa de Pré-Requisições](https://tdn.totvs.com/pages/releaseview.action?pageId=237386050)**
