---
content_hash: 0de99b832ddcff60a34205a806bf3f43e19468d5e810a3aba086432b34f8aa53
fetched_at: '2026-06-29T00:10:05.027546+00:00'
page_id: '452719270'
product: rm
source: tdn-rm
title: Exemplo de cálculo da avaliação de desempenho (RHU)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719270
version: 2
---

**Exemplo de cálculo da avaliação de desempenho**

**1) Criação das competências e seus itens de performance: Acompanhamento| Competências| Dicionário de Competências.**  
   
Competência: Desenvolvimento de Pessoas  
Tipo: Comportamental  
Sem itens de performance relacionados.  
   
Competência: Análise e Solução de Problemas  
Tipo: Comportamental  
Itens de Performance:  
                Trabalha com metodologia e desenvolve soluções permanentes – **peso padrão = 3**  
                Resolve vários problemas ao mesmo tempo organizando-se em função de prioridades e cumprimento de prazos – **peso padrão = 4**  
   
Competência: Busca por Realização  
Tipo: Comportamental  
Itens de Performance:  
                Atinge resultados com qualidade – **peso padrão = 3**  
                Identifica necessidade de melhorias e modifica métodos de trabalho – **peso padrão = 5**  
   
**Observação**:

Considera somente os Itens de Performance ativos.

**2) Verificar quem serão os avaliados na Avaliação de Desempenho. Neste exemplo, vamos considerar os funcionários que tenham a função "Gerente Administrativo e Financeiro".**

**No exemplo, apenas um funcionário.**  
   
**3) Definição das competências - Vínculo "Função" - Gerente Administrativo e Financeiro: Acompanhamento| Mapa de Conhecimento| Definição por Competências.**  
   
Tipo de Vínculo: Função  
   
Competência: Desenvolvimento de Pessoas  
Graduação: Aplicação   
Tipo: Exigido   
   
Competência: Análise e Solução de Problemas  
Graduação: Especialização   
Tipo: Exigido   
   
Competência: Busca por Realização  
Graduação: Compreensão   
Tipo: Desejado   
   
**Observação**:  
Graduação das competências  
00001    Consciência  
00002    Compreensão  
00003    Aplicação  
00004    Especialização  
00005    Domínio  
   
**4) Criação das metas a serem consideradas na Avaliação de Desempenho: Acompanhamento| Gestão de Metas.**  
   
Criação da Meta Agrupadora e Meta Valor, sendo que na composição da meta Agrupadora = 100% da meta Valor.  
   
**5) Criação da Avaliação de Desempenho: Acompanhamento| Avaliações de Desempenho.**  
   
Itens a avaliar:  
Competências Comportamentais  
Metas  
   
Considerar Competências por: Função  
   
**6) Respondendo a Avaliação de Desempenho: Totvs Portal| Recursos Humanos| Gestão por Competências| Avaliação de Desempenho.**  
   
Competência: Desenvolvimento de Pessoas – Supera   
Competência: Análise e Solução de Problemas – Atende Parcialmente   
Competência: Busca por Realização – Supera   
Meta – Atende Parcialmente   
   
**Observação**:  
Escala de Avaliação  
1 - Não Atende    
2 - Atende Parcialmente   
3 - Atende           
4 - Supera                        (Ponto de Corte)  
5 - Supera com excelência           
   
O ponto de corte pode ser definido de acordo com a necessidade do cliente.  
   
**7) Cálculo da Avaliação de Desempenho**  
   
- Cálculo da nota obtida em cada Competência:  
   
Peso do Item de Performance x Valor da Nota obtida na Avaliação / Soma dos pesos dos itens de performance

|  |
| --- |
| Fórmula: **NC = (pIP1 \* VN1) + (pIP2 \* VN2) + ...(pIPn \* VNn)+** |
| **(pIP1 + pIP2 + ...+pIPn)** |

Onde,  
NC = Nota da Competência  
pIP = Peso do Item de Performance  
VN = Valor da Nota Obtida na Avaliação  
   
   
Desenvolvimento de Pessoas  
(1x 4)/1 = **4**  
   
Análise e Solução de Problemas  
Trabalha com metodologia e desenvolve soluções permanentes – peso padrão = 3  
            Resolve vários problemas ao mesmo tempo organizando-se em função de prioridades e cumprimento de prazos – peso padrão = 4  
(3x 2) + (4 x 2)/ (3+ 4) = 6 + 8 / 7 = **2**  
   
