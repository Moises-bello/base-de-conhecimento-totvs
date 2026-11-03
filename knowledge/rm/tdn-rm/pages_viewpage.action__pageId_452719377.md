---
content_hash: 29af1a2c49c6271ce0d95676714efbd58207c1dd8787af89dcff34ce7ee19d5d
fetched_at: '2026-06-29T00:10:07.227023+00:00'
page_id: '452719377'
product: rm
source: tdn-rm
title: Diferença de Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719377
version: 12
---

Através deste processo são calculadas as diferenças de férias, ocasionada por algum aumento salarial ou devido à variação de médias.  
   
A diferença é calculada verificando a data do aumento salarial (existente no histórico salarial) e todos os períodos de gozo posteriores a esta data.   
   
Somente é permitido o cálculo da diferença de férias quando as mesmas estão lançadas.  
   
Antes do processamento da diferença é fundamental verificar as parametrizações do sindicato (Médias, Eventos para Diferença, etc).  
   
Para encontrar o valor da diferença é calculado novamente os eventos do período informado e subtraído os valores já pagos dentro deste período, verificando a tabela PFVERBASDIS (eventos de diferenças) se houve alguma diferença paga neste período.  
Sendo o procedimento interno do sistema:  
1.     Recalcular as férias;  
2.     Comparar os valores encontrados com os valores pagos no recibo de férias;  
3.     Quando o valor encontrado é maior que o valor calculado no recibo, é lançado o valor da diferença;  
4.     Os valores são dispostos em eventos específicos de diferença e lançados automaticamente para o envelope.

Dica:

Veja também informação importante no cálculo de diferença quando envolve Pensão Alimentícia no TDN

**Atenção:**

* Quando as férias forem partidas, os valores referente as diferenças de "médias" serão somados  no evento de diferença de férias , ou seja , não serão discriminados no envelope.
* Os eventos de médias serão discriminados  quando as férias forem gozadas integralmente dentro mês.

**Exemplo1 : Férias partidas com médias.**

Recibo de férias : Salário R$1344,00

1. Salário para cálculo diferença : R$2000,00
2. Valor da diferença de médias Horas extras- R$9,32.

Cod.     Descrição Evento              Valor

0038   Férias mês                         R$1344,00

0040   1/3 Férias mês                   R$  454,36

0086   Média de Hora Extra          R$    19,09

Calculado diferença de Férias 20/01/2019 a 19/02/2019

Valor da diferença de médias Horas extras- R$9,32.

 Lançado no envelope:

Cod.     Descrição Evento                           Valor

0045-    Diferença Férias mês    12 dias    R$266,13 (Considerou o valor da diferença das médias horas extras proporcional )

0079-    Diferença 1/3 férias mês               R$88,71

0080-    Diferença Férias Próximo mês 18 dias–   R$399,19  (Considerou o valor da diferença das médias horas extras proporcional)

0081-    Diferença 1/3 férias próximo mês- R$133,07

****Exemplo2 : Férias dentro mês com médias.****

Calculando diferença de Férias 02/01/2019 a 31/01/2019

Diferença de médias R$9,32.

 Lançado no envelope:

Cod.         Descrição Evento                              Valor

0045-       Diferença Férias mês -                      R$656,00

0079-       Diferença 1/3 férias mês -                 R$221,78

0121-       Diferença de médias Horas extras – R$9,32

**Conceito e Procedimento das diferenças**  
Competência 01/2014  
Cálculo da diferença período 01/09/2013 a 30/09/2013  
Início gozo das férias: 18/09/2013   
   
Histórico Salarial  
Data Processamento              Data Mudança               Salário  
20/05/2012                               01/04/2012                   1.000,00  
01/08/2013                               01/05/2013                   1.050,00  
01/08/2013                               02/05/2013                   1.100,00  
01/10/2013                               01/07/2013                   1.200,00  
01/01/2014                               01/01/2014                   1.300,00  
   
