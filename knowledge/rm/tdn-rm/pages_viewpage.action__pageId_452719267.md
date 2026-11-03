---
content_hash: b15c162c5a430e3646c3dfb4e2829318aa85e8af364a17dbe9041aa08f6f0696
fetched_at: '2026-06-29T00:10:04.940241+00:00'
page_id: '452719267'
product: rm
source: tdn-rm
title: Convocação para Trabalho Intermitente - RHU
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719267
version: 6
---

A reforma trabalhista regulamentou a criação do contrato de trabalho intermitente, segue trecho do Art. 443 da reforma trabalhista:  
"Considera-se como intermitente o contrato de trabalho no qual a prestação de serviços, com subordinação, não é contínua, ocorrendo com alternância de períodos de prestação de serviços e de inatividade, determinados em horas, dias ou meses, independentemente do tipo de atividade do **empregado** e do empregador, exceto para os aeronautas, regidos por legislação própria" (BRASIL, Lei nº 13.467, Art. 443, § 3º, de 13 de julho de 2017).  
Embora as regras estabelecidas pela MP 808 tenham perdido a validade a portaria n° 349, de 23 de maio de 2018, reestabelece as regras para contratação para trabalho intermitente.  
   
**Registro**  
Não há, de forma clara, restrições de atividade que um intermitente possa assumir. Desse modo, neste passo-a-passo é orientado que o funcionário contratado em regime de trabalho intermitente seja classificado com o tipo "Normal". Além disso, é necessário para o eSocial que seja utilizado o código de categoria "111 – Empregado – contrato de trabalho intermitente" para preenchimento do campo "Código da Categoria eSocial".  
   
**Salário/Jornada**  
O Trabalhador Intermitente será configurado no sistema marcando o campo "Regime de Trabalho Intermitente" na aba de "Salário / Jornada".  
Para obter o salário hora contratual do trabalhador intermitente, informe o salário e a jornada conforme se cadastraria para um funcionário de regime indeterminado e mensalista. Desse modo, o sistema calculará o valor hora.  
Devido ao regime intermitente não ter um horário previamente definido (a jornada é específica para cada convocação), deverá ser informado um horário padrão sem necessidade de batidas para o intermitente.  
O campo "Tipo de Regime da Jornada" é obrigatório para o eSocial e, portanto, deve ser preenchido. Entretanto, o eSocial não definiu um valor para este campo específico para o Trabalho Intermitente. Desse modo, o preenchimento do campo deverá ser coerente com a jornada do funcionário. Caso haja dúvidas no preenchimento deste campo, consulte seu setor jurídico e/ou sindicato.  
   
**FGTS/SEFIP**  
De acordo com a orientação da caixa econômica na Circular CAIXA nº 758, de 27 de março de 2017 e com o que consta no FGTS Manual de Orientações Recolhimentos Mensais e Rescisórios ao FGTS e das Contribuições Sociais de 09/11/2017, que informa que a categoria do Intermitente deve ser 04 Empregado sob contrato de trabalho por prazo determinado / Intermitente - Lei n°. 9.601/98, com as alterações da Medida Provisória n° 2.164-41, de 24/08/2001 e, Lei nº. 13.467, de 13 de julho de 2017.  
   
**RAIS**   
Não há instrução de qual será a situação ou o vínculo para RAIS, não sendo possível inferir um valor. Como o campo é obrigatório e impede o cadastro do funcionário, deve-se assumir um valor equiparado ao de um empregado não intermitente de mesma função. Na ocasião da publicação de uma norma para RAIS, os devidos ajustes deverão ser efetuados.  
O Layout da RAIS 2017/2018 solicita o preenchimento do campo de 543 a 543, no registro tipo 2, com os valores 1 – SIM ou 2 – NÃO, dependendo se o funcionário no ano base trabalhou em regime intermitente ou não. Para preencher este campo, o sistema verifica o campo "Regime de trabalho intermitente" em "Salário/Jornada" do cadastro do funcionário.  
   
