---
content_hash: a4bcda277f48a92fc94f7d129643e0be6dde7ae28f91c569853a6359a78ea059
fetched_at: '2026-06-29T00:10:05.977687+00:00'
page_id: '452719307'
product: rm
source: tdn-rm
title: Sindicatos
type: documentation
url: https://tdn.totvs.com/display/LRM/Sindicatos
version: 15
---

Através deste cadastro é possível parametrizar as médias relativas a CLT ou Convenções Coletivas dos sindicatos dos trabalhadores.  
   
As parametrizações são divididas em abas e sub-abas que contém as definições específicas de média de Férias, média de 13º Salário, média de Aviso Prévio, média Licença Maternidade, média de Comissão e também Valores Associados do Sindicato e HomologNet.  
   
   
**Identificação**  
   
Valor Salário Mínimo  
O valor mínimo definido pelo sindicato para a categoria.   
Este campo é meramente informativo.   
   
   
Valor mínimo garantido  
O valor do mínimo garantido para os funcionários comissionados.   
Este valor é utilizado para o cálculo do salário base dos comissionados, com a seguinte consideração:  
   
Se a soma dos eventos que compõem o salário dos comissionados, dividido pelo número de meses para o cálculo da média, é menor que o valor do mínimo garantido, o cálculo das férias, 13º salário, aviso prévio e salário-maternidade serão sobre o valor do mínimo garantido.   
Se a média é maior, os cálculos serão sobre o valor da média.  
   
Este campo é utilizando também no cálculo dos eventos do tipo hora e dia, caso o funcionário não possua eventos que compõem o salário-comissão lançados na movimentação do mês de processamento.  
   
O valor da média é substituído pelo valor do mínimo garantido a partir do segundo mês, somente se o valor da média for de valor inferior ao mínimo garantido.  
   
   
Grupo de insalubridade  
É o grupo de média do evento com código de cálculo '22 - Insalubridade'.   
O cálculo de média deste evento é baseado no salário mínimo e não no salário do funcionário.  
   
   
Corrige média do tipo Hora de Insalubridade para o Salário Mínimo atual  
Será utilizado para que a média do evento de código de cálculo 22 – Insalubridade seja calculada no grupo informado proporcionalizando o valor de cada mês, corrigindo para o salário mínimo atual de acordo com as datas de vigência nos valores fixos.  
   
O cálculo fará uma regra de 3 com o valor do mês que tiver um salário mínimo diferente do atual.  
   
**Exemplo:**  
Competência atual = 02/2015  
Calculando média dos últimos 6 meses.  
Salário mínimo de 01/2014 até 12/2014 = 724,00  
Salário mínimo de 01/2015 até 12/2015 = 788,00  
No valor do código de cálculo 22 - Insalubridade dos meses 09/2014, 10/2014, 11/2014 e 12/2014 será feita a proporcionalização para o salário mínimo atual.  
Nos meses 01/2015 e 02/2015 não será necessária a proporcionalização, e será considerado o valor do evento na ficha financeira.  
   
**Observação:** O novo parâmetro só será considerado na média do tipo Hora, no Grupo de Insalubridade.  
   
   
Agência e DV  
O número da agência e digito verificador da conta corrente do Sindicato.   
Este campo é utilizado na emissão da GRCSU - Guia de Recolhimento da Contribuição Social Urbana.  
   
   
Fornecedor para lançamento financeiro  
O lançamento financeiro da GRCSU - Guia de Recolhimento da Contribuição Social Urbana considera o fornecedor registrado neste campo, caso haja parametrização dos lançamentos Financeiros por sindicato.  
   
**Observação:**  
Quando existir integração com TOTVS Gestão Financeira, a possibilidade de selecionar um fornecedor cadastrado como 'Global' é definida na parametrização do TOTVS Gestão Financeira.  
   
   
Desconta contribuição no mês de admissão  
Para que o desconto da contribuição sindical seja feito no mês de admissão do funcionário.   
Caso contrário, o desconto da contribuição é feito no mês seguinte ao da admissão.  
   
   
Vale Transporte - % de desconto  
Este percentual é verificado no cálculo do evento com código de cálculo '6-Vale Transporte' para os funcionários desta categoria.  
   
   
Vale Transporte – Desconto Único  
O desconto de vale transporte (código de cálculo 6) passa a considerar o somatório do valor do evento com código de cálculo '32-Total Entregue de Vale Transporte' de todos os períodos.  
Caso contrário, é considerado apenas o valor encontrado nos lançamentos do período.  
   
**Exemplo:**  
A empresa com funcionário semanalista lança a compra de vale transporte por semana (período), porém o desconto é apenas na última semana.  
Para esta situação deve marcar o parâmetro.  
   
   
Vale Transporte - Usa 30 dias p/ desconto  
Para considerar a base de vale transporte integral, caso contrário é considerado sobre os dias úteis preenchidos nos parâmetros de vale transporte do cadastro de funcionário.  
   
**Exemplo:**  
Salário: R$700,00  
Número de Dias úteis: 20 dias  
Quando habilitado o campo: R$700,00 \* 6% = R$42,00  
Quando não habilitado: (R$700,00 / 30) \* 20 = R$466,67  
R$466,67 \* 6% = R$28,00  
   
**Observação:**  
Sempre é comparado o valor encontrado com o total entregue de vale transporte e descontado o menor valor.  
   
   
Fórmula de estabilidade  
É utilizado na rescisão, impedindo o cadastramento da rescisão quando o resultado da fórmula é verdadeiro.  
Caso deseje que a fórmula seja apenas aviso, deve cadastrar em Configurações | Parametrizador | Rescisão.  
   
**Observação:**  
As funções de fórmula PAR, DTD e TABFUNC não podem ser utilizadas em fórmulas para estabilidade, devido utilizar valores já gravados no banco, e qualquer dado informado na tela de cadastro da Rescisão ainda não está gravado no banco.  
   
   
Fórmula para cálculo de indenização artigo 479  
É utilizada na rescisão para o cálculo do evento com código de cálculo '124 – Indenização Art. 479'.  
Caso não informe a fórmula, é utilizado o salário como base de cálculo do evento.   
   
   
Fórmula número de dias de aviso prévio  
Para atender a Lei 12.506/2011, que regulamenta o aviso prévio proporcional por tempo de serviço.  
A Lei 12.506/2011 prevê que o trabalhador com até um ano de emprego que for dispensado sem justa causa tem direito a 30 dias de aviso prévio, ou indenização correspondente, sendo que esse tempo é aumentado em 3 dias para cada ano adicional de serviço prestado, até o limite de 60 dias de acréscimo, ou seja, 90 dias de aviso prévio no total.  
   
