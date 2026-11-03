---
article_id: 37153645709591
category: Financeiro - Conciliador Backoffice
content_hash: dba175adfafb55f7e04dd777bc1dfd487f6b6f26037a05b446adb899dbab05f7
fetched_at: '2026-06-28T22:37:47.281918+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - Financeiro - CTBA940 - Conciliador
  não demonstra baixas via API
type: support-article
updated_at: '2025-12-22T11:29:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37153645709591-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-CTBA940-Conciliador-n%C3%A3o-demonstra-baixas-via-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37153645695127) Tempo aproximado para leitura: **00:05:00 min**

##### **Dúvida** Por que as baixas realizadas via retorno de API bancária de pagamentos não são localizadas ou apresentadas no Conciliador Financeiro?

##### **Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210

#### **Solução**

O Conciliador (CTBA940) tem como premissa básica a existência de registros na tabela **FK5** (Movimentação Bancária). Quando uma baixa é realizada (seja via API, CNAB ou Manual), o sistema verifica o **Motivo/Tipo de Baixa** utilizado para determinar se haverá atualização de saldo bancário.

No contas a pagar, se for utilizado o motivo de baixa **"NOR" (Normal)**, o sistema, por padrão, **não altera saldo bancário** e, consequentemente, não gera registros na tabela **FK5**. Sem o registro nesta tabela, o Conciliador não possui dados para processar a movimentação.

Para que a movimentação seja refletida no Conciliador, deve-se utilizar um motivo de baixa que movimente banco (Ex: **DEB - Débito em Conta Corrente**).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37153645696535)

1. Verifique o cadastro do retorno, para validar qual campo esta retornando no padrão **Motivos de Baixa**
2. Certifique-se de que o motivo utilizado na configuração do retorno (API) esteja configurado para **Movimentar Banco = Sim, esta ação pode ser validada através da FINA490.**
3. Caso o título já tenha sido baixado com o motivo "NOR":

   * Realize o cancelamento da baixa do título;
   * Efetue a baixa novamente utilizando um motivo que movimente conta corrente (Ex: Débito CC);
4. Verifique se o registro foi gerado corretamente na tabela **FK5**;
5. Acesse o **Conciliador (CTBA940)** e utilize o processo adequado:

   * **Processo 0024 (Conciliação Manual):** Utiliza a FK5 como base e gera os dados na SIG durante a conciliação. Recomendado para este cenário onde não houve integração prévia de extrato.
   * **Processo 0023 (Conciliação Automática):** Compara o extrato bancário (previamente populado na SIG) com os dados da FK5.