**Configurações iniciais da convocação**  
Acessando "Configurações | Parametrizador | 06.01.02 – Funcionário | Trabalho Intermitente", é possível ajustar a máscara que será utilizada para gerar automaticamente o código de cada convocação:  
Atenção: **A criação de uma máscara para o código da convocação é obrigatória para utilizar o anexo de funcionários "Convocação para Trabalho Intermitente"!**  
Trata-se de uma máscara no mesmo formato da lotação tributária e matrícula do trabalhador adotadas pelo eSocial. É uma máscara composta de:  
·          **Prefixo:** opcional. É um texto livre que não pode começar com "esocial" e nenhuma variação dessa palavra com letras maiúsculas e minúsculas ("eSocial", "ESOCIAL", etc). O mesmo prefixo será utilizado para gerar o código de todas as convocações;  
·          **Coligada:** obrigatório. Com tamanho mínimo de 3 caracteres ou tamanho do maior código de coligada + 1, o que for maior. Será um "C" seguido do código da coligada corrente do funcionário;  
·          **Sequencial:** obrigatório. Com tamanho mínimo de 7 caracteres. Será um "S" seguido de um número auto incremento único por coligada  
   
**Atenção:** **O tamanho total da máscara gerada não pode ultrapassar 30 caracteres.**  
Ao marcar o checkbox "Utilizar prefixo", o campo para selecionar a quantidade de caracteres do prefixo será habilitado e configurado para 1. O campo para inserir o texto do prefixo também será habilitado.  
   
**Atenção:** **Após configurar a máscara, o código de cada convocação será gerado automaticamente ao salvar o registro.**  
   
**Cadastro da convocação**  
Foi criado o Cadastro de Convocação, anexo ao cadastro do funcionário (a partir da visão de funcionários, acessar "Anexos | Movimento | Convocação para Trabalho Intermitente"). Nesse cadastro, é importante destacar as seguintes observações:

* Os campos 'Código da Convocação', 'Data da Convocação', 'Local de Prestação do Serviço', 'Data Início Prest. Serviço' e 'Data Fim Prest. Serviço' são obrigatórios;
* Apesar de obrigatório, o campo 'Código da Convocação' não pode ser preenchido. O código será gerado automaticamente ao salvar o registro, de acordo com a máscara definida no parametrizador;
* O campo 'Data Prevista de Pagamento' somente é obrigatório quando a 'Situação da Convocação' for diferente de 'Aguardando Resposta' ou 'Rejeitada pelo Funcionário'. **É importante o preenchimento deste campo, pois esse dado é enviado para o eSocial;**
* O campo 'Data da Resposta' somente é obrigatório quando a 'Situação da Convocação' for diferente de 'Aguardando Resposta';
* Ao selecionar 'Em local fixo com endereço diferente do estabelecimento' no grupo 'Local de Prestação do Serviço', será habilitada a aba 'Endereço', para cadastrar o endereço onde o funcionário prestará o serviço;
* No campo 'Situação da Convocação', ao selecionar 'Interrompida pelo funcionário' ou 'Interrompida pelo empregador', será habilitado o campo 'Data de Interrupção', que se tornará obrigatório.

**Aba "Pagamentos" do cadastro de convocação**  
A aba de "Pagamentos" é utilizada para que seja vinculado ao registro de convocação um ou mais envelopes de pagamento em que a convocação esteja sendo paga.   
**Atenção:** **É através dos dados inseridos nessa aba que os pagamentos efetuados ao funcionário intermitente serão identificados e poderão ser enviados ao eSocial.**  
Obs.: Caso essa aba não esteja visível, verifique se todos os procedimentos indicados na seção 8 deste documento foram realizados com sucesso.  
É importante destacar que essa aba não permite a inclusão/edição/exclusão de envelopes de pagamento. Ela permite apenas buscar envelopes existentes e vinculá-los à convocação que é identificada na aba "Identificação". Desse modo, ao incluir/editar/excluir um registro na aba "Pagamentos", o que será afetado é o vínculo do envelope de pagamento com a convocação, enquanto o envelope permanecerá inalterado.  
Quanto aos campos dessa aba, é importante destacar que:

