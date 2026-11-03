---
article_id: 6303611346711
category: eSocial - Gerar XML/ Integração Evento
content_hash: a795bd727226e41a6150c96ab4017fb19b81771eeb960d776c668dbf9c1cc76d
fetched_at: '2026-06-28T22:47:12.262597+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro código 008 ao transmitir S-1200: Informações
  complementares de identificação do trabalhador deve ser preenchido'
type: support-article
updated_at: '2024-06-26T15:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6303611346711-RH-RM-FOP-eSocial-Erro-c%C3%B3digo-008-ao-transmitir-S-1200-Informa%C3%A7%C3%B5es-complementares-de-identifica%C3%A7%C3%A3o-do-trabalhador-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446213063447) Tempo aproximado para leitura: **00****:03:00 min****Ocorrência**Ao transmitir o evento S-1200 para o governo é retornado a inconsistência **Código do erro: 008 - Descrição:** **Grupo** [#39](https://totvssuporte.zendesk.com/agent/tickets/39)**;Informações complementares de identificação do trabalhador#39;deve ser preenchido. Verifique as condições de preenchimento no leiaute.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6804894056855)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando o trabalhador não possui cadastramento de vínculo no Governo e a *tag* **infoComplem** não é preenchida, sendo o preenchimento obrigatório neste caso, conforme previsto no leiaute 1.0

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6302807521815)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Confirme se o trabalhador não possui o S-2300 ou S-2200 no portal do eSocial;  
2. Localize na **F****ila de Eventos Não Periódicos** o evento S-2200 ou S-2300 para este trabalhador. Para melhor identificação, poderá aplicar o filtro da **Chapa** do funcionário e selecionar o **Tipo de Evento** desejado;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6303572454551)

3. Se não possuir no ambiente do Governo, mas existir o S-2200 ou S-2300 na Fila de Eventos, deverá [**excluí-lo**;](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017738251-RH-RM-FOP-eSocial-Exclus%C3%A3o-de-eventos-da-fila-independente-do-status?source=search)  
4. Depois gere o XML do S-1200 novamente e envie ao eSocial.
