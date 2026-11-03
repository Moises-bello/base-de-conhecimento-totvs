---
content_hash: 9f3b290f0284f32d751f80ddacea3ac36af02bf7fa7e974fcb02509c5e8bb0b7
fetched_at: '2026-06-29T00:06:08.677459+00:00'
page_id: '201751321'
product: rm
source: tdn-rm
title: SAU_Cadastros_de_Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/SAU_Cadastros_de_Faturamento
version: 5
---

# Cadastros de Faturamento

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Hospitalar |
| **Menu:** | Cadastros |
| **Assunto:** | 1. Como cadastrar planos de Convênio?  2. Como cadastrar Empresa?  3. Como cadastrar Bloqueio de Atendimento?  4. Como cadastrar Local de Uso?  5. Como cadastrar Tabelas de MATMED Usadas?  6. Como cadastrar Tabelas de Portes Anestésicos?  7. Como cadastrar Tabelas de Preços Utilizadas?  8. Como cadastrar Tabela de Portes de Procedimento CBHPM?  9. Como cadastrar Tabelas de Procedimentos e Serviços?  10. Como cadastrar Padrões de Faturamento e Codificação?  11. Como cadastrar Condições Contratuais com Convênios?  12. Como cadastrar Condição Financeira com Convênio?  13. Como cadastrar Regras para Lançamento Dentro ou Fora da Conta?  14. Como cadastrar Kits de Lançamentos?  15. Como cadastrar Lançamento Automático no Registro de Atendimento?  16. Como cadastrar Itens Terceirizados?  17. Como cadastrar Grupos de Gastos?  18. Como cadastrar Cartão de Crédito?  19. Como cadastrar Tipos de Pré-Glosa?  20. Como cadastrar Motivos de Pré-Glosa?  21. Como cadastrar Tipos de Glosa?  22. Como cadastrar Motivos de Glosa?  23. Como cadastrar Motivos de Recurso de Glosa?  24. Como cadastrar Motivo de Estorno de fatura?  25. Como cadastrar Motivo de Reprocessamento?  26. Como cadastrar Desconto em Repasse?  27. Como cadastrar Critério Geral de Repasse?  28. Como cadastrar Caderno de Gabaritos?  29. Como cadastrar Pendências de Conta?  30. Como cadastrar Setor de Controle de Pendências? |

### 1. Como cadastrar planos de Convênio?

1. ### No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Planos de Convênios**.
2. Clique em **Incluir** (página em branco).
3. Será exibida a tela para cadastro, nela informe a descrição do plano.
4. Preencha a Máscara.
5. Selecione o convênio e o tipo de acomodação (apartamento, enfermaria, berçário, etc).
6. Clique em **OK**.

**Importante**: O campo Máscara é utilizado caso o Plano de Saúde possua um número elevado de sub-planos (superior a 1000). Neste campo você poderá cadastrar a estrutura de codificação da carteira do usuário para permitir a identificação rápida no atendimento. A máscara será utilizada no momento do Registro de Internações e Registro de Atendimentos Externos.

### 2. Como cadastrar Empresa?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Empresa**.
2. Clique em **Incluir** (página em branco).
3. Será exibida a tela para cadastro de empresa, nela informe a descrição da empresa.
4. Clique em **OK**.

### 3. Como cadastrar Bloqueio de Atendimento?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Bloqueio de Atendimento**.
2. Clique em **Incluir** (página em branco).
3. Será exibida a tela para cadastro de bloqueio de atendimento.
4. Nela selecione o convênio e o plano.
5. Selecione a data de inicio e fim do bloqueio.
6. Preencha o motivo do bloqueio.
7. Clique em **OK**.

### 4. Como cadastrar Local de Uso?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Local de Uso**.
2. Clique em **Incluir** (página em branco).
3. Será exibida a tela para cadastro de local de uso.
4. Informe a descrição do local de uso e selecione o Centro de Custo.
5. Na guia **Local de Uso Correlativo** clique em **Incluir** (página em branco) para incluir um padrão de faturamento.
6. Clique em **OK**.

