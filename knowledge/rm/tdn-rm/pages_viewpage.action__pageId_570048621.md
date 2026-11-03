---
content_hash: 98944bcda654fd6de1a8f9041f2f092e2a1c36d27b64439b604c1d598899ab40
fetched_at: '2026-06-29T00:10:52.088731+00:00'
page_id: '570048621'
product: rm
source: tdn-rm
title: Cálculo 2/2 - Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=570048621
version: 11
---

Considera sábado no cálculo de dias para pagamento de férias  
Com este parâmetro marcado, o sistema irá considerar o sábado no cálculo da data que será apresentada no campo de pagamento das férias.

Permite recálculo de eventos de férias com fórmula no envelope  
Com o parâmetro marcado, os eventos que tem fórmula serão recalculados no envelope após o lançamento do recibo.  
Caso o parâmetro esteja desmarcado, os eventos não sofreram recálculo, permanecendo o valor calculado no recibo de férias.

**Atenção:**  
Lembramos que, o mais correto, é não permitir recalcular no envelope eventos já pagos no recibo de férias.  
Este parâmetro faz com que os valores de férias fiquem sobre inteira responsabilidade do usuário.  
Com ele marcado, qualquer evento de férias que tenha fórmula será recalculado.

Calcular Recibo de Férias Automaticamente  
Com este parâmetro marcado, o recibo de férias será calculado automaticamente sempre que o usuário fizer uma alteração e clicar em Salvar e/ou OK e o parâmetro 'Não Recalcular' disponível no recibo de férias estiver desmarcado.  
Caso este parâmetro Calcular Recibo de Férias Automaticamente esteja desmarcado, o recibo não será recalculado automaticamente, sendo necessário que o usuário execute o cálculo de férias manualmente toda vez que fizer uma alteração.

Diferença de média de férias antecipadas considera período até o vencimento

Utilize este parâmetro para pagar diferença de média de acordo com o período aquisitivo do funcionário quando estas férias foram antecipadas.

**Exemplo:** Período aquisitivo de 01/08/2019 a 31/07/2020, funcionário tem 30 dias de gozo de férias em 01/04/2020 a 30/04/2020.

Na competência 04/2020 o cálculo da média de hora extra considera 8 avos de férias. Portanto, o cálculo de média considera todas as horas extras de 08/2019 a 03/2020 e divide por 8. Após a finalização destas ferias, o período aquisitivo é fechado, e já é aberto o período aquisitivo futuro.

No mês 10/2020, será calculado o pagamento do 1/3 que a MP 927 permitiu que fosse adiado. Nesse momento deverá ser feito o cálculo da diferença para o pagamento da diferença de média conforme parâmetro acima marcado.

Com o **parâmetro marcado**, a média é recalculada pela diferença considerando o período aquisitivo completo, já que no momento atual o período aquisitivo já está vencido. Ou seja, considerará na média o período de 08/2019 a 07/2020 e divide por 12.

Com o **parâmetro desmarcado**, o processo que o sistema fará é refazer o cálculo do recibo exatamente na situação original. Então a média é recalculada com o mesmo período, de 08/2019 a 03/2020, e divide por 8.

Ignora lançamento da média no caso de recálculo com valor de diferença negativo

Marcando o parâmetro acima será habilitado a escolha se quer lançar o valor da média mesmo que a diferença seja um valor negativo.

O fato de mudar o período original de apuração da media pode tanto aumentar o valor, quanto pode também diminuir o valor desta media. O que antes era dividido por 8, passa a ser dividido por 12. Aumentar ou diminuir o valor vai depender do número de horas extras feitas depois do retorno das férias.

Para indicar se deve ou não descontar a diferença de media negativa do funcionário.

Esta verificação de valor negativo ou positivo é feita em cada grupo de media separado.

Permite alterar o saldo de salário das férias em meses de 31 dias  
Marcando este parâmetro, o sistema irá permitir que o usuário some mais um dia trabalhado ou horas normais correspondente a um dia, quando ocorrerem férias em meses de 31 dias.

**Exemplo**  
Férias de 10/10 a 08/11  
Considerando mês de Outubro - Dias trabalhados = 8 dias  
Se o parâmetro estiver marcado, o sistema permitirá que o usuário poderá alterar os dias trabalhados para 9 que o sistema permitirá o cálculo, pois Outubro tem 31 dias.  
Se o parâmetro estiver desmarcado e o usuário alterar os dias trabalhados para 9 dias, ao realizar o recálculo, o sistema retornará para 8 dias trabalhados.  
   
**Observação**  
Quando o parâmetro estiver marcado, deverá permitir que o usuário some mais um dia trabalhado ou horas normais correspondente a um dia, quando ocorrerem férias em meses de 31 dias, na folha normal e na rescisão.

