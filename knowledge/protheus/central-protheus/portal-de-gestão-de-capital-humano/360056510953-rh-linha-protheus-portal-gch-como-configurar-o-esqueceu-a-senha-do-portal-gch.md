---
article_id: 360056510953
category: Portal de Gestão de Capital Humano
content_hash: ed28e7fc8ff6e885fd8634c3683f2edbc7735b899e553709c081558bab2594ac
fetched_at: '2026-06-28T22:42:59.036930+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus  - PORTAL GCH - Como configurar o Esqueceu a Senha do Portal
  GCH
type: support-article
updated_at: '2021-04-07T12:44:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056510953-RH-Linha-Protheus-PORTAL-GCH-Como-configurar-o-Esqueceu-a-Senha-do-Portal-GCH
---

**Dúvida**Como configurar o Esqueceu a Senha do Portal GCH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) -  Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Para utilizar o Esquece a Senha do Portal GCH você deve seguir as orientações e premissas informadas na [Configuração envio de e-mail esqueci minha senha Portal](https://tdn.totvs.com/display/public/PROT/3360662+DRHGCH-3951+DT+Erro+para+enviar+e-mail+esqueci+minha+senha+Portal)  
  
Abaixo trazemos um passo a passo com prints dessa configuração levando em consideração o provedor de E-mail Office365. Porém, neste caso você deve consultar internamente em sua Empresas as informações do seu provedor de E-mail e ajustar essa configuração.  
  
**1ª Passo:**Através do Configurador (SIGACFG) acesse as opções "Ambiente > Workflow > Contras de E-mail" e cadastre seu E-mails com as informações do seu provedor de E-mail, conforme exemplo abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/CxTcbYFdGwMbFiMego6vLGJcx/?name=inline1420706956.png)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092531034/mceclip0.png)  
  
**2ª Passo:**Através do Configurador (SIGACFG) acesse as opções "Ambiente > E-mail/Proxy > Configurar" e cadastre seu E-mail com as informações do seu provedor de E-mail, conforme documentação abaixo:  
  
**Boletim Técnico: [Configurar o SMTP para envio de relatórios por e-mail](https://tdn.totvs.com/pages/releaseview.action?pageId=271166884)**  
Exemplo de configuração para do provedor de e-mail Office365:  
  
![](https://totvssuporte.zendesk.com/attachments/token/wkWuVeCxZORfFkwKhnhMGLZjz/?name=inline-107445667.png)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094752833/mceclip1.png)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094752913/mceclip2.png)  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094752993/mceclip3.png)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094753033/mceclip4.png)  
  
**IMPORTANTE:** Após a configuração do **2º Passo** o Sistema grava a chave [MAIL] no APPSERVER.INI do serviço do Protheus que você utilizou para acessar o Configurador (SIGACFG). Para clientes no CLOUD da TOTVS, entrem em contato com o atendimento do CLOUD e solicite a replicação dessa informação para o serviço do Portal GCH.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092531534/mceclip5.png)  
  
**3ª Passo:**Configure os parâmetros abaixo com as informações do seu provedor de E-mail, conforme exemplo abaixo:

* MV\_EMCONTA: e-mail do disparo;  
  Exemplo: **[seuemail@outlook.com](mailto:seuemail@gmail.com,)**[,](mailto:seuemail@gmail.com,)o mesmo utilizado nas configurações acima.
* MV\_EMSENHA: senha da conta do e-mail;  
  Exemplo: **Senha que utiliza para acessar o E-mail no site do provedor.**
* MV\_RELSERV: servidor do SMTP.  
  Exemplo: **smtp.office365.com**
* MV\_PORSMTP: porta SMTP.  
  Exemplo: **587**
* MV\_RELAUTH: se o servidor necessita autenticação para o disparo do E-mail.  
  Exemplo: **.T.**MV\_RELTLS: se o servidor possui/exige conexão segura SSL/TLS.  
  Exemplo: **.T.**
* MV\_RHSERV: Servidor de e-mail.  
  Exemplo: **smtp.office365.com**
* MV\_RHAUTEN: Determina se o servidor de e-mail requer autenticação.  
  Exemplo: **.T.**
* MV\_RELAUSR: Usuário para autenticação no servidor de e-mail.  
  Exemplo: **[seuemail@outlook.com](mailto:seuemail@gmail.com,)**
* MV\_RELAPSW: Senha para autenticação no servidor de e-mail;  
  Exemplo: **Senha que utiliza para acessar o E-mail no site do provedor.**
* MV\_RELFROM: E-mail utilizado no campo FROM no envio de e-mail   
  Exemplo: Nome<**[seuemail@outlook.com](mailto:seuemail@gmail.com,)>**
* MV\_RELSSL: Define se o envio e recebimento de e-mails utilizará conexão segura.  
  Exemplo: **.F.**
* Se MV\_RELSSL ou MV\_RELTLS forem **.T.** o parâmetro de autenticação (**MV\_RHAUTEN**) obrigatoriamente deve ser **.T.** também

**4ª Passo:**Acesse o Portal GCH e clique sobre o "Esqueceu a Senha", será solicitado o Login, que no padrão é o CPF ou login cadastrado, e o E-mail que deve ser o mesmo cadastrado no Funcionário (SRA) e no Participante (RD0).  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094753933/mceclip6.png)  
  
**IMPORTANTE:** A imagem abaixo será apresentada se a configuração indicada acima foi respeitada, porém, caso ainda não receba o E-mail em sua Caixa de Entrada você deve revisar as configurações do seu provedor de E-mail nos passos indicados acima.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094754073/mceclip7.png)  
  
**5ª Passo:**Caso esteja tudo certo na sua configuração do Remetente do E-mail o usuário vai receber o E-mail informando qual a senha:  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094754153/mceclip8.png)  
  
Observação: No caso específico do Office365 é necessário configurar as permissões no e-mail. Efetue as devidas configurações de acordo com o provedor de e-mail utilizado.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092536374/mceclip9.png)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
