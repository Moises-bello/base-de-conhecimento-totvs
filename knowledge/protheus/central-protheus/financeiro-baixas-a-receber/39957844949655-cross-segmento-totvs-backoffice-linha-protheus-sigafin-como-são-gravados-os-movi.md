---
article_id: 39957844949655
category: Financeiro - Baixas a Receber
content_hash: e329afe8dbf659f253fbe5d0b68c5d66989f238856af0ad2291990576a01ab9b
fetched_at: '2026-06-28T22:37:43.834564+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Como são gravados
  os movimentos de baixa com valores acessórios?
type: support-article
updated_at: '2026-04-23T16:47:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39957844949655-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Como-s%C3%A3o-gravados-os-movimentos-de-baixa-com-valores-acess%C3%B3rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39957844931607) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
Ao realizar a baixa de um título a receber com valor acessório (como desconto ou abatimento), por que o sistema gera duas movimentações na tabela SE5 — uma com o valor líquido e outra com o valor acessório negativo.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Releases

**Solução:**  
O comportamento apresentado é o esperado e faz parte do padrão do sistema, sendo adotado para garantir a rastreabilidade contábil e a consistência do saldo bancário.

No momento da baixa, caso seja selecionado um tipo de baixa com movimentação de saldo bancário, o sistema desmembra a operação em duas movimentações distintas na tabela **SE5** (Movimentação Bancária):

* **Movimentação Bancária (Valor Líquido):**  
  Representa o valor que efetivamente transitou na conta bancária.  
  Exemplo: para um título de **R$ 100,00** com desconto de R$ 2,00, a movimentação será de R$ 98,00  **E5\_TIPODOC = 'VL'** — valor que reflete o extrato bancário (tabela **SE8**).
* **Movimentação de Valor Acessório (Tipo VA):**  
  Registra o valor do desconto ou abatimento (ex: -R$ 2,00).  
  Essa movimentação possui o campo **E5\_TIPODOC = 'VA****'** e tem finalidade exclusivamente contábil e histórica, não representando uma movimentação financeira real.

Embora ambas as linhas sejam exibidas na rotina de extrato bancário (**FINA100**), o sistema não considera o valor acessório (VA) para efeito de saldo bancário. Isso ocorre porque ele identifica que esse registro não corresponde a uma entrada ou saída efetiva de recursos, mas sim a um ajuste de composição do título.

Isso também indica que somente a movimentação bancária irá popular a **FK5**.

![image.png](https://totvssuporte.zendesk.com/attachments/token/ujdey3B5XdJPLG8QXVRHmbB2L/?name=image.png&lotus_request=true)

Esse modelo permite:

* Manter o detalhamento do valor original do título;
* Evidenciar os abatimentos/descontos aplicados;
* Garantir que o saldo bancário reflita apenas o valor efetivamente movimentado.