Abono de Férias (importante para Diferença de Férias e Abono em Dobro)   
01- O sistema tem três opções para proceder o cálculo de **Diferença de Abono de Férias**:

* **Antes**: Escolhendo esta opção, o sistema não calculará a Diferença de Abono de Férias
* **Durante**: Escolhendo esta opção, o sistema calculará a Diferença de Abono de Férias proporcionalmente
* **Após**: Escolhendo esta opção, o sistema calculará a Diferença de Abono de Férias integralmente

02 - O sistema tem três opções para proceder o cálculo de **Abono de Férias em Dobro**:

Considerando a Data Limite como o último dia do período concessivo.

* **Antes**: Só paga o abono em dobro se a data de inicio das férias for posterior a Data Limite, dobra de todo o abono
* **Durante**: Paga somente os dias de férias que ocorrerem após a Data Limite
  + Se o número de dias posteriores for maior que o total de dias de abono, a dobra será de todo o abono
* **Após**: Se a data fim das férias for posterior a Data Limite, dobra todo o abono
  + Se a data fim das férias for anterior, é feita uma projeção com os dias de abono
  + Se a data projetada for após a Data Limite, dobra somente os dias que forem posteriores

Exemplo abono das férias em dobro

* **Antes**: Só paga o abono em dobro se a data de início das férias for posterior a Data Limite, dobra de todo o abono

Período aquisitivo de férias 17/06/2024 a 16/06/2025

Nas férias vence o dobro em 17/06/2026

início das férias em 15/06/2026 com abono - NÃO PAGA ABONO EM DOBRO

início das férias em 16/06/2026 com abono - NÃO PAGA ABONO EM DOBRO

início das férias em 17/06/2026 com abono - PAGA ABONO EM DOBRO INTEGRAL

* **Durante**: Paga somente os dias de férias que ocorrerem após a Data Limite
  + Se o número de dias posteriores for maior que o total de dias de abono, a dobra será de todo o abono

Período aquisitivo de férias 17/06/2024 a 16/06/2025

Nas férias vence o dobro em 17/06/2026

Férias de 01/06/2026 a 20/06/2026 com abono - PAGA ABONO EM DOBRO DE 04 DIAS (17 A 20/06)

Férias de 15/06/2026 a 04/07/2026 com abono - PAGA 10 DIAS DE ABONO PORQUE A QUANTIDADE DE DIAS DA DOBRA DAS FÉRIAS (18 DIAS - DE 17/06/2026 A 04/07/2026) É MAIOR QUE O TOTAL DE DIAS DE ABONO

Férias em 17/06/2026 a 06/07/2026 com abono - PAGA ABONO EM DOBRO INTEGRAL

* **Após**: Se a data fim das férias for posterior a Data Limite, dobra todo o abono
  + Se a data fim for anterior, é feita uma projeção com os dias de abono
  + Se a data projetada for após a Data Limite, dobra somente os dias que forem posteriores

Período aquisitivo de férias 17/06/2024 a 16/06/2025

Nas férias vence o dobro em 17/06/2026

Férias de 01/06/2026 a 20/06/2026 com abono - PAGA ABONO EM DOBRO DE 04 DIAS (17 A 20/06)

Férias de 15/06/2026 a 04/07/2026 com abono - PAGA ABONO EM DOBRO INTEGRAL

Férias em 17/06/2026 a 06/07/2026 com abono - PAGA ABONO EM DOBRO INTEGRAL

IMPORTANTE:

As versões que essa implementação do abono de férias em dobro está disponível está informada em [DT - Calcular as férias em dobro quando for referente ao abono pecuniário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1071995018)

Considera projeção dos dias de Abono para pagamento de Diferença

Esse parâmetro servirá para calcular a diferença na projeção do abono pecuniário quando a alteração salarial for retroativa e houver dias de abono pecuniário projetados na data do cálculo da diferença.

**Exemplo:**

Competência atual março/2022

Períodos de Férias  05 dias - 24/12/2021 a 28/12/2021        

                               18 dias - 07/02/2022 a 24/02/2022 COM ABONO DE 7 DIAS 

Alteração salarial em 01/03/2022 

Calculei diferença com data de pagamento de férias a partir de 01/02/2022

Com o parâmetro de pagamento de “Abono de Férias (importante apenas para cálculo da diferença)” marcado como “Após”, então o abono pecuniário seria de 25/02/2022 a 03/03/2022

E o parâmetro “Considera projeção dos dias de Abono para pagamento de Diferença” marcado, para efeito de cálculo a diferença de férias considera a projeção do abono pecuniário lançando o valor dos 3 dias de março.

---

<< Retornar para **Férias**