### 5. Como cadastrar Tabelas de MATMED Usadas?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Tabelas de MAT/MED Usadas**.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição.
4. Selecione o tipo de tabela (materiais, medicamentos ou ambos).
5. Marque a caixa **Atualiza itens automaticamente** para que os valores sejam atualizados de acordo com a Nota Fiscal.
6. Nos painéis Itens Brasíndice e Itens Simpro devem ser configurados de acordo com a tabela que está sendo registrada a atualização das informações de materiais/medicamentos.
7. Clique em **OK**.

### 6. Como cadastrar Tabelas de Portes Anestésicos?

Nessa opção é realizado o cadastro de Tabelas de Portes Anestésicos que serão utilizadas no sistema.  
A Tabela Básica de Portes Anestésicos é a definida pela AMB (Associação Médica Brasileira), ela é utilizada pela maioria dos Convênios. Eventualmente, alguns Convênios poderão adotar Tabelas de Portes Anestésicos próprias, que também deverão ser cadastradas.

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Tabelas de Portes Anestésicos**.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição da tabela.
4. Clique em **OK**.

### 7. Como cadastrar Tabelas de Preços Utilizadas?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Tabelas Preços Usadas**.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição da tabela.
4. Selecione o tipo de tabela (procedimentos ou taxas)
5. Selecione a Tabela de Portes.
6. Selecione o Padrão de Faturamento e Codificação.
7. Se necessário marque a caixa CBHPM.
8. Se necessário Marque a caixa Usa Digito Verificador.
9. Selecione a Tabela TISS.
10. Caso a tabela de preço seja de taxas selecione a Tabela TISS de Serviços, a Tabela TISS de Taxas e a Tabela TISS de Diárias.
11. Clique em **OK**.

### 8. Como cadastrar Tabela de Portes de Procedimento CBHPM?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Tabelas de Portes de Procedimento CBHPM**.
2. Clique em **Incluir** (página em branco).
3. Preencha o código, a descrição do porte e o valor do procedimento.
4. Clique em **OK**.

### 9. Como cadastrar Tabelas de Procedimentos e Serviços?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Tabelas de Procedimentos e Serviços**.
2. Clique em **Incluir** (página em branco).
3. Selecione a tabela de preço utilizada.
4. Preencha o Código, o Código Próprio e a Discriminação.
5. Selecione o Fator e o Porte Anestésico.
6. Preencha Incidências e o Filme (m²).
7. Preencha o Custo Operacional CH, o valor do Custo Operacional (R$), o Honorário CH e o valor do Honorário (R$).
8. Informe o Custo Unitário, o Total CH/UPH e o Valor Total Moeda.
9. Marca a caixa **Pacote** para que o valor seja cobrado por pacote.
10. Marque a caixa **Alterar Grupo de Gasto** para que o Grupo de Gasto seja alterado.
11. Selecione o Tipo de Procedimento.
12. Informe a Idade Mínima e a Idade Máxima.
13. Selecione o Sexo e a Classificação.
14. Informe a Quantidade de Permanência.
15. Clique em **OK**.

### 10. Como cadastrar Padrões de Faturamento e Codificação?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Padrões de Faturamento e Codificação**.
2. Clique em **Incluir** (página em branco).
3. Selecione a tabela de Procedimentos e a tabela de Serviços.
4. Informe a quantidade de Visitas Hospitalares após Ato Cirúrgico.
5. Preencha o Percentual do Procedimento Principal.
6. Preencha o Percentual do Procedimento Secundário.
7. Preencha o Percentual do Procedimento por outra Via.
8. Preencha o Percentual do Primeiro Auxiliar em Cirurgias.
9. Preencha o Percentual de outros Auxiliares.
10. Preencha o Percentual de Auxiliar de Anestesista.
11. Preencha o Percentual do Instrumentador.
12. Informe o Horário Extra Inicial e Horário Extra Final.
13. Informe a partir de qual Horário no Sábado é Extra.
14. Preencha o Percentual de Acréscimo de Horário Extra.
15. Preencha o Percentual de Acréscimo de Taxa de Saída.
16. Preencha o Percentual de Taxa Principal.
17. Preencha o Percentual de Taxa de Mesma Via.
18. Preencha o Percentual de Taxa de Via Diferente.
19. Nas guias **Códigos 1**, **Códigos 2**, **Códigos 3**, **Materiais e Medicamento** e **Outras Codificações** inclua Faixas de Codificação.
20. Clique em **OK**.

