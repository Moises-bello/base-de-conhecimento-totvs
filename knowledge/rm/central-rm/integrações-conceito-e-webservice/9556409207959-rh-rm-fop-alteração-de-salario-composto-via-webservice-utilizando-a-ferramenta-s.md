---
article_id: 9556409207959
category: Integrações - Conceito e WebService
content_hash: e80325613f2a3918913cd24f064fb6fde0b1eb382637f1e311c586f1b4ccefd5
fetched_at: '2026-06-28T22:46:44.927599+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Alteração de Salario Composto via WebService utilizando a ferramenta
  SoapUI
type: support-article
updated_at: '2025-02-03T17:14:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9556409207959-RH-RM-FOP-Altera%C3%A7%C3%A3o-de-Salario-Composto-via-WebService-utilizando-a-ferramenta-SoapUI
---

**Dúvida**Como realizar a alteração de salario composto via integração WebService, utilizando a ferramenta SoapUI?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar o processo de alteração de salario composto, vamos utilizar o seguinte DataServer: **FopSalCompostoData.**1. No aplicativo SoapUI, acesse **File | New SOAP Project**para iniciar um novo projeto no SoapUI.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29715515172119)  
  
2. Informe um nome para o Projeto e a URL referente ao serviço que vamos realizar que será consumir um DataServer. Clique neste [Link](http://localhost:8051/wsPageIndex/) para obter o endereço local.  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29715515174935)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29715526346391)  
  
3. Copie todo o endereço e cole no SoapUi  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29715515180311)

4. Após a criação do projeto, acessar **ReadRecord** e abrir o **Request 1**. Nessa tela você informa os parâmetros para consumo, mas primeiro temos que realizar o login como no RM. Clique em Auth e em Authorization, selecione Add New Authorization do Type Basic mesmo.  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29715526351767)  
  
5. Informe o Usuário e senha do RM e marque a opção Authenticate pre-emptively e pronto, o acesso está concedido. Agora realizamos a passagem de Parâmetros, vamos usar o DataServer **FopSalCompostoData**, lembrando que para identificar qual é o Data Server basta, na respectiva tela do RM, pressionar o atalho CTRL+ALT+F9.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9556302638615)  
  
5.1. Sendo como **CODCOLIGADA, CHAPA** irei solicitar coligada 1, Chapa 00001, separados por ponto e vírgula cada chave. Podem existir apenas 1 ou mais de 2 PrimaryKey.  
  
5.2. No contexto, deve-se informar CODCOLIGADA, CODSISTEMA (ou CODAPLICACAO) e CODUSUÁRIO. Como utilizamos folha de pagamento o sistema é P, ficando: **CODCOLIGADA=1;CODAPLICACAO=P;CODUSUARIO=mestre.**6. Com todos parâmetros informados corretamente, clique em PLAY e observe o retorno no campo à direita.  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9556308178071)  
  
6.1 Todas informações do RM serão apresentadas no XML a direita, separadas por TAG. Para alterar as informação, basta copiar o XML obtido nesse consumo e Realizar o SaveRecord, do mesmo modo.  
  
7. Copiar desde <![CDATA] até ]]> para poder salvar.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9556396847767)  
  
7.1. Com o XML copiado, vamos utilizar um SaveRecord. Abra o Request 1 no canto esquerdo e informe o DataServer, o Contexto e também o botão Auth como feito em ReadRecord.  
  
7.2. Apague a interrogação em XML e cole o obtido pelo ReadRecord.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29715515184407)  
  
7.3. Qualquer informação editada dentro da TAG no XML será replicada no RM. clique em PLAY e observe o retorno no RM.  
  
**Saiba mais**[FopSalCompostoData](https://api.totvs.com.br/legado/devrm/bo_rm/FopSalCompostoData.html?Objeto=FopSalCompostoData)