**Exemplo fórmula:**  
MAX(30,MIN(90,((TCASA-1)\*3)+30))  
   
   
Lança indenização adicional na dispensa sem justa causa, no período de 30 dias antes da data base  
Este parâmetro será utilizado para lançar o evento de código de cálculo 344 – Indenização adicional na dispensa antes data base dentro do período de 30 dias que antecede a data base cadastrada. As informações de dia e mês da data base devem ser cadastradas para que o parâmetro calcule e lance o evento.  
**Exemplo:**  
Parâmetro marcado, data base 01/04 e rescisão com aviso prévio de 01/03 a 30/03 será lançado o valor da fórmula cadastrada no evento de código de cálculo 344 – Indenização Adicional na Dispensa antes Data Base.  
**Observação:** A data informada no sindicato não entra no cálculo de dias, portanto se o aviso for 03/03 terminando dia 01/04 não será pago o evento. Mais informações: [Código de Cálculo 344 - Indenização Adicional na Dispensa Antes Data Base](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718308)  
   
Endereço  
Informe nesta aba dados relativos a localização do Sindicato/Federação/Confederação  
   
   
**Média**  
Parametrização geral das médias Férias, 13º Salário, Aviso Prévio e Licença Maternidade.

**Atenção:**

* O sistema  grava  “todos os valores gerados no cálculo das médias” nas tabelas PFMEDIACALCULO,PFMEDCALCEVT , PFMEDCALCEVTMES , PFMEDCALCGRUPO ePFMEDCALCFORMADIC.
* O usuário poderá criar relatórios personalizados a partir das informações obtidas na tabelas mencionadas .
* Serão gravados também “valores do cálculo da média de comissão”.
* Caso haja fórmula com a função CALCMED não gravará valores nessas tabelas.
* Quando existir valor informado nos campos de 'Últimos Meses Per Aquisitivo', a forma de gravação nas tabelas  PFMEDIACALCULO,PFMEDCALCEVT , PFMEDCALCEVTMES , PFMEDCALCGRUPO ePFMEDCALCFORMADIC considerará a concatenação do valor informado nos campos de  'Últimos Meses Per. Aquisitivo' com o 99 informado em 'Número de meses' para gravar na coluna NMESESORIGINAL.

Considera mês de rescisão para média  
São considerados todos os eventos que incidem férias, 13º salário e aviso prévio no mês da rescisão.  
Caso contrário é considerado até o mês anterior.   
   
**Atenção:**  
Para considerar o mês da rescisão depende do próximo parâmetro.   
   
Considera mês atual se data (início férias/rescisão) menor do que 15  
É considerado o mês de gozo das férias/demissão para o cálculo das médias independente do dia das Férias/Rescisão.  
Caso contrário, somente é considerado quando o início de gozo ou data de demissão for maior ou igual a 15.  
   
**Observação:**  
Quando o cálculo da média é parametrizado por período aquisitivo e a data de início do gozo é maior que o término do período aquisitivo, este parâmetro não é considerado.  
   
   
Calcula média de salário comissão verificando número de meses de comissão  
O cálculo das médias das comissões recebidas (Salário Comissão), para cálculo da base de Férias, 13° Salário, Aviso Prévio ou Licença Maternidade, é feito sobre o valor total das comissões recebidas no período indicado no sindicato, dividido pelo número de meses em que o funcionário recebeu comissão.  
   
**Exemplo:**  
A apuração de médias de férias está parametrizada para considerar os últimos 12 meses de movimentação.   
O funcionário, com um tempo de casa superior a 12 meses, passou a ser comissionista a partir de Janeiro de 2009 e, consequentemente, o valor do campo Salário do cadastro do funcionário passou a ser 0,00.   
Nos meses de Janeiro, Fevereiro e Março esse funcionário teve a seguinte movimentação:  
Janeiro – Comissão no valor de R$ 1.500,00;  
Fevereiro – Comissão no valor de R$ 3.000,00;  
Março – Comissão no valor de R$ 2.500,00.  
   
Ou seja, recebeu comissões em três meses dentro do período de apuração.  
   
Entre os dias 01/04/2009 e 30/04/2009 esse funcionário irá gozar seus 30 dias de direito de férias. Com o parâmetro desmarcado o sistema irá apurar o salário comissão considerando os últimos 12 meses e no recibo de férias irão constar os seguintes pagamentos:  
   
Férias – 583,33 (1.500,00 + 3.000,00 + 2.500,00 = 7.000,00)  
   (7.000,00 / 12 = 583,33)  
1/3 de Férias – 194,43 (583,33 / 3 = 194,43).  
   
Se marcarmos o parâmetro, o sistema irá considerar o número de vezes que o funcionário recebeu comissões e os pagamentos encontrados no recibo ficarão conforme abaixo:  
   
Férias – 2.333,33 (1.500,00 + 3.000,00 + 2.500,00 = 7.000,00)  
   (7.000,00 / 3 = 2.333,33)  
1/3 de Férias – 777,78 (2.333,33 / 3 = 777,78).  
   
   
Utiliza parâmetros específicos para média de comissão  
É habilitada a aba Comissão, para que as parametrizações para média de comissão sejam específicas, isso é, não utilize as configurações do processo calculado (férias, 13º salário, Aviso Prévio e Licença Maternidade)  
   
Com a evolução do Labore em .Net a média para comissão teve sua parametrização evoluída no ambiente .Net. Foi criado o parâmetro no sindicato "Utiliza parâmetros específicos para média de Comissão" que quando marcado, a função de fórmula MEDCOMIS respeita o que foi definido na aba "Comissão" do cadastro do sindicato. Quando desmarcado obtém as parametrizações da aba Férias / Média de Férias. Este comportamento não foi evoluído em Delphi.  
Para que a função de fórmula MEDCOMIS seja compatível tanto em Delphi como em .Net o parâmetro "Utiliza parâmetros específicos para média de Comissão" deverá estar desmarcado.  
   
Caso use esta função de fórmula em relatórios Delphi este deve ser acionado pela nova MDI, pois os relatórios do gerador Delphi acionado pela nova MDI invoca as funções de fórmula do .Net contemplando toda sua evolução. E neste caso não haverá divergência de comportamento, devido a função MEDCOMIS usar todos os recursos implementados na nova plataforma.

Calcula média para aviso prévio descontado  
Será somado ao aviso prévio descontado o valor da média calculada.

**Exemplo:**

Salário 3676,00 + Média de aviso prévio 16,67 = Total 3692,67

