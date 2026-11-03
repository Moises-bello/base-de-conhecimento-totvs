---
content_hash: f7804ec6145775c81c03aece4ba89c4038be714a35137c81fac79cf38eab4188
fetched_at: '2026-06-29T00:09:54.796343+00:00'
page_id: '445647302'
product: rm
source: tdn-rm
title: Aba Valores
type: documentation
url: https://tdn.totvs.com/display/LRM/Aba+Valores
version: 50
---

As informações sobre os valores do lançamento financeiro são divididas em quatro grupos:

Valores Gerais

Nesta aba são apresentadas informações sobre valores gerais do Lançamento Financeiro.

Campos de Fórmulas

Os campos de fórmulas só estarão disponíveis se o parâmetro "Usar Fórmulas para Valores" (Assistente de Implantação de Processos | etapa Recursos Adicionais do Lançamento Financeiro) estiver marcado.

Valor Original

Informe o valor do lançamento.  
Depois de ter cadastrado dados na pasta Rateios, sempre que for alterado o "Valor Original", o sistema apresenta uma confirmação de recálculo dos rateios do lançamento.  
Ao alterar o "Valor Original" o Valor do Serviço é atualizado automaticamente.

Valor Indexado

Neste campo poderá ser informada uma moeda que indexará o lançamento no momento da Baixa.  
Cálculo da Indexação Valor em Real dividido pelo valor da moeda indexadora na inclusão do lançamento vezes valor da moeda indexadora na baixa do lançamento.

Valor Baixado

Será preenchido pelo sistema durante o processo de baixa do lançamento.

Valor Desconto

Informe um valor fixo, um percentual ou uma fórmula.  
Ao informar um percentual, o valor de desconto é calculado automaticamente.  
Não é possível utilizar um valor fixo e uma fórmula ao mesmo tempo.

Juros

Informe um valor fixo, um percentual ou uma fórmula.  
Ao informar um percentual, o valor de juros é calculado automaticamente.  
Não é possível utilizar um valor fixo e uma fórmula ao mesmo tempo.  
Este campo só estará disponível para edição se o campo "Juros ao Dia" estiver com o valor "0,00".

Juros ao Dia

Através deste campo você pode definir uma "Taxa" ou um "Valor" de juros ao dia.  
Taxa (%) - O valor informado no campo é considerado como percentual.  
Este campo só estará disponível para edição se o campo "Juros" estiver com o valor "0,00".  
Ao incluir um lançamento e informar no campo "Juros ao dia %" um determinado valor, é possível determinar que aqueles juros sejam default para todos os lançamentos. Para isso, basta clicar no campo com o botão direito do mouse e selecionar "Valor Default".

**Observação**

Os campos de Juros acima citados devem ser utilizados para inserir os Juros de Mora dos lançamentos financeiros.

Carência Juros

Informe neste campo a quantidade de dias de carência para o cálculo dos juros ao dia.  
Os juros serão cobrados se a quantidade de dias de atraso for superior à quantidade de dias de carência.  
Caso a carência termine em um final de semana ou feriado, o próximo dia útil será considerado como a data final da carência, e não serão cobrados juros nesta data.  
A quantidade de dias para o cálculo dos juros será definida de acordo com o parâmetro "Considerar os dias de carência no cálculo dos juros ao dia" (Assistente de Implantação de Processos | processo Baixa | etapa Valor Líquido do Lançamento Financeiro).

Multa

Informe um valor fixo ou um percentual ou uma fórmula.  
Ao informar um percentual o valor de multa é calculado automaticamente.  
Não é possível utilizar um valor fixo e uma fórmula ao mesmo tempo.  
Este campo só estará disponível para edição se o campo "Multa ao Dia %" estiver com o valor "0,00".

Multa ao dia %

Informe um percentual de multa ao dia de atraso.  
Esse percentual será acrescido ao "Valor Líquido Parcial" ou ao "Valor Original" do lançamento, dependendo de como foi definido o parâmetro "Calcula Multa ao Dia" usando (Assistente de Implantação de Processos | processo Baixa | etapa Valor Líquido do Lançamento Financeiro).  
Este campo só estará disponível para edição se o campo "Multa" estiver com o valor "0,00".

Capitalização

