---
content_hash: dc8626d4f56612f50385583111f94f19400aab44430ca92e3c4f1fcaa358c520
fetched_at: '2026-06-29T00:09:18.844993+00:00'
page_id: '421388793'
product: rm
source: tdn-rm
title: FIN - Faturas
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Faturas
version: 23
---

Através deste módulo você controla os cadastros de Faturas. Na janela principal é possível visualizar de forma simplificada, informações de uma ou de várias faturas. Você define quantos e quais cadastros serão apresentados, criando filtros através do Gerenciados de Filtros (localizado na Barra de Ferramentas). Ao executar um filtro cada cadastro será apresentado em uma linha e as informações em colunas.

Dicas  
A permissão para visualização de informações ou realização de processos deste módulo pode ser configurada por Usuário ou por Perfis, no menu Segurança dos Serviços Globais.  
Você pode definir quais as colunas que serão apresentadas na janela de visão dos registros, utilizando a funcionalidade "Configurar Colunas", ícone localizado na barra de ferramentas.

Inclusão de Fatura

O processo de inclusão de fatura é realizado através do cadastro de Lançamento Financeiro.

O processo consiste em gerar um ou mais lançamentos que representem um ou mais lançamentos.

Os lançamentos que darão origem ao processo se tornarão "Lançamentos Faturados" e os lançamentos que serão gerados se tornarão lançamentos de "Vencimento de Fatura".

A inclusão de fatura só pode ser realizada para lançamento que:

* Estiver em aberto;
* Não possuir cheque emitido;
* Não possuir vínculos (adiantamento, devoluções ou nota de crédito);
* Não estiver bloqueado para alteração;
* Não tiver sido remetido para banco;
* Não for de previsão;
* Não estiver com a contabilização pendente (a contabilizar).
* Possuir a mesma Moeda;
* Possuir a mesma Natureza;
* Possuir Classificação Tributária compatível (verificar Observações);
* Possuir a mesma compatibilidade Contábil (Não Contábil com Não Contábil, Contábil com Contábil, Contábil com Baixa Contábil, Baixa Contábil com Baixa Contábil, A Contabilizar com A Contabilizar);
* Não sejam de tributos a pagar (são identificados pelas Classificações: 6 (IRRF/PJ), 7 (IRRF/PF - quando fornecedor não possuir categoria do eSocial informada), 18 (CSLL/RF), 19 (PIS/RF), 20 (COFINS/RF), 21 (Tributos Agrupados)), quando o parâmetro "Lançamentos de Tributos serão Faturados pelo TOTVS Gestão Fiscal" estiver marcado.
* Não seja originado do TOTVS Educacional quando estiver com Conta Corrente habilitada.

Situações que impedem a conclusão do processo de Inclusão de Fatura:

* Possuir Cliente/Fornecedor Inativo;
* Possuir Cliente/Fornecedor Bloqueado;
* Possuir Natureza diferente do Tipo de Documento selecionado;
* Possuir Centro de Custo Inativo;
* Possuir Departamento Inativo;
* Rateio com Centro de Custo Inativo;
* Rateio com Departamento Inativo;
* Utilizar Tipo de Documento que Gere INSS;
* Utilizar Tipo de Documento que Gere IRRF;
* Lançamentos possuírem Tipos de Documento diferentes;
* Departamento do Rateio não pertencer a Filial;
* Faltar alguma informação obrigatória;
* Lançamento negativado ou em processo de negativação;
* Rateio de "centro de custo / natureza financeira" inconsistente.

**Observações**

