---
article_id: 22311331664535
category: Financeiro - Contas a Pagar
content_hash: 128f24a0793929492c1221b3fbe2d485dfc6063e3c22c74f68e9dea2a909e73d
fetched_at: '2026-06-28T22:38:09.734237+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA790 - Retenção
  Autopeças Cadastro
type: support-article
updated_at: '2024-03-26T20:02:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22311331664535-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA790-Reten%C3%A7%C3%A3o-Autope%C3%A7as-Cadastro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22311331653783) Tempo aproximado para leitura: **03:00 min** **Dúvida**  
Como realizar o vencimento específico para o Regime de Autopeças?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**

Para **vencimento de PCC** no regime de autopeças o sistema disponibiliza a rotina **FINA790** - no qual deverá ser incluída no menu através do ambiente **Configurador.**

Foi criada uma melhoria no controle de vencimentos dos impostos

Devendo ativar o parâmetro **MV\_CRTVENC**, será considerado o **vencimento** x **código de retenção** que tenha sido configurado na rotina **FINA790**.

**Exemplo:**   
Vamos considerar que para os **CODRET** (**E2\_CODRET**) de número 1708 o cliente queira considerar o vencimento Mensal (**dia 20 do próximo mês**) e para os de código 6147 como quinzenal (**vencendo no final da quinzena subsequente**).

As opções disponíveis para relacionamento com o Código de Retenção cadastrado:

**1 – Diário** (na data de ocorrência)

**2 – Semana**l (3º dia útil da semana subsequente)

**3 – Decendia**l (3º dia útil do próximo decênio)

**4 – Quinzenal** (Até o último dia útil da quinzena subsequente)

**5 – Mensal** (Até o dia 20 do mês seguinte)

O mesmo irá efetuar a amarração de **código de retenção** com um vencimento determinado;

Para inclusões de forma manual no ambiente **Financeiro** é necessário habilitar os campos:

Cód. Ret. PIS (**E2\_CODRPIS**)

Cód. Ret. Cof. (**E2\_CODRCOF**)

Cód. Ret. CSL (**E2\_CODRCSL**)

Para que seja apresentado no browser e que esteja como usado no ambiente **Configurado**r, no momento da inclusão seja informado os códigos amarrados na rotina **FINA790** com seus respectivos impostos.

**Saiba Mais**

**[FINA790 - Autopeças](https://tdn.totvs.com/pages/releaseview.action?pageId=249956940)**
