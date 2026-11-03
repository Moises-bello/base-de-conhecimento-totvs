---
article_id: 39399902652823
category: Financeiro - Baixas a Pagar
content_hash: 195f2c86639c443e9a4c0fffb3fe283d35ac7cb2449bcb0d88083f56cbcc6520
fetched_at: '2026-06-28T22:42:13.610395+00:00'
product: protheus
section_id: 38310054605975
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Preenchimento do campo
  E2_DATACAN
type: support-article
updated_at: '2026-03-31T11:03:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39399902652823-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Preenchimento-do-campo-E2-DATACAN
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39399902621079)Tempo aproximado para leitura: 00:06 min**

**Dúvida**  
Qual a finalidade e como é realizado o preenchimento do campo E2\_DATACAN(data de cancelamento) no módulo Financeiro do Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Financeiro - Todas as versões  
  
**Solução**  
O campo E2\_DATACAN tem a função de registrar a data em que ocorreu o cancelamento da liberação de um título para pagamento. Este campo é alimentado exclusivamente quando um título, que já havia sido liberado para baixa, tem sua situação revertida para "Cancelado" através da rotina de Liberação de Pagamentos (FINA580).

Para preenchimento, certifique-se de que os parâmetros abaixo estejam configurados no módulo Configurador (SIGACFG):

* **MV\_FINCTAL** = 1 (Habilita a utilização de liberação simples).
* **MV\_CTLIPAG** = .T. (Ativa o controle de liberação de pagamentos).

Exemplo de utilização:

1. Acesse a rotina **Contas a Pagar (FINA750)** e inclua um título.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39399872703895)
2. Ainda na rotina **FINA750 (ou utilize a FINA580)**, e realize a liberação do título utilizando a opção "Lib p Pagamento" definida como **Manual**. Após a confirmação, observe que a legenda do título ficará verde (Título liberado para pagamento).  
   ![liberacaobx.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39399872705559)
3. Acesse a rotina **Liberação de Pagamentos (FINA580)**.
4. Selecione o título desejado, clique em **Outras Ações** e escolha a opção **Situação**.
5. Altere a situação para **03 - Cancelado**  
   **![cancelamentolib.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39399902628247)**
6. O sistema processará a alteração, mudando a legenda do título para laranja (Titulo Cancelado) e gravando automaticamente a data base do sistema no campo **E2\_DATACAN**.
