---
article_id: 360035867734
category: Financeiro
content_hash: d5e8251dca18a5e5f677266baa5581ae8c2c2afffe9a27eadfe3db61fbe70967
fetched_at: '2026-06-28T22:38:00.961427+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Compartilhamento de
  tabelas para rastreamento financeiro
type: support-article
updated_at: '2026-01-27T14:07:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035867734-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Compartilhamento-de-tabelas-para-rastreamento-financeiro
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15415760931351)***Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como compartilhar as tabelas para o rastreamento no financeiro?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Regra de compartilhamento para as Tabelas **SA6** – Bancos, **SE5** – Movimentação Bancária e **SE8** – Saldos Bancários, utilizadas na rotina **Miscelâneas / Recálculos / Rec. Saldos Bancários (FINA210)** para o reprocessamento do saldo bancário.  
Desta forma, podem ser efetuadas as seguintes configurações de compartilhamento de tabelas, para efetuar o **Recálculo de Saldos Bancários (FINA210)**:  
  
**Configuração 1**

| **SA6 – Bancos** | **SE5 – Mov. Bancárias** | **SE8 – Saldos Bancários** | **Multi Filial** |
| --- | --- | --- | --- |
| Exclusivo | Exclusivo | Exclusivo | Sim |
| Compartilhado | Exclusivo | Exclusivo | Sim |

**Comportamento do Sistema:** Apresenta o saldo movimentado por filial e não o saldo real no banco. Deve ser utilizado para separar o saldo movimentado para cada filial. Permite que a tabela **SE8** **Saldo Bancário** seja multi-filial. Para os casos em que somente a tabela **SA6 Bancos** esteja compartilhada haverá diferenças nos saldos bancários no relatório (**FINR470**) Extrato Bancário para que isto não ocorra é necessário o compartilhamento da tabela **SE8** sendo assim a configuração 2.    
  
**Configuração 2**

| **SA6 – Bancos** | **SE5 – Mov. Bancárias** | **SE8 – Saldos Bancários** | **Multi Filial** |
| --- | --- | --- | --- |
| Exclusivo | Exclusivo | Compartilhado | Não |
| Exclusivo | Compartilhado | Compartilhado | Não |
| Compartilhado | Exclusivo | Compartilhado | Não |

**Comportamento do Sistema:** Apresenta o saldo do banco com as movimentações de todas as filiais. Não permite multi-filial, devido ao saldo do banco ser único.  
**Observação**: Se o existir o mesmo banco em filiais diferentes, o sistema poderá acumular o saldo bancário **(SE8).**  
  
**Configuração 3**

| **SA6 – Bancos** | **SE5 – Mov. Bancárias** | **SE8 – Saldos Bancários** | **Multi Filial** |
| --- | --- | --- | --- |
| Exclusivo | Compartilhado | Exclusivo | Sim |
| Compartilhado | Compartilhado | Exclusivo | Sim |

**Comportamento do Sistema**: apresenta o saldo de cada filial para os bancos cadastrados na filial corrente e consulta todos os movimentos pelo campo **Filial de Origem** da tabela **SE5** - Movimentação Bancária. Permite multi-filial para a Tabela **SE8** – Saldos Bancários.  
  
**Configuração 4**

| **SA6 – Bancos** | **SE5 – Mov. Bancárias** | **SE8 – Saldos Bancários** | **Multi Filial** |
| --- | --- | --- | --- |
| Compartilhado | Compartilhado | Compartilhado | Não |

**Comportamento do Sistema:**Atualiza o saldo do Banco para todas as filiais e não permite multi-filial.  
  
**Importante**  
A forma mais comum de utilização é definir a Tabela **SE8** – Saldos Bancários como compartilhada.  
O modo de compartilhamento aplicado às tabelas **SE1** e **SE2** deve ser aplicado às tabelas **FI7** (**FI7 - Rastreamento CR**) e **FI8** (**FI8 - Rastreamento CP)**, pois se referem ao rastreamento de Contas a Receber e Pagar. Desta forma, o vínculo estará mantido.

**Saiba mais**

Compartilhamento de tabela para reprocessamento de saldo bancário (FINA210)
