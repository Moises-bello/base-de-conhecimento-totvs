---
article_id: 360052463293
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 0c1bda5e72d132159057818fa6a57123b35e23eeafe657b388d85732ad21436f
fetched_at: '2026-06-28T22:45:20.913573+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Atualização - Como realizar a atualização
  do SmartClient
type: support-article
updated_at: '2026-06-26T12:14:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052463293-RH-Linha-Protheus-TAF-eSocial-Atualiza%C3%A7%C3%A3o-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-SmartClient
---

**Dúvida**

Como atualizar o SmartClient?

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Atualização do SmartClient -

Todas as versões.

**Solução**

1- Verifique a sua release e realize o download do **smartclient:**

2 - Para verificar a release, basta acessar o TAF e acessar a tela de diagnósticos:

**Release: 12.1.33 e 12.1.2210:**

* **Windows**:
  + Arquitetura (32 bits):
    - <https://suporte.totvs.com/portal/p/10098/download#detail/1112222>
  + Arquitetura (64 bits):
    - <https://suporte.totvs.com/portal/p/10098/download#detail/1112221>
* **Linux**:
  + <https://suporte.totvs.com/portal/p/10098/download#detail/1112223>
* **Mac**:
  + <https://suporte.totvs.com/portal/p/10098/download#detail/1112224>

**Obs.:** Após extrair os arquivos após o donwload, substituir na pasta smartclient dentro da pasta bin/smartclient.

3 - Em alguns casos ao acessar o atalho do TAF, é exibido a mensagem abaixo para atualizar conforme imagem:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083165853)

4 - Acesse o arquivo "**appserver.ini**" da pasta "**appserver**" e comente a seção [UPDATE] colocando o ponto e vírgula antes do colchete de abertura:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083165873)

5 - Replique a pasta SmartClient para outras estações de trabalho:

[TAF - CONFIGURAÇÃO - Replicando o SmartClient do servidor para outras estações de trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043647533-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Replicando-o-SmartClient-do-servidor-para-outras-esta%C3%A7%C3%B5es-de-trabalho)
