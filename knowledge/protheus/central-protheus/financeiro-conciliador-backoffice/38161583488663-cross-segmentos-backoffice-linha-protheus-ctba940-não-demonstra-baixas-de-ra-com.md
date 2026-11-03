---
article_id: 38161583488663
category: Financeiro - Conciliador Backoffice
content_hash: d88072430d8ca52ed77cdf95c01a56eca312b701c9e2a4a56b80baefa82815fa
fetched_at: '2026-06-28T22:37:47.119266+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - CTBA940 - Não demonstra baixas
  de RA com origem na FK1
type: support-article
updated_at: '2026-02-04T19:07:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38161583488663-Cross-Segmentos-Backoffice-Linha-Protheus-CTBA940-N%C3%A3o-demonstra-baixas-de-RA-com-origem-na-FK1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38161551591063) Tempo aproximado para leitura: **00:06 min**  
  
**Dúvida**  
Por que as baixas de títulos RA, que possuem origem na tabela FK1, não estão sendo demonstradas corretamente no Conciliador Bancário (CTBA940)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33.  
  
**Solução:**

No padrão do sistema **Protheus**, as baixas realizadas no **Contas a Receber** são registradas **prioritariamente na tabela FK1**, ocorrendo também, a atualização das tabelas **SE5** e **FK5**.

É importante destacar que, para fins de **conciliação de baixas**, a **origem legítima da movimentação** (campo **E5\_TABORI**) é registrada na **FK1** para o Contas a Receber, e na **FK2** para o Contas a Pagar.

Para que o valor da baixa seja demonstrado corretamente no **conciliador**, é indispensável validar o **tipo de baixa** realizado. Em alguns cenários específicos, a tabela **FK5** **não é atualizada no momento da baixa**, sendo alimentada apenas quando ocorre a **efetivação bancária**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38161831405079)

Dessa forma, o registro na **FK5** será gravado **somente quando o tipo de documento informado no campo E5\_TIPODOC implicar em movimentação de saldo bancário, conforme tabela abaixo:**

|  |  |  |
| --- | --- | --- |
| E5\_TIPODOC | DESCRIÇÃO | Altera Saldo Bancário / Caixa |
| AP | Aplicação | Sim |
| **BA** | **Baixa de titulo** | **Não** |
| BD | Transferência por borderõ descontado | Sim |
| BL | Baixa por Lote | Sim |
| C2 | Correção Monetária de titulo em carteira descontada | Não |
| CA | Cheque Avulso / Cancelamento de Cheque Avulso | Sim |
| CB | Cancelamento de Transferência por borderô descontado | Sim |
| CD | Cheque pré datado via Movimento Bancário Manual | Não |
| CH | Cheque | Sim |
| CM | Correção Monetária | Não |
| **CP** | **Compensação CR ou CP** | **Não** |
| CX | Correção Monetária | Não |
| D2 | Desconto em título em carteira descontada | Não |
| DB | Despesas bancárias | Sim |
| DC | Desconto | Não |
| E2 | Estorno de movimento de desconto (Cobrança Descontada) | Sim |
| EC | Estorno de cheque | Sim |
| EP | Emprestimo | Sim |
| ES | Estorno de Baixa | Sim |
| IS | Imposto Substitutivo (Localizações) | Não |
| J2 | Juros de titulo em carteira descontada | Não |
| JR | Juros | Não |
| LJ | Movimento do SigaLoja | Sim |
| M2 | Multa de titulo em carteira descontada | Não |
| MT | Multa | Não |
| OC | Outros Créditos | Sim |
| OD | Outras Despesas | Sim |
| OG | Otras Ganancias (Localizações) | Não |
| PA | Inclusão PA | Sim |
| PE | Pagamento Empréstimo | Sim |
| R$ | Dinheiro | Sim |
| **RA** | **Inclusão RA** | **Sim** |
| RF | Resgate de Aplicações | Sim |
| SG | Entrada de Dinheiro no Caixa (Loja) | Sim |
| TC | Troco | Sim |
| TE | Estorno de transferência (Movimento Bancário Manual) | Sim |
| TL | Tolerância de Recebimento | Não |
| TR | Transferência para carteira descontada | Sim |
| VA | Valores Acessórios | Não |
| V2 | Baixa de titulo em carteira descontada | Não |
| VL | Baixa de titulo | Sim |
| VM | Variação Monetária | Não |

Caso contrário, a ausência de registro na FK5 faz parte do **comportamento padrão do sistema**, não caracterizando inconsistência ou erro de processamento.
