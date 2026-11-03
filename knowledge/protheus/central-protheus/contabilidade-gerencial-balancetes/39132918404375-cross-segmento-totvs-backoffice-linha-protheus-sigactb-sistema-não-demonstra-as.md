---
article_id: 39132918404375
category: Contabilidade Gerencial - Balancetes
content_hash: d34d98c3224bae0fedad780f9d6702552b92c5ad0db4f7ec3a9807eee985b669
fetched_at: '2026-06-28T22:41:04.245562+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - Sistema não
  demonstra as contas sintéticas no balancete
type: support-article
updated_at: '2026-03-19T17:33:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39132918404375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-Sistema-n%C3%A3o-demonstra-as-contas-sint%C3%A9ticas-no-balancete
---

**Dúvida**   
O sistema não demonstra as contas sintéticas no balancete ao selecionar a opção "Imprime Contas?" igual a "Sintéticas" ou "Ambas".

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade de Gestão (SIGACTB) -  Versão 12

**Solução**   
Para que as contas sintéticas sejam corretamente demonstradas no balancete, é necessário validar os parâmetros de impressão do relatório, a configuração da hierarquia no Plano de Contas e, caso haja inconsistência nos valores, realizar o reprocessamento dos saldos.

**Passos**

**1 - Verifique o parâmetro "Imprime Valor Zera?":**

* Ao gerar o relatório de balancete, localize a pergunta I**mprime Valor Zera****?**.
* Se o parâmetro estiver como **Não** e a conta sintética tiver saldo zero (mesmo nos casos em que possua movimentações a débito e crédito que se anularam no período), a conta não será impressa.
* **Ação:** Altere o parâmetro para **Sim** e gere o relatório novamente para testar a impressão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39137193969815)

**2 - Valide o cadastro da conta no Plano de Contas:**

* Acesse o módulo **Contabilidade de Gestão (SIGACTB)**.
* Siga o caminho: **Atualizações > Entidades > Plano de Contas (CTBA020)**.
* Localize a conta sintética que não está sendo apresentada no relatório.
* Verifique o conteúdo do campo **Classe (CT1\_CLASSE)**: o mesmo deve estar preenchido como **1 - Sintética**.

  + *Observação:* Se o campo estiver configurado como "2 - Analítica", o sistema tratará o registro como conta de lançamento, o que fará a hierarquia falhar caso existam contas "filhas" atreladas.
* Verifique se o campo **Conta Superior (CT1\_CTASUP)** está devidamente preenchido apontando para as contas sintéticas da hierarquia correspondente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39137193973655)

**3 - Efetue o Reprocessamento de Saldos (se necessário):**

* Se a conta está parametrizada corretamente, deveria apresentar saldo e ainda assim não é exibida, pode haver inconsistência nas tabelas de saldos contábeis (Família CQ0 a CQ9 / CQ1).
* Nesse cenário, execute a rotina de **Reprocessamento (CTBA960 / CTBA980)** para o período solicitado, a fim de recalcular os saldos das entidades contábeis a partir da tabela de lançamentos.

**Saiba Mais**

* [Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como realizar o reprocessamento de saldos no SIGACTB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007452371-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-realizar-o-reprocessamento-de-saldos-no-SIGACTB)
