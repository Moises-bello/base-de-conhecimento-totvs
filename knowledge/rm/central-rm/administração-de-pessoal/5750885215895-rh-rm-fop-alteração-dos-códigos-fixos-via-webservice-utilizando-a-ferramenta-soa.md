---
article_id: 5750885215895
category: Administração de Pessoal
content_hash: 56865fd5427b41668b13275b6751fd1a014d055e36cf75ff024719c2387c54af
fetched_at: '2026-06-28T22:47:01.358729+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: 'RH - RM - FOP - Alteração dos códigos fixos via WebService utilizando a ferramenta
  SoapUI '
type: support-article
updated_at: '2025-03-13T09:55:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5750885215895-RH-RM-FOP-Altera%C3%A7%C3%A3o-dos-c%C3%B3digos-fixos-via-WebService-utilizando-a-ferramenta-SoapUI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como realizar a alteração dos códigos fixos via integração WebService, utilizando a ferramenta SoapUI?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar o processo de alteração dos códigos fixos, vamos utilizar o seguinte DataServer: **FopCodFixData.**No aplicativo SoapUI, acesse**File | New SOAP Project** para iniciar um novo projeto no SoapUI.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749621615511/mceclip1.png)  
  
Devemos informar um nome para o Projeto e a URL referente ao serviço que vamos realizar que será consumir um DataServer. Clique neste [Link](http://localhost:8051/wsPageIndex/) para obter o XML.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749682924183/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749762110359/mceclip5.png)  
  
Copie todo o endereço e cole no SoapUi  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749774768023/mceclip6.png)

Após a criação do projeto, acessar **ReadRecord** e abrir o **Request 1**. Nessa tela você informa os parâmetros para consumo, mas primeiro temos que realizar o login como no RM. Clique em Auth e em Authorization, selecione Add New Authorization do Type Basic mesmo.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749955727511/mceclip8.png)  
  
Informe o Usuário e senha do RM e marque a opção Authenticate pre-emptively e pronto, o acesso está concedido. Agora realizamos a passagem de Parâmetros, vamos usar o DataServer, **FopCodFixData**, lembrando que para identificar qual é o Data Server basta, na respectiva tela do RM, pressionar o atalho CTRL+ALT+F9.  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5750178928791/mceclip10.png)  
  
Sendo como **CODCOLIGADA, CHAPA, CODEVENTO** irei solicitar o registro do funcionário X coligada 1, chapa 00001, e o evento de código 002 separados por ponto e vírgula cada chave. Podem existir apenas 1 ou mais de 2 PrimaryKey.  
  
No contexto, deve-se informar CODCOLIGADA, CODSISTEMA (ou CODAPLICACAO) e CODUSUÁRIO. Como utilizamos folha de pagamento o sistema é P, ficando:  
  
**CODCOLIGADA=1;CODAPLICACAO=P;CODUSUARIO=mestre.**Com todos parâmetros informados corretamente, clique em PLAY e observe o retorno no campo à direita.  
  
![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5750520009623/mceclip11.png)  
  
Todas informações do RM serão apresentadas no XML a direita, separadas por TAG. Para alterar as informação, basta copiar o XML obtido nesse consumo e Realizar o SaveRecord, do mesmo modo.  
  
Deverá copiar desde <![CDATA] até ]]> para poder salvar.  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5750618536215/mceclip12.png)  
  
Com o XML copiado, vamos utilizar um SaveRecord. Abra o Request 1 no canto esquerdo e informe o DataServer, o Contexto e também o botão Auth como feito em ReadRecord.  
  
Apague a interrogação em XML e cole o obtido pelo ReadRecord.  
  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5750821475095/mceclip14.png)  
  
Qualquer informação editada dentro da TAG no XML será replicada no RM. clique em PLAY e observe o retorno no RM.  
  
**Saiba mais**[FopCodFixData](https://api.totvs.com.br/legado/devrm/bo_rm/FopCodFixData.html?Objeto=FopCodFixData)
