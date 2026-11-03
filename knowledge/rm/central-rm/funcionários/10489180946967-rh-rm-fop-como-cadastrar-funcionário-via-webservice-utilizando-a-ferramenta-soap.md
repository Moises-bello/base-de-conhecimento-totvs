---
article_id: 10489180946967
category: Funcionários
content_hash: f36d7b894c65af4de0fdf5fd10d1bc260626c28befd62b53a6c204f650912bc7
fetched_at: '2026-06-28T22:47:03.200620+00:00'
product: rm
section_id: 1500000861022
source: central-rm
title: RH - RM - FOP - Como cadastrar Funcionário via WebService utilizando a ferramenta
  SoapUI
type: support-article
updated_at: '2025-01-07T17:29:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10489180946967-RH-RM-FOP-Como-cadastrar-Funcion%C3%A1rio-via-WebService-utilizando-a-ferramenta-SoapUI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17745927989143) Tempo aproximado para leitura:**00:04:00 min** **Dúvida**Como Cadastrar funcionário via integração WebService, utilizando a ferramenta SoapUI?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar cadastra um novo funcionário, vamos utilizar o seguinte DataServer:

**FopFuncdata**No aplicativo SoapUI, acesse**File | New SOAP Project**para iniciar um novo projeto no SoapUI:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17745927995031)  
  
Devemos informar um nome para o Projeto e a URL referente ao serviço que vamos realizar que será consumir um DataServer. Clique neste [Link](http://localhost:8051/wsPageIndex/)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17745898125847)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17745928002327)  
  
Copie todo o endereço e cole no SoapUi:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17745898134551)

Após a criação do projeto, acessar **SaveRecord**e abrir o **Request 1**. Nessa tela você deverá informar os parâmetros para consumo, mas primeiro temos que realizar o login como no RM. Clique em **Auth**e em **Authorization**, selecione Add New Authorization do Type Basic mesmo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17745928014231)  
  
Informe o Usuário e senha do RM e marque a opção Authenticate pre-emptively e pronto, o acesso está concedido. Agora realizamos a passagem de Parâmetros, vamos usar o DataServer **FopFuncData**, lembrando que para identificar qual é o Data Server basta na respectiva tela do RM, pressionar o atalho**CTRL+ALT+F9.**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10489335109271)  
  
Apague a interrogação em XML e cole o obtido. No contexto, deve-se informar CODCOLIGADA, CODSISTEMA (ou CODAPLICACAO) e CODUSUÁRIO. Como utilizamos folha de pagamento o sistema é P, ficando: **CODCOLIGADA=1;CODAPLICACAO=P;CODUSUARIO=mestre.**  
  
Clique em PLAY e observe o retorno no RM, todas as informações contida no XML serão apresentadas no cadastro do funcionário.  
 **Saiba mais**[FopFuncData](https://apitotvslegado.z15.web.core.windows.net/FopFuncData.html?Objeto=FopFuncData)