* A geração do lançamento de Vencimento de Fatura respeitará regras do processo de Inclusão de Lançamento Financeiro.
* Com o surgimento da  guia unificada pela DCTFweb será permitida a inclusão de fatura de lançamentos de diferentes classificações tributárias mas que sejam referentes a tributos (INSS, IR, CSLL, PIS, COFINS, Contribuição Social, FGTS e Pensão do módulo TOTVS Folha de Pagamento, lançamentos sem classificação do módulo TOTVS Gestão Fiscal). Para maiores esclarecimentos referente a recolhimento de impostos favor consultar a Secretaria da Receita Federal do Brasil.
* Caso seja necessário o ajuste de diferença a maior ou menor entre o valor da guia DCTF gerada e o valor da fatura, na edição do vencimento de fatura na tela do processo de inclusão, pode ser informado um valor de integração previamente configurado no TOTVS Gestão Financeira (vide mais detalhes em ).
* Na geração dos lançamentos de Vencimento de Fatura o "limite de crédito" do Cliente/Fornecedor não é validado.
* Ao selecionar lançamentos que estejam [bloqueados para a baixa](https://tdn.totvs.com/display/LRM/Bloqueia+baixa++e+Desbloqueia+Baixa) junto com outros desbloqueados, o bloqueio dos vencimentos de fatura seguirão o bloqueio da baixa dos lançamento faturados. Se houver ao menos um lançamento de origem bloqueado, os vencimentos serão gerados bloqueados. Caso contrário, serão criados desbloqueados. Essa regra independe do valor dos lançamentos e do [parâmetro](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+pagar) que determina o comportamento de bloqueio ("Incluir Lançamento a Pagar Bloqueado para Baixa").

**Informações para o Lançamento de Vencimento de Fatura**

Ao utilizar no processo de Inclusão de Fatura o método "Uma fatura para todos os lançamentos selecionados", é possível definir algumas informações que serão levadas para o lançamento de Vencimento de Fatura.  
As informações são:

* Cliente/Fornecedor;
* Filial;
* Conta/Caixa;
* Centro de Custo;
* Departamento;
* Moeda;
* Indexador;
* Histórico;
* Segundo Número;
* Tabelas Opcionais;
* Datas Opcionais;
* Opcionais Alfa.

Ao selecionar o método e avançar o processo os campos são apresentados para que as informações sejam incluídas, dependendo de algumas situações as informações já são apresentadas automaticamente, podendo ser alteradas.

|  |  |
| --- | --- |
| **Lançamentos selecionados** | **Informações apresentadas** |
| Um lançamento com as informações: Cliente/Fornecedor, Filial, Tipo de Documento e Moeda. | São apresentadas as informações do lançamento e as outras em branco. |
| Um lançamento com todas as informações. | São apresentadas todas as informações do lançamento. |
| Um lançamento com todas as informações e que possui um Cliente/Fornecedor que possui informações no Default. | São apresentadas todas as informações do lançamento. |
| Dois lançamentos com todas as informações iguais. | São apresentadas todas as informações dos lançamentos. |
| Dois lançamentos com a informação de "Moeda" igual e todas as outras diferentes. | É apresentado o Cliente/Fornecedor do primeiro lançamento incluído na base, a Moeda e as outras em branco. |
| Dois lançamentos com todas as informações iguais e um dos lançamentos possui um Cliente/Fornecedor que possui informações no Default. | São apresentadas todas as informações dos lançamentos. |
| Dois lançamentos com a informação de "Moeda" igual, todas as outras diferentes e um dos lançamentos possui um Cliente/Fornecedor que possui informações no Default. | É apresentado o Cliente/Fornecedor do primeiro lançamento incluído na base, a Moeda e as outras em branco. |

**Observações**

Informações obrigatórias para a inclusão da fatura:

* Cliente/Fornecedor;
* Filial;
* Tipo de Documento;
* Moeda;
* Número da Fatura;
* Quantidade;
* Data Base;
* Data de Emissão;
* Valor Original.

- Centro de Custo Centro de Custo "Inativo" e que não "Permite Lançamento" não será apresentado para seleção, se ele estiver no lançamento é apresentado no campo, mas a conclusão do processo não será permitida.

- Ao selecionar os outros métodos o preenchimento do lançamento de Vencimento de Fatura terá comportamentos específicos. Por exemplo, quando existir mais de um cliente/fornecedor, quando o mesmo possuir defaults, quando uma Conta/Caixa possuir Default ou quando as informações forem diferentes entre os lançamentos.

- Em cenário onde a fatura é criada a partir de outro módulo, como por exemplo o TOTVS Gestão Fiscal, ou a partir do TOTVS Gestão Financeira e o parâmetro *Copiar Ref. Para Fatura* marcado, o número da fatura é gerado com o mesmo número atribuído ao campo Ref. Fatura, acrescido de zeros à esquerda quando parametrizado. Caso já exista um registro com este número, um novo será montado buscando entre as faturas já existentes na coligada o último número que contenha somente caracteres numéricos e incrementado de 1.

Data de Vencimento - Vencimento de Fatura

A data de vencimento dos lançamentos de Vencimento de Fatura é definida pelas informações dos campos "Intervalo em dias", "Data Base" e "Manter o mesmo dia de vencimento".  
A data de vencimento do primeiro lançamento gerado será a data informada no campo "Data Base" e a data dos demais será de acordo com a informação do campo "Intervalo em dias" ou do campo "Manter o mesmo dia de vencimento".

Intervalo em dias

Este campo fica disponível apenas quando a informação do campo "Quantidade" for maior que "1" e o campo "Manter o mesmo dia de Vencimento" estiver desmarcado.  
A quantidade de dias entre as Datas de Vencimento dos lançamentos de Vencimento de Fatura serão de acordo com a informação deste campo.

Data Base

A informação é apresentada automaticamente, quando a "Data de Vencimento" dos lançamentos selecionados para a Inclusão da Fatura for diferente, a data apresentada será a data do "Sistema", quando a "Data de Vencimento" for a mesma em todos os lançamentos, a data apresentada será a data de vencimento dos lançamentos.

Manter o mesmo dia de vencimento

Ao marcar este campo o campo "Intervalo em dias" fica desabilitado.  
Com este campo marcado a Data de Vencimento dos lançamentos de Vencimento de Fatura terá o mesmo "dia" da data informada no campo "Data Base" só que em meses posteriores.

Gerar Número do Documento de acordo com as opções - Vencimento de Fatura

O Número do Documento dos lançamentos de Vencimento de Fatura pode ser gerado automaticamente ou manualmente.  
A definição de como ele será gerado é realizada através da opção "Gerar Número do Documento de acordo com as opções" no processo de Inclusão de Fatura.

*Automaticamente*

Com a opção desmarcada o número do documento será gerado de acordo com os parâmetros "Gerar Número do Documento Sequencialmente" e "Copiar Referência para Número do Documento".

*Manualmente*

Com a opção marcada o número do documento será gerado de acordo com as informações dos campos "Número Base", "Separador" e "Parcela Inicial".

Incluir, Editar e Excluir - Vencimento de Fatura

No último passo para a Inclusão da Fatura é apresentada a janela "Edição dos Vencimentos de Fatura", nesta janela é possível visualizar os Vencimentos de Fatura que serão gerados e seus respectivos valores.  
Neste momento é possível Incluir manualmente mais Vencimentos de Fatura, Editar ou Excluir alguns, antes de serem gerados.

**Inclusão**

Para incluir um novo Vencimento de Fatura selecione um Vencimento de Fatura e clique no ícone "Novo Vencimento de Fatura", informe o Número de Documento, a Data de Vencimento e o Valor Original. Também é possível informar Valor de Multa, Valor de Desconto, Valor de Juros e Valores Opcionais e Valores de Integração do TOTVS Gestão Financeira.  
As informações abaixo serão buscadas das informações já preenchidas na Inclusão de Fatura:

* Filial;
* Conta/Caixa;
* Tipo de Documento;
* Centro de Custo;
* Departamento;
* Moeda;
* Indexador;
* Histórico;
* Segundo Número;
* Tabelas Opcionais;
* Datas Opcionais;
* Opcionais Alfa;
* Data de Emissão.

**Edição**

Para realizar a edição selecione um Vencimento de Fatura e clique no ícone "Editar Vencimento de Fatura".  
Os Vencimentos de Fatura podem ser editados individualmente nos seguintes campos:

* Data de Vencimento;
* Valor Original;
* Valor Multa;
* Valor Desconto;
* Valor Juros;
* Valores Opcionais;
* Valores de integração do TOTVS Gestão Financeira.

Observação: valores de integração de outros módulos (TOTVS Incorporação e TOTVS Educacional) não poderão ser alterados neste passo.

**Observação**

Caso exista um Vencimento de Fatura para mais de um lançamento, os valores apresentados serão a soma dos valores dos lançamentos.

**Exclusão**

Para realizar a exclusão selecione um Vencimento de Fatura e clique no ícone "Excluir Vencimento de Fatura".  
Informações sobre alguns campos:

Número Documento

É o número que será preenchido no campo "Núm. Documento" do lançamento de Vencimento de Fatura gerado após a Inclusão da Fatura.  
O campo só estará disponível para edição se o campo "Gerar Número do Documento de acordo com as opções" estiver marcado.  
Quando o campo estiver indisponível para edição, o "Número do Documento" será de acordo com as regras dos parâmetros "Gerar Número do Documento Seqüencialmente" e "Copiar Referência para Número do Documento".  
Quando o campo estiver disponível para edição e sem preenchimento, o "Número de Documento" será de acordo com as regras dos parâmetros "Gerar Número do Documento Seqüencialmente" e "Copiar Referência para Número do Documento".  
Quando o campo estiver disponível para edição e preenchido, a informação será levada para o "Número do Documento".

Valores

Os campos de valores na inclusão manual de Vencimento de Fatura não apresentarão nenhuma informação default. O preenchimento será a critério do usuário.

Informação de Valores

Na parte inferior da janela "Edição dos Vencimentos de Fatura" é apresentado um comparativo entre os valores da Fatura, que são os valores do lançamento ou dos lançamentos selecionado(s) para a Inclusão de Fatura, e os valores totais dos Vencimentos de Fatura a serem gerados.  
Se houver uma diferença entre os valores o valor com a diferença será exibido na cor vermelha.  
Quando houver diferença entre os "Valores Originais" a Inclusão da Fatura não será permitida.

Proporcionalizar Valores dos lançamentos de Vencimento de Fatura

Ao alterar algum valor dos Detalhes dos Vencimentos de Fatura e confirmar a alteração o sistema oferece a possibilidade de Proporcionalizar os valores dos outros lançamentos de Vencimento de Fatura automaticamente, corrigindo assim as diferenças entre valores.

Informações preenchidas automaticamente - Vencimento de Fatura

Ao concluir o processo de Inclusão de Fatura o sistema gera os lançamentos de Vencimento de Fatura e já preenche algumas informações automaticamente.  
As informações são buscadas do lançamento selecionado para o faturamento ou do processo de Inclusão de Fatura.

* Natureza;
* Filial;
* Cliente/Fornecedor;
* CNPJ/CPF;
* Tipo de Documento;
* Número Documento;
* Segundo Número;
* Data de Emissão;
* Data de Vencimento;
* Data Previsão de Baixa;
* Histórico;
* Valor Original;
* Moeda;
* Indexador;
* Conta/Caixa;
* Desconto;
* Desconto Fórmula;
* Juros;
* Juros Fórmula;
* Juros ao dia;
* Multa;
* Multa Fórmula;
* Multa ao dia;
* Capitalização Mensal;
* Valores Opcionais;
* Valores Opcionais Fórmula;
* Tributos;
* Centro de Custo;
* Rateio por Centro de Custo;
* Departamento;
* Rateio por Departamento;
* Mês de Competência;
* Tabelas Opcionais;
* Datas Opcionais;
* Campos Alfa Opcionais;
* Banco;
* Carteira;
* Convênio;
* Dígito do Convênio;
* Campos Complementares;
* Valores de Integração.

**Observações**

* Dependendo de algumas situações o preenchimento terá comportamentos específicos. Por exemplo, quando existir mais de um cliente/fornecedor, quando um deles possuir defaults, quando uma Conta/Caixa possuir Default ou quando as informações forem diferentes entre os lançamentos.
* A geração do lançamento de Vencimento de Fatura respeitará regras do processo de Inclusão de Lançamento Financeiro.
Informações sobre alguns preenchimentos:

Rateio por Centro de Custo: Se for faturado um lançamento que tenha Rateio, o lançamento de Vencimento de Fatura é preenchido com este Rateio. Se não tiver Rateio, o campo é apresentado em branco.  
Se for faturado mais de um lançamento que tenha Rateio, o lançamento de Vencimento de Fatura é preenchido com estes Rateios, com os valores proporcionais a cada Rateio. Se um dos lançamentos não possuir Rateio, o campo é apresentado em branco.

Rateio por Departamento: Se for faturado um lançamento que tenha Rateio, o lançamento de Vencimento de Fatura é preenchido com este Rateio. Se não tiver Rateio, o campo é apresentado em branco.  
Se for faturado mais de um lançamento que tenha Rateio, o lançamento de Vencimento de Fatura é preenchido com estes Rateios, com os valores proporcionais a cada Rateio. Se um dos lançamentos não possuir Rateio, o campo é apresentado em branco.  
Se o Departamento do Rateio não pertencer a Filial informada no processo, a Inclusão da Fatura não será permitida.

Informações que não podem ser alteradas - Inclusão de Fatura

Neste tópico são apresentadas as informações que não poderão ser alteradas após a execução do processo de Inclusão de Fatura.

Lançamento Faturado

* Natureza
* Filial
* Cliente/Fornecedor
* CNPJ/CPF
* Tipo de Documento
* Data de Emissão
* Data de Vencimento
* Valores Gerais
* Valores Adicionais
* Tipo Contábil
* Funcionário

Lançamento de Vencimento de Fatura

* Natureza
* Filial
* Cliente/Fornecedor
* CNPJ/CPF
* Tipo de Documento
* Data de Emissão
* Valor Original
* Moeda
* Indexador
* Tipo Contábil
* Funcionário
Processos que não podem ser realizados - Inclusão de Fatura

Neste tópico são apresentados os processos que não poderão ser realizados após a execução do processo de Inclusão de Fatura.

Lançamento Faturado

* Cancelamento de Lançamento
* Vínculo
* Baixa
* Cheque
* Incluir Fatura
* Repasse
* Descontar Lançamento
* Gerar Acordo
* Parcelar
* Remeter para Banco

Lançamento de Vencimento de Fatura

* Cancelamento de Lançamento
* Incluir Fatura
* Gerar Acordo
Contabilização - Inclusão de Fatura

Neste tópico são apresentadas informações sobre a Contabilização dos lançamentos Faturados e dos lançamentos de Vencimento de Fatura. Para que o preenchimento das informações contábeis seja realizado corretamente é necessária a utilização de Evento Contábil através de Tabela Default para Evento. Se essa configuração não for realizada e o Tipo Contábil do lançamento Faturado for "Contábil", a Inclusão da Fatura não será concluída. Se o Tipo Contábil for "Baixa Contábil", o processo será concluído e as informações contábeis serão exigidas apenas no processo de Baixa do lançamento de Vencimento de Fatura.

Tipo Contábil

Quando o Tipo Contábil do lançamento selecionado para faturamento for "Baixa Contábil", o Tipo Contábil do lançamento de Vencimento de Fatura será o mesmo.  
Quando o Tipo Contábil do lançamento selecionado para faturamento for "Contábil", o Tipo Contábil do lançamento de Vencimento de Fatura poderá ser "Contábil" ou "Baixa Contábil", essa definição deve ser feita através do campo "Tipo Contábil" apresentado no processo de Inclusão de Fatura.

Informações Contábeis de Inclusão

As informações contábeis de Inclusão podem ser realizadas nos lançamentos Faturados e nos lançamentos de Vencimento de Fatura.

Informações Contábeis de Baixa

As informações contábeis de Baixa são realizadas somente nos lançamentos de Vencimento de Fatura.

Atualização do valor do IRRF-PF na baixa de lançamentos faturados

No momento da inclusão do lançamento, o valor do IRRF/PF, quando a data de geração é "Baixa" o sistema calcula como uma "provisão" baseado no valor que seria retido se o lançamento fosse baixado naquele instante. Como a retenção de IRRF/PF depende dos lançamentos já baixados no período (mês) do Cliente/Fornecedor, no momento da baixa é possível que o valor retido seja muito diferente. Então ao habilitar o parâmetro "[Calcular valor de IRRF de pessoa física do lançamento faturado durante a baixa](https://tdn.totvs.com/x/I_IdGQ)", habilita-se o comportamento de atualizar os valores do IR dos lançamentos faturados, na eventual baixa de um vencimento de fatura. Para que os valores sejam atualizados será preciso também marcar o parâmetro "[Proporcionalizar valor baixado dos lançamentos faturados pelo valor líquido](https://tdn.totvs.com/x/I_IdGQ)".

 Veja Também
