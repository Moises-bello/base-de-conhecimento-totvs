---
content_hash: 7404998df1646529b05be4d61d805f0bc910472fa2c24299bb22ade2272aba4e
fetched_at: '2026-06-29T00:10:37.001647+00:00'
page_id: '533740337'
product: rm
source: tdn-rm
title: MP 905/2019 - Encargos Sociais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=533740337
version: 58
---

As contratações na modalidade do Contrato de Trabalho Verde e Amarelo terão como salário-base mensal de até um salário-mínimo e meio nacional, e ficam garantidos os direitos determinados na CLT e/ou convenção coletiva.

**ALTERAÇÃO PARA A EMPRESA**

### **INSS**

Ficam isentas das seguintes parcelas incidentes sobre a folha de pagamentos dos contratados na modalidade Contrato de Trabalho Verde e Amarelo, limitado ao salário-base mensal de até um salário-mínimo e meio nacional:

* I – 20% contribuição previdenciária patronal
* II – Salário-educação
* III – Contribuição social destinada ao:

a) Serviço Social da Indústria – Sesi

b) Serviço Social do Comércio – Sesc

c) Serviço Social do Transporte – Sest

d) Serviço Nacional de Aprendizagem Industrial – Senai

e) Serviço Nacional de Aprendizagem Comercial – Senac

f) Serviço Nacional de Aprendizagem do Transporte – Senat

g) Serviço Brasileiro de Apoio às Micro e Pequenas Empresas – Sebrae

h) Instituto Nacional de Colonização e Reforma Agrária – Incra

i) Serviço Nacional de Aprendizagem Rural – Senar

j) Serviço Nacional de Aprendizagem do Cooperativismo – Sescoop

Atenção

As empresas terão isenção de contribuição patronal do INSS de 20% e das alíquotas do Sistema S e do Salário Educação, sobre o remuneração base de até um salário e meio, devendo recolher a contribuição nos casos que ocorrer excedentes como horas extras, periculosidade e etc.

A isenção da Contribuição Patronal não se estende ao RAT (Riscos Ambientais do Trabalho).

### **FGTS**

No caso do FGTS, as empresas contratantes ganharão desconto na hora de recolher o dinheiro para o fundo. Ao invés de realizarem o pagamento de 8% da alíquota em cima do salário do trabalhador, a taxa cairá para 2% com esse tipo de contrato.

### **ALTERAÇÃO NO PRODUTO TOTVS FOLHA DE PAGAMENTO**

Para atender as normas estabelecidas acima, foram necessárias adequações em algumas rotinas. Orientamos ao usuário a proceder conforme documentado abaixo:

# **FGTS**

***SEFIP***

Foi publicada a Circular Caixa nº 888 em 07 de Janeiro de 2020, com orientações para o trabalhador Contrato Verde e Amarelo, sendo estabelecido que:

* A categoria do trabalhador que deve ser informada é a 07, sendo que a mesma teve seu nome alterado para Aprendiz - Lei n°10.097/2000 - Contrato Verde/Amarelo MP905.
* Incluída a movimentação do trabalhador X1 - Trabalhador com contrato Verde e Amarelo, que deve ser utilizado exclusivamente para empregados com contrato Verde Amarelo com admissão a partir de 01/01/2019, devendo ser informado pelo empregador em todos os recolhimentos indicando, como data de movimentação a data da admissão do trabalhador.

O processo da Geração da SEFIP foi adequado para atender a regra estabelecida pela Circular nº 888. Para que seja enviado o Código de Categoria e a movimentação do trabalhador é necessário que o vínculo de Contrato Verde e Amarelo tenha as informações do Código de Categoria e Tipo de Funcionário conforme orientado no link .

*Exemplo*

Funcionário com contrato verde Amarelo admitido em 06/01, com salário mensal de R$1200,00, teve as seguintes verbas incidentes em FGTS:

No programa SEFIP 8.4 é possível verificar a Base de Cálculo e o Código de Movimentação do trabalhador:

  

