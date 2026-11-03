---
article_id: 39424767108759
category: Contabilidade Gerencial - Plano de Contas
content_hash: 8e44b2afc388fcc80cdffc72056d2a6825f7c72656864cc70be059059881a6f1
fetched_at: '2026-06-28T22:40:33.402471+00:00'
product: protheus
section_id: 1500001549022
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - CTBA020 - Regras
  de preenchimento das datas de existência da Conta Contábil
type: support-article
updated_at: '2026-03-31T20:31:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39424767108759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Regras-de-preenchimento-das-datas-de-exist%C3%AAncia-da-Conta-Cont%C3%A1bil
---

No Protheus (versão 12.1.2310), os campos CT1\_DTEXIS (data inicial) e CT1\_DTEXSF (data final) no Plano de Contas são editáveis apenas na inclusão da conta. CT1\_DTEXIS é obrigatório e sugere uma data antiga para permitir lançamentos retroativos. CT1\_DTEXSF pode ficar em branco, indicando validade indefinida da conta para lançamentos contábeis.

**Dúvida**  
Como funcionam as regras de liberação, bloqueio e preenchimento dos campos de data de existência inicial "Dt Ini Exist (CT1\_DTEXIS)" e  "Dt Fim Exist (CT1\_DTEXSF)" na rotina de Plano de Contas (CTBA020)?

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - a partir da versão 12.1.2310  
  
**Solução**  
Os campos **"Dt Ini Exist (CT1\_DTEXIS)" e  "Dt Fim Exist (CT1\_DTEXSF)"** ficam liberados para edição exclusivamente no momento da inclusão das contas contábeis. O intuito destes campos é delimitar as datas de existência da conta, configurando o início e o término de sua utilização no sistema.

Comportamento do campo **Dt Ini Exist (CT1\_DTEXIS):** O sistema sugere, por padrão, uma data bem antiga para o início de sua existência. Este comportamento existe para garantir que a conta possa ser utilizada de forma segura em lançamentos retroativos. Além disso, trata-se de um campo de preenchimento obrigatório, não podendo ter seu conteúdo gravado em branco.

Comportamento do campo **Dt Fim Exist (CT1\_DTEXSF)**: diferente da data de início, este campo pode permanecer em branco durante a inclusão. Quando o conteúdo fica em branco, o sistema não considera uma data final para o uso da conta, mantendo-a válida e ativa indefinidamente para os lançamentos contábeis.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39424757588759)

**Saiba mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA020 - Bloqueio de Conta Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021958832-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA020-Bloqueio-de-Conta-Cont%C3%A1bil)
