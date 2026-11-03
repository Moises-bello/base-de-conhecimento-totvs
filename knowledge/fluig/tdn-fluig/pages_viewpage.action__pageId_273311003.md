---
content_hash: 219af7ee674ce63d57f75795aca814e801d3d9d17cdf98fae4be4c15e9080668
fetched_at: '2026-06-28T21:35:24.978418+00:00'
page_id: '273311003'
product: fluig
source: tdn-fluig
title: Plataforma ❙ Cálculo da nota de tópicos em turmas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273311003
version: 14
---

# Índice

4true.\*ndicenone

## Falando de cálculo da nota de tópicos em turmas...

A nota dos tópicos em turmas é calculada levando em consideração o peso e a nota dos seus itens.

### Pesos

---

Você deve definir um peso para cada item de tópico, desde que o peso seja maior que zero. Os pesos maiores que zero serão considerados no momento do cálculo da nota do tópico, enquanto os pesos iguais a zero não serão levados em conta na nota final.

Os tópicos também devem ter seus pesos definidos e cada tópico que possuir peso maior que zero será considerado no momento de calcular a nota da turma.

### Exemplo

---

Foi criado um tópico *"Conhecimentos Gerais"* com peso **1** e dentro dele foram incluídos dois itens de tópico:

* "*Matemática Básica*" com peso **1**.
* "*Matemática Avançada*" com peso **2**.

Nesse caso, o peso total dos itens de tópico (soma dos pesos) é **1** + **2** = **3**.

Supondo que a nota do item de tópico "*Matemática Básica*" seja **100,00**, como ela possui peso **1**, valerá apenas **33,33%** do total que pode ser obtido no tópico (**100%**).

Supondo que a nota do item de tópico "*Matemática Avançada*" seja **75,00**, como ela possui peso **2**, valerá **66,66%** do total que pode ser obtido no tópico (**100%**).

A fórmula que utilizamos então é: **(total de pontos do tópico) / (soma dos pesos de cada item de tópico)**.

Para esse exemplo: **100 / 3**

Peso **1** (Matemática básica, que equivale a um terço do total) = **33,33**

Peso **2** (Matemática avançada, que equivale a dois terços do total) = **66,66** (**33,33** + **33,33**).

Como no item de tópico *"Matemática Básica*" a nota obtida foi **100,00**, a nota deste item equivale a **33,33**.

Como no item de tópico "*Matemática Avançada*" a nota obtida foi **75,00**, a nota deste item equivale a **49,99**.

Portanto, o resultado final é: **83,32**.

Caso o item de tópico *"Matemática avançada*" possuísse peso **3**, por exemplo, a fórmula seria:

Peso **1** = **25%**

Peso **3** = **75%**

Importante!

A partir da atualização **[1.6.5-190219](http://tdn.totvs.com/pages/viewpage.action?pageId=442961412#Atualiza%C3%A7%C3%B5es(1.6.5)-190219)**, o **LMS** não faz mais parte da plataforma para **novas instalações**.

Mas, não se preocupe: se você adquiriu a plataforma com o **LMS incluso**, entre em contato com o [Suporte Fluig](https://suporte.fluig.com/) para que você consiga utiliza-lo normalmente – mesmo após a atualização **1.6.5-190219**. Se você não lembra se o LMS está incluso ou não no seu pacote, consulte sua proposta comercial ou entre em contato com o seu ESN.
