---
content_hash: c1704e8651712b621be559e73df21531e9c8acc959b880a008d222537d696187
fetched_at: '2026-06-29T00:09:49.639606+00:00'
page_id: '435105333'
product: rm
source: tdn-rm
title: Modelos de cálculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105333
version: 79
---

**Modelos de cálculos**

---

Os Modelos de Cálculos são cadastrados nos Componentes ( somente nos componentes que tenham o seu Tipo de Componente = Principal ), em uma Modalidade de Venda.  
Estes Modelos de Cálculos servem para especificar como será o cálculo do valor das parcelas de uma venda.  
   
Em todos os Modelos de Cálculos, o sistema irá levar em consideração a parametrização dos componentes da Modalidade de Venda utilizada.  
Os parâmetros são:  
Tipo de Componente, Tipo de Parcela, Surgimento do Componente (Na geração do Plano de Retorno, Na Valorização), Ação do Componente (Antes da Entrega, Após a entrega, Ambos), Valor opcional do Fluxus e Componente compõe valor base para cálculo de (Reajuste de Juros de Contrato, Reajuste de Correção Monetária)  
   
No sistema SGI, existem 6 Modelos de Cálculos. Cada modelo trabalha de sua forma específica e com seus devidos parâmetros. São eles:  
   
**1 - Modelo Padrão**   
   
**2 - Tabela Price**   
   
**3 - Juros Mensal**   
    
**4 - Tabela SAC**  
   
**5 - Tabela SACRE**  
   
**6 - Minha Casa Minha Vida**  
   
   
**1 - Modelo Padrão:**  
   
**Geração do Plano:**  
   
A geração do Plano no Modelo Padrão se dá através da divisão do valor total do financiamento pelo número de parcelas de cada componente do tipo principal. Não há nenhum cálculo para inserir reajustes financeiros.  
   
**Reajuste Financeiro:**  
   
As vendas sofrem reajustes financeiros (através do processo de reajuste) de acordo com a periodicidade dos componentes de reajustes.  
   
**Reajuste do Juros**   
   
• Juros (%) – Percentual do juros que representará o valor da parcela.  
• Periodicidade – Prazo para que o reajuste seja realizado  
• Juros acumulado pela periodicidade – Utilizará o valor da periodicidade para o cálculo do ;juros.  
• Data do próximo reajuste – Definirá a data do reajuste com as regras estabelecidas no componente. Será preenchido no momento da efetivação da venda desde que seu valor seja nulo. Para os componentes que reajustam as parcelas antes da entrega, esta data de próximo reajuste receberá o valor nulo quando o mesmo for após a data de entrega do empreendimento.   
   
**Tipo de Juros:**  
   
**Juros Acumulado:**   
Para ocorrer juros acumulado, a periodicidade tem que ser maior que 1.  
Simples : Utiliza a fórmula : (( PERIODO \* VALOR ) \* PERIODICIDADE )  
Composto : Utiliza a fórmula : ((((VALOR / 100) + 1)^ PERIODICIDADE) – 1) \* 100  
Por exemplo : Se a taxa de juros for de 1% para um reajuste anual será calculado um juros de 12% para simples e 12,68% para composto.   
   
  **Juros não Acumulado**   
Simples : Utiliza a fórmula : (PERIODO \* VALOR )  
Composto : Utiliza a fórmula : ((((VALOR / 100) + 1)^ PERIODO) – 1) \* 100  
   
   
**Ação do reajuste de juros**   
   
O reajuste do juros de contrato poderá ser realizado :  
   
Juros Simples:  
                      - Sobre o Valor original das Parcelas

* Sobre o Valor original das Parcelas mais a CM até o mês anterior
* Sobre o Valor original das Parcelas mais a CM do mês do reajuste  
     
  Juros Compostos:  
                        - Sobre o Valor original das Parcelas
