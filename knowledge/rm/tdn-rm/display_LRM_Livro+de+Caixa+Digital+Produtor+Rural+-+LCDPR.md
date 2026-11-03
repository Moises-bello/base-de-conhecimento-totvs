---
content_hash: ef195107f3bcbf944c0482201591f5e2cdbd6ee11628da3ef27b328e74bf6127
fetched_at: '2026-06-29T00:10:37.762349+00:00'
page_id: '540885605'
product: rm
source: tdn-rm
title: Livro de Caixa Digital Produtor Rural - LCDPR
type: documentation
url: https://tdn.totvs.com/display/LRM/Livro+de+Caixa+Digital+Produtor+Rural+-+LCDPR
version: 135
---

LGPD - Lei Geral de Proteção de Dados

Informamos que os dados pessoais contidos nesta rotina foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O cumprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).

Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).

O Livro Caixa Digital do Produtor Rural (LCDPR) foi instituído pela Instrução Normativa RFB no 1.848, de 28 de novembro de 2018, que alterou a Instrução Normativa SRF nº 83, de 11 de outubro de 2001.

O resultado da exploração da atividade rural deverá ser apurado mediante escrituração do LCDPR, que deverá abranger as receitas, as despesas de custeio, os investimentos e demais valores que integram a atividade.

O produtor rural que auferir, durante o ano, receita bruta total da atividade rural superior ao limite estabelecido, deverá entregar arquivo digital que contém o LCDPR até o final do prazo de entrega da declaração do Imposto sobre a Renda da Pessoa Física referente ao respectivo ano-calendário.

Observa-se que o limite de receita bruta deve abranger todas as unidades rurais exploradas pelo contribuinte, de modo a permitir a apuração do resultado da atividade rural.

O Totvs Gestão Financeira desenvolveu a partir do Gerador de Saídas o layout FINLAY0060 - LCDPR - Livro Caixa Digital Produtor Rural.TotvsGen para gerar o arquivo do Livro Caixa do Produtor Rural atendendo a legislação, separado em blocos. Layout disponível no book de Objetos Gerenciais.

Em relação à entidades da aplicação serão mapeadas da seguinte forma:

* Produto Rural: Coligada
* Imóvel rural: Filial
* Terceiros: Partes envolvidas na exploração de propriedades rural e vinculada a filial com percentual de participação

**Parametrização para geração do arquivo**

Totvs Gestão Financeira | Gestão | Gerador de Saídas | Processos | Geração de Saídas

Seleção do Layout

Layout:

Importar da página “Objetos Gerenciais” o layout FINLAY0060 - LCDPR - Livro Caixa Digital Produtor Rural.TotvsGen

Diretório de Destino:

Informar caminho onde o arquivo gerado será salvo.

Gerar arquivos no servidor:

Quando selecionado o arquivo será salvo no servidor de aplicação.

Parâmetros para Geração

Coligada Produtor Rural:

Identificação do declarante cadastrado como Produtor Rural.

CPF Coligada CEI:

Para casos onde o CEI já está informado na coligada, foi disponibilizado na tela da geração do arquivo um parâmetro para informar o CPF do produtor rural. O valor informado nesse parâmetro será usado na geração do registro 0000 de dados do produtor rural declarante do Livro Caixa Digital do Produtor Rural

Data Início do Período:

Este campo deve ser preenchido com a data inicial do período correspondente ao ano-calendário a que se referir o LCDPR.

Data Final do Período:

Data final correspondente ao ano-calendário a que se referir o LCDPR.

Indicador do Início do Período:

* Regular (Início no primeiro dia do ano).
* Abertura (Início de atividades no ano-calendário).
* Início de obrigatoriedade da escrituração no curso do ano calendário. (Exemplo: desenquadramento como isento do IRPF)

Indicador de Situação Especial e Outros Eventos:

* Normal
* Falecimento
* Espólio
* Saída definitiva do País

Data da Situação Especial: em caso de falecimento da pessoa física, a data de falecimento: Informar data solicitada se for o caso.

Forma de Apuração:

* Livro Caixa: Apurou o resultado da atividade rural com base nos lançamentos registrados no Livro Caixa do Produtor Rural.
* Apuração do lucro pelo disposto no artigo 5º da lei nº 8.023, de 1990: Apurou o resultado da atividade rural com base na faculdade disposta no art. 5º da Lei nº 8.023, de 1990 (20% da Receita Bruta)

Código da versão do leiaute:

* Leiaute: Leiaute 1.3
* Período: Ano-Calendário e Situações Especiais a partir de 2019
* Manual: Ato Declaratório Copes nº 1/2020

