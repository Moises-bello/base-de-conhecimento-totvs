---
article_id: 35189531058967
category: Financeiro
content_hash: f4b0a6440f173d4c0bd6d7d33733a0d7d64186f9fe387341fab71310c18ab048
fetched_at: '2026-06-28T22:38:00.978899+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Fórmulas - Utilização
  da fórmula para ajuste no cálculo de juros
type: support-article
updated_at: '2026-03-02T19:19:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35189531058967-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-F%C3%B3rmulas-Utiliza%C3%A7%C3%A3o-da-f%C3%B3rmula-para-ajuste-no-c%C3%A1lculo-de-juros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35189517757079) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Utilização da fórmula para ajuste no cálculo de juros

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210  
  
**Solução**

A **Rotina de Fórmulas** é uma funcionalidade que possibilita a criação de expressões lógicas ou cálculos personalizados sem a necessidade de customizações em **ADVPL**. Essa ferramenta é amplamente utilizada para **campos calculados**, **validações**, **gatilhos de eventos** ou **campos virtuais** em cadastros, relatórios e consultas.

**Exemplo prático:**

Data da operação: 05/09/2025

Vencimento: 30/10/2025

Valor: R$ 10.000,00

Taxa: 1,46% ao mês

Prazo: 55 dias

Cálculo correto dos juros (pro rata temporis):

𝐽𝑢𝑟𝑜𝑠 = 10.000 × 1,46% × (55 / 30) ≈ R$ 267,67

Neste caso, é possível utilizar a Rotina de Fórmulas para que o campo de cálculo seja ajustado.

Imagem de referência:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35189531036055)

**Saiba mais**

[Cadastro de templates - FINA716](https://tdn.totvs.com/display/public/PROT/Cadastro+de+templates+-+FINA716#CadastrodetemplatesFINA716-Exemplo1-Jurospersonalizado)
