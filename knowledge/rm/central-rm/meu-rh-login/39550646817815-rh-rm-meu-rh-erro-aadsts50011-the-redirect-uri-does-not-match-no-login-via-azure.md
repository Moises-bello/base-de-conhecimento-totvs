---
article_id: 39550646817815
category: Meu RH - Login
content_hash: 1b6647577f4ceaf3edc9aad2eef38aca15cf7c8dc6c2452839d1d4d03f8dda4f
fetched_at: '2026-06-28T22:47:27.181424+00:00'
product: rm
section_id: 37725850167319
source: central-rm
title: 'RH - RM - Meu RH - Erro "AADSTS50011: The redirect URI does not match" no
  login via Azure'
type: support-article
updated_at: '2026-04-09T13:28:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39550646817815-RH-RM-Meu-RH-Erro-AADSTS50011-The-redirect-URI-does-not-match-no-login-via-Azure
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39550685411351) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao realizar o login no Meu RH utilizando a integração com Azure, o código de erro apresentado é o AADSTS50011 (que indica uma divergência na URI de redirecionamento configurada).  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.33.158  
  
**Causa**  
O erro é referente à URL incorreta como descrito na própria mensagem, provavelmente está faltando ou passando uma / no fim do endereço ou alguma letra maiúscula/minúscula está diferente da URL informada no Azure pois o campo é case sensitive.  
  
**Solução**  
Na mensagem de erro, é apresentada exatamente a URL que deve ser informada no campo de **Autenticação | Adicionar URL de Redirecionamento | Aplicativo de Página Únic**a pois o campo é case sensitive, ou seja, sistema faz a **diferenciação rigorosa entre letras maiúsculas e minúsculas.**

Isso significa que o sistema entende a letra "A" como um caractere completamente diferente da letra "a".

No exemplo abaixo, a URL foi informada como http://localhost/FrameHTML/**web**/App/RH/PortalMeuRH e no erro foi informado que a URL esperada era http://localhost/FrameHTML/**Web**/App/RH/PortalMeuRH em que estava diferente apenas o W maiúsculo entre uma URL e  outra.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39550685412119)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39550646798743)

Basta copiar exatamente a URL do erro *"AADSTS50011: The redirect URI '**http://localhost/FrameHTML/web/app/RH/PortalMeuRH**' specified in the request does not match the redirect URIs"*e informar no campo da plataforma do Azure em **Autenticação | Adicionar URL de Redirecionamento | Aplicativo de Página Única** e tentar novamente conforme o exemplo a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39550685413655)![](https://centraldeatendimento.totvs.com/hc/article_attachments/39550685416471)