Informe um valor fixo, um percentual ou uma fórmula.  
Ao informar um percentual, o valor de capitalização é calculado automaticamente.  
Não é possível utilizar um valor fixo e uma fórmula ao mesmo tempo.  
Este campo só estará disponível para edição se o campo "Capitalização Mensal %" estiver com o valor "0,00".

Capitalização Mensal %

Informe o percentual de capitalização mensal do lançamento.  
O cálculo da capitalização será feito a partir do percentual informado neste campo e o valor do lançamento será capitalizado pelo período compreendido entre a data de emissão e a data da baixa do lançamento.  
Caso o lançamento não possua um Valor de Capitalização, o sistema irá basear-se no valor informado na Capitalização Mensal, informado através de um percentual (%).  
Este campo só estará disponível para edição se o campo "Capitalização" estiver com o valor "0,00".

Convênio

Caso esteja parametrizada a "Contabilização de Mútuo" disponível em Integração Contábil | Contabilização, para lançamentos a pagar em conta caixa global com tipo contábil diferente de "Não contábil", poderá ser feita uma remessa para um convênio de outra coligada onde será feito o pagamento propriamente dito. Assim, na pesquisa desse campo também serão exibidos convênios da coligada proprietária da conta caixa.

Valor Líquido

O Valor Líquido pode ser calculado de acordo com a data informada no campo 'Data valor líquido' pela visão de lançamentos ou pelo lançamento na aba Valores / Gerais. Como default a data preenchida será sempre a data atual do sistema.  
Para que o valor líquido seja calculado e este campo seja preenchido é necessário "Salvar" a edição do lançamento e utilizar o botão "Calcular o Valor Líquido".  
Utilizando o botão "Exibir Cálculo do Valor Líquido" é possível verificar os valores que compõem o Valor Líquido na data desejada.

**Observações:**

* Serão exibido os valores calculados de acordo com a data informada no campo Data Valor Líquido, sendo que para esse cálculo serão usados os dados atuais do lançamento.
* A data informada manualmente para o cálculo não fica salva e retorna à data atual do sistema ao fechar o lançamento e a visão de lançamentos.
* Os valores opcionais negativos gerados pelo aplicativo RM SGI são utilizados para compor o valor líquido.
Valores Adicionais

Nesta pasta são apresentadas informações sobre Valores Opcionais, Cheques, Vínculos e Empréstimo Vendor.

A apresentação e funcionalidade dos valores opcionais serão de acordo com os parâmetros de Valores Opcionais (Assistente de Implantação de Processos | etapa Valores Opcionais do Lançamento Financeiro).

* Informe um valor fixo, um percentual ou uma fórmula.
* Ao informar um percentual, o valor é calculado automaticamente.
* Não é possível utilizar um valor fixo e uma fórmula ao mesmo tempo.

**Observação:**

Para lançamentos gerados pelo aplicativo RM SGI são aceitos valores opcionais negativos.

Campos de Fórmulas

Os campos de fórmulas só estarão disponíveis se o parâmetro "Usar Fórmulas para Valores" (Assistente de Implantação de Processos | etapa Recursos Adicionais do Lançamento Financeiro) estiver marcado.

Vínculos – Adiantamento

Esse campo é preenchido automaticamente com o valor vinculado.

Vínculos – Devolução

Esse campo é preenchido automaticamente com o valor vinculado.

* No lançamento que possui Tipo de Documento "Sem Classificação", é apresentado o valor que foi vinculado a ele.
* No lançamento que possui Tipo de Documento "Devolução", não é informado nenhum valor.
* Ao baixar o lançamento, este valor será deduzido do Valor Original.

Vínculos – Nota de Crédito

Esse campo é preenchido automaticamente com o valor vinculado.

* No lançamento que possui Tipo de Documento "Sem Classificação", não é informado nenhum valor.
* No lançamento que possui Tipo de Documento "Nota de Crédito", é apresentado o valor que foi vinculado a ele.
* Ao baixar o lançamento de Nota de Crédito, este valor será deduzido do Valor Original.
* Após a baixa, esse campo é preenchido no lançamento que possui Tipo de Documento "Sem Classificação".

Vendor – Taxa

Corresponde a taxa que será utilizada no cálculo dos juros pró-rata mês – exclusiva para empréstimo Vendor.

Vendor – Juros

