---
article_id: 1500007690322
category: Financeiro - Contas a Pagar
content_hash: 77cc0e4bb68b86df378810233741b5b1a77fcfa0bb9dcce915b670b074e3c94b
fetched_at: '2026-06-28T22:38:08.261980+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA080 - Regras baixar  PA
type: support-article
updated_at: '2022-03-31T00:28:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007690322-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA080-Regras-baixar-PA
---

**Dúvida**Quais a situações onde a PA pode ser baixado, para que não ocorra a mensagem "Não é possível realizar a baixa de pagamento antecipado sem movimentação bancária"

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Ocorrência**Ao tentar realizar uma baixa a pagar de título PA (pagamento adiantado) é apresentada a mensagem "Não é possível realizar a baixa de pagamento antecipado sem movimentação bancária"

**Solução**

A baixa de títulos do tipo PA será permitida nas seguintes situações:

1. Na inclusão do PA a pergunta "**Gera Chq. p/ Adiant.**" estava igual a **SIM**e **"Mov. Banc. sem Cheque?"** igual a **NÃO**, sendo que o cheque já foi gerado e liberado (nº do cheque informado no momento da inclusão do PA ou gerado através da rotina Geração de Cheques-FINA190);  
   1. Será gerada movimentação bancária a receber (E5\_RECPAG = R), representando uma devolução do adiantamento feita ao fornecedor;
2. Na inclusão do PA a pergunta "**Gera Chq. p/ Adiant.**" estava igual a **NÃO**e **"Mov. Banc. sem Cheque?"** igual a **SIM**;
   1. Será gerada movimentação bancária a receber (E5\_RECPAG = R), representando uma devolução do adiantamento feita ao fornecedor;
3. Na inclusão do PA a pergunta "**Gera Chq. p/ Adiant.**" estava igual a **NÃO**e **"Mov. Banc. sem Cheque?"** igual a **NÃO**;
   1. Esse cenário é utilizado para envio do PA na remessa do CNAB, para que a movimentação bancária a pagar seja gerada no retorno do arquivo CNAB;
   2. Caso seja utilizada a rotina de baixa automática (FINA090/FINA091) o comportamento será o mesmo do retorno do CNAB, ou seja, será gerada movimentação bancária a pagar (**E5\_RECPAG** = P) e (**E5\_TIPODOC** = PA);
   3. Na rotinas de baixa automática (FINA090/FINA091) existe a pergunta "**Gera Cheque automaticamente?**", em hipótese alguma será gerado cheque para esses registros de PA na remessa CNAB, pois no momento da inclusão do adiantamento foi selecionado que o mesmo não iria possuir cheque, sendo assim, as rotinas não irão amarrar um cheque indevidamente neste titulo, garantindo o mesmo comportamento do retorno do CNAB (FINA430).
   4. No caso da baixa manual (FINA080) a baixa não será permitida sem que antes seja gerada a movimentação bancária do título (via processamento do retorno CNAB ou a baixa automática);

**Saiba mais**[MP - SIGAFIN - Quais os modos de inclusão de PA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115004726827-MP-SIGAFIN-Quais-os-modos-de-inclus%C3%A3o-de-PA?source=search)