Ao calcular a diferença é verificada a data de processamento que tem a data > (MAIOR) do que o início do gozo das férias, para saber o dia em que foi aplicada a alteração na base de dados.   
Dentro deste filtro verifica a data de mudança que tem a data <= (MENOR OU IGUAL) do que a data de fim de gozo.  
No exemplo acima é utilizado o salário R$1.200,00 para o cálculo da diferença.  
   
   
Sempre que existir evento utilizando variável de fórmula contendo parâmetros MÊS e ANO (mesmo quando este parâmetro é interno, como por exemplo a variável SM (retorna salário mínimo)), é considerado o MES e ANO da época da diferença.  
**Exemplo I:**   
O salário mínimo de 2012 é de R$500,00 e em 2013 foi ajustado para R$600,00.  
Caso a competência atual da base seja 2013, e a diferença processada é referente a 2012, se existir uma fórmula que utilize a variável SM, é considerado o valor de 500,00 para o salário mínimo.  
   
**Exemplo II:**  
Um evento tem a fórmula HANT (MTDATA(DIADT(ULTDIAMES(MTDATA(01,MES,ANO))), MES,ANO) ), quando processar uma diferença retroativa, o MES e ANO será da época da diferença.  
Exemplo de outras variáveis: MV, C, MH, etc.  
   
   
O parâmetro 'Zera evento de diferença quando o valor for negativo' existente em Configurações | Parametrizador | Folha Normal | Cálculo é verificado apenas no recálculo do envelope original, ou seja, o valor é zerado somente quando um evento que constava no envelope original fica com valor negativo após o novo recálculo.  
   
**Exemplo:** Considerando que o funcionário recebeu um evento utilizando a fórmula:

SE RC<1600 ENTAO 100 SENAO 50 FIMSE  
   
Salário inicial: R$1.500,00  
Envelope Inicial

Cod.     Descrição Evento              Valor  
0001           Salário                       1.500,00

2033          Desconto                    100,00 (calculado pela formula acima)  
   
Alterado o salário para: R$1.670,00

Envelope Recalculado:

Evento                     Valor pago        Val. recalculado             Diferença

0001     Salário          1.500,00           1.670,00                       170,00

2033     Desconto       100,00                50,00                          -50,00 (como o valor deste evento é negativo, caso o parâmetro esteja marcado o valor é zerado).  
   
**Atenção:**   
Existe situação em que mesmo com o parâmetro desmarcado, ou seja, não permitindo lançar valores negativos, o evento pode ser lançado com o valor negativo.  
   
**Exemplo:**   
Um evento de desconto teve cálculo de diferença, porém neste evento não está informado um evento de diferença.  
Neste caso a diferença é lançada no evento com código de cálculo 45 (provento). Caso o valor do desconto seja maior que o valor do código de cálculo 45, o evento com cc45 é lançado negativo.  
Para que isso não ocorra, basta criar um evento de diferença do tipo desconto, e informá-lo no cadastro do evento original.  
   
   
Quando no intervalo do cálculo da diferença de férias existir mais de um período de gozo (recibo de férias), é necessário realizar o processo da diferença individual para cada período de gozo e em períodos(envelopes) distintos.  
   
**Exemplo:**  
Competência do registro do aumento 06/2013  
Data do aumento salarial 01/07/2012  
1- Férias gozadas em 01/10/2012 a 30/10/2012  
2- Férias gozadas em 01/06/2013 a 30/06/2013  
   
Para calcular a diferença de férias, nesse exemplo, deve calcular no período 1 (envelope), a diferença referente ao período de gozo 01/10/2012 a 30/10/2012.   
Em seguida alterar o período (envelope) para 2 e processar novo cálculo de diferença referente ao período de gozo de férias de 01/06/2013 a 30/06/2013.  
   
   
   
