---
article_id: 360055860033
category: Contabilidade Gerencial - Balancetes
content_hash: 586fc1ce9212965753cae75532ef2338b04fbe04cc1d612197f3b85e0a913322
fetched_at: '2026-06-28T22:41:04.196477+00:00'
product: protheus
section_id: 1500001537281
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBR040 -  Como emitir
  o balancete anual, com apurações trimestrais
type: support-article
updated_at: '2026-06-08T17:17:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055860033-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBR040-Como-emitir-o-balancete-anual-com-apura%C3%A7%C3%B5es-trimestrais
---

**Dúvida**  
Como emitir o relatório Balancete (CTBR040) anual, com apurações trimestrais  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - a partir da versão 12.1.33  
  
**Solução**  
No Protheus, quando há mais de uma apuração no mesmo ano, é possível configurar a impressão do Balancete para ignorar uma apuração específica ou visualizar a movimentação das contas de resultado (Receitas e Despesas) sem que elas estejam zeradas.  
  
Siga os passos abaixo para a configuração:

Nessa demonstração o objetivo é imprimir apenas os valores dos lançamentos referente ao ano de 2026 sem os valores das apurações (2025/2026) e também sem os saldos anteriores referente a 2025 sejam impressos.  
  
 - Ano 2025 e 2026 com 4 trimestres apurados (Março/Junho/Setembro/Dezembro)  
- Apuração sem Conta Ponte

* Contas de Crédito - 311010001
* Conta de Apuração - 235010001

**Lançamentos:**

Total dos lançamentos em 2025 → R$ 10.000,00

Total das apurações de 2025 → R$ 10.000,00

Total dos lançamentos em 2026 → R$ 10.000,00

Total das apurações de 2026  → R$ 10.000,00

![](https://tdn.totvs.com/download/attachments/718409259/image-2024-11-27_14-9-41.png?version=1&modificationDate=1732727381367&api=v2)

**Balancete Modelo 1**

**Parâmetros:**

![](https://tdn.totvs.com/download/attachments/718409259/image-2024-11-27_14-22-11.png?version=1&modificationDate=1732728131607&api=v2)

**Na pergunta 23:** Data Lucros/Perdas foi informado a data do primeiro trimestre de 2026.

**Na pergunta 25:**Ignora Sl Ant. Rec/Des foi informado que Sim desejo ignorar o saldo anterior das contas de receitas/despesas conforme o grupo e a data escolhida nos dois parâmetros abaixo (26 e 27).

**Na pergunta 26:** Grupos Receitas/Despesas foi informado a inicial do código do grupo de receitas/ despesas que deverá ter seu saldo anterior ignorado.

**Observação:** Caso deseje ignorar mais de um grupo, pode-se utilizar o caractere virgula " , " ou ponto e virgula " ; " para separar os grupos. "Essa pergunta será considerada somente se a pergunta 'Ignora Sl Ant. Rec/Desp' estiver preenchida com 'Sim'."

**Na pergunta 27:**Data Sld Ant. Receita/Desp. foi informado a data do início do ano de 2026, não trazendo assim saldo anterior a essa data.

**Observação:**Essa pergunta será considerada somente se a pergunta 'Ignora Sl Ant.Rec/Desp?' estiver preenchida com 'Sim'.

![](https://tdn.totvs.com/download/attachments/718409259/image-2024-11-27_14-22-59.png?version=1&modificationDate=1732728179177&api=v2)

Valores referente aos lançamentos de 2026 sem considerar as apurações e saldos anteriores.

**Saiba mais:**

[**https://tdn.totvs.com/pages/releaseview.action?pageId=718409259**](https://tdn.totvs.com/pages/releaseview.action?pageId=718409259)

[Balancetes (CTBR040) - Como emitir o relatório anual, com apurações trimestrais/semestrais/mensais.](https://tdn.totvs.com/pages/releaseview.action?pageId=718409259)