* No *lookup* "Envelope de Pagamento", é possível recuperar envelopes da competência anterior à competência de início de prestação de serviços em diante, independente do filtro aplicado na visão do *lookup* (aberta ao clicar em "..."). Na caixa de texto que fica à esquerda, será apresentado o período do envelope, enquanto na da direita será apresentada uma descrição do envelope que informa mês/ano competência e período. Essa descrição independe da descrição cadastrada para o envelope aberto.
* Os campos "Ano Competência", "Mês Competência" e "Período" são somente-leitura, mostrando os dados do envelope selecionado através do *lookup* "Envelope de Pagamento".
* No campo "Qtde de Dias", deverá ser informada a quantidade de dias de convocação que o envelope recuperado através do *lookup* "Envelope de Pagamento" está pagando. Segundo layout 2.4.02 do eSocial, "... Deve ser um número entre 0 e 31.". Entretanto, se a quantidade total de dias de prestação de serviço referentes a essa convocação for menor que 31, esse será o número máximo de dias que um envelope poderá pagar. É igualmente importante destacar que a soma dos valores informados no campo "Qtde de Dias" para todos os envelopes vinculados a uma convocação não pode exceder a quantidade de dias de serviço prestado nessa convocação.

**Atenção:** **Para a correta geração das informações referente a trabalho intermitente  nos eventos S-1200 e S-2299 do eSocial, se faz necessário a vinculação de um envelope de pagamento na competência para as convocações.**  
**Exemplo:** Se for cadastrada uma convocação de trabalho com início em 01/06/2011 e término em 03/06/2011, a quantidade de dias de serviço prestado será 3. Desse modo, o valor máximo para o campo "Qtde de Dias" de uma única vinculação de pagamento será 3. Se forem cadastradas, por exemplo, duas vinculações com valores 2 e 1 para o campo "Qtde de dias", as próximas vinculações inseridas poderão pagar no máximo 0 dias.  
   
**Validações da convocação**  
As seguintes validações ocorrem ao incluir/editar uma nova convocação:

1. Para abrir o anexo de convocação a fim de incluir/editar um registro para determinado funcionário, o mesmo deverá ter o parâmetro 'Regime de Trabalho Intermitente' marcado na aba 'Salário/Jornada';
2. Para inserir/editar uma convocação, o funcionário não pode estar demitido (o mesmo não se aplica aos pagamentos vinculados, que podem ser inseridos/editados/excluídos livremente);
3. A data de fim da prestação de serviços para uma convocação deverá ser maior ou igual à data de início da prestação de serviços;
4. A data de início da prestação de serviços deverá ser maior ou igual à data de convocação;
5. A data de início da prestação de serviços deverá ser maior ou igual à data de resposta, quando essa existir;
6. O período de prestação de serviços de uma convocação não poderá ter interseção com outros períodos de convocação;
7. O período de prestação de serviços de uma convocação não poderá ter interseção com nenhum período de gozo de férias;
8. O período de prestação de serviços de uma convocação não poderá ter interseção com afastamentos;
9. Caso seja preenchida, a data de resposta deverá ser maior ou igual à data de convocação;
10. Caso seja selecionado um horário, será obrigatório selecionar também um índice de início (letra);
11. Caso seja selecionado o local de prestação de serviço 'Em local fixo com endereço diferente do estabelecimento', o preenchimento de todos os campos da aba 'Endereço' será obrigatório, exceto 'Complemento';
12. Caso a convocação esteja com situação interrompida, tanto pelo funcionário quanto pelo empregador, a data de interrupção será de preenchimento obrigatório;
13. Quando existir, a data de interrupção deverá ser maior ou igual a data de início de prestação de serviços e menor ou igual à data fim;
14. O campo 'Data da Convocação' deve ser maior ou igual a data de admissão do funcionário;
15. O campo 'Data Prevista de Pagamento' deve ser preenchido com uma data maior ou igual à data de resposta;
16. No cadastro de convocação para trabalho intermitente, caso o campo "Horário" seja preenchido, o campo "Descrição da Jornada" não deve ser preenchido e vice-versa, conforme leiaute do e-Social;
17. A competência dos pagamentos vinculados à convocação deverá ser, no máximo, uma competência anterior à competência de início de prestação de serviços;
18. A quantidade total de dias pagos somando-se todas as vinculações de pagamentos deverá ser menor ou igual à quantidade de dias de serviço prestado;
19. A quantidade de dias pagos por cada envelope vinculado à convocação deverá ser maior ou igual a 0 e menor ou igual a 31. Caso a quantidade de dias de prestação de serviço da convocação seja menor que 31, então esse será o valor máximo;
20. As validações acima impedem que a inclusão/edição do registro seja concluída. Entretanto, ainda outras validações são necessárias, mas não obrigatórias. As seguintes validações solicitam confirmação do usuário para incluir/editar um registro:
    1. A emissão da convocação deve ocorrer, no mínimo, 3 dias antes da data de início da prestação de serviços;
    2. O campo 'Data da Convocação' deve ser maior ou igual à data de transferência do funcionário, quando houver.