### 11. Como cadastrar Condições Contratuais com Convênios?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Condições Contratuais com Convênios**.
2. Clique em **Incluir** (página em branco).
3. Selecione a Unidade de Faturamento e o Convênio.
4. Selecione o Padrão de Faturamento e Codificação que será usado para o referido Convênio.
5. Selecione a Tabela de Procedimentos adotada pelo Convênio.
6. Selecione a Tabela de Diárias, Taxas e Serviços adotada pelo Convênio.
7. Caso houver necessidade de uma tabela específica utilize o campo Tabela Especial.
8. Selecione a tabela de Portes Anestésicos adotada pelo Convênio.
9. Selecione a tabela de Materiais adotada pelo Convênio.
10. Selecione a tabela de Medicamentos adotada pelo Convênio.
11. No campo Limite para apresentação de contas (em dias) preencha o número de dias que o convênio aceitará as contas, contando a partir da data da Alta do Paciente. Caso o tempo seja excedido, no momento do encerramento da conta, será exibida mensagem de alerta.
12. Na guia **Parâmetros 1** é possível configurar os parâmetros relacionados ao Registro de Atendimento de pacientes, e configurações de diárias.
13. No painel **Código do Beneficiário** deve ser informada a rotina para cálculo do dígito verificador do código do beneficiário. Se informado, o sistema fará a consistência do código do Beneficiário no momento da digitação na tela de registro de atendimento interno e externo.
14. Na guia **Parâmetros 2** é possível configurar os parâmetros relacionados ao faturamento, a honorários, a cobrança de atendimentos seriados, a aplicação de valor de CH não credenciado e exames.
15. Na guia **Parâmetros 3** é possível configurar os parâmetros relacionados a diagnose e terapia, Mat/Med, taxas e serviços e cálculo de repasse.
16. No campo "**Considerar Alto Custo a partir de"**, informe o valor base para os itens de **Alto Custo**.
17. Marque as opções **Necessita Justificativa** e **Inclui na Central de Autorização**.
18. Na Movimentação de Estoque e na Elaboração de Contas será exibida mensagem de alerta ao usuário informando que o item é de Alto custo.
19. Caso seja marcada a opção **Necessita Justificativa** o médico na prescrição deverá preencher a justificativa.

    20. O parâmetro "**Verifica autorização de execução de procedimento pelo médico através de critério de repasse**" definirá se o convênio verifica a autorização do médico para a realização de determinados procedimentos.

**Importante:**A rotina de Critério de Repasse é alterada para a verificação do parâmetro. Com o parâmetro habilitado o sistema verificará a existência de critério de repasse para o procedimento e o prestador (somente honorários e exames). Caso houver critério de repasse, o processo continuará. Caso contrário, será gerada uma exceção, no qual informará que o Prestador não possui autorização para a execução do procedimento.  
O processo de repasse é executado a cada lançamento na conta, portanto validará também neste momento. Se o item for invalido, ele será estornado ou excluído. A validação será incluída na agenda de atendimento. Antes de salvar, será verificado se o prestador executará o procedimento selecionado.

    21. Na guia **Eletrônico** é possível configurar os parâmetros relacionados a Padrões ABRAMGE, Configurações específicas para Unimed e IPERGS.

    22. Na guia **Eletrônico II** é possível configurar os parâmetros relacionados a grupos de codificação.

    23. Na guia **Eletrônico III – TISS** é possível configurar os parâmetros relacionados a TISS.

    24. Na guia **Taxa Administrativa** é possível configurar os parâmetros relacionados ao percentual de taxa administrativa.

    25. Clique em **OK** para salvar as informações.

