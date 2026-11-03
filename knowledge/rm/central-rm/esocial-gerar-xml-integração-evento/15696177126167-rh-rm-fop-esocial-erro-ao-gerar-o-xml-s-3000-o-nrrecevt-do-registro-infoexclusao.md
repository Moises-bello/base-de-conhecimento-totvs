---
article_id: 15696177126167
category: eSocial - Gerar XML/ Integração Evento
content_hash: 2c4124d5648d6742cc5e3f4359749ae3035a158804a933751c59500afc2ea753
fetched_at: '2026-06-28T22:47:12.194519+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar o XML S-3000: O nrRecEvt do registro
  infoExclusao é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-06-05T11:45:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15696177126167-RH-RM-FOP-eSocial-Erro-ao-gerar-o-XML-S-3000-O-nrRecEvt-do-registro-infoExclusao-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15696203447575) Tempo aproximado para leitura: **00****:02:00 min****Ocorrência**Ao gerar o XML S-3000 ocorre o erro: **O nrRecEvt do registro infoExclusao é obrigatório e não está preenchido.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15694931835031)**

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este incidente ocorre quando o XML que está tentando excluir não consta com o número do recibo preenchido, quando o processo de exclusão está sendo realizado incorretamente, ou quando o evento que está tentando excluir já consta com o *Status* 11-Excluído RET ou foi retificado. Assim, ao gerar o XML S-3000 a *tag* nrRecEvt não é preenchida, cujo preenchimento é obrigatório em caso de exclusão do evento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15695253219479)

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique se o processo de exclusão através do evento S-3000 foi realizado corretamente ([CLIQUE AQUI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos));  
2. Verifique se o evento que deseja excluir consta na fila de eventos com o Número do Recibo**.** Caso o **Recibo** não esteja preenchido, será necessário realizar o preenchimento para depois gerar o S-3000.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15695449051671)

3. Verifique se o evento que está tentando excluir consta na fila com o status **11 - Excluído RET ou foi retificado.**

3.1. Caso conste como 11- Excluído RET, significa que o evento que está tentando excluir já não consta mais no portal do governo;

3.2. Caso o evento já tenha sido retificado, será necessário encaminhar o S-3000 de exclusão do evento de retificação.
