---
content_hash: 51fd5ff39663ec38e71ad66312e0aaeae367e4940ea832acd138129bca7896d2
fetched_at: '2026-06-29T00:10:42.205514+00:00'
page_id: '546697981'
product: rm
source: tdn-rm
title: RM - MPs COVID-19 - FAQ - Webinar
type: documentation
url: https://tdn.totvs.com/display/LRM/RM+-+MPs+COVID-19+-+FAQ+-+Webinar
version: 40
---

**PERGUNTAS E RESPOSTAS DO 1º WEBINAR**

01 - Com relação a redução de Jornada/Salário, existe valor máximo para o auxilio emergencial?

O cálculo do auxilio emergencial segue a tabela do Seguro Desemprego onde o teto é  R$1813,03.

02 - Com o (CC) 436 será possível proporcionalizar dias trabalhados e dias de atestado por Covid-19, assim como o dedução do INSS. Em caso de eventos variáveis (insalubridade, periculosidade, etc.) que incorporam a remuneração do colaborador, eles também podem ter dedução de INSS referente aos dias de atestado? Caso sim, como isso pode ser feito no RM?

O Código de Cálculo 436 funciona conforme o Código de Cálculo 145 calculado com  salário, mais as formulas adicionais de afastamento.

03 - O Módulo Folha de Pagamento disponibilizou o relatório de férias para imprimir com a data de aviso com 48 horas de antecedência?

O relatório do book FOPREL00030 - Aviso de Férias, leva a data de aviso conforme preenchimento do campo "Data de início do aviso" do Cadastro de Férias do funcionário, portanto, não teve alterações nos relatórios, basta informar a data correta do Aviso no cadastro das férias.

04 - Para a suspensão do FGTS: a empresa precisa comunicar ao Governo que não vai pagar ou basta não gerar a Guia? Como fará essa suspensão?