[Classificação de Municípios](https://tdn.totvs.com/x/n4ovGQ):

No cadastro de Municípios do Gestão fiscal | Codificação de Município, deverá ser atribuído um Código a um Município e sua Classificação.

[Classificação de País](https://tdn.totvs.com/x/woovGQ):

No cadastro de País do Gestão fiscal | Codificação de País, deverá ser atribuído um Código a um País e sua Classificação.

Nos campos abaixo serão inseridas  informações do profissional de contabilidade responsável pela elaboração do LCDPR.

* Nome do Contador
* CPF/CNPJ do Contador
* CRC do Contador
* Email do Contador
* Telefone do Contador

Diretório para geração do arquivo de conferência (formato CSV)

Preenchido, será gerado um arquivo no formato CSV, onde será possível fazer uma conferência de todos os dados gerados no registro Q100.

Caso utilize três camadas, é necessário colocar um diretório no qual o servidor da aplicação tenha acesso de escrita.

A partir da versão **12.1.2306**, o Arquivo de Conferência será gerado na pasta GestaoFinanceira/LCDPR dentro do diretório do FileServerPath.

Salvar os parâmetros de geração

Uma vez gerado o arquivo, quando este parâmetro estiver marcado a próxima geração será carregada com os dados anteriormente informados. Os campos de Classificação de Município e Classificação de País, serão informados a cada geração.

**Blocos do Arquivo**

Entre o registro inicial e o registro final o arquivo digital é constituído por blocos, referindo-se cada um deles a um agrupamento de informações.

Bloco 0: Abertura, Identificação e ReferênciasRegistro 0000

Registro 0000: Abertura do Arquivo Digital e Identificação da Pessoa Física

Na tela de execução do processo de geração da rotina o usuário irá parametrizar para produtores (registros de coligada) os dados para o arquivo que será gerado. Os campos serão informados pelo usuário para cada produtor: Indicador do Início do Período, Indicador de Situação Especial e Outros Eventos e Data da Situação Especial. Os campos Data do Início do Período e Data final do Período serão únicos para todos.

Registro 0010

Registro 0010: Parâmetros de Tributação

Apresenta os parâmetros fiscais que identificam quais blocos e registros serão preenchidos. O campo Forma de Apuração será informado na tela da geração do processo.

Registro 0030

Registro 0030: [Dados Cadastrais](https://tdn.totvs.com/x/QSJtE)

Apresenta os dados cadastrais do produtor rural pessoa física.

Na aplicação (Totvs Gestão Financeira) um produtor rural será um registro da tabela de coligada. Os dados para geração deste registro virão dessa tabela.

Registro 0040

Registro 0040: [Cadastro dos Imóveis Rurais](https://tdn.totvs.com/x/SokvGQ)

Apresenta os dados cadastrais dos imóveis rurais do produtor rural pessoa física.

Na aplicação um imóvel rural será representado pelo cadastro de filial, de onde serão buscados os dados para geração registro no campo CAFIR - Cadastro de Imóvel Rural. Para identificar se um imóvel é propriedade rural será usado o campo “Produtor rural”, e o Cadastro de Atividade Econômica da Pessoa Física CNAE-F.

**Propriedades que o produtor rural é terceiro**

Na aplicação as propriedades rurais que o produtor rural (coligada) participa na exploração, mas que pertencem a outros precisa ser informado no LCDPR.  Os dados deverão ser inseridos na própria filial e deve ter todas as informações necessárias para geração do registro 0040.

No cadastro de Filial campo PROPRIEDADERURAL da GFILIAL foram disponibilizadas as opções:

* 0 - Não rural - Imóvel em zona não rural
* 1 - Rural - Imóvel em zona rural
* 2 - Terceiro não rural - Exploração de Terceiro em imóvel na zona não rural
* 3 - Terceiro Rural - Exploração de Terceiro em imóvel na zona rural

Obs: Na inclusão do cadastro da propriedade (Filial) o default será “Não Rural”.

Para as propriedades de terceiros cadastradas em que o produtor tem participação na exploração, não será permitido realizar movimentações.

Na de inclusão e alteração do lançamento ou extrato de caixa não será apresentada filial parametrizada como Propriedade rural “ Terceiro rural” ou “Terceiro não rural”. No processo de Importação de lançamento e Importação de extrato de caixa, não haverá processamento, caso a filial do cadastro esteja parametrizada com as opções de terceiro.

**Movimentações de propriedades de contraparte**

Na aplicação as propriedades que o produtor rural tem participação na exploração, a qual pertence a um segundo produtor rural serão carregadas no registro 0040.

Serão carregadas para o registro 0040, propriedades rurais, as informações de filiais de outras coligadas da base que tem no anexo de Contraparte do imóvel um vínculo com um terceiro cujo CPF é o mesmo da coligada da geração da rotina.

Exemplo:

Um Produtor rural tem participação na propriedade de um segundo produtor rural.

* O produtor rural deve ser cadastrado como Terceiro (Cadastro Terceiros) na coligada do segundo produtor rural informando seu CPF.
* O produtor rural deverá ser cadastrado como filial (imóvel rural) na coligada do segundo produtor rural e informar seu CPF.
* No anexo “Contraparte do imóvel” dessa filial, deverá ser selecionado o terceiro (cadastrado no passo anterior), informando o tipo do terceiro e o percentual de exploração de participação do produtor rural.

Observação:

As movimentações referentes a essa propriedade serão carregadas para o registro Q100 e deverão ser realizadas na coligada do segundo produtor rural.

Registro 0045

Registro 0045: [Cadastro de Terceiros](https://tdn.totvs.com/x/8CcdHw)

Apresenta os dados de terceiros. Neste registro, deve constar a identificação das partes envolvidas, assim como o Tipo de terceiro relacionado ao imóvel (1 - Condômino, 2 - Arrendador, 3 - Parceiro, 4 - Comodante, 5 - Outro) e o percentual de participação de cada produtor rural na exploração em cada uma unidade rural, quando for o caso.

O terceiro deverá ser vinculado a cada um dos imóveis (filial) ao qual possui participação, informando o tipo de terceiro relacionado e o percentual na exploração do imóvel.

No caso de contra-parte de imoveis de outra coligada, no qual o produtor rural tem participação, a identificação será (ão) apresentada (s) no registro 0045. 

Registro 0050

Registro 0050: [Cadastro das Contas Bancárias](https://tdn.totvs.com/x/JeIdGQ)

Apresenta os dados das contas bancárias da pessoa física utilizadas na atividade rural.

Na aplicação as contas bancárias serão as contas caixas, que poderão ser globais. As informações para o registro virão do cadastro de banco, agência e conta vinculados. A informação que indica se a conta é no exterior virá da agência (campo País).

Para o campo de conta bancária movimentada será considerada a conta caixa onde foi realizada a baixa do (s) lançamento (s) ou inclusão de extrato de Caixa (somente as contas caixas com código específico inserido em seu cadastro serão consideradas).  Caso o pagamento tenha sido realizado com dinheiro será usado o código “000” e para contas caixas sem vínculo a banco o código “999”.

Bloco Q: Demonstrativo do Resultado da Atividade RuralRegistro Q100

Registro Q100: O registro trata os valores movimentados dentro de cada imóvel.

Lançamento Financeiro

Na aplicação os valores serão carregados dos lançamentos financeiros baixados ou parcialmente baixados para a coligada (produtor rural) e filial (imóvel). Lançamentos a receber serão receitas e a pagar despesas. Para o campo “CPF/CNPJ do participante” será carregada a informação do Cliente/Fornecedor informado no lançamento. Aba "Dados Adicionais".

Para lançamentos do tipo "Adiantamento" as infprmações de dados do LCDPR , não deverão ser preenchidos na inclusão de lançamento, o preenchimento dos dados implicará na geração de linha de registro incorreta no LCDPR.

**Exemplo:**

###### REG   **|**DATA        **|**COD\_IMÓVEL **|**COD\_CONTA **|**NUM\_DOC **|**TIPO\_DOC **|**HIST       **|**ID\_PARTIC        **|**TIPO\_LANC  **|**VL\_ENTRADA   **|**VL\_SAIDA   **|**SLD\_FIN  **|**NAT\_SLD\_FIN**|** Q100  **|**02012019  **|**001                 **|**001                 **|**2                 **|**3                **|** Venda   **|** 12345678912   **|** 1                   **|**1000000          **|** 0                **|** 1100000  **|** P                  **|**

Campos disponíveis no lançamento para inclusão de dados:

Tipo de Lançamento no LCDPR

No lançamento financeiro foi criado o campo “Tipo de Lançamento no LCDPR” onde será configurado despesa ou receita com as seguintes opções:

1. Receita da Atividade Rural
2. Despesas de custeio e investimentos
3. Receita de produtos entregues no ano referente a adiantamento de recursos financeiros

Classificação do Lançamento no LCDPR

No lançamento financeiro foi criado o campo “Classificação do lançamento no LCDPR”  onde serão informados valores ou carregados como default do [Tipo de documento](https://tdn.totvs.com/x/l_EdGQ), que deverá ser preenchido, com uma das seguintes opções:

1. Nota Fiscal
2. Fatura
3. Recibo
4. Contrato
5. Folha de Pagamento
6. Outros

CPF/CPNJ do contribuinte sujeito passivo do tributo

Este campo deverá ser preenchido na inclusão do lançamento financeiro e quando gerada a rotina do LCDPR será carregado o valor desse campo para o Registro Q100.

Modalidade Lançamento

Financiamento

A opção "Financiamento" foi disponibilizada para lançamentos com  informações de despesa de juros de financiamento. O valor de juros do financiamento será lançado no campo Juros do lançamento e carregado para o item de baixa. Somente o valor de Juros do financiamento será carregado como despesa para o registro Q100 do LCDPR.

Desconto IOF LCDPR

Na aplicação as movimentações de despesa com IOF em valores de adiantamento feitos junto ao banco serão registras através do item de baixa do lançamento e lançado como um desconto.

* O valor do IOF deverá ser lançado no campo “Desconto” do lançamento.
* Na aba Dados Adicionais deve ser selecionado no campo “Modalidade Lançamento” a opção “Desconto IOF LCDPR”.

No registro Q100 o valor do campo “Desconto” do lançamento será carregado para o item de baixa e lançado como um registro de despesa de adiantamento, aplicado o percentual de exploração da propriedade rural informado na filial.

NPR - Nota promissória

Quando houver receita de determinada transação e em decorrência dessa receita houver juros a pagar a um segundo envolvido, no sistema será realizado lançamento de receita do valor bruto da nota e despesa para o valor de juros, que será inserido no sistema como desconto e lançado no LCDPR como despesa.

Exemplo: O produtor rural faz a venda de 1.000.000,00 de corte de carne para um frigorifico. O frigorifico só irá fazer o pagamento daqui 60 dias. Para que o produtor tenha capital de giro ele negocia com o banco a antecipação do valor, só que o banco fica com 100.00,00 referente a juros e antecipa para o produtor rural 900.000,00.

No sistema a nota fiscal/lançamento financeiro terá o valor de R$ 1.000.000,00 e um desconto de R$ 100.000,00

No registro Q100 essas movimentações serão registradas da seguinte forma:

Será gerado um registro de receita no valor bruto da nota R$ 1.000.000,00, para o CNPJ do frigorífico.  
Será gerado um registro de despesa no valor do desconto R$ 100.000,00, para o CNPJ do banco.

**Observações**:

Para que o registro de despesa seja carregado para o registro Q100 será preciso informar a modalidade de NPR, o CNPJ do participante (CNPJ do banco) e o valor do desconto.

O histórico do registro Q100 corresponderá ao tipo de modalidade definido no lançamento, quando não houver modalidade definida o valor do campo histórico corresponderá ao valor histórico do lançamento.  O histórico fixo carregado para registroQ100 referente a cada modalidade será:

* Financiamento - Juros de financiamento
* Desconto IOF LCDPR - IOF de financiamento
* NPR -Nota Promissória - Despesas NPR
* Financiamento Juros no valor - Juros descontado no valor do financiamento

Tributos no desconto

Para casos onde o lançamento financeiro não vinculado a um movimento e com retenção de tributos são representados no campo desconto foi criada a modalidade “Tributos no Desconto”. Para esse caso será gerado um registro Q100 de receita no valor bruto, referente ao lançamento financeiro, e um outro registro Q100 de despesa com os tributos de retenção presentes na nota referente ao valor lançado no lançamento financeiro como desconto.

Exemplo:

Lançamento de receita baixado no valor de R$1.000,00, desconto de R$200,00 referente a retenções de FUNRURAL E FUNDERSUL e valor da baixa de 800,00.

* Será gerado um registro Q100 de receita no valor de R$1.000,00
* Será gerado um registro Q100 de despesa no valor de R$200,00 com a descrição "Retenção de Tributos" + histórico do lançamento.

Financiamento juros no valor  **Modalidade disponível a partir do layout versão 1.3.1**

Nos financiamentos onde o juros é abatido no valor do financiamento, deve-se usar essa modalidade onde o valor do juros do financiamento será colocado no desconto do lançamento a receber.

Exemplo:

Financiamento de R$ 10.000,00 onde serão R$ 500,00 de juros. Produtor rural irá receber apenas R$ 9.500,00. No lançamento financeiro a receber deverá ser lançado R$ 10.000,00 no valor original e R$ 500, 00 no campo desconto que  é o juros do financiamento.

* Será gerado um registro Q100 de despesa  no valor de R$ 500,00 na conta corrente 999 (Numerário em trânsito)
Tratamentos 

**Alteração Global e Importação de Lançamentos**

Para facilitar o preenchimento dos campos necessários para geração do registro Q100 os processos de Alteração Global e Importação de Lançamento poderão ser usados.

**Preenchimento dos dados do LCDPR automático quando o lançamento for originado de outros módulos**

* No campo "Classificação do lançamento no LCDPR", o default configurado no "Tipo de Documento" será carregado na inclusão do lançamento no financeiro (quando existir).
* No campo "Tipo de lançamento no LCDPR" será considerado o seguinte:

Quando a classificação do tipo de documento for definida como "A Pagar e A Receber" e o lançamento gerado for "A Receber", a opção "Receita da atividade rural" será carregado como default. Quando o lançamento for "A Pagar" será carregado como default a opção "Despesas de custeio e investimentos". Caso a classificação do tipo de documento seja somente "A Receber" ou somente "A Pagar" será verificado a classificação do lançamento a ser gerado e carregado o default de acordo com a despesa ou receita.

**Das retenções de tributos FUNRURAL / INSS e Outros retido nas notas**

Para os lançamentos de receita gerados a partir de movimento vinculado (Totvs Gestão de Estoque, compras e Faturamento) e com o campo "Tipo de Documento" (do livro caixa) definido como "Nota Fiscal" será gerado um registro Q100 de receita no valor bruto do movimento e um outro registro Q100 de despesa com os tributos de retenção presentes na nota.

**Exemplo**:  
Nota fiscal: R$1.000,00  
Tributos retidos: R$100,00  
Valor líquido da nota (valor financeiro): R$900,00

Gera um registro Q100 de receita no valor da nota fiscal  
Gera um registro Q100 de despesa no valor dos tributos retidos.

**Observações**:

* O tipo de tributo "Outros" será carregado para registro Q100 quando a opção "Incluir tributos retidos do tipo Outros", for marcada na geração do arquivo.
* Os tributos citados acima são carregados do registro de movimento.
* Os tributos FUNRURAL/INSS e Outros retidos no movimento, no item ou em ambos serão carregados para o registro Q100 como despesa.

**Parcelamento de notas**

Quando houver parcelamento de uma nota no módulo Gestão de Estoque, Compras e Faturamento o valor do registro Q100 será proporcional ao valor bruto da nota, ou seja será gerado um registro para cada parcela proporcional ao seu valor, respeitando o valor do percentual de participação do imóvel (filial).

Ex. O valor bruto da nota inserida no sistema será parcelado em  3 vezes, assim serão gerados registros proporcionais aos valores de cada parcela e com percentual de exploração do imóvel de 50%.

* Valor da Nota R$ 5.755,35
* Percentual de exloração 50% - R$ 2.877,68
* Valor das parcelas nos registro Q100:

1. R$ 1.084,88 - (30% do valor da nota)
2. R$   512.22 - (20% do valor da nota)
3. R$ 1.280.56 - (50% do valor da nota)

No registro Q100 serão gerados 3 registros referentes ao valor de cada parcela já aplicado o percentual que cada uma representa na nota e que foi definido na configuração do movimento (na primeira parcela 30%, na segunda parcela  20% e na terceira parcela 50%  ). Sobre esses valores ainda será aplicado o percentual de participação do imóvel de 50% sobre o valor bruto da nota (50% de 5.755,35= 2.877,68 ).

Obs: Caso o valor do percentual de participação do imóvel seja de 100% os valores das parcelas serão proporcionais ao valor bruto da nota considerando apenas os percentuais de cada parcela.

Quando na nota houver parcelamento financeiro, os tributos deverão ser destacado apenas na primeira parcela .  Abaixo segue alguns exemplos de como deverá ser feito:

**Exemplo de parcelamento com tributo**:

Um Movimento que gerou dois lançamentos financeiro.

Movimento:

Valor Bruto: 10.000,00

FUNRURAL: 120,00

Valor Líquido: 10.120,00

Parcelamento Financeiro: 10.000,00

Primeira Parcela (60%)

   Data da Baixa: 01/01/2020

   Valor baixado: 6.000,00

Segunda Parcela (40%)

   Data Baixa: 01/02/2020

   Valor Baixado: 4.000,00

O cálculo para gerar o valor do registro Q100 das parcelas será:

Primeira Parcela:  
  valorbaixado + valortributos = valor q100  
  6.000,00 + 120,00 = 6.120,00  
  
Segunda parcela em diante  
  valorbaixado = valor q100  
  4.000,00

Geração registro Q100  
Q100 | 01/01/2020 | PRIMEIRA PARCELA | 6.120,00 | 6.120,00 | P  
Q100 | 01/01/2020 | FUNRURAL | 120,00 | 6.000,00 | P  
Q100 | 01/01/2020 | SEGUNDA PARCELA | 4.000,00 | 10.000,00 | P

**Desconto de duplicata**

Quando houver um desconto de duplicata para um lançamento a receber, será gerado um registro Q100 com o valor do desconto como despesa.

**Exemplos**:

1 - Lançamento a receber no valor de 1.000.000,00.

Situação: É gerado um desconto de duplicata no valor de 200.000,00

Comportamento: É gerado um registro Q100 no valor 1.000.000,00 como receita e um registro no valor de 200.000,00 como despesa, na mesma conta caixa registrada no lançamento.

Movimentações de propriedades de contraparte

Na aplicação as movimentações das propriedades que o produtor rural tem participação, mas que foram feitas por um segundo produtor rural, deverão ser inseridas na coligada deste segundo produtor rural, essas movimentações serão carregadas para o registro Q100 do produtor rural gerador da rotina. Para isso deve ser informado na inclusão do (s) lançamento (s) a propriedade (filial) do outro produtor rural e preenchido corretamente os demais campos para geração da rotina.

**Nota fiscal com vinculo de adiantamento**

Quando é feito a baixa de uma Nota Fiscal onde o valor total ou parcial foi vinculado a um crédito de adiantamento, será gerado no Q100 o registro dessa movimentação de acordo com a conta caixa do lançamento de nota fiscal e de seu (s) crédito de adiantamento.

**Exemplos**:

1 - Lançamento de nota fiscal com vinculo de crédito de adiantamento na mesma conta caixa:

Situação: Adiantamento, vínculo e nota fiscal tem o mesmo valor, então o vínculo é total e a conta caixa da nota fiscal informada na baixa é a mesma do crédito de adiantamento.

Comportamento: Sistema deverá gerar um registro Q100 com o valor baixado + valor vinculado do crédito de adiantamento para conta caixa do adiantamento.

Adiantamento: 1000,00 - Conta caixa: 0004

Lançamento de Nota: 1000,00

Vinculo: 1000,00

Baixa: 0,00

Q100 - 0004 | 1000,00

2 - Lançamento de nota fiscal com vinculo de crédito de adiantamento em conta caixa diferente:

Situação: Adiantamento foi efetuado em uma conta caixa, vinculado a nota e a parte em aberto da nota, baixada em outra conta caixa.

Comportamento: Sistema deverá gerar um registro Q100 com o valor baixado na conta caixa da nota e um outro registro Q100 com o valor vinculado na conta caixa do adiantamento.

Adiantamento: 1000,00 - Conta caixa: 0004

Lançamento de nota: 5000,00

Vinculo: 1000,00

Baixa: 4000,00 - Conta caixa: 0003

Q100 - 0004 | 1000,00  
Q100 - 0003 | 4000,00

3 - Lançamento de nota fiscal com vários vínculos de crédito de adiantamento em conta caixa diferente:

Situação: Dois créditos de adiantamento efetuados em contas caixas diferentes, vinculados a uma nota e a nota baixada em uma outra conta caixa.

Comportamento: Sistema deverá gerar um registro Q100 com o valor baixado na conta caixa da nota e outros dois Q100, na conta caixa dos adiantamentos.

Adiantamento1: 1000,00 - Conta caixa: 0004

Adiantamento2: 300,00 - Conta caixa: 0009

Lançamento de nota: 5000,00

Vinculo: 1300,00

Baixa: 3700,00 - Conta caixa: 0003

Q100 - 0004 | 1000,00  
Q100 - 0009 | 300,00

Q100 - 0003 | 3700,00

**Observações**

* Caso um ou mais adiantamentos e a baixa da nota sejam na mesma conta caixa, então o valor do vínculo e da baixa serão somados e gerado apenas um registro Q100 para essa conta caixa.
* Os registros Q100 referentes ao adiantamento sempre serão gerados na data da nota fiscal pois é onde ocorreu a entrega efetiva dos produtos.
* Todo lançamento quando preenchido os dados obrigatórios para geração do LCDPR serão carregados para o registro Q100. Assim para os lançamentos de Adiantamento e Crédito de Adiantamento o campo“Classificação do lançamento no LCDPR” não deverá ser preenchido na inclusão desse tipo de lançamento. Caso isso ocorra, na geração da rotina, as informações estarão inconsistentes. Sugerimos que os defaults para  esses dois tipos de documento não sejam preenchidos.

**Inclusão de fatura para Lançamento Financeiro e oriundos do Gestão de Estoque, Compras e Faturamento**

Para geração de registro Q100 de lançamentos faturados será preciso que os campos referente a geração do LCDPR sejam preenchidos no (s) lançamento (s) de origem da geração de fatura (lançamento faturado). A medida que os vencimentos de fatura forem baixados nas respectivas datas de pagamento do título, será gerado no Q100 um registro referente ao valor baixado. 

**Exemplo**:

Lançamento A de R$ 1.000,00

Lançamento B de R$ 1.000,00

Gera-se fatura para esses dois lançamentos no valor total e R$ 2.000,00 com vencimentos de fatura nos seguintes valores e datas de vencimento:

Vencimento de Fatura 01 - R$ 666,67 - venc. 02/06/2020

Vencimento de Fatura 02 - R$ 666,67 - venc. 02/07/2020

Vencimento de Fatura 03 - R$ 666,66 - venc. 02/08/2020

Quando for realizado o pagamento/baixa do primeiro vencimento de fatura será gerado um registro Q100 no valor da baixa e o lançamento de fatura ficará com status "Fatura parcialmente Baixada". A medida que acontecer os demais pagamentos/baixas serão gerados registros referente a essas baixas.

O valor do tributo referente a fatura será integral destacado na primeira parcela e lançado como despesa.

**Exemplo**:

Dois movimento gerando um lançamento financeiro e agrupando esses lançamento em uma mesma fatura.    
   
Primeiro Movimento:

     Valor Bruto: 10.000,00

     FUNRURAL: 120,00

     Valor Líquido: 10.120,00

Segundo Movimento:

     Valor Bruto: 30.000,00

     FUNRURAL: 360,00

     Valor Líquido: 30.360,00

Lançamento do Primeiro Movimento: 

     Valor Original: 10.000,00

Lançamento do Segundo Movimento: 

     Valor Original: 30.000,00

Fatura (2 Parcelas)

Primeiro vencimento de fatura (20.000,00)

     Data da Baixa: 01/01/2020  
     Valor Baixado: 20.000,00

Segundo vencimento de fatura (20.000,00)

     Data da Baixa: 01/02/2020  
     Valor Baixado: 20.000,00

Geração registro Q100 

     Referente baixa do primeiro vencimento de fatura

Q100 | 01/01/2020 | LANCAMENTO DO PRIMEIRO MOVIMENTO | 5.120,00 | 5.120,00 | P  
Q100 | 01/01/2020 | FUNRURAL DO PRIMEIRO MOVIMENTO      |     120,00 | 5.000,00 | P    
Q100 | 01/01/2020 | LANCAMENTO DO SEGUNDO MOVIMENTO | 15.360,00 | 20.360,00 | P  
Q100 | 01/01/2020 | FUNRURAL DO SEGUNDO MOVIMENTO      |     360,00 | 20.000,00 | P    
   
     Referente baixa do segundo vencimento de fatura    
Q100 | 01/02/2020 | LANCAMENTO DO PRIMEIRO MOVIMENTO | 5.120,00 | 25.120,00 | P  
Q100 | 01/02/2020 | FUNRURAL DO PRIMEIRO MOVIMENTO      |     120,00 | 25.000,00 | P    
Q100 | 01/02/2020 | LANCAMENTO DO SEGUNDO MOVIMENTO | 15.360,00 | 40.360,00 | P  
Q100 | 01/02/2020 | FUNRURAL DO SEGUNDO MOVIMENTO      |     360,00 | 40.000,00 | P

**Valor de desconto**

Para lançamentos que possuir valor de desconto será gerado no arquivo um registro Q100 para discriminar esse desconto. No arquivo será gerado registro referente ao desconto sempre para a conta 999 - Numerário em trânsito.

Quando o lançamento for a receber o registro de desconto será lançado no arquivo como despesa.  Quando o lançamento for a pagar o registro de desconto será lançado no arquivo como receita.

**Observação**:

As modalidades "Desconto IOF", "NPR - Nota Promissória" e "Tributos no desconto" não tiveram seu comportamento alterado, pois estes utilizam o campo desconto para outra finalidade.

**Exemplo**:

Tipo: Lançamento recebido

   Valor original: 1.000,00

   Desconto: 100,00

   Valor baixado: 900,00

Geração do registro Q100: 

Q100 | Lançamento a receber                 | 1.000,00 | 1.000,00 | P

Q100 | Desconto Lançamento a receber |   100,00 |   900,00 | P

Tipo: Lançamento Pago

   Valor original: 1.000,00

   Desconto: 100,00

   Valor Baixado: 900,00

Geração do registro Q100:

Q100 | Lançamento a Pagar                 | 1.000,00 | 1.000,00 | N

Q100 | Desconto Lançamento a Pagar |   100,00 |   900,00  | N

**Valores Opcionais a descontar**

Para lançamentos com valores opcionais parametrizados com a ação "Descontar" será gerado no arquivo um registro Q100 referente a cada valor opcional a descontar. Para cada valor opcional será gerado um registro Q100. O registro do valor opcional  será sempre na conta 999 - Numerário em trânsito.

Quando o lançamento for a receber o valor opcional a descontar será lançado no arquivo como despesa. Quando o lançamento for a pagar o valor opcional a descontar será lançado no arquivo como receita. A descrição do valor opcional mais o histórico do lançamento  serão carregados para o histórico do registro Q100.

**Exemplo Lançamento recebido**:

   Valor original: 1.000,00

   Valor Opcional 1: 100,00

   Valor Baixado: 900,00

Geração do registro Q100: 

Q100 | Lançamento a receber                            | 1.000,00 | 1.000,00 | P

Q100 | Valor Opcional 1 Lançamento a receber |   100,00 |   900,00 | P

**Exemplo Lançamento Pago**:

   Valor original: 1.000,00

  Valor Opcional 4: 100,00

   Valor Baixado: 900,00

Geração do registro Q100:

Q100 | Lançamento a Pagar                            | 1.000,00 | 1.000,00 | N

Q100 | Valor Opcional 4 Lançamento a Pagar |   100,00 |   900,00  | N

**Valores que acrescentam**

Para lançamentos que possuir valor de multa, juros, capitalização e valores opcionais que acrescentam,  será gerado no arquivo um registro Q100 referente a cada valor  a acrescentar. Para cada valor será gerado um registro Q100. O código da conta será o mesmo do lançamento pois o valor realmente transitou na conta.

**Exemplo Lançamento recebido**:

   Tipo: Receber

   Valor original: 1.000,00

   Juros : 100,00

   Multa: 200,00

   Capitalização : 300,00

   Valor Opcional 4: 400,00

   Valor Baixado: 2.000,00

Geração do registro Q100: 

Q100 | Lançamento a receber                 | 1.000,00 | 1.000,00 | P

Q100 | Juros Financeiro Lançamento a receber |   100,00 |   1100,00 | P

Q100 | Multa Financeira Lançamento a receber |   200,00 |   1300,00 | P

Q100 | Capitalização Lançamento a receber |   300,00 |   1600,00 | P

Q100 | Valor Opcional 4 Lançamento a receber |   400,00 |   2000,00 | P

**Exemplo Lançamento Pago**:

   Tipo: Pagar

   Valor original: 1.000,00

   Juros : 100,00

   multa: 200,00

   Capitalização : 300,00

   Valor Opcional 4: 400,00

   Valor Baixado: 2.000,00

Geração do registro Q100: 

Q100 | Lançamento a Pagar                 | 1.000,00 | 1.000,00 | N

Q100 | Juros Financeiro Lançamento a Pagar |   100,00 |   1100,00 | N

Q100 | Multa Financeira Lançamento a Pagar |   200,00 |   1300,00 | N

Q100 | Capitalização Lançamento a Pagar |   300,00 |   1600,00 | N

Q100 | Valor Opcional 4 Lançamento a Pagar|   400,00 |   2000,00 | N

**Observação**:

Para a modalidade "Financiamento" o comportamento não foi alterado pois este utiliza o campo juros para outra finalidade.

**Inclusão de Movimento de Exportação**

Implementada  validação do campo "Núm. Declaração de Exportação" para preenchimento do número do documento no Livro Caixa Digital do Produtor Rural quando o movimento se referir a exportação.

Nestes casos, a informação deverá ser obtida no TOTVS Gestão de Estoque, Compras e Faturamento, no movimento associado ao registro, no campo que está localizado na aba Exportação do movimento (TMOVFISCAL.DECLARACAOEXPORTACAO).

Extrato de Caixa

Movimentações de despesas bancárias serão lançadas no Extrato de Caixa.

Quando os campos estiverem preenchidos no extrato de caixa o registro Q100 será carregado com o valor e número do documento. A filial movimentada levará a informação do imóvel e a conta caixa as informações da conta.

Campos disponíveis no extrato de caixa para inclusão de dados:

Tipo de Lançamento no LCDPR

No extrato de caixa foi criado o campo “Tipo de Lançamento no LCDPR” onde será configurado despesa ou receita com as seguintes opções:

1. Receita da Atividade Rural
2. Despesas de custeio e investimentos
3. Receita de produtos entregues no ano referente a adiantamento de recursos financeiros

Classificação do Lançamento no LCDPR

No extrato de caixa foi criado o campo “Classificação do lançamento no LCDPR”, que deverá ser preenchido, com uma das seguintes opções:

1. Nota Fiscal
2. Fatura
3. Recibo
4. Contrato
5. Folha de Pagamento
6. Outros

CPF/CNPJ do Participante

Na aplicação este campo poderá ser usado para informar CNPJ do banco. Um dos usos previstos é para geração de movimentações de despesa a partir do extrato de caixa para o LCDPR. Quando preenchido no extrato de caixa será carregado para o campo CPF/CNPJ do participante do registro Q100 de movimentação, quando não, será levado o CPF do Produtor rural (coligada).

**Alteração Global e Importação de Extrato de Caixa**

Para facilitar o preenchimento dos campos necessários para geração do registro Q100 os processos de Alteração Global e Importação de Extrato poderão ser usados.

Arquivo de conferência (CSV)

Quando o parâmetro “Diretório para geração do arquivo de conferência” estiver preenchido com um diretório válido, na geração do arquivo do LCDPR, será gerado um log com a memória de cálculo dos registros Q100 para que seja possível validar as informações coletadas e carregadas no arquivo.

A partir da versão **12.1.2306**, o Arquivo de Conferência será gerado na pasta GestaoFinanceira/LCDPR dentro do diretório do FileServerPath.

No log (arquivo CSV) será apresentada as seguintes informações:

|  |  |  |
| --- | --- | --- |
| **CAMPO** | **ORIGEM** | **DESCRIÇÃO** |
| Origem | Interno | Origem do registro Q100:  Lançamento Extrato Retenção Movimento Modalidade Financiamento Modalidade Desconto no IOF Modalidade NPR Modalidade Tributos no Desconto Adiantamento Desconto Duplicata Fatura Descontos Financeiro Acréscimos Financeiro Modalidade Financiamento Transitório |
| Ref. Lançamento | FLAN | Referência dos lançamentos |
| Ref. Baixa | FLANBAIXA | Identificador do item de baixa |
| Ref. Movimento | TMOV | Identificador do movimento |
| Ref. Fatura | FLAN | Identificador da fatura |
| Ref. Extrato | FXCX | Identificador do extrato |
| Filial | GFILIAL | Identificador da filial |
| Conta Caixa | FCXA | Identificador da conta caixa |
| Num. Documento | FLAN, FXCX | Número do documento |
| Cód. Tipo Documento | FTDO | Código do tipo do documento |
| Descrição Tipo Documento | FTDO | Descrição do tipo do documento |
| Data | FLANBAIXA, FXCX | Data da baixa / compensação |
| Percentual Exploração | GFILIAL | Percentual de exploração |
| Valor Entrada | FLANBAIXA, FXCX | Valor da receita |
| Valor Saída | FLANBAIXA, FXCX | Valor da despesa |
| Saldo | Cálculo interno | Saldo = receita - despesa |
| Histórico | FLAN, FXCX | Histórico fixo + histórico do lançamento / extrato de caixa |
| Classe LCDPR | FLAN | Classe da LCDPR |
| Tipo LCDPR | FLAN | Tipo da LCDPR |
| Valor Juros | FLAN | Valor dos juros |
| Valor Desconto | FLAN | Valor dos descontos |
| CPF/CNPJ Beneficiário | FLAN | CPF/CNPJ do beneficiário |
| Valor Bruto Movimento | TMOV | Valor bruto do movimento |
| Forma Pagamento | FLANBAIXA, FXCX | Forma de pagamento |

Registro Q200

Registro Q200: Resumo Mensal do Demonstrativo do Resultado da Atividade Rural

Bloco preenchido com base nas informações do Bloco Q100.

Será apresentado neste bloco o saldo cumulativo até o mês, ou seja, registra o saldo dos lançamentos do mês, acrescido do saldo final do mês imediatamente anterior da declaração.

Bloco 9: Encerramento do Arquivo DigitalRegistro 9999

Registro 9999: Identificação do Signatário do LCDPR e Encerramento do Arquivo Digital

Este registro traz informações do profissional de contabilidade responsável pela elaboração do LCDPR e a quantidade total de registros (linhas) do arquivo do LCDPR. Há que se ressaltar que vários registros ocorrem mais de uma vez. Portanto, na contagem dos registros, será considerado todos os registros informados, ainda que repetidos.

 Informações Complementares

* [Manual Receita Federal](http://receita.economia.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/lcdpr-livro-caixa-digital-do-produtor-rural/lcdpr-livro-caixa-digital-do-produtor-rural)
* [Tabelas de Código SPED](http://sped.rfb.gov.br/pasta/show/1932)
* [DT -Layout Livro Caixa Digital Produtor Rural - LCDPR](https://tdn.totvs.com/x/y86-Hw)
* [DT - Campo CPF/CNPJ do contribuinte sujeito passivo do tributo para LCDPR](https://tdn.totvs.com/x/LVo9I)
* [DT - Campo no lançamento para "modalidade" no LCDPR](https://tdn.totvs.com/x/mf5eI)
* [DT - Campos da LCDPR no extrato de caixa](https://tdn.totvs.com/x/2d5eI)
* [DT - Código da conta caixa para LCDPR](https://tdn.totvs.com/x/K1ErI)
* [DT - Gerar registro Q100 para despesa de juros de financiamento](https://tdn.totvs.com/x/KZhvI)
* [DT - Tratar despesas movimentadas por extrato de caixa no LCDPR](https://tdn.totvs.com/x/UeBeI)