Utiliza cálculo de média de Remuneração Base para Professor  
Caso esta opção seja marcada, será habilitada a aba "Remuneração Base" no sindicato, onde possuirá abas específicas para configuração da composição do salário base de todos os funcionários do tipo P – Professor nos cálculos de Férias, 13º Salário, Rescisão e Salário Maternidade.  
Para essa nova remuneração base, o sistema desconsiderará o salário composto do funcionário nos cálculos citados, e serão considerados todos os eventos que possuam o parâmetro "Compõe Remuneração Base de Professor" marcado, que tenham sido lançados na ficha financeira do funcionário de acordo com a parametrização a ser realizada para cada tipo de cálculo.  
   
   
**Férias | Parâmetros**  
   
Parametrizações específicas para o cálculo da média de férias.   
   
Permite antecipação de dias de férias do próximo período aquisitivo  
São antecipados dias de férias do próximo período aquisitivo quando o funcionário não tem saldo suficiente nas féria vencidas para total de dias de férias informado.  
   
No primeiro período, na pasta 'Antecipação de Férias' é informado o número de dias referente ao próximo período aquisitivo que foi antecipado, a data do final do período aquisitivo e a data de pagamento para identificar o período de gozo cadastrado para o próximo período aquisitivo.   
Estas datas são gravadas após finalizar as férias.  
   
No registro do próximo período aquisitivo que é criado, o parâmetro 'Período Antecipado' fica marcado, indicando que este período é referente a uma antecipação em período anterior, pois o mesmo não tem recibo de férias.  
   
Quando ocorrer saldo com valor fracionado (meio dia) é cadastrado como abono do primeiro período.  
Por exemplo 22.5 dias é cadastrado '0.5'.

Não pagar 0,5 dia de abono pecuniário quando o saldo de Férias for fracionado

Com o parâmetro "Não pagar 0,5 dia como abono pecuniário" marcado, no caso de antecipação de dias de férias com saldo de férias fracionado, não será cadastrado automaticamente 0,5 dia como abono pecuniário.

Vale ressaltar que o parâmetro somente estará habilitado se o parâmetro "Permite antecipação de dias de férias do próximo período aquisitivo" estiver marcado e seu efeito será aplicado exclusivamente para Férias Coletivas.

Ignora faltas em férias normais  
Não considera as faltas do período aquisitivo do funcionário para o cálculo das férias.   
**Observação:**  
Não é válido para o cálculo da rescisão.  
   
   
Ignora feriados na contagem das férias  
Verifica no calendário da seção do funcionário os feriados que tem o parâmetro 'Ignorar o dia na contagem das férias' marcado.  
Este parâmetro é considerado em todos os processos que envolvem férias, tais como provisão, variáveis de fórmulas, diferença de férias, finalização de férias, etc.  
   
**Observação:**   
Os dias de feriados desconsiderados são somados nos códigos de cálculos: 1-Horas Normais e 2-Dias Trabalhados.  
   
   
Paga férias proporcionais p/ demitidos por justa causa  
Calcula na rescisão férias proporcionais para funcionários demitidos pelo tipo '1 - Inic.Empregador com justa causa'.  
   
   
Paga férias proporcionais para demitidos com menos de 1 ano  
Pagamento de férias proporcionais para demitidos com menos de 1 ano com tipo de demissão igual '4-Inic.Empregado sem justa causa'.  
   
   
Mínimo para pagamento férias proporcionais  
É habilitado quando o parâmetro anterior está marcado.  
Devendo informar o número mínimo de meses para que o empregado tenha direito a férias proporcionais.   
É utilizado apenas em rescisões sem justa causa por iniciativa do empregado (pedido de demissão).  
   
   
Fórmula de Adicional Constitucional  
Permite utilizar percentual distinto do previsto na Constituição, por força de convenção ou contrato coletivo.   
Quando não informado a fórmula, é calculado 1/3 sobre as férias e médias.  
   
   
   
**Férias Coletivas**  
   
Menores 18 anos podem ter férias partidas  
Quando convenção ou acordo coletivo da categoria determinar que menores de 18 anos tenham Férias Coletivas partidas (menos de 30 dias).   
Caso contrário, as férias Coletivas serão concedidas apenas integralmente (30 dias) aos menores de 18 anos de idade, em conformidade com o artigo 134, parágrafo 2º da CLT.   
   
   
Paga licença para quem tem menos de 1 ano  
São lançados dias de licença remunerada para funcionário com menos de 1 ano de casa, quando os dias de gozo são maiores que os dias de direito. Caso não marque esse parâmetro será cadastrado, pelo processo que está em Férias / Coletivas Globais, apenas os dias de direito até o fim do período aquisitivo no mês informado no cadastro.  
**Atenção:** Em qualquer situação, ou seja, parâmetro "Paga licença para quem tem menos de 1 ano " marcado ou desmarcado, caso o funcionário não tenha dias de direito de férias quando for cadastrado pelo processo será apresentada a mensagem: "A Licença Remunerada deverá ser informada manualmente no Histórico de Afastamentos.".   
**Exemplo:**  
Funcionário admitido em 20/12/2023  
Período aquisitivo 20/12/2023 a 19/12/2024  
No mês de 12/2023 os dias de direito ainda está 0(zero) dia porque refere-se ao período de 20/12/2023 a 31/12/2023 totalizando 12 dias que não é permitido um avo de férias (2,5 dias)  
Supondo que seja cadastrado nas férias coletivas o período a partir de 26/12/2023, então será apresentada a mensagem para esse funcionário sem cadastrar licença, sendo possível fazer o cadastro através do histórico de afastamentos com o tipo R - Licença Remunerada.

DICA

Veja mais exemplos no parâmetro "Considera data retorno para início período aquisitivo quando < 1" que está em Parametrizador / Férias / Férias Coletivas TDN [Férias Coletivas](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719025)

Esse parâmetro também influenciará no cadastro das férias coletivas.

Paga dias de direito fracionados  
São cadastrados os dias de férias coletivas de acordo com os dias de direito fracionado do funcionário, ou seja, se o funcionário tem direito aos 17.5 dias, e é processado o cadastramento de 20 dias de férias coletivas, são cadastrados apenas 17.5 dias de férias e os 2.5 dias são cadastrados como licença remunerada.  
   
**Exemplo:**  
Dias de Férias Coletivas: 20  
Dias de direito do funcionário: 17.5  
Inicio: 18/11/2007  
Final: 05/12/2007  
   
Parâmetro desmarcado  
É cadastrado no campo 'Dias Férias' 18 dias e no campo 'Lic.prox.mês' são cadastros 2 dias. Que totalizam os 20 dias de férias coletivas.  
   
