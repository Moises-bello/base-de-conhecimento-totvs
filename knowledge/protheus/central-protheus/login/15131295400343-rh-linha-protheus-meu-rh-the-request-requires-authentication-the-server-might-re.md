---
article_id: 15131295400343
category: LOGIN
content_hash: 99a8b439a023bf874ad80f861814a6ff1f4586b1a4bde12df8400fe28da3a06e
fetched_at: '2026-06-28T22:44:40.506772+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - The request requires authentication. The server
  might return this response for a page behind a login
type: support-article
updated_at: '2026-06-18T18:34:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131295400343-RH-Linha-Protheus-MEU-RH-The-request-requires-authentication-The-server-might-return-this-response-for-a-page-behind-a-login
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19463113979799) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Na página inicial do Meu RH é apresentada mensagem "***The request requires authentication. The server might return this response for a page behind a login***."  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**A mensagem "***The request requires authentication. The server might return this response for a page behind a login.***" pode ser apresentada na página inicial do Meu RH, ao realizar o acesso **via *web*** em **duas** situações:  
  
**1.** Ao não possuir usuário genérico associado ao **usuário do Configurador** que possua acesso **à todas as empresas/filiais**.   
Neste cenário, para correção, será necessário seguir os passos abaixo para **garantir** que o funcionário que realizou o *login*, esteja associado a um Usuário Genérico que utilize um **Usuário do Configurador com os devidos direitos**:   
-> [RH - Linha Protheus - MEU RH - Como cadastrar um Usuário do Protheus via Configurador para acesso ao MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729194)  
-> [RH - Linha Protheus - MEU RH - Como associar o Usuário do Protheus ao Usuário do Portal para acesso ao MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043730394)-> [RH - Linha Protheus - MEU RH - Como associar o Usuário do Portal ao Cadastro de Participante para acesso ao MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043731394)  
  
**2.** Certifique-se de que o usuário **Mestre** no **Configurador** não está **bloqueado**.   
  
Para isso acesse o **SIGACFG** em **Usuário** -> **Senhas** -> **Usuários**, selecione o usuário e clique em **Alterar**.  
Caso o usuário esteja bloqueado realize a alteração e clique em Salvar.  
![chrome_89slKJfMkH.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19463149751831)  
  
**3.** Ao possuir os **Arquivos do Portal** com **versão** de **30/05/2023 ou superior**.  
Neste cenário, devido a melhoria disponibilizada abaixo, a **configuração** no **serviço *REST* deverá ser alterada** como demonstrado em seguida:  
<https://tdn.totvs.com/pages/viewpage.action?pageId=757238802>   
  
\*Na seção do serviço ***REST***, na chave ***Public*** precisará **acrescentar** o serviço ***setting/companySettings*** como demonstrado abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/15131009599511)  
Public=fwjwt/refresh\_token,auth,setting/companySettings  
  
Obs.: Caso seu ambiente se encontre em nossa **infraestrutura *Cloud***, necessário **abrir um chamado** para a **equipe *Cloud,*** informando a necessidade de realização deste procedimento acima, no serviço responsável por manter a execução do App Meu RH.  
 **Saiba Mais****[RH - Linha Protheus - MEU RH - Aprenda sobre o MEU RH e como fazer a implantação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036164214)  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referência sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
