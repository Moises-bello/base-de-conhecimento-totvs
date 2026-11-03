---
article_id: 5968323614871
category: Integrações - Conceito e WebService
content_hash: 7be20f339853628f0a5c57b6203d9876399945a7a2d6c161c24964d6528a6b0a
fetched_at: '2026-06-28T22:46:44.937490+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Alteração dos dados do dependente FopDependData via WebService
  utilizando a ferramenta SoapUI
type: support-article
updated_at: '2025-12-18T17:32:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5968323614871-RH-RM-FOP-Altera%C3%A7%C3%A3o-dos-dados-do-dependente-FopDependData-via-WebService-utilizando-a-ferramenta-SoapUI
---

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para realizar o processo de alteração dos dados do dependente, vamos utilizar o seguinte DataServer: **FopDependData**  
  
No aplicativo SoapUI, acesse**File | New SOAP Project** para iniciar um novo projeto no SoapUI:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24167562990871)  
  
Devemos informar um nome para o Projeto e a URL referente ao serviço que vamos realizar que será consumir um DataServer. Clique neste [Link](http://localhost:8051/wsPageIndex/)para obter o XML.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24167516270999)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24167516283415)  
  
Copie todo o endereço e cole no SoapUi:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24167563026455)

Após a criação do projeto, acessar **ReadRecord** e abrir o **Request 1**. Nessa tela você informa os parâmetros para consumo, mas primeiro temos que realizar o login como no RM. Clique em Auth e em Authorization, selecione Add New Authorization do Type Basic mesmo.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24167516306327)  
  
Informe o Usuário e senha do RM e marque a opção Authenticate pre-emptively e pronto, o acesso está concedido. Agora realizamos a passagem de Parâmetros, vamos usar o DataServer, **FopDependData**, lembrando que para identificar qual é o Data Server basta, na respectiva tela do RM, pressionar o atalho CTRL+ALT+F9.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5976306335767)  
  
Sendo como **CODCOLIGADA, CHAPA, NRODEPEND** irei solicitar o registro do funcionário X coligada 1, chapa 00001, e condigo do dependente 1 separados por ponto e vírgula cada chave. Podem existir apenas 1 ou mais de 2 PrimaryKey.  
  
No contexto, deve-se informar CODCOLIGADA, CODSISTEMA (ou CODAPLICACAO) e CODUSUÁRIO. Como utilizamos folha de pagamento o sistema é P, ficando:  
  
**CODCOLIGADA=1;CODAPLICACAO=P;CODUSUARIO=mestre.**  
  
Com todos parâmetros informados corretamente, clique em *PLAY* e observe o retorno no campo à direita.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5968337921559)  
  
Todas informações do RM serão apresentadas no XML a direita, separadas por TAG. Para alterar as informação, basta copiar o XML obtido nesse consumo e Realizar o SaveRecord, do mesmo modo.  
  
Deverá copiar desde <![CDATA] até ]]> para poder salvar:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5975167981975)  
  
Com o XML copiado, vamos utilizar um SaveRecord. Abra o Request 1 no canto esquerdo e informe o DataServer, o Contexto e também o botão Auth como feito em ReadRecord.  
  
Apague a interrogação em XML e cole o obtido pelo ReadRecord.  
  
![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24167516309143)  
  
Qualquer informação editada dentro da TAG no XML será replicada no RM. clique em PLAY e observe o retorno no RM.
