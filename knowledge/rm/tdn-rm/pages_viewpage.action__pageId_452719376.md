---
content_hash: c31363d0b8bb96416c356eaee4c15a663edf98b7c0e291be7db5e5eb266dab8c
fetched_at: '2026-06-29T00:10:07.215785+00:00'
page_id: '452719376'
product: rm
source: tdn-rm
title: Afastamento 1/2
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719376
version: 27
---

Nesta etapa são configuradas as opções de cálculo para afastamentos

**Parâmetros e Campos**  
Dias de carência para afastamento com atestado médico  
Este campo representa o número de dias que a empresa considerará para contagem dos dias de afastamento do funcionário, caso esteja afastado pela mesmo motivo do afastamento anterior em conformidade com o Decreto 3.048/99, Artigo 75, Parágrafo 3º do Regulamento da Previdência Social:  
*"Se concedido novo benefício decorrente da mesma doença dentro de sessenta dias contados da cessação do benefício anterior, a empresa fica desobrigada do pagamento relativo aos quinze primeiros dias de afastamento prorrogando-se o benefício anterior e descontando-se os dias trabalhados, se for o caso."*

Usa mês comercial para afastamentos no final do mês de 31 dias  
Marque este parâmetro caso deseje que o sistema considere os dias trabalhados observando o mês comercial para funcionários afastados no final do mês.

Atenção:

Este parâmetro somente será considerado quando o funcionário for mensalista, caso o funcionário seja horista o sistema sempre pagará o dia 31 do mês.

Exemplo parâmetro Usa mês comercial para afastamentos no final do mês de 31 dias

Dados Fictícios

Afastamento por licença maternidade dia 20/03

PARÂMETRO MARCADO - PAGA 18 DIAS TRABALHADOS

PARÂMETRO DESMARCADO - PAGA 19 DIAS TRABALHADOS

Considera divisor pelo número de dias do mês na remuneração de funcionário com afastamento

Marque este parâmetro para, quando o funcionário estiver afastado, o sistema considerar a quantidade real de dias do mês como divisor.  
  
**Exemplo: Funcionário afastado de 13/01 à 08/02**  
  
Campo marcado:  
     Em Fevereiro, o sistema calculará 22 dias trabalhados e 08 dias de afastamento, utilizando como divisor 28 dias.  
          Salario: R$ 5000  
          Calculo: Salário / Dias do Mês \* Dias Trabalhados = 5000 / 28 \* 22  
  
Campo desmarcado:  
     Em Fevereiro, o sistema calculará 22 dias trabalhados e 08 dias de afastamento, considerando como divisor 30 dias.   
          Salario: R$ 5000  
          Calculo: Salário / Dias do Mês \* Dias Trabalhados = 5000 / 30 \* 22

Mais informações:

Lança o evento de atestado médico via grupo de eventos  
Marcando este parâmetro, o usuário poderá efetuar o lançamento do evento Atestado Médico (Código de Cálculo 145) no período que desejar na movimentação do funcionário. Após marcar o parâmetro, será obrigatório o cadastramento de um Grupo de Eventos com o evento com o código de cálculo 145, para que o mesmo seja lançado na movimentação do funcionário.  
Não marcando este parâmetro, o lançamento do atestado do funcionário será feito no evento de código de cálculo 2 ou 1 se eles forem informados no grupo de eventos.

**Observação 1:**  
Pode informar um evento para discriminação nos campos 'Evento para atestado médico (mensalista)' e 'Evento para atestado médico (horista)' para lançar de forma global, caso este parâmetro esteja desmarcado e o usuário deseje discriminar o pagamento referente a atestado médico.  
Caso marque o parâmetro e não informe nenhum evento via grupo de parâmetros, o sistema entende que o usuário queira separar a parte do atestado dos dias/horas trabalhadas e lançará somente a parte trabalhada nos eventos de CC1 ou CC2.

