---
content_hash: 1eb579e7979d0972c2a36583e73d1defa3b362ac9d21e7c879c73267f4dbb07d
fetched_at: '2026-06-29T00:11:54.598816+00:00'
page_id: '856434519'
product: rm
source: tdn-rm
title: Parâmetros - Gestão de Condomínio - Fechamento do condomínio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=856434519
version: 5
---

**Definições de Fatores do CRD**

* Ao habilitar estes campos o sistema passa a permitir editar os valores de CRD de uma determinada subunidade. Para saber mais sobre os fatores de CRD, consulte a documentação abaixo:

**Subsídio**

* **Utiliza cálculo de subsídio no fechamento do condomínio:** Ao habilitar essa opção, o sistema passa a considerar o subsídio nos cálculos do fechamento. Ao marcar este parâmetro a opção nascerá habilitada por padrão no [item de cobrança do condomínio.](https://tdn.totvs.com/pages/viewpage.action?pageId=435105029)
* **Considerar a priorização da cobrança no cálculo do subsídio:** Esse parâmetro altera a forma como o subsídio é calculado ao considerar lançamentos adicionais (como locação e fundo promocional) no cálculo do CTO (Custo Total Operacional). Se este parâmetro não estiver marcado, o cálculo do subsídio leva em conta apenas o CTO fixo e os descontos simples. Agora, com o parâmetro ativado, o sistema inclui no cálculo:
  1. **Valores de locação apurados na competência**.
  2. **Valores de fundo promocional apurados na competência**.

  Se o parâmetro estiver **ativado**, esses valores são abatidos do CTO antes de calcular a diferença que será subsidiada para o sócio. Caso o parâmetro esteja **desativado**, o cálculo ignora esses valores adicionais, mantendo o comportamento anterior.
