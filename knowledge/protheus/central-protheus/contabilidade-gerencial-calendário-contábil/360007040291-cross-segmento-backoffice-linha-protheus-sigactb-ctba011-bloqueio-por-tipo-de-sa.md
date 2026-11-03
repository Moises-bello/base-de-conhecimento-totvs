---
article_id: 360007040291
category: Contabilidade Gerencial - Calendário Contábil
content_hash: cca5b4a69739066179fb822a58c0eab2e8466291081f50e1fa33c34d58df3a76
fetched_at: '2026-06-28T22:41:03.406387+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA011: Bloqueio por
  tipo de saldos não funciona'
type: support-article
updated_at: '2022-07-18T19:39:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007040291-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA011-Bloqueio-por-tipo-de-saldos-n%C3%A3o-funciona
---

**Ocorrência:**Após efetuar o bloqueio de calendário contábil através do tipo de saldo, na inclusão/alteração/exclusão de lançamentos, o bloqueio não é validado no sistema.  
  
**Ambiente:**

#### Cross Segmento - Backoffice Linha Protheus - SIGACTB - Versões 11 e 12 **Causa:** Falha na parametrização do sistema. **Solução:**Para que seja corrigida a inconsistência, é necessário avaliar o conteúdo dos parâmetros MV\_CTBCACH e MV\_CTBCTG, onde: -MV\_CTBCACH: Quando este parâmetro está igual a "1", e o ambiente é acessado utilizando o SIGAMDI, é necessário que feche a rotina de lançamentos contábeis e acesse-a novamente. Caso preferir, configure-o com "0", para que os dados de configuração não fiquem gravados em cache. -MV\_CTBCTG: Para que o processo de bloqueio seja validado, é necessário que este parâmetro esteja igual a ".T.".