### 12. Como cadastrar Condição Financeira com Convênio?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Condição Financeira com Convênio**.
2. Clique em **Incluir** (página em branco).
3. Selecione a Unidade de Faturamento clicando em '' **...**''.
4. Selecione o Convênio clicando em ''**...**''.
5. Selecione a data da vigência.
6. Clique em **Anexos/Valores de CH/CO**.
7. Clique em **Incluir** (página em branco).
8. Selecione o Plano de Convênio.
9. Selecione o Tipo de CH/CO (Principal ou Especial).
10. Selecione o Tipo de Valor (CH ou CO).
11. Selecione se é referente a médico credenciado, não credenciado ou ambos.
12. Selecione o Tipo de Paciente (Interno, Externo ou Ambos).
13. Caso o CH/CO seja do tipo Especial selecione se é especial para Especialidade, Grupo, Honorários, SADT, Diárias, Taxas, Serviços ou Faixa.
14. Selecione a Especialidade/ Grupo/ Item.
15. Preencha o valor.
16. Clique em **OK**.
17. Na tela inicial de cadastro de Condição Financeira com Convênio clique em Anexos/Valores de Filme.
18. Clique em **Incluir** (página em branco).
19. Selecione o Tipo (Básico, Especialidade, Grupo ou Item).
20. Preencha o valor do m².
21. Caso o Tipo seja referente à Especialidade, Grupo ou Item, clique em '' ...'' para selecionar a opção correspondente.
22. Clique em **Salvar**.

### 13. Como cadastrar Regras para Lançamento Dentro ou Fora da Conta?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/Regras para Lançamento Dentro ou Fora da Conta**.
2. Clique em **Incluir** (página em branco).
3. Selecione a Unidade de Faturamento.
4. Selecione o Convênio e o Prestador.
5. Selecione o Tipo de Paciente (Internos, Externos ou Ambos).
6. Selecione o Tipo de Item (Honorário, Exame ou Ambos).
7. Selecione o Tipo de Lançamento (dentro ou fora da conta).
8. Clique em **OK**.

### 14. Como cadastrar Kits de Lançamentos?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Kits de Lançamentos**.
2. Será exibida a tela de cadastro de Kits de Lançamentos.
3. Clique em **Inclui** (página em branco).
4. Selecione a Tabela de Procedimento e a Tabela de Serviço.
5. Preencha o código e a descrição e clique em **Grava**.
6. Na guia **Itens** clique nos botões para incluir itens.
7. Será exibida a tela para pesquisa do item no estoque.
8. Selecione o item e clique em **OK**.
9. Após a inclusão dos itens Clique em **Grava**.
10. Na guia **Procedimento (Vinculado)**, clique no botão de pesquisa.
11. Realize a pesquisa do procedimento vinculado ao KIT e clique em **OK**.
12. Clique em **Grava**.

### 15. Como cadastrar Lançamento Automático no Registro de Atendimento?

Nessa opção é realizado o cadastro de Lançamento Automático durante o Registro de Atendimento no sistema. São cadastrados todos os itens referentes a Diárias / Taxas / Serviços, que serão lançados automaticamente na conta do Paciente.

* Para **Pacientes Internos** serão realizados lançamentos na conta do paciente quando for realizado um Registro de Internação.
* Para **Pacientes Externos** serão realizados lançamentos na conta do paciente quando for realizado um Registro de Atendimento Externo.

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Lançamento Automático no Registro de Atendimento**.
2. Clique em **Incluir** (página em branco).
3. Selecione o Tipo de Paciente (Interno ou Externo).
4. Selecione o Tipo de Atendimento e clique em '' **...**'' para adicionar itens.
5. Preencha a descrição do item ou código e clique em '' ...'' para realizar a busca.
6. Clique no item para selecioná-lo e clique em **OK**.
7. Na tela de cadastro de **Lançamento Automático no Registro de Atendimento** clique em **OK**.

