---
content_hash: 3f1f2475d4ff4243a4c855f1a4cf159e0fe076de70ceee02b9c8491f584147ad
fetched_at: '2026-06-29T00:10:05.251992+00:00'
page_id: '452719280'
product: rm
source: tdn-rm
title: Encargos - Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Encargos+-+Folha+de+Pagamento
version: 37
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Tipos de Encargos**
3. **Parâmetros e Campos**
4. **Tabelas Utilizadas**
5. **Assuntos Relacionados**

## **01. VISÃO GERAL**

Este cadastro é destinado para os cadastros de encargos, para que o mesmos possam ser calculados nativamente conforme os tipos e parametrizações disponíveis e ainda tem a opção de customizar por fórmula.

## **02.** **TIPOS DE ENCARGOS**

O TOTVS Folha de Pagamento disponibiliza os tipos de encargos abaixo. Este tipos de encargos são nativos no produto e constam na Tabela dinâmica INT01. Não é permitidos incluir novos encargos pelo usuário esta tabela dinâmica,

* 2 - Base: incidência de FGTS
* 3 - Base: incidência de INSS
* 4 - Provisão de férias
* 5 - Provisão de FGTS de férias
* 6 - Provisão de encargos de férias
* 7 - Provisão de 13o. salário
* 8 - Provisão de FGTS de 13o. salário
* 9 - Provisão de encargos 13o. salário
* A - Valor calculado através de fórmula
* G - Dedução 13o ref. a lic. maternidade
* H - Base: incidência de INSS de 13o. salário
* M - Base: incidência de FGTS de 13o. salário
* R - Base: incidência de INSS Dissídio (a partir do Release 12.1.29)
* S - Base: incidência de INSS de 13o. salário Dissídio (a partir do Release 12.1.29)
* T- Base INSS DCTFWeb (a partir do release 12.1.2410)
* U- Base INSS 13º Salário DCTFWeb (a partir do release 12.1.2410)

