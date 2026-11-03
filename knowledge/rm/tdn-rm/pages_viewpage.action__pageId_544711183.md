---
content_hash: 4c37a6771ddd3097bc0cd30e644075dc30cc459780eeeced33d320a34ef42f3a
fetched_at: '2026-06-29T00:10:38.702451+00:00'
page_id: '544711183'
product: rm
source: tdn-rm
title: MP927/1046 - Concessão de Férias Coletivas 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544711183
version: 7
---

Art. 11.  Durante o estado de calamidade pública a que se refere o art. 1º, o empregador poderá, a seu critério, conceder férias coletivas e deverá notificar o conjunto de empregados afetados com **antecedência de, no mínimo, quarenta e oito horas, não aplicáveis o limite máximo de períodos anuais e o limite mínimo de dias corridos** previstos na [Consolidação das Leis do Trabalho, aprovada pelo Decreto-Lei nº 5.452, de 1943.](http://www.planalto.gov.br/ccivil_03/Decreto-Lei/Del5452.htm)

Art. 12.  Ficam dispensadas a comunicação prévia ao órgão local do Ministério da Economia e a comunicação aos sindicatos representativos da categoria profissional, de que trata o [art. 139 da Consolidação das Leis do Trabalho, aprovada pelo Decreto-Lei nº 5.452, de 1943.](http://www.planalto.gov.br/ccivil_03/Decreto-Lei/Del5452.htm#art139)

**FÉRIAS COLETIVAS**

Primeiramente, informamos que já temos um TDN com diversas informações relacionadas as Férias Coletivas:

<https://tdn.totvs.com/pages/releaseview.action?pageId=452719357>

Abaixo será demonstrado alguns cenários de exemplo, para melhor entendimento das Férias Coletivas:

Cenário de exemplo:

Funcionários:

Chapa 00014 - Tem direito a 30 dias de férias

Chapa 00002 - Tem direito a 5 dias de férias e tem **mais** de um ano de casa

Chapa 98765 - Tem direito a 8 dias de férias e tem **menos** de um ano de casa

Chapa 00008 - Tem direito a 20 dias de férias, tem **mais** de um ano de casa e já tem cadastrado um período de gozo de 10 dias de férias (Antecipando conforme próximo Período Aquisitivo)

Férias Coletivas cadastradas:

**Observações**

1. O campo Data Aviso permite alteração pelo usuário, atendendo a MP 927.
2. Marcando Férias Coletivas, seguirá as regras da CLT das Férias Coletivas
3. Demais parâmetros de tela, estão documentadas de forma detalhada através do tdn: <https://tdn.totvs.com/pages/releaseview.action?pageId=452719357>
4. Ao avançar, o produto emite o alerta abaixo:

Conforme a MP 927, o alerta poderá ser ignorado, basta clicar em Sim para prosseguir.

*Resultados após cadastro das Férias Coletivas*

1. Chapa 00002 - Tem direito a 5 dias de férias e **tem mais de um ano de casa**

Foi cadastrado 30 dias de férias e pelo fato do funcionário não ter direito aos 30 dias, o saldo ficará negativo e conforme for liberando a competência, mensalmente irá abater o saldo de 2,5 dias na contagem.

Ao finalizar as férias, ficará dessa forma:

Será encerrado o Período Aquisitivo, mostrará o saldo negativo onde mensalmente irá abater, até ficar zerado.

Foi criado um novo Período Aquisitivo na data 02/01/2021 à 01/01/2022.

2. Chapa 98765 - Tem direito a 8 dias de férias e tem **menos de um ano de casa**

Somente neste cenário, será lançado automaticamente a Licença Remunerada, pois o funcionário possui menos de um ano e não terá o saldo disponível para férias, portando 22 dias serão lançados como Licença Remunerada (Ao clicar em Lançar, demonstrará no envelope somente).

**OBSERVAÇÃO: Diferença do campo Saldo Total = 5 e Dias de Férias = 8**

O campo Saldo total, representa a quantidade de dias conforme a “competência atual do sistema”, como as férias foram cadastradas no mês 02, o saldo é: 2 avos \* 2,5 dias= 5 dias de férias

Sobre o campo Dias de Férias, como as férias está cadastrada para o dia 01/04/2020, funcionário terá direito a 3 avos, então 3 avos x  2,5 dias = 7,5 (arredonda para 8 dias de férias).

Portanto em resumo, Saldo Total valida a quantidade de dias conforme competência atual, Dias de Férias validando quantos dias conforme o mês das férias.

Dica

 ”Limita dias de direito”, pois o mesmo apenas deverá ser utilizado caso queira pagar apenas o que o funcionário possui de direito SEM licença remunerada.

3. Chapa 00014 Tem direito a 30 dias de férias

Foi lançado os 30 dias conforme direito, ao finalizar será encerrado e criado um novo Período Aquisitivo.

4. Chapa 00008 - Tem direito a 20 dias de férias, tem **mais** de um ano de casa e já tem cadastrado um período de gozo de 10 dias de férias (Antecipando conforme próximo Período Aquisitivo) Observação: Precisa marcar o parâmetro do sindicato: Permite antecipação de dias de férias do próximo período aquisitivo

Mesmo que o funcionário já tenha gozado 10 dias de férias nesse período aquisitivo, no novo período de gozo, mostrará 30 dias, porém teremos a aba Antecipação das Férias, demonstrando que 10 dias serão antecipados do próximo conforme print abaixo: 

Ao finalizar as Férias, ficará da seguinte forma:

No período aquisitivo fechado, ficará somente os 30 dias totais (10 que já existiam + 20 das Férias Coletivas), já no período aquisitivo novo, foi levado os “10 dias Férias Coletivas” referente ao antecipado:

**Parametrizações:**

Produto disponibiliza diversas parametrizações específicas para Férias Coletivas, tanto no Sindicato do Funcionário como no Parametrizador / Férias / Férias Coletivas, antes de realizar o processo, recomendamos a conferência dos parâmetros.

*Para o Sindicato, temos um Link detalhando o comportamento de todos os parâmetros: [Sindicato](https://tdn.totvs.com/display/public/LRM/Sindicatos)*

*Para o parametrizador da Folha de Pagamento:* [Licença Remunerada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020374831-RM-FOP-Licen%C3%A7a-Remunerada-Parametriza%C3%A7%C3%A3o)

**Explicação dos Parâmetros:**

**Considera data retorno para início período aquisitivo quando < 1 ano**

Marcando o parâmetro, o produto irá alterar a data fim do período aquisitivo do funcionário para o último dia das férias e ao criar o novo período aquisitivo, será considerado a data de retorno das férias.

Exemplo:  

Data das Férias Coletivas: 20/12/2017 até 31/12/2017

Período Aquisitivo do funcionário: 02/08/2017 - 01/08/2018

Parâmetro **Marcado**: Ao finalizar as férias, a data FINAL do Período Aquisitivo será alterada para: 31/12/2017

Parâmetro **Desmarcado**: Ao finalizar as férias, a data FINAL do Período Aquisitivo será alterada para: 19/12/2017

**Mantém período aquisitivo quando < 1 ano** 

Se marcado, o produto não irá alterar a data do período aquisitivo.

**Evento de pagamento da Licença Remunerada**

Informar um evento sem código de cálculo do tipo Provento e Dia com percentual igual a 1, ao lançar as Férias Coletivas para funcionários menores de 1 ano que não possui saldo necessário, será lançado automaticamente como licença remunerada.

**Motivo de afastamento por licença remunerada**

Para os dias em que o funcionário ficará como Licença Remunerada, o produto criará um histórico de afastamento automaticamente e passará o motivo de afastamento conforme passado no parâmetro em questão.
