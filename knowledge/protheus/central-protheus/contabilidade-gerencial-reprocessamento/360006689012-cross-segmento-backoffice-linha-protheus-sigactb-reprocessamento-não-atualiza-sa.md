---
article_id: 360006689012
category: Contabilidade Gerencial - Reprocessamento
content_hash: a86a6f8d4527625bc50a03987535960c7945c7c03c0619f9212a25b3d873f285
fetched_at: '2026-06-28T22:40:41.999806+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Reprocessamento não
  atualiza saldos
type: support-article
updated_at: '2022-05-31T14:00:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689012-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Reprocessamento-n%C3%A3o-atualiza-saldos
---

**Dúvida**Reprocessamento não atualiza saldos

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 12.1.17

**Solução**Realize os seguintes passos:

1. Verificar se o ambiente esta atualizado, conforme último pacote disponibilizado no portal do       cliente

2. Verifique se as procedures estão instaladas:

* P12\_01
* P12\_02
* P12\_03
* P12\_06
* P12\_23

3. Verificar como está preenchido o campo CT2\_FILIAL, compare com o campo CQx\_FILIAL (CQ0, CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ7, CQ8 E CQ9) o conteúdo dos campos deve ser igual

4. Verifique se o compartilhamento das tabelas CT2, CQ0, CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ7, CQ8 E CQ9 estão iguais, pois devem estar.

5. Após conferir as informações e ajustar o que for preciso (se algo não estiver em conformidade com os tópicos acima).  
  
6. Fazer backup e limpar as tabelas CQ0, CQ1, CQ2, CQ3, CQ4, CQ5, CQ6, CQ7, CQ8 E CQ9 (Não limpar a CT2)  
  
7. Será necessário efetuar o Reprocessamento de saldos (CTBA190) a partir do primeiro movimento, para todo o período contábil existente na rotina de Lançamentos Contábeis Automáticos (CTBA102 – tabela CT2).  
  
8. Considerar tanto as moedas utilizadas nos lançamentos contábeis quanto o tipo de saldo.

Validar o procedimento em ambiente teste.

**Veja mais**

* [Como realizar o reprocessamento de saldos no SIGACTB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-CTB-SIGACTB-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB-)
* [MP - SIGACTB - Saldos não estão sendo atualizados de forma online.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019534772-MP-SIGACTB-Saldos-n%C3%A3o-est%C3%A3o-sendo-atualizados-de-forma-online-?source=search)
* [MP - SIGACTB - CTBA190 Saldos não são atualizados com Stored Procedure](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021997171-MP-SIGACTB-CTBA190-Saldos-n%C3%A3o-s%C3%A3o-atualizados-com-Stored-Procedure?source=search)
