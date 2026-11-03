---
content_hash: 9c9aa41ed4434382420a8fb56206ee55cf8606f504af1d324109a5720d461c56
fetched_at: '2026-06-29T00:10:03.914878+00:00'
page_id: '452719173'
product: rm
source: tdn-rm
title: Aviso Prévio Rescisão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719173
version: 10
---

Etapa onde será configurado como será feito o cálculo de aviso prévio  
**Campos e Parâmetros**  
   
   
Comum Acordo paga metade somente do aviso prévio, projeções consideram período completo  
Conforme o Art. 484-A ([{+}](http://www.planalto.gov.br/ccivil_03/Decreto-Lei/Del5452.htm#art484a)<http://www.planalto.gov.br/ccivil_03/Decreto-Lei/Del5452.htm#art484a+>), o contrato de trabalho poderá ser extinto por acordo entre empregado e empregador, caso em que serão devidas as seguintes verbas trabalhistas:  
I - por metade:  
a) o aviso prévio, se indenizado; e  
b) a indenização sobre o saldo do Fundo de Garantia do Tempo de Serviço, prevista no § 1º do art. 18 da Lei nº8.036, de 11 de Maio de 1990;  
II - na integralidade, as demais verbas trabalhistas.  
Com este entendimento, foi criado este parâmetro com o seguinte comportamento:  
Quando marcado, o sistema irá calcular o aviso prévio indenizado e pagando pela medida a parte devida do empregador. As demais verbas que são calculadas sobre a projeção do aviso prévio indenizado (Férias e 13º Salário) serão pagas na integralidade de dias de aviso prévio indenizado  
Com este parâmetro desmarcado, o sistema irá calcular e pagar o aviso prévio indenizado e as verbas sobre a projeção dos dias aviso prévio, na integralidade.

**Exemplo**  
Salário base: 2.766,49  
Data de demissão: 31/05  
Início do Aviso Prévio indenizado: 01/06  
Dias de aviso: 45  
Salário dia: 2.766,49/30 = 92,216333  
Calculo do Aviso prévio indenizado: 45 \* 92,216333 = 4.149,735   
   
*Com parâmetro marcado*  
Aviso prévio = 4.149,735 / 2 = **2.074,8675**  
13º salário indenizado = (2.766,49 / 12) \* 2 (avos) = **461,081667**  
Férias indenizadas sobre aviso prévio = (2.766,49 / 30) \* 5 (dias de férias) = **461,081667**  
   
*Com o parâmetro desmarcado*  
Aviso prévio = **4.149,735**  
13º salário indenizado = (2.766,49 / 12) \* 2 (avos) = **461,081667**  
Férias indenizadas sobre aviso prévio = (2.766,49 / 30) \* 5 (dias de férias) = **461,081667**  
   
**Observação**  
Caso o usuário queira que todas as verbas projetadas pelos dias de aviso prévio indenizado sejam pagas pela metade, deve informar no campo 'Dias de Aviso Indenizado', no processo de Rescisão, somente a metade dos dias de aviso. O Parâmetro deve está desmarcado, para o correto cálculo de todas as verbas de aviso prévio indenizado pela metade.   
   
**Atenção**  
Este parâmetro só interfere no cálculo do aviso prévio da Rescisão com o Tipo V (Comum Acordo) e quando o mesmo é indenizado. Caso o aviso prévio seja descontado não será descontado a metade, caso o parâmetro esteja marcado, sendo o mesmo descontado na integralidade dos dias de aviso prévio.

**Resc.Compl.recalcula fórmulas quando aumento salarial for posterior a demissão, durante a projeção do aviso:**

O sistema irá realizar o cálculo da Rescisão Complementar dos eventos que utilizam fórmula, com ou sem código de cálculo e quando no histórico salarial existir um aumento salarial  posterior a data de Demissão durante a projeção do aviso.

