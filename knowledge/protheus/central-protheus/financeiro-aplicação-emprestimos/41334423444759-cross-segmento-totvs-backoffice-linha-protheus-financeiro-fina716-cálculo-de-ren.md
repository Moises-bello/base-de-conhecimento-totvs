---
article_id: 41334423444759
category: Financeiro - Aplicação / Emprestimos
content_hash: 82c7d007797789952c36623be88179c03d0bb9f42b5abc98af74b8ec83b30e45
fetched_at: '2026-06-28T22:37:59.332830+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA716 -
  Cálculo de rendimento para Aplicação FAF por Cotas, mensal e anual
type: support-article
updated_at: '2026-06-22T13:53:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41334423444759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-FINA716-C%C3%A1lculo-de-rendimento-para-Aplica%C3%A7%C3%A3o-FAF-por-Cotas-mensal-e-anual
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41334423438231) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
FINA716 - Cálculo de rendimento para Aplicação FAF por Cotas, mensal e anual  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as releases  
  
**Solução:**

O cálculo do rendimento para aplicações do tipo FAF por cotas é diretamente influenciado pela configuração do parâmetro **MV\_RENAPL4**.

Este parâmetro determina se o rendimento será apurado de forma acumulada (desde a data inicial da aplicação) ou de forma mensal (considerando apenas a valorização ocorrida após a última apropriação).

Abaixo é demonstrado o funcionamento de cada cenário com base em um exemplo prático de evolução da cota.

**Dados dos valores de 1 Cota dia a dia.**

* 30/03/2026: R$ 2,00
* 31/03/2026: R$ 3,00
* 29/04/2026: R$ 4,00
* 30/04/2026: R$ 5,00
* 04/05/2026: R$ 6,00

**Inclusão da Aplicação FAF (30/03/2026)**

* Quantidade de cotas adquiridas: 1.000 cotas
* Valor da cota inicial: R$ 2,00
* Valor aplicado: R$ 2.000,00 (1.000 unidades x R$ 2,00)

**Cenário 1: MV\_RENAPL4 = 1 (Acumulado)** Neste modo, o rendimento é calculado considerando o valor histórico desde a data da aplicação, subtraindo a cota inicial do valor da cota atual multiplicada pelo saldo de cotas.

* **31/03/2026 (Apropriação):** 1.000 x (3,00 - 2,00) = **R$ 1.000,00  de rendimento**
* **29/04/2026 (Resgate de 300 cotas):** 300 x (4,00 - 2,00) = **R$ 600,00 de rendimento**. O saldo de cotas passa a ser 700 unidades (1.000 unidades - 300 unidades).
* **30/04/2026 (Apropriação):** 700 unidades x (5,00 - 2,00) = **R$ 2.100,00  de rendimento**
* **30/05/2026 (Simulação de Apropriação - sem executar a ação):** 700 unidades x (6,00 - 2,00) = **R$ 2.800,00  de rendimento**

   (Com o parâmetro MV\_10892 = ' ' para não considerar o come cotas)
* **04/05/2026 (Resgate Total):** 700 x (6,00 - 2,00) = **R$ 2.800,00  de rendimento**

**Cenário 2: MV\_RENAPL4 = 2 (Mensal)** Neste modo, o rendimento considera somente a valorização da cota ocorrida após a última apropriação ou evento financeiro registrado. A cota de referência para os cálculos subsequentes é sempre atualizada.

* **31/03/2026 (Apropriação):** 1.000 x (3,00 - 2,00) = **R$ 1.000,00  de rendimento** . A cota de referência passa a ser R$ 3,00.
* **29/04/2026 (Resgate de 300 cotas):** 300 x (4,00 - 3,00) = **R$ 300,00  de rendimento** O saldo de cotas passa a ser 700 unidades.  
  = (saldo em cotas) \* (Cota da apropriação atual - Cota da última apropriação)
* **30/04/2026 (Apropriação):** 700 x (5,00 - 3,00) = **R$ 1.400,00  de rendimento**. A cota de referência passa a ser R$ 5,00.

  = (saldo em cotas) \* (Cota da apropriação atual - Cota da última apropriação)
* **30/05/2026 (Simulação de Apropriação - sem executar):** 700 x (6,00 - 5,00) = **R$ 700,00  de rendimento**

   (Com o parâmetro MV\_10892 = ' ' para não considerar o come cotas)
* **04/05/2026 (Resgate Total):** 700 unidades x (6,00 - 5,00) = **R$ 700,00  de rendimento**

  = (saldo em cotas) \* (Cota da apropriação atual - Cota da última apropriação)

**Reflexo na tabela SEI (Movimento de Aplicações/Empréstimos)** Para os registros gerados a partir destas movimentações, o sistema utilizará o campo **EI\_TIPODOC** com os seguintes identificadores:

* **I7:** Grava o valor referente ao rendimento.
* **I6:** Grava o valor referente ao IRF (Imposto de Renda Retido na Fonte).

Saiba mais:  
[Valores utilizados neste documento e utilização do parâmetro MV\_RENAPL4](https://tdn.totvs.com/pages/releaseview.action?pageId=571786367)  
[Apropriação - FINA716](https://tdn.totvs.com/pages/releaseview.action?pageId=684987454)

[Empréstimos - FINA716](https://tdn.totvs.com.br/pages/releaseview.action?pageId=684987254)  
[Exemplo\_de\_Contabilização\_de\_Aplicação\_e\_Empréstimo](https://tdn.totvs.com/pages/releaseview.action?pageId=236430682)  
[Aplicações e Empréstimos - Financeiro P12](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=392500138)
