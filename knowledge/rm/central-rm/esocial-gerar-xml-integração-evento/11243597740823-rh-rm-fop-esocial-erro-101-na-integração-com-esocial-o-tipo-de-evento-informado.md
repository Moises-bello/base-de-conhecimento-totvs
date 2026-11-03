---
article_id: 11243597740823
category: eSocial - Gerar XML/ Integração Evento
content_hash: fd76e976599ac92008e2e88299ccbb08a7856c17c1d95b1bae0efadcf4c771cd
fetched_at: '2026-06-28T22:47:12.082118+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro 101 na integração com eSocial - O tipo de evento
  informado não é aceito para este tipo de lote/serviço
type: support-article
updated_at: '2024-06-27T19:30:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11243597740823-RH-RM-FOP-eSocial-Erro-101-na-integra%C3%A7%C3%A3o-com-eSocial-O-tipo-de-evento-informado-n%C3%A3o-%C3%A9-aceito-para-este-tipo-de-lote-servi%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**  
Ao transmitir um eventos para o eSocial, é apresentado a mensagem **Código de Ocorrência 101 - O tipo de evento informado não é aceito para este tipo de lote/serviço.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
Esse incidente ocorre devido a uma falha de conexão com o TSS ao comunicar-se com o ambiente do Governo RET.  
  
**Solução**Para solucionar este erro, siga os passos abaixo:  
Para realizar a atualização do ID do evento, será necessário regerar os eventos e enviá-los ao eSocial novamente.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11270742406295)

**Observação**  
Se o erro persistir, poderá criar um novo evento XML para que o sistema gere uma nova identificação(ID) para ser enviado ao eSocial.
