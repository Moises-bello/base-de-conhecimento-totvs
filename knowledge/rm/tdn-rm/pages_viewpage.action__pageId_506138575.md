---
content_hash: 9ca352589daac5601ed9028a1b06ad41dfc0c31ce8b8dcd81fc4693cf9eca124
fetched_at: '2026-06-29T00:10:25.841778+00:00'
page_id: '506138575'
product: rm
source: tdn-rm
title: Transferência Manual da Fila de Eventos do eSocial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=506138575
version: 14
---

A rotina realiza a transferência dos registros da Fila de Eventos do eSocial (PESOCIALEVENTOS) para a **Fila de Eventos do eSocial Complementar** (PESOCIALEVENTOSCOMPL) de acordo com o parâmetro "Meses a manter na Fila de Eventos", localizado em Parametrizador | eSocial | Configurações Gerais 1/7. Esse parâmetro determina o período de permanência dos registros na tabela PESOCIALEVENTOS.

**ATENÇÃO:**

1) O processo verifica o campo **"Data do Evento"** (DATAEVENTO) para realizar a transferência.

2) Para restaurar os dados transferidos deverá executar [Restauração da Fila de Eventos do eSocial](http://tdn.totvs.com/pages/viewpage.action?pageId=506143901).

3) Caso não execute o processo de transferência manual, o sistema irá fazer a transferência na [Liberação de Competência](http://tdn.totvs.com.br/pages/releaseview.action?pageId=452719172).