Veja também: [Resc.Compl.recalcula fórmulas quando aumento salarial for posterior a demissão , durante a projeção do aviso".](https://tdn.totvs.com.br/pages/viewpage.action?pageId=500286424)

**Resc.Compl. com aumento salarial posterior a demissão paga férias e 13º somente sobre dias após reajuste**

Quando a alteração salarial ocorre durante a projeção do aviso prévio e posterior ao mês da rescisão, ao calcular a rescisão complementar será pago diferença de férias indenizadas e diferença de 13º salário indenizado proporcionalizado a partir do dia da alteração salarial.

**Exemplo:** Funcionário foi demitido no mês março e teve aumento salarial por dissidio no mês de maio, supondo que a projeção do aviso indenizado foi até o dia 05/05 e o parâmetro está marcado, será calculada a diferença apenas dos 5 dias de aviso prévio e a proporcionalização da diferença da parte indenizada das Férias e 13º salário indenizado.

Atualmente o padrão é proporcionalizar somente a diferença do aviso prévio indenizado, sendo que Férias e 13º salário tem os valores de diferença calculados integralmente, considerando o valor do salário no último dia da projeção. Esse procedimento continua quando o parâmetro estiver desmarcado.

**Forçar incidência de INSS no CC62 e CC99 até a data:**  
A Solução de Consulta nº 99.014 que foi publicada pela Receita Federal do Brasil no Diário Oficial da União (DOU) 27/03/2017 informa que  o [aviso prévio](http://www.guiatrabalhista.com.br/guia/aviso_previo.htm) indenizado não integra a [base de cálculo](http://www.portaltributario.com.br/artigos/base-de-calculo-tributaria.htm) para fins de incidência das contribuições sociais previdenciárias incidentes sobre a folha.

De acordo com esta solução visando o correto funcionamento do sistema foi criado o campo   
**"Forçar incidência de INSS no CC62 e CC99 até a data:".**  
   
Até a data informada neste campo o sistema passará a exibir no envelope de pagamento na base de INSS o valor pago a título de Aviso Prévio Indenizado representado na folha pelo evento de Código de Cálculo 62 (CC 62 – Aviso Prévio) e sua Diferença pelo Código de Cálculo 99 (CC 99 - Dif. Aviso Prévio).   
   
**Exemplo:**  
No campo "Forçar incidência de INSS no CC62 e CC99 até a data:" está informado com uma data válida.  
   
Nesta data informada foram alterados os eventos de CC62 – Aviso Prévio e CC99 - Dif. Aviso Prévio desmarcando sua incidência em INSS.  
   
**01 -** Foram calculadas rescisões anteriores a esta data.  
   
Neste caso as rescisões foram calculadas com o evento de Código de Cálculo 62 incidindo em INSS. O valor do código de cálculo 62 SOMARÁ para a base de INSS no envelope pasta incidências, pois o evento INCIDIA em INSS e a data da rescisão é ANTERIOR à data informada no campo "Forçar incidência de INSS no CC62 e CC99 até a data:".  
   
**02 -** Foram calculadas rescisões posteriores a data informada no parâmetro "Forçar incidência de INSS no CC62 e CC99 até a data:".   
   
Neste caso estas rescisões foram calculadas com o evento CC 62 não incidindo em INSS. O valor do código de cálculo 62 NÃO SOMARÁ para a base de cálculo de INSS, pois o evento NÃO INCIDE em INSS e a data da rescisão é POSTERIOR à data informada no campo "Forçar incidência de INSS no CC62 e CC99 até a data:".  
   
**Observação:**  
Este parâmetro não estará preenchido, pois deve ser alterado pelo usuário de acordo com o seu entendimento e utilização da incidência de INSS nos eventos CC 62 – Aviso Prévio pagos nas rescisões e eventos CC 99 - Dif. Aviso Prévio pagos nas rescisões complementares. Este parâmetro não estará preenchido, pois deve ser alterado pelo usuário de acordo com o seu entendimento e utilização da incidência de INSS nos eventos CC 62 – Aviso Prévio pagos nas rescisões e eventos CC 99 - Dif. Aviso Prévio pagos nas rescisões complementares. Uma vez clicando no parâmetro este deve obrigatoriamente ser preenchido porque não poderá ficar em branco. Caso o usuário não queira uma validação neste momento poderá colocar uma data antiga.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Retornar para **Rescisão**