Para o encargo Tipo R - Base: incidência de INSS Dissídio, o produto verifica o valor do evento de Código de Cálculo [415 - Base de INSS diferença Salarial por Dissídio](https://tdn.totvs.com.br/pages/viewpage.action?pageId=488864232) lançado na PFVERBASDIS, aba "Verbas geradas por diferenças" do anexo da Ficha Financeira do funcionário.

Observação:

Precisa existir um evento com o Código de Cálculo [415 - Base de INSS diferença Salarial por Dissídio](https://tdn.totvs.com.br/pages/viewpage.action?pageId=488864232) cadastrado, antes de executar os processos de Diferença / Rescisão Complementar.

Para o encargo Tipo S - Base: incidência de INSS de 13o. salário Dissídio o produto verifica os eventos lançados na PFVERBASDIS  onde no evento está configurado com incidência em INSS 13º Salário e não está marcado Incidência exclusiva segurado ou o evento está configurado com incidência exclusiva empregador.

Para os encargos tipo **T**:  Base INSS DCTFWeb e tipo **U**: Base INSS 13º Salário DCTFWeb, a base será composta com o eventos lançados na Ficha Financeira do colaborador referente ao pagamento mensal + os eventos de dissídio lançados na PFVERBASDIS e PFVERBASDISFER. Logo, será o retorno das bases dos encargo serão:

* + Encargo tipo T: Tipo 3 - Base: incidência de INSS + Tipo R - Base: incidência de INSS Dissídio
  + Encargo tipo U: Tipo H - Base: incidência de INSS de 13º salário + Tipo S - Base: incidência de INSS de 13º salário Dissídio

Além disto, para estes novos encargos foi disponibilizado a opção para considerar o Histórico de Percentual para INSS da Seção e percentual de Redução cadastrado no Período de Apuração do eSocial.

Dica

Veja também: [FAQ - Encargos - Base de INSS e Base de INSS 13º conforme DCTFWeb](https://tdn.totvs.com/pages/viewpage.action?pageId=866529609)

Em conformidade com o disposto no artigo 2º da Lei 10.097/00, onde altera o artigo 15º da Lei 8036/90, que determina que os contratos de aprendizagem com admissão a partir de 20/12/2000 tenham sua alíquota do FGTS reduzida de oito por cento para dois por cento.   
Para fins de contabilização de encargos, no cadastro de encargos o usuário deverá incluir mais dois códigos encargos do tipo 5 e 8 com porcentagem 2:   
Provisão FGTS de 13º salário Aprendiz;  
Provisão FGTS de férias Aprendiz.  
Incluir a fórmula de seleção para estas situações conforme a seguir:  
SE (TFUNC = 'Z') e (DTA >= '20/12/2000')  
ENTAO VERDADE  
SENAO FALSO  
   
Deverá incluir também fórmula de seleção para situações de provisão do FGTS sobre 13º e férias, para demais funcionários com porcentagem 8, porém de forma inversa ou seja:  
SE (TFUNC = 'Z') e (DTA >= '20/12/2000')  
ENTAO FALSO  
SENAO VERDADE  
   
Os encargos 2, 3, H e M são Bases de incidências e os encargos 4, 5, 7, 8 são relativos a valores a provisionar de férias e 13º salário e se este tratamento for aplicado a estes encargos o usuário que necessitar contabilizar apenas as bases de incidências ou provisões não conseguirá.

Atenção

Os tipos de encargos 1, B, C, D, E, F, I e J foram descontinuados por serem combinações dos tipos enumerados acima. Todavia, estes encargos estão cadastrados na tabela dinâmica INT01 para efeitos de compatibilidade com o RM Folha e para permitir importação de dados desse sistema. Caso haja a necessidade de contabilizá-los, deverá ser criado um encargo do tipo "A - Valor calculado através de fórmula", utilizando uma fórmula adequada a cada tipo de encargo.

## **03. PARAMETROS E CAMPOS**

**Porcentagem**

Este campo só ficará habilitado para os tipos de encargos abaixo:

* 2 - Base: incidência de FGTS
* 3 - Base: incidência de INSS
* 5 - Provisão de FGTS de férias
* 6 - Provisão de encargos de férias
* 8 - Provisão de FGTS de 13º salário
* 9 - Provisão de encargos 13º salário
* G - Dedução 13º ref. a lic. maternidade
* H - Base: incidência de INSS de 13º salário
* M - Base: incidência de FGTS de 13º salário
* R - Base: incidência de INSS Dissídio (a partir do Release 12.1.29)
* S - Base: incidência de INSS de 13º salário Dissídio (a partir do Release 12.1.29)
* T- Base INSS DCTFWeb (a partir do release 12.1.2410)
* U- Base INSS 13º Salário DCTFWeb (a partir do release 12.1.2410)

**Ordem de Cálculo**

O campo 'Ordem de Cálculo' só ficará visível para o tipo de encargo **A - Valor calculado através de formula** e servirá para definir a prioridade e/ou ordem de cálculo  de um encargo do tipo 'A - Valor calculado através de fórmula', que utilizar o valor de um outro encargo do tipo 'A - Valor calculado através de fórmula', para retornar o valor através de uma variável de fórmula (VALENCARGOM) para o encargo que for receber o valor calculado no primeiro encargo.

Exemplo

Encargo 0010 - Encargo 0010

Fórmula de valor:  RC \* 0,08

Ordem de cálculo: 1

Encargo 0009 - Encargo 0009

Fórmula de valor: VALENCARGOM('0010') + 100

Ordem de cálculo: 2

Neste caso a 'Ordem de Cálculo' do encargo 'Encargo 0010' deverá ser menor que a 'Ordem de cálculo' do encargo 'Encargo 0009' e a 'Fórmula de valor' do encargo 'Encargo 0009' deverá conter a variável VALENCARGOM para recuperar o valor.

**Formula de Seleção**

A fórmula de seleção servirá para excluir alguns tipos de funcionário (por exemplo, autônomos e estagiários) da base de cálculo dos encargos.

Exemplo de fórmula de seleção

SE TFUNC <> 'A' E TFUNC <> 'T'

ENTAO VERDADE

SENAO FALSO

FIMSE

Neste caso o cálculo dos encargos será feito para funcionários cujo tipo seja diferente de 'A' - autônomos - e 'T' - estagiários

**Formula de Valor**

O campo Fórmula de valor só ficará habilitado se o encargo for do tipo A - Valor Calculado através de fórmula

**Aplicar Arredondamento sobre o valor total**

O parâmetro "Aplicar Arredondamento sobre o valor total do encargo" será utilizado quando o cálculo do encargo para cada funcionário é realizado sem arredondamento então, somente ao gerar o lançamento contábil será aplicado o arredondamento sobre a soma dos valores individuais de cada funcionário.  
Dessa forma, a diferença entre a soma dos valores dos funcionários e do valor final arredondado geral do lançamento é apurada. Essa diferença é adicionada tanto ao lançamento contábil quanto no histórico de encargos.

Atenção

O parâmetro "Trunca valores de FGTS/INSS" localizado em parametrizador | Folha Normal | Encargos Sociais, interfere nos cálculos de arredondamento dos encargos de FGTS. O parâmetro "Trunca valores de FGTS/INSS" marcado têm prioridade sobre o parâmetro "Aplicar arredondamento sobre o valor total do encargo", também marcado, durante a geração do encargo. Os tipos de encargos afetados são:

* 2 - Base: incidência de FGTS
* 5 - Provisão de FGTS de férias
* 8 - Provisão de FGTS de 13o. salário
* M - Base: incidência de FGTS de 13o. salário

**Provisão Acumulada**

Selecionando a provisão acumulada será gerada acumulada para os encargos do tipo:  
4 - Provisão de Férias  
5 - Provisão de FGTS de Férias  
6 - Provisão de Encargo de Férias  
7 - Provisão de 13º Salário  
8 - Provisão de FGTS de 13º salário  
9 - Provisão de encargos 13º salário  
   
Este parâmetro influenciará diretamente no valor do encargo tipo "8" (Provisão de FGTS de 13º salário).

* Se o parâmetro estiver marcado o sistema irá subtrair da base de cálculo de FGTS de 13º salário o valor do adiantamento de 13o. (se este tiver sido pago dentro do mês).
* Se parâmetro não estiver marcado o valor de adiantamento não será descontado da base de cálculo de FGTS de 13º salário.

Dica

01 - Veja também: [Exemplos para regra de cálculo dos encargos 5 - Provisão de FGTS de férias e 6 - Provisão de encargos de férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=790646098#1-1)

02 - Veja sobre transferência do histórico de provisões em [Rescisão - RHU](https://tdn.totvs.com/pages/editpage.action?pageId=452719347)

**Considera Centro de Custo da Seção Anterior**

O parâmetro "Considera Centro de Custo da Seção Anterior" permite o estorno das Provisões de Férias e 13º Salário. O estorno de provisão é geralmente aplicado na situação em que funcionário estava em centro de custo diferente do atual no mês anterior. Sendo assim, o funcionário que foi transferido de seção (não mudou de CGC) e mudou do centro de custo X para Y, ao gerar a contabilização do encargo de provisão ocorrerá o estorno da provisão do mês anterior.  
   
Para que seja efetuado o estorno deverão ser criados dois encargos. O primeiro encargo, com a opção "Considera Centro de Custo da Seção Anterior" marcada e efetuando o débito (estorno) no centro de custo ligado à seção onde o funcionário estava lotado anteriormente. O segundo encargo, com a opção "Considera Centro de Custo da Seção Anterior" desmarcada e efetuando o crédito no centro de custo ligado à seção atual do funcionário.  
   
Estes encargos deverão utilizar fórmula de seleção para filtrar funcionários que tenham mudado de centro de custo, e ambos utilizarão a fórmula de cálculo que retorne o valor da provisão acumulada da competência anterior.

Este parâmetro só será habilitado para o encargo do tipo A – Valor calculado através de fórmula e se o parâmetro "Utiliza Cálculo por Centro de Custo" em Parametrizador | Folha Normal | Cálculo 2/2 estiver desmarcado.

**Deduz Verde e Amarelo**

Este parâmetro atende a **Medida Provisória nº 905/2019**, publicada em 11 de novembro de 2019, onde menciona a desoneração da folha de pagamento em que a empresa passa a ser isenta do recolhimento de contribuição patronal do INSS (de até 20% sobre o total da remuneração paga nas demais modalidades de contratação), salário-educação e contribuição social destinada ao Sistema S.

Este tipo de contratação, todavia, se aplica para **salários de até 1,5 salário mínimo.**

Com isso ao marcar o parâmetro o sistema irá deduzir o valor do contrato Verde e Amarelo da Base de INSS, conforme a regra estabelecida.

A regra é aplicada somente para funcionário com categoria do eSocial igual a:

“**107 - Empregado - Contrato de trabalho Verde e Amarelo - sem acordo para antecipação mensal da multa rescisória do FGTS**” ou

“**108 - Empregado - Contrato de trabalho Verde e Amarelo - com acordo para antecipação mensal da multa rescisória do FGTS conforme Medida Provisória n° 905, de 2019 (Programa Verde e Amarelo)**”.

O parâmetro ficará habilitado apenas para o encargo do Tipo '**3-Incidência de INSS**' e **'R - Base: incidência de INSS Dissídio**'.

**Aplicar Percentual FAP por filial**

Marcando este parâmetro o valor do encargo será acrescido do seguinte calculo: (Valor base do encargo) multiplicado pelo (Percentual do FAP vigente) multiplicado pelo (Percentual do SAT - agora denominado RAT), onde:

* "Valor base do encargo": Valor obtido pelo sistema antes da aplicação do percentual informado na parametrização do encargo.
* "Percentual do FAP" vigente: Percentual informado na seção centralizadora da filial (em "Cadastro | Seções | Anexo FAP por Estabelecimento  Empresarial")
* "Percentual do SAT": Percentual informado no cadastro da seção do funcionário.

Exemplo

Encargo do tipo **3-Incidência de INSS** com o campo "Porcentagem" preenchido com 20.

Seção centralizadora da filial informado o FAP 2,0000

Seção do funcionário informado 3% no campo SAT

Base de INSS = 1.000,00

Campo porcentagem = 20%

O calculo será ((1000,00\*20%) + (1000,00 \*(2,0000\*3%))) = 260,00

**Acréscimo de Aposentadoria Especial**

Este parâmetro ficará habilitado no cadastro de encargos quando os tipos abaixo para indicar o acréscimo de aposentadoria especial.

* 3 - Base INSS Empresa
* H - Base INSS Empresa 13º Salário
* R - Base: incidência de INSS Dissídio
* S - Base: incidência de INSS de 13o. salário Dissídio
* T- Base INSS DCTFWeb
* U- Base INSS 13º Salário DCTFWeb

Aposentadoria Especial são as alíquotas de contribuição destinadas ao financiamento da aposentadoria especial prevista nos Art. 57 e 58 da Lei nº 8.213/91, concedida em razão de maior incidência de incapacidade laborativa decorrente de riscos ambientais do trabalho (até junho/97, Seguro de Acidentes do Trabalho). Será acrescida dos valores digitados em pontos percentuais, conforme a atividade exercida pelo segurado a serviço da empresa permita, a concessão de aposentadoria especial após 15, 20 e 25 anos de contribuição, respectivamente.

O acréscimo incide exclusivamente sobre o total das remunerações pagas ou creditadas, no decorrer do mês, aos segurados empregados e trabalhadores avulsos sujeitos a condições especiais.

Para calcular o acréscimo de aposentadoria especial é necessário que os percentuais sejam cadastrados na seção aba Dados p/ INSS e é verificado o código de ocorrência do colaborador no Menu FGTS/Sefip se o mesmo foi exposto a agente nocivo.

Exemplo

Percentual de acréscimo para 15 anos de aposentadoria = 4  
Percentual de acréscimo para 20 anos de aposentadoria = 3  
Percentual de acréscimo para 25 anos de aposentadoria = 2

Base de INSS do Colaborador com aposentadoria 20 anos = R$ 500,00  
Base de INSS do Colaborador com aposentadoria 15 anos = R$ 300,00  
  
R$ 500,00 \* 3% (percentual de acréscimo 20 anos) = R$ 15,00  
R$ 300,00 \* 4% (percentual de acréscimo 15 anos) = R$ 12,00

A alíquota de SAT (agora denominada RAT) para funcionários com aposentadoria especial (15, 20, 25 anos) será tratada durante a contabilização para os encargos 6 e 9 porque somente estes encargos são de responsabilidade da empresa.

**Considerar Histórico de percentuais para INSS**

Este parâmetro somente ficará disponível para os tipos de encargos T  e U  e se somente ficará habilitado caso o parâmetro 'Habilita Histórico de INSS no cadastro de Seção' esteja marcado em 'Parametrizador | Folha Normal | Encargos Sociais

Com este parâmetro marcado o campo porcentagem ficará desabilitado sendo considerado os percentuais para Empresa, Acidente de trabalho e Terceiros da seção centralizadora conforme cadastrado em Seções | Anexo | Histórico de Percentuais para INSS da seção centralizadora, com vigência na competência informada no processo de geração do encargo. 

Caso o parâmetro 'Descriminar percentual de terceiros' esteja marcado em 'Parametrizador | Folha Normal | Encargos Sociais, será calculado a parte de terceiros considerando cada percentual informado no anexo do histórico de percentuais de INSS

Caso o parâmetro 'Utiliza quebra de FPAS esteja marcado em Parametrizador | eSocial | Configurações Gerais | Lotação Tributária, o encargo irá buscar os percentuais do histórico de acordo com a quebra informada. Caso não encontre registro na seção conforme a quebra, será considerado da seção centralizadora do Colaborador

Para o cálculo de acidente de trabalho será considerado o cadastro de FAP por estabelecimento da Seção centralizadora disponível em Seção | Anexos | FAP por estabelecimento Empresarial dentro da vigência da competência de geração do encargo. Caso não encontre cadastro dentro da vigência, será buscado o valor da tabela de valores fixos. Se também não encontrar registro dentro da vigência, será retornado zero

Para os encargos do tipo T e U o parâmetro 'Aplicar percentual FAP por filial' sempre ficará desabilitado. A utilização da alíquota FAP só será aplicada quando o parâmetro 'Considerar os históricos de percentuais de INSS' estiver marcado, dentro das regras exemplificada acima.

Mais informações: [FAQ - Encargos Base de INSS e Base de INSS 13º Conforme DCTFWeb](https://tdn.totvs.com/pages/viewpage.action?pageId=866529609)  
   
**Considerar Percentual Redução (Lei 12.546/2011)**

O parâmetro 'Considerar Percentual de Redução (Lei 12.546/2011)' só será exibido nos cadastros de encargos do Tipo T e U e só será permitido marcar o mesmo caso no cadastro de Informações do Empregador em eSocial | Cadastros, o indicativo de desoneração da Folha seja **1 - Empresa enquadrada nos critérios da legislação vigente** ou **2 - Município enquadrado nos critérios da legislação vigente**.

O percentual de redução será retornado o valor do campo 'Percentual de Redução (Lei 12.546/2011)' do cadastro de Período de apuração do eSocial da competência da geração. No caso do 13º Salário, só será verificado o Indicativo de período apuração como anual na competência 12

Mais informações: [FAQ - Encargos Base de INSS e Base de INSS 13º Conforme DCTFWeb](https://tdn.totvs.com/pages/viewpage.action?pageId=866529609)

**Calcular reoneração gradual da folha**

O parâmetro **'Reoneração Gradual da Folha'** será exibido apenas nos cadastros de encargos do tipo **T, 3, 6 e R** e só poderá ser habilitado caso, no cadastro de **Informações do Empregador** em **eSocial | Cadastros**, o indicativo de desoneração da folha (campo **INDDESFOLHA**) esteja configurado como:

* **1** - Empresa enquadrada nos critérios da legislação vigente;
* **2** - Município enquadrado nos critérios da legislação vigente.

Quando habilitado, o cálculo do encargo será realizado conforme o valor do campo **Indicativo de Substituição Patronal (INDSUBSPATRONAL)** no cadastro de **PESOCIALFOLHAMENSAL** da competência correspondente

Importante

Caso utilize o indicativo de substituição patronal integral em conjunto com o percentual redutor no cadastro de encargo, o valor do calculo será igual a 0 (zero).

Para encargos do tipo **T**, caso esteja configurado para considerar o histórico de percentual de INSS, o sistema retornará o valor do campo **PERCENTEMPRESA** na tabela **PSECAODADOSINSS**, referente à competência da geração.

**Rateio que o Encargo Segue**

Deve ser informado neste campo o código do rateio definido em Administração Pessoal | Eventos | Rateio de evento. O Encargo com informação de rateio que o encargo segue não seguirá o Rateio Fixo definido no cadastro de funcionários e sim, seguirá ocorrência dos eventos que foram cadastrados no Rateio por Evento para que ele seja calculado. Ele só seguirá o Rateio Fixo definido no cadastro de funcionários, se os eventos cadastrados no Rateio por Evento não existirem na movimentação do funcionário. O código do rateio é definido no cadastro de Rateio de Eventos.  
   
Preenchendo o campo "Rateio que o Encargo segue" será obrigatório preencher também o "Período para Cálculo de Rateio" com um dos os seguintes períodos:  
**1 – Mês Atual -** Rateia conforme os rateios fixos informados no cadastro do funcionário.  
**2 – Período Aquisitivo –** Rateia conforme os rateios realizados durante o período aquisitivo de Férias.  
**3 – Ano de Competência –** Rateia conforme os rateios realizados durante o ano de competência atual.  
**4 - Mês Anterior –** Rateia de acordo com o rateio por centro de custo utilizado no mês anterior, tomando como base, a ficha financeira por centro de curto. Quando essa movimentação não existir o sistema deverá buscar o centro de custo do "Rateio Fixo" do funcionário.  
   
**Incide no Custo do Funcionário**

Farão parte do cálculo das horas pagas ao funcionário os eventos e os encargos que tiverem esse parâmetro marcado, caso contrário ele não fará parte do cálculo de horas pagas para o funcionário.

Este parâmetro é utilizado para integração do TOTVS Folha de Pagamento e TOTVS Automação de Ponto com o TOP (TOTVS Obras e Projetos)

**Considerar rateio fixo quando eventos do rateio que segue for zero**

Este parâmetro só ficará habilitado quando o cadastro de encargos estiver informado rateio que o Encargo segue.

Quando marcado irá considerar o rateio fixo do funcionário caso exista evento que compõe rateio lançado na ficha financeira com valor zerado. Se existir pelo menos um evento que compõe rateio com valor maior que zero, independe do parâmetro será feito o rateio do encargo.

Quando desmarcado não irá fazer rateio de encargo, caso exista evento que compõe rateio lançado na ficha financeira com valor zerado. Se existir pelo menos um evento que compõe rateio com valor maior que zero, independe do parâmetro será feito o rateio do encargo.

## **04. TABELAS UTILIZADAS**

PENCARGO

PTPENCARGO

## **05. ASSUNTOS RELACIONADOS**

Dados Contábeis do Encargo

Códigos Ativos do Encargo

[Roteiro para contabilizar os encargos utilizando o parâmetro "Considera Centro de Custo da Seção Anterior"](http://totvsconnect.blogspot.com/2011/10/como-fazer-roteiro-para-contabilizar-os)