Parâmetro marcado  
É cadastrado no campo 'Dias Férias' 17.5 dias e no campo 'Lic.prox.mês'  2.5 dias de licença remunerada.  
   
   
Férias vencidas integrais  
Considera 30 (trinta) dias de férias adquiridas ao invés de considerar somente o período concedido pela empresa como Férias Coletivas.  
   
   
Paga férias cujo período aquisitivo ainda não começou  
Quando o funcionário tem idade menor que 18 anos ou maior que 50 anos e os parâmetros 'Menores 18 anos podem ter férias partidas' e 'Maiores 50 anos podem ter férias partidas' estão desmarcados, serão concedidas férias, embora seu novo período aquisitivo ainda não tenha começado.   
   
**Exemplo:**  
Funcionário com idade igual 52 anos;  
Competência: 12/2013  
Período aquisitivo: 05/03/2013 a 04/03/2014   
Férias coletivas: 15/12 a 30/12/2013  
Nesta situação em conformidade com o artigo 134, parágrafo 2º, da CLT, mesmo as férias coletivas sendo de 15 dias, este o funcionário gozou 30 dias de férias.   
E o novo período aquisitivo teve início em 05/03/2014.  
Em fevereiro de 2014, a empresa decide conceder mais 15 dias de Férias Coletivas.   
   
   
Maiores 50 anos podem ter férias partidas  
Quando convenção ou acordo coletivo da categoria determinar que maiores de 50 anos tenham Férias Coletivas partidas (menos de 30 dias).   
Caso contrário, as férias Coletivas serão concedidas apenas integralmente (30 dias), em conformidade com o artigo 134, parágrafo 2º da CLT.   
   
   
Proporcionais integrais para menos de 1 ano  
As férias do funcionário com menos de um ano de casa serão pagas integralmente, conforme dias adquiridos no momento do cadastramento das férias coletivas.  
   
**Exemplo**  
Dias de Férias Coletivas: 10  
Dias de direito: 22,5   
Neste caso, mesmo os dias de férias coletivas sendo 10, serão gozados 22,5 dias de férias.   
   
   
Completa período de férias quando saldo ficar menor que 10 dias  
Este parâmetro é considerado apenas para férias vencidas.  
Quando no cadastramento das férias coletivas restarem menos de 10 dias de saldo, serão concedidos os dias de férias conforme dias de direito.  
   
**Exemplo:**  
Funcionário tem férias vencidas e já gozou 15 dias.  
São concedidos 12 dias de férias coletivas  
Com o parâmetro marcado o funcionário terá 15 dias de férias coletivas.  
Caso contrário é concedido os 12 dias.   
   
   
   
**Férias | Média de Férias**  
   
Ignora média paga em evento de férias (comissionados)  
Os eventos de média relativos ao mês das férias gozadas anteriormente não entrarão para o cálculo da média atual, no caso de empregados comissionados.  
   
   
Considera mês das férias p/ cálculo de média  
Para considerar no cálculo das médias, os eventos que incidem em média de férias e foram pagos no mês de início de gozo das férias.  
   
**Exemplo:**  
Competência: 08/2013  
Período de gozo: 15/08 a 29/08/2013  
Os eventos que incidem em média de férias e foram pagos na competência 08/2013 serão considerados no cálculo das médias.   
   
**Atenção:**  
Lembrando que, quando o inicio de gozo é menor que dia 15, este parâmetro depende do parâmetro 'Considera mês atual se data (início férias/rescisão) menor do que 15' existente na aba de Médias.  
   
   
Despreza fórmula base salário  
As fórmulas adicionais cadastradas nos parâmetros de férias existente no módulo Parametrizador serão desconsideradas para os cálculos de médias.  
   
**Observação:**  
Este parâmetro influencia apenas o cálculo das médias.  
   
   
Desconsidera o mês em que houver período de férias também para a soma dos valores  
Para desconsiderar eventos que incide em médias, e foram pagos no mês do período de gozo das férias.   
   
**Atenção:**  
Este parâmetro depende do próximo parâmetro 'Desconsidera para contagem o mês em que houver período de férias igual ou maior'.  
   
**Exemplo:**  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Evento do tipo valor que incidem em média de férias lançados em:  
03/2013 = 100,00  
06/2013 = 100,00  
Média dos últimos 6 meses  
   
Com o parâmetro desmarcado  
São considerados os dois valores e o valor encontrado é divido por 6 para retorna a média.  
   
Com o parâmetro marcado e o campo 'Desconsidera para contagem o mês em que houver período de férias igual ou maior' informado 8.  
Os meses 03/2013 e 04/2013 são desconsiderados no cálculo da média, tanto para o divisor do cálculo da média como para buscar valores de eventos que incidem na média.  
   
   
Desconsidera para contagem o mês em que houver período de férias igual ou maior  
Para desconsiderar o mês do período de gozo das férias no divisor do cálculo das médias.  
O dia informado neste parâmetro compara com a quantidade de dias de férias no mês.  
   
**Exemplo I:**  
Parâmetro = 8 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso serão desconsiderados os meses 03 e 04/2013 no divisor da média, devido no mês 03/2013 ter 22 dias de férias e no mês 04/2013 ter 8 dias de férias.  
   
**Exemplo II:**  
Parâmetro = 10 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso é desconsiderado apenas o mês 03 no divisor da média.  
   
**Atenção I:**  
Caso não deseje desconsiderar o mês deve informar 31 neste campo.  
   
**Atenção II:**  
Este parâmetro não depende do parâmetro anterior. Caso o parâmetro anterior 'Desconsidera o mês em que houver período de férias também para a soma dos valores' esteja desmarcado, o período do gozo de férias é desconsiderado apenas no divisor da média.  
   
   
Utiliza parâmetros específicos para média de férias na rescisão  
É habilitada a aba 'Média de Férias na Rescisão' para que as parametrizações sejam específicas para a rescisão, isso é, não utilize as configurações da aba 'Média de Férias'.  
   
   
Substitui período de férias por meses anteriores  
Quando este parâmetro estiver marcado será verificado a informação do parâmetro "Desconsidera para contagem o mês em que houver período de férias igual ou maior", para verificar se o mês de gozo será considerado para o cálculo das médias. Caso o mês não seja considerado, o sistema irá substitui-lo pelo mês anterior ao início de período de apuração de média.  
   
**Exemplo:**  
Sindicado parametrizado para calcular média dos 6 últimos meses, caso em um destes meses o funcionário tenha gozado férias, o sistema irá considerar os últimos 7 meses, desconsiderando o mês de gozo.   
   
