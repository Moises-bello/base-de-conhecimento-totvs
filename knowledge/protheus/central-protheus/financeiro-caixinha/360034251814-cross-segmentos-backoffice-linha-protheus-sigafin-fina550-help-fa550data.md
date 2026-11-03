---
article_id: 360034251814
category: Financeiro - Caixinha
content_hash: 1034204deffef8f896354127a57ab41107174bf7e44b184322b973aa8b060370
fetched_at: '2026-06-28T22:37:53.906887+00:00'
product: protheus
section_id: 1500001550702
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA550 - HELP: FA550DATA
type: support-article
updated_at: '2022-06-21T01:40:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034251814-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA550-HELP-FA550DATA
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Ao tentar fazer a reposição do caixinha (com data retroativa) apresenta a mensagem HELP: FA550DATA.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044784394/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA550 - Todas as versões

**Causa**Este help é apresentado ao efetuar uma movimentação em um determinado caixinha, uma reposição com data base anterior a última movimentação.**Exemplo:**  
Efetuar uma movimentação de **Despesa** com data (23/04/2019), efetuar a reposição com data base 23/04/2019 será feito com sucesso. Ao logar na rotina **Manutenção**(**FINA550**) com data base 22/04/2019 (1 dia antes da última movimentação) e tentar repor será apresentado o help: **FA550DATA**. 

**Solução**Faça a reposição em data igual ou posterior de seu último comprovante. Não é possível efetuar a reposição do caixinha com movimentações em datas posteriores ao da reposição.

**Importante*****:*** Esse processo é legado do sistema e não será alterado.
