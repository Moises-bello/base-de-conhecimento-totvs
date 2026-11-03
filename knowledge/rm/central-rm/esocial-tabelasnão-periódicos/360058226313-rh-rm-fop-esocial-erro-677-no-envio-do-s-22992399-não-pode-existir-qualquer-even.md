---
article_id: 360058226313
category: eSocial - Tabelas/Não Periódicos
content_hash: 2f48b34f4602e1c13d9e64637212d183296a7efad743129b3a412b1ace8ed3c8
fetched_at: '2026-06-28T22:47:10.336951+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 677 no envio do S-2299/2399: Não pode existir
  qualquer evento para o vínculo trabalhista com data posterior a data do desligamento'
type: support-article
updated_at: '2024-12-30T15:27:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058226313-RH-RM-FOP-eSocial-Erro-677-no-envio-do-S-2299-2399-N%C3%A3o-pode-existir-qualquer-evento-para-o-v%C3%ADnculo-trabalhista-com-data-posterior-a-data-do-desligamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24454908117911)**Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao transmitir **S-2299/S-2399** ocorre o erro **677** com descrição **Não pode existir qualquer evento para o vínculo trabalhista com data posterior a data do desligamento**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24455693767447)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este incidente ocorre quando há eventos já Aceito RET, cuja a data de inclusão/alteração é posterior a data de desligamento do funcionário.

**Solução**Para solucionar este incidente siga os passos abaixo:  
**1**. Acesse **Folha de Pagamento | eSocial | Fila de Eventos** filtre o evento **S-2299/S-2399** com erro, edite o gatilho e localize a tag **dtDeslig**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24455725429783)

2. Acesse o portal do governo e identifique em **Empregados** **|****Gestão de Empregados | Movimentações Trabalhistas**se há algum evento com data posterior à rescisão;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24455725436439)

3. Para que o governo aceite o evento da rescisão, não poderá existir evento com data posterior a esta data, sendo necessário enviar o S-3000 dos eventos com data posterior. Para isso identifique o evento na fila e envie o **[S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos)** do mesmo;  
4. Caso seja necessário, após enviar a exclusão do evento identificado no passo 3, inclua-o novamente na fila de eventos com a data de inclusão/alteração anterior à demissão;

5. Envie o evento **S-2299/S-2399**.
