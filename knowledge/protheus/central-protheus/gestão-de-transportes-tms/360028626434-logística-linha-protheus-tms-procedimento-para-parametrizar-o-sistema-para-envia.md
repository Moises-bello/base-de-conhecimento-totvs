---
article_id: 360028626434
category: Gestão de Transportes (TMS)
content_hash: df50e4b70d3f41a6a5350b17c3bf2f511d24ab4a77ebcb5c8808774a1975ad54
fetched_at: '2026-06-28T22:45:32.487294+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Procedimento para parametrizar o Sistema
  para enviar e-mail do XML de CT-e
type: support-article
updated_at: '2025-07-23T13:14:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028626434-Log%C3%ADstica-Linha-Protheus-TMS-Procedimento-para-parametrizar-o-Sistema-para-enviar-e-mail-do-XML-de-CT-e
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21125245860375)***Tempo aproximado para leitura: **00:00:50 min**  
**Dúvida**Como parametrizar o Sistema para enviar e-mail do **XML - Extensible Markup Language** de **CT-e - Conhecimento de Transporte Eletrônico**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões.  
  
**Solução**Para enviar o e-mail do arquivo **XML** e **DACTE - Documento Auxiliar do Conhecimento de Transporte Eletrônico** para o cliente, é necessário que no cadastro do cliente devedor, o campo **A1\_EMAIL** esteja preenchido. Não poderá conter caractere especial ou espaços.  
Caso deseje inserir mais de um e-mail, basta separa-los por ponto e virgula.No arquivo **APPSERVER.INI** da instalação do **TSS - Totvs Sped Service**, deverá existir o parâmetro **SPED\_DELMAIL** igual a **1.**Com essa configuração, o **TSS**efetuará o envio do e-mail para o cliente devedor quando o **CT-e** for autorizado ou quando o cancelamento do **CT-e** for autorizado pelo **SEFAZ**.  
  
Após a transmissão, os endereços de e-mails serão gravados na tabela do **TSS** **SPED050**, campo **EMAIL.**

**Saiba mais**   
Para maiores informações sobre envio de e-mails pelo TSS, acesse:  
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como enviar DANFE e XML por e-mail via TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043007793-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-enviar-DANFE-e-XML-por-e-mail-via-TSS?source=search)  
  
Caso deseje enviar o **DACTE** customizado por e-mail, acesse:  
[Configurando o envio de DACTE Customizada por E-mail.](https://tdn.totvs.com/pages/viewpage.action?pageId=632498882)