Cálculo de média de 13º dos últimos 6 meses  
Competência: dezembro.   
Período de apuração das médias: 07 a 12  
Período de gozo: 15/09 a 14/10, ou seja, 16 dias do mês de Setembro e 14 dias do mês de Outubro.  
Considerando que o parâmetro "Nº dias de férias para que o mês seja desconsiderado na contagem para a média" esteja com 12 dias, serão desconsiderados os 2 meses no cálculo das médias.  
Com o parâmetro desmarcado, serão considerados os eventos na ficha financeira dos meses 7, 8, 11 e 12, e a divisão será por 4.  
Com o parâmetro marcado, os meses desconsiderados 9 e 10 serão substituídos pelos 2 meses anteriores ao mês inicial do período de apuração, ou seja, meses 5, 6, 7, 8, 11 e 12, e o número de meses não é alterado, fazendo a divisão por 6.  
Se o parâmetro "Nº dias de férias para que o mês seja desconsiderado na contagem para a média" estivesse com 15 dias, seria desconsiderado apenas o mês 9, que tem 16 dias de férias, ou seja, somente o mês 09 seria substituído pelo mês 06.   
**Observação:**  
Este parâmetro foi disponibilizado em todas as pastas de Médias do Cadastro de Sindicato (Férias, 13º Salário, Aviso Prévio e Salário Maternidade).  
   
**Atenção**   
Este parâmetro não é valido caso a média seja por período aquisitivo  
   
   
Considera soma total da competência para buscar maiores valores   
Com o parâmetro marcado, serão consideradas as competências onde as somas totais dos valores são os maiores.  
Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo, ou seja serão considerados os maiores valores acumulados por grupo de média.  
   
   
**Exemplo:**  
Os 3 (três) eventos abaixo incidem em média:

0082 - Hora Extra 50% - Evento tipo Hora (Incide em Média no Grupo 1)

0083 - Hora Extra 100% - Evento tipo Hora (Incide em Média no Grupo 1)

0084 - Comissão - Evento tipo Valor (Incide em Média no Grupo 2)  
   
Competência atual 06/2016. Cálculo dos últimos 5 meses, considerando os 3 maiores valores.  
   
**Ficha Financeira**  
01/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        500,00

0084 - Comissão                   300,00

Total Grupo 1 = 700,00  
Total Grupo 2 = 300,00  
Total da competência = 1.000,00  
   
02/2016

0082 - Hora Extra 50%          400,00

0083 - Hora Extra 100%        100,00

0084 – Comissão                   800,00    
Total Grupo 1 = 500,00  
Total Grupo 2 = 800,00  
Total da competência = 1.300,00  
   
03/2016

0082 - Hora Extra 50%          100,00

0083 - Hora Extra 100%        500,00

0084 – Comissão                   200,00     
Total Grupo 1 = 600,00     
Total Grupo 2 = 200,00  
Total da competência = 800,00  
   
04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00

0084 – Comissão                   400,00    
Total Grupo 1 = 800,00     
Total Grupo 2 = 400,00  
Total da competência = 1.200,00  
   
05/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        100,00

0084 – Comissão                   600,00     
Total Grupo 1 = 300,00     
Total Grupo 2 = 600,00  
Total da competência = 900,00  
   
No exemplo acima, com o parâmetro marcado, serão consideradas as competências, onde as somas totais dos valores são os maiores, ou seja, meses 01/2016, 02/2016 e 04/2016.  
**Grupo 1**

01/2016

0082 - Hora Extra 50%          200,00    
0083 - Hora Extra 100%        500,00

02/2016

0082 - Hora Extra 50%          400,00

0083 - Hora Extra 100%        100,00

04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00  
   
Total Grupo 1 = 700,00 + 500,00 + 800,00 = 2.000,00 / 3 = **666,67**  
   
**Grupo 2**

01/2016

0084 – Comissão                   300,00

02/2016

0084 – Comissão                   800,00

04/2016

0084 – Comissão                   400,00  
   
Total Grupo 2 = 300,00 + 800,00 + 400,00 = 1.500,00 / 3 = **500,00**  
   
Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo, ou seja, meses 01/2016, 03/2016 e 04/2016 para o Grupo 1, e meses 02/2016, 04/2016 e 05/2016 para o Grupo 2.

**Grupo 1**

01/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        500,00

03/2016

0082 - Hora Extra 50%          100,00

0083 - Hora Extra 100%        500,00

04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00  
   
Total Grupo 1 = 700,00 + 600,00 + 800,00 = 2.100,00 / 3 = **700,00**  
   
**Grupo 2**

02/2016

0084 – Comissão                   800,00

04/2016

0084 – Comissão                   400,00

05/2016

0084 – Comissão                   600,00  
   
 Total Grupo 2 = 800,00 + 400,00 + 600,00 = 1.800,00 / 3 = **600,00**  
   
   
Mês da admissão entra para cálculo se admitido até dia  
Informar o dia limite para verificar se o mês da admissão é considerado no cálculo das médias.  
Quando informado 0 (zero) o mês de admissão não é considerado.  
Quando informado 31 o mês de admissão é sempre considerado.  
   
**Exemplo:**  
Mês da admissão entra para o cálculo se admitido até dia = 15   
   
Admissão = 14/01  
O mês de janeiro é considerado para o cálculo das médias.  
   
Admissão = 16/01  
O mês de janeiro é desconsiderado para o cálculo das médias.  
   
   
   
**Tipo de Cálculo, Correção de Valores, Habitualidade e Parâmetros Relacionados a Afastamentos** Informações  
   
   
   
**13º Salário | Média de 13º**  
   
Considera ano anterior p/ médias  
Considerar meses do ano anterior para o cálculo da média do 13º salário.  
De acordo com a CLT, a média de 13º salário somente poderá envolver eventos relativos ao ano a que se refere o 13º, mas acordos coletivos podem alterar esta restrição.  
   
   
Paga média na 1ª parcela  
Para o caso em que as médias são pagas também na 1ª parcela do 13º salário.  
   
   
Despreza fórmula base salário  
As fórmulas adicionais cadastradas nos parâmetros de 13º salário existente no módulo Parametrizador serão desconsideradas para os cálculos de médias.  
   
**Observação:**  
Este parâmetro influencia apenas o cálculo das médias.  
   
   
Desconsidera o mês em que houver período de férias também para a soma dos valores  
Para desconsiderar eventos que incide em médias, e foram pagos no mês do período de gozo das férias.   
   
**Atenção:**  
Este parâmetro depende do próximo parâmetro 'Desconsidera para contagem o mês em que houver período de férias igual ou maior'.  
   
**Exemplo:**  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Evento do tipo valor que incidem em média de férias lançados em:  
03/2013 = 100,00  
06/2013 = 100,00  
Média dos últimos 6 meses  
   
Com o parâmetro desmarcado:  
São considerados os dois valores e o valor encontrado é divido por 6 para retorna a média.  
   
Com o parâmetro marcado e o campo 'Desconsidera para contagem o mês em que houver período de férias igual ou maior' informado 8.  
Os meses 03/2013 e 04/2013 são desconsiderados no cálculo da média, tanto para o divisor do cálculo da média como para buscar valores de eventos que incidem na média.  
   
   
Desconsidera para contagem o mês em que houver período de férias igual ou maior  
Para desconsiderar o mês do período de gozo das férias no divisor do cálculo das médias.  
O dia informado neste parâmetro compara com a quantidade de dias de férias no mês.  
   
