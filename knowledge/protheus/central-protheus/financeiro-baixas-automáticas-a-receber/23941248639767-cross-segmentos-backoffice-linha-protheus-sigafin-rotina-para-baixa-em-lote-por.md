---
article_id: 23941248639767
category: 'Financeiro - Baixas Automáticas a Receber '
content_hash: 55fcc2d097644611531b954f49cd93c530d7468bc9151facdf034b2fc7a7e1f7
fetched_at: '2026-06-28T22:37:38.762236+00:00'
product: protheus
section_id: 35057325714199
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Rotina para Baixa em
  Lote por Dação
type: support-article
updated_at: '2026-03-30T14:48:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23941248639767-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Rotina-para-Baixa-em-Lote-por-Da%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23941248616087) Tempo aproximado para leitura: **00:02 min**  
  
**Dúvida**  
Existe uma rotina específica para ser realizada a baixa em lote por Dação?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões.  
  
**Solução**

Por padrão, o sistema não possui uma rotina específica de baixa em lote por dação (sem movimentação bancária). No entanto, é possível efetuar a baixa de múltiplos registros em massa utilizando a rotina de FINA110 Baixa Automática, desde que seja utilizado um motivo de baixa configurado para dação.

**Passos**

1. Acesse a rotina de **Baixas Automáticas de Título**s (como Contas a Receber) no módulo Financeiro.
2. Na tela principal da rotina, clique na opção "+ Automatica".
3. Na janela de parâmetros da "Baixa Automatica", preencha os filtros desejados, como período de Vencimento e Cliente.
4. No campo "Mot.Baixa", selecione ou digite o código do motivo correspondente à dação (exemplo: DACAO). Observe que, com este preenchimento, não é necessário informar os campos de Banco, Agência e Conta.
5. Clique em "Ok" para confirmar a parametrização e aguarde o processamento das baixas.
6. Após a conclusão, ao consultar as movimentações geradas (tabela **SE5**), os registros apresentarão o histórico da dação no campo **E5\_HISTOR** e o tipo de documento como BA no campo **E5\_TIPODOC.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/39306953534999)](https://centraldeatendimento.totvs.com/hc/article_attachments/39306953534999)

Tabela (SE5)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/39306953535895)](https://centraldeatendimento.totvs.com/hc/article_attachments/39306953535895)

Saiba mais:

[FINA110 -Baixa Automática de Títulos a Receber](https://tdn.totvs.com/pages/viewpage.action?pageId=312167132)
