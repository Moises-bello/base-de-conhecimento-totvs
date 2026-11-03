---
article_id: 17793814555415
category: LOGIN
content_hash: ef0673dcae2a495a441f1425f985c6e61051fa91e5021f6818305e4c0aea4b8b
fetched_at: '2026-06-28T22:44:40.495474+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Object Object e Internal Server Error ao realizar
  o logout no MEU RH
type: support-article
updated_at: '2026-06-18T19:42:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17793814555415-RH-Linha-Protheus-MEU-RH-Object-Object-e-Internal-Server-Error-ao-realizar-o-logout-no-MEU-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17793821350039) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao realizar o ***logout*** dentro do Meu RH é apresentado o erro ***Object Object*** e ***Internal Server Error***e o ***logout*** não acontece.  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**Quando utilizado SSL no Meu RH é preciso que a *Tag* ***Security*** esteja com o conteúdo igual a 1 dentro da seção **[HTTPREST]**do contrário é apresentada a mensagem e o *Logout* não acontece.  
  
**Solução**Realize o ajuste dentro da seção **[HTTPREST]** na *tag* ***Security*** no serviço do Meu RH.  
  
**Obs.:**Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH. **[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)**  
**[RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)**Se com este procedimento não solucionar a demanda, importante coletar todos os arquivos ***console.log*** dos serviços ***Appserver, Master e Slaves***, juntamente com a URL do Meu RH, *login* e senha para testes e, com estas informações abrir um ticket ao Suporte para análise.  
  
Para esse envio ao Suporte, poderão utilizar a **Ferramenta Minha Senha TOTVS**.  
<https://minhasenha.totvs.com.br/home> **Saiba Mais:  
[RH - Linha Protheus - MEU RH - O que fazer quando não consigo acessar o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050238493)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
