---
article_id: 28451460305687
category: Suricato
content_hash: 531ee4d267027250bf660205795cbcb226beaccb41898652a9985a794e28a15f
fetched_at: '2026-06-28T22:46:26.364942+00:00'
product: rm
section_id: 28312167464215
source: central-rm
title: RH - RM - PTO - Como gerar o log do webservice RM e os XMLs da integração com
  o Suricato
type: support-article
updated_at: '2025-09-09T19:46:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28451460305687-RH-RM-PTO-Como-gerar-o-log-do-webservice-RM-e-os-XMLs-da-integra%C3%A7%C3%A3o-com-o-Suricato
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28451445988247) Tempo aproximado para leitura: **00:05:00min****Dúvida**

Como gerar o log do webservice RM e os XMLs da integração com o Suricato?

**Ambiente**TOTVS RH - TOTVS RH(Linha RM) - Automação de Ponto - A partir da versão 12.1

**Solução**

1. Acesse o Servidor onde está instalado o Webservice RM
2. Abra o arquivo Web.config do Webservice RM (Caminho padrão C:\TSA)
3. Localize a tag WebServiceIntegracaoTSALogEnabled.
   * Para ativar o log altere o valor para true
   * Para desativar altere o valor para false

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28451445989527)

4. O Log será salvo no servidor onde está configurado o Webservice RM e o caminho do log é definido na tag **LogWebServiceIntegracaoTSAPath**

* O caminho padrão do log é **C:\LogWebServiceIntegracaoTSA**
* E o nome padrão do log é **WebServiceIntegracaoTSALog.txt**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28451460285335)

5. Após habilitar o log, para gerar os XMLs da integração é preciso adicionar no arquivo Web.config do WebserviceRM a tag **<add key="WebServiceMensagensPath" value="C:\LogWebServiceIntegracaoTSA"/>**

* A tag deve ser inserida após a tag **<appSettings>**
* O valor da tag é o caminho onde serão gerados os xmls

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28451460289047)

6. Para efetivar as alterações reinicie o IIS.

Quando uma ação no RM for realizada que envolva a integração com o Suricato, serão gerados os arquivos XMLs request e response (como na imagem abaixo) assim como o log que poderão ser encaminhados ao time de suporte para análise.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28451460290327)