Outras regras importantes relacionadas à convocação e à vinculação de pagamentos:

* Podem ser vinculados um ou mais envelopes de pagamento ao registro da convocação. Porém, ao vincular um envelope a uma convocação, ele não poderá ser vinculado novamente a nenhuma convocação (exceto se a vinculação for excluída).

**Cálculo do pagamento para o funcionário intermitente**  
Os procedimentos abaixo visam nortear o usuário na parametrização, lançamento e cálculo para o regime intermitente observado o que trata o artigo 452-A § 6º.  
   
§ 6º Na data acordada para o pagamento, observado o disposto no § 11, o empregado receberá, de imediato, as seguintes parcelas:  
   
I – Remuneração;   
II – Férias proporcionais com acréscimo de um terço;   
III – décimo terceiro salário proporcional;   
IV – Repouso semanal remunerado; e   
V – Adicionais legais.  
   
§ 11. Na hipótese de o período de convocação exceder um mês, o pagamento das parcelas a que se referem o § 6º não poderá ser estipulado por período superior a um mês, contado a partir do primeiro dia do período de prestação de serviço.  
   
**Exemplos de fórmulas que podem ser utilizadas para o cálculo**  
Remuneração  
Código: RGITREM   
Descricão: REGIME INTERMITENTE REMUNERACAO  
Texto: (C('0506')+C('x')....)  
Deve ser informado a lista de eventos que fará parte da remuneração a ser utilizada para os cálculos proporcionais de férias e décimo  
   
DSR  
RGITDSR - REGIME INTERMITENTE DSR  
FOR('RGITREM')/6  
Está é uma forma possível para o cálculo do DSR;  
Descanso semanal remunerado do horista: considerando o que dispõe o art. 7º da Lei nº 605/49, temos que dividir o número de horas trabalhadas por 6.  
   
13º. Salário  
RGIT13 - REGIME INTERMITENTE 13 SALARIO  
(FOR('RGITREM') + FOR('RGITDSR'))/12  
Décimo terceiro seria a remuneração mais DSR dividido por 12.  
   
Férias  
RGITFER - REGIME INTERMITENTE FÉRIAS  
(FOR('RGITREM') + FOR('RGITDSR'))/12  
Férias seria a remuneração mais DSR dividido por 12.  
   
1/3 de Férias  
RGITFER3 - REGIME INTERMITENTE 1/3 DE FÉRIAS  
FOR('RGITFER')/3  
Um terço de férias é obtido do resultado do cálculo das férias dividido por 3.  
   
Referência proporcional de férias e 13º  
RGITREF - REGIME INTERMITENTE REFERENCIA FÉRIAS / 13º SALARIO  
1  
Esta formula é para colocar o valor na referência a fim de não ficar zerado o valor de referência de avos de Férias e 13º.  
A Formula "C" retorna o valor do evento do movimento atual no Mês / Ano / Período.  
A formula "MV" só pode ser para um único pagamento na competência, uma vez que soma o valor do evento em todos os períodos da competência.  
A formula "RGITREM" deve informar os eventos que farão parte da remuneração, está formula será a base para as demais.  
   
MÉDIA PARA O AVISO PREVIO INDENIZADO  
Conforme descrito no Art. 452-F O valor do aviso prévio indenizado é a metade da média paga ao intermitente nos últimos 12 meses, devendo considerar somente os meses que teve remuneração.  
Para isso pode ser usado a função "CalcMedJor" que obtém a média de uma lista de eventos   
Código: RGITMEDR   
Título: REGIME INTERMITENTE MEDIA PARA AVISO PREVIO INDENIZADO  
Texto: CALCMEDJOR (3,12,'0506;0702;0701;0501;0500', 'SNSN') em que:  
3-Aviso Prévio  
12- Os últimos 12 meses  
'0506;0702;0701;0501;0500' – lista de eventos lançadas na ficha financeira referente ao pagamento das convocações  
S – Resultado da média por valor  
N – Não considerar formula adicionais  
S – Para considerar só os meses que teve remuneração  
N – Não permitir comparação de valores de média  
   
