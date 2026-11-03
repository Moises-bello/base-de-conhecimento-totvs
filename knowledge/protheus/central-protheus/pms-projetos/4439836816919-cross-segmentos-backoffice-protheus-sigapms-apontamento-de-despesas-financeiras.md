---
article_id: 4439836816919
category: PMS - Projetos
content_hash: 9c1a084f48bde36485858da8d140df5e7dc8468e0a9b0ff1953a20fbe45dbe12
fetched_at: '2026-06-28T22:37:15.164828+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Apontamento de Despesas Financeiras
  das Cauções de Contratos - SIGAGCT
type: support-article
updated_at: '2024-02-26T18:22:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4439836816919-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Apontamento-de-Despesas-Financeiras-das-Cau%C3%A7%C3%B5es-de-Contratos-SIGAGCT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21628065688215) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Como realizar apontamento de Despesas Financeiras das Cauções de Contratos?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Versão 12  
  
**Solução**

Para as empresas que utilizam o ambiente SIGAPMS - Gestão de Projetos integrado a demais ambientes do Protheus, com o objetivo de automatizar o gerenciamento de projetos em todas as suas etapas, é possível apontar, através do ambiente Gestão de Contratos, os lançamentos das despesas financeiras das cauções dos contratos em seus projetos relacionados.

O Sistema relaciona o rateio de distribuição dos valores financeiros entre os projetos em execução controlados pelo ambiente Gestão de Projetos através da Caução. Tais informações financeiras poderão ser integradas aos projetos, quando relacionadas às Cauções de Contratos e quando forem geradas pelas seguintes situações:

* Baixa da caução de retenção, efetuada na rotina “Contratos”, que possibilita a geração de títulos a pagar do tipo nota de débito ao fornecedor (NDF)
* Inclusão da caução de abatimento, efetuada na rotina “Caução”, que possibilita a geração de títulos a pagar do tipo pagamento antecipado (PA).
* Baixa da caução, efetuada na rotina “Caução”, que possibilita a geração de títulos a pagar do tipo duplicata (DP).

Nas três situações apresentadas, ao confirmar a gravação da despesa financeira, será exibida a janela “Assistente de Apontamento – Gerenciamento de Projetos – Despesas”, que permite informar os dados dos projetos relacionados, tais como: código do projeto, tarefa, tipo de despesa, valor do projeto, etc.

Para o seu correto funcionamento, deve habilitar os seguintes parâmetros:

* MV\_CAUCNAT, Informar a natureza dos títulos de pagamento antecipado de cauções do módulo SIGAGCT
* MV\_CNRETNA, Informar a Natureza dos títulos financeiros gerados pela retenção de contratos do SIGAGCT.
* MV\_CNEXPMS, que determina se o ambiente Gestão de Contratos gera lançamentos de despesas de projetos, durante as movimentações financeiras.
* MV\_INTPMS, que determina que o ambiente Gestão de Projetos está integrado aos outros ambientes do Protheus.

**Saiba mais em: [Apontamento das Cauções dos Contratos - GCT](https://tdn.totvs.com/x/Es4KDg)**
