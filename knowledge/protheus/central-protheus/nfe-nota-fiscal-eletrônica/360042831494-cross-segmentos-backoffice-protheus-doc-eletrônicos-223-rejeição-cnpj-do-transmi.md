---
article_id: 360042831494
category: NFe - Nota Fiscal Eletrônica
content_hash: 46f35a3dd31f571c2b515f889835bcb5edafd0b52b339d325274fb912f719dc0
fetched_at: '2026-06-28T22:40:00.193038+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: '  Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 223 Rejeição
  : CNPJ do transmissor do lote difere do CNPJ do transmissor da consulta'
type: support-article
updated_at: '2021-10-08T17:48:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042831494--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-223-Rejei%C3%A7%C3%A3o-CNPJ-do-transmissor-do-lote-difere-do-CNPJ-do-transmissor-da-consulta
---

**Dúvida**

Como corrigir a 223 Rejeição: CNPJ do transmissor do lote difere do CNPJ do transmissor da consulta ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Validação da SEFAZ:**

A **Rejeição (223)**: “CNPJ do transmissor do lote difere do CNPJ do transmissor da consulta” indica que o certificado usado na autenticação (SSL) da consulta é diferente do certificado usado na autenticação do envio.

**Solução**

Caso esteja com a rejeição 223 em seu ambiente e já foi configurado com o certificado digital válido no **Wizard Config** da rotina **SPEDNFE**, porém, permanece apresentando a rejeição 223 de maneira intermitente em seu ambiente, significa que no seu cenário está ocorrendo uma **concorrência de serviços do****TSS**, onde possui dois TSS 3.0 apontados para a mesma base de dados.  
   
**Exemplo**: Um TSS para **e-social(TAF)** e outro para **NF-e** apontados para mesma base de dados.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058443153/mceclip0.png)  
  
No cenário acima os dois serviços do TSS ficam procurando **pendencias** na tabela **TSSTR1**, **independente** do **modelo** do documento, com isso a transmissão pode ocorrer tanto pelo **TSS 1** (denominado e-social) ou **TSS 2**(denominado Nf-e), então para que não haja essa concorrência a TOTVS orienta não ter estruturas distintas

**Obs:** Estruturas do **TSS** distintas significa que há pastas estruturais diferentes, como: **Certs**, **APO(RPO)** ou **binário(appserver)**.  
   
Concluímos que para a **solução definitiva** do caso deverá utilizar **somente um TSS 3.0** para atender a sua demanda, com uma **estrutura separada** e com **banco de dados** separado **ou** utilizar somente um TSS para **todos os documentos eletrônicos**.  
   
**DICA:** Caso tenha dificuldades em descobrir onde está o segundo serviço pode ser identificado no **DBMONITOR** em “IP ORIGEM”, exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014600932/mceclip0.png)

Verifique pelos usuários, para o **TSS** sempre será denominado como “Totvs Service Gateway” e no comentário estará o **JOB** que está rodando e a entidade, no **IP Origem** ira demonstrar o Ip do servidor que está rodando o **TSS** e a porta do serviço.

Assim devera desativar o serviço do **TSS** que estiver rodando com o certificado digital vencido.
