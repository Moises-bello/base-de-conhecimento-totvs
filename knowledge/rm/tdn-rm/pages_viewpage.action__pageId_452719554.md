---
content_hash: b6a1c8bdd4544252a1c96acbfcc7671814feb0fdc8bdc35725cf690dd3bdb920
fetched_at: '2026-06-29T00:10:08.664830+00:00'
page_id: '452719554'
product: rm
source: tdn-rm
title: Salário Maternidade 1/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719554
version: 5
---

Parâmetros que definem como será feito o cálculo do Salário Maternidade e Salário Maternidade Complementar  
   
**Parâmetros e Campos**  
   
**Salário Maternidade Complementar (Tipo W) Considera Formulas Adicionais**: Este parâmetro, quando marcado, irá considerar o valor calculado na(s) fórmula(s) adicional(is) informada(s) no menu Fórmulas Adicionais para Licença Maternidade, somando o mesmo no salário base para o cálculo de Licença Maternidade Complementar, lançando no evento com código de cálculo 352. Quando o mesmo não está marcado, não será considerado as fórmulas adicionais informadas.  
   
**Salário Maternidade Complementar (Tipo W) Considera Dias Corridos no Mês**: Este parâmetro, quando marcado, irá considerar para o cálculo de dias de licença maternidade complementar os dias corridos no mês. Quando desmarcado, irá considerar o mês comercial (30 dias) para o cálculo do Salário de Licença Maternidade Complementar. O valor é lançado no evento de Código de Cálculo 352, com a referencia de dias de afastamento.  
Exemplo  
Funcionário com Licença Maternidade Complementar: 01/02/2017 a 15/02/2017  
Dias corridos em Fevereiro: 28  
Parâmetro Marcado: (Salário Base /28) \* 15  
Parâmetro Desmarcado: (Salário Base/30) \*15  
   
**Salário Maternidade por adoção pago pela previdência**  
Se o parâmetro estiver marcado, o sistema irá lançar os eventos informados nos campos 'Evento Salário Maternidade pago pela previdência' e 'Evento média Salário Maternidade pago pela previdência' como base de cálculo, para os funcionários que estão afastados por Tipo de Licença Maternidade(E), e por Motivo igual ao 'Motivo de afastamento ref. a licença maternidade por adoção', informado na pasta 'Afastamento' do Parametrizador. Uma vez marcado este parâmetro, o usuário deverá obrigatoriamente informar o evento de salário maternidade pago pela previdência, localizado abaixo. Se o parâmetro não estiver marcado, o sistema lançará o Salário Maternidade para todos os funcionários afastados pelo Tipo E.

O parâmetro também habilitará a seleção dos eventos ‘13º Salário Licença Maternidade pago pela Previdência’ e ‘13º Rescisão Licença Maternidade pago pela Previdência’ para os funcionários que tiveram afastamento por Tipo de Licença Maternidade (E), e por Motivo igual ao 'Motivo de afastamento ref. a licença maternidade por adoção', informado na pasta 'Afastamento' do Parametrizador.

**Atenção**

Para o sistema lançar automaticamente os valores de Salário Maternidade Pago pela Previdência e a Média Salário Maternidade Pago pela Previdência, o usuário deverá criar dois eventos sem código de cálculo, tipo Base de Cálculo/Valor, dois eventos com o Código de Cálculo 17 e informa-los em Administração de Pessoal | Sindicatos, na aba Licença maternidade | Eventos p/ Pagamento Média Lic. Maternidade. Se o usuário não trabalhar com médias, deverá criar apenas um evento de Salário Maternidade com Código de Cálculo 17 e informa-lo no Sindicato.

Calcula salário maternidade conforme SEFIP  
Com este parâmetro marcado, o sistema irá calcular a remuneração proporcional considerando o mês calendário (28, 29, 30 ou 31 dias), conforme o cálculo do SEFIP. O valor do salário maternidade será a base de licença maternidade dividido pelo número de dia do mês (de acordo com o parâmetro), multiplicado pelo número de dias de licença no mês.