Busca por Realização  
Atinge resultados com qualidade – peso padrão = 3  
            Identifica necessidade de melhorias e modifica métodos de trabalho – peso padrão = 5  
(3x 4) + (5x 4)/ (3+ 5) = 12 + 20/ 8 = **4**  
   
Meta  
(1x 2)/ 1 = **2**  
   
- Cálculo da nota obtida na Avaliação:  
   
Soma das notas das competências / Número de competências  
   
(4 + 2 + 4)/ 3 = 10 / 3 = **3,33**  
   
**Atenção**:  
No cálculo citado foi encontrado o valor 3,33, a NC seria 3,0 ao invés de 4,0, pois 3,33 está entre 3,0 e 4,0.  
   
- Caso o parâmetro ' *Não arredondar as notas das competências para o calculo da nota geral no portal* ' esteja marcado, a nota considera para o calculo será sem arredondamento.  
Como ficaria o exemplo acima:  
(4 + 2 + 4)/ 3 = 10 / 3 = **3,33**  
   
**8) Fechar avaliação de desempenho: Acompanhamento| Avaliações de Desempenho| Processos| Fechar avaliação de desempenho.**  
   
Para finalizar as avaliações no caso de quando existem mais de um avaliador é necessario fazer o calculo para determinar a nota final da competência.   
- Cálculo da nota obtida em cada Competência:

|  |
| --- |
| Fórmula: **NCT = (pA1 \* NAC1) + (pA2 \* NAC2) + ...(pAn \* NACn)+** |
| **(pA1 + pA2 + ...+pAn)** |

Onde,  
NCT = Nota da Competência Total  
pA = Peso do Avaliador  
NAC = Valor da Nota Dada pelo Avaliador na Competência  
   
Desenvolvimento de Pessoas  
Avaliador1 deu nota **3** e ele possui peso **10**.  
Avaliador2 deu nota **2** e ele possui peso **20**.  
   
((10 x 3) + (20 x 2))/ (10 + 20) = (30 + 40)/ 30 = **2,33**  
   
Assim a nota final seria **2,33**.  
   
   
Avaliação finalizada.  
Funcionário recebe as seguintes competências:  
Desenvolvimento de Pessoas – Graduação: Aplicação  
Análise e Solução de Problemas – Graduação: Consciência  
Busca por Realização – Graduação: Compreensão  
   
Respeitando as seguintes regras:  
   
- **Nota obtida corresponde ao ponto de corte:**

Se o funcionário possuir a competência, a graduação será alterada para a graduação da definição do Mapa de Conhecimento;  
Se o funcionário não possuir a competência, será concedida a competência na graduação da definição do Mapa de Conhecimento.

- **Nota obtida está acima do ponto de corte:**

Se o funcionário possuir a competência numa graduação abaixo da graduação exigida / desejada, a graduação do funcionário será elevada para o nível da graduação da definição do Mapa de Conhecimento;   
Se o funcionário possuir a competência na mesma graduação exigida / desejada, a graduação do funcionário será elevada em um nível;   
Se o funcionário possuir a competência numa graduação acima da graduação exigida / desejada, nada será feito;  
Se o funcionário não possuir a competência, será concedida a competência na graduação da definição do Mapa de Conhecimento.   
   
- **Nota obtida está abaixo do ponto de corte:**

Se o funcionário possuir a competência numa graduação abaixo da graduação exigida / desejada, nada será feito;   
Se o funcionário possuir a competência na mesma graduação ou acima da exigida / desejada, a graduação do funcionário é reduzida um nível da graduação abaixo da graduação atual do funcionário;  
Se o funcionário não possuir a competência, será concedida a competência na graduação mínima.  
   
**Observação:**

Se o parâmetro "Atualizar competências de acordo com a graduação definida na escala" estiver marcado, as regras acima mudam e são consideradas as graduações definidas diretamente na escala.  
   
**9) Geração dos gráficos da Avaliação de Desempenho: Acompanhamento| Avaliações de Desempenho| Anexos| Gráficos.**  
   
Como achar os valores apresentados nos gráficos?  
   
A cada competência, meta e fator organizacional avaliados dentro de uma avaliação de desempenho por competência, deve-se aplicar as fórmulas abaixo, após aplicação das fórmulas, deve-se somar os valores obtidos em cada um desses, essa soma será o resultado apontado no gráfico.   
   
Neste exemplo, a comparação no gráfico é "Função x Funcionário".  
   
**- GRÁFICO COMPARATIVO DE NOTAS:**  
   
**Nota Obtida:**

Fórmula: NOA = NA\* PA onde:

