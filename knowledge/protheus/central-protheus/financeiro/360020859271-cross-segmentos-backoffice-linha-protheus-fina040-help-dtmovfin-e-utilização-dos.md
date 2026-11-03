---
article_id: 360020859271
category: Financeiro
content_hash: 19191553a72fee18b3bf3615bfd320e49ef5311f510311a19c5e3892d60cb2cf
fetched_at: '2026-06-28T22:38:01.186761+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA040 - HELP - DTMOVFIN e utilização
  dos parâmetros MV_DATAFIN e MV_BXDTFIN
type: support-article
updated_at: '2026-05-27T10:56:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020859271-Cross-Segmentos-Backoffice-Linha-Protheus-FINA040-HELP-DTMOVFIN-e-utiliza%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-DATAFIN-e-MV-BXDTFIN
---

**Dúvida**  
Como utilizar os parâmetros MV\_DATAFIN e MV\_BXDTFIN?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Financeiro - A partir da versão 11.80  
  
**Solução**  
O parâmetro **MV\_DATAFIN** determina a data limite para início das movimentações financeiras no sistema. Já o parâmetro **MV\_BXDTFIN** define se as operações de baixa de Contas a Pagar e Contas a Receber deverão respeitar a data configurada no **MV\_DATAFIN**.

Nas rotinas de Contas a Receber (FINA040/FINA740), o sistema sempre valida a data definida no parâmetro **MV\_DATAFIN em conjunto com o MV\_DTCNREC**, que pode assumir os seguintes valores:

* **1 = Data de Emissão (padrão)**
* **2 = Data Base (Database)**

##### **Cenário quando MV\_DTCNREC = 1**

Caso a data base do usuário seja posterior à data definida no **MV\_DATAFIN**, o sistema permitirá informar uma data de emissão inferior à data do parâmetro, pois a validação será realizada com base no campo **E1\_EMIS1**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40764520508567)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40764520509591)

Por outro lado, se a data base for inferior à data definida no **MV\_DATAFIN**, nenhuma operação será permitida, independentemente do tipo de documento utilizado (NF, PA, RA, BOL, entre outros).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40764520509975)

##### **Cenário quando MV\_DTCNREC = 2**

Neste cenário, mesmo que o usuário esteja logado em uma data posterior à configurada no **MV\_DATAFIN**, o sistema não permitirá a inclusão de títulos cuja data seja inferior à data definida no parâmetro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40764549761559)

**Cenário relacionados a exclusões:**  
Alterado o parâmetro **MV\_DATAFIN** = 20/03/2021   
Realizar a exclusão do titulo no dia 13/03/2021, o sistema ira apresentar a mensagem de help informando que não é possível realizar movimentações financeiras com data menor ao parâmetro **MV\_DATAFIN**.  
Realizar a exclusão dia 21/03/2021, o sistema permitira a exclusão, pois se trata de uma movimentação financeira, após o período de bloqueio.

O parâmetro **MV\_BXDTFIN** será considerado nas operações de e Baixas a receber, independente do tipo de baixa - Dação, Devolução, Normal, etc., que envolvem:

- **Baixas a Receber - FINA070**   
 - **Baixa por lote**  
 - **Cancelamento de baixa e exclusão de baixa**.  
 - **Baixas a Receber Automática - FINA110**  
 - **Baixa por lote**  
 - **Cancelamento de baixa e exclusão de baixa**.

Nestas operações, o Sistema verifica a configuração do parâmetro **MV\_BXDTFIN** para determinar se permite as baixas de acordo com a data definida no parâmetro  **MV\_DATAFIN.**

**Exemplo 2 FINA080**  
Alterado o parâmetro **MV\_DATAFIN** = 31/04/2021 e **MV\_BXDTFIN** = 2 (sem aspas) , ou seja, só poderão ser efetuados movimentos financeiros que atualizem banco após a data 31/04/2021   
Acessar o sistema com uma data maior a 31/04/2021 e efetuar o cancelamento normalmente.

**Importante**  
O parâmetro **MV\_BXDTFIN** não permite que o usuário realize baixas, cancelamentos ou exclusões de baixas com a data base anterior a data configurada no parâmetro **MV\_DATAFIN**. Porém, o cancelamento de baixa com data base posterior a data do parâmetro **MV\_DATAFIN**  o sistema permite realizar, mesmo com a configuração destes parâmetros. Pois no cancelamento da baixa é criada uma nova linha na tabela **SE5** (movimentos bancários) no dia em que operação é cancelada (data posterior ao fechamento) não alterando a movimentação realizada antes do fechamento definido no parâmetro **MV\_BXDTFIN**.   
Apenas a exclusão, mesmo com data posterior não será permitida, pois na exclusão, o registro da baixa é deletado da tabela, alterando o saldo antes do fechamento.  
Possível help que pode ser apresentado, caso o esteja tentando fazer uma movimentação anterior a data digitada no parâmetro **MV\_DATAFIN**:   
**AJUDA:DTMOVFIN** - Não são permitidas movimentações financeiras com datas menores que a data limite de movimentações no Financeiro.  
Verificar parâmetro **MV\_DATAFIN.**  
  
**![mv_datafin.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019459542)**

**Saiba mais**  
[Utilização dos parâmetros MV\_DATAFIN e MV\_BXDTFIN](https://tdn.totvs.com.br/pages/releaseview.action?pageId=6070721)
