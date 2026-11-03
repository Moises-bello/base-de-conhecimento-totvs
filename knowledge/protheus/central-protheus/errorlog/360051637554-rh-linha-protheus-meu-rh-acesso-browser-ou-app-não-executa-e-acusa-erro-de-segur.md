---
article_id: 360051637554
category: ERRORLOG
content_hash: 56538373e2ea0eafce0603c34174bc277ae41c9d50cea3a1f6c812df1227beb7
fetched_at: '2026-06-28T22:44:39.502311+00:00'
product: protheus
section_id: 10299583475863
source: central-protheus
title: RH - Linha Protheus - MEU RH - Acesso browser ou App não executa e acusa erro
  de segurança - [ERROR][SSL] SSL Accept method error
type: support-article
updated_at: '2026-06-18T18:33:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051637554-RH-Linha-Protheus-MEU-RH-Acesso-browser-ou-App-n%C3%A3o-executa-e-acusa-erro-de-seguran%C3%A7a-ERROR-SSL-SSL-Accept-method-error
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28390477859863) Tempo aproximado para leitura: 00:01:00 min****Ocorrência**Ao utilizar SSL e tentar acessar o MEU RH, via APP ou BROWSER, a página não é executada. Ou é acusado o erro no console do appserver: [ERROR][SSL] SSL Accept method error.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Causa**Este problema ocorre por causa da configuração das *tags* de *SSL* incorretas dentro do appserver.ini.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o appserver.ini;  
2. Identifique as chaves abaixo, dentro das sessões [HTTPREST] e [SSLCONFIGURE];  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19282678298391)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19282678300567)  
3. Altere os conteúdos das chaves, conforme indicamos mais acima.  
  
Após esta alteração, reinicie os serviço do REST e execute novamente o acesso para corrigir o problema indicado.  
  
**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
[**MP - MEU RH - Como Atualizar os arquivos do Portal Meu RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)  
**[MP - GPE - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)****Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
