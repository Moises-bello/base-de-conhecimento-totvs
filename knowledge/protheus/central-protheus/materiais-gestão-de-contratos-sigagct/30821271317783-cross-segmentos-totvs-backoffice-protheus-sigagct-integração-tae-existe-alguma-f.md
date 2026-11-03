---
article_id: 30821271317783
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b26e5619c7ea1e796465881c658bbfa456086fc490be24581c7f456fa4eeba01
fetched_at: '2026-06-28T22:37:23.002830+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Integração TAE -  Existe
  alguma forma para se trocar o endereço de e-mail do workflow/e-mail da integração
  do Documento
type: support-article
updated_at: '2025-03-21T14:28:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30821271317783-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Integra%C3%A7%C3%A3o-TAE-Existe-alguma-forma-para-se-trocar-o-endere%C3%A7o-de-e-mail-do-workflow-e-mail-da-integra%C3%A7%C3%A3o-do-Documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30821299313815) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Na integração do SIGAGCT com o TAE-Totvs Assinatura Eletrônica, existe alguma forma para se trocar o e-mail apresentado no workflow/e-mail enviado da integração do Documento:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30821271289495)

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Atualmente, no que se refere à integração do SIGAGCT com o Totvs Sign, não possui uma funcionalidade ou configuração para se mudar as credenciais de autenticação principais, as quais foram definidas durante a implementação da funcionalidade, contidas na doc abaixo da integração, e que é a responsável pela inclusão/envio do doc integrado na plataforma do TAE-Totvs Assinatura Eletrônica:

[- Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a configuração Gestão de Contratos (SIGAGCT) x TOTVS Assinatura Eletrônica (TAE)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8349602927255-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-configura%C3%A7%C3%A3o-Gest%C3%A3o-de-Contratos-SIGAGCT-x-TOTVS-Assinatura-Eletr%C3%B4nica-TAE)

[- Gestão de Contratos (SIGAGCT) x TOTVS Assinatura Eletrônica (TAE)](https://tdn.totvs.com/x/K1cBMg)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30821299318935)

No caso, uma alternativa existente, conforme reporta a documentação acima, é realizar a troca da senha deste usuário de acesso **na Plataforma do Totvs Sign**, para que então sejam solicitadas novas credenciais na integração posterior a esta alteração de senha, e assim podendo se inserir um novo usuário e senha da plataforma para essas credencias, as quais ficaram para as integrações a partir daí.

Lembrando que este usuário das credencias de comunicação precisam ter os devidos acessos a inclusão de docto (Permissão para Publicação) no Totvs Sign, conforme informa a documentação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30821271296151)

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar a configuração Gestão de Contratos (SIGAGCT) x TOTVS Assinatura Eletrônica (TAE)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8349602927255-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-a-configura%C3%A7%C3%A3o-Gest%C3%A3o-de-Contratos-SIGAGCT-x-TOTVS-Assinatura-Eletr%C3%B4nica-TAE)

[Gestão de Contratos (SIGAGCT) x TOTVS Assinatura Eletrônica (TAE)](https://tdn.totvs.com/x/K1cBMg)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
