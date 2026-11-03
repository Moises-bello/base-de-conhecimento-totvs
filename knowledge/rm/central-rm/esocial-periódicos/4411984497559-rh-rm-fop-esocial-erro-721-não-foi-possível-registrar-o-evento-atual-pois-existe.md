---
article_id: 4411984497559
category: esocial - Periódicos
content_hash: efc7adaa11e7cc60c6abbcace82f7fe4daacf800ce644341a5b8f6fdbdc7654a
fetched_at: '2026-06-28T22:47:09.287305+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Erro 721 - Não foi possível registrar o evento atual
  pois existe(m) evento(s) cadastrado(s) com data de ocorrência posterior para esse
  trabalhador
type: support-article
updated_at: '2024-05-07T12:01:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411984497559-RH-RM-FOP-eSocial-Erro-721-N%C3%A3o-foi-poss%C3%ADvel-registrar-o-evento-atual-pois-existe-m-evento-s-cadastrado-s-com-data-de-ocorr%C3%AAncia-posterior-para-esse-trabalhador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15449105761431) Tempo aproximado para leitura: **00:02:30 min****Dúvida**Ao gerar o XML do S-2230 e/ou S-2299 é apresentado erro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23308674624407)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões

**Causa**O erro ocorre quando o governo identifica que já existe(m) evento(s) cadastrado(s) com data posterior aos eventos S-2230/ S-2299 que estão sendo enviados.

**Solução**Para solucionar o erro, realize os seguintes passos:  
1. Acessar o ambiente do governo **eSocialWeb** na aba de **Movimentações Trabalhistas** e analisar quais eventos foram enviado com data posterior ao S-2230/ S-2299 que está sendo enviado;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411989813143)

2. Realizar a exclusão,  através do evento [S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos), de todos os eventos com data posterior ao evento que se pretende enviar; verificar se existe algum evento de alteração (**S-2206** ou **S-2205**) com **data igual** ou **posterior** a **demissão** do funcionário;

3. Fazer o registro do evento conforme pretendido, com a data anterior a demissão do funcionário e/ou afastamento;

4. Enviar novamente em ordem cronológica, caso necessário, os eventos excluídos ou seja S-2205, S-2206, S-2230 e depois o S-2299 ou o evento que necessita ser integrado.
