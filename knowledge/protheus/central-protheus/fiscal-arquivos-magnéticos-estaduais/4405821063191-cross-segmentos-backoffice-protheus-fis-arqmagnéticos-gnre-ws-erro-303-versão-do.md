---
article_id: 4405821063191
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: c6c7c9b373220e83b43cf2f33abf12ccc7151c5f08e2f4cf2fc1e7315f460583
fetched_at: '2026-06-28T22:42:11.697518+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - ERRO
  303 - VERSÃO DOS DADOS NÃO SUPORTADA '
type: support-article
updated_at: '2022-08-17T19:31:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405821063191-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-ERRO-303-VERS%C3%83O-DOS-DADOS-N%C3%83O-SUPORTADA
---

**Dúvida****GNRE WS** - Como corrigir o **erro 303- VERSÃO DOS DADOS NÃO SUPORTADA** na transmissão da **GNREWS.**  
**Ambiente**Cross Segmento - Backoffice (**Linha Protheus**) - Livros Fiscais - A partir da versão 12.1.25.  
  
**Causa**Esse incidente ocorre, pois seu TSS precisa de atualização devido a mudança de versão da **GNREWS** para **2.0** a partir de 04/08/2021; a versão 1.0 da GNRE não será mais aceita após essa data conforme aviso da Sefaz.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406101950743/mceclip0.png)  
  
**Solução**Para solucionar essa ocorrência, deve realizar a transmissão da GNRE somente na versão 2.00

Clique em Ambiente >> altere a versão para 2.00

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4406110208407/mceclip1.png)

A correção já se encontra no RPO do TSS, basta substituir o arquivo conforme a sua versão:   
  
**OBS:** Para realizar a atualização do repositório do TSS**,** faça o *download* em um dos *links* abaixo de acordo com sua release:

**TSS:**

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search>

Atualize a sua pasta Schemas do TSS conforme abaixo:

[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS?source=search)

**URLs**  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025394911-TSS-Atualiza%C3%A7%C3%A3o-das-URLs-do-TSS?source=search>

**Binário**:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062416694-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Appserver-bin%C3%A1rio-do-TSS?source=search>

Após atualizações retransmita a GNRE , caso ocorra a mesma rejeição abra um chamado com o suporte técnico.
