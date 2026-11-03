---
article_id: 11545423487383
category: Integrações - Conceito e WebService
content_hash: e916ecba5e4c94a7091f927780431427a09f74d5c2a16edd5e445eedb738ab76
fetched_at: '2026-06-28T22:46:44.918918+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Como gerar avisos automáticos via WebService, utilizando a
  ferramenta SoapUI
type: support-article
updated_at: '2025-01-07T18:15:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11545423487383-RH-RM-FOP-Como-gerar-avisos-autom%C3%A1ticos-via-WebService-utilizando-a-ferramenta-SoapUI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23528007003159)**Tempo aproximado para leitura: **00:04:00 min****Dúvida**Como gerar avisos automáticos via integração WebService, utilizando a ferramenta SoapUI?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar o processo de geração dos avisos automáticos via webservice e necessário utilizar o seguinte DataServer: **FopProgAvisoAutoData** No aplicativo SoapUI, acesse**File | New SOAP Project** para iniciar um novo projeto no SoapUI.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23528040568855)  
  
Devemos informar um nome para o Projeto e a URL referente ao serviço que vamos realizar que será consumir um DataServer. Clique neste [Link](http://localhost:8051/wsPageIndex/)para obter o XML.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23528040579479)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23528017138327)  
  
Copie todo o endereço e cole no SoapUi  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23528017141399)

Após a criação do projeto, acessar **ReadRecord** e abrir o **Request 1**. Nessa tela você informa os parâmetros para consumo, mas primeiro temos que realizar o login como no RM. Clique em Auth e em Authorization, selecione Add New Authorization do Type Basic mesmo.  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23528040611607)  
  
Informe o Usuário e senha do RM e marque a opção Authenticate pre-emptively e pronto, o acesso está concedido. Agora realizamos a passagem de Parâmetros, vamos usar o DataServer, **FopProgAvisoAutoData** lembrando que para identificar qual é o Data Server basta, na respectiva tela do RM, pressionar o atalho CTRL+ALT+F9.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11545263362711)  
  
Sendo como **CODCOLIGADA, IDAVISO** irei solicitar a coligada 1, idaviso 4, separados por ponto e vírgula cada chave. Podem existir apenas 1 ou mais de 2 PrimaryKey.  
  
No contexto, deve-se informar CODCOLIGADA, CODSISTEMA (ou CODAPLICACAO) e CODUSUÁRIO. Como utilizamos folha de pagamento o sistema é P, ficando:  
  
**CODCOLIGADA=1;CODAPLICACAO=P;CODUSUARIO=mestre.**Com todos parâmetros informados corretamente, clique em PLAY e observe o retorno no campo à direita.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11545339883671)  
  
Todas informações do RM serão apresentadas no XML a direita, separadas por TAG. Para alterar as informação, basta copiar o XML obtido nesse consumo e Realizar o SaveRecord, do mesmo modo.  
  
Deverá copiar desde <![CDATA] até ]]> para poder salvar.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11545349264535)  
  
Com o XML copiado, vamos utilizar um SaveRecord. Abra o Request 1 no canto esquerdo e informe o DataServer, o Contexto e também o botão Auth como feito em ReadRecord.  
  
Apague a interrogação em XML e cole o obtido pelo ReadRecord.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11545418782487)  
  
Qualquer informação editada dentro da TAG no XML será replicada no RM. clique em PLAY e observe o retorno no RM.  
  
**Saiba mais****[FopProgAvisoAutoData](https://api.totvs.com.br/legado/devrm/bo_rm/FopProgAvisoAutoData.html?Objeto=FopProgAvisoAutoData)**
