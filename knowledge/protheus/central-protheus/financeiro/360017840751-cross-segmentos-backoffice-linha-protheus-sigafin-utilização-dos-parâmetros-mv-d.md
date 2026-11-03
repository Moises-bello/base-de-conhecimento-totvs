---
article_id: 360017840751
category: Financeiro
content_hash: 11ac56634d0f581ff59931b44ff118918ff81a7399b97cb9f08843948a4fbb58
fetched_at: '2026-06-28T22:38:04.143467+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Utilização dos parâmetros
  MV_DATAFIN e MV_BXDTFIN '
type: support-article
updated_at: '2023-12-19T20:01:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017840751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Utiliza%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-DATAFIN-e-MV-BXDTFIN
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como utilizar os parâmetros MV\_DATAFIN e MV\_BXDTFIN

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O parâmetro **MV\_DATAFIN** determina a data em que serão iniciadas as movimentações financeiras, já o parâmetro **MV\_BXDTFIN** determina se as operações de baixas a pagar e a receber considerarão a data definida no parâmetro **MV\_DATAFIN**.

Para as operações de inclusão, exclusão e alterações de **Contas a Receber** e a **Pagar FINA040, FINA050**, o Sistema sempre verifica a data definida no parâmetro **MV\_DATAFIN**.  
  
Caso a data da operação seja inferior à data definida no parâmetro, não será permitido realizar nenhuma destas operações, independente do tipo de documento utilizado - **NF**, **PA**, **RA**, **BOL**, etc.  
  
O parâmetro **MV\_BXDTFIN** será considerado nas operações de Baixas a pagar e Baixas a receber, independente do **tipo de baixa - Dação, Devolução, Normal,** etc., que envolvem:

 - **Baixas a Receber** - FINA070   
 - **Baixa por lote**  
 - **Cancelamento de baixa e exclusão de baixa.**  
 - **Baixas a Receber Automática** - FINA110  
 - **Baixas a Pagar** - Fina080   
 - **Baixa por lote**  
 - **Cancelamento de baixa e exclusão de baixa.**  
 - **Baixas a Pagar Automática** - FINA090

Nestas operações, o Sistema verifica a configuração do parâmetro **MV\_BXDTFIN** para determinar se as baixas serão efetuadas, independente do parâmetro **MV\_DATAFIN**.

**Importante.:**

Ao configurar os parâmetros **MV\_DATAFIN / MV\_BXDTFIN,** é importante que coloque o conteúdo no parâmetro sem informar "Aspas", exemplo de como utilizar:

**Exemplo: Parâmetro MV\_BXDTFIN:**

**![teste.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/12272372300055)**

**Exemplo: Parâmetro MV\_DATAFIN:**

**![teste_22.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/12272469596951)**
