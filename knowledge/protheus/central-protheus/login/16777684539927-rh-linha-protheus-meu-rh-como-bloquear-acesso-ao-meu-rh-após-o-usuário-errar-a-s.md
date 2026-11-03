---
article_id: 16777684539927
category: LOGIN
content_hash: 51715a0c502cec39e42b03bb11227d97f11df345f4b51b21d3617f4b2ac71f77
fetched_at: '2026-06-28T22:44:40.499923+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como bloquear acesso ao Meu RH após o usuário
  errar a senha
type: support-article
updated_at: '2026-06-18T18:08:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16777684539927-RH-Linha-Protheus-MEU-RH-Como-bloquear-acesso-ao-Meu-RH-ap%C3%B3s-o-usu%C3%A1rio-errar-a-senha
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16777697383063) Tempo aproximado para leitura: **03:00 min** **Dúvida**Como bloquear o acesso ao Meu RH, após o usuário errar a senha inicial?  
  
**Ambiente**TOTVS RH -  (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**O parâmetro **MV\_MRHULI** estabelece **o número de tentativas incorretas** que o usuário poderá tentar, até ter o seu acesso bloqueado ao Meu RH.  
  
**MV\_MRHULI**   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16777168192919)  
  
Neste exemplo, **na terceira tentativa de login**, o usuário será bloqueado, tendo a seguinte mensagem:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16777179593495)  
  
O Meu RH **não avisará a quantidade de tentativas** que o usuário possui **ou então as que ainda são restantes para que o acesso seja bloqueado**.  
  
Cabe ressaltar que o campo **RD0\_ULI será utilizado nesse caso**, como um contador de vezes que o usuário realizou a tentativa de forma incorreta.  
  
Para **desbloquear** o usuário, será necessário acessar a **rotina de Manutenção de Usuários - TCFA130**, no **módulo 18 - SIGATCF** do **Protheus** e, em **Outras Ações -> Gerenciar Usuários**, realizar o processo de **Iniciar Usuário** e **Gerar Senhas** para que **o *login* tenha a senha padrão novamente.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16777381083927)  
  
Efetuar o processo **primeiramente com a opção Iniciar Usuário** e, **posteriormente, Gerar Senhas**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16777391250967)  
  
Com isso, o usuário com a senha padrão, conseguirá novamente, realizar o *login* no Meu RH.  
  
Primeiro acesso (senha padrão):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16777476208919)  
  
Após alteração da senha, como num primeiro *login*, o acesso é liberado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16777515862295)  
 **Saiba Mais**[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
