---
article_id: 22539651067927
category: PMS - Integrações
content_hash: d2ba9bb49facebe02e6c109992a0a8394d8a457935e84c935d3dedb281a81467
fetched_at: '2026-06-28T22:37:16.767663+00:00'
product: protheus
section_id: 1500001550742
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Integração do módulo Gestão
  de Projetos (SIGAPMS) com o Financeiro (SIGAFIN)
type: support-article
updated_at: '2024-07-01T17:31:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22539651067927-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Integra%C3%A7%C3%A3o-do-m%C3%B3dulo-Gest%C3%A3o-de-Projetos-SIGAPMS-com-o-Financeiro-SIGAFIN
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22539627392663) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**  
Como funciona a integração do módulo Gestão de Projetos (SIGAPMS) com o Financeiro (SIGAFIN)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões.  
  
**Solução**  
Pré-requisitos:

* MV\_PMSITMU = 0
* MV\_INTPMS = S

   
A integração do SIGAPMS com o SIGAFIN se dá por meio de receitas (contas a receber) e despesas (contas a pagar), isso permite uma visão ampla do projeto nos relatórios gerenciais de projetos.  
   
1 - SIGAFIN -> SIGAPMS

* A) Entrar na rotina FINA740 (contas a receber) e amarrar pelo outras ações o título com o projeto, gerando a tabela AFT (Contas a Receber x SIGAPMS)
* B) Entrar na rotina FINA750 (contas a pagar) e amarrar pelo outras ações o título com o projeto, gerando a tabela AFR (Contas a Pagar x SIGAPMS

2 - SIGAPMS -> SIGAFIN

* A) Criar uma TES entrada com "Movimenta estoque? (F4\_ESTOQUE = Sim)" e "Mov. Projet. (F4\_MOVPRJ = 1)" e criar uma TES saída com "Movimenta estoque? (F4\_ESTOQUE = Sim)" e "Mov. Projet. (F4\_MOVPRJ = 2)"
* B) O título a pagar (despesa) relacionado ao PMS será gerado quando feito um documento de entrada (com a TES entrada configurada como acima) que parta de uma solicitação de compras que tenha a amarração com o projeto (Projeto -> SC -> PC -> DE).
* C) O título a receber (receita) relacionado ao PMS será gerado quando faturado um pedido de venda (com a TES saída configurada como acima) que parta de um projeto (Projeto -> PV -> DS)

**Relatórios de verificação do PMS e suas tabelas verificadas:**

* Receitas de projetos (PMSR220) - AF8/SA1/SA2
* Despesas de projeto (PMSR230) - AF8/SA2/SA1
* Despesas (PMSR330) - AJ8
* Receitas (PMSR320) - AJ8

   
OBSERVAÇÃO: O orçamento de projeto seria apenas um rascunho para o projeto final.