Corresponde ao valor total dos juros cobrados pelo Banco, no ato da contratação do empréstimo.

Ajuste Financeiro

Este campo é preenchido automaticamente pelo sistema após a execução do processo de "Baixa por Distrato / Perda Financeira", com o valor líquido do lançamento no momento da baixa.

Valores Tributos

Nesta pasta são apresentadas informações sobre valores de Tributos do lançamento financeiro.  
Esta pasta é apresentada apenas nas seguintes situações:

* Lançamento a Pagar – Pessoa Jurídica
* Lançamento a Pagar – Ambos – Pessoa Jurídica
* Lançamento a Pagar – Pessoa Física – Tipo de Documento com a Classificação "Gera INSS"
* Lançamento a Pagar – Pessoa Física – Tipo de Documento com a Classificação "Gera IRRF"
* Lançamento a Pagar – Pessoa Física – Tipo de Documento com a Classificação "Gera IRRF e INSS"
* Lançamento a Pagar – Pessoa Física – Tipo de Documento com a Classificação "Gera IRRF-PF Aliquota Fixa"
* Lançamento a Receber – Pessoa Jurídica
* Lançamento a Receber – Ambos – Pessoa Jurídica

Valor do Serviço

Este valor é apresentado automaticamente. Se for lançamento incluído no sistema de Gestão Financeira, é apresentado o mesmo valor do Valor Original. Se for lançamento gerado por outro sistema, é apresentado o valor de "Serviço" informado pelo sistema. Se o sistema não enviar este valor, o campo é preenchido com o mesmo valor do Valor Original.  
O valor informado neste campo será utilizado para o cálculo do "Valor Base" para os cálculos de INSS e de IRRF.  
Ao alterar o valor do campo "Valor Original" o "Valor do Serviço" é atualizado automaticamente.

Valor do IRRF

O campo do valor e os botões de IRRF estarão disponíveis na seguinte situação:

* Lançamento = "A Pagar";
* Cliente/Fornecedor = Classificação "Fornecedor" ou "Ambos";
* Tipo de Documento = Classificação "Gera IRRF" ou "Gera IRRF e INSS".
* Campo Valor:  O campo valor é preenchido automaticamente ao utilizar o botão "Calcular Valor do IRRF".

Nos dados do IRRF existe o campo "Natureza de rendimentos" para informar esta classificação para geração de rotinas do Fiscal. O default será carregado do cliente/fornecedor. Caso a natureza de rendimentos informada marcada como "Rendimentos Isentos ou Não tributáveis", o valor do IRRF será zerado gerando apenas a base de cálculo. Para mais informações, veja .

