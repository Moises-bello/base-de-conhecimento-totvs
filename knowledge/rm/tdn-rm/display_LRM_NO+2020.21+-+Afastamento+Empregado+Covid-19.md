---
content_hash: 3344de252e6d5d665c62185dc1d7a7edea8aafb9a964dec813b968d3d473775d
fetched_at: '2026-06-29T00:10:39.067444+00:00'
page_id: '545647646'
product: rm
source: tdn-rm
title: NO 2020.21 - Afastamento Empregado Covid-19
type: documentation
url: https://tdn.totvs.com/display/LRM/NO+2020.21+-+Afastamento+Empregado+Covid-19
version: 33
---

Conforme a Nota Orientativa 2020.21, A Lei nº 13.982 de 02 de abril de 2020, artigo 5º, autoriza as empresas a deduzirem de suas contribuições devidas à previdência social os valores pagos em relação aos 15 primeiros dias de salário do trabalhador afastado por enfermidade causada pelo Covid-19.

**Procedimento na Folha de Pagamento**

false

**A implementação foi disponibilizada a partir dos patchs abaixo:**

* **12.1.25.271 ou superior**
* **12.1.26.217 ou superior**
* **12.1.27.173 ou superior**
* **12.1.28.107 ou superior**

**Código de Cálculo**

Para atender a NO 2020.21, foi criado o código de cálculo (CC) 436 - Atestado Médico de afastamento por COVID-19 que irá considerar o valor a deduzir conforme regras estabelecidas na NO no eSocial, GPS e SEFIP. Mais informações do Código de Cálculo pode acessadas neste [Link](https://tdn.totvs.com.br/pages/releaseview.action?pageId=546670916)

Também foi criado o Código de Cálculo (CC) 437 - Diferença de atestado Médico de afastamento por COVID-19 que irá armazenar a diferença do evento de CC 436 na diferença Salarial e Rescisão Complementar.

O evento deve ser cadastrado como Base de Cálculo, sem nenhum incidência.

falseDica

Para que os Códigos de Cálculos sejam disponibilizados no produto para cadastro, é necessário executar qualquer processo de cálculo, como por exemplo, o processo 'Executa Recalculo'.

**Parametrizador**

Foi criado o campo 'Motivo de Afastamento por COVID-19' no parametrizador para que seja identificado o afastamento por COVID-19. O campo está localizado em Parametrizador | 06.01 - Folha de Pagamento | 06.01.03 - Folha Normal | Afastamento.

Este mesmo motivo deve ser preenchido nos afastamentos por COVID-19 para a identificação correta. Neste caso poderá incluir um novo motivo na tabela dinâmica INT28 ou usar um já existente. Orientamos a não usar o motivo informado no parametrizador para afastamento que não seja de COVID-19. No nosso exemplo criamo um novo motivo na tabela dinâmica e associamos o mesmo no parametrizador, conforme a ilustração abaixo:

Tabela Dinâmica:

Parametrizador:

**Afastamento**

No cadastro do afastamento informar o motivo associado no parametrizador, conforme abaixo:

**Folha de Pagamento**

Ao fazer o Lançamento para o envelope de pagamento, é lançado o evento de Base de Cálculo conforme cadastrado acima. Este valor irá considerar somente a parte de afastamento por COVID-19 que deve ser deduzido no INSS.

Exemplo 1: Funcionário que teve somente um afastamento de 20 dias no mês de abril. Foi lançado o evento de CC 145 com o valor do atestado e o evento CC 436 com o valor dedutível por COVID-19.

Exemplo 2:  Funcionário teve três afastamentos de tipo e motivo diferente, no mês de abril. sendo um deles sem retorno. O produto calculou 20 dias de atestado, mas a parte referente ao atestado por COVID-19 é referente a 10 dias e os mesmo foram lançados no evento de CC 436:

falseAtenção

* O valor lançado no evento de atestado por COVID-19 é limitado ao Salário Contribuição, para os casos onde o valor do afastamento pago pela empresa seja maior que o Salário Contribuição.
* Para os casos de funcionários que tem afastamentos iniciando em um mês e terminando no próximo mês, o valor do evento será calculado considerando o afastamento como todo e lançado proporcionalizado.
* Será lançado no primeiro mês o valor considerando o total do afastamento limitando ao valor do afastamento pago pela empresa naquele mês e o Salario Contribuição. Caso o valor da dedução seja menor que o salário contribuição, o restante será lançado na próxima competência (onde existe pagamento de atestado pago pela da empresa).

**GPS**

Na GPS, o valor é levado no campo dedução para ser deduzido do valor da Guia. A Guia foi gerada considerando somente o funcionário do exemplo 1 acima:

**SEFIP**

Na SEFIP, o valor da dedução é levado para o campo Salario Família. O arquivo da SEFIP foi gerado considerando somente o funcionário do exemplo 1 acima:

**eSocial**

falseAtenção

* Caso os eventos S-1010 e S-1200 tenham sido enviados antes dos Patches **12.1.25.271, 12.1.26.217, 12.1.27.173 e 12.1.28.107**, será necessário realizar uma retificação para correta dedução. Veja mais detalhes no [TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=547236037)

Conforme orientação do eSocial, em afastamento por motivo de COVID-19, deve criar uma nova rubrica informativa utilizando o código de incidência de contribuição previdenciária = 51 (o mesmo de salário-família) e a Natureza de Rubrica = 9933 (auxílio-doença) e informar o valor da rubrica (quinze primeiros dias de afastamento por COVID-19) até o limite máximo do salário-de-contribuição.

No cadastro do evento acima, foi informado a Natureza de Rubrica = 9933. No evento S-1010 foi gerado considerando as informações conforme orientado:

falseImportante

A partir de 02/07/2020 encerrou-se o prazo de direito à dedução do custo salarial referente aos 15 primeiros dias de auxílio dos trabalhadores acometidos de afastamento por Covid-19. Para que não seja lançado o evento de CC 436, basta retirar o motivo de afastamento por COVID-19 do parametrizador. Desta forma, com o evento não lançado na ficha financeira do funcionário, não será feito mais a dedução prevista nesta Nota orientativa.
