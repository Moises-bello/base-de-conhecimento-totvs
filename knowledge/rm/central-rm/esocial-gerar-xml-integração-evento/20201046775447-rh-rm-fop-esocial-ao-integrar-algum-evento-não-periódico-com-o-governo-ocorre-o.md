---
article_id: 20201046775447
category: eSocial - Gerar XML/ Integração Evento
content_hash: d2ff345f64ac0c650be452286bca3a9f641581d990a009d57c93c058a5d6efe6
fetched_at: '2026-06-28T22:47:11.966516+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao integrar algum evento não periódico com o governo
  ocorre o erro 1257: A folha de pagamento do período XXXX-XX se encontra fechada.
  Ação sugerida: Será necessário reabrir a folha para continuar com o envio deste
  evento.'
type: support-article
updated_at: '2024-10-23T10:59:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20201046775447-RH-RM-FOP-eSocial-Ao-integrar-algum-evento-n%C3%A3o-peri%C3%B3dico-com-o-governo-ocorre-o-erro-1257-A-folha-de-pagamento-do-per%C3%ADodo-XXXX-XX-se-encontra-fechada-A%C3%A7%C3%A3o-sugerida-Ser%C3%A1-necess%C3%A1rio-reabrir-a-folha-para-continuar-com-o-envio-deste-evento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20201016199703) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao integrar algum evento não periódico com o governo ocorre o erro 1257: A folha de pagamento do período XXXX-XX se encontra fechada. Ação sugerida: Será necessário reabrir a folha para continuar com o envio deste evento.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20201016204567)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse erro normalmente vem acompanhado do erro 721. E ocorre ao enviar algum evento periódico ou não periódico ao governo, porém já consta no governo um evento de Fechamento - S-1299 com o mesmo período.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Identifique no erro qual é o período da folha que já se encontra fechada;

2. Gere o S-1298 de reabertura do período da folha informado no erro;

3. Reenvie o evento desejado.

**Saiba mais**  
Para mais informações acesse:

- [RH - RM - FOP - eSocial - Erro 721 - Não foi possível registrar o evento atual pois existe(m) evento(s) cadastrado(s) com data de ocorrência posterior para esse trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411984497559-RH-RM-FOP-eSocial-Erro-721-N%C3%A3o-foi-poss%C3%ADvel-registrar-o-evento-atual-pois-existe-m-evento-s-cadastrado-s-com-data-de-ocorr%C3%AAncia-posterior-para-esse-trabalhador);

- [RH - RM - FOP - eSocial - Como realizar a reabertura da folha de pagamento no eSocial utilizando o evento S-1298](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5676190571799?source=search) .