O processo de [Alteração da Natureza de Rendimentos](https://tdn.totvs.com/x/txdZLw), permite alterar a natureza de rendimentos do IRRF já cadastrada nos lançamentos financeiros.

**LEGISLAÇÃO IRRF – Isenção de Dividendos (Lei 15.270/2025)**

Por ocasião da Lei 15.270/2025, o cálculo do IRRF para pagamentos de dividendos a pessoas físicas passou a considerar uma faixa de isenção mensal, na qual o imposto somente será retido quando o montante acumulado no mês ultrapassar o limite definido.

### Cálculo do IRRF sobre Dividendo

Segundo a legislação:

* Não há retenção de IRRF enquanto o total de dividendos no mês for **menor ou igual ao limite de isenção.**
* Ao ultrapassar o limite:
  + O IRRF é calculado sobre o **total acumulado** no mês;
  + O sistema retém apenas o valor **incremental (diferença)** no lançamento que ultrapassou;

### Exemplo prático:

| Lançamento | Valor | Acumulado | IRRF |
| --- | --- | --- | --- |
| 1º | 5.000 | 5.000 | 0 |
| 2º | 45.000 | 50.000 | 0 |
| 3º | 10.000 | 60.000 | 6.000 |

### Parâmetro de Configuração

Para atender a esta regra, foi criado um novo parâmetro no sistema na aba Financeiro > Contas a Pagar > Calculo de Tributos > Geração IRRF PF

**Nome:** Limite de Isenção IRRF PF (Lei 15.270)

### 

### Tipos de Lançamentos Tributáveis

* A regra será aplicada apenas para lançamentos que atendam aos seguintes critérios:
* Cliente/Fornecedor: Pessoa Física
* Tipo de Documento: Classificação "Gera IRRF PF Alíquota Fixa"
* Código de Receita no Lançamento: Dividendos (1841)
* Tipo de Lançamento: A Pagar

### Regra de Competência (Cumulatividade)

O cálculo considera a **competência mensal**, conforme parâmetro de geração de IRRF: Emissão/Vencimento/Baixa/Contabilização

O sistema utiliza a data configurada para:

* Agrupar os lançamentos no mês;
* Calcular o acumulado da base de IRRF

**LEGISLAÇÃO IRRF - atendimento à medida provisória 1.171/2023**

Por ocasião desta lei, o cálculo do IRPF passou a ser calculado pelo módulo TOTVS Folha de Pagamento, considerando o que for mais benéfico ao contribuinte: o cálculo de IRPF pelo modelo simplificado ou completo. 

* Veja mais informações nos links abaixo:

[http://www.planalto.gov.br/ccivil\_03/\_ato2023-2026/2023/Mpv/mpv1171.htm](http://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/Mpv/mpv1171.htm "Follow link")

* Documentação da configuração e cálculo do IRRF simplificado:

<https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/>

* Segundo a legislação, o fornecedor pode optar que o cálculo não utilize o modelo de desconto simplificado. Para atender a este caso, será necessária a seguinte configuração:
  + Criar um campo complementar para a entidade Clientes/Fornecedores com nome da coluna **NAOUSARCALCSIMPIRPF**, tipo do campo *Texto*. Para a descrição sugerimos "Não usar cálculo simplificado para IRPF (MP 1.171/2023)".
  + No cadastro do fornecedor, o novo campo será exibido na aba Campos Complementares. Quando o valor contiver o texto **NUNCA,** o cálculo será sempre pela dedução legal (modelo anterior) e não considera o cálculo com dedução simplificada. Caso necessite configurar este mesmo comportamento somente para algumas operações, pelo código de receita, informe os mesmos neste mesmo campo separados por **; (ponto e vírgula)**. No exemplo "3208;9408" (não é necessário usar o caractere aspas), quando o código de receita no lançamento for um destes, o cálculo será pela dedução legal (modelo anterior) e não considera o cálculo com dedução simplificada.
  + Campo complementar não criado, sem valor ou com valor inválido, o cálculo irá considerar a regra nova com dedução legal. Caso o valor do campo contenha códigos de receita e o texto NUNCA, este sempre prevalecerá.

Valor das Retenções

O campo do valor e os botões de Retenções estarão disponíveis na seguinte situação:

* Lançamento = "A Pagar" ou "A Receber";
* Cliente/Fornecedor = Categoria "Pessoa Jurídica".

O campo valor é preenchido automaticamente ao utilizar o botão "Calcular Valor das Retenções".  
Passa a ser permitido editar a base de retenção de tributos de lançamentos a receber, que estejam parcialmente baixados.

No cadastro das retenções existe o campo "Natureza de rendimentos" para informar esta classificação para geração de rotinas do Fiscal.

O processo de [Alteração da Natureza de Rendimentos](https://tdn.totvs.com/x/txdZLw), permite alterar naturezas de rendimentos já cadastradas nas retenções dos lançamentos financeiros.

Valor do INSS

O campo de valores e os botões de INSS estarão disponíveis na seguinte situação:

* Lançamento = A Pagar;
* Cliente/Fornecedor = Classificação "Fornecedor" ou "Ambos", Categoria "Pessoa Física";
* Tipo de Documento = Classificação "Gera INSS" ou "Gera IRRF e INSS";
* Campo Valor.  O campo valor é preenchido automaticamente ao utilizar o botão "Calcular Valor do INSS".

**LEGISLAÇÃO INSS - Realizar o cálculo do INSS apenas para o empregado com 20% quando o Cliente Fornecedor for "Sócio Cooperado".**

Legislação: em 26 de maio de 2015 a Receita Federal baixou por meio do ato declaratório interpretativo nº5 e publicado no “Diário Oficial da União” na mesma data, informando que o sócio cooperado será considerado contribuinte individual, devendo recolher 20% sobre o total da remuneração recebida pelos serviços prestados, respeitados os limites mínimo e máximo de contribuição”.

No sistema a parametrização para o cálculo do INSS no caso de sócio cooperado será através de campo complementar do cadastro de cliente/Fornecedor, para as versões 12.1.27 e 12.1.28.  A partir da versão 12.1.29 o campo oficial será apresentado no cadastro de Cliente Fornecedor.

Para que o sistema considere o valor do INSS do empregador como isento e trabalhe com a alíquota de 20% para o empregado, será preciso incluir esse campo complementar no cadastro e marcar a opção de uso do campo. Quando não marcado o campo complementar o comportamento do sistema será o atual, ou seja, será gerado INSS para o empregador e para o empregado. Conforme imagem acima, o campo complementar deverá ser cadastrado com o nome da coluna "SOCIOCOOPERADO" e com o Tipo do Campo igual a "LÓGICO", para que a opção seja disponibilizada para marcação no sistema. Já a partir da versão 12.1.29, foi criado o campo específico no cadastro do Cliente/Fornecedor para indicar se o mesmo é Sócio Cooperado.

O parâmetro por coligada "Entidade beneficente de assistência social isenta das contribuições patronais", deve estar desmarcado para que o sistema considere a marcação do campo complementar criado. Se o parâmetro já estiver marcado o sistema irá desconsiderar a parametrização do campo complementar, no caso de versões anteriores a 12.1.29, ou da opção no cadastro do cadastro do Cliente/Fornecedor nas versões mais recentes.

**PRODUTOR RURAL - Isenção da retenção dos 11% do INSS do Empregado**

Referente ao tratamento da isenção da retenção dos 11% do INSS do Empregado, no contexto do Contratante (tratado no sistema como Coligada) quando Produtor Rural Pessoa Física, basta indicar no cadastro da Coligada (localizada no módulo Serviços Globais) que o mesmo é "Produtor Rural" e inserir um CPF em seus respectivos campos.

**Contribuição previdenciária aplicada em regime de competência**

A IN vigente é a 971/09 que traz em seu **artigo 52** as regras para a retenção da contribuição previdenciária que, no caso do contribuinte individual, se dá no mês em que houver pagamento ou o credito da remuneração. Assim, para se chegar a base de cálculo do Imposto de Renda, o tomador de serviços deverá considerar apenas o valor efetivamente retido do INSS.

É importante ressaltar que a cumulatividade do INSS ocorre quando não há o atingimento do valor mínimo para o recolhimento do tributo (R$10,00). Se recebidas no mesmo mês, o valor acumula até que se atinja o montante superior ao mínimo para a retenção não ultrapassando o teto para recolhimento no mês.

Neste caso porém, os pagamentos são realizados em meses distintos pelo mesmo fornecedor e a data de vencimento é a mesma. Como a remuneração ocorre em meses distintos, o tomador de serviços deverá, em cada um dos meses que se fizer o pagamento ou credito do rendimento tributável, calcular a contribuição previdenciária a ser deduzida em cada mês.

Mais detalhes no documento abaixo:

[IRRF - Base de Cálculo X Dedução do INSS - Sem vínculo Empregatício](https://tdn.totvs.com/x/wgglJ)

SEST/SENAT

A alíquota desse tributo é de 2,50% e será calculado no sistema quando informado no cadastro do Cliente/Fornecedor a categoria do autônomo.

**MEDIDA\_PROVISÓRIA\_932/2020 - Governo reduz temporariamente as contribuições destinadas ao Sistema "S".**

A alíquota do tributo referente ao SEST/SENAT sofreu uma redução temporariamente devido ao COVID-19. A alíquota de 2,50% passa a ser de 1,25% e começa a valer a partir de **01/04/20** até **30/06/20.**

Para lançamentos inseridos no sistema dentro do período estipulado será aplicada a alíquota reduzida.

Mais informações acesse:

[http://www.in.gov.br/en/web/dou/-/medida-provisoria-n-932-de-31-de-marco-de-2020-250477890](http://www.in.gov.br/en/web/dou/-/medida-provisoria-n-932-de-31-de-marco-de-2020-250477890 "Follow link")

[https://www.totvs.com/blog/fiscal-clientes/mp-n-923-2020-reducao-da-contribuicao-ao-sistema-s/](https://www.totvs.com/blog/fiscal-clientes/mp-n-923-2020-reducao-da-contribuicao-ao-sistema-s/ "Follow link")

**Inclusão dos Tributos em Lançamentos Financeiros com Retenção Tributária**

Para o perfeito funcionamento da rotina de controle de Retenções Tributárias, é necessário seguir os passos informados no roteiro de Retenções Tributárias.  
Os tributos são incluídos no campo "Valor das Retenções" (pasta Valores | Tributos)

**LEI No 10.485, DE 3 DE JULHO DE 2002.**

Essa mesma lei foi alterada no que diz respeito a venda de produtos de autopeças e passam a ficar sujeitos à incidência de contribuição para o PIS/PASEP e COFINS.

As alíquotas são 0,1% de PIS e 0,5% de COFINS, sua apuração deverá ser quinzenal e o código da DARF para recolhimento deve ser 3770 para o PIS e 3746 para a COFINS.

O Totvs Gestão Financeira implementou o processo de cálculo de retenção de contribuições sociais (PIS-RF, COFINS-RF, CSLL-RF), conforme determinações prescritas na Lei 10.485.

No Contas a Pagar | Baixa |Retenção das Contribuições | Geração de Retenções foram implementados os seguintes parâmetros, por coligada:

Usar retenção de tributos conforme Lei 10.485  
No contexto da Lei 10.485, a cumulatividade de tributos deve ocorrer de forma diária, ou seja, se ao executar o pagamento o valor do tributo for inferior a R$ 10,00, a retenção não ocorre. Caso no mesmo dia ocorra algum outro pagamento para mesmo Fornecedor e somados, o valor do tributo acumulado e o respectivo valor do tributo do pagamento corrente, o valor for maior que R$ 10,00, o valor somado é então retido.

Usar cumulatividade conforme as Leis 10.485 e 13.137  
Usar cumulatividade diária para cálculo das retenções dos tributos  
Quando habilitado irá fazer a cumulatividade diária de acordo com as Leis 10.485 e 13.137.

**Tratamento das retenções**

O tratamento das retenções em lançamentos a receber, gerados pela emissão de notas fiscais pelo TOTVS Gestão de Estoque, Compras e Faturamento, deverão ser gerados indicando os tributos, com a alíquota correta, e código de receita indicado pela Lei. No Financeiro, estes dados ficam consolidados na tabela de retenções de tributos do lançamento, com efeito no valor líquido e na baixa apenas como um deduções. A exceção, por ora, seria para os tributos 'IBS' e 'CBS' que os valores que constar nessa guia serão apenas informativos e não serão considerados no valor líquido e no item de baixa do lançamento financeiro.

O tratamento das retenções em lançamentos a pagar, gerados pelo Financeiro, buscarão o padrão de impostos, alíquotas e códigos de receita que são definidos no fornecedor. No momento do cálculo do valor líquido é executado conforme os atributos definidos nos parâmetros. Os lançamentos dos tributos são gerados na data de vencimento indicado pelas Leis.

**Vencimentos dos tributos**

No contexto da Lei 13.113, a data de vencimentos dos tributos é o primeiro dia útil anterior ao vigésimo dia do próximo mês. Já no contexto da Lei 10.485 a data de vencimento dos lançamentos de tributos é definido por quinzena (se a data de vencimento é anterior ao dia 15 do mês, o vencimento do tributo é definido pelo dia útil anterior ao último dia do mês | se a data de vencimento é posterior ao dia 15 do mês, o vencimento do tributo é definido pelo dia útil anterior ao dia 15 do mês posterior).

**Código de Retenção 3770 e 3746 - Autopeças**

Para os códigos de retenção **3770 (PIS)** e **3746 (COFINS)**, referentes à aquisição de autopeças, o sistema aplica a **regra de vencimento quinzenal** independentemente da configuração do parâmetro **"Usar cumulatividade conforme as Leis 10.485 e 13.137"**.

Essa regra se mantém porque, conforme a **Lei nº 10.485/2002**, os títulos de PIS e COFINS gerados nessas operações devem ter o **vencimento no último dia da quinzena subsequente ao pagamento**, e o mesmo não foi revogado pela Lei 13.137.

**Código de Receita 8053 / Código de Receita 0916**

Quando o código da receita é 8053 (Pagamento de Rendimento de Mútuo) e 0916 (Pagamento de Premiações), a data de vencimento será o 3º dia útil subsequente ao decêndio da ocorrência do fato gerador (pessoa física), fundamentado pelas legislações indicadas abaixo:

* No **art. 930, inciso II, alínea "a"** do **Decreto nº 9.580/2018**
* E no **art. 70, inciso I.2, alínea “b”** da **Lei nº 11.196/2005**

**Decreto Nº 9.580, de 22 de novembro de 2018:**

*Art. 930. O recolhimento do imposto sobre a renda retido na fonte deverá ser efetuado (Lei nº 11.196, de 2005, art. 70, **caput,**  inciso I) :*  
*II - até o terceiro dia útil subsequente ao decêndio de ocorrência dos fatos geradores, na hipótese de:*  
*a) juros sobre o capital próprio e aplicações financeiras, inclusive aqueles atribuídos a residentes ou domiciliados no exterior, e títulos de capitalização;*

***Lei 11.196/2005, artigo 70, item b:***

***b)** até o 3o (terceiro) dia útil subsequente ao decêndio de ocorrência dos fatos geradores, no caso de:  
1. juros sobre o capital próprio e aplicações financeiras, inclusive os atribuídos a residentes ou domiciliados no exterior, e títulos de capitalização;  
2. prêmios, inclusive os distribuídos sob a forma de bens e serviços, obtidos em concursos e sorteios de qualquer espécie e lucros decorrentes desses prêmios; e 3. multa ou qualquer vantagem, de que trata o art. 70 da Lei no 9.430, de 27 de dezembro de 1996;*

**Lançamento a Pagar**

O sistema permite que os tributos sejam informados manualmente ou buscados do cadastro do fornecedor. Caso não existam tributos no cadastro, o sistema busca os tributos incluídos nos Parâmetros de Tributos.  
Os tributos cadastrados no anexo "Tributos Defaults de Fornecedor" do cadastro do fornecedor podem ser buscados por duas formas:  
Clicando no ícone "Calcular Valor das Retenções" (apenas no momento da inclusão); -Clicando no ícone "Exibir Dados para Cálculo das Retenções" e no botão "Buscar Default" (no momento da inclusão e na edição).

Manualmente

Passo a Passo  
1º) Clique no ícone "Exibir Dados para Cálculo das Retenções"; 2º) Clique no ícone "Incluir"; 3º) No campo "Tributo" digite o código do tributo ou clique no botão ao lado do campo para selecionar um tributo; 4º) Se for incluir mais de um tributo, clique no botão "Confirmar" e repita o passo "2º", se for apenas um tributo, clique no botão "OK".

