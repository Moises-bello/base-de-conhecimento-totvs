---
article_id: 9215898695063
category: eSocial - Gerar XML/ Integração Evento
content_hash: f293c5785b19c814d0106b14972be8b5886cce02d0e24baf1147f1e15c1c2144
fetched_at: '2026-06-28T22:47:12.186931+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao enviar retificação do evento S-2299: Evento
  de Exclusão ou Retificação deverá ser do mesmo tipo e se referir ao mesmo objeto
  do evento a ser excluído/retificado.'
type: support-article
updated_at: '2025-12-29T14:31:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9215898695063-RH-RM-FOP-eSocial-Erro-ao-enviar-retifica%C3%A7%C3%A3o-do-evento-S-2299-Evento-de-Exclus%C3%A3o-ou-Retifica%C3%A7%C3%A3o-dever%C3%A1-ser-do-mesmo-tipo-e-se-referir-ao-mesmo-objeto-do-evento-a-ser-exclu%C3%ADdo-retificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22743021544215) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao transmitir o evento de retificação S-2299, o governo retorna a mensagem de erro: **Código da Ocorrência: 157 - Descrição : Evento de Exclusão ou Retificação deverá ser do mesmo tipo e se referir ao mesmo objeto do evento a ser excluído/retificado. - Localização : /eSocial/evtDeslig/ideEvento**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse incidente ocorre, quando é enviado uma **retificação** do S-2299 com data de desligamento diferente da data enviada no S-2299 de **inclusão**.

**Solução**  
De acordo com o Manual de Orientações do eSocial, quando for necessário alterar a data de desligamento do funcionário (dtDeslig), é necessário enviar a **exclusão** do evento original através do S-3000 e enviar um novo S-2299 de inclusão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9215579094935)

**Saiba mais**  
Para mais informações acesse:

* [Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos)
* [MOS esocial (manual de orientação)](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/mos-s-1-3-consolidada-ate-a-no-s-1-3-06-2025.pdf)
