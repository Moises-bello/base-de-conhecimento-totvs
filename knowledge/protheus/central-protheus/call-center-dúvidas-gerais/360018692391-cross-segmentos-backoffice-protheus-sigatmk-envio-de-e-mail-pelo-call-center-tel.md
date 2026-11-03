---
article_id: 360018692391
category: Call Center - Dúvidas Gerais
content_hash: c6a8eafc1644decaacc8f1a4ab37b11f1e02fa81a1e8713bf61001a944b3e15d
fetched_at: '2026-06-28T22:41:26.666568+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Envio de E-mail pelo Call
  Center (Telemarketing/Telecobrança)
type: support-article
updated_at: '2024-11-13T13:07:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018692391-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Envio-de-E-mail-pelo-Call-Center-Telemarketing-Telecobran%C3%A7a
---

**Ocorrência**

Quais as configurações para envio de e-mail para o responsável da ação no Call - Center nas modalidades de telemarketing e telecobrança?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**Configuração para envio de e-mail Protheus**

1 - Cadastre um usuário no configurador (CFGA510). Seguindo o menu "Usuários>Senhas>Usuários".   
Ainda no cadastro do usuário preencha o campo "E-mail"(USR\_EMAIL) com o e-mail do usuário.   
Ex: [user@empresa.com.br](mailto:user@empresa.com.br)  
  
2 - Realize a configuração de envio de e-mail do Protheus conforme a documentação [Configurar o SMTP para envio de relatórios por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071-MP-FRAME-Configurar-o-SMTP-para-envio-de-relat%C3%B3rios-por-e-mail)  
  
3 - Além dos parâmetros da documentação preencha os  parâmetros abaixo:

- MV\_PORSMTP = 587 (por exemplo) - Porta do smtp disponibilizada pelo servidor de E-mails utilizado

- MV\_RELAPSW = senha do e-mail (Senha APP, configurada no provedor de E-mail)

- MV\_RELAUSR = user (OBS: **Para Office365**, inclua todo o e-mail, inclusive domínio: MV\_RELAUSR = user@empresa.com.br)

IMPORTANTE: Caso faça uso de SSL é necessário configurar também o certificado conforme detalhes no item *"**Configurar SSL para comunicação**"* da página: [**CRM0022** - Integração do Cadastro de Atividades com Exchange Server](http://tdn.totvs.com/pages/viewpage.action?pageId=272712174)

**Configuração para utilização do módulo "Call - Center"(SIGATMK)**

3.1 - Entre com o usuário vinculado ao operador no Call - Center (Caso não possua um operador cadastrado  e vinculado ao usuário, acesse o link: [Cadastro de Operador (TMKA090)](https://tdn.totvs.com/x/IoT6E) 

3.2 - No cadastro de "Grupo de Atendimento" (TMKA040), informar o campo "Envia E-mail" (U0\_USAMAIL)/(U0\_TLCMAIL), nas aba Telemarketing / Telecobrança, como "1-SIM"

3.3 - Acessar o "Cadastro de Operadores" (TMKA090), selecionar a opção "Outras ações" e a opção "e-mail" e informar:

* "Conta"(CEMAIL): conta não é o e-mail, por isso deve ser retirada a extensão @[empresa.com.br.](http://empresa.com.br/)
* "Senha"(CSENHA): senha do e-mail do servidor de e-mail.

OBSERVAÇÂO: Caso tenha necessidade de aumentar o tamanho dos campos, realize o procedimento da documentação: [MP - FRAME - Como alterar o tamanho de um campo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000583568-MP-FRAME-Como-alterar-o-tamanho-de-um-campo)  aumentando os campos    
"Conta E-mail"(U7\_CONTA) e "Senha E-mail" (U7\_SENHA).

4 - No "Cadastro de Ações"(TMKA240) associe o "Responsável"(UQ\_CODRESP) ao usuário que receberá o e-mail. Ex: responsavel@email.com.br 

5 - Ao confirmar um atendimento (Telemarketing ou Telecobrança), ao selecionar uma ação caso o cadastro possua um responsável com e-mail cadastrado no SIGACFG (responsavel@email.com.br), o sistema enviará um e-mail para esse usuário. Independentes do status da operação.

**Observações Importantes:**

**TELECOBRANÇA:** Para atendimentos do Telecobrança basta preencher o campo "Responsável" (ACG\_OPERAD) com um usuário do sistema que tenha um e-mail vinculado.  
  
**TELEMARKETING:** Para atendimentos do telemarketing deve ser realizado o vínculo de ocorrência x ação (Para ser selecionada uma ação no Responsável"(UQ\_CODRESP) na rotina (TMKA240) do qual foi preenchido o e-mail no passo 4.  
  
Para efetuar esse relacionamento, segue abaixo um link com mais detalhes sobre o processo:  
[Processo para cadastrar Ocorrência x Ações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018472092-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Processo-para-cadastrar-Ocorr%C3%AAncia-x-A%C3%A7%C3%B5es)  
  
Após o processo ao selecionar uma ocorrência do qual a ação do e-mail possui um responsável, o disparo é realizado.