**Exemplo I:**  
Parâmetro = 8 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso serão desconsiderados os meses 03 e 04/2013 no divisor da média, devido no mês 03/2013 ter 22 dias de férias e no mês 04/2013 ter 8 dias de férias.  
   
**Exemplo II:**  
Parâmetro = 10 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso é desconsiderado apenas o mês 03 no divisor da média.  
   
**Atenção I:**  
Caso não deseje desconsiderar o mês deve informar 31 neste campo.  
   
**Atenção II:**  
Este parâmetro não depende do parâmetro anterior. Caso o parâmetro anterior 'Desconsidera o mês em que houver período de férias também para a soma dos valores' esteja desmarcado, o período do gozo de férias é desconsiderado apenas no divisor da média.  
   
   
Utiliza parâmetros específicos para média de 13º rescisão  
É habilitada a aba 'Média de 13º na Rescisão' para que as parametrizações sejam específicas para a rescisão, isso é, não utilize as configurações da aba 'Média de 13º'.  
   
   
Considera mês atual p/ cálculo de média de 13º  
Para considerar no cálculo das médias, os eventos que incidem em média de 13º salário e foram pagos no mês do cálculo.  
   
   
Considera fórmula adicional na 1ª parcela de 13º  
Para considerar no cálculo da 1ª parcela de 13º salário as fórmulas informadas em Configurações | Parametrizador | 13º Salário | Fórmulas Adicionais.   
   
   
Mês da admissão entra para cálculo se admitido até dia   
Informar o dia limite para verificar se o mês da admissão é considerado no cálculo das médias.  
Quando informado 0 (zero) o mês de admissão não é considerado.  
Quando informado 31 o mês de admissão é sempre considerado.  
   
   
Considera soma total da competência para buscar maiores valores   
Com o parâmetro marcado, serão consideradas as competências onde as somas totais dos valores são os maiores.  
Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo, ou seja serão considerados os maiores valores acumulados por grupo de média.  
   
   
**Exemplo:**  
Os 3 (três) eventos abaixo incidem em média:  
0082 - Hora Extra 50% - Evento tipo Hora (Incide em Média no Grupo 1) 0083 - Hora Extra 100% - Evento tipo Hora (Incide em Média no Grupo 1) 0084 - Comissão - Evento tipo Valor (Incide em Média no Grupo 2)  
   
Competência atual 06/2016. Cálculo dos últimos 5 meses, considerando os 3 maiores valores.  
   
**Ficha Financeira**  
01/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        500,00

0084 - Comissão                   300,00     
Total Grupo 1 = 700,00  
Total Grupo 2 = 300,00  
Total da competência = 1.000,00  
   
02/2016     0082 - Hora Extra 50%          400,00         0083 - Hora Extra 100%        100,00     0084 – Comissão                   800,00    
Total Grupo 1 = 500,00  
Total Grupo 2 = 800,00  
Total da competência = 1.300,00  
   
03/2016

0082 - Hora Extra 50%          100,00

0083 - Hora Extra 100%        500,00

0084 – Comissão                   200,00     
Total Grupo 1 = 600,00     
Total Grupo 2 = 200,00  
Total da competência = 800,00  
   
04/2016     0082 - Hora Extra 50%          600,00       0083 - Hora Extra 100%        200,00     0084 – Comissão                   400,00    
Total Grupo 1 = 800,00     
Total Grupo 2 = 400,00  
Total da competência = 1.200,00  
   
05/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        100,00

0084 – Comissão                   600,00     
Total Grupo 1 = 300,00     
Total Grupo 2 = 600,00  
Total da competência = 900,00  
   
No exemplo acima, com o parâmetro marcado, serão consideradas as competências, onde as somas totais dos valores são os maiores, ou seja, meses 01/2016, 02/2016 e 04/2016.  
**Grupo 1**

01/2016

0082 - Hora Extra 50%          200,00    
0083 - Hora Extra 100%        500,00

02/2016

0082 - Hora Extra 50%          400,00

0083 - Hora Extra 100%        100,00

04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00  
   
Total Grupo 1 = 700,00 + 500,00 + 800,00 = 2.000,00 / 3 = **666,67**  
   
**Grupo 2**

01/2016

0084 – Comissão                   300,00

02/2016

0084 – Comissão                   800,00

04/2016

0084 – Comissão                   400,00  
   
Total Grupo 2 = 300,00 + 800,00 + 400,00 = 1.500,00 / 3 = **500,00**  
   
Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo, ou seja, meses 01/2016, 03/2016 e 04/2016 para o Grupo 1, e meses 02/2016, 04/2016 e 05/2016 para o Grupo 2.  
**Grupo 1** 01/2016                                 0082 - Hora Extra 50%          200,00       0083 - Hora Extra 100%        500,00  
03/2016     0082 - Hora Extra 50%          100,00     0083 - Hora Extra 100%        500,00  
04/2016     0082 - Hora Extra 50%          600,00     0083 - Hora Extra 100%        200,00  
   
Total Grupo 1 = 700,00 + 600,00 + 800,00 = 2.100,00 / 3 = **700,00**  
   
**Grupo 2**

02/2016

0084 – Comissão                   800,00

04/2016

084 – Comissão                   400,00

05/2016

0084 – Comissão                   600,00  
   
Total Grupo 2 = 800,00 + 400,00 + 600,00 = 1.800,00 / 3 = **600,00**  
   
   
**Tipo de Cálculo, Correção de Valores, Habitualidade e Parâmetros Relacionados a Afastamentos** Informações  
   
   
   
**Aviso Prévio | Parâmetros de Média**  
   
Despreza fórmula base salário  
As fórmulas adicionais cadastradas nos parâmetros de Rescisão existente no módulo Parametrizador serão desconsideradas para os cálculos de médias.  
   
   
Desconsidera o mês em que houver período de férias também para a soma dos valores  
Para desconsiderar eventos que incide em médias, e foram pagos no mês do período de gozo das férias.   
   
**Atenção:**  
Este parâmetro depende do próximo parâmetro 'Desconsidera para contagem o mês em que houver período de férias igual ou maior'.  
   
**Exemplo:**  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Evento do tipo valor que incidem em média de férias lançados em:  
03/2013 = 100,00  
06/2013 = 100,00  
Média dos últimos 6 meses  
   
Com o parâmetro desmarcado:  
São considerados os dois valores e o valor encontrado é divido por 6 para retorna a média.  
   