**Exemplo**  
Funcionário com 10 dias de atestado no mês 01-04 com salário de R$ 3000,00  
Marcando o parâmetro para lançar o evento de atestado pelo grupo de eventos e não informado no grupo de eventos nenhum evento com o código de cálculo 145.  
Informado o evento com o código de cálculo 2.  
O sistema irá lançar o valor de R$ 2000,00 com referência = 20, no evento com o CC2  
O sistema não lançará o valor de R$ 1000,00, com referencia = 10 e nenhum evento.

**Observação 2:**

Através da publicação da Nota Técnica [Parecer SEI nº 16120/2020/ME](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes/#7-23----29-12-2020----parecer-sei-n--16120-2020-me--como-deve-ser-tratada-a-incid-ncia-tribut-ria-nos-15-primeiros-dias-de-afastamento-que-antecedem-o-benef-cio-de-aux-lio-doen-a-) em 28/12, ficaram estabelecidos os critérios para cálculo do atestado médico que antecede ao Afastamento Previdenciário. Para maiores informações sobre os procedimentos acesse [Folha de Pagamento - Atestado médico com incidência somente segurado (CC445)](https://tdn.totvs.com/pages/viewpage.action?pageId=590618716).

Proporcionalizar eventos considerando os dias de atestado médico   
Para o sistema proporcionalizar os dias de afastamento sem considerar os 15 primeiros dias da Empresa foi criado o parâmetro: "Proporcionalizar eventos considerando os dias de atestado médico". Em que:

* Caso esteja marcado no **cadastro de evento** a proporcionalidade no afastamento e este parâmetro, o sistema irá proporcionalizar também os dias de atestado.
* Caso esteja marcado **Apenas o parâmetro do cadastro de evento (Ou seja, o parâmetro no parametrizador estiver desmarcado)**, o sistema irá proporcionalizar, mas não irá considerar os 15 primeiros dias de atestado médico.

Com o parâmetro marcado o sistema proporcionaliza o valor do evento **(''Qualquer'' evento que esteja com a proporcionalização marcada)** sem considerar os 15 primeiros dias de atestado médico. Desmarcado passou a considerar os 15 primeiros dias de atestado médico.

Atestado médico considera somente afastamentos da última sequência do período de carência

O sistema realiza a validação de novos afastamentos pelo mesmo tipo e motivo com base no histórico do funcionário e no período de carência (ex: 60 dias), seguindo dois comportamentos principais de acordo com a parametrização:

* **Parâmetro Marcado:** O sistema analisa apenas os afastamentos que foram finalizados dentro do período de carência de 60 dias anteriores ao novo atestado.
* **Parâmetro Desmarcado:** A verificação retrocede por todos os afastamentos anteriores pelo mesmo motivo, a partir do início do último, até que se encontre um intervalo sem afastamentos superior a 60 dias.

Em ambos os casos, se for identificado um afastamento anterior pelo mesmo motivo dentro da regra, a empresa pagará apenas a quantidade de dias necessária para completar o total de 15 dias de responsabilidade do empregador, antes do encaminhamento à Previdência Social.

Exemplo parâmetro marcado

Um novo afastamento iniciando em 04/06/2024 (80 dias de afastamento).

Retroage 60 dias, voltando a 05/04/2024. Contudo a retroação tem interseção com um outro período de afastamento, que iniciou em 19/12/2023 e finalizou em 25/04/2024.

Só que, antes deste afastamento, havia ainda um outro afastamento, de 15 dias, do dia 04/12/2023 ao dia 18/12/2023.

Por terminar um afastamento no dia 18/12/2023 e começar outro em 19/12/2023, o sistema entende que não houve retorno ao trabalho e então considera o afastamento de 15 dias como parte de um afastamento maior, sendo pago 10 dias de afastamento pela empresa, ficando com um saldo de 5 dias para possíveis afastamentos posteriores.

Conforme regra da previdência implementada neste parâmetro, o funcionário só pode ter mais um afastamento pela previdência caso tenha um retorno dentro do período de carência e neste caso foi considerado o afastamento do dia 09/05/2024 (1 dia) como pela previdência.

Então, após um período trabalhado e já tendo utilizado um afastamento pela previdência dentro do período de carência conforme regra da previdência citada, ao iniciar um novo período de afastamento (04/06/2024 - 80 dias de afastamento), também começará a considerar os dias de atestado pela empresa novamente, descontando os 10 dias já pagos dentro de todo o período considerado e explicado acima e então são lançados mais 5 dias de atestado antes de retornar à cobertura pela previdência.

Portanto, se o funcionário não tivesse o afastamento do dia 09/05/2024, o novo período de afastamento em 04/06/2024 seria o retorno dentro da carência e não haveria a cobrança dos 5 dias. Como houve o afastamento no dia 09/05/2024, a cobrança dos 5 dias, neste caso, é correta.

Exemplo parâmetro desmarcado

Um funcionário tem o seguinte histórico de afastamento:  
01/11 à 10/11 Afastamento previdência  -> Motivo: 001  -> 10 dias

10/09 à 14/09 Afastamento previdência  -> Motivo: 001  -> 5 dias  
05/08 à 09/08 Afastamento previdência  -> Motivo: 001  -> 5 dias  
01/05 à 03/05 Afastamento previdência -> Motivo: 001  -> 3 dias  
   
Afastamento em 01/11 – O sistema retrocede 60 dias de carência = 02/09 a 01/11  
Afastamento em 10/09 dentro da carência – O sistema retrocede 60 dias de carência novamente = 12/07 a 10/09  
Afastamento em 05/08 dentro da carência – O sistema retrocede 60 dias de carência novamente = 05/06 a 05/08  
Afastamento em 01/05 – **Fora da carência**  
   
01/11 à 10/11 Afastamento previdência  -> Motivo: 001  -> 10 dias    (5 dias de atestado médico pagos pela empresa e 5 dias pela previdência)    
05/08 à 09/08 Afastamento previdência  -> Motivo: 001  -> 5 dias      (5 dias de atestado médico pagos pela empresa)  
10/09 à 14/09 Afastamento previdência  -> Motivo: 001  -> 5 dias      (5 dias de atestado médico pagos pela empresa)  
01/05 à 03/05 Afastamento previdência  -> Motivo: 001  -> 3 dias     – **Fora da carência**

**Conforme datas acima o 15 dias foram pagos separadamente conforme foi retrocedendo as datas para carência.**

Habilita controle manual de continuidade de afastamentos com atestado médico  
Este parâmetro foi criado para controle manual da continuidade de afastamento.   
A utilização deste novo parâmetro irá criar a possibilidade de vincular afastamentos de diferentes tipos, dentre P (Previdência), T (Acidente de Trabalho) e O (Doença Ocupacional), com afastamento anterior, permitindo assim da continuidade quando motivos diferentes, ou com mesmo motivos, mas a doença se relaciona com o anterior.   
Este vínculo será preenchido manualmente pelo usuário fazendo a ligação dos registros através de um lookup no cadastro de histórico de afastamentos, que irá guardar a data de início do afastamento inicial da sequência de continuidade.  
*Ao marcar o parâmetro no parametrizador, será exibida a mensagem de alerta abaixo:*  
*ATENÇÃO! Marcando este parâmetro, o cálculo de Atestado Médico e Dias Trabalhados de todos os funcionários passará a verificar as relações de continuidade informada pelo usuário no histórico de afastamento, anexo ao Cadastro do Funcionário. Os dias para pagamento de Atestado Médico serão contabilizados acatando o intervalo entre os afastamentos, informando no campo "Dias de carência para afastamento com atestado médico" do Parametrizador.*   
Para o melhor funcionamento, o parâmetro só deve ser marcado quando o Histórico de Afastamentos de todos os funcionários estiver atualizado com as novas informações necessárias para o controle da continuidade.

**Atenção**  
Caso o parâmetro esteja marcado e o histórico não esteja atualizado, mesmo que exista afastamentos com mesmo tipo e motivo e dentro do período de carência, o sistema não irá fazer o cálculo de dias de atestado considerando a continuidade de afastamento automático. Para que o sistema continue fazendo automático, este parâmetro não deve ser marcado.

Data final do período em que o auxilio doença teve duração de 30 dias (MP 664)  
Este parâmetro foi criado para definir uma data onde a empresa irá informar qual a data de final de validade da MP 664.   
O sistema considera internamente que a MP 664 começou a valer a parti do dia 1 de março de 2015 e a sua validade depende do entendimento jurídico de cada empresa.   
Se o usuário informar para este campo a data 28/02/2015, o sistema irá considerar que para todo o afastamento sempre seja contado 15 dias de atestado pagos pela empresa. Caso é informado uma data superior ao dia 01/03/2015 e dentro deste período houve afastamento do funcionário superior a 30 dias, a empresa é responsável pelo pagamento dos 30 primeiros dias, mesmo que a data final do afastamento seja superior a data final do período de duração da MP 664.  
   
Este campo foi criado após o vencimento da MP 664. O sistema já tinha sido implementado para considerar 30 dias de afastamento pagos pela empresa. Logo, quando for preencher esse campo, deve ficar atento aos cálculos efetuados, períodos aquisitivos de férias, etc, pois a data final pode interferir no valor final da verba a ser paga.

**Exemplo 1**  
Funcionário afastou no período de 01/03/2015 a 30/04/2015  
Empresa pagou 30 dias de atestado e o restante foi pago pela previdência.  
Em 01 de Junho de 2015 a empresa preencheu a data final do período da MP = 28/02/2015  
Em 01 de agosto de 2015 foi feito um cálculo de diferença salarial retroativo a 01/02/2015  
O sistema irá considerar que a empresa teve a obrigação de pagar 15 dias de atestado, logo irá calcular a diferença somente de 15 dias e não os 30 que foram efetivamente pagos.   
Neste exemplo a empresa deve ficar atenta, pois pode gerar verbas negativas para o funcionário.

**Exemplo 2**  
Funcionário afastou no período de 01/06/2015 a 30/07/2015  
Empresa pagou 30 dias de atestado e o restante foi pago pela previdência  
Em 02 de junho de 2015 a empresa preencheu a data final no período da MP = 17/06/2015  
Em 01 de Agosto de 2015 foi feito um cálculo da diferença salarial retroativo a 01/04/2015  
O sistema irá calcular a diferença do atestado, considerando os 30 dias que foram pagos, mesmo a empresa informando ao final do período antes do termino, pois a data final da MP 664 é superior ao início do atestado médico.

**Exemplo 3**  
Funcionário afastou no período de 15/02/2015 até 31/03/215  
Empresa pagou 15 dias de atestado e o restante foi pago pela previdência  
Em 01/06/2015 a empresa preencheu a data final no período da MP = 01/06/2015  
Em 01 de Julho de 2015 foi feito um cálculo de diferença salarial retroativo a 01/02/2015  
O sistema irá considerar 15 dias de afastamento para o cálculo das diferenças, mesmo que o termino do afastamento tenha interseção com o período de vigência da MP 664.  
   
**Observação**  
O período de carência irá considerar 30 dias a soma de todos os atestado pelo mesmo tipo e motivo, caso a data da validade seja superior ao dia 01/03/2015 e o início do afastamento maior que 28/02/2015 e menor que data final da MP.

Manter a situação dos funcionários com retorno de afastamento na próxima competência  
Na Liberação de Competência, o funcionário com afastamento terá a situação alterada para 'Ativo' quando:

* 'Marcado': Afastamento com data de retorno na Competência atual.
* 'Desmarcado': Afastamento com data de retorno na Competência atual e na próxima.

Gerar histórico de situação do funcionário somente para afastamentos tipo T ou P sem retorno no mês

Na Liberação de Competência da Competência será criado um histórico de situação somente para os funcionários afastados com os tipos 'P - Af. Previdência' e 'T - Af. Ac. Trabalho' que não tenham data de retorno de afastamento no mês.