E será calculado o recolhimento do FGTS considerando a alíquota de 2% sobre a base informada:

***Folha Analítica***

Para facilitar a conferência dos valores referente ao FGTS, no Relatório da Folha Analítica foi criado os campos abaixo que discriminam as bases de FGTS e o valor do FGTS devido ao Vínculo de Contrato Verde e Amarelo.

* Base FGTS Verde e Amarelo: Retorna o valor da Base de Cálculo do Vínculo Verde e Amarelo somando as verbas que incidem em FGTS de Folha e subtraindo os eventos que estornam FGTS de Folha.
* FGTS Verde e Amarelo: Retorna o valor do campo 'Base FGTS Verde Amarelo' multiplicado pela alíquota de 2%

Exemplo: Funcionário com eventos de Base de FGTS de R$ 1.825,00.

No campo Base FGTS Verde e Amarelo retornou o valor de 1.825,00.

No campo FGTS Verde e Amarelo calculou o valor do FGTS considerando a base acima: 1.825,00 x 2% =  36,50

* Base FGTS 13º Verde/Amar.: Retorna o valor da Base de Cálculo do Vínculo Verde e Amarelo somando as verbas que incidem em FGTS de 13º Salário e subtraindo os eventos que estornam FGTS de 13º Salário.
* FGTS 13º Verde e Amarelo: Retorna o valor do campo 'Base FGTS 13º Verde/Amar.' multiplicado pela alíquota de 2%.

Exemplo: Funcionário com eventos de Base de FGTS de R$ 125,00.

No campo Base FGTS 13º Verde/Amar. retornou o valor de 125,00.

No campo FGTS 13º Verde e Amarelo calculou o valor do FGTS considerando a base acima: 125,00 x 2% =  2,50

* Base FGTS Ant. Verde/Amar.: Retorna o valor do Campo FGTS Verde e Amarelo do Vínculo Verde e Amarelo como base de cálculo da antecipação da multa rescisória paga junto com a remuneração Mensal.
* FGTS Ant. Verde e Amarelo: Retorna o valor do campo Base FGTS Ant. Verde/Amar. multiplicado pela alíquota da multa rescisória de 20%.

Exemplo: Funcionário com eventos de Base de FGTS de R$ 1.825,00 e FGTS Verde e Amarelo de 36,50.

No campo Base FGTS Ant. Verde/Amar. retornou o valor de 36,50.

No campo FGTS Ant. Verde e Amarelo calculou o valor da antecipação da multa considerando a base acima: 36,50 x 20% =  7,30

* Base FGTS 13º Ant. Verd.Am.: Retorna o valor do Campo FGTS 13º Verde e Amarelo do Vínculo Verde e Amarelo como base de cálculo da antecipação da multa rescisória paga junto com a remuneração Mensal.
* FGTS 13º Ant. Verde/Amar.: Retorna o valor do campo Base FGTS 13º Ant. Verd.Am. multiplicado pela alíquota da multa rescisória de 20%.

Exemplo: Funcionário com eventos de Base de FGTS de R$ 1.825,00 e FGTS 13º Verde e Amarelo de 2,50.

No campo Base Base FGTS 13º Ant. Verd.Am. retornou o valor de 2,50.

No campo FGTS 13º Ant. Verde/Amar. calculou o valor da antecipação da multa considerando a base acima: 2,50 x 20% =  0,50

Antecipação de Multa Rescisória

Os campos 'Base FGTS Ant. Verde/Amar.' e 'Base FGTS 13º Ant. Verd.Am.' considera se o campo Código da Categoria eSocial é 108 - 'Empregado - Contrato de trabalho Verde e Amarelo - com acordo para antecipação mensal da multa rescisória do FGTS' para serem preenchidos.

# **INSS**

***Guia de INSS***

Para a Geração da Guia de INSS foi criado o campo 'Ded. Base Verde Amarelo', que retorna a soma da base dos valores deduzidos de cada vínculo verde Amarelo, limitado ao teto de 1,5 Salário. O valor retornado no campo 'Ded. Base Verde Amarelo' é deduzido da Base de INSS para o cálculo de Terceiros e Empresa.

