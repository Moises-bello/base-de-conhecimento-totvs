---
article_id: 360053505014
category: NFe - Nota Fiscal Eletrônica
content_hash: e1eab3ef6a20c78babfe137b5444dffb5b7d8e6834de22b1e0bb608b6ce48ce6
fetched_at: '2026-06-28T22:40:00.343716+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Instrução Normativa
  SEFAZ Nº 54 DE 27/08/2020'
type: support-article
updated_at: '2021-10-11T17:02:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053505014--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Instru%C3%A7%C3%A3o-Normativa-SEFAZ-N%C2%BA-54-DE-27-08-2020
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da Instrução Normativa SEFAZ Nº 54 DE 27/08/2020 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A Sefaz do Ceará  **conforme o link abaixo:**

<https://www.legisweb.com.br/legislacao/?id=400743>

No qual, houve a divulgação **da Instrução Normativa SEFAZ Nº 54 DE 27/08/2020.**

Nesta **Instrução não foi alterada ou acrescentada** nenhuma validação da nota fiscal eletrônica, sendo assim **não será necessário** realizar manutenções em nossos fontes.

* **Referente ao Cancelamento de NFe:**

![image.png](https://mail.google.com/mail/u/0?ui=2&ik=b781bb0fef&attid=0.1&permmsgid=msg-a:r1224196588120816803&th=174924bbe78ee48d&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ-eUhY2VLXd8IuFamf5U5oHhP92ickQEcbdIPl10_uPfrR3CR0_dSAlsnfOvq47ivpcmFDqvWAow0Y9SIl9YUtxEI9KVYuZR12APKcN6qgel9asjmOZcBHTk0Y&disp=emb&realattid=ii_kf428u8z2)

* Cancelamento **até 24 horas.**

[MP - NFE - Qual o parâmetro que define a quantidade de horas para exclusão da nota fiscal eletrônica autorizada ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052702853-MP-NFE-Qual-o-par%C3%A2metro-que-define-a-quantidade-de-horas-para-exclus%C3%A3o-da-nota-fiscal-eletr%C3%B4nica-autorizada-?source=search)

* Cancelamento **extemporâneo até 720 horas.**

[MP - NFE - Cancelamento extemporâneo (Cancelamento fora do prazo)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020663032-MP-NFE-Cancelamento-extempor%C3%A2neo-Cancelamento-fora-do-prazo-?source=search)

[MP - NFE - Parâmetro MV\_INFXJUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026661472-MP-NFE-Par%C3%A2metro-MV-INFXJUS?source=search)

* Após esse prazo deve ser realizado o **estorno de cancelamento.**

[MP - NFE - Inclusão de Nota de Estorno e Estorno de Devolução](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020898192-MP-NFE-Inclus%C3%A3o-de-Nota-de-Estorno-e-Estorno-de-Devolu%C3%A7%C3%A3o?source=search)

* **Saiba mais:**

O estorno deve ser gerado **com os CFOPs abaixo:**

II - no campo CFOP o código **5949**para importação ou **1949** para exportação, conforme o caso;

Caso seja necessário alterar o **CFOP** altere pelo TES da nota no campo **Cod. Fiscal "F4\_CF":**

* No estorno é necessário **informar a mensagem abaixo:**

IV - a justificativa do estorno no campo destinado às informações adicionais de interesse do Fisco (campo infAdFisco), consignando a expressão:

a) para estorno de importação "Nota fiscal emitida para estorno da NF-e nº \_\_\_\_\_\_\_, a qual foi substituída pela NF-e nº \_\_\_\_\_\_\_\_, referente à DI nº \_\_\_\_\_\_\_\_. Dados do Exportador: \_\_\_\_\_\_\_\_\_\_\_\_\_\_."

b) para estorno de exportação "Nota fiscal emitida para estorno da NF-e nº \_\_\_\_\_\_\_, a qual foi substituída pela NF-e nº \_\_\_\_\_\_\_\_, referente à DDE nº \_\_\_\_\_\_\_\_. Dados do Destinatário no Exterior: \_\_\_\_\_\_\_\_\_\_\_\_\_\_."

[MP - NFE - Gerar mensagem em informações complementares do Danfe utilizando fórmula ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871-MP-NFE-Gerar-mensagem-em-informa%C3%A7%C3%B5es-complementares-do-Danfe-utilizando-f%C3%B3rmula-?source=search)

[MP - NFE - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773-MP-NFE-Como-gerar-informa%C3%A7%C3%B5es-na-TAG-infCpl-ou-infAdFisco-no-XML-e-no-DANFE?source=search)

* **Referente ao Manifesto de NFe:**

![image.png](https://mail.google.com/mail/u/0?ui=2&ik=b781bb0fef&attid=0.2&permmsgid=msg-a:r1224196588120816803&th=174924bbe78ee48d&view=fimg&sz=s0-l75-ft&attbid=ANGjdJ-3HCdpYxz2KT6QmX78pB7ynrWRoKZ3s40PkRBfT2vrW9U2NAnLiUyu91evjgQhciyjybs6heyaHwY2qOPQYlsFJiCJNqZrpeg59SoP1_pkL5Y-gpDzXz1_FnY&disp=emb&realattid=ii_kf42wlh54)

Os eventos que devem ser enviados são apenas de **Confirmação da Operação, Operação não realizada e Desconhecimento da operação.**

[MP - MDE -Sincronização pelo menu](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021041191--MP-MDE-Sincroniza%C3%A7%C3%A3o-pelo-menu?source=search)

[MP - MDE - Como incluir Manualmente notas na rotina SPEDMANIFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034457493-MP-MDE-Como-incluir-Manualmente-notas-na-rotina-SPEDMANIFE?source=search)

[MP - MDE - Sincronização Automática da MDe via Schedule](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018757651-MP-MDE-Sincroniza%C3%A7%C3%A3o-Autom%C3%A1tica-da-MDe-via-Schedule?source=search)

[MP - MDE - Como manifestar notas na rotina SPEDMANIFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033920194-MP-MDE-Como-manifestar-notas-na-rotina-SPEDMANIFE?source=search)