CALCULO DO AVISO PREVIO INDENIZADO  
Código: RGITAVIR   
Descrição: REGIME INTERMITENTE AVISO PREVIO INDENIZADO  
Texto: (FOR ('RGITMEDR') / 2)  
Deve vincular esta formula a um evento que pode ter as seguintes característica:  
o    Ordem de Cálculo: 9  
o    % de Incidência: 1  
o    Provento, Valor  
o    Incidência: FGTS  
   
**Configuração dos eventos**  
Cadastrada as formula. O próximo passo será vincula-las os seus respectivos eventos.  
O entendimento que estamos tendo sobre as férias e 13º salario, não segue especificamente a legislação de férias e Décimo e sim como pagamento de folha normal. Tendo suas incidências em folha.  
   
Salário que faz parte da Remuneração  
Cadastre um novo evento para o valor das horas trabalhadas, do empregado intermitente, com as características do evento de código calculo 1 – Horas Normais, inclusive informando o código de cálculo 1.  
   
DSR, 13º Salário, Férias e Um Terço Férias  
Os demais eventos para DSR, 13º Salário, Férias e Um Terço Férias devem ser do tipo valor e suas incidências devem ser alinhadas com o jurídico da própria empresa alinha com os sindicatos das categorias.  
   
Eventos de Adicionais  
Eventos de adicionais podem ser os mesmos já usados para os funcionários não intermitente. Observando no Jurídico da empresa e Sindicato da categoria.   
Caso incidam na férias e décimo devem ser informados para que some a base para o cálculo do proporcional.  
   
0507 - REGIME INTERMITENTE AVISO PREVIO INDENIZADO  
Código de cálculo pode ser 62 Aviso Prévio  
Ordem de Cálculo: 9  
% de Incidência: 1  
Provento, Valor  
Incidência: FGTS  
Formula Valor: RGITAVIR - REGIME INTERMITENTE AVISO PREVIO INDENIZADO sintaxe da fórmula: (FOR('RGITMEDR')/2)   
Formula Referência: deve retornar os dias de direito do aviso prévio indenizado.  
   
0508 - REGIME INTERMITENTE 13 INDENIZADA  
Código de cálculo pode ser 71 13º Salário indenizado  
Ordem de Cálculo: 9  
% de Incidência: 1  
Provento, Valor  
Incidência: INSS, IRRF, FGTS  
Formula Valor: RGIT13R - REGIME INTERMITENTE 13 INDENIZADA sintaxe da fórmula: (FOR ('RGITAVIR')/12)   
Formula Referência: RGITREF - REGIME INTERMITENTE REFERENCIA FÉRIAS / 13º SALARIO sintaxe da formula: 1  
   
   
0509 - REGIME INTERMITENTE FÉRIAS INDENIZADA  
Ordem de Calculo: 70  
% de Incidência: 1  
Provento, Valor  
Incidência: Nada  
Formula valor: RGITFRA - REGIME INTERMITENTE FÉRIAS INDENIZADA Sintaxe: (FOR('RGITAVIR')/12)  
Formula Referência: RGITREF - REGIME INTERMITENTE REFERENCIA FÉRIAS / 13º SALARIO sintaxe da formula: 1  
   
0510 - REGIME INTERMITENTE 1/3 FÉRIAS INDENIZADA  
Ordem de Calculo: 75  
% de Incidência: 1  
Provento, Valor  
Incidência: Nada  
RGITFRA3 - REGIME INTERMITENTE 1/3 FÉRIAS INDENIZADA  
(FOR('RGITFRA')/3)  
   
0513 - F.G.T.S. 13º Rescisão Regime Intermitente  
Código de Cálculo pode ser informado o 31 F.G.T.S. 13º Rescisão  
Prioridade: 81  
Ordem de Cálculo: 8  
% de Incidência: 1  
Base de cálculo, Valor  
Incidência: Nada  
Formula de calculo  
RGCC31 - F.G.T.S. 13º Rescisão Regime Intermitente Sintaxe:  C('0508') \* 0.08  
Formula de referência para informar 8%  
REREFC31 - REFERENCIA F.G.T.S. 13º Rescisão Regime Intermitente retorna 8.00  
   