Acidente de Trabalho

Para o cálculo de acidente de trabalho é considerado o valor da Base INSS sem deduzir o valor do campo Ded. base Verde Amarelo.

*Exemplos*

* Funcionário com contrato Verde Amarelo com Base INSS no valor de R$ 1.240,00. Ao gerar a Guia de INSS foi retornado no campo Base INSS o valor de 1.240,00 e no campo Ded. Base Verde Amarelo também 1.240,00, pois a base do funcionário é menor que um salário mínimo e meio.

Para o cálculo de Terceiros, o processo executa o seguinte cálculo: (Base INSS - Ded. Base Verde Amarelo ) x %Terceiros = (1.240,00 - 1.240,00) x 5,8% = 0

Para o cálculo de Acidente Trabalho, o processo executa o seguinte cálculo: Base INSS x %Acid. Trabalho = 1.240,00 x 3% = 37,20

Para o cálculo Empresa, o processo executa o seguinte cálculo: (Base INSS - Ded. Base Verde Amarelo ) x %Empresa  = (1.240,00 - 1.240,00) x 20% = 0

* Funcionário com Contrato Verde Amarelo com Base de INSS no valor de 1.650,00. No campo Base INSS retornou o valor de 1.650,00. No campo Ded. Base verde Amarelo retornou o valor de 1.567,50, pois é o Teto limite de um salário mínimo e meio para a isenção do encargo.

Para o cálculo de Terceiros, o processo executa o seguinte cálculo: (Base INSS - Ded. Base Verde Amarelo ) x %Terceiros = (1.650,00 - 1.567,50) x 5,8% = 4,78

Para o cálculo de Acidente Trabalho, o processo executa o seguinte cálculo: Base INSS x %Acid. Trabalho = 1.650,00 x 3% = 49,50

Para o cálculo Empresa, o processo executa o seguinte cálculo: (Base INSS - Ded. Base Verde Amarelo ) x %Empresa  = (1.650,00- 1.567,50) x 20% = 16,50

* Três Funcionários, sendo:
  + Um Contrato Verde Amarelo com Base INSS no valor de 1.240,00
  + Um Contrato Verde Amarelo com Base INSS no valor de 1.650,00
  + Um Contrato Normal com Base INSS no valor de 2.390,29

Ao Gerar a Guia de INSS, retornou  para o campo Base INSS o valor de 5.280,29 e para o campo Ded. Base Verde Amarelo o valor de 2.807,50 que é soma da parte dedutível de cada vínculo verde e amarelo, respeitando o teto de até um salário mínimo e meio.

Para o cálculo de Terceiros, o processo executa o seguinte cálculo: (Base INSS - Ded. Base Verde Amarelo ) x %Terceiros = (5.280,29 - 2.807,50) x 5,8% = 143,42

Para o cálculo de Acidente Trabalho, o processo executa o seguinte cálculo: Base INSS x %Acid. Trabalho = 5,280,29 x 3% = 158,40

Para o cálculo Empresa, o processo executa o seguinte cálculo: (Base INSS - Ded. Base Verde Amarelo ) x %Empresa  = (5.280,29 - 2,807,50) x 20% = 494,55

***Encargos***

Para Geração de Encargos, foi disponibilizado o parâmetro 'Deduz Verde Amarelo', no cadastro do encargo. Com este parâmetro marcado irá deduzir de até um salário mínimo e meio da Base de INSS remunerada do Vínculo de contrato Verde e Amarelo no cálculo de INSS Empresa.

Atenção

* Este parâmetro só ficará habilitado para os tipos de encargos 3 - Base: incidência de INSS.
* É necessário executar o RM.Atualizador.exe para que o campo seja criado.

*Exemplos*

* Funcionário com contrato Verde Amarelo com Base de INSS no valor de R$ 1.353,34. Ao gerar o encargo irá retornar zero. Neste caso o sistema valida se o base de INSS é menor que o valor de um Salário Mínimo e Meio e caso positivo retorna 0 (zero) para base de INSS:

