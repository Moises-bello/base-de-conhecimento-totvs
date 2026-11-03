---
article_id: 360026509054
category: Portal do Candidato
content_hash: 7635d2c1375f7fdaf11747a6cbb7de8f9ad8e14f93e34f96513b84b7d05c1944
fetched_at: '2026-06-28T22:42:57.789578+00:00'
product: protheus
section_id: 360005048093
source: central-protheus
title: RH - Linha Protheus - PORTAL CANDIDATO - Como configurar e-mail do "Fale Conosco"
  no Portal do Candidato
type: support-article
updated_at: '2023-10-03T20:39:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026509054-RH-Linha-Protheus-PORTAL-CANDIDATO-Como-configurar-e-mail-do-Fale-Conosco-no-Portal-do-Candidato
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18002567235607) Tempo aproximado para leitura: 00:07:00 min****Dúvida**Como configurar e-mail do "Fale Conosco" no Portal do Candidato?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) – Portal Candidato – Todas as versões  
  
**Solução**É possível definir uma conta de *e-mail* para recebimento das mensagens enviadas pelo Fale Conosco do Portal do Candidato através do parâmetro **MV\_RHFALE.**Abaixo trazemos um passo a passo com prints dessa configuração levando em consideração o provedor de *E-mail Office365*. Porém, neste caso você deve consultar internamente em sua Empresa as informações do seu provedor de E-mail e ajustar essa configuração.  
  
**1° Passo:** No módulo Configurador, acesse o menu **Ambientes > Cadastros > Parâmetros** e filtre os parâmetros abaixopara configuração:

* MV\_RHCONTA: conta de e-mail para envio das mensagens.  
  Exemplo: **[emailresponsavel@outlook.com](mailto:emailresponsavel@outlook.com)**
* MV\_RHSENHA: senha da conta do e-mail;  
  Exemplo: **Senha que utiliza para acessar o E-mail no site do provedor.**
* MV\_RHSERV : Servidor de e-mail para envio de mensagens. SMTP.  
  Exemplo: **smtp.office365.com:587**
* MV\_RHAUTEN: Determina se o servidor de e-mail requer autenticação.  
  Exemplo: **.T.**

**2° Passo:** Através do Configurador (SIGACFG) acesse as opções **"Ambiente > Workflow > Contras de *E-mail*"** e cadastre seu *e-mail* com as informações do seu provedor de *e-mail*, conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097342693)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097342773)  
  
**3° Passo:** Ainda no módulo Configurador (SIGACFG) acesse as opções "**Ambiente > E-mail/Proxy > Configurar**" e cadastre seu *e-mail* com as informações do seu provedor de *e-mail*, conforme documentação abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097342833)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18002291924759)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18002314710551)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18002312045975)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18002347775895)  
  
**4° Passo:** Acesse o Portal do Candidato, **clique no Menu "Fale Conosco"** e preencha as informações (lembrando que o *e-mail* será enviado para o que foi definido no parâmetro **MV\_RHFALE**).  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095043694)  
  
Será apresentado a mensagem que o *e-mail* foi enviado com sucesso!  
  
**IMPORTANTE:** A imagem abaixo será apresentada se a configuração indicada acima foi respeitada, porém, caso ainda não receba o *e-mail* em sua Caixa de Entrada, deverá revisar as configurações do seu provedor de *e-mail* nos passos indicados acima.  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095043714)  
  
**5° Passo:** Caso esteja tudo correto na configuração do Remetente do *e-mail*, receberá o *e-mail*:  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097343773)  
  
Observação: No caso específico do *Office365* é necessário configurar as permissões no *e-mail*.   
Efetuar as devidas configurações de acordo com o provedor de *e-mail* utilizado.  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360095044434)  
 **Saiba Mais**  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal Candidato](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048093-RH-Portal-do-Candidato)
