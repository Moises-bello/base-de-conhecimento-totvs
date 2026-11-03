---
content_hash: 1bbd6fe18284aa70307f0b8e616f70d2634b59bdfc5b8fce5e45446c6328482e
fetched_at: '2026-06-29T00:10:08.682928+00:00'
page_id: '452719558'
product: rm
source: tdn-rm
title: Férias em Dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719558
version: 6
---

Nesta etapa será definido o tratamento e pagamento de férias em dobro  
   
**Campos e Parâmetros**

**Paga férias em dobro**  
Se este parâmetro estiver marcado, as férias e o abono pecuniário serão pagos em dobro, acrescida de 1/3 constitucional, caso tenha ultrapassado o Limite de início de gozo, conforme o artigo 137 da CLT (Consolidação das Leis do Trabalho).  
Para que seja feito o pagamento correto, é necessário cadastrar os eventos com os respectivos códigos de cálculo nos campos abaixo:

* Evento férias em dobro: Código de Cálculo 309 - FÉRIAS EM DOBRO
* Evento 1/3 de férias em dobro: Código de Cálculo 310 - ADICIONAL 1/3 DE FÉRIAS EM DOBRO
* Evento abono de férias em dobro: Código de Cálculo 311 - ABONO DE FÉRIAS EM DOBRO
* Evento 1/3 de abono de férias em dobro: Código de Cálculo 312 - ADICIONAL 1/3 DE ABONO DE FÉRIAS EM DOBRO

A quantidade de dias de pagamento de férias em dobro será mesma que ultrapassar o limite, não contando todo o período devido, caso a quantidade seja menor que 30.

**Exemplo**  
Período aquisitivo em aberto: 13/06/2015 a 12/06/2016  
Limite para início de gozo: 14/05/2017  
Funcionário marcou as férias para o dia 01/06/2017  
Será pago 16 dias de Férias em dobro mais 1/3 constitucional, nos eventos informados acima.   
Os demais dias (14) não serão calculados para serem pagos em dobro.  
   
**Observação**  
Quando é marcado as férias, o sistema emite um alerta para o usuário da possibilidade de pagamento de férias em dobro.

**Interrompe contagem do período para pagto de férias em dobro nos afastamentos I - L - M - P - T**  
Com este parâmetro marcado, é interrompido na contagem do período de gozo para pagamento de férias em dobro, o período do afastamento.

**Exemplo**  
Período aquisitivo em aberto: 13/06/2015 a 12/06/2016  
Limite para início de gozo: 14/05/2017  
Funcionário afastado pelo tipo 'P' de 01/01/2017 a 30/01/2017  
O Limite para início de gozo passa a ser 14/06/2017  
Caso o funcionário inicie o gozo de férias 01/06/2017´, o sistema não irá calcular férias em dobro para o mesmo.

**Desconsidera período de atestado médico na interrupção**

Esse parâmetro deve ser marcado para que não seja computado os dias de atestado referente ao período do afastamento quando houver interrupção da contagem do período de gozo para pagamento de férias em dobro.

**Exemplo**  
Período aquisitivo em aberto: 13/06/2019 a 12/06/2020

Limite para início de gozo: 14/05/2021  
Funcionário afastado pelo tipo 'P' de 01/01/2021 a 30/01/2021 – dentro do segundo período aquisitivo

O Limite para início de gozo passa a ser 29/05/2021

**Não interrompe contagem do período para pagto de férias em dobro no afast. por Licença Maternidade (E)**  
Quando o funcionário está afastado por Licença Maternidade (tipo E), é interrompido o período de afastamento na contagem de período para pagamento de férias em dobro. Com este parâmetro marcado, será considerado este período na contagem do período para pagamento de férias em dobro.

**Exemplo**  
*Parâmetro desmarcado*  
Período aquisitivo em aberto: 13/06/2015 a 12/06/2016  
Limite para início de gozo: 14/05/2017  
Funcionário afastado pelo tipo 'E' de 01/01/2017 a 30/04/2017  
O Limite para início de gozo passa a ser 14/09/2017  
Caso o funcionário inicie o gozo de férias 01/06/2017´, o sistema não irá calcular férias em dobro para o mesmo.  
   
*Parâmetro marcado*  
Período aquisitivo em aberto: 13/06/2015 a 12/06/2016  
Limite para início de gozo: 14/05/2017  
Funcionário afastado pelo tipo 'E' de 01/01/2017 a 30/04/2017  
O Limite para início de gozo passa a ser 14/05/2017  
Caso o funcionário inicie o gozo de férias 01/06/2017´, o sistema irá calcular férias em dobro para o mesmo do período do dia 15/05 a 31/05.

**Marcar automaticamente férias em dobro ao liberar competência**  
Com este parâmetro marcado, no processo de Liberação de competência será feita a marcação de férias para todos os funcionários que possuem férias em dobro ou que tenha férias a vencer, conforme a quantidade de dias informado no campo 'Qtd. de dias a ser considerada para marcação' . As férias do funcionário serão marcadas para a primeira segunda-feira da próxima competência.  
   
**Qtd. de dias a ser considerada para marcação**  
Quando é marcado o parâmetro 'Marcar automaticamente férias em dobro ao liberar competência', é habilitado este campo. Nele o usuário irá informar a quantidade de dias que o sistema deve verificar antes de completar as férias em dobro.

**Não exibir mensagens de férias em dobro para funcionários intermitentes no cadastro individual de férias**

Com este parâmetro marcado, não serão apresentadas as mensagens relacionadas a férias em dobro para funcionários com o tipo de contrato de trabalho intermitente.

**Observação:**

Para que seja habilitado o parâmetro **'Não exibir mensagens de férias em dobro para funcionários intermitentes no cadastro individual de férias**' deverão ser confirmados os parâmetros 'Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017', disponível em **RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Geral,** 'Usa Trabalho Intermitente' e 'Trata cadastro de férias para contrato intermitente' disponível em **RH | Folha de Pagamento | Configurações | Parametrizador | Folha de Pagamento | Funcionário | Trabalho Intermitente | Parâmetros do Trabalho Intermitente** e 'Regime de Trabalho Intermitente' disponível em **RH | Folha de Pagamento | Administração de Pessoal | Funcionários |  Informações Contratuais | Salário / Jornada**.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<< Retornar para **Férias**