* Sobre o Valor original das Parcelas mais a CM até o mês anterior
* Sobre o Valor original das Parcelas mais a CM do mês do reajuste  
     
     
  **Correção Monetária**   
     
  • Moeda – Símbolo utilizado para reajustar a parcela  
  • Coeficiente – Será acrescido a variação da moeda. Sua representação será em valor. Exemplo : 1% - 1,01; 5% - 1,05

  Importante: Alerta
  + Ao utilizar componentes antes e após a entrega para um grupo de uma venda na data deverá sempre observar a defasagem "Meses de defasagem" descrita a seguir.  
    O sistema se comporta efetuando as cargas de todos os índices utilizados no cálculo, ainda que não serão utilizados, por exemplo: na "Correção Monetária Após a Entrega", o sistema irá exigir que já tenha o índice cadastrado para a utilização do calculo do "Coeficiente", no momento de efetuar o cálculo será decidido se já foi entregue ou não a subunidade, de acordo com as definições efetuadas no sistema. Assim, o Coeficiente poderá ser utilizado ou não.  
    *Exemplo:* Empreendimento com entrega em 30/07/2010, com CM Antes (IGPM) com Defasagem '0' e CM Após (IPCA) com Defasagem '0', Data Inicio do Reajuste 01/03/2010.   
    Ao efetuar o reajuste para o mês 07/2010 o empreendimento é considerado não entregue. Contudo, o sistema irá buscar o índice do CM Após (IPCA) para a data de 01/06/2010 de acordo a defasagem informada de '0' para efetuar a carga de cálculo para o "Coeficiente". Mas no log do cálculo do reajuste poderá ser observado que não foi calculado nenhum valor para o CM Após (IPCA) como demonstrado:

    ------**Log exemplo de reajuste** -------  
    *Reajuste de "Correção Monetária" [CM Apos Entrega]:*

    *Moeda: IPCA*  
    *Tipo de Moeda: Índice*  
    *Data Base: 01/03/2010 00:00:00*  
    *Data do Reajuste: 01/07/2010 00:00:00*  
    *Data Entrega: 30/07/2010*  
    *Data de Vencime15/08/2010*  
    *Reajustar até dia vencimento: Não*  
    *Data Inicial: 30/07/2010*  
    *Data Final: 01/07/2010*

    *0 (Variação Final) \* R$0,00 (Valor Base) = R$0,00 (Correção Monetária)*

  • Meses de defasagem – Quantidade de meses que será decrescido da data base para se achar o índice de reajuste.

  Importante: Alerta
  + Modelo Padrão - é sempre acrescido a soma de 1 a defasagem informada no componente de "Correção Monetária"  
    Exemplo: usuário cadastrou componente "Correção Monetária Antes da Entrega" e informou no campo "Defasagem" o valor de 0, o sistema irá buscar o índice de um mês antes.   
    - *Data Reajuste:*01/05/2018  
    - *Defasagem informada no componente:* 0  
    - *Defasagem utilizada pelo sistema :*1  
    - *Índice a ser utilizado no cálculo:* 01/04/2018

  • Periodicidade – Prazo para que o reajuste seja realizado  
  • Data do próximo reajuste – Definirá a data do reajuste com as regras estabelecidas no componente. Será preenchido no momento da efetivação da venda desde que seu valor seja nulo. Para os componentes que reajustam as parcelas antes da entrega, esta data de próximo reajuste receberá o valor nulo quando o mesmo for após a data de entrega do empreendimento.   
  • Correção monetária acumulada no prazo do reajuste – O índice de reajuste será calculado a partir da data base até o momento do reajuste utilizando a seguinte fórmula : COTACAOACUMULADA \* COTACAOMENSAL (Quando o reajuste é anual e o mesmo é acumulado deverá ser analisado que até a entrega do empreendimento utilizará o reajuste acumulado da moeda antes da entrega).  
  • Correção monetária não capitalizada – reajustará a parcela partindo sempre do valor original.  
  • Correção monetária capitalizada – reajustará a parcela partindo do valor acumulado dos reajustes anteriores da parcela.  
  O cálculo da Correção Monetária capitalizada ocorre da seguinte maneira:  
  (Índice correção anterior – 1) \* (índice correção atual – 1) \* (parcela original + juros)   
     
  **Ação do reajuste da correção monetária**   
     
  O reajuste da correção monetária poderá ser realizada :  
              - Sobre o Valor original das Parcelas