### 16. Como cadastrar Itens Terceirizados?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Itens Terceirizados**.
2. Será exibida a tela de cadastro de Itens Terceirizados.
3. Clique em **Inclui**.
4. Na guia **Dados** preencha o código e a descrição do item.
5. Selecione a unidade de medida do item.
6. Clique em **Grava**.
7. Clique na guia **Preços**.
8. Clique em **Inclui**.
9. Selecione a Tabela Mat/Med e preencha o preço.
10. Clique em **Grava**.

## 

### 17. Como cadastrar Grupos de Gastos?

Nessa opção é realizado o cadastro de Grupos de Gastos no sistema.  
A conta do paciente é dividida em Grupos de Gastos, cada Grupo de Gastos representa uma série de itens que se assemelham.  
Através dessa tela são informados todos os grupos de gastos utilizados na operação do Sistema. Você poderá definir quais os grupos de gastos que terão Incidência de ISSQN (Imposto Sobre Serviços de Qualquer Natureza), informando o seu Percentual. Ao agrupar nota fiscal /recibo por grupo de gasto, é possível informar um produto e um interno.

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Grupos de Gastos**.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição.
4. Caso o grupo calcule ISSQN, marque a caixa **Calcula ISSQN** e preencha a Alíquota ISSQN.
5. Caso o grupo Agrupe nota fiscal, marque a caixa **Agrupa Nota Fiscal** e selecione o Produto Interno e Produto Externo clicando em '' **...**''.
6. Clique em **OK**.

### 18. Como cadastrar Cartão de Crédito?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Cartões de Crédito**.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição da bandeira do cartão de crédito.
4. Clique em **OK**.

### 19. Como cadastrar Tipos de Pré-Glosa?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Tipos de Pré-Glosa**.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição do Tipo de Pré-Glosa.
4. Clique em **OK**.

### 20. Como cadastrar Motivos de Pré-Glosa?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Motivos de Pré-Glosa**.
2. Clique em **Incluir** (página em branco).
3. Selecione o Tipo de Pré-Glosa clicando em '' **...**''.
4. Preencha a descrição.
5. Selecione o Tipo de Auditoria (Interna ou de Convênios).
6. Preencha o resumo da descrição.
7. Marque a caixa **Ativo**.
8. Clique em **OK**.

### 21. Como cadastrar Tipos de Glosa?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Tipos de Glosa**.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição do Tipo de Glosa.
4. Clique em **OK**.

### 22. Como cadastrar Motivos de Glosa?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Motivos de Glosa**.
2. Clique em **Incluir** (página em branco).
3. Selecione o Tipo de Glosa clicando em '' **...**''.
4. Selecione o Tipo de Auditoria (Administrativa ou Médica).
5. Preencha a Descrição.
6. Preencha o resumo da descrição e caso deseje informe a ação a tomar.
7. Clique em '' ...'' para selecionar o Motivo de Glosa da ANS, que são motivos de glosa que serão utilizados no padrão TISS (Troca de Informações em Saúde Suplementar).
8. Clique em **OK**.

### 23. Como cadastrar Motivos de Recurso de Glosa?

1. No TOTVS Gestão Hospitalar acesse Cadastros/Faturamento/ Motivos de Recurso de Glosa.
2. Clique em **Inclui** (página em branco).
3. Preencha a descrição do motivo de recurso de glosa.
4. Clique em **OK**.

### 24. Como cadastrar Motivo de Estorno de fatura?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Motivo de Estorno de Fatura**.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição do motivo de estorno de fatura.
4. Clique em **OK**.

### 25. Como cadastrar Motivo de Reprocessamento?

1. No TOTVS Gestão Hospitalar acesse Cadastros/Faturamento/ Motivo de Reprocessamento.
2. Clique em **Incluir** (página em branco).
3. Preencha a descrição do motivo de reprocessamento.
4. Clique em **OK**.