Com o parâmetro marcado e o campo 'Desconsidera para contagem o mês em que houver período de férias igual ou maior' informado 8.  
Os meses 03/2013 e 04/2013 são desconsiderados no cálculo da média, tanto para o divisor do cálculo da média como para buscar valores de eventos que incidem na média.  
   
   
Desconsidera para contagem o mês em que houver período de férias igual ou maior  
Para desconsiderar o mês do período de gozo das férias no divisor do cálculo das médias.  
O dia informado neste parâmetro compara com a quantidade de dias de férias no mês.  
   
**Exemplo I:**  
Parâmetro = 8 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso serão desconsiderados os meses 03 e 04/2013 no divisor da média, devido no mês 03/2013 ter 22 dias de férias e no mês 04/2013 ter 8 dias de férias.  
   
**Exemplo II:**  
Parâmetro = 10 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso é desconsiderado apenas o mês 03 no divisor da média.  
   
**Atenção I:**  
Caso não deseje desconsiderar o mês deve informar 31 neste campo.  
   
**Atenção II:**  
Este parâmetro não depende do parâmetro anterior. Caso o parâmetro anterior 'Desconsidera o mês em que houver período de férias também para a soma dos valores' esteja desmarcado, o período do gozo de férias é desconsiderado apenas no divisor da média.  
   
   
Mês da admissão entra para cálculo se admitido até dia   
Informar o dia limite para verificar se o mês da admissão é considerado no cálculo das médias.  
Quando informado 0 (zero) o mês de admissão não é considerado.  
Quando informado 31 o mês de admissão é sempre considerado.  
   
   
Considera soma total da competência para buscar maiores valores   
Com o parâmetro marcado, serão consideradas as competências onde as somas totais dos valores são os maiores.  
Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo, ou seja serão considerados os maiores valores acumulados por grupo de média.  
   
   
**Exemplo:**  
Os 3 (três) eventos abaixo incidem em média:  
0082 - Hora Extra 50% - Evento tipo Hora (Incide em Média no Grupo 1) 0083 - Hora Extra 100% - Evento tipo Hora (Incide em Média no Grupo 1) 0084 - Comissão - Evento tipo Valor (Incide em Média no Grupo 2)  
   
Competência atual 06/2016. Cálculo dos últimos 5 meses, considerando os 3 maiores valores.  
   
**Ficha Financeira**  
01/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        500,00

0084 - Comissão                   300,00     
Total Grupo 1 = 700,00  
Total Grupo 2 = 300,00  
Total da competência = 1.000,00  
   
02/2016

0082 - Hora Extra 50%          400,00

0083 - Hora Extra 100%        100,00

0084 – Comissão                   800,00    
Total Grupo 1 = 500,00  
Total Grupo 2 = 800,00  
Total da competência = 1.300,00  
   
03/2016

0082 - Hora Extra 50%          100,00

0083 - Hora Extra 100%        500,00

0084 – Comissão                   200,00

Total Grupo 1 = 600,00     
Total Grupo 2 = 200,00  
Total da competência = 800,00  
   
04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00

0084 – Comissão                   400,00    
Total Grupo 1 = 800,00     
Total Grupo 2 = 400,00  
Total da competência = 1.200,00  
   
05/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        100,00

0084 – Comissão                   600,00     
Total Grupo 1 = 300,00     
Total Grupo 2 = 600,00  
Total da competência = 900,00  
   
No exemplo acima, com o parâmetro marcado, serão consideradas as competências, onde as somas totais dos valores são os maiores, ou seja, meses 01/2016, 02/2016 e 04/2016.  
**Grupo 1**

01/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        500,00

02/2016

0082 - Hora Extra 50%          400,00

0083 - Hora Extra 100%        100,00

04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00  
   
Total Grupo 1 = 700,00 + 500,00 + 800,00 = 2.000,00 / 3 = **666,67**  
   
**Grupo 2**

01/2016

0084 – Comissão                   300,00

02/2016

0084 – Comissão                   800,00

04/2016

0084 – Comissão                   400,00  
   
Total Grupo 2 = 300,00 + 800,00 + 400,00 = 1.500,00 / 3 = **500,00**  
   
Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo, ou seja, meses 01/2016, 03/2016 e 04/2016 para o Grupo 1, e meses 02/2016, 04/2016 e 05/2016 para o Grupo 2.  
**Grupo 1**

01/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        500,00

03/2016

0082 - Hora Extra 50%          100,00

0083 - Hora Extra 100%        500,00

04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00  
   
Total Grupo 1 = 700,00 + 600,00 + 800,00 = 2.100,00 / 3 = **700,00**  
   
**Grupo 2**

02/2016

0084 – Comissão                   800,00

04/2016

0084 – Comissão                   400,00

05/2016

0084 – Comissão                   600,00  
   
Total Grupo 2 = 800,00 + 400,00 + 600,00 = 1.800,00 / 3 = **600,00**  
   
   
**Tipo de Cálculo, Correção de Valores, Habitualidade e Parâmetros Relacionados a Afastamentos** Informações  
   
   
   
    
**Licença Maternidade | Parâmetros de Média**  
   
   
Despreza fórmula base salário  
As fórmulas adicionais cadastradas nos parâmetros de Folha Normal existente no módulo Parametrizador serão desconsideradas para os cálculos de médias.  
   
   
Desconsidera para contagem o mês em que houver período de férias igual ou maior  
Para desconsiderar o mês do período de gozo das férias no divisor do cálculo das médias.  
O dia informado neste parâmetro compara com a quantidade de dias de férias no mês.  
   
**Exemplo I:**  
Parâmetro = 8 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso serão desconsiderados os meses 03 e 04/2013 no divisor da média, devido no mês 03/2013 ter 22 dias de férias e no mês 04/2013 ter 8 dias de férias.  
   
**Exemplo II:**  
Parâmetro = 10 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso é desconsiderado apenas o mês 03 no divisor da média.  
   
**Atenção I:**  
Caso não deseje desconsiderar o mês deve informar 31 neste campo.  
   
   
Mês da admissão entra para cálculo se admitido até dia   
Informar o dia limite para verificar se o mês da admissão é considerado no cálculo das médias.  
Quando informado 0 (zero) o mês de admissão não é considerado.  
Quando informado 31 o mês de admissão é sempre considerado.  
   
   
Considera soma total da competência para buscar maiores valores   
Com o parâmetro marcado, serão consideradas as competências onde as somas totais dos valores são os maiores.  
Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo, ou seja serão considerados os maiores valores acumulados por grupo de média.  
   
   
**Exemplo:**  
Os 3 (três) eventos abaixo incidem em média:  
0082 - Hora Extra 50% - Evento tipo Hora (Incide em Média no Grupo 1) 0083 - Hora Extra 100% - Evento tipo Hora (Incide em Média no Grupo 1) 0084 - Comissão - Evento tipo Valor (Incide em Média no Grupo 2)  
   
