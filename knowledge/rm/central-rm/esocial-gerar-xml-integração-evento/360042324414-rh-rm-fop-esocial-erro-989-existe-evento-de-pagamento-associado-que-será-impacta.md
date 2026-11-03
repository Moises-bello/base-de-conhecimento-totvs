---
article_id: 360042324414
category: eSocial - Gerar XML/ Integração Evento
content_hash: 4c5116e2b3e0e21aea311fbcf9307c87d2e34f8574bbc7aa03a08e0f01919227
fetched_at: '2026-06-28T22:47:12.180022+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 989: Existe evento de pagamento associado que
  será impactado pelo evento retificador'
type: support-article
updated_at: '2026-05-27T20:32:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042324414-RH-RM-FOP-eSocial-Erro-989-Existe-evento-de-pagamento-associado-que-ser%C3%A1-impactado-pelo-evento-retificador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23077918562711)Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Ao transmitir a retificação ou exclusão extemporânea de evento remuneratório **S-1200**, **S-1202**, **S-1207**, **S-2299** ou **S-2399** ocorre o erro de código **989** com o seguinte aviso:**Não é possível retificar o evento. Existe evento de pagamento associado que será impactado pelo evento retificador**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial  - Todas as versões  
  
**Causa**  
Este incidente ocorre quando é realizado o envio de um evento remuneratório (**S-1200**, **S-1202**, **S-1207**, **S-2299** ou **S-2399**) que irá alterar o valor líquido porém, existe um evento **S-1210**aceito pelo RET que será impactado com a retificação.  
  
**Solução**  
Para o correto envio realize os passos abaixo:  
1. Acesse **Folha de Pagamento | eSocial | Eventos Periódicos** selecione o evento **S-1210** aceito pelo RET, gere sua exclusão em **Processos | Gerar Evento de Exclusão S-3000** e realize o envio do evento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21079942001687)

2. Envie a retificação que inicialmente foi rejeitada;  
3. Após a retificação ser aceita pelo RET, gere e transmita um novo **S-1210**.  
  
**Saiba Mais**  
Para mais informações acesse:   
- [Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RM-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos?source=search)
