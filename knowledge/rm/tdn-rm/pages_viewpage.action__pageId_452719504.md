---
content_hash: 304012822afcb70ee7b0f99d97eb71dcdacc1ff837672d834856e820d2311812
fetched_at: '2026-06-29T00:10:08.059771+00:00'
page_id: '452719504'
product: rm
source: tdn-rm
title: Férias - Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719504
version: 15
---

Nesta etapa será configurado o cálculo de férias na rescisão.  
   
**Campos e Parâmetros**  
Considera faltas para cálculo de férias  
Com este parâmetro marcado, o sistema irá considerar as faltas do funcionário ocorridas no período aquisitivo de férias vencidas e proporcionais para o cálculo das férias na rescisão. Caso contrário, o sistema não irá considerar as faltas para o cálculo das férias vencidas e proporcionais na rescisão.

Perda de férias devido a faltas não deve afetar avo do aviso prévio indenizado

Parâmetro para calcular avos de férias referente ao período do aviso prévio indenizado desconsiderando a proporção perdida pelas faltas e será habilitado somente quando marcar para considerar faltas para cálculo de férias.

Os CC's 329, 330 e 331 na rescisão serão calculados de acordo com essa parametrização, ou seja, a parte desconsiderada no avo do CC 329 será acumulada no CC's 330 ou 331, dependendo se o aviso entra nas férias proporcionais ou vencidas.

**Dica:** No cadastro de eventos orientamos informar o campo prioridade ou o campo ordem de cálculo na ordem correta que é na ordem crescente de códigos de cálculo 329, 330 e 331.

**Observação:** Caso haja perda de período aquisitivo por mais de 32 faltas, os avos de férias referente a projeção do aviso prévio indenizado também serão perdidos independente do parâmetro marcado ou não.

**Exemplo:**

**Parâmetro marcado**

Cálculo de férias com 20 dias de faltas - direito a 18 dias de férias

CC 25 - 10 MESES + 1 INDENIZADO = 27,5 DIAS

Quando proporcionaliza devido a faltas fica 16,5 dias

O processo adiciona  Valor de 1,00 referente ao avo indenizado e o  Numero de dias de Férias passa a ser 17,50

Valor Salário (6.184,430000) / 30 \* Dias Férias (17,500000) = 3.607,584167 = 3607,58

Cálculo da Média: 927,664500 / 10 = 92,766450 = 92,77

Proporcionalizando para 17,50 dias: 92,77 / 30 \* 17,50 = 51,023500 = 54,1137 = 54,12

**CC 329** – Salário (6.184,430000) / 30 \* **Dias Férias (2,500000)** = 515,369167

Média:  54,12 / 11 \* 1 = 4,92

TOTAL - CC 329 = 515,369167 + 4,92 = 520,28

**CC 330** – Salário (6.184,430000) / 30 \* **Dias Férias (15,000000)** =3 092,15

Média: 54,12 / 11 \* 10 = 49,20

TOTAL - CC 330 3.092,215000 + 49,20 = 3141,42

**Parâmetro desmarcado**

Cálculo de férias com 20 dias de faltas - direito a 18 dias de férias

CC 25 - 10 MESES + 1 INDENIZADO = 27,5 DIAS

Quando proporcionaliza devido a faltas fica 16,5 dias

Valor Salário (6.184,430000) / 30 \* Dias Férias (16,500000) = 3.401,436500 = 3.401,44

Cálculo da Média: 927,664500 / 10 = 92,766450 = 92,77

Proporcionalizando para 16,50 dias: 92,77 / 30 \* 16,50 = 51,023500 = 51,02

Total: 3452,46

**CC 329** – Salário (6.184,430000) / 30 \* **Dias Férias (1,500000)** = 309,2215

Média:  51,02 / 11 \* 1= 4,63

TOTAL - CC 329 = 309,221500 + 4,6385 = 313,86

**CC 330** – Salário (6.184,430000) / 30 \* **Dias Férias (15,000000)** = 3092,215

Média: 51,02 / 11 \* 10 = 46,385 = 46,38

TOTAL - CC 330 3.092,215000 + 46,38 = 3138,60

Separar Médias de Férias Vencidas e Proporcionais na Rescisão  
Se o parâmetro for marcado o sistema possibilitará ao usuário separar as médias de férias vencidas das férias proporcionais na rescisão (quando as médias forem discriminadas) e abrirá a pasta "Eventos p/Pág. de Média Proporcional" no cadastro de sindicatos.   
É importante lembrar que também é obrigatória a informação dos eventos nesta pasta, já que o sistema apresentará uma mensagem de inconsistência ao tentar gerar as Provisões de Férias e 13º salário.  
Este parâmetro também deve rá ser marcado pois, segundo as regras do eSocial, as verbas rescisórias referentes as férias do período vencido devem ser enviadas separadas das verbas referentes ao período proporcional.  
   
A partir de   
Para marcar a partir de qual data será o marco do cálculo feito separando Médias e 1/3 de férias vencidas e proporcionais na rescisão informe esta data.

**Observação**  
É importante informar a data correta na marcação do parâmetro, para evitar inconsistências no caso de uma Rescisão Complementar.

Lança eventos adicionais de férias na rescisão  
Marcando este parâmetro, ao calcular a rescisão do funcionário, o sistema lançará na rescisão os eventos adicionais informados em Configurações | Parâmetros | Parametrizador | Folha de Pagamento | Férias | Eventos Adicionais de Férias.  
   
Proporcionaliza média na rescisão considerando a fórmula referência  do evento

Paga férias em dobro quando segundo período aquisitivo vence durante projeção do aviso prévio

Com esse parâmetro marcado, caso de demissões com projeção do aviso prévio indenizado em que houver o vencimento de segundo período de férias durante a projeção, será pago as Férias em Dobro com o código de cálculo 365 - FÉRIAS EM DOBRO RESCISÃO verificando até o final da projeção do aviso prévio indenizado.

Se o parâmetro estiver desmarcado, será pago as Férias em Dobro com o código de cálculo 365 - FÉRIAS EM DOBRO RESCISÃO verificando até a data da demissão.

**Exemplos:**

Competência da base = 02/2021

Período aquisitivo em aberto = 10/04/2019 a 09/04/2020

Demissão = 28/02/2021

Aviso = 01/03/2021 – 90 dias

Vencimento da projeção = 29/05/2021

Vencimento do segundo período aquisitivo = 10/04/2020 a 09/04/2021

Parâmetro marcado – PAGA FÉRIAS EM DOBRO – 30 DIAS

Parâmetro desmarcado – NÃO PAGA FÉRIAS EM DOBRO

Competência da base = 02/2021

Período aquisitivo em aberto = 15/02/2019 a 14/02/2020

Demissão = 28/02/2021

Aviso = 01/03/2021 – 30 dias

Vencimento da projeção = 30/03/2021

Vencimento do segundo período aquisitivo = 15/02/2020 a 14/02/2021 (nesse caso antes da data de demissão)

Parâmetro marcado – PAGA FÉRIAS EM DOBRO – 30 DIAS

Parâmetro desmarcado – PAGA PROPORCIONAL 14 DIAS ME DOBRO SOMENTE PARA O MÊS 02 – MÊS DA DEMISSÃO

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Retornar para **Rescisão**