NOA = Nota Obtida na Avaliação

NA = Nota Avaliada

PA = Peso definido na Avaliação  
   
**Nota obtida - Funcionário:**

|  |  |  |
| --- | --- | --- |
| **Item Avaliado** | **Nota Avaliada** | **Peso definido na Avaliação** |
| Desenvolvimento de Pessoas | 4 | 1 |
| Análise e Solução de Problemas | 2 | 1 |
| Busca por Realização | 4 | 1 |
| Meta | 2 | 1 |

NOA = (4 x 1) + (2 x 1) + (4 x 1) + (2 x 1) = 4 + 2 + 4 + 2 = 12 NOA = 12  
   
**Nota obtida - Função:**

|  |  |  |
| --- | --- | --- |
| **Item Avaliado** | **Nota Avaliada** | **Peso definido na Avaliação** |
| Desenvolvimento de Pessoas | 4 | 1 |
| Análise e Solução de Problemas | 2 | 1 |
| Trabalha com metodologia e desenvolve soluções permanentes | 2 | 3 |
| Resolve vários problemas ao mesmo tempo organizando-se em função de prioridades e cumprimento de prazos | 2 | 4 |
| Busca por Realização | 4 | 1 |
| Atinge resultados com qualidade | 4 | 3 |
| Identifica necessidade de melhorias e modifica métodos de trabalho | 4 | 5 |
| Meta | 2 | 1 |

   
NOA = (4 x 1) + (2 x 1) + (2 x 3) + (2 x 4) + (4 x 1) + (4 x 3) + (4 x 5) + (2 x 1)

= 4 + 2 + 6 + 8 + 4 + 12 + 20 + 2 = 58

NOA = 58   
   
**Nota Máxima Possível:**

Fórmula: NMA = MN \* PA onde:

NMA = Nota Máxima na Avaliação

MN = Maior nota possível da escala

PA = Peso definido na Avaliação  
   
**Nota máxima possível - Funcionário:**

|  |  |  |
| --- | --- | --- |
| **Item Avaliado** | **Maior nota possível da escala** | **Peso definido na Avaliação** |
| Desenvolvimento de Pessoas | 5 | 1 |
| Análise e Solução de Problemas | 5 | 1 |
| Busca por Realização | 5 | 1 |
| Meta | 5 | 1 |

   
NMA  = (5 x 1) + (5 x 1) + (5 x 1) + (5 x 1)

= 5 + 5 + 5 + 5 = 20

NMA = 20  
   
**Nota máxima possível - Função:**

|  |  |  |
| --- | --- | --- |
| **Item Avaliado** | **Maior nota possível da escala** | **Peso definido na Avaliação** |
| Desenvolvimento de Pessoas | 5 | 1 |
| Análise e Solução de Problemas | 5 | 1 |
| Trabalha com metodologia e desenvolve soluções permanentes | 5 | 3 |
| Resolve vários problemas ao mesmo tempo organizando-se em função de prioridades e cumprimento de prazos | 5 | 4 |
| Busca por Realização | 5 | 1 |
| Atinge resultados com qualidade | 5 | 3 |
| Identifica necessidade de melhorias e modifica métodos de trabalho | 5 | 5 |
| Meta | 5 | 1 |

   
NMA = (5 x 1) + (5 x 1) + (5 x 3) + (5 x 4) + (5 x 1) + (5 x 3) + (5 x 5) + (5 x 1)

= 5 + 5 + 15 + 20 + 5 + 15 + 25 + 5 = 95

NMA = 95   
   
**Aproveitamento (%):**

Fórmula: PERCENT = (NOA / NMA)\*100 onde:

PERCENT = Percentual de Aproveitamento

NOA = Nota Obtida na Avaliação

NMA = Nota Máxima na Avaliação  
   
**Funcionário**: 12 / 20 \* 100 = 60% **Função**: 58 / 95 \* 100 = 61,05%  
   
**- GRÁFICO DO PERCENTUAL DE APROVEITAMENTO:**  
   
**Nota Obtida:**

Fórmula: NO = NOA\* PIF onde:

NO = Nota Obtida NOA = Nota obtida na Avaliação

PIF = Peso do Item na Função (Definição de competência)  
   
**Nota obtida - Funcionário:**

|  |  |  |
| --- | --- | --- |
| **Item Avaliado** | **Nota obtida na Avaliação** | **Peso do Item na Função** |
| Desenvolvimento de Pessoas | 4 | 3 |
| Análise e Solução de Problemas | 2 | 4 |
| Busca por Realização | 4 | 2 |
| Meta | 2 | 1 |

