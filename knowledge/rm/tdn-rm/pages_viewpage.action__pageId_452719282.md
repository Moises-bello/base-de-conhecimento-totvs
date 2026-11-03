---
content_hash: 0cc5e835c1448bb916e15fca332b8e0dd1f28a911188bf58b4c69c604bbd64b0
fetched_at: '2026-06-29T00:10:05.296821+00:00'
page_id: '452719282'
product: rm
source: tdn-rm
title: Parâmetros de Cálculo 1/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719282
version: 17
---

O objetivo desta etapa é definir como será a configuração de alguns parâmetros de cálculo.  
   
**Parâmetros**  
**Usa mês comercial para admissão**  
Selecione esta opção para que o sistema considere, para cálculo dos dias trabalhados na admissão o número de dias do mês comercial (30 dias). Se o campo não for marcado, o sistema irá considerar para o cálculo os dias trabalhados na admissão, o número de dias efetivos (28, 29, 30 ou 31), caso o funcionário seja admitido após o dia 01 do mês. Se o funcionário for admitido no dia 01 de algum mês que a quantidade de dias efetivos for diferente de 30 o sistema mesmo assim irá considerar 30 dias para o funcionário.   
**Exemplo**  
Mês 31 dias

|  |  |  |
| --- | --- | --- |
| Admissão | Parâmetro Desmarcado | Parâmetro Marcado |
| Funcionário admitido em 01/12 | 30 dias | 30 dias |
| Funcionário admitido em 02/12 | 30 dias | 29 dias |
| Funcionário admitido em 11/12 | 21 dias | 20 dias |
| Funcionário admitido em 16/12 | 16 dias | 15 dias |

Mês 28 dias

|  |  |  |
| --- | --- | --- |
| Admissão | Parâmetro Desmarcado | Parâmetro Marcado |
| Funcionário admitido em 01/02 | 30 dias | 30 dias |
| Funcionário admitido em 02/02 | 27 dias | 29 dias |
| Funcionário admitido em 11/02 | 18 dias | 20 dias |
| Funcionário admitido em 16/02 | 13 dias | 15 dias |

**Observação**  
O parâmetro acima só é válido para mensalista, no caso de Horista/Tarefeiro o sistema não verifica o parâmetro, considerando os dias efetivos do mês calendário

**Considera divisor pelo número de dias do mês na remuneração da Admissão e Demissão**  
Com esse parâmetro marcado, o fator divisor do numero de dias no mês na admissão ou demissão, será considerado o número de dias no mês.     
Se estiver desmarcado, o divisor será sempre 30, independente da quantidade de dias no mês.

**Atenção**  
O parâmetro acima não é válido para casos de Horista/Tarefeiro, o sistema não verifica o parâmetro, considerando sempre 30 dias.

**Considera data de admissão nos CC1 e CC2 nas transf. sem ônus**  
Com o parâmetro marcado, o sistema considera o cálculo do salário de acordo com a "Data de Admissão" do funcionário, ignorando a "Data de Transferência" que foi informada no menu registro no cadastro de funcionário.  
Com o parâmetro desmarcado, o sistema considera o cálculo do salário de acordo com a "Data de Transferência" que foi informada no menu registro no cadastro de funcionário.  
   
**Evento de código de cálculo 84 inibe evento de código de cálculo 04**  
Se o parâmetro for marcado, ao ser lançado o evento com o Código de Cálculo 84 - IRRF CALCULADO PELO USUÁRIO na movimentação do funcionário, o sistema irá zerar o evento com Código de Cálculo 4 - IRRF.  
Se o parâmetro não for marcado e for lançado na movimentação do funcionário o evento com o Código de Cálculo 84 - IRRF CALCULADO PELO USUÁRIO, o sistema irá considerar os dois eventos e se o valor informado no Código de Cálculo 84 for menor que o valor do evento com o Código de Cálculo 4. Caso o valor informado no evento de Código de Cálculo 84 for maior ou igual ao evento com o Código de Cálculo 4, o sistema irá zerar o evento com o Código de Cálculo 4.  
   
**Evento de código de cálculo 85 inibe evento de código de cálculo 03**  
Se o parâmetro for marcado, ao ser lançado o evento com o Código de Cálculo 85 - INSS CALCULADO PELO USUÁRIO na movimentação do funcionário, o sistema irá desconsiderar o evento com o Código de Cálculo 3 - INSS.   
Se o parâmetro não for marcado e for lançado na movimentação do funcionário o evento com o Código de Cálculo 85 - INSS CALCULADO PELO USUÁRIO, o sistema irá considerar os dois eventos desde que o valor informado no Código de Cálculo 85 seja menor que o valor do evento de Código de Cálculo 3. Caso o valor informado no evento de Código de Cálculo 85 for maior ou igual ao valor do evento de Código de Cálculo 3, o sistema irá desconsiderar o evento de Código de Cálculo 3.   
   
**Zerar evento de diferença quando o valor ficar negativo**  
Este parâmetro servirá para zerar o valor dos eventos que, no momento do cálculo, os valores forem negativos e com isso esses eventos não serão listados no envelope de pagamento nem gravados na tabela de ficha financeira.    
  
**Não zerar evento de fórmula quando valor retornado for negativo**  
Com este parâmetro marcado não será zerado o evento calculado por fórmula quando este retornar um valor negativo. Este tratamento é feito para eventos calculados por valor, hora e referência e que, o cálculo seja lançado no envelope de pagamento.

**Observação**  
Este parâmetro não interfere no cálculo do recibo de férias, zerando os eventos calculados por fórmula que retornarem valor negativo.  
**Proporcionaliza eventos**  
Com este parâmetro marcado, o sistema irá realizar o lançamento da movimentação, proporcionalizando os eventos do tipo valor que tiverem os seus parâmetros de proporcionalidade confirmados em Administração de Pessoal | Cadastros | Eventos, aba identificação, para funcionários que tiveram admissão, licença e/ou férias no mês da competência.   
Com o parâmetro desmarcado, o sistema realizará o lançamento da movimentação sem proporcionalidade também para estes funcionários.   
   
**Considera percentual de incidência integral para comissionista**

**Média de evento salário composto em meses anteriores deve atualizar valor com salário atual**  
Com este parâmetro marcado irá considerar o salário hora do funcionário para o cálculo de média do evento informado no salário composto quando o mesmo compor média e não faça mais parte da composição. Quando desmarcado irá considerar o valor informado na Ficha Financeira. Mais informações:

---

[<< Retornar para **Folha Normal**](http://tdn.totvs.com.br/display/LRM/Folha+Normal)
