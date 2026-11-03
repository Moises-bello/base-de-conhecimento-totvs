---
article_id: 360037382194
category: IMPLANTAÇÃO
content_hash: fb68434e80706ad8c342d623656953b787a97c48d6a8c9e4c2908fed1630061b
fetched_at: '2026-06-28T22:44:33.451102+00:00'
product: protheus
section_id: 10299929290007
source: central-protheus
title: RH - Linha Protheus - MEU RH - Erro FRHMENU por configuração incorreta no appserver.ini
type: support-article
updated_at: '2026-06-22T19:46:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037382194-RH-Linha-Protheus-MEU-RH-Erro-FRHMENU-por-configura%C3%A7%C3%A3o-incorreta-no-appserver-ini
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19450025982359)Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Quando a chave [HTTPENV] dentro do appserver.ini, no itens *PREPAREIN* estiver escrito de maneira incorreta, como por exemplo PREPARELN, ao acessa o MeuRH o sistema gera o erro abaixo:

*Alias dows not exist: SX3*  
*Pilha de erro: [*  
*THREAD ERROR ([13648], HTTP\_WT\_TESTE\_HTTPREST\_HTTPENV@, THIS) 27/09/2019 18:4256*  
*Alias does not exist: SX3 on FRHMENU(WSPORTAL01.PRX) 03/07/2019 17:12:28 line : 2570*  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049003994)  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Para solucionar o erro deverá corrigir a *TAG* dentro do appserver.ini, deixando conforme abaixo:  
  
[HTTPENV]  
URL=/restT1  
**PrepareIn**=T1   
Instances=2,5,1,1  
ENVIRONMENT= NOME DO SEU AMBIENTE  
CORSEnable=1  
AllowOrigin=\*  
Public=fwjwt/refresh\_token,auth,setting/companySettings  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
