---
article_id: 18171378062615
category: Integrações - Conceito e WebService
content_hash: 92f4c2e8adbc8c522ed66bf4d71de08b6415581dbd00e5a9f353b96f52feb7a7
fetched_at: '2026-06-28T22:46:44.700563+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - FOP - Como utilizar o DataServer do TBC no SoapUI
type: support-article
updated_at: '2025-01-07T17:38:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18171378062615-RH-RM-FOP-Como-utilizar-o-DataServer-do-TBC-no-SoapUI
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18171363235351) Tempo aproximado para leitura: **00:02:31 min****Dúvida**Como utilizar o DataServer TBC no SoapUI?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para  efetuar a configuração no SoapUI, para consumir o Data Server do Totvs Business Conector.

**1º Passo:** Acesse o TBC para consultar os serviços:

<http://localhost:8051/wspageindex/>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18171082713623)
Obs.: A porta do local host é configurada no momento da instalação das Bibliotecas do RM Totvs. É importante que sempre seja validada esta informação

**2º Passo:** Clique no WSDL desejado. Nesse exemplo vamos conectar ao WSDL referente ao Data Server:

![](https://comunidade.knowgap.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBenozdVE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--ea0c07acef8692b116a893d5e9908c9797af493b/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNITUdrQ09BUTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--cfda350175ba87e768b4e96e935a8171fc679bec/image.png)
Lembrando que esse WSDL possibilita efetuar leitura das tabelas do RM Totvs. No próprio link é possível acessar outros tipos de Serviços, como execução de Consultas SQL, Relatórios e outros objetos.

Será aberta a tela conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18171218515735)
  
Copie o endereço que foi aberto: <http://localhost:8051/wsDataServer/MEX?wsdl>

**3º Passo:** Acessar o SoapUI e inserir um novo projeto:

![](https://comunidade.knowgap.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBNHozdVE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--c4ef9506a3f8781ad4fcff8e3d88d4b2ca3fa0d6/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNITUdrQ09BUTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--cfda350175ba87e768b4e96e935a8171fc679bec/image.png)
Informar os dados conforme copiado do TBC:
![](https://comunidade.knowgap.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBNW4zdVE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--541d4776bb7a0c1568fe67034e1d5679802da39c/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNITUdrQ09BUTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--cfda350175ba87e768b4e96e935a8171fc679bec/image.png)
No campo “Project Name” informar o nome do projeto e no campo “Initial WSDL” informar a URL copiada do TBC. Após informar os dados, clique em “OK”.

**4º Passo:** Após clicar em OK, será criado o projeto:

![](https://comunidade.knowgap.com.br/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBBN1AzdVE9PSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--0ddd02d34a5d79f194b7a76441f739d0bdfa843d/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNITUdrQ09BUTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--cfda350175ba87e768b4e96e935a8171fc679bec/image.png)
