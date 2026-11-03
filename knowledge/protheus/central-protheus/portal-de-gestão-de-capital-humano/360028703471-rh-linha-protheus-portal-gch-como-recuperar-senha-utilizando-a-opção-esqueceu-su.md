---
article_id: 360028703471
category: Portal de Gestão de Capital Humano
content_hash: a5449b153a72b36de1bfac3b8a7600b0c4324de859c4d3f74f002c50586a2a27
fetched_at: '2026-06-28T22:43:00.158644+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH- Como recuperar senha utilizando a opção "Esqueceu
  sua senha" no Portal GCH
type: support-article
updated_at: '2021-09-29T13:10:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028703471-RH-Linha-Protheus-PORTAL-GCH-Como-recuperar-senha-utilizando-a-op%C3%A7%C3%A3o-Esqueceu-sua-senha-no-Portal-GCH
---

**Dúvida**Como recuperar senha utilizando a opção "Esqueceu sua senha" no Portal GCH?   
  
**Ambiente**TOTVS RH (Linha Protheus) -  Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**No **módulo SIGAGPE**, no menu: *Atualizações > Funcionários > Funcionários,*deve ser preenchido o campo **E-mail Principal** (RA\_EMAIL).  
  
No **módulo SIGAAPD**, no menu: *Atualizações > Participantes > Cadastro,* deve ser preenchido o campo **E-mail** (RD0\_EMAIL).  
  
**Observação:** É possível enviar o e-mail com ou sem autenticação. Verifique as configurações:  
  
Configuração para envio de e-mail **SEM**autenticação**:**Entre no **módulo Configurador,** acesse o menu *Ambiente > Cadastros > Parâmetros.***Observação:** Deverá entrar em cada um dos parâmetros abaixo para devida configuração.  
  
- **MV\_RHAUTEN** = .F. (Parâmetro para informar se é necessário autenticar no servidor SMTP).  
- **MV\_RELSERV**   = Servidor de envio de Email (Ex: [mail.totvs.com.br](http://mail.totvs.com.br/)).  
- **MV\_PORSMTP** = (Porta do Servidor SMTP).  
- **MV\_RHCONTA** = Conta para o envio do e-mail (Ex: [mail@dominio.com.br](mailto:mail@dominio.com.br)).  
- **MV\_RHSENHA** = Senha da conta informada no parâmetro MV\_RHCONTA.  
- **MV\_RELFROM** = Remetente (Opcional), caso preenchido deve conter o (@dominio.com.br).  
  
Configuração para envio de e-mail **COM**autenticação**:**- **MV\_RHAUTEN** = .T. (Parâmetro para informar se é necessário autenticar no servidor SMTP).  
- **MV\_RELSERV** e **MV\_RHSERV** = Servidor de envio de Email (Ex: [mail.totvs.com.br](http://mail.totvs.com.br/)) - Os dois parâmetros devem estar preenchidos iguais com o SMTP da empresa.  
- **MV\_PORSMTP**= (Porta do Servidor SMTP).  
- **MV\_RELAUSR**  = Usuário para autenticar no servidor SMTP (usuário de rede).  
- **MV\_RELAPSW** = Senha do usuário de rede.  
- **MV\_RELFROM** = Remetente (Opcional), caso preenchido deve conter o (@dominio.com.br).  
- **MV\_RELSSL** = .T. ou .F. (Informa se o protocolo SSL é utilizado na comunicação com o servidor SMTP).  
- **MV\_RELTLS** = .T. ou .F. (Informa se o protocolo TLS é utilizado na comunicação com o servidor SMTP).  
  
**Observação:** Se os parâmetros **MV\_RELSSL** ou **MV\_RELTLS** estiverem com (.T.), o parâmetro de autenticação (**MV\_RHAUTEN**) obrigatoriamente deve ser (.T.).  
  
Os parâmetros abaixo também devem ser configurados em ambas configurações (com ou sem autenticação):  
- **MV\_EMCONTA** = (Indica qual conta será utilizada para envio de e-mails).  
- **MV\_EMSENHA** = (Indica qual a senha da conta utilizada para envio de e-mails).  
- **MV\_RHSERV**  = Servidor de e-mail para envio de mensagens. Ex.: (@dominio.com.br).  
- **MV\_RELSERV =**Nome do Servidor de envio de e-mail utilizado nos relatórios.  
  
**Observação:** O conteúdo do parâmetro **MV\_RHSERV** deve ser configurado somente com o servidor, não deve ser incluído informação de porta em seu conteúdo.  
  
Após realizar a configuração acima, entre no Portal Capital Humano e clique em "**Esqueceu sua**Senha?".  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065480614/mceclip0.png)  
  
Será aberto a tela abaixo para preencher os dados do funcionário:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065480754/mceclip1.png)  
  
Será enviado um e-mail para o funcionário com a senha de acesso:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029135731/mceclip4.png)  
  
E-mail com a senha:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029134872/mceclip5.png)  
  
Após receber a senha, poderá efetuar o acesso ao Portal GCH.  
  
Para redefinir a senha, verifique o artigo: [MP - PORTAL GCH - Como redefinir senha do participante para acesso ao Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028704251)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
