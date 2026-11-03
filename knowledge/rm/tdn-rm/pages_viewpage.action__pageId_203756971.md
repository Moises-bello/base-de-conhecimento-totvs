---
content_hash: 92621ee7848ad08ed70d1194c4e70e916181765ba87edb5d9e42a99215bc1c62
fetched_at: '2026-06-29T00:06:09.764320+00:00'
page_id: '203756971'
product: rm
source: tdn-rm
title: ER_PCREQ - 6543_SAÚDE_CIH_FLUIG_12.1.9_CONFIGURAÇÕES
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=203756971
version: 1
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS CIH | **Módulo** | CONFIGURAÇÕES |
| **Segmento Executor** | SAÚDE | | |
| **Projeto1** | SAÚDE\_CIH\_FLUIG\_12.1.9 | **IRM1** | * [PCREQ-6530](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-6530 "PCREQ-6530") |
| **Requisito1** | * [PCREQ-6543](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-6543 "PCREQ-6543") | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | ( X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

A rotina tem como objetivo o envoi de questionários para controle de pós-alta dos pacientes cirúrgicos que passaram pelo hospital. Esse questionário é utilizado para vigilância pós-alta.  

### Definição da Regra de Negócio

**Envio de e-mail Pós Alta**

 

1. O usuário poderá configurar duas maneiras para o paciente receber o e-mail:
   1. Informando o intervalo de datas na qual tenha ocorrido a alta do paciente de sua internação;
   2. Informando a defasagem de dias em relação à data atual da data da alta da internação e informar também o número de dias que irá compor este período.
2. O corpo do e-mail será configurado pelo usuário, podendo criar quantos e-mails for necessário;
3. Após as configurações necessárias, o usuário selecionará o corpo do e-mail que será utilizado e informará o Título do E-mail a ser enviado e executará;
4. Ao executar processo, o CIH irá percorrer todas as internações que já possuíram alta e se enquadram nas configurações e enviará um e-mail a cada paciente.
5. Caso ocorra algum erro no momento da execução, o CIH adicionará no log de execução do processo o motivo do não envio do e-mail.

 

 

**Envio de e-mail de Produção Cirúrgica**

 

1. O usuário irá informar               a defasagem de dias em relação à data atual;
2. O corpo do e-mail será configurado pelo usuário, podendo criar quantos e-mails for necessário;
3. Após as configurações necessárias, o usuário selecionará o corpo do e-mail que será utilizado e informará o Título do E-mail a ser enviado e executará;

 

 

1. Ao executar processo, o CIH irá percorrer todas cirurgias que foram realizadas, de acordo com a defasagem informada, agrupará por médicos e enviará os e-mails aos médicos contendo as informações de produção cirúrgica de cada um.

 

 

**Envio de e-mail Alerta de Cultura Positiva**

 

1. O usuário deverá definir um e-mail para cada unidade existente no hospital;
2. Usuário configura o corpo do e-mail, que será usado para Alerta de Cultura Positiva;
3. Após as configurações realizadas, ao selecionar a opção “Alerta de Cultura Positiva”, o CIH deverá verificar a qual unidade o paciente pertence e enviar o e-mail para o setor alertando o isolamento do Paciente.

### Protótipo de Tela

## Fluxo do Processo

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