O procedimento de como informar a suspensão do recolhimento do FGTS deve ser realizado na SEFIP conforme a orientação na [Circular Nº 893](http://www.in.gov.br/en/web/dou/-/circular-n-893-de-24-de-marco-de-2020-249616403).

05 - Sobre as portarias 139 e 150, devemos enviar alteração de codigo dos Terceiros via eSocial ou será automaticamente considerado a redução dos percentuais? Tem alguma orientação sobre?

Neste [link](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046503773) foi documentado as instruções referente a portaria 139 no Módulo Folha de Pagamento.

Com relação ao eSocial foi divulgado a orientação de alterar as informações diretamente via DCTFWEB:  [Instruções de emissão da DARF - DCTFWeb - Vencimento Prorrogado](http://receita.economia.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/DCTFWeb/notas-orientativas/instrucoes-emissao-darf-dctfweb-vencimento-prorrogado.pdf)

06 - Quando o atestado for para prevenção de COVID-19, dos 14 dias pode deduzir no INSS?

A MP fala que será abatido os primeiros 15 dias de afastamento do trabalho dos segurados se o empregado for diagnosticado com coronavírus. Não fala de atestado de prevenção.

07 - Referente a esse cadastro do BEM, a data que vai para o S-2206 será a informada no campo de DATA DO ACORDO ou DATA DA MUDANÇA?

É considerado a Data de Acordo que é data Data de início da vigência do acordo firmado entre o empregador e o empregado. A data de Mudança é para preenchimento de Histórico. 

08 - Fazendo o preenchimento da Aba B.E.M. no cadastro do Funcionário, o envelope de pagamento já calcula considerando o salário com a Jornada Reduzida?

A redução será calculada em um evento de desconto calculado por fórmula conforme exemplo em nossa documentação neste [Link](https://tdn.totvs.com/pages/viewpage.action?pageId=545621517). 

09 - O preenchimento da TAG de OBSERVACAO no S-2206, trará a informação de qual campo no sistema RM?

A tag OBSERVACAO terá as informações do prazo da Redução da Jornada/Salário e o percentual definido no campo 'Percentual de Redução de Jornada' no cadastro do Funcionário | Aba B.E.M. Ele será preenchido de forma automática na geração do evento S-2206. Mais informações pode ser consultadas [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=545621517).

10 - O campo valor Reduzido Recebe qual valor?

O campo Valor Reduzido recebe a parte proporcional que será baseada para o cálculo do auxilo emergencial pago pelo Governo. Exemplo:

Funcionário recebe R$ 3000,00 e teve a redução de 25%. O campo Valor Reduzido deverá ser preenchido com 750,00.

Mais informações sobre o campo pode ser consultadas [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=545621517).

11 - A Redução de Jornada/Salário pode ser realizada em qualquer dia do mês?

A redução de Jornada/Salário pode ser realizada em qualquer dia do mês. Com relação ao cálculo da Folha Mensal é possível realizar a parametrização para que o cálculo do desconto seja de forma proporcional.

Mais informações sobre o campo pode ser consultadas [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=545621517).

12 - Há algum problema em a data do acordo ser 21/04/2020, já que é um feriado?

A nível de produto não há problemas. Nossa orientação é acionar sua consultoria e verificar se você poderá proceder com a alteração nesta data.

**PERGUNTAS E RESPOSTAS DO 2º WEBINAR**

01 - Antecipei férias e não marquei o parâmetro o que fazer?

Disponibilizamos a documentação de como o produto trata a antecipação de férias com o parâmetro marcado/desmarcado:

.

02 - Para o cálculo correto de atrasos e horas extras criei novos horários no RM Chronus e vinculei nos funcionários esse é o procedimento correto?

Sim. Disponibilizados um documento orientativo: 

Só observar a orientação para envio do e-Social, utilizando o parâmetro implementado: .

03 - Faltas serão descontados por valor integral do salário ou considerado reduzido.

Recomendamos que valide com seu departamento jurídico as questões e detalhes da legislação. Conforme comentado durante a apresentação existem 'possibilidade' de interpretações adversas, em ambos casos existem benefícios e riscos que devem ser analisados com cautela, recomendamos a análise jurídica de sua empresa.

04 - Reduzir ou Suspender aposentados -, o que vocês entendem pelo texto da portaria? § 2º É vedada a celebração de acordo individual para redução proporcional de jornada de trabalho e de salário ou para suspensão temporária do contrato de trabalho com empregado que se enquadre em alguma das vedações à percepção do BEM previstas neste artigo (portaria 10.486).

Recomendamos que valide com seu departamento jurídico as questões e detalhes da legislação. Conforme comentado durante a apresentação existem 'possibilidade' de interpretações adversas, em ambos casos existem benefícios e riscos que devem ser analisados com cautela, recomendamos a análise jurídica de sua empresa.

05 - Sobre a MP 927 já existe algum posicionamento sobre o pagamento de 1/3 de férias? 

Para o pagamento de 1/3 em Folha, foi atualizado a documentação, veja através do link: 

Caso o pagamento do 1/3 seja via rescisão, veja através do link:

06 - Caso a MP 932 decline e precisarmos voltar o valor das alíquotas de terceiros como era antes de forma nominal. Como voltaremos o sistema?

Para facilitar esse processo de alteração de Terceiros, foi liberado a opção de alteração desse campo de forma global. Caso tenha usando o histórico de percentual de INSS é só alterar o fim da vigência, conforme orientado:  <https://tdn.totvs.com/pages/viewpage.action?pageId=547234754> 

Se não tiver usando o histórico de percentual de INSS e alterado direto no cadastro de seção no campo %Terceiros, deverá fazer o ajuste manual. 

07 - Onde posso controlar os dias de férias pendentes para um colaborador ou se caso ele retorne das férias antecipadamente, como teremos este controle?

No Folha de Pagamento na aba Férias, tem a rotina chamada: Marcação, retorna em tela informações como Período Aquisitivo Aberto do funcionário, Data Limite de Gozo e saldo de férias.

Também é disponibilizado relatórios que podem auxiliar nesse controle, como:

* FOPREL00184 - Escala Mensal de Férias.TotvsReport
* FOPREL00032 - Funcionários com Férias Vencidas.TotvsReport
* FOPREL00031 - Escala Anual de Férias.TotvsReport
08 - Quando a empresa suspendeu o contrato por 30 dias e passados os 30 vai prorrogar por mais 30. Como informar essa "retificação" ao Governo?

Neste caso tem que enviar um Arquivo do BEM com o novo acordo.

09 - Quando a empresa reduziu a Jornada/Salário por 30 dias e vai prorrogar por mais 30 dias alterando o percentual, como proceder? Vamos alterar o histórico já existente no RM ou vamos criar um novo e enviar um novo Layout?

Deve alterar no cadastro do Funcionário e gerar um novo arquivo, pois para geração do arquivo do Beneficio Emergencial são consideradas as informações da aba B.E.M.

10 - A Empresa fez a comunicação do Acordo de redução de Jornada/Salário, porém o funcionário pediu demissão. Mesmo enviando o S-2299 para o e-social é cruzada essas informações com Empregador Web?

O e-social e Empregador Web não são integrados. Quando preenche os campos da aba BEM é gerado o S-2206.

Neste caso é necessário restabelecer a jornada/salário do funcionário antes enviando um evento S-2206 antes de enviar o S-2299.

Com relação ao Empregador Web o ajuste do período da redução deve ser feito diretamente no portal.

 11 - Devemos aguardar a liberação do layout do bem com a opção de exclusão e alteração?

O Empregador Web lhe permite ajustes manuais diretamente no portal. Antes que seja liberado o layout para alteração/exclusão o único caminho será o reenvio do arquivo para sobrepor, ou ajuste manual. Entretanto em ambos não é possível a exclusão.

12 - Realizando o acordo do 50% é gerado o S-2206, mas também fica pendente de reduzir a carga horária e enviar o evento de horário do funcionário?

Colocamos na documentação o procedimento e tratativas que implementamos para envio do e-Social para o caso de redução de Jornada feita no módulo automação de ponto: .

13 - Com relação a Estabilidade, o sistema irá gerar automaticamente, lá em Anexo/folha de pagamento/estabilidade?

Não será gerado estabilidade neste anexo para os casos previsto nesta MP. O Módulo Folha de Pagamento possuiu um recurso de mensagem que pode ser usando para informar se o funcionário tem estabilidade. Fizemos uma documentação para exemplificar o uso do recurso: 

14 - Fizemos o cadastro do funcionário do BEM (aba) e as fórmulas para a geração da folha de pagamento, porém trabalhamos com pagamento dia 20 (vale) e quinto dia útil (salário). No caso do salário, utilizamos a fórmula da redução de jornada, associada a um evento. Como faremos para lançar o vale, dia 20. Tem algum procedimento específico

No Lançamento da Folha, será pago o salário integral e deduzido o desconto da redução e adiantamento salarial, obtendo um mesmo líquido/resultado, portanto fica a cargo da Empresa em decidir pagar o adiantamento reduzido ou não. Normalmente o evento de pagamento de adiantamento de salário, é calculado através de formula, é só adequar a fórmula do pagamento de adiantamento, para abater o valor do percentual reduzido proporcional ao adiantamento.
