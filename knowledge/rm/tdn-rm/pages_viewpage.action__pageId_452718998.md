---
content_hash: 9d6ed576c642b3d341d88103cc470f719af5da1bed7a0abb5fe2ce22a83835d6
fetched_at: '2026-06-29T00:10:03.083945+00:00'
page_id: '452718998'
product: rm
source: tdn-rm
title: Horário de Sobreaviso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718998
version: 7
---

**Horário de Sobreaviso**

O Sobreaviso deve ser lançado para aqueles funcionários para pagar as horas que o funcionário estará a disposição da empresa fora do seu horário de serviço.

Pode ser utilizado no caso de plantão, quando um funcionário vai para casa mas está de plantão, ou seja a disposição da empresa e poderá ser chamado para trabalhar a qualquer minuto.

**Exemplo:**

No dia 08/04/2002 um funcionário X tem o horário é 08:00E 12:00S 14:00E 18:00S. Lançamos um Horário de Sobreaviso no período de 18:00 às 24:00 horas. Se o funcionário sair da empresa as 18:00 horas, o sistema irá calcular para ele 06:00 horas de Sobreaviso referente ao intervalo de 18:00 às 24:00 horas. Se o funcionário tiver efetuado as batidas 08:00E 12:00S 14:00E 20:30S no dia 08/04/2002, a movimentação do funcionário neste dia será: 02:30 horas extras normais referentes ao intervalo de 18:00 às 20:30 06:00 horas de Sobreaviso referente ao intervalo cadastro de Sobreaviso (18:00 às 24:00) 02:30 horas extras de Sobreaviso, pois o funcionário trabalhou dentro do horário de sobre aviso.

**Observação:** Para funcionários com horário flexível, o cálculo do sobreaviso é um pouco diferente. As horas de sobreaviso serão calculadas com base na flexibilidade do horário, ou seja, se o funcionário realizou uma jornada diferente do planejado, o sobreaviso será gerado considerando a jornada **executada**, e não a jornada planejada. Veja abaixo.

Horário planejado do funcionário: 08:00 12:00 13:00 17:00  
Intervalo de sobreaviso: 00:00 23:59

Exemplos:

O cálculo será gerado de acordo com o número de horas planejado, considerando o início da jornada, portanto se o funcionário iniciar às 09:00, o fim será às 18:00, e assim por diante.

01/01 09:00 12:00 13:00 18:00 = 00:00 às 09:00 - SAV 18:00 às 23:59 - SAV;

02/01 09:00 12:00 13:00 19:00 = 00:00 às 09:00 - SAV 18:00 às 19:00 - SAN 18:00 às 23:59 - SAV;

03/01 09:00 12:00 13:00 17:30 = 00:00 às 08:00 - SAV 17:00 às 23:59 - SAV (não ocorreu a compensação das extras geradas após a jornada com os atrasos, será mantida a jornada planejada para o cálculo de sobreaviso);

04/01 09:00 12:00 13:00 17:30 = 00:00 às 08:30 - SAV 17:30 às 23:59 - SAV (neste cenário ocorreu a compensação dos 30 minutos de atrasos com as extras no fim da jornada, gerando assim a adequação do fim do primeiro intervalo de sobreaviso e o início do segundo intervalo de sobreaviso);

05/01 09:00 12:00 12:30 17:30 = 00:00 às 08:00 - SAV 17:00 às 23:59 - SAV (não ocorreu a compensação da extra gerada após a jornada com o atraso, será mantida a jornada planejada para o cálculo de sobreaviso);

06/01 11:00 12:00 13:00 19:00 = 00:00 às 10:00 - SAV 19:00 às 23:59 - SAV (neste cenário ocorreu a compensação das 02:00 horas de atrasos com as 02:00 horas de extras no fim da jornada, gerando assim a adequação do fim do primeiro intervalo de sobreaviso e o início do segundo intervalo de sobreaviso);

**Grupo de Funcionários -** No grupo de funcionários você faz a seleção para aqueles que receberão horário de sobreaviso. A seleção de funcionários pode ser feita por:

**Quebra de seção -** Este campo deve ser utilizado para selecionar o grupo de funcionários pela seção que está cadastrado. Podendo informar o código da seção, ou até mesmo o código de quebra da seção.

**Seleção de funcionários -** Ao clicar no botão de Seleção de funcionários o sistema abrirá uma janela com os campos onde você poderá selecionar um funcionário digitando sua chapa ou localizando seu nome, ou também fazer a seleção de funcionários pela situação, tipo de funcionário e recebimento.

**Horário -** Informe nos campos início e fim o intervalo de datas que pretende fazer o lançamento do horário de Sobreaviso do(s) funcionário(s).

**Observação**

 O período informado tem que estar no período atual do sistema. A data início não pode ser maior que a data fim.

**Cancelar dados lançados no período -** Marque esta opção para cancelar o sobreaviso lançado para o(s) funcionário(s). O sistema só irá cancelar se informar o intervalo de hora igual ao que foi lançado.

**Perfil de Parâmetros -** Este campo permite guardar a configuração dos parâmetros habilitados do lançamento. Ao acessar novamente este lançamento, basta selecionar o perfil criado para o sistema trazer os parâmetros salvos.

**Salvar perfil ao concluir -** Este parâmetro é utilizado para incluir um novo perfil de parâmetros. Informe um nome de um novo perfil, marque o parâmetro "salvar perfil ao concluir" e ao clicar no botão "OK" para efetuar o lançamento o sistema gravará o novo perfil de parâmetros.
