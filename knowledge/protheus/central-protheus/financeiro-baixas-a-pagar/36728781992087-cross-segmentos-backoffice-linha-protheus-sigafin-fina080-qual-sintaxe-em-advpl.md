---
article_id: 36728781992087
category: Financeiro - Baixas a Pagar
content_hash: 22d5057c986c5adaac71ed419b95de9c312eadc388fd460756ddfacaef174058
fetched_at: '2026-06-28T22:37:24.893944+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA080 - Qual sintaxe
  em ADVPL deve ser utilizado na contabilização online do LP 530 e 531
type: support-article
updated_at: '2026-03-25T20:29:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36728781992087-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Qual-sintaxe-em-ADVPL-deve-ser-utilizado-na-contabiliza%C3%A7%C3%A3o-online-do-LP-530-e-531
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36728755492503) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
FINA080 - Qual sintaxe em ADVPL deve ser utilizada na contabilização online do LP 530 e 531.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Protheus Financeiro - Todas as versões  
  
**Causa**  
Não contabilização correta do lançamento padrão 530 Baixas a pagar, e lançamento padrão 531 Estorno/Cancelamento de baixas a pagar.  
  
**Solução:**

O ideal é criar expressões em ADVPL utilizando as tabelas **SE5, FK5, FK2** ou **variáveis**.  
Caso a expressão seja posicionada em outra tabela, isso poderá causar falhas e impedir a contabilização, pois outras tabelas podem estar em processo de gravação e não conter os dados necessários durante o processo de validação da sintaxe criada pela empresa e gerar a não contabilização.

Segue algumas documentações que referenciam essa sugestão de posicionamento nas tabelas **SE5, FK5, FK2** ou **variáveis**.

**1)** "LP 532 - Baixas de Títulos por Borderô de Pagamento" tem quase o mesmo comportamento do "LP 530 - Baixa de Títulos a Pagar  
[532 Baixas de Títulos por Bordero de Pagamento](https://tdn.totvs.com/display/public/PROT/532+Baixas+de+Titulos+por+Bordero+de+Pagamento#Exemplo-1)

É informado na documentação a sugestão de posicionamento em variáveis como VALOR, VALOR2 etc.

E no campo SE5->E5\_VALOR

**2)**Na documentação sobre a nova estrutura das tabelas FKs, que são várias tabelas que correspondem a tabela "SE5 de baixas de títulos".

Nessa documentação é indicado posicionar o lançamento padrão 530 na tabela FK2, utilização de sintaxe FK2->FK2\_VALOR e das variáveis como exemplo MULTA1, JUROS1 etc.

Logo o estorno terá que ser feito no processo inverso no LP 531, tendo que posicionar nos mesmos campos e variáveis.

[Contabilização da nova estrutura de gravação do processo de movimento bancário e baixas.](https://tdn.totvs.com/pages/releaseview.action?pageId=184779769)

**3)** Documentação "LP 531 - Exclusão/Estorno de Baixa a pagar" informa que:  
[DSERFINP-896 Contabil on-line lp 531 cancel baixa cp](https://tdn.totvs.com/display/public/PROT/DSERFINP-896+Contabil+on-line+lp+531+cancel+baixa+cp)

"*Devido a possibilidade de ocorrer baixas parciais, a contabilização do LP: 531 cancelamentos de baixa a pagar  não pode ser configurado pelo campo:*  
***E2\_VALLIQ** . Para contabilização do LP, deverá ser usada a variável **VALOR***"

**4)**Documentação sobre "Borderô de Impostos (FINA241 - SIGAFIN)" que utiliza o lançamento padrão 530 e 531 para realizar a baixa e cancelamento de baixas a pagar, sugere a utilização na tabela SE5 ou FK2  
[Borderô de Impostos (FINA241 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312165366)

LP 530  sugere IIF(SE5->E5\_MOTBX='PCC',SE5->E5\_VALOR,0)

LP 531 sugere IIF(SE5->E5\_MOTBX='PCC',SE5->E5\_VALOR,0)

ou  
LP 531 sugere também IIF(FK2->FK2\_MOTBX="PCC",FK2->FK2\_VALOR,0)

E existe uma observação

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/36728781971479)](https://centraldeatendimento.totvs.com/hc/article_attachments/36728781971479)

**5) Documentação** sugere a contabilização do LP 530 utilizando as tabelas SE5 e FK´s  
[TUUTSE\_DT\_AJUSTE\_FINA290\_CONTAB\_LPS\_587\_530](https://tdn.totvs.com/display/public/PROT/TUUTSE_DT_AJUSTE_FINA290_CONTAB_LPS_587_530)

"*Alterada a rotina FINA290 observando a nova estrutura de tabelas FKs relacionadas à tabela SE5..*"
