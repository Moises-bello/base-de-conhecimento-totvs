---
content_hash: a5ea452fee372978ac1fbf0e40956db311c040475d0bf80b7210114ba6b4b359
fetched_at: '2026-06-29T00:09:14.939375+00:00'
page_id: '421385308'
product: rm
source: tdn-rm
title: Curva ABC de Insumos
type: documentation
url: https://tdn.totvs.com/display/LRM/Curva+ABC+de+Insumos
version: 7
---

**Curva ABC de Insumos**  
Através da Curva de isumos, consulta-se a previsão do gasto de cada insumo, de acordo com a quantidade, informando qual o percentual do valor deste insumo em relação ao valor total do projeto. As quantidades e os valores improdutivos dos insumos também serão mostrados. O relatório pode ser visualizado e impresso com os totais das colunas, bem como seu gráfico.   
As colunas Custo Unitário e Custo Total foram adicionadas a curva ABC de insumos.  
A coluna Custo unitário traz o preço do insumo , livre das incidências de taxas (BDI, Fator K, etc).  
A coluna Custo Total traz a soma do custo unitário daquele insumo incidente em todas as tarefas.

**Exemplo:**  
Coluna custo Total: O preço do insumo x é 150,00.  
Insumo X esta sendo utilizado na planilha em duas tarefas, ao calcular a curva ABC do insumo o valor do campo Custo Total será de 300,00  
   
A quantidade dos insumos do grupo DNIT A (Equipamentos) e B (Mão-de-obra) é dividida pela produção da equipe das composições que pertencem. Isso é feito para cada composição por produção, depois a quantidade é totalizada;  
A quantidade do insumo do grupo DNIT F (Transporte) é multiplicada pelo DMT da composição a que pertence. Isso é feito para cada composição por produção, depois a quantidade é totalizada.  
Colunas da Curva ABC de Insumos.

·          **Código:** Código do insumo.  
·          **Descrição:** Descrição do insumo.  
·          **Valor (valor produtivo):** traz o valor do insumo referente a todas as incidências do insumo.   
·          **Valor Improdutivo:** traz o valor improdutivo do insumo referente a todas as incidências do insumo.   
·          **Valor unitário**: é obtida através da divisão do conteúdo da coluna Valor pelo conteúdo da coluna Quantidade.  
·          **Quantidade:** quantidade referente a todas as incidências do insumo.   
·          **Qtd. Improdutiva:** quantidade improdutiva referente a todas as incidências do insumo.   
·          **Custo (custo produtivo):** soma do custo unitário daquele insumo incidente em todas as tarefas.   
·          **Custo unitário:** custo médio do unitário do insumo. Este valor é obtido por: Custo/ Quantidade.  
·          **Custo improdutivo:** soma do custo unitário improdutivo daquele insumo incidente em todas as tarefas.  
·          **Custo unitário improdutivo:** custo médio do unitário improdutivo do insumo. Este valor é obtido por: Custo Improdutivo/ Quantidade Improdutiva  
·          **%:** percentual do insumo referente a todos os insumos do projeto  
·          **% Acum.:** Armazena o somatório dos valores da coluna %.

Atenção: Se o parâmetro de projeto **Utilizar preço unitário do insumo na Curva ABC (F6)** estiver desmarcado ele irá utilizar Custo/Quantidade no campo Custo unitário na Curva ABC.

**Observação:** Os campos Custo Unitário e Custo Unitário Improdutivo serão informados quando o Insumo estiver associado a uma Composição por Produção, onde deve ser informado os Coeficientes Produtivo e Improdutivo.  
O quadro abaixo apresenta quais os fatores são aplicados nas grandezas listadas na primeira coluna, seguindo as condições listadas abaixo, de acordo com as colunas apresentadas na Curva ABC de Insumos.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | **Leis Sociais** | **BDI Proj** | **BDI Dif.** | **BDI**  **G. Custo** | **FatoK Cmp** | **FatorK Ism** | **DMT** | **Produção** | **Quant Obra** | **Quant**  **Tarefa** | **Quan**  **Cmp** | **Quant**  **Rec (Ism)** | **Coef Prod** | **Coef Imp** |
| **Valor** | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Não |
| **Valor Improd.** | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Não | Sim |
| **Quant.** | Não | Não | Não | Não | Não | Não | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Não |
| **Quant. Improd.** | Não | Não | Não | Não | Não | Não | Sim | Sim | Sim | Sim | Sim | Sim | Não | Sim |
| **Custo** | Sim | Não | Não | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Não |
| **Custo Improd.** | Sim | Não | Não | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Sim | Não | Sim |

