---
article_id: 360027016712
category: Gestão de Transportes (TMS)
content_hash: f5ada303a5f8fc40fe473b2120c6d58b9805b6c1ee8f5ebb6eface3eef381f53
fetched_at: '2026-06-28T22:45:29.431795+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Mensagem Fora do período de faturamento
type: support-article
updated_at: '2022-06-21T12:28:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027016712-Log%C3%ADstica-Linha-Protheus-TMS-Mensagem-Fora-do-per%C3%ADodo-de-faturamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:00:30 min****Dúvida**Como avaliar a mensagem **Fora do período de Faturamento na geração de Fatura**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) – Todas as versões  
  
**Solução**A rotina **Fatura Automática - TMSA491** deve ser executada quando o conteúdo do parâmetro **MV\_TMSMFAT** estiver preenchido com **2 - DT6 - Documentos de Transporte**, permitindo gerar faturas automáticas conforme **configuração do perfil do cliente** e os dados informados no **Tipo de Faturamento**.  
  
Uma fatura pode gerar diversas parcelas, de acordo com a **condição de pagamento,** informada no cadastrado do **Cliente Devedor**.  
  
Exemplo de como o sistema valida os cadastros envolvidos x datas utilizadas:

* Verificar a **Data base do sistema 08/05/19:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026897391/mceclip7.png)

* **Atualizações\Financeiro\Fatura Automática:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026881932/mceclip1.png)**

* **Atualizações\Recebimento\Entrada de Documentos de Clientes** com data de emissão igual a 22/04/19

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026881852/mceclip0.png)**

* **Atualizações\Comercial\Perfil Cliente** pasta **Financeiro,** campo **Tipo Fatura.** No exemplo abaixo é semanal.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026894551/mceclip2.png)**

* **Atualizações\Cadastros\Clientes** pasta **Vendas,** campo **Cond. Pagto:** Verificar o cliente devedor, a condição de pagamento utilizada, no exemplo abaixo é pagamento no ato/à vista.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026882052/mceclip3.png)**

Nesse exemplo o Sistema irá apresentar a mensagem, pois a data de emissão do documento é 22/04/19, a data base do Sistema é 08/05/19, são 16 dias de diferença e está sendo utilizada uma condição de pagamento semanal, ou seja, 7 dias.  
  
Após alterar a data base do Sistema para 30/04/19, ficando dentro do período da condição de pagamento. O Sistema gerou a fatura corretamente:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026894711/mceclip4.png)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026882112/mceclip5.png)**