0514 - F.G.T.S. Quitação Intermitente  
Código de Cálculo pode ser informado o 26 F.G.T.S. Quitação  
Prioridade: 81  
Ordem de Cálculo: 8  
% de Incidência: 1  
Base de cálculo, Valor  
Incidência: Nada  
Formula de calculo  
RGCC26 - F.G.T.S. Quitação Intermitente Sintaxe: C('0507') \* 0.08  
Formula de referência para informar 8%  
REREFC31 - REFERENCIA F.G.T.S. 13º Rescisão Regime Intermitente retorna 8.00  
   
**Lançamento das verbas de folha de pagamento**  
O Lançamento e cálculo da remuneração do intermitente pode ser realizada pela "Entrada de dados do Movimento" seguido do "Lançamento de Grupo de Evento".  
No modulo "Entrada de dados do Movimento" selecione apenas os funcionários intermitente informando um filtro e efetue a entrada de dados.  
Para cada intermitente informe o evento de remuneração com o valor da hora trabalhada referente ao pagamento da convocação no período da competência atual.  
Após lançar as horas trabalhadas para os intermitentes salve todas as alterações sem efetuar o recalculo.  
Em lançamento grupo de evento crie um grupo de eventos com filtros apenas para o intermitente a fim de lançar as demais verbas que tomam como base a remuneração como Férias, DSR e 13º Salário.  
   
**SEFIP**  
No Manual do SEFIP no item 4.1.9 "As categorias previstas no SEFIP, para utilização pelo empregador, nas situações em que é devido o FGTS ", o trabalhador intermitente deve ser classificado na categoria: 04 Empregado sob contrato de trabalho por prazo determinado / Intermitente - Lei n°. 9.601/98, com as alterações da Medida Provisória n° 2.164-41, de 24/08/2001 e, Lei nº. 13.467, de 13 de julho de 2017. E no item 4.1.11.5.2 Para os trabalhadores com contrato de trabalho intermitente não deverá ser informado o R1 na admissão.  
   
**Guia de INSS**  
Para emissão da GPS nada muda. Uma vez configurada as verbas do funcionário e demais parâmetros irá considerar as incidências previdenciárias.  
   
**Folha Analítica**  
Para emissão da Folha Analítica nada muda. Uma vez configurada as verbas do funcionário e demais parâmetros irá considerar as incidências previdenciárias.  
   
**Cancelamento Folha Mensal e Férias**  
Ao realizar o processo de cancelamento de férias e/ou cancelamento de movimento mensal, é importante verificar se o envelope que está sendo cancelado está vinculado a alguma convocação. Caso esteja é necessário retirar este vínculo antes de efetuar o cancelamento.  
Para verificar acesse: 'Funcionário >> Anexo >> Movimento >> Convocação para Trabalho Intermitente >> Pagamentos'.**Cadastro de Rescisão**  
O tipo de demissão a ser utilizado é o tipo 'V – Comum Acordo'. Ao selecionar este tipo de rescisão, o eSocial fará um De/Para levando para o xml o tipo de rescisão correspondente ao layout do governo.

**Calculo de Férias**

No parametrizador Funcionário>> trabalho Intermitente foi criado o parâmetro abaixo:

Trata cadastro de férias p/contrato intermitente.

Marcando este parâmetro ao acessar o cadastro de férias o botão calculo ficará desabilitado,não permitindo nenhum calculo, pois o funcionário com contrato intermitente recebe férias ao final de cada período de prestação de serviço(férias proporcionais com acréscimo de um terço), as férias são pagas mensalmente juntamente com o salário.

**Observação:**

 - Ao fazer o lançamento não serão lançados no envelope os eventos de ferias, mas o funcionário passará de A p/ F

- Ao finalizar as férias o sistema volta o funcionário para situação Ativo.

