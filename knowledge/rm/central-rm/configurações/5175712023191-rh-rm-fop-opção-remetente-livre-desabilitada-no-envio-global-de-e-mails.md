---
article_id: 5175712023191
category: Configurações
content_hash: 2f3e2292b8d8f2854348b92984dcf50b64de05a1e705e94848485901652d5838
fetched_at: '2026-06-28T22:46:49.529419+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Opção Remetente Livre desabilitada no envio global de e-mails
type: support-article
updated_at: '2022-04-01T19:33:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5175712023191-RH-RM-FOP-Op%C3%A7%C3%A3o-Remetente-Livre-desabilitada-no-envio-global-de-e-mails
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**No módulo Folha de pagamento, ao tentar realizar o envio de e-mails ao funcionário através da rotina **Envio global de e-mail** na aba **Configurações**, o campo Remetente Livre fica desabilitado:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5175291254295/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as Versões  
  
**Causa**O bloqueio do campo ocorre devido ao parâmetro **Utilizar usuário de e-mail como remetente** estar habilitado em Parâmetros globais, na aba **Ambiente**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5175480465047/mceclip1.png)  
  
**Solução**  
Para habilitar o campo **Remetente Livre** para utilização será necessário:  
1. Acessar a aba **Ambiente | Parâmetros | Parâmetros globais**;   
2. Acessar a aba **Envio de e-mails**;  
3. Desabilitar o parâmetro **Utilizar usuário de e-mail como remetente**.