Aviso:

Parâmetro 'Calcula salário maternidade conforme SEFIP' só deve ser considerado quando a licença maternidade é no mês inteiro.

Dica:

Para afastamento de licença maternidade durante o mês que tem 31 dias e o usuário quiser pagar 31 dias veja o parâmetro "[Usa mês comercial para afastamentos no final do mês de 31 dias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719376)" em Parametrizador | Folha Normal | Afastamento.

Exemplo parâmetro Calcula salário maternidade conforme SEFIP

Dados Fictícios

Afastamento por licença maternidade dia 01/03

PARÂMETRO MARCADO - DIVIDE POR 31

PARÂMETRO DESMARCADO - DIVIDE POR 30

**Evento salário maternidade pago pela previdência**  
Informe o evento de Licença Maternidade pago pela previdência que deverá ser lançado na movimentação no momento do Lançamento automático de Licença Maternidade para os funcionários com afastamento por Licença de Maternidade. O evento deverá ser cadastrado em Administração de Pessoal | Cadastros | Eventos, sem código de cálculo, do tipo Valor e Base de Cálculo, com incidência somente em FGTS e Salário Família.  
   
**Evento média salário maternidade pago pela previdência**  
Se a empresa discriminar média de Licença Maternidade, informe o evento de Média de Licença Maternidade pago pela previdência. Este evento será lançado na movimentação no momento do Lançamento automático de Licença Maternidade para os funcionários com afastamento por Licença de Maternidade. O evento deverá ser cadastrado em Administração de Pessoal | Cadastros | Eventos, sem código de cálculo, do tipo Valor e Base de Cálculo, com incidência somente em FGTS e Salário Família.

**Atenção**  
Se o evento de média de Salário Maternidade não for informado, o sistema procederá da seguinte forma:  
1. Se no sindicato houver evento de discriminação de média, o sistema interpretará que o usuário deseja que o valor da média seja desconsiderado.  
2. Se no sindicato não houver evento de discriminação de média, o sistema assimilará que o usuário deseja que o valor das médias seja considerado e deve ser somada ao salário maternidade correspondente ao campo 'evento salário maternidade pago pela previdência'

**Observação**  
Quando os dias de Licença Maternidade não forem pagos pela empresa, estes eventos deverão constar no envelope do funcionário como base de FGTS, para ser informado no arquivo SEFIP. O programa SEFIP calcula o FGTS sobre a base informada no arquivo. Embora estes eventos não tem incidência no INSS, o sistema irá no momento do cálculo da SEFIP, da GRPS e da GPS considerar os valores destes para o calculo do valor do INSS empresa, acidente de trabalho e terceiros. O INSS retido na empresa do campo SEGURADOS, o sistema gera automaticamente no arquivo SEFIP buscando o evento de desconto de INSS presentes na movimentação.

**Evento 13º Salário Licença Maternidade pago pela Previdência**

Informe o evento de 13º Salário Licença Maternidade pago pela Previdência que deverá ser lançado na movimentação no momento do Lançamento 13º salário para os funcionários com afastamento por Licença de Maternidade com o motivo de Adoção. O evento deverá ser cadastrado em Administração de Pessoal | Cadastros | Eventos, sem código de cálculo.

**Evento 13º Rescisão Licença Maternidade pago pela Previdência**

Informe o evento de 13º Rescisão Licença Maternidade pago pela Previdência que deverá ser lançado na movimentação no momento do Lançamento 13º salário para os funcionários com afastamento por Licença de Maternidade com o motivo de Adoção. O evento deverá ser cadastrado em Administração de Pessoal | Cadastros | Eventos, sem código de cálculo.

**Observação:** Os eventos “13º Salário Licença Maternidade pago pela Previdência” e “13º Rescisão Licença Maternidade pago pela Previdência” serão calculados pelo usuário podendo ser por fórmula.

 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Fórmulas Adicionais Para Licença Maternidade