**Rescisão Parâmetros adicionais**  
Os eventos cadastrados anteriormente que se referem especificamente a rescisão devem ser informados nos parâmetros adicionais de rescisão com formula de seleção para contemplar apenas funcionário do regime de trabalho intermitente.  
Segue um exemplo da fórmula de seleção que pode ser utilizada   
Código: TRBITSIM  
Descrição: CONSIDERA TRABALHADOR INTERMITENTE  
Sintaxe: (TABFUNC('CODTIPOCONTRATO','V') = 1)  
   
**Cálculo da rescisão**   
O RMLabore para o intermitente já calcula automaticamente a multa sobre o saldo de FGTS para fins rescisórios pela metade e os demais cálculos mediante lançamento dos eventos adicionais informado no parâmetro de rescisão.  
   
**Rescisão por transferência**  
Ao efetuar uma rescisão por transferência os registros de convocações para trabalho intermitente serão transferidos seguindo as seguintes regras:  
·          Transferência do tipo '6 - Transferência com ônus p/ Cedente' e tipo '5 - Transferência sem ônus p/ Cedente'. Quando houver convocações com o campo 'Situação da Convocação', preenchidos com uma das seguintes situações: (Aguardando resposta), (Aceita pelo funcionário) ou (Em progresso) será emitida uma mensagem de erro ao tentar transferir o funcionário, solicitando que a convocação seja finalizada para que seja possível efetivar a transferência.  
   
·          Transferência do tipo '6 - Transferência com ônus p/ Cedente'. Quando houver apenas convocações com o campo 'Situação da Convocação', preenchidos com uma das seguintes situações: (Rejeitada pelo funcionário), (Concluída), (Interrompida pelo funcionário) ou (Interrompida pelo empregador) o funcionário será transferido, porém os registros de convocação não serão copiados.  
   
·          Transferência do tipo '5 - Transferência sem ônus p/ Cedente'. Quando houver apenas convocações com o campo 'Situação da Convocação', preenchidos com uma das seguintes situações: (Rejeitada pelo funcionário), (Concluída), (Interrompida pelo funcionário) ou (Interrompida pelo empregador) o funcionário será transferido e os registros de convocações também serão transferidos.   
   
·          No caso de transferência entre coligadas somente é transferido o cadastro de convocação se o parâmetro "Permite cópia da ficha financeira na transferência entre coligadas" estiver marcado, este parâmetro fica localizado em: 'Configurações >> Parametrizador >> Rescisão Transferência'.  
   
OBS: A convocação para trabalho intermitente é copiada quando a ficha financeira do funcionário também é copiada, por este motivo a transferência entre coligadas está condicionada ao parâmetro mencionado acima.  
   
·          Transferência do tipo '5 - Transferência sem ônus p/ Cedente', quando o parâmetro "Transfere movimentação do mês atual" estiver marcado os pagamentos vinculados a convocação que se referem ao mês atual da transferência serão copiados para a nova chapa, e deletados da chapa anterior. Caso o parâmetro esteja desmarcado o registro do mês atual não é copiado para a nova chapa, e permanece na chapa anterior.   
   
É importante lembrar que este comportamento ocorre apenas para o pagamento associado a convocação, o cadastro da convocação é transferido conforme as demais regras mencionadas acima.  
   
**Cancelamento Rescisão**   
Ao realizar o processo de cancelamento da rescisão é importante verificar se o envelope onde foi calculada a rescisão está vinculado a alguma convocação. Caso esteja é necessário retirar este vínculo antes de efetuar o cancelamento.  
Para verificar acesse: 'Funcionário >> Anexo >> Movimento >> Convocação para Trabalho Intermitente >> Pagamentos'.  
**CAGED**  
O CAGED realizou uma alteração no layout criando um novo campo 'Trabalho Intermitente'. Este campo recebe a informação 1 ou 2 que corresponde a SIM e NÃO respectivamente. Para que o sistema preencha a informação com 1 é necessário marcar a flag 'Regime de Trabalho Intermitente' na aba de 'Salário/Jornada' ao cadastrar o funcionário, quando o parâmetro está desmarcado a informação será levada como 2.   
   
Algumas regras devem ser observadas ao cadastrar um novo funcionário em regime de trabalho intermitente:  
   
