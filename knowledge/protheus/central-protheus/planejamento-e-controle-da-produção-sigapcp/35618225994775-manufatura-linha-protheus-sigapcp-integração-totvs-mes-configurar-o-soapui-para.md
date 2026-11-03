---
article_id: 35618225994775
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 03cacc55662bafbf4be0b25095809c9be9c0427e4e1199420ba26409809bc285
fetched_at: '2026-06-28T22:42:43.451680+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Integração TOTVS MES - Configurar o
  SoapUI para teste com o TOTVS MES
type: support-article
updated_at: '2025-10-17T17:54:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35618225994775-Manufatura-Linha-Protheus-SIGAPCP-Integra%C3%A7%C3%A3o-TOTVS-MES-Configurar-o-SoapUI-para-teste-com-o-TOTVS-MES
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35618225967255)** Tempo aproximado para leitura:**00:01:44 min**  
  
**Dúvida**  
Como configurar a ferramenta **SoapUI** para testes de integração do **TOTVS MES** com o **Protheus**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O **SoapUI** é uma aplicação *open source* utilizada para envio de mensagens para **Web Services**.  
Possibilita enviar **XMLs** para reprocessar lançamentos e verificar erros de comunicação de forma externa às aplicações do **Totvs MES**.  
  
Após *download* da ferramenta, com o **SoapUI** aberto, criar um novo projeto:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35618236720791)  
  
Em seguida preencher os dados para conexão com o **WebService**. Deverá ser informado o caminho do **WebService** do **Protheus**, que segue o seguinte formato:  
  
**IP:porta/WSPCP.apw?WSDL**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35618225971735)  
  
Neste momento será criada a árvore com os métodos e as requisições de acordo com o **WebService**.  
Clique no nome do projeto WSPCPSOAP, ReceiveMessage e com o botão direito New Request  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35618236722455)  
  
Será aberta a tela abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35618225973911)  
  
O conteúdo do **XML** deverá ser informado no lugar do **?** , acrescentando a informação **<![CDATA[  <conteúdo xml>  ]]>** :  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35618225977111)  
  
Neste espaço deverá ser inserido o conteúdo de arquivo **XML** gerado pelo **Totvs MES** e que deve ser integrado ao **Protheus**.  
  
Para execução do **XML** utilizar o botão **Submit Request**, onde o resultado do processamento será apresentado na tela ao lado direito.  
  
**Saiba mais**  
*Link* para *download* do **SoapUI Open Source**: <https://www.soapui.org/downloads/soapui/>