**Lançamento a Receber**

O sistema permite que os tributos sejam informados manualmente ou buscados dos Parâmetros de Tributos. Caso não existam tributos nos parâmetros, os tributos devem ser informados manualmente.

**Observações**

Para excluir um tributo da janela de tributos clique na linha do tributo e clique no ícone "Excluir".

O valor para a base de cálculo é apresentado automaticamente no campo "Base de Cálculo" de acordo com o "Valor Original" do lançamento, podendo ser editado.

O valor de "Base de Cálculo" é atualizado sempre que o "Valor Original" for alterado, mas o cálculo dos Tributos não é atualizado, sendo necessário excluí-los e incluí-los novamente ou apenas clicar no botão "Buscar Defaults".

O valor da retenção do tributo pode ser alterado manualmente clicando duas vezes sobre o valor na coluna "Valor".

**EAI 2.0**

Na versão 12.1.31 em diante, visando facilitar a visualização de tributos e retenções gerados no Protheus, foi criado o campo "Consultar Tributos Protheus". Este botão irá listar todos os tributos e seus respectivos valores que foram gerados diretamente no ERP Protheus:

Ao clicar no botão o sistema irá mostrar os respectivos tributos do lançamento:

Valores de Integração

Esta aba será apresentada se houver valores de integração parametrizados em algum segmento da Linha RM.

**Observação**

A configuração da quantidade de "Casas Decimais" dos campos de "Valores" e "Percentuais" é definida através dos parâmetros Nº Casas Decimais (Assistente de Implantação de Processos | etapa Opções Gerais do Financeiro) e Nº Decimais Percentual (Assistente de Implantação de Processos | etapa Inclusão dos Lançamentos Financeiros).