### 26. Como cadastrar Desconto em Repasse?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Desconto em Repasse**.
2. Clique em **Incluir** (página em branco).
3. Preencha o Nome do desconto.
4. Preencha o nome reduzido.
5. Informe o Percentual de desconto ou o Valor de desconto.
6. Clique em **OK**.

### 27. Como cadastrar Critério Geral de Repasse?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Critério Geral de Repasse**.
2. Clique em **Incluir** (página em branco).
3. Na guia **Identificação** preencha a descrição.
4. Informe o período de vigência.
5. Selecione a Unidade de Faturamento e a Unidade de Atendimento.
6. Informe o período de Vigência.
7. Selecione o Tipo de Base de Cálculo (Valor total do Procedimento, Valor total com deduções ou Valor total com acréscimos).
8. Selecione o Tipo de Distribuição (Normal, Individual ou Indicação).
9. Selecione o Tipo de Repasse (por Grupo de Itens, Lista de Itens, Item, Faixa, Grupo ou Especialidade).
10. Marque a caixa **Valor recebido** caso o repasse seja realizado de acordo com o valor recebido.
11. Marque a caixa **Plantonista Recebe Repasse** caso o plantonista receba repasse.
12. Marque a caixa **Não incluir o custo operacional no Repasse** para que o custo operacional não seja incluído no repasse.
13. Marque a caixa **Não inclui valor do filme no Repasse** para que o valor do filme não seja incluído no repasse.
14. No painel **Faixa** clique em **Incluir** (página em branco) para adicionar faixa de codificação.
15. Na guia **Complemento** pode-se atribuir o critério a um Convênio/Plano/Subplano, ou a um Prestador, ou aplica-lo somente a prestadores cooperados.
16. Selecionando um tipo de paciente ou classe, o critério será aplicado a eles.
17. Na guia **Observação** é possível incluir observações referentes ao critério de repasse.
18. Na guia **Deduções/Acréscimos** são cadastradas as deduções / acréscimos para cada Critério de Repasse. Essa guia somente ficará visível se o campo "Tipo de base de calculo" for igual a valor total com deduções ou valor total com acréscimos.
19. Na guia **Descontos** são informados possíveis descontos em repasses para Prestadores de Serviços de Saúde. Eles devem estar previamente cadastrados na funcionalidade Cadastro/Faturamento/Desconto em Repasses.
20. Na guia Valores de Repasse são informados possíveis descontos em repasses para Prestadores de Serviços de Saúde.
21. Caso a caixa **Valor Restante** esteja marcada, o cálculo para o repasse é feito por último, ou seja, é o valor base de cálculo menos o somatório dos valores de repasse para os outros prestadores.
22. Clique em **OK**.
23. Na tela inicial de cadastro, clique em **OK** para salvar.

### 28. Como cadastrar Caderno de Gabaritos?

1. No TOTVS Gestão Hospitalar acesse Cadastros/Faturamento/ Caderno de Gabaritos.
2. Clique em **Inclui** (página em branco).
3. Clique em '' **...**'' para selecionar o convênio.
4. Preencha a descrição do caderno e informe a Data Inicial e a Data Final.
5. Serão atualizadas as Tabelas Utilizadas conforme Convênio selecionado.
6. Clique em **OK**.

### 29. Como cadastrar Pendências de Conta?

1. No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Pendências de Conta**.
2. Clique em **Inclui** (página em branco).
3. Preencha a descrição.
4. Selecione o Tipo (Impeditiva ou Risco Gerenciável).
5. Clique em **OK**.

### 30. Como cadastrar Setor de Controle de Pendências?

1. ### No **TOTVS Gestão Hospitalar** acesse **Cadastros/Faturamento/** **Setor de Controle de Pendências**.
2. Clique em **Inclui** (página em branco).
3. Preencha a descrição do setor.
4. Clique em **OK**.

divs
