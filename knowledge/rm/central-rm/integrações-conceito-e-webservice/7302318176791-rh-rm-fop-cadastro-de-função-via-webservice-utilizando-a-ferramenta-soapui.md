---
article_id: 7302318176791
category: Integrações - Conceito e WebService
content_hash: b495d8ada1b88dcfcd8e8c66f733d739193df3391b5aca7ccc58607097835c46
fetched_at: '2026-06-28T22:46:44.932577+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Cadastro de função via WebService utilizando a ferramenta SoapUI
type: support-article
updated_at: '2024-09-24T12:29:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7302318176791-RH-RM-FOP-Cadastro-de-fun%C3%A7%C3%A3o-via-WebService-utilizando-a-ferramenta-SoapUI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23912022494231) Tempo aproximado para leitura:**00:04:00 min****Dúvida**Como realizar a alteração de função no cadastro do funcionário via integração WebService, utilizando a ferramenta SoapUI?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar o processo de alteração do código de função, vamos utilizar o seguinte DataServer: **FopfuncaoData.**No aplicativo SoapUI, acesse**File | New SOAP Project** para iniciar um novo projeto no SoapUI.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17313468487191)  
  
Devemos informar um nome para o Projeto e a URL referente ao serviço que vamos realizar que será consumir um DataServer. Clique neste [Link](http://localhost:8051/wsPageIndex/) para obter o XML.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17313452799127)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17313468492695)  
  
Copie todo o endereço e cole no SoapUi  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17313452803735)

Após a criação do projeto, acessar **ReadRecord** e abrir o **Request 1**. Nessa tela você informa os parâmetros para consumo, mas primeiro temos que realizar o login como no RM. Clique em Auth e em Authorization, selecione Add New Authorization do Type Basic mesmo.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17313452806423)  
  
Informe o Usuário e senha do RM e marque a opção Authenticate pre-emptively e pronto, o acesso está concedido. Agora realizamos a passagem de Parâmetros, vamos usar o DataServer, **FopfuncaoData**, lembrando que para identificar qual é o Data Server basta, na respectiva tela do RM, pressionar o atalho CTRL+ALT+F9.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7302176063895)  
  
Sendo como **CODCOLIGADA, CODIGO** irei solicitar coligada 1, código função 00011, separados por ponto e vírgula cada chave. Podem existir apenas 1 ou mais de 2 PrimaryKey.  
  
No contexto, deve-se informar CODCOLIGADA, CODSISTEMA (ou CODAPLICACAO) e CODUSUÁRIO. Como utilizamos folha de pagamento o sistema é P, ficando:  
  
**CODCOLIGADA=1;CODAPLICACAO=P;CODUSUARIO=mestre.**Com todos parâmetros informados corretamente, clique em PLAY e observe o retorno no campo à direita.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7302182103575)  
  
Todas informações do RM serão apresentadas no XML a direita, separadas por TAG. Para alterar as informação, basta copiar o XML obtido nesse consumo e Realizar o SaveRecord, do mesmo modo.  
  
Deverá copiar desde <![CDATA] até ]]> para poder salvar.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7302221284119)  
  
Com o XML copiado, vamos utilizar um SaveRecord. Abra o Request 1 no canto esquerdo e informe o DataServer, o Contexto e também o botão Auth como feito em ReadRecord.  
  
Apague a interrogação em XML e cole o obtido pelo ReadRecord.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7302269953943)  
  
Qualquer informação editada dentro da TAG no XML será replicada no RM. clique em PLAY e observe o retorno no RM.  
  
**Saiba mais**[FopFucaoData](https://api.totvs.com.br/legado/devrm/bo_rm/FopFuncaoData.html?Objeto=FopFuncaoData)
