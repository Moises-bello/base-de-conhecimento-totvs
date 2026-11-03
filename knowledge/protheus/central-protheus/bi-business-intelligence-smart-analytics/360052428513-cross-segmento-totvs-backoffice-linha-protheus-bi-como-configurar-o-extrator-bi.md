---
article_id: 360052428513
category: BI - Business Intelligence - Smart analytics
content_hash: 44096b5cccb203db0ed960cc2529a6915ab1fb1ad949847d8e59fe81ced61033
fetched_at: '2026-06-28T22:37:04.118310+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Como configurar o extrator
  BI do Protheus - Smart Analytics
type: support-article
updated_at: '2021-09-17T17:47:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052428513-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Como-configurar-o-extrator-BI-do-Protheus-Smart-Analytics
---

**Dúvida**Como configuro o extrator BI do Protheus para o Smart Analytics?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Smart Analytics – Todas as versões.  
  
**Solução**Para configurar a extração de dados do Protheus para o Smart Analytics, é necessário inicialmente efetuar a conexão do Banco de Dados com o Extrator BI.   
Dentro do **Configurador**, acesse **Ambiente / Extratores BI/ Config. Parâmetros.**O **Wizard de Configuração** será exibido, informe os parâmetros desejados e clique em **Avançar**.

**Exemplo:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083004393/mceclip0.png)

**Tipo de Conexão ao DBAccess:**TCP/IP ou *Named Pipes*

**Tipo de Banco de Dados:**Microsoft SQL  
IBM DB2  
Oracle  
Informix

**Servidor do Banco de Dados:**Informe o IP (Internet Protocol) ou nome do servidor de banco de dados configurado no DBAccess.

**Porta do Servidor DBAccess:**Informe a porta do servidor configurado no DBAccess.

**Alias no DBAccess:**Informe o *alias* configurado no DBAccess para o servidor de banco de dados.  
Após a conexão ser bem sucedida, basta prosseguir com as parametrizações do extrator e completar a ação.  
Lembrando que por boas práticas, o extrator utiliza um banco apartado da produção (Alias do DbAccess) configurado no ODBC e na ferramenta de banco de dados.

**Saiba mais**  
[Configuração dos Parâmetros do Extrator BI](https://tdn.totvs.com/pages/releaseview.action?pageId=237373225)

[Extrator BI - Documentação](https://tdn.totvs.com/pages/releaseview.action?pageId=240976367)