·          Leis Sociais incidirá se for parametrizada para ser aplicada sobre o custo unitário.  
·          O BDI do projeto não é aplicado nos recursos associados a tarefas de custo indireto.  
·          O BDI do grupo de custo não é aplicado sobre o preço improdutivo do insumo.  
·          Para o fator k ser aplicado o parâmetro utiliza Fator k da Curva ABC de Insumos precisa estar selecionado.  
·          O Fator k de insumos só será aplicado quando o mesmo for recurso de uma composição, conforme parametrizado.  
·          Para aplicar DMT o recurso precisa ser do Grupo de custo transporte e ser recurso de uma composição por produção  
·          A produção somente é aplicada em recursos do tipo equipamento ou mão de obra que sejam recursos de uma composição por produção.  
·          Quantidade da composição somente se aplica se o insumo estiver associado a uma composição.

·          Se a composição no qual o insumo está associado for do tipo Turma Típica e por sua vez, esta, estando associada a uma composição do tipo Por Unidade de Serviço, o valor do Standard desta última, será multiplicado a quantidade que irá influenciar na quantidade utilizada do insumo.  
·          Os coeficientes somente serão aplicados em recursos do tipo equipamento que forem recursos de uma composição por produção caso contrário o coeficiente produtivo será 1 e o improdutivo 0.  
·         A coluna Valor Unitário do Insumo deve ser utilizada com cuidado, pois traz o valor do insumo considerando a lei social (se a mesma estiver sendo aplicada sobre o custo unitário) e o bdi do grupo de custo, bdi do projeto e Fator K do insumo.   
·         O fator k da composição é considerado somente no cálculo dos insumos percentuais. Portanto, não recomendamos conferências do campo Valor do insumo na curva abc multiplicando-se o preço unitário pela quantidade.

**Detalhamento de cálculos de grandezas improdutivas**

* **Quantidade Improdutiva**

Considere as seguintes variáveis:

**Improd\_Insumo** = Percentual de Improdutividade do Insumo;

**Qtde\_Improd** = Quantidade Improdutiva;

**Qtde\_Improd\_Calculada** = Quantidade Improdutiva Calculada;

**Qtde\_Recurso** = Quantidade do Recurso da Composição;

**Coef\_Improd** = Coeficiente Improdutivo;

**Qtde\_Tarefa** = Quantidade da Tarefa;

**Qtde\_Obra** = Quantidade da Obra;

**Producao\_Composicao** = Produção por Hora da Composição;

**Transporte** = Considera os DMT’s no caso de Recurso do tipo Momento de Transporte.

**1) Composição por Produção**

O cálculo da Quantidade Improdutiva é realizado da seguinte maneira:

Se **Improd\_Insumo** for maior que Zero, então o mesmo é aplicado à **Qtde\_Recurso**:

Qtde\_Improd = Qtde\_Recurso X (Improd\_Insumo / 100)

Em seguida é realizado o cálculo da Quantidade Improdutiva Calculada, da seguinte maneira:

Se existir Coeficiente Improdutivo para o Recurso, então o mesmo é aplicado ao cálculo:

         Qtde\_Improd\_Calculada = Qtde\_Recurso + Qtde\_Improd

         Qtde\_Improd\_Calculada = Qtde\_Improd\_Calculada X Coef\_Improd

Em seguida é aplicado à Quantidade Improdutiva Calculada as demais variáveis, da seguinte forma:

Qtde\_Improd\_Calculada = Qtde\_Improd\_Calculada X Qtde\_Tarefa X Qtde\_Obra X Transporte

Qtde\_Improd\_Calculada = Qtde\_Improd\_Calculada / Producao\_Composicao

Ao final, se a Quantidade Improdutiva Calculada for maior que Zero a Quantidade Improdutiva assume seu valor:

                Sendo Qtde\_Improd\_Calculada maior que Zero, então **Qtde\_Improd = Qtde\_Improd\_Calculada**

**2) Demais tipos de Composição**

A Quantidade Improdutiva assume o seguinte cálculo:

Se **Improd\_Insumo** for maior que Zero, então o mesmo é aplicado à **Qtdee\_Recurso**:

                                Qtde\_Improd = Qtde\_Recurso X (Improd\_Insumo / 100)

* **Valor Improdutivo e Custo Unitário Improdutivo**

Considere as seguintes variáveis:

**Valor\_Improd\_Insumo** = Valor Improdutivo do Insumo;

**Valor\_Prod\_Insumo** = Valor Produtivo do Insumo;

**Valor\_Improd\_Calculado** = Valor Improdutivo Calculado;

**Custo\_Improd\_Insumo** = Custo Improdutivo do Insumo;

**Custo\_Improd\_Insumo\_Calculado** = Custo Improdutivo Calculado;

**Qtde\_Recurso** = Quantidade do Recurso da Composição;

**Coef\_Improd** = Coeficiente Improdutivo;

**Qtde\_Tarefa** = Quantidade da Tarefa;

**Qtde\_Obra** = Quantidade da Obra;

**Producao\_Composicao** = Produção por Hora da Composição;

**Transporte** = Considera os DMT’s no caso de Recurso do tipo Momento de Transporte;

