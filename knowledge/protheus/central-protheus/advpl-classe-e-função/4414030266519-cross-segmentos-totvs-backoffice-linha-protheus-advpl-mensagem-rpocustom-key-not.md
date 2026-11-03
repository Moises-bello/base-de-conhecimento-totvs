---
article_id: 4414030266519
category: ADVPL - Classe e Função
content_hash: 1c4f10f51611099945dafd254389f95ae1a53ed2cb357411647b0960cf9869b2
fetched_at: '2026-06-28T22:40:19.373078+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Mensagem RpoCustom
  Key Not defined in the ini file
type: support-article
updated_at: '2021-11-24T14:01:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414030266519-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-Mensagem-RpoCustom-Key-Not-defined-in-the-ini-file
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao iniciar o Server, o sistema apresenta a mensagem "RpoCustom Key Not defined in the ini file. Using Defaul set to..."

![Customrpo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4414030202903/Customrpo.jpg)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - A partir da versão 12.1.33  
  
**Causa**A partir da versão 12.1.33 o Protheus possui um Repositório exclusivo para os fontes customizados, sempre que compilado um fonte de usuário, o sistema adiciona o mesmo ao RpoCustom.

Este arquivo "Custom.rpo" pode ser inserido em qualquer pasta do sistema, desde que indicado o caminho da pasta no AppServer.ini.

Caso não seja indicado o caminho da pasta no AppServer.ini, o sistema irá gerar essa mensagem e criará o arquivo na pasta do AppServer.  
  
**Solução**Insira o caminho da pasta onde será criado o "Custom.rpo" no AppServer.ini conforme exemplo abaixo:

![rpocustom...jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/4414044064151/rpocustom...jpg)

**Saiba mais**: [**RpoCustom**](https://tdn.totvs.com/x/YElwJQ)
