---
article_id: 6986600848663
category: Administração de Pessoal
content_hash: e3be6654e1764e6a59a80276f8f53e9bbbf3dca27c85624f490930b56c60fb0b
fetched_at: '2026-06-28T22:47:01.326878+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Cadastro de Rescisão via WebService utilizando a ferramenta
  SoapUI
type: support-article
updated_at: '2025-03-12T13:38:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6986600848663-RH-RM-FOP-Cadastro-de-Rescis%C3%A3o-via-WebService-utilizando-a-ferramenta-SoapUI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min****Dúvida**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar o processo de rescisão, vamos utilizar o seguinte DataServer: **FopRescisaoData**No aplicativo SoapUI, acesse**File | New SOAP Project** para iniciar um novo projeto no SoapUI:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749621615511/mceclip1.png)  
  
Devemos informar um nome para o Projeto e a URL referente ao serviço que vamos realizar que será consumir um DataServer. Clique neste [Link](http://localhost:8051/wsPageIndex/)para obter o XML.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749682924183/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749762110359/mceclip5.png)  
  
Copie todo o endereço e cole no SoapUi:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749774768023/mceclip6.png)

Após a criação do projeto, acessar **SaveRecord** e abrir o **Request 1**. Nessa tela você informa os parâmetros para consumo, mas primeiro temos que realizar o login como no RM. Clique em Auth e em Authorization, selecione Add New Authorization do Type Basic mesmo.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749955727511/mceclip8.png)  
  
Informe o Usuário e senha do RM e marque a opção Authenticate pre-emptively e pronto, o acesso está concedido. Agora realizamos a passagem de Parâmetros, vamos usar o DataServer, **FopRescisaoData**, lembrando que para identificar qual é o Data Server basta, na respectiva tela do RM, pressionar o atalho CTRL+ALT+F9.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6986678079255/mceclip1.png)

No contexto, deve-se informar CODCOLIGADA, CODSISTEMA (ou CODAPLICACAO) e CODUSUÁRIO. Como utilizamos folha de pagamento o sistema é P, ficando:  
  
**CODCOLIGADA=1;CODAPLICACAO=P;CODUSUARIO=mestre.**  
  
Com o XML copiado, acessar SaveRecord. Abra o Request 1.  
  
Apague a interrogação em XML e cole o obtido.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6986756728983/mceclip2.png)  
  
Qualquer informação dentro da TAG no XML será replicada no RM. clique em PLAY e observe o retorno no RM.  
 **Saiba mais**[FopRescisaoData](https://api.totvs.com.br/legado/devrm/bo_rm/FopRescisaoData.html?Objeto=FopRescisaoData)