Quando utiliza salário composto, a diferença de férias é calculada com base no salário ATUAL, não é feita a proporcionalidade de eventos que porventura tenham tido aumentos em datas diferentes.  
   
   
Quando o funcionário tem férias partidas, e ocorrerem dois aumentos salariais, sendo um no mês do início do gozo das férias e o segundo aumento no mês de fim de gozo, e o primeiro aumento já teve a diferença calculada, é lançado o evento com código de cálculo 80-Dif. Férias Próx. Mês.  
   
   
Ao calcular diferenças para funcionários com múltiplos vínculos (parametrizações do sistema), é feito o lançamento de INSS e IRRF apenas na chapa centralizadora.

 **Atenção:**  
   Quando no parametrizador estiver marcado os parâmetros abaixo :

      - Calcula IRRF/INSS de Múltiplos Vínculos sem chapa Centralizadora

         -Calcula INSS conforme eSocial

      Antes de calcular uma diferença de ferias devermos primeiro calcular uma diferença salarial.

    
IRRF Férias  
Para o cálculo do IRRF Diferença de Férias, existem as seguintes considerações:  
Se a diferença de férias é calculada no mesmo mês em que as férias são lançadas, o valor do IRRF é recalculado utilizado as novas bases, e é lançado a diferença entre o novo IRRF e o IRRF já descontado.  
   
Se a diferença de férias é calculada em meses posteriores ao do lançamento das férias, o IRRF é calculado sobre o valor da diferença de férias.  
   
13º Pago nas Férias  
É necessário informar um evento com código de cálculo '9-1ª Parcela de 13º Salário' para que a diferença da 1ª parcela seja lançada.  
   
Dissídio NÃO  
Considera a tabela de incidência de INSS da competência atual.

Dissídio SIM

Considera a tabela de incidência de INSS do mês das férias, sendo necessária a existência de eventos com os códigos de cálculos:  
CC 110 – INSS DE DIF. SALARIAL DE FÉRIAS;  
CC 111 – BASE DE FGTS DE DIF. SALARIAL DE FÉRIAS;  
CC 116 – ESTORNO BASE INSS DISSÍDIO RET. FÉRIAS.  
   
**Observação:**   
Quando utiliza as configurações de Múltiplos Vínculos, para que o INSS por dissídio seja lançado corretamente, é necessário sempre processar a diferença por dissídio para a chapa centralizadora de INSS, independentemente de ter aumento salarial.  
   
Aumentos a não considerar  
Para desconsiderar aumentos que foram concedidos dentro do período de apuração da diferença.  
   
**Exemplo:**  
Férias gozadas: Agosto/2013  
Salário utilizado no cálculo das férias: R$950,00  
Histórico Salarial  
Data Processamento      Data Mudança   Salário              Motivo  
01/08/2013                   01/08/2013       R$950,00          Mérito  
01/09/2013                   01/09/2013       R$1.010,00       Enquadramento   
01/10/2013                   01/07/2013       R$1.100,00       Dissídio  
   
Marcando para desconsiderar o motivo 'Enquadramento', o valor da diferença entre o salário alterado por Dissídio e o salário alterado por Mérito não é considerado, e o resultado encontrado é somado ao salário da época em que as férias foram pagas, neste caso 08/2013.  
Sendo o cálculo:  
R$1.100,00 – R$1.010,00 = R$90,00 (diferença entre o aumento do salário por 'Dissídio' e o salário por 'Mérito'.  
   
Para cálculo da diferença das férias é utilizado a base:  
R$950,00 + R$90,00 = R$1.040,00 (base para cálculo da diferença)  
Cálculo da diferença de férias:  
R$1.040,00 (base para cálculo da diferença) – 950,00 (salário pago nas férias) = 90,00.  
A diferença do evento Férias é R$90,00.  
   
**Observação:**  
Este exemplo não contempla 1/3 de férias e outras verbas pagas no recibo de férias.  
   
   
   
Local da Chamada

Processo Visão de Funcionário

Processo Férias | Diferença