Competência atual 06/2016. Cálculo dos últimos 5 meses, considerando os 3 maiores valores.  
   
**Ficha Financeira**  
01/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        500,00

0084 - Comissão                   300,00     
Total Grupo 1 = 700,00  
Total Grupo 2 = 300,00  
Total da competência = 1.000,00  
   
02/2016

0082 - Hora Extra 50%          400,00

0083 - Hora Extra 100%        100,00

0084 – Comissão                   800,00    
Total Grupo 1 = 500,00  
Total Grupo 2 = 800,00  
Total da competência = 1.300,00  
   
03/2016

0082 - Hora Extra 50%         100,00

0083 - Hora Extra 100%        500,00

0084 – Comissão                   200,00     
Total Grupo 1 = 600,00     
Total Grupo 2 = 200,00  
Total da competência = 800,00  
   
04/2016

0082 - Hora Extra 50%         600,00

0083 - Hora Extra 100%        200,00

0084 – Comissão                   400,00    
Total Grupo 1 = 800,00     
Total Grupo 2 = 400,00  
Total da competência = 1.200,00  
   
05/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        100,00

0084 – Comissão                   600,00     
Total Grupo 1 = 300,00     
Total Grupo 2 = 600,00  
Total da competência = 900,00  
   
No exemplo acima, com o parâmetro marcado, serão consideradas as competências, onde as somas totais dos valores são os maiores, ou seja, meses 01/2016, 02/2016 e 04/2016.  
**Grupo 1**

01/2016

0082 - Hora Extra 50%        200,00

0083 - Hora Extra 100%        500,00

02/2016

0082 - Hora Extra 50%          400,00

0083 - Hora Extra 100%        100,00

04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00  
   
Total Grupo 1 = 700,00 + 500,00 + 800,00 = 2.000,00 / 3 = **666,67**  
   
**Grupo 2**

01/2016

0084 – Comissão                   300,00

02/2016

0084 – Comissão                   800,00

04/2016

0084 – Comissão                   400,00  
   
Total Grupo 2 = 300,00 + 800,00 + 400,00 = 1.500,00 / 3 = **500,00**  
   
Com o parâmetro desmarcado, a apuração dos maiores valores irá verificar os totais por grupo, ou seja, meses 01/2016, 03/2016 e 04/2016 para o Grupo 1, e meses 02/2016, 04/2016 e 05/2016 para o Grupo 2.  
**Grupo 1**

01/2016

0082 - Hora Extra 50%          200,00

0083 - Hora Extra 100%        500,00

03/2016

0082 - Hora Extra 50%         100,00

0083 - Hora Extra 100%        500,00

04/2016

0082 - Hora Extra 50%          600,00

0083 - Hora Extra 100%        200,00  
   
Total Grupo 1 = 700,00 + 600,00 + 800,00 = 2.100,00 / 3 = **700,00**  
   
**Grupo 2**

02/2016

0084 – Comissão                   800,00

04/2016

0084 – Comissão                   400,00

05/2016

0084 – Comissão                   600,00  
   
 Total Grupo 2 = 800,00 + 400,00 + 600,00 = 1.800,00 / 3 = **600,00**  
   
   
   
**Tipo de Cálculo, Correção de Valores, Habitualidade e Parâmetros Relacionados a Afastamentos** Informações  
   
   
   
**Comissão**  
   
Despreza fórmula base salário  
As fórmulas adicionais cadastradas nos parâmetros de Folha Normal, Férias e Rescisão existente no módulo Parametrizador serão desconsideradas para os cálculos de médias.  
   
   
Desconsidera o mês em que houver período de férias também para a soma dos valores  
Para desconsiderar eventos que incide em médias, e foram pagos no mês do período de gozo das férias.   
   
**Atenção:**  
Este parâmetro depende do próximo parâmetro 'Desconsidera para contagem o mês em que houver período de férias igual ou maior'.  
   
**Exemplo:**  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Evento do tipo valor que incidem em média de férias lançados em:  
03/2013 = 100,00  
06/2013 = 100,00  
Média dos últimos 6 meses  
   
Com o parâmetro desmarcado:  
São considerados os dois valores e o valor encontrado é divido por 6 para retorna a média.  
   
Com o parâmetro marcado e o campo 'Desconsidera para contagem o mês em que houver período de férias igual ou maior' informado 8.  
Os meses 03/2013 e 04/2013 são desconsiderados no cálculo da média, tanto para o divisor do cálculo da média como para buscar valores de eventos que incidem na média.  
   
   
   
Desconsidera para contagem o mês em que houver período de férias igual ou maior  
Para desconsiderar o mês do período de gozo das férias no divisor do cálculo das médias.  
O dia informado neste parâmetro compara com a quantidade de dias de férias no mês.  
   
**Exemplo I:**  
Parâmetro = 8 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso serão desconsiderados os meses 03 e 04/2013 no divisor da média, devido no mês 03/2013 ter 22 dias de férias e no mês 04/2013 ter 8 dias de férias.  
   
**Exemplo II:**  
Parâmetro = 10 dias  
Período do gozo de férias: 10/03/2013 a 08/04/2013   
Competência atual: 09/2013  
Período do gozo de férias: 15/09/2013 a 04/10/2013  
Média dos últimos 6 meses  
Neste caso é desconsiderado apenas o mês 03 no divisor da média.  
   
**Atenção I:**  
Caso não deseje desconsiderar o mês deve informar 31 neste campo.  
   
**Atenção II:**  
Este parâmetro não depende do parâmetro anterior. Caso o parâmetro anterior 'Desconsidera o mês em que houver período de férias também para a soma dos valores' esteja desmarcado, o período do gozo de férias é desconsiderado apenas no divisor da média.  
   
   
   
   
**HomologNet**  
   
São cadastradas as formas de apuração das médias de Férias, 13º Salário e Aviso Prévio conforme manual do HomologNet fornecido pelo Ministério do Trabalho.  
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

Média de Férias na Rescisão   
Média de 13º na Rescisão  
Evento Pagamento Média Férias   
Evento Pagamento Média Rescisão  
Evento Pagamento Média Proporcinal Rescisão  
Evento Pagamento Média Média Abono  
Evento Pagamento Média 13º Segunda Parcela  
Evento Pagamento Média 13º Salário Rescisão  
Evento Pagamento Média Aviso Prévio  
Evento Pagamento Licença Maternidade  
Historico Mínimo Garantido  
Valores Associados dos Sindicatos  
Tipos de Cálculo de Média, Habitualidade, Correção de Valores e Parâmetros Relacionados a Afastamentos   
Remuneração Base
