---
article_id: 360052543934
category: LOGIN
content_hash: 7a703ecd55365b16c5265d13f52524e0b4eacd7ed02a6527dd34aab2f9c830d0
fetched_at: '2026-06-28T22:44:40.614053+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como configurar o Esqueceu a Senha do MEU RH
type: support-article
updated_at: '2026-06-18T19:30:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052543934-RH-Linha-Protheus-MEU-RH-Como-configurar-o-Esqueceu-a-Senha-do-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17989838552855) Tempo aproximado para leitura: 00:05:00 min****Dúvida**Como configurar o Esqueceu a Senha do MEU RH  
  
**Ambiente**TOTVS RH (Linha Protheus) - MEU RH - Todas as versões  
  
**Solução**Para utilizar o Esqueceu a Senha do MEU RH, seguir as orientações e premissas informadas na **[Documentação de Referência do MEU RH: 1.4 Esqueceu a senha?](https://tdn.totvs.com/pages/releaseview.action?pageId=519727565)**  
  
Abaixo, é trazido um passo a passo com *prints* dessa configuração levando em consideração o provedor de *E-mail GMAIL*. Porém, neste caso é necessário consultar internamente em sua Empresa, as informações do seu provedor de *E-mail* e ajustar essa configuração.  
  
**1ª Passo:** Através do Configurador (SIGACFG) acessar as opções **"Ambiente > E-mail/Proxy > Configurar"** e cadastrar o *e-mail* com as informações do provedor de *e-mail*, conforme documentação abaixo:  
  
**Boletim Técnico: [Configurar o SMTP para envio de relatórios por e-mail](https://tdn.totvs.com/pages/releaseview.action?pageId=271166884)**  
Exemplo de configuração para do provedor de *e-mail OUTLOOK*:  
​![](https://centraldeatendimento.totvs.com/hc/article_attachments/17987808160535)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17987809344407)​  
  
​![](https://centraldeatendimento.totvs.com/hc/article_attachments/17987861254935)  
  
​![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008613441)  
  
**IMPORTANTE:**   
Após a configuração, o Sistema grava a chave [MAIL] no **APPSERVER.INI** do serviço do Protheus que foi utilizado, para acessar o Configurador **(SIGACFG)**, ou seja, em muitos casos é necessário copiar a chave **[MAIL]** e informá-la da mesma forma no **APPSERVER.INI** do serviço do MEU RH.   
  
Para clientes no ***CLOUD*** da TOTVS, entrar em contato com o atendimento do ***CLOUD*** e solicite a replicação dessa informação para o serviço do MEU RH.  
  
**[MAIL]**  
**Protocol=SMTP**   
**ExtendSMTP=1**  
**TLSVersion=3**  
**SSLVersion=2**   
**TRYPROTOCOLS=0**  
**authLogin=1**   
**authPlain=0**  
**authNTLM=0**  
**VERBOSE=1​**  
  
**2ª Passo:** Configurar os parâmetros abaixo com as informações do provedor de *e-mail*, conforme exemplo abaixo:

1. **MV\_RELACNT: email do disparo;**  
   **Exemplo: [seuemail@????.com](mailto:seuemail@gmail.com,)[,](mailto:seuemail@gmail.com,) o mesmo utilizado nas configurações acima.**
2. **MV\_RELPSW : senha da conta do email;**  
   **Exemplo: Senha que utiliza para acessar o E-mail  no site do provedor.**
3. **MV\_RELSERV: servidor do SMTP e porta;  
   Exemplo: smtp.office365.com:587**
4. **MV\_RELAUTH: se o servidor necessita autenticação para o disparo do E-mail;**  
   **Exemplo: .F.**
5. **MV\_RELTLS: se o servidor possui/exige conexão segura SSL/TLS.**  
   **Exemplo: .T.**
6. **MV\_RELSSL: Define se o envio e recebimento de e-mails na rotina SPED utilizará conexão segura (SSL).**  
   **Exemplo: .F.**
7. **MV\_RELFROM: E-mail utilizado no campo FROM no envio de relatórios por e-mail**  
   **Exemplo: Totvs<testeworkflowprotheus@outlook.com.br>**   
     
   [**Documentação referencia ligada aos parâmetros acima**](https://tdn.totvs.com/pages/releaseview.action?pageId=519727565)

**3ª Passo:** Acessar o MEU RH e clicar sobre o **"Esqueceu a Senha"**, será solicitado o Usuário, que no padrão é o CPF, e o *e-mail* que deve ser o mesmo cadastrado no Funcionário (SRA) e no Participante (RD0).  
​![chrome_mhF6LXFs47.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/18057450631447)  
  
A imagem acima refere-se a confirmação do envio de *e-mail,* e será apresentada se a configuração indicada nos passos anteriores foi respeitada, porém, caso ainda não receba o *e-mail* na Caixa de Entrada, deverá ser revisada as configurações do provedor de *e-mail* nos passos indicados acima.  
  
**4ª Passo:** Caso esteja tudo certo na configuração do Remetente do *e-mail,* o usuário irá receber o *e-mail* abaixo com as instruções para reiniciar a senha.  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008413122)  
  
**IMPORTANTE**:  
Se houver erros no disparo do e-mail, neste processo do Esqueceu a Senha pelo Meu RH, e para trazer, ao Suporte uma evidência, com um nível de detalhamento nos *logs* gerados no **MEU RH** é necessário adicionar uma chave na sessão [*MAIL]* chamada *VERBOSE=1* no arquivo de configuração ***appserver.ini do MEU RH*****:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19448294646551)  
  
Segue abaixo, um pouco mais sobre este chave a ser inserida:  
**[Como evidenciar nos logs elementos de disparo de e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19429764987159)**  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)  
[**CLIQUE AQUI** para acessar Envio do "esqueceu a senha" quando se utiliza SSL/certificado digital](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052412773)  
[**CLIQUE AQUI** para acessar Para qual e-mail é enviado a redefinição de senha ao selecionar a opção "Esqueceu a senha" no MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007991422)