**FatorK\_Insumo** = Fator K Insumo;

**FatorK\_Composição** = Fator K Composição;

**BDI\_Projeto** = BDI do Projeto;

**BDI\_Dif** = BDI Diferenciado.

**Valor\_Improdutivo\_Final** = Valor Improdutivo Final do Insumo

**Custo\_Improdutivo\_Final** = Valor Improdutivo Final do Insumo

Se a vigência utilizada no projeto é considerada em Todo o Projeto, os **Valor\_Prod\_Insumo** e **Valor\_Improd\_Insumo** são definidos da seguinte forma:

                Se é recurso do tipo Percentual:

                                Valor\_Prod\_Insumo = Valor Unitário Médio por Tarefa / Fator K Composição

                Se não é recurso do tipo Percentual:

                               Valor\_Prod\_Insumo = Valor Unitário Médio por Tarefa

                Se é recurso do tipo Equipamento em composição por produção:

                               Valor\_Improd\_Insumo = Valor Unitário Improdutivo Médio por Tarefa

                Se não é recurso do tipo Equipamento e nem composição por produção:

                               Valor\_Improd\_Insumo = Valor\_Improd\_Insumo

**1) Composição por Produção**

O cálculo do Valor Improdutivo e Custo Unitário Improdutivo é realizado da seguinte maneira:

É realizado o cálculo do Valor Improdutivo Calculado, da seguinte maneira:

Se existir Coeficiente Improdutivo para o Recurso, então o mesmo é aplicado ao cálculo:

Valor\_Improd\_Calculado = Valor\_Improd\_Insumo

                Valor\_Improd\_Calculado = Valor\_Improd\_Calculado X Coef\_Improd

Se não existir Coeficiente Improdutivo para o Recurso:

                Valor\_Improd\_Calculado = 0

Nesse momento o Custo Improdutivo Calculado assume o Valor Improdutivo Calculado

Custo\_Improd\_Insumo\_Calculado = Valor\_Improd\_Calculado

Em seguida é aplicado ao Valor Improdutivo Calculado as demais variáveis, da seguinte forma:

Valor\_Improd\_Calculado = Valor\_Improd\_Calculado X Qtde\_Recurso X FatorK\_Insumo X FatorK\_Composicao  X Transporte

Valor\_Improd\_Calculado = Valor\_Improd\_Calculado / Producao\_Composicao

Valor\_Improd\_Calculado = Valor\_Improd\_Calculado X Qtde\_Tarefa X Qtde\_Obra

Valor\_Improd\_Calculado = Valor\_Improd\_Calculado X BDI\_Projeto X BDI\_Dif

Ao final, se o Valor Improdutivo Calculado for maior que Zero o Valor Improdutivo Final assume seu valor:

                Valor\_Improdutivo\_Final **=** Valor\_Improd\_Calculado

Se o Valor Improdutivo Calculado for igual a Zero o Valor Improdutivo Final assume o seguinte cálculo:

Valor\_Improdutivo\_Final  = Valor Unitário Recurso X Quantidade Improdutiva

                Para o cálculo do Custo Improdutivo Calculado as seguintes regras são consideradas:

                               Se a vigência utilizada no projeto é considerada em Todo o Projeto, então:

                Custo\_Improd\_Insumo\_Calculado = Custo\_Improd\_Insumo\_Calculado / BDI\_Dif

Se NÃO aplica BDI no total do projeto então

Custo\_Improd\_Insumo\_Calculado = Custo\_Improd\_Insumo\_Calculado / BDI\_Projeto

                Em seguida é aplicado ao Custo Improdutivo Calculado as demais variáveis, da seguinte forma:

Custo\_Improd\_Insumo\_Calculado = Custo\_Improd\_Insumo\_Calculado X Qtde\_Recurso X FatorK\_Insumo X FatorK\_Composicao  X Transporte

Custo\_Improd\_Insumo\_Calculado = Custo\_Improd\_Insumo\_Calculado / Producao\_Composicao

Custo\_Improd\_Insumo\_Calculado = Custo\_Improd\_Insumo\_Calculado X Qtde\_Tarefa X Qtde\_Obra

Custo\_Improd\_Insumo\_Calculado = Valor\_Improd\_Calculado X BDI\_Projeto X BDI\_Dif

                        Por fim o Custo Improdutivo Final assume o valor do calculado e o Custo Unitário Improdutivo também é definido:

                               Custo\_Improdutivo\_Final = Custo\_Improd\_Insumo\_Calculado

                               Custo Unitário Improdutivo = Custo\_Improdutivo\_Final / Quantidade Improdutiva

**2) Demais tipos de Composição**

O Valor Improdutivo Final assume o seguinte cálculo:

       Valor\_Improdutivo\_Final  = Valor Unitário Recurso X Quantidade Improdutiva

       O Custo Improdutivo Final assume o valor Zero.