* Sobre o Valor original das Parcelas mais os Juros até o mês anterior
* Sobre o Valor original das Parcelas mais os Juros do mês do reajuste  
     
  Para realizar o cálculo da Correção Monetária no Modelo Padrão, pode ser parametrizado a data de reajuste de referência para fazer o cálculo da correção.  
     
  **Exemplo:**  
  Cliente "XYZ" comprou um lote na da 01/11/2001, no valor de R$ 10.000,00, para pagar em 5 parcelas, a uma taxa de juros simples 3% a.m. com correção monetária mensal e 1 mês de defasagem.

  |  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | Parcela | Data | Cotação | Índice | Valor Original | Correção | Juros | Valor Total |
  | - | 1/9/2001 | 210.853 | - | - | - | - | - |
  | - | 1/10/2001 | 213.339 | - | - | - | - | - |
  | 1 | 1/11/2001 | 215.685 | 1.0118 | 2,000.00 | - | - | 2,000.00 |
  | 2 | 1/12/2001 | 216.163 | 1.0110 | 2,000.00 | 24.31 | 60.00 | 2,084.31 |
  | 3 | 1/1/2002 | 216.944 | 1.0022 | 2,000.00 | 48.34 | 120.00 | 2,168.34 |
  | 4 | 1/2/2002 | 217.074 | 1.0036 | 2,000.00 | 54.50 | 180.00 | 2,234.50 |
  | 5 | 1/3/2002 | 217.276 | 1.0006 | 2,000.00 | 64.06 | 240.00 | 2,304.06 |

  No Modelo Padrão, para o cálculo do índice da correção, o sistema pega a data da venda como base para o cálculo.  
     
  **Exemplo do cálculo da Correção Monetária do Modelo Padrão:**  
     
  • Mês 12/2001  
  213.339 / 210.853 = 1.0118 (índice)  
  (Índice mês anterior – 1) + (índice mês atual – 1) \* (parcela original + juros )   
  (0 + (1.0118 – 1 )) \* (2000 + 60) = 0.0118 \* 2060 = 24.31  
     
  • Mês 01/2002  
  215.685 / 213.339 = 1.0110 (índice)  
  (Índice mês anterior – 1) + (índice mês atual – 1) \* (parcela original + juros )   
  ((1.0118 – 1) + (1.0110 – 1 )) \* (2000 + 60) = 0.0228 \* 2120 = 48.34  
     
  • Mês 02/2002  
  216.163 / 215.685 = 1.0022 (índice)  
  (Índice mês anterior – 1) + (índice mês atual – 1) \* (parcela original + juros )   
  ((1.0118–1) + (1.0110–1 ) + (1.0022–1)) \* (2000+60) = 0.025 \* 2180 = 54.50  
     
     
     
  **2 - Tabela Price:**   
     
  **Geração do Plano:**  
     
  No Sistema de Amortização Francês, também chamado de "Tabela Price", o pagamento do empréstimo é feito ao final de cada período, através de prestações iguais, as quais se constituem de juros sobre o saldo devedor e uma quota de amortização do capital  
     
  **Exemplo:**  
  Cliente "XYZ" comprou um lote no valor de R$ 10.000,00, para pagar em 5 parcelas, a uma taxa de 3% a.m.

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | **PERÍODO** | **PMT** | **JUROS** | **AMORTIZAÇÃO** | **SALDO DEVEDOR** |
  | 0 | - | - | - | -10.000,00 |
  | 1 | 2.183,55 | 300,00 | 1.883,55 | -8.116,45 |
  | 2 | 2.183,55 | 243,49 | 1940,06 | -6.176,39 |
  | 3 | 2.183,55 | 185,29 | 1998,26 | -4.178,13 |
  | 4 | 2.183,55 | 125,34 | 2.058,21 | -2.119,92 |
  | 5 | 2.183,55 | 63,60 | 2.119,95 | -0,00 |

  6,152%
   
  \*Observação:\*
  Se a periodicidade da taxa de juros for anual (campo "Periodicidade da Taxa = Anual"), o sistema irá converter esta taxa de juros para mensal antes de calcular o valor dos Juros Price.
   
  \*Exemplo:\*
  Taxa de Juros anual (i)= 9,5 %
  Fórmula = (1+ i/100)^(1/12)
  (1+9,5/100)^(1/12) => (1+0,095)^(0,08333333333333) => (1,095) ^ (0,08333333333333) => 1,0075915342905826452817375492048
  Juros mensal = (1,0075915342905826452817375492048 - 1) \* 100
  Juros mensal = 0,7591534290582645281737549204
   
  \*Reajuste Financeiro:\*
   
  \*Observação:\*
  a) No caso de Price, como os juros já compõem a parcela, os contratos serão apenas reajustados pelo índice de correção monetária.
   
  b) Somente as parcelas em aberto a partir da data do reajuste serão atualizadas, ou seja, parcelas em atraso não serão atualizadas
   
  \*Tabela Price com Correção Monetária:\*
   
  Para realizar o cálculo da Correção Monetária na Tabela Price, o sistema utiliza a data do primeiro reajuste como referência para fazer o cálculo da correção.
   ]]>

  |  |  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | **Parcela** | **Data** | **Cotação** | **Índice** | **Saldo Dev.** | **Amortização** | **Juros** | **Correção** | **Vr. Total** |
  | - | 1/9/2001 | 210,853 | - | - | - | - | - | - |
  | - | 1/10/2001 | 213,339 | - | 10,000.00 | - | - | - | - |
  | 1 | 1/11/2001 | 215,685 | - | 8,116.48 | 1,883.55 | 300 | - | 2,183.55 |
  | 2 | 1/12/2001 | 216,163 | 1.011790205 | 6,176.42 | 1,940.06 | 243.49 | 25.74 | 2,209.29 |
  | 3 | 1/1/2002 | 216,944 | 1.010996583 | 4,178.16 | 1,998.26 | 185.29 | 50,03 | 2,233.58 |
  | 4 | 1/2/2002 | 217,074 | 1.002216195 | 2,119.95 | 2,058.21 | 125.34 | 54,98 | 2,238.53 |
  | 5 | 1/3/2002 | 217,276 | 1.003613014 | 0.00 | 2,119.95 |  |  |  |

  Venda efetuado data 01/11/2001 com defasagem de 2 meses.  
     
  **Cálculo CM:**  
  01/12/01 – 2 meses de defasagem = 01/10/01  
  Cotação de 01/10/01 / Cotação de 01/09/01 = Índice 213,339/210,853 = 1,011790205  
  (Índice \* Valor da parcela de 01/11/01) – Valor da parcela de 01/11/01 = Correção  
  1,011790205 \* 2183,55 = 2209,29  
  2209,29 – 2183,55 = 25,74  
     
  **Observação:**  
  O índice é calculado mensalmente de acordo com a data de reajuste e meses de defasagens. É multiplicado pelo valor da parcela do mês anterior com todas as correções monetárias e Juros que existir na parcela.  
     
     
     
  **3 - Juros Mensal:**   
     
  **Geração do Plano:**  
     
  Neste modelo, os juros contratuais já serão distribuídos a partir da 2ª parcela de financiamento no momento da geração do plano de financiamento, ou seja, não é feito reajuste de juros mês a mês, somente é calculada a correção monetária dos contratos, podendo ser mensalmente, anualmente ou como previsto em contrato  
     
  **Reajuste Financeiro:**  
     
  A correção é feita pelo valor original das parcelas (sem os juros).  
     
  **Exemplo:**  
  O exemplo a seguir refere-se à uma venda em 11/01/2002 depois da entrega do empreendimento, no valor de R$ 12.000,00, sendo 2.000,00 de sinal e 10.000,00 financiado em 10 parcelas mensais, com a 1ª vencendo em 11/02/2002.   
     
  A título de exemplo o reajuste ( correção das parcelas de financiamento ) acontece de 4 em 4 meses pelo IGP-M com defasagem de 3 meses, ou seja, o primeiro reajuste acontecerá em 11/05/2002, o próximo será em 11/10/2002 e assim por diante. Quanto aos juros, será cobrado 1% a.m. juros simples.  
     
  Teremos o seguinte plano de financiamento:

  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- |
  | **Parcela** | **Data** | **Vr. Original** | **Juros** | **Correção** | **Total** |
  | 1 - Sinal | 11/1/2002 | 2.000,00 | 0,00 | 0,00 | 2.000,00 |
  | 1 – Mensal | 11/2/2002 | 1.000,00 | 0,00 | 0,00 | 1.000,00 |
  | 2 – Mensal | 11/3/2002 | 1.000,00 | 10,00 | 0,00 | 1.010,00 |
  | 3 – Mensal | 11/4/2002 | 1.000,00 | 20,00 | 0,00 | 1.020,00 |
  | 4 – Mensal | 11/5/2002 | 1.000,00 | 30,00 | 0,00 | 1.030,00 |
  | 5 – Mensal | 11/6/2002 | 1.000,00 | 40,00 | 0,00 | 1.040,00 |
  | 6 – Mensal | 11/7/2002 | 1.000,00 | 50,00 | 0,00 | 1.050,00 |
  | 7 – Mensal | 11/8/2002 | 1.000,00 | 60,00 | 0,00 | 1.060,00 |
  | 8 – Mensal | 11/9/2002 | 1.000,00 | 70,00 | 0,00 | 1.070,00 |
  | 9 – Mensal | 11/10/2002 | 1.000,00 | 80,00 | 0,00 | 1.080,00 |
  | 10 – Mensal | 11/11/2002 | 1.000,00 | 90,00 | 0,00 | 1.090,00 |

  **Observação** : A parcela foi acrescida de 1% de juros simples a partir da 2ª parcela mensal  
  Em 11/05/02 acontecerá o primeiro reajuste. Modelo de cálculo:  
  A Data da Cotação Procurada é o mês do Reajuste defasado de 3 meses, sempre dia 1º   
  Data do Reajuste: 11/05/2002  
  Data da Cotação Procurada: 11/02/2002  
  Cotação: 217,074  
  Data da Cotação Anterior: 11/10/2001 ( como o reajuste é de 4 em 4 meses, o sistema calcula do acumulado do IGPM de out/2001 a fev/2002)  
  Cotação Anterior: 213,339 (cotação em out/2001)  
  Variação da cotação da CM: 0,0175 ( IGPM acumulado de out/2001 a fev/2002 = cotação de fev/2002 dividido pela cotação de out/2001 menos 1 = (217,074 / 213,339) – 1 = 0,0175  
     
  **Cálculo da correção:**  
  Vr. Original \* Variação do acumulada do índice =   
  = (1.000,00 + 0,00) \* 0,0175 = 17,50  
     
  Para realizar o cálculo da Correção Monetária no Juros Mensal, o sistema utiliza a data da venda como referência para fazer o cálculo da correção.  
     
  **Plano de Financiamento Corrigido:**

  |  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- |
  | **Parcela** | **Data** | **Cotação** | **Índice** | **Vr. Original** | **Juros** | **Correção** | **Total** |
  | - | 1/10/2001 | 213.339 | - | - | - | - | - |
  | - | 1/11/2001 | 215.685 | - | - | - | - | - |
  | - | 1/12/2001 | 216.163 | - | - | - | - | - |
  | 1 - Sinal | 11/1/2002 | 216.944 | - | 2000.00 | 0.00 | 0.00 | 2000.00 |
  | 1 – Mensal | 11/2/2002 | 217.074 | - | 1000.00 | 0.00 | 0.00 | 1000.00 |
  | 2 – Mensal | 11/3/2002 | 217.276 | - | 1000.00 | 10.00 | 0.00 | 1010.00 |
  | 3 – Mensal | 11/4/2002 | 218.492 | - | 1000.00 | 20.00 | 0.00 | 1020.00 |
  | 4 – Mensal | 11/5/2002 | 220.292 | 1.0175 | 1000.00 | 30.00 | 17.50 | 1047.50 |
  | 5 – Mensal | 11/6/2002 | 223.688 | - | 1000.00 | 40.00 | 17.50 | 1057.50 |
  | 6 – Mensal | 11/7/2002 | 228.057 | - | 1000.00 | 50.00 | 17.50 | 1067.50 |
  | 7 – Mensal | 11/8/2002 | 233.348 | - | 1000.00 | 60.00 | 17.50 | 1077.50 |
  | 8 – Mensal | 11/9/2002 | 238.943 | 1.0305 | 1000.00 | 70.00 | 48.53 | 1118.53 |
  | 9 – Mensal | 11/10/2002 | 244.234 | - | 1000.00 | 80.00 | 48.53 | 1128.53 |
  | 10 – Mensal | 11/11/2002 | 249.525 | - | 1000.00 | 90.00 | 48.53 | 1138.53 |

     
    
     
  **4 – Tabela SAC**  
     
  Sistema de Amortização Constante (Tabela SAC), também conhecido como Sistema Hamburguês.  
  Este sistema é extremamente simples, uma vez que os valores das amortizações periódicas são todas iguais ou constantes. Trata-se de um sistema de amortização (quitação da dívida) muito utilizado pelas instituições financeiras. Como o próprio nome diz, uma parcela fixa da prestação vai abatendo constantemente o que você deve, fazendo com que o saldo devedor seja cada vez menor, e é sobre esse saldo que se aplicam os juros.   
  Isso faz com que o valor pago e as próprias prestações sejam decrescentes ao longo do tempo, pois à medida que o tempo passa e a dívida vai sendo quitada e o valor a ser pago com juros sobre o saldo devedor diminui. Se a parte dos juros diminui e a amortização é constante, então o valor da parcela também vai diminuir.  
  Lembre-se: no Sistema de Amortização Constante, o pagamento da dívida ocorre constante e igualmente em cada período.  
  Considera-se como "saldo devedor" a diferença entre o valor financiado reajustado e o valor total que já foi amortizado (quitado) até o presente momento.  
  **Exemplo:**  
  Cliente "XYZ" comprou um lote no valor de R$ 10.000,00, para pagar em 5 parcelas, a uma taxa de 3% a.m.   
  **Solução: Tabela SAC**
* |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | **PERÍODO** | **PMT** | **JUROS** | **AMORTIZAÇÃO** | **SALDO DEVEDOR** |
  | 0 | - | - | - | -10.000,00 |
  | 1 | 2.300,00 | 300,00 | 2.000,00 | -8.000,00 |
  | 2 | 2.240,00 | 240,00 | 2.000,00 | -6.000,00 |
  | 3 | 2.180,00 | 180,00 | 2.000,00 | -4.000,00 |
  | 4 | 2.120,00 | 120,00 | 2.000,00 | -2.000,00 |
  | 5 | 2.060,00 | 60,00 | 2.000,00 | -0,00 |

  • PMT = Valor da parcela no SGI  
  • JUROS = Valor do componente de Juros  
  • AMORTIZAÇÃO = Valor do Componente principal  
   **Observação:**  
  a) No caso do SAC, como os juros já compõem a parcela, os contratos serão apenas reajustados pelo índice de correção monetária.  
  **Cálculo da Tabela SAC:**  
  Valor da Parcela:  
  Amortização = Vr. Empréstimo / Nr. Parcelas  
  Amortização = 10.000,00 / 5 = 2.000,00  
  Valor dos Juros:  
  Juros = Saldo devedor \* % de Juros  
  Juros = 10.000,00 \* 0,03 = 300,00  
  **Tabela SAC com Correção Monetária:**  
  O cálculo da Correção Monetária na Tabela SAC funciona da mesma forma que o Price.  
     
  **5 – Tabela SACRE**  
     
  É uma variação da tabela SAC que é utilizada pela Caixa Econômica Federal. A tabela SACRE utiliza um Sistema de Amortização Crescente.  
     
  A diferença do SAC – Sistema de amortização constante para o SACRE – Sistema de Amortização Crescente é apenas o recalculo, ou seja, um novo calculo após um determinado período de andamento do contrato. O SACRE é baseado na mesma metodologia do SAC, mas, sempre considerando o prazo remanescente (que falta) para pagar.  Assim o recalculo força o crescimento da amortização e a rapidez do pagamento.  
     
  Ao contrário do que acontece no SAC a parcela de amortização não é constante e sim crescente, o que permite que a dívida seja paga mais rapidamente.  
     
  Neste sistema, o valor da parcela é mantido fixo durante 12 meses. Devido ao fato de que a cada mês o saldo devedor diminui um pouco, ao se manter o valor fixo aumenta-se o valor utilizado para quitar o saldo devedor.  
     
  De 12 em 12 meses do financiamento, o saldo devedor é recalculado e dividido pelos meses restantes do financiamento fazendo com que o valor da parcela abaixe.  
     
  **Observação:**  
  No caso do SACRE, como os juros já compõem a parcela, os contratos serão apenas reajustados pelo índice de correção monetária.  
     
     
  **Tabela SACRE com Correção Monetária:**  
     
  O cálculo da Correção Monetária na Tabela SACRE funciona da mesma forma que o Price.

**6 - Minha Casa Minha Vida:**  
   
Para saber sobre este modelo, clique: **Minha Casa Minha Vida**