·          De acordo com orientações do Ministério do Trabalho no campo "horas contratuais" deverá ser informado a quantidade default igual a "1". O sistema leva para este campo por padrão o valor da jornada do funcionário que foi informado no momento da admissão, seguindo seguinte cálculo. O valor informado no campo 'Jornada' na aba de 'Salário/Jornada' é dividido pela quantidade de semanas o valor obtido é levado para o campo 'Horas Contratuais' no CAGED.  
   
·          De acordo com orientações do Ministério do Trabalho não será permitido trabalho intermitente igual a "sim" para os tipos de movimentações iguais a 25 – Contrato por Prazo Determinado, 43 – Término de Contrato por Prazo Determinado e 45 – Término de Contrato, é necessário atentar-se as orientações ao cadastrar um novo funcionário em regime de trabalho intermitente.  
·          De acordo com orientações do Ministério do Trabalho não será permitido informar trabalho intermitente igual a "sim" para contrato de trabalhador Aprendiz é necessário atentar-se as orientações ao cadastrar um novo funcionário em regime de trabalho intermitente.  
   
**Integração com o Automação de Ponto**  
Para que a Automação de Ponto (Automação de Ponto) trabalhe com funcionários adaptados ao regime de trabalho intermitente, será necessário realizar as seguintes parametrizações:  
Observação Importante: Orientamos a utilização do horário por jornada nestes casos pois, apresenta uma certa facilidade em relação ao horário por intervalo. No caso de se trabalhar com horário por intervalo, deverá ser criada a escala de horário de acordo com as convocações do funcionário.    
·          Cadastro Horário por Jornada  
Acesse o módulo de Automação de Ponto e vá em: 'Cadastros >> Horário por Jornada'.  
As flags 'Paga adicional noturno' e 'Considera redução quando a jornada iniciar a partir de', são opcionais.  
·          Cadastrar Índice da Jornada  
Dentro da jornada cadastrada anteriormente vá em 'Anexos >> Índice da Jornada', e inclua um novo índice.  
·          Vincular um horário por jornada ao funcionário.  
Na tela de cadastro de incide da jornada preencha o campo 'Horas da Jornada', este campo define a quantidade de horas que será executada pelo convocado.  
Após cadastrar o horário por jornada, será necessário a vinculação deste horário ao funcionário que     possui este tipo de regime intermitente.   
Para vincular a jornada ao funcionário acesse: Tela de funcionários vá em 'Anexos >> Horário Planejado >> Histórico de Horário da Jornada', incluir um novo registro. Ao incluir o horário por jornada, informe o horário criado anteriormente.  
Feito a vinculação, acesse o espelho de ponto do funcionário e verifique em "Visualizar Horários" e confirme se o horário está vinculado corretamente.     
Observação: caso o funcionário convocado possua mais de uma convocação (mais de um dia de trabalho combinado), será necessário cadastrar outro índice para o horário.   
Quando o funcionário não possui convocação em algum dia do contrato o sistema gera falta. Para que esta ocorrência de falta não seja gerada, será necessário a criação de um novo horário por jornada, com um índice de descanso, ou então, criar um grupo de descanso e associar este descanso as escalas do funcionário nos dias em que ocorrer ausência de convocações.  
Ao incluir um índice da Jornada, no campo 'Tipo' selecione 'Descanso'.  
Vincule este horário por jornada com o índice de descanso para o funcionário dentro de "Anexos -> Histórico de Horário -> Histórico de Horário por Jornada" e acesse o espelho do funcionário.  
·          Sindicato  
Conforme documentado acima, não será necessário carregar a informação de falta para um contrato do tipo intermitente. Desta forma, será necessário possuir um sindicato (opcional) direcionado para este tipo de contrato. Neste sindicato, não poderá conter os eventos de "Faltas" cadastrados tanto na linha "Eventos" quanto em "Eventos da Folha". Sendo assim, ao realizar o lançamento dos eventos para a folha de pagamento (Folha de Pagamento), não serão considerados faltas ao funcionário.   
Para acessar o sindicado no módulo de automação de ponto vá em: 'Ambiente >> Parâmetros >> Automação de Ponto >> Sindicato >> Eventos e Eventos da Folha'.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Segue link do TDN com as informações mais detalhadas:  
 [Convocação para Trabalho Intermitente](http://tdn.totvs.com/pages/viewpage.action?pageId=364924305)
