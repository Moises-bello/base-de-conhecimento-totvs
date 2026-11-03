---
content_hash: b9c43e788a4b0526c0a9d26e747ae0cee47a6f8b4e57b78c2ce94c845960cf38
fetched_at: '2026-06-29T00:10:06.691337+00:00'
page_id: '452719329'
product: rm
source: tdn-rm
title: Cálculo - 13º Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719329
version: 2
---

Nesta etapa será definida como será feito o cálculo de 13º salário.  
    
 **Campos e Parâmetros**  
 Utiliza salário atual p/ 1ª parcela  
 Com este campo habilitado, o sistema assumirá como base de cálculo da 1ª parcela do 13º salário, o salário atual do mês de pagamento. Neste caso é verificado a alteração de salário no mês de pagamento (normalmente Novembro) ao invés do mês anterior (como prevê a legislação).  
 **Exemplo**  
 Histórico salarial do funcionário  
 01/02 - R$ 4000,00  
 01/11 - R$ 5000,00  
 Com o parâmetro marcado, o sistema assumirá para cálculo da 1ª parcela o salário de R$ 5000,00  
 Com o parâmetro desmarcado, o sistema assumirá para cálculo da 1ª parcela o salário de R$ 4000,00  
    
 Histórico salarial do funcionário  
 01/02 - R$ 4000,00  
 01/10 - R$ 5000,00  
 Neste caso o parâmetro não será influenciado, pois o funcionário não teve alteração de salário no mês de novembro (quando normalmente se paga a 1ª parcela. Será considerado o salário do mês 10 (R$ 5000,00)  
 Paga eventos adicionais na 1ª parcela do 13º salário  
 Com este parâmetro marcado, os eventos adicionais globais de 13º serão considerados no pagamento da 1ª parcela de 13º salário. Estes eventos não serão discriminados no movimento da 1ª parcela de 13º salário. Eles serão discriminados apenas no movimento da 2ª parcela de 13º salário.  
    
 Eventos código de cálculo 106 inibe evento código de cálculo 49  
 Se este parâmetro for marcado, ao ser lançado o evento com o Código de Cálculo 106 - IRRF 13º CALCULADO PELO USUÁRIO na movimentação do funcionário, o sistema irá zerar o evento com o Código de Cálculo 49 - IRRF 13º Salário. Se o parâmetro não for marcado, for lançado na movimentação do funcionário o evento com o CC 106 e este valor for menor que o evento de CC 49, que seja calculado automaticamente pelo sistema, o sistema irá considerar os dois eventos. Esta diferença será lançada no evento de CC 49. Caso o valor informado no evento CC 106 seja maior ou igual ao valor do evento de CC 49, o sistema irá zerar o evento CC 49.  
    
 Calcula avos p/ 1ª parcela considerando meses até Dezembro  
 Com este parâmetro marcado, o sistema passa a considerar Dezembro para cálculo da 1ª parcela do 13º salário o número de avos para funcionários admitidos no curso do ano, inclusive a partir de 18 de Janeiro do ano corrente.

**Exemplo**  
 Funcionário admitido em 01/02 do ano corrente  
 Com o parâmetro marcado, será considerado 11 avos para pagamento  
 Com o parâmetro desmarcado, será considerado 10 avos para pagamento  
    
 **Observação**  
 para funcionários admitidos em anos anteriores, este parâmetro não influência, sendo considerado sempre 12 avos para o cálculo da 1ª parcela do 13º salário  
    
 **Atenção**  
 Ao marcar este parâmetro, o sistema não permite marcar o parâmetro 'Calcula avos p/ 1ª parcela considerando meses até o atual'  
 Calcula avos p/ 1ª parcela considerando meses até o atual  
 Com este parâmetro marcado, o sistema passa a considerar o número de avos até o mês de pagamento da 1ª parcela do 13º salário (normalmente em Novembro), dos funcionários admitidos a partir de 18 de Janeiro do ano corrente.

**Exemplo**  
 Funcionário admitido em 01/02 do ano corrente  
 Com o parâmetro marcado será considerado 10 avos para pagamento  
 Com o parâmetro desmarcado será considerado 9 avos para pagamento  
    
 **Observação**  
 para funcionários admitidos em anos anteriores, este parâmetro não influência, sendo considerado sempre 12 avos para o cálculo da 1ª parcela do 13º salário  
    
 **Atenção**  
 Ao marcar este parâmetro, o sistema não permite marcar o parâmetro 'Calcula avos p/ 1ª parcela considerando meses até Dezembro'  
 Meses afastamento por acidente de trabalho reduz avos de 13º salário  
 Quando marcado, este parâmetro considera os afastamentos por Acidente de Trabalho (T) e Doença Ocupacional (O) para diminuir os avos de 13º salário que o funcionário tem direito. Se estiver desmarcado, estes tipos de afastamentos não afetará o calculo de número de avos de 13º salário.  
 **Observação**  
 Pela lei os afastamentos por acidente de trabalho não devem reduzir o número de avos de 13º, porém algumas empresas podem interpretar de outra forma ou terem previdência privada e desta forma não considerar estes afastamentos no cálculo de 13º salário  
    
 **Exemplo**  
 Afastamento por Acidente de Trabalho: 26/06 (16º dia seguinte ao do afastamento do trabalho até dia 21/10.  
 *Parâmetro marcado*: 6/12 avos (anterior ao afastamento) + 2/12 avos (posterior ao afastamento) = 8/12 avos  
 *Parâmetro desmarcado*: 12/12 avos (este afastamento não reduz avos de 13º salário)  
 Bloqueia reversão automática de 13º salário no mês de janeiro  
 Com este parâmetro marcado, no momento da realização da contabilização da provisão mensal de 13º salário no mês de janeiro, o sistema considerará o valor da provisão acumulada do mês anterior igual a zero. Portanto, a provisão mensal do mês de janeiro é a própria provisão acumulada do mês de Janeiro.  
 Esclarecemos que em Dezembro a provisão acumulada é relativa a 12/12 avos e em Janeiro a provisão acumulada é de apenas 1/12 avos. Ao final de um ano contábil, é necessário uma reversão nas contas de resultado de provisão da contabilidade. O TOTVS Folha de Pagamento faz isto automaticamente, quando o usuário opta pela provisão mensal (valor acumulado mês atual - valor acumulado do mês anterior), pois esta é negativa e o sistema inverte as contas débito/crédito. Esta reversão só ocorre no mês de Janeiro  
 Quando as empresas fazem a reversão por conta própria em Dezembro (o próprio contador faz um artifício contábil sem o conhecimento do TOTVS Folha de Pagamento para que seja zerada o conteúdo das contas de resultado de provisão), não é mais necessário a reversão automática das contas débito/crédito que o TOTVS Folha de Pagamento faz. Logo, este parâmetro possibilita o bloqueio desta reversão de contras automaticamente.

**Exemplos**  
 Mês de competência Janeiro  
 Provisão acumulada do mês atual (Janeiro): R$ 41,67 (1/12)  
 Provisão acumulada do mês anterior (Dezembro): R$ 522,47 (12/12)  
 Contabilização dos encargos tipos 7 (Provisão de 13º), 8 (Provisão FGTS de 13º) e 9 (Provisão Encargos de 13º)  
 Conta Débito: 1.0001.1  
 Conta Crédito: 2.0001.0  
 Cálculo da provisão Mensal = Provisão acumulada mês atual (Janeiro) - Provisão acumulada do mês anterior (Dezembro)  
    
 *Com parâmetro marcado:*  
 Resultado: R$ 41-67 - 0 = R$ 41,67  
    
 Lançamento Contábil:

* Conta Débito: 1.0001.0 = R$ 41,67
* Conta Crédito: 2.0001.0 = R$ 41,67

*Com parâmetro desmarcado:*  
 Resultado: R$ 41,67 - R$ 522,47 = R$ -480,80 (valor negativo - reversão das contas débito/crédito)  
    
 Lançamento Contábil:

* Conta Débito: 2.0001.0 = R$ 480,80
* Conta Crédito: 1.0001.0 = R4 480,80

Ignora eventos que incidem em salário  
 Com este parâmetro marcado, o sistema irá desconsiderar os eventos que incidem em salário para os cálculos da base de 13º salário. Caso contrário, todos os eventos que incidem no salário participarão do cálculo do 13º salário.   
 **Observação**  
 Os eventos devem ser lançados antes do cálculo do 13º salário.  
 Lança desconto de arredondamento (código de cálculo 21)  
 Com este parâmetro desmarcado, o sistema não irá lançar o evento com o código de cálculo 21 -  Arredondamento Descontos, no lançamento do 13º salário e será lançado o evento com o Código de Cálculo 314 - Arredondamento Desconto Base, armazenando o valor do arredondamento (CC 21), para que o mesmo seja descontado no próximo período.   
 Quando parâmetro está marcado, é lançado o evento de CC 21 para ser descontado da parcela de 13º salário.  
 **Atenção**  
 Este tratamento atenderá 1ª e 2ª parcela do 13º salário.  
    
 **Exemplo**  
 No período 1 foram realizados os seguintes lançamentos:

|  |  |  |  |
| --- | --- | --- | --- |
| Código | Descrição | Valor | Prov/Desc/Base |
| 0008 | Desconto de Falta | 1.000,00 | Desconto |
| 0020 | Arredondamento | 1.000,00 | Provento |
| Liquido | | 0,00 (zero) | |

*Com parâmetro desmarcado:*  
 No período 2 foi processado o lançamento da 1ª parcela

|  |  |  |  |
| --- | --- | --- | --- |
| Código | Descrição | Valor | Prov/Desc/Base |
| 0009 | 1ª parcela 13º | 500,00 | Provento |
| 0314 | Base Arredondamento (CC 314) | 1.000,00 | Base |
| Liquido | | 500,00 | |

No período 3 foi feito um lançamento para o funcionário. O arredondamento será descontado

|  |  |  |  |
| --- | --- | --- | --- |
| Código | Descrição | Valor | Prov/Desc/Base |
| 0002 | Provendo | 1.300,00 | Provento |
| 0021 | Arredondamento Desc. (CC 21) | 1.000,00 | Desconto |
| Liquido | | 300,00 | |

Valor a somar ao 13º salário  
 Selecione uma fórmula cujo resultado será somado na base de cálculo do 13º salário.  
    
 Valor a somar na Provisão de 13º salário  
 Selecione uma fórmula cujo resultado será somado na base de cálculo da provisão de 13º salário.  
    
 Provisão de Eventos Adicionais de 13º salário  
 Conforme a seleção dos parâmetros abaixo, o sistema irá considerar ou não os Eventos Adicionais de 13º Salário na Geração de Histórico de Provisões:

* Sempre Provisionar: Marcando esta opção, o sistema irá considera na Geração de Histórico de Provisões os Eventos Adicionais Globais de 13º salário.
* Nunca Provisionar: Marcando esta opção, o sistema não irá considera na Geração de Histórico de Provisões os Eventos Adicionais Globais de 13º salário.
* Provisionar de forma personalizada: Marcando esta opção, será habilitado nos Eventos Adicionais Globais o campo 'Provisionar Evento'. Com este campo será possível selecionar os eventos que irão ou não participar do cálculo da Geração do Histórico de Provisões.

|  |  |
| --- | --- |
|  | Informações Complementares |

[<<Voltar para tela anterior **13º Salário**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=452718783)
