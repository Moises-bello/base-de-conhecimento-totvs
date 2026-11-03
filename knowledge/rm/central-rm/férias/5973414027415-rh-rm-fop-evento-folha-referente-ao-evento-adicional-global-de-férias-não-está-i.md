---
article_id: 5973414027415
category: Férias
content_hash: 16a899f303d2d234b8b182d2e328ea90e088b0b4dded5380ddebaffb90e0b602
fetched_at: '2026-06-28T22:46:56.298385+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Evento Folha referente ao Evento Adicional Global de Férias
  não está informado
type: support-article
updated_at: '2025-02-27T17:50:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5973414027415-RH-RM-FOP-Evento-Folha-referente-ao-Evento-Adicional-Global-de-F%C3%A9rias-n%C3%A3o-est%C3%A1-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20717536839575) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao lançar férias ocorre a mensagem: Evento Folha referente ao Evento Adicional Global de Férias XXXX não está informado. Esta informação é obrigatória para o correto Lançamento das Férias do funcionário XXXX.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5973143267991)  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
A mensagem ocorre, pois o evento Folha não estar informado no cadastro do evento adicional global de férias inserido.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**01.** Acesse; **Configurações - Parametrizador - Férias - Eventos Adicionais Globais**  
**02.** Acesse o evento adicional informado na mensagem;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5973245472151)  
  
**03.** Informe o evento folha;

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5973297093527)

**Atenção:**

Para cada evento contido no campo "Evento de Recibo" que tiver código de cálculo ou fórmula, deverá ter um evento correspondente no campo "Evento Folha", sem código de cálculo e sem fórmula.

Na pasta de Eventos adicionais, há os seguintes campos:

**Evento do recibo:**

Selecione o evento para inclusão no recibo de férias.

**Evento da folha:**

Selecione um evento com as mesmas características do evento do recibo (incidências e, se houver, código de cálculo). Porém, caso o evento recibo tenha fórmula, o evento folha não poderá ter. Esta restrição é importante para garantir que o valor do evento no recibo de férias permaneça idêntico na folha, mesmo se ocorrer uma alteração salarial.
