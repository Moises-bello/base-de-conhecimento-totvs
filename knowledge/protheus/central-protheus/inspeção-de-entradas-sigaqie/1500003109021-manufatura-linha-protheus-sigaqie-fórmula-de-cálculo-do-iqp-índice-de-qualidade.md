---
article_id: 1500003109021
category: Inspeção de Entradas (SIGAQIE)
content_hash: 75be5bcf6683111a21902fb2ac39aa4759c004a0fd21fd81495475def1d60ee4
fetched_at: '2026-06-28T22:42:26.983728+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Fórmula de cálculo do IQP - Índice
  de Qualidade do Produto
type: support-article
updated_at: '2021-06-18T19:13:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003109021-Manufatura-Linha-Protheus-SIGAQIE-F%C3%B3rmula-de-c%C3%A1lculo-do-IQP-%C3%8Dndice-de-Qualidade-do-Produto
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min**  
**Dúvida**Qual a fórmula de cálculo do **IQP - Índice de Qualidade do Produto**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Versão 12  
  
**Solução**Para calcular o **IQP** é necessário verificar o nível de qualidade do produto fornecido no período, que é determinado por meio dos resultados obtidos durante a inspeção de recebimento de cada item de um mesmo fornecedor e do seu desempenho durante a utilização.  
A fórmula utilizada para cálculo do **IQP** é:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104318453/mceclip0.png)

**Onde**:  
**k** = quantidade tabulada em função do **Ia- Índice de Aceitação**, onde o **Ia** será convertido em pontos. Este índice está especificado na rotina **QIEA270 - Fatores I.A.**, e é calculado à partir dos laudos registrados a cada entrega em função das respectivas quantidades, utilizando a fórmula abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003282042/mceclip1.png)

**Onde**:  
**Fn** = **Fator do laudo registrado na inspeção de entrada**  
**Qn** = **Quantidade entregue com o fator n**  
  
Ou seja, deve-se observar quantas unidades do produto foram recebidas com cada laudo, multiplicar pelo fator do laudo especificado na rotina **QIEA260 - Fatores do IQP** e dividir pela quantidade total do período.  
  
**Exemplo**  
Se ocorrer 4 entradas no período, sendo:

* 1 aprovada sem restrições, de quantidade 50, e observarmos esse laudo na rotina **QIEA260** temos que para ele o fator é 1;
* 2 aprovadas com desvio simples, de quantidade 10 cada uma, e se observarmos esse laudo na rotina **QIEA260** temos que para ele o fator é 0,95;
* 1 aprovada com desvio grave, de 15 unidades, e se observarmos esse laudo na rotina **QIEA260** temos que para ele o fator é 0,7.

Aplicando na fórmula, tem-se portanto **Ia = ((50 \* 1)+(20 \* 0,95)+(15 \* 0,70)/85) \* 100= 93,529**  
Se consultarmos a tabela da rotina **QIEA270**, vemos que para o intervalo de 90,00 até 99,99 o **fator K** deve ser 5, portanto **k** é igual à 5.  
  
Já com relação à pontuação de não-conformidades, vê-se as **FNCs - Fichas de Não Conformidades** geradas no período e a classe da **FNC** gerada. Na rotina **QIEA160** **- Classes de Não Conformidades** temos atribuído para cada classe uma pontuação, a totalidade dessa pontuação será subtraída para o cálculo do **IQP**.  
  
Voltando ao nosso exemplo: Se para a as duas entradas com desvio simples atribuímos uma **FNC** e classe moderadamente sério, teremos 2 pontos de cada **FNC**, totalizando 4 pontos.  
  
Se para a entrada com desvio grave, atribuímos uma **FNC** e classe sério, teremos 5 pontos, totalizando portanto 9 pontos.  
Neste caso o **IQP** será:  
**IQP** = (100 - **k** )- total demérito em função das **FNCs** geradas   
**IQP** = (100 - 5) - 9   
**IQP** = (95 - 9)  
**IQP** = 86
