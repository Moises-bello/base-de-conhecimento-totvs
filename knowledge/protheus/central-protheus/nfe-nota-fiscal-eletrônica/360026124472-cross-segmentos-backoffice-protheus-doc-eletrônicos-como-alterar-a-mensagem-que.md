---
article_id: 360026124472
category: NFe - Nota Fiscal Eletrônica
content_hash: 08ef048df54672ddad0f27bb20d62925abd6897be524fa50b7b4bbf4befc7c81
fetched_at: '2026-06-28T22:40:05.620958+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como alterar a mensagem
  que é enviada o xml e DANFE por e-mail
type: support-article
updated_at: '2025-12-01T12:48:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026124472-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-alterar-a-mensagem-que-%C3%A9-enviada-o-xml-e-DANFE-por-e-mail
---

**Dúvida**Como alterar a mensagem que é enviada o xml e DANFE por e-mail   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

O e-mail é possível **alterar** somente o **texto e a cor de fundo.**  
  
Para modificar o **texto ou fundo do E-mail** que é enviado é necessário alterar o arquivo chamado **TotvsMail** que contém a extensão **HTML.**  
  
1º Realize o Backup do arquivo **TotvsMail** antes de ser alterado;

2º Deve ir até o diretório do servidor de TSS que contenha o arquivo TotvsMail   
  
**C:\totvssped\mailtemplate**  
  
3º Para o texto, o sistema lê o arquivo TotvsMail e o cliente deverá efetuar as **trocas (macro) em tudo que tiver <%= %>**  
  
Para **cores** o sistema **lê os códigos RGB**  
  
4º Após todas as alterações realizadas **salvar o arquivo**, cada template deve ter seu **nome especifico:**  
  
NFeCanc.html -> template de cancelamento de nfe  
NFe.html -> template de nfe  
CTe.html -> template de cte  
CCe.html -> template de cce  
EventoCTe.html -> template de evento cte  
nfse.html -> template de nfse  
nfsecanc.html -> template de cancelamento provedor  
nfsenac -> template nfse nacional  
cancnac -> template nfse nacional cancelamento  
  
  
**Obs.** Deve-se ter conhecimento em HTML para tais alterações.

* **Saiba mais:**

* Ao configurar o Danfe por e-mail há 3 opções:

**0-**Desabilitado (**não envia** o DANFE por e-mail)  
**1-** Enviar DANFE do TSS (neste caso é enviado DANFE com layout **padrão do TSS**)  
**2-** Enviar DANFE do ERP (neste caso é enviado DANFE com layout **do ERP que pode conter customização**)

[MP - TSS - Como enviar DANFE por e-mail via TSS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043007793)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25346258758167)

Ao escolher a **opção 1 ou 2** será enviada a mensagem alterada do **Danfe por e-mail**
