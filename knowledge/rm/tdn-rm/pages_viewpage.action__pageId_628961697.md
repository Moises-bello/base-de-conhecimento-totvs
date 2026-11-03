---
content_hash: 315b56d2d92a2d3f606e12d5e87a33694c5d20b3621c3d9869f97a2373f1db3a
fetched_at: '2026-06-29T00:11:05.312575+00:00'
page_id: '628961697'
product: rm
source: tdn-rm
title: EXEMPLO DE CÁLCULO - Considera percentual total nas pensões com mais de um
  dependente, que utilizam ordenado líquido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628961697
version: 1
---

Funcionário tem dois dependentes de utilizando o ordenado líquido no cálculo

Dependente 1 = 10% sobre o líquido

Dependente 2 = 20% sobre o líquido

**Parâmetro desmarcado:**

Parâmetro "Considera percentual total nas pensões que utilizam ordenado líquido" está desmarcado.

**DEPENDENTE 1**

**Cálculo inicial do IRRF:**

                    BaseCaixa = 4.000,00 + 0 - 418,93 - 0 + 0 - 0 - (1 \* 189,59) = 3.391,48

                     Valor aplicado na Tab.IRRF (BaseCaixa)          : 3.391,48

                     Percentual desconto IRRF   (PercentualIRRF)     : **15,00**

                     Parcela deduzir IRRF       (DeduzirIRRF)        : **354,80**

**Cálculo da pensão com o IRRF calculado anteriormente:**

                     Percentual desconto Pensão (PercentualPensao)   : **10,00**

                     Base Pensão = ( 4.000,00 + 0 + 0 + 0 - 418,93 - 0 - 0 + **354,80** - 0

                                   - (0,1500 \* (4.000,00 + 0 + 0 - 0)) + (0,1500 \* 1 \* 189,5900)

                                   + (0,1500 \* (418,93 + 0)) - (0,1500 \* 0) ) = 3.427,148000

                          Pensâo = 3.427,148000 \* 0,10 = 342,714800

                          Pensâo = 342,714800 / (1 - (0,10 \* 0,1500)) = 347,933807

**Total da Pensão: 347,933807**

**DEPENDENTE 2**

**Cálculo inicial do IRRF:**

                     BaseCaixa = 4.000,00 + 0 - 418,93 - 0 + 0 - 0 - (1 \* 189,59) = 3.391,48

                     Valor aplicado na Tab.IRRF (BaseCaixa)          : 3.391,48

                     Percentual desconto IRRF   (PercentualIRRF)     : **15,00**

                     Parcela deduzir IRRF       (DeduzirIRRF)        : **354,80**

**Cálculo da pensão com o IRRF calculado anteriormente:**

                     Percentual desconto Pensão (PercentualPensao)   : **20,00**

                    Base Pensão = ( 4.000,00 + 0 + 0 + 0 - 418,93 - 0 - 0 + **354,80** - 0

                                   - (0,1500 \* (4.000,00 + 0 + 0 - 0)) + (0,1500 \* 1 \* 189,5900)

                                   + (0,1500 \* (418,93 + 0)) - (0,1500 \* 0) ) = 3.427,148000

                          Pensâo = 3.427,148000 \* 0,20 = 685,429600

                          Pensâo = 685,429600 / (1 - (0,20 \* 0,1500)) = 706,628454

**Total da Pensão: 706,628454**

**Novo valor aplicado na Tab.IRRF (BaseCaixa - ValorPensao): 3391,4800 - 706,628454 = 2.684,851546**

                     Novo percentual desconto IRRF : **7,50**

                     Nova parcela a deduzir IRRF   : **142,80**

                     Base Pensão = ( 4.000,00 + 0 + 0 + 0 - 418,93 - 0 - 0 + **142,80** - 0

                                   - (0,0750 \* (4.000,00 + 0 + 0 - 0)) + (0,0750 \* 1 \* 189,5900)

                                   + (0,0750 \* (418,93 + 0)) - (0,0750 \* 0) ) = 3.469,509000

                          Pensâo = 3.469,509000 \* 0,20 = 693,901800

                          Pensâo = 693,901800 / (1 - (0,20 \* 0,0750)) = 704,468832

**Valor a ser descontado: 704,46**

**OBSERVAÇÃO:** Veja que no novo cálculo da pensão o valor do IRRF alterou a faixa de desconto e houve recálculo. para o segundo dependente. O recálculo somente acontece quando o percentual de desconto de IRRF muda de faixa. No primeiro caso não mudou de faixa.

**Parâmetro marcado:**

Parâmetro "Considera percentual total nas pensões que utilizam ordenado líquido" está marcado.

**DEPENDENTES 1 E 2**

**Cálculo inicial do IRRF:**

BaseCaixa = 4.000,00 + 0 - 418,93 - 0 + 0 - 0 - (1 \* 189,59) = 3.391,48

                     Valor aplicado na Tab.IRRF (BaseCaixa)          : 3.391,48

                     Percentual desconto IRRF   (PercentualIRRF)     : **15,00**

                     Parcela deduzir IRRF       (DeduzirIRRF)        : **354,80**

                     Percentual desconto Pensão (PercentualPensao)   : **30,00**

**Cálculo da pensão com o IRRF calculado anteriormente:**

                     Base Pensão = ( 4.000,00 + 0 + 0 + 0 - 418,93 - 0 - 0 + **354,80** - 0

                                   - (0,1500 \* (4.000,00 + 0 + 0 - 0)) + (0,1500 \* 1 \* 189,5900)

                                   + (0,1500 \* (418,93 + 0)) - (0,1500 \* 0) ) = 3.427,148000

                          Pensâo = 3.427,148000 \* 0,30 = 1.028,144400

                          Pensâo = 1.028,144400 / (1 - (0,30 \* 0,1500)) = 1.076,590995

**Total da Pensão: 1.076,590995**

**Novo valor aplicado na Tab.IRRF (BaseCaixa - ValorPensao): 3391,4800 - 1.076,590995 = 2.314,889005**

                     Novo percentual desconto IRRF : **7,50**

                     Nova parcela a deduzir IRRF   : **142,80**

                     Base Pensão = ( 4.000,00 + 0 + 0 + 0 - 418,93 - 0 - 0 + **142,80** - 0

                                   - (0,0750 \* (4.000,00 + 0 + 0 - 0)) + (0,0750 \* 1 \* 189,5900)

                                   + (0,0750 \* (418,93 + 0)) - (0,0750 \* 0) ) = 3.469,509000

                          Pensâo = 3.469,509000 \* 0,30 = 1.040,852700

                          Pensâo = 1.040,852700 / (1 - (0,30 \* 0,0750)) = 1.064,810946

                     Valor a ser descontado do Pensionista 1: 1.064,810946 / 30,00 \* **10,00 = 354,93**

                     Valor a ser descontado do Pensionista 2: 1.064,810946 / 30,00 \* **20,00 = 709,88**

**OBSERVAÇÃO:** Veja que no novo cálculo da pensão o valor do IRRF alterou a faixa de desconto e houve recálculo. Ao final o valor integral encontrado foi proporcionalizado pelos dependentes.
