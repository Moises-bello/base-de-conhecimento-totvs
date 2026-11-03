---
content_hash: 92f63703e432e0dd35448eefdc8a3485bb45c954e05e1ceb9b2fe129b2928309
fetched_at: '2026-06-29T00:09:24.836020+00:00'
page_id: '423938036'
product: rm
source: tdn-rm
title: Revisão de Vida Útil/Valor Residual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938036
version: 6
---

**Foram mapeados dados pessoais ou sensíveis que estão de acordo com a Lei Geral de Proteção de Dados Pessoais. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei n° 13.709/2018.**

**Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).**

Um ativo imobilizado de qualquer empresa é depreciado considerando sua vida útil e seu valor depreciável, com isso a vida útil de um ativo é o período durante o qual o ativo espera-se seja utilizado por ela, não sendo necessariamente a vida econômica do ativo. O objetivo da Revisão de vida útil/valor residual é determinar o valor de vida útil econômica dos ativos imobilizados alinhada com seu uso de fato, determinando assim novas taxas de depreciação baseada na sua vida útil econômica estimada.

**Realizando a Revisão de Vida Útil/ Valor Residual:**  
Na primeira etapa de parametrização, deverá ser selecionado um ou mais patrimônios que sofrerão o processo. Ao avançar etapa, além do Código do Patrimônio, Descrição e Valor Base de Depreciação o sistema irá carregar as informações abaixo:

Depreciação Acumulada ao Final do Mês Anterior: É a depreciação que o patrimônio sofreu até o final do mês anterior ao de cálculo.

Valor Contábil: É o custo de aquisição do ativo menos a depreciação acumulada até o momento do teste de recuperação do ativo.

Taxa de Depreciação Acumulada: Trata-se da taxa já depreciada até o momento.

Vida Útil Restante (meses): Este campo pode ser editado. Nele será apresentado o tempo de vida restante para o patrimônio se tornar irreparável, seja no contexto operacional, técnico e\ou econômico. Ao editar a vida útil restante, automaticamente a taxa de depreciação (% mensal) será alterada.

Valor Residual ao Final da Vida Útil: Esse campo poderá ser editado. Caso o valor do patrimônio ao final da vida útil for diferente de 0,00, o valor deverá ser informado neste campo. Ao altera-lo o sistema ajustará automaticamente a Vida Útil Restante e Taxa de Depreciação.

Taxa de Depreciação (% mensal): Este campo pode ser editado. Nele será apresentada a taxa de depreciação ao mês do patrimônio. Ao editar esta taxa automaticamente a vida útil restante será modificada.

Nesta etapa além do cenário de cálculo, deve ser informada a data que o processo entrará em vigência, a data do laudo onde foi constatada a necessidade da Revisão e o Responsável pela mesma.

**Exemplos:** Selecionamos um patrimônio com data de aquisição 20/06/2011 onde na tabela de cálculos são apresentadas as seguintes faixas em 01/2013.

Moeda R$:

-Valor Base: R$ 345,00

- Depreciação Acumulada: R$ 105,61

- Valor Residual ao final da vida útil: R$0,00

- Valor Contábil: R$ 239,39 - Vida Útil Restante em Meses: 42

- Valor residual ao Final da Vida Útil: 0,00

- Taxa de Depreciação (% mensal): 1,6667 Note que a taxa de depreciação deste patrimônio é 20% ao ano.

**1) Alterando a Vida Útil do Patrimônio.**  
Após uma análise foi verificado que a vida útil deste patrimônio é superior ao calculado pelo sistema. O sistema calculou de acordo com os dados 42 meses restantes, porém este patrimônio ainda terá uma vida útil de 50 meses. Ao alterar a vida útil do patrimônio para 50 meses, o sistema irá automaticamente diminuir a taxa de depreciação mensal, tendo em vista que o patrimônio terá um tempo maior para depreciar totalmente.

Desta forma, os novos valores de cálculo deste patrimônio serão apresentados conforme abaixo:

Moeda R$:

-Valor Base: R$ 345,00

- Depreciação Acumulada: R$ 105,61

- Valor Residual ao final da vida útil: R$0,00

- Valor Contábil: R$ 239,39

- Vida Útil Restante em Meses: 50

- Valor residual ao Final da Vida Útil: 0,00

- Taxa de Depreciação (% mensal): 1,3878

Como o sistema chegou nesta nova taxa de depreciação?

(Valor Contábil / Valor Base) x 100 = % que ainda falta para depreciar. % que ainda falta para depreciar / Vida Útil Restante em Meses  
Ou seja:  
(239,39 / 345,00) x 100 = 69,3884 aproximadamente. 69,38 / 50 = 1,3878

**2) Alterando o valor residual ao final da Vida Útil**  
Após uma avaliação neste mesmo patrimônio foi verificado que ao final da vida útil este permanecerá com o valor R$ 150,00. Ou seja, este patrimônio ao final da sua vida operacional e técnica ainda terá valor econômico. Ao informar para o sistema que o valor residual deste patrimônio será R$ 150,00 e não mais R$ 0,00, sua taxa de depreciação mensal irá aumentar automaticamente. Ou seja, o patrimônio irá depreciar R$ 150,00 a menos do que deveria. Com a vida útil 42 meses sua taxa de depreciação não poderá ser apenas 1,6667% e sim 0,6169%.

Desta forma, o novo valor de cálculo do patrimônio ficará desta forma:

Moeda R$:

-Valor Base: R$ 345,00

- Depreciação Acumulada: R$ 105,61

- Valor Residual ao final da vida útil: R$0,00

- Valor Contábil: R$ 239,39 - Vida Útil Restante em Meses: 42

- Valor residual ao Final da Vida Útil: R$ 150,00 - Taxa de Depreciação (% mensal): 0,6169.

Como o sistema chegou nesta nova taxa de depreciação?

(Valor Contábil - Valor residual ao Final da Vida Útil) = Novo valor Contábil. (Novo valor Contábil / Valor Base) x 100 = % que ainda falta para depreciar. % que ainda falta para depreciar / Vida Útil Restante em Meses  
Ou seja:  
(R$ 239,39 – R$ 150,00) = R$ 89,39 (R$ 89,39 / R$ 345,00) X 100 = 25,91 25,91/ 42 = 0,6169

**3) Alterando a taxa de depreciação.**  
Após uma revisão foi verificado que este patrimônio terá sua taxa de depreciação reduzida. Deixará de ser 20% ao ano (1,6667 a.m.) e passará a ser 15% ao ano (1,25% a.m.). Ao realizar esta alteração a vida útil do patrimônio não mais poderá ser 42 meses. Com a taxa de depreciação menos a vida útil do patrimônio será mais longa, neste caso 56 meses.

O novo valor de cálculo do patrimônio ficará desta forma:

Moeda R$:

-Valor Base: R$ 345,00

- Depreciação Acumulada: R$ 105,61

- Valor Residual ao final da vida útil: R$0,00

- Valor Contábil: R$ 239,39

- Vida Útil Restante em Meses: 56

- Valor residual ao Final da Vida Útil: R$ 0,00

- Taxa de Depreciação (% mensal): 1,2500.

Como o sistema chegou nesta nova Vida Útil Restante em Meses?

(Valor Contábil / Valor Base) x 100 = % que ainda falta para depreciar. % que ainda falta para depreciar / Taxa de Depreciação (% mensal)  
Ou seja:  
(R$ 239,39/ R$ 345,00)x 100= 69,3884 69,3884/1,25 = 56 aproximadamente

**Observação**

Após alterar a taxa de depreciação, o valor residual ou a vida útil restante em meses, dos patrimônios que possuem [Avaliação Patrimonial](https://tdn.totvs.com/pages/viewpage.action?pageId=423938421), a taxa de depreciação será aumentada ou reduzida nos cenários principal e avaliado, permitindo que eles terminem de depreciar juntos.

Veja Também

* Impairment
