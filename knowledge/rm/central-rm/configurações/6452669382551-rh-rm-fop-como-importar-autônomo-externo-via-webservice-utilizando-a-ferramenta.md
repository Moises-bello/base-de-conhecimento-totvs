---
article_id: 6452669382551
category: Configurações
content_hash: aaf0f58a416c6229afa583add27800cff61ec125ca848a0d5bb8db0e64984317
fetched_at: '2026-06-28T22:46:49.510753+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Como importar autônomo externo via WebService utilizando a
  ferramenta SoapUI
type: support-article
updated_at: '2025-03-12T13:45:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6452669382551-RH-RM-FOP-Como-importar-aut%C3%B4nomo-externo-via-WebService-utilizando-a-ferramenta-SoapUI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: ****00:04:00 min******Dúvida**Como importar autônomo externo via integração WebService, utilizando a ferramenta SoapUI?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar o processo de importação do autônomo externo, vamos utilizar o seguinte DataServer: **FopPagAutonomosExtData**No aplicativo SoapUI, acesse**File | New SOAP Project** para iniciar um novo projeto no SoapUI:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749621615511/mceclip1.png)  
  
Devemos informar um nome para o Projeto e a URL referente ao serviço que vamos realizar que será consumir um DataServer. Clique neste [Link](http://localhost:8051/wsPageIndex/)para obter o XML  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749682924183/mceclip4.png)  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749762110359/mceclip5.png)  
  
Copie todo o endereço e cole no SoapUi:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5749774768023/mceclip6.png)

Após a criação do projeto, acessar **SaveRecord** e abrir o **Request 1**. Nessa tela você deverá informar os parâmetros para consumo, mas primeiro temos que realizar o login como no RM. Clique em **Auth** e em **Authorization**, selecione Add New Authorization do Type Basic mesmo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6452247447959/mceclip0.png)  
  
Informe o Usuário e senha do RM e marque a opção Authenticate pre-emptively e pronto, o acesso está concedido. Agora realizamos a passagem de Parâmetros, vamos usar o DataServer **FopPagAutonomosExtData**, lembrando que para identificar qual é o Data Server basta na respectiva tela do RM, pressionar o atalho **CTRL+ALT+F9.**  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6452605833367/mceclip3.png)  
  
Apague a interrogação em XML e cole o obtido. No contexto, deve-se informar CODCOLIGADA, CODSISTEMA (ou CODAPLICACAO) e CODUSUÁRIO. Como utilizamos folha de pagamento o sistema é P, ficando: **CODCOLIGADA=1;CODAPLICACAO=P;CODUSUARIO=mestre.**  
  
Qualquer informação dentro da TAG no XML será replicada no RM. Clique em PLAY e observe o retorno no RM:  
  
**Encargos | autônomos externos**  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6452847322391/mceclip4.png)  
  
**Saiba mais** **[FopPagAutonomosExtData](https://api.totvs.com.br/legado/devrm/bo_rm/FopPagAutonomosExtData.html?Objeto=FopPagAutonomosExtData)**