* Funcionário com contrato Verde Amarelo com Base de INSS no valor de R$ 1.803,34. Ao gerar o encargo irá subtrair da Base INSS o valor de um Salário Mínimo e Meio e tributar no resultado a alíquota informado no cadastro do encargo:

Encargo Gerado:

* Dois funcionários, sendo:
  + Contrato Verde Amarelo com Base de INSS de R$ 1.353,34
  + Contrato Normal com Base de INSS de R$ 1.536,00

Ao gerar o encargo foi deduzido o valor de até um salário Mínimo e Meio do vínculo Verde e Amarelo. Do funcionário normal não foi feito nenhuma dedução

* Gerando encargo para um funcionário de Vínculo Verde e Amarelo com o parâmetro desmarcado. Calculou a alíquota informada sem fazer dedução:

Os exemplos acima foram feitos considerando somente o 20% de contribuição previdenciária patronal. A mesma configuração deve ser feita para o cálculo do encargo de Terceiros. Porém para o cálculo do encargo do RAT orientamos a não usar o parâmetro visto que segundo o entediamento da MP e o retorno no xml de fechamento (S-5011), o código de receita 1646-01 CP PATRONAL - GILRAT AJUSTADO é sempre calculado para toda base de INSS do Vínculo Verde Amarelo.

***Folha Analítica***

Para facilitar a conferência dos valores referente ao INSS, no Relatório da Folha Analítica foi criado os campos abaixo que discriminam as bases dedutível de INSS do vinculo Verde Amarelo, limitado ao teto de 1,5 Salário. Com isto foi ajustando os cálculos de INSS Empresa e Terceiros considerando a dedução prevista na MP 905.

* Ded. Base INSS Verde/Amar.: Este campo retorna a base dedutível de INSS do funcionário de Contrato Verde e Amarelo, abatendo o valor da Base INSS - GPS para o cálculo de INSS Empresa e INSS Terceiro:
* Ded. Base INSS 13º Ver.Ama.: Este campo retorna a base dedutível de INSS 13º Salário do funcionário de Contrato Verde e Amarelo, abatendo o valor da Base INSS 13º - GPS para o cálculo de INSS Empresa e INSS Terceiro:

Exemplo: Funcionário com Base INSS: 1. 825,00 e Base INSS 13º: 125,00

No campo Base INSS - GPS retornará 1.825,00

No campo Base INSS 13º - GPS retornará: 125,00

No campo Ded. Base INSS Verde/Amar. retornará 1567,50

No campo Ded. Base INSS 13º Verde/Amar. retornará 125,00

O cálculo de INSS Empresa irá proceder da seguinte forma: (('Base INSS - GPS' - 'Ded. Base INSS Verde/Amar.') + ('Base INSS 13º - GPS' - 'Ded. Base INSS 13º Verde/Amar.')) x %Empresa  = ((1.825,00 - 1567,50) + (125,00 - 125,00)) x 20% = 51,50

O cálculo de INSS SAT irá proceder da seguinte forma: ('Base INSS - GPS' + 'Base INSS 13º - GPS')  x %Acid. Trabalho = 1.825,00 x 3% = 58,50

O cálculo de INSS Terceiro irá proceder da seguinte forma: (('Base INSS - GPS' - 'Ded. Base INSS Verde/Amar.') + ('Base INSS 13º - GPS' - 'Ded. Base INSS 13º Verde/Amar.')) x %Terceiros = ((1.825,00 - 1567,50) + (125,00 - 125,00)) x 5,8% =14,94

Observação

Para fazer a dedução do teto de até um Salário Mínimo e meio sobre a Base de INSS do Vínculo de Contrato Verde e Amarelo, é verificado se o Campo Código da Categoria eSocial do Cadastro do Funcionário é 107 ou 108 e o Teto considerado para fazer a dedução é o valor cadastrado na Tabela de Valores Fixos de Finalidade 'Valor do Salário Mínimo", acrescentado de 50%.