NO = (4 x 3) + (2 x 4) + (4 x 2) + (2 x 1)

= 12 + 8 + 8 + 2 = 30

NO = 30  
   
**Nota obtida - Função:**

|  |  |  |
| --- | --- | --- |
| **Item Avaliado** | **Nota obtida na Avaliação** | **Peso do Item na Função** |
| Desenvolvimento de Pessoas | 4 | 3 |
| Análise e Solução de Problemas | 2 | 4 |
| Trabalha com metodologia e desenvolve soluções permanentes | 2 | 3 |
| Resolve vários problemas ao mesmo tempo organizando-se em função de prioridades e cumprimento de prazos | 2 | 4 |
| Busca por Realização | 4 | 2 |
| Atinge resultados com qualidade | 4 | 3 |
| Identifica necessidade de melhorias e modifica métodos de trabalho | 4 | 5 |
| Meta | 2 | 1 |

NO = (4 x 3) + (2 x 4) + (2 x 3) + (2 x 4) + (4 x 2) + (4 x 3) + (4 x 5) + (2 x 1)

= 12 + 8 + 6 + 8 + 8 + 12 + 20 + 2 = 76

NO = 76  
   
**Nota Máxima Possível:**

Fórmula: NM = NMA \* PIF onde:

NM = Nota Máxima

NMA = Nota Máxima na Avaliação

PA = Peso do Item na Função

**Nota máxima possível - Funcionário:**

|  |  |  |
| --- | --- | --- |
| **Item Avaliado** | **Nota Máxima na Avaliação** | **Peso do Item na Função** |
| Desenvolvimento de Pessoas | 5 | 3 |
| Análise e Solução de Problemas | 5 | 4 |
| Busca por Realização | 5 | 2 |
| Meta | 5 | 1 |

NM  = (5 x 3) + (5 x 4) + (5 x 2) + (5 x 1)

= 15 + 20 + 10 + 5 = 50

NM = 50  
   
**Nota máxima possível - Função:**

|  |  |  |
| --- | --- | --- |
| **Item Avaliado** | **Nota Máxima na Avaliação** | **Peso do Item na Função** |
| Desenvolvimento de Pessoas | 5 | 3 |
| Análise e Solução de Problemas | 5 | 4 |
| Trabalha com metodologia e desenvolve soluções permanentes | 5 | 3 |
| Resolve vários problemas ao mesmo tempo organizando-se em função de prioridades e cumprimento de prazos | 5 | 4 |
| Busca por Realização | 5 | 2 |
| Atinge resultados com qualidade | 5 | 3 |
| Identifica necessidade de melhorias e modifica métodos de trabalho | 5 | 5 |
| Meta | 5 | 1 |

NM = (5 x 3) + (5 x 4) + (5 x 3) + (5 x 4) + (5 x 2) + (5 x 3) + (5 x 5) + (5 x 1)

= 15 + 20 + 15 + 20 + 10 + 15 + 25 + 5 = 125

NM = 125  
   
**Aproveitamento (%):**

Fórmula: PERCENT = (NO / NM)\*100 onde:

PERCENT = Percentual de Aproveitamento

NO = Nota Obtida

NM = Nota Máxima  
   
**Funcionário**: 30 / 50 \* 100 = 60%

**Função**: 76 / 125 \* 100 = 60,8%  
   
**- QUADRANTE: POTENCIAL X RESULTADO**  
   
**Nota Resultado:**

Fórmula: Nota obtida na Avaliação \* 100 / Nota máxima na Avaliação  
   
**Nota Potencial – Funcionário e Função**

|  |  |  |
| --- | --- | --- |
| **Metas** | **Nota obtida na Avaliação** | **Nota Máxima na Avaliação** |
| Meta | 2 | 5 |

2 \* 100 / 5 = 40% Nota Resultado = 40%

**Nota Potencial:** Fórmula: Nota obtida na Avaliação \* 100 / Nota máxima na Avaliação  
   
**Nota Potencial – Funcionário e Função**

|  |  |  |
| --- | --- | --- |
| **Competência** | **Nota obtida na Avaliação** | **Nota Máxima na Avaliação** |
| Desenvolvimento de Pessoas | 4 | 5 |
| Análise e Solução de Problemas | 2 | 5 |
| Busca por Realização | 4 | 5 |

   
(4 + 2 + 4) \* 100 / (5 + 5 + 5) 10 \* 100 / 15 

= 66,6 %

Nota Potencial = 66,6%
