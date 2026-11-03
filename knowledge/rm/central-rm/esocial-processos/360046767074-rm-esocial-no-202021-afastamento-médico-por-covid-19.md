---
article_id: 360046767074
category: esocial - Processos
content_hash: 3686354ae3f9abf20f76b6fbbe804f6a8ad1973e2ab545d636f2e5dcb0dec5e0
fetched_at: '2026-06-28T22:47:08.455540+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RM - eSocial - N.O. 2020.21 - Afastamento médico por Covid-19
type: support-article
updated_at: '2021-04-09T12:35:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046767074-RM-eSocial-N-O-2020-21-Afastamento-m%C3%A9dico-por-Covid-19
---

**Dúvida**  
Como realizar a dedução dos valores pagos em relação aos 15 primeiros dias de salário do trabalhador afastado por  Covid-19 das contribuições devidas à previdência social?  
  
**Ambiente**  
RM - eSocial - A partir dos *Patches* 12.1.25.271, 12.1.26.217, 12.1.27.173 e 12.1.28.107  
  
**Solução**  
O governo orientou na **N.O. 2020.21** que durante os primeiros quinze dias consecutivos ao do afastamento da atividade por motivo de doença, incumbirá à empresa pagar ao segurado empregado o seu salário integral. A Lei nº 13.982 de 02 de abril de 2020, artigo 5º, autoriza as empresas a deduzirem de suas contribuições devidas à previdência social os valores pagos em relação aos 15 primeiros dias de salário do trabalhador afastado por enfermidade causada pelo Covid-19.

Para usufruírem desse direito, as empresas devem adotar as seguintes ações:

1. A empresa deve continuar lançando o valor referente aos 15 primeiros dias de afastamento na rubrica usual. Ou seja, deve ser mantido o tipo, a incidência e informado o valor total da rubrica. Isto se deve ao fato de a lei limitar o direito apenas aos casos de Covid-19 e ainda em decorrência da limitação do direito ao limite máximo do salário-de-contribuição;  
2. Adicionalmente, em afastamento por motivo de Covid-19, deve criar uma nova rubrica informativa utilizando o código de incidência de contribuição previdenciária = 51 (o mesmo de salário-família) e a Natureza de Rubrica = 9933 (auxílio-doença) e informar o valor da rubrica (quinze primeiros dias de afastamento por Covid-19) até o limite máximo do salário-de-contribuição.

Desta forma não haverá tributação e o valor dessa rubrica será enviado para a DCTFWeb para dedução, junto com os valores referentes ao salário-família, quando for o caso. A RFB fará a distinção dos benefícios a partir do código da tabela de natureza de rubrica.

No TOTVS Folha de Pagamento foi criado o código de cálculo (CC) [436 - Atestado Médico de afastamento por COVID-19](https://tdn.totvs.com.br/pages/releaseview.action?pageId=546670916) que irá considerar o valor a deduzir conforme regras estabelecidas na **N.O.** no eSocial, GPS e SEFIP. Também foi criado o Código de Cálculo (CC) [437 - Diferença de atestado Médico de afastamento por COVID-19](https://tdn.totvs.com.br/pages/releaseview.action?pageId=546670920) que irá armazenar a diferença do evento de CC 436 na diferença Salarial e Rescisão Complementar. 

Assim, para enviar corretamente os dados para o eSocial, siga as orientações abaixo:

1. Acesse o menu **Administração de Pessoal | Eventos**;  
1.1. Cadastre um novo evento com o CC **436** e outro com CC **437**, ambos como base de cálculo, com natureza da rubrica **9933** e sem incidência;  
1.2. Será gerado o **S-1010** para os eventos cadastrados. Informe no gatilho o início da competência 04/2020, gere o XML e transmita ao governo;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360067652334/mceclip1.png)

2. Acesse o menu **Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Afastamento**;  
2.1. Preencha o campo **Motivo de Afastamento por COVID-19** com o mesmo motivo que será preenchido nos afastamentos por Covid-19. Poderá ser incluído um novo motivo na tabela dinâmica **INT28** ou usar um já existente. Importante não preencher com um motivo que seja usado para afastamentos não vinculados ao Covid-19;

![](https://tdn.totvs.com/download/attachments/545647646/image2020-4-22_14-31-38.png?version=1&modificationDate=1587576699714&api=v2)

3. Ao realizar o cadastro do afastamento do funcionário, informe o motivo de afastamento utilizado no **passo 2**;

![](https://tdn.totvs.com/download/attachments/545647646/image2020-4-22_15-4-44.png?version=1&modificationDate=1587578685641&api=v2)

4. Ao fazer o lançamento da folha para o envelope de pagamento, será lançado o evento de Base de Cálculo cadastrado no **passo 1.1**. Este valor irá considerar somente a parte de afastamento por Covid-19 que deve ser deduzido no INSS.

**Importante**  
Para que os códigos de cálculos sejam disponibilizados no produto para cadastro, é necessário executar qualquer processo de cálculo, como por exemplo, o processo **Executa Recálculo**.

Caso os eventos S-1010 e S-1200 tenham sido enviados antes dos Patches indicados acima na área **Ambiente**, será necessário realizar uma retificação para correta dedução. Ver artigo [Alteração de evento para dedução de INSS em afastamentos por Covid-19.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047675133)

O valor lançado no evento de atestado por Covid-19 é **limitado ao salário contribuição**, para os casos onde o valor do afastamento pago pela empresa seja maior que o Salário Contribuição. 

Para os casos de funcionários que tem afastamentos iniciando em um mês e terminando no próximo mês, o valor do evento será calculado considerando o afastamento como todo e lançado proporcionalizado. 

Será lançado no primeiro mês o valor considerando o total do afastamento limitando ao valor do afastamento pago pela empresa naquele mês e o salario contribuição. Caso o valor da dedução seja menor que o salário contribuição, o restante será lançado na próxima competência (onde existe pagamento de atestado pago pela da empresa).  
  
**Saiba mais**  
Para mais informações como exemplos de cálculo da folha, Sefip e GPS, acesse:  
      • [NO 2020.21 - Afastamento Empregado Covid-19](https://tdn.totvs.com/display/public/LRM/NO+2020.21+-+Afastamento+Empregado+Covid-19)      • [RM - eSocial - Alteração de evento para dedução de INSS em afastamentos por Covid-19](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047675133)  
      • [RM - eSocial - Adequações e Alternativas Trabalhistas - COVID-19](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046489613)
