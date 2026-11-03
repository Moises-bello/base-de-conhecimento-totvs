---
content_hash: 932a52ed00d54064eaf57c3017aab06adf0cf1ac1d900f0b29277c741f446a80
fetched_at: '2026-06-29T00:10:32.903839+00:00'
page_id: '528450667'
product: rm
source: tdn-rm
title: Taxa de Inscrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528450667
version: 12
---

|  |  |
| --- | --- |
| Descrição | Processo Seletivo |
| Observações | Cobrança de Taxa de Inscrição |

Esta página se destina à explicação detalhada do processo de seleção de alunos com cobrança de taxa de inscrição.

**PREMISSAS:**

É necessário que já exista uma conta caixa

# Identificação

 Caminho: **Módulo Educacional | Processo Seletivo| Cadastro| Processo Seletivo| Aba: Identificação| Valor da Inscrição**:

**Campos "Código"** - Preenchido após salvar a tela inicial do processo seletivo e ele é sequencial.

**Campo "Nome do Processo Seletivo"** - Ele é preenchido com o nome que deseja dar ao Processo Seletivo

**Campo “Instituição”** - Ele só será preenchido quando o processo seletivo for realizado para terceiros (empresas que queiram utilizar o modulo Processo Seletivo para selecionar candidatos para determinado curso ou atividade).

AtençãoSe o campos INSTITUIÇÃO for preenchido em outra situação NÃO conseguiremos executar o processo até o final. Fazendo-se necessário criar um novo Processo Seletivo

**Campo “Máximo de Inscrições por Candidato”**- Especifica o número de vezes que uma mesma pessoa poderá se inscrever no Processo Seletivo. Podem existir Processos Seletivos nos quais uma mesma pessoa concorrerá em uma ou mais vagas.

**Campo “Valor da inscrição”** - Define um valor de inscrição padrão para o Processo Seletivo. Ao incluir uma Área de Interesse Ofertada, automaticamente ela irá assumir esse valor como taxa de inscrição, no entanto, será possível definir taxas específicas para cada uma das áreas de interesse do Processo Seletivo.

Quando o Processo Seletivo utiliza a opção de “Controle de Vagas”, as “Áreas Ofertadas” oferecidas pelo mesmo, não podem ter áreas opcionais, pois a classificação de Processos Seletivos com “Controle de Vagas” é feita, somente, por ordem de inscrição. Sendo assim, a classificação em uma área opcional iria afetar a ordem de candidatos classificados pelo número de inscrição

# Informações Financeiras

Caso o Processo seletivo tenha taxa de inscrição, deve-se seguir as  informações abaixo para sua parametrização.

Caminho: **Módulo Educacional| Processo Seletivo| Cadastro| Processo Seletivo| Aba: Informações Financeiras**

Importante

O parâmetro "Não habilitar opções de pagamento para boleto vencido" faz com que os métodos de pagamento parametrizados(Boleto, Cartão, Pix) não estejam disponíveis na central do candidato caso o boleto esteja vencido. **Disponível a partir da versão 12.1.2209.114.**

Nesta aba são configuradas diversas informações utilizadas na integração com o Módulo Gestão Financeira. Os serviços do Módulo Gestão Financeira são necessários para inclusão de lançamentos financeiros, servindo de base para emissão e baixa de boletos da inscrição. Os lançamentos financeiros também são realizados para o pagamento de Fornecedores que tenham trabalhado em um determinado Processo Seletivo.

O campo “nosso número” pertencente ao lançamento e será gerado com base no *Id Boleto* (Código sequencial utilizado para gerar o campo nosso número).

Na opção “Informações Financeiras – Inscrições”, devem ser definidos os parâmetros para geração dos lançamentos e boletos de inscrição por meio da integração com o Módulo Gestão Financeira.

**Cliente/Fornecedor** - Deve ser selecionado um registro de cliente a partir do cadastro de clientes/ fornecedores. Esse registro compõe o lançamento financeiro de cada uma das inscrições, evitando a necessidade de se criar uma entrada no cadastro de clientes/fornecedores para cada um dos candidatos.

**Conta/Caixa -** Identifica a conta corrente utilizada no processo de recebimento dos boletos. Ex: “Caixa Econômica Federal”.

**Tipo de Documento -** Deve ser selecionado um tipo de documento a partir da lista de “Tipos de Documento” disponível. Um tipo de documento, é um registro que armazena uma série de parâmetros que caracterizam um lançamento financeiro. Uma das funções de um registro de “Tipo de Lançamento” é parametrizar o lançamento a ser feito, informando se ele é um lançamento “A pagar” ou “A Receber”. Para os lançamentos de inscrição devem ser usados tipos de registro a “A Receber”. Ex: “Recebimento de Taxas”.

**Moeda -** Moeda corrente utilizada na geração dos boletos. Ex: “Real”.

**Histórico:** Informação textual que compõe o campo histórico dos lançamentos.

**Testar geração de lançamento -** Através deste recurso, é possível simular uma geração de lançamento para a inscrição, verificando se os parâmetros financeiros configurados são válidos, segundo as regras do Módulo Gestão Financeira. Após a simulação do lançamento, uma mensagem informará se a configuração é válida ou se houve algum erro, informando o motivo.

**Disponibilizar pagamento com Pix no portal** - Este parâmetro tem como objetivo, permitir que os candidatos do processo seletivo possam efetuar o pagamento da inscrição através do portal utilizando Pix. Para mais informações [clique aqui.](https://tdn.totvs.com/x/aVbuIw)

**Disponibilizar pagamento de cartão de crédito no portal** - Este parâmetro tem como objetivo, permitir que os candidatos do processo seletivo possam efetuar o pagamento da inscrição através do portal utilizando cartão de crédito. O pagamento ficará disponível nos serviços de Impressão após a inscrição do candidato e em 2ª via de boleto e será exibido um ícone, possibilitando ao usuário clicar na tela para informação dos dados de cartão de crédito, caso o processo seletivo esteja configurado. Caso contrário, será exibido somente o código IPTE do boleto e a opção de impressão do boleto. Pix. Para mais informações [clique aqui.](https://tdn.totvs.com/x/GD0xHQ)

* Importante: Para realizar o pagamento da inscrição via cartão de crédito é preciso que seja parametrizado no RM Fluxus as configurações do cartão de crédito.

**Gerar lançamentos /boletos com registro online** - Este parâmetro tem como objetivo permitir aos candidatos a impressão do boleto de inscrição registrado.

**Apresentar boleto de cobrança registrada ainda não registrado no Portal** - Este parâmetro tem como objetivo permitir que os boletos provenientes de convênios com cobrança registrada sejam impressos, mesmo que os boletos não tenham sido registrados.

Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar documentos.

**Campo “Filial do lançamento”** – Filial (Unidade Operacional) responsável pelos lançamentos.

Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar Documentos.  
Esse campo, fica visível após “salvar” todo o cadastro do processo seletivo.

**Campo “Departamento do lançamento”** - Departamento da filial (Unidade Operacional) responsável pelos lançamentos.  
**Campo “Centro de Custo”:** Identifica o centro de custo que é o responsável pela receita gerada com as inscrições.  
**Campo “Tipo Contábil**” - Define o status contábil do lançamento que será criado. As opções disponíveis são: “Não contábil”, “Contábil”, “Baixa contábil” e “A contabilizar”.  
**Campo “Evento Contábil de inclusão”** - Identifica o registro contábil que será gerado em decorrência do lançamento de inscrição.

**Campo “Tabelas opcionais”** - Permite que seja informado o valor para cada uma das tabelas opcionais que tenham sido parametrizadas para utilização no Módulo Gestão Financeira.  
**Campo: “Campos alfa”** - Permite que seja informado o valor para cada um dos campos alfanuméricos opcionais que tenham sido parametrizados para utilização no Módulo Gestão Financeira.  
Na opção “**Informações Financeiras - Pagamento de Profissionais - Cliente/Fornecedor”**, são definidos os parâmetros para geração dos lançamentos “A pagar”, que devem ser efetuados para pagamento dos fornecedores durante a execução do processo Gerar Pagamento de Profissionais.  
**Campo “Conta/Caixa”:** Identifica a conta corrente utilizada no processo de pagamento do fornecedor.  
**Campo “Pessoa Física/Pessoa Jurídica - Tipo de Documento”** - Deve ser selecionado um tipo de documento a partir da lista de “Tipos de Documento” disponível. Um tipo de documento, é um registro que armazena uma série de parâmetros que caracterizam um lançamento financeiro. Esse tipo de documento irá compor os lançamentos de pagamento dos fornecedores, logo, deve ser selecionado o tipo “A pagar”. A parametrização deste campo é diferenciada de acordo com o tipo de fornecedor: pessoa física ou jurídica. Ex: “NF RPA - RPA”.

 Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar Documentos.  
Campo “Pessoa Física/Jurídica - Código de Receita” - Deve ser preenchido se o respectivo “Tipo de Documento” possuir no Módulo Gestão Financeira, as classificações  
“Gerar IRRF” ou “Gerar IRRF e INSS”.

**Campo “Moeda”** - Moeda corrente que será utilizada na geração dos lançamentos de pagamento;

Se o código de receita não for preenchido e o tipo de documento é um tipo parametrizado para reter imposto de renda sobre o lançamento, o serviço de integração não fará o lançamento de pagamento, será gerado um erro.  
**Campo “Centro de custo”** - Identifica qual centro de custo é o responsável pela despesa gerada com o pagamento dos profissionais;  
**Campo “Histórico”** - Informação textual que compõe o campo histórico dos lançamentos;  
**Campo “Filial do lançamento”** - Filial (Unidade Operacional) responsável pelos lançamentos;  
**Campo “Departamento do lançamento”** - Departamento da Filial (Unidade Operacional) responsável pelos lançamentos;  
**Campo “Data do lançamento”** - Define a data dos lançamentos que são criados para pagamento dos profissionais;  
**Campo “Tipo Contábil”** - Define o status contábil do lançamento que é criado. As opções disponíveis são: “Não contábil”, “Contábil”, “Baixa contábil” e “A contabilizar”;  
**Campo “Evento Contábil”** - Identifica o registro contábil que é gerado em decorrência do lançamento de inscrição .  
**Campo “Tabelas opcionais”** - Permite que seja informado o valor para cada uma das tabelas opcionais que tenham sido parametrizadas para utilização no Módulo Gestão Financeira;  
**Campo “Campos alfa”** - Permite que seja informado valor para cada um dos campos alfanuméricos opcionais que tenham sido parametrizados para utilização no Módulo Gestão Financeira.

A aba “Teste de geração de lançamento” permite que as configurações feitas para geração de lançamento de pagamento de profissionais sejam testadas. Ao clicar em “Testar geração de lançamento”, o Sistema realiza uma simulação de inclusão de lançamento a pagar conforme a parametrização feita nas abas anteriores, sendo necessário informar um “Cliente/Fornecedor” (Pessoa Física ou Jurídica) no campo correspondente.

**Conta/Caixa:** Identifica a conta corrente utilizada no processo de pagamento do fornecedor.

**Pessoa Física/Pessoa Jurídica - Tipo de Documento** - Deve ser selecionado um tipo de documento a partir da lista de “Tipos de Documento” disponível. Um tipo de documento, é um registro que armazena uma série de parâmetros que caracterizam um lançamento financeiro. Esse tipo de documento irá compor os lançamentos de pagamento dos fornecedores, logo, deve ser selecionado o tipo “A pagar”. A parametrização deste campo é diferenciada de acordo com o tipo de fornecedor: pessoa física ou jurídica. Ex: “NF RPA - RPA”.

Os tipos de documentos tratados aqui não devem ser confundidos com os tipos de documentos presentes na tabela auxiliar [Documentos](#Tabela_Auxiliar_Documentos).

**Pessoa Física/Jurídica - Código de Receita -** Deve ser preenchido se o respectivo “Tipo de Documento” possuir no Módulo Gestão Financeira, as classificações “Gerar IRRF” ou “Gerar IRRF e INSS”.

Se o código de receita não for preenchido e o tipo de documento é um tipo parametrizado para reter imposto de renda sobre o lançamento, o serviço de integração não fará o lançamento de pagamento, será gerado um erro.

**Moeda** - Moeda corrente que será utilizada na geração dos lançamentos de pagamento;

**Centro de custo** - Identifica qual centro de custo é o responsável pela despesa gerada com o pagamento dos profissionais;

**Histórico** - Informação textual que compõe o campo histórico dos lançamentos;

**Filial do lançamento** - Filial (Unidade Operacional) responsável pelos lançamentos;

**Departamento do lançamento** - Departamento da Filial (Unidade Operacional) responsável pelos lançamentos;

**Data do lançamento** - Define a data dos lançamentos que são criados para pagamento dos profissionais;

**Tipo Contábil** - Define o status contábil do lançamento que é criado. As opções disponíveis são: “Não contábil”, “Contábil”, “Baixa contábil” e “A contabilizar”;

**Evento Contábil** - Identifica o registro contábil que é gerado em decorrência do lançamento de inscrição.

**Tabelas opcionais -** Permite que seja informado o valor para cada uma das tabelas opcionais que tenham sido parametrizadas para utilização no Módulo Gestão Financeira;

**Campos alfa** - Permite que seja informado valor para cada um dos campos alfanuméricos opcionais que tenham sido parametrizados para utilização no Módulo Gestão Financeira.

A aba “Teste de geração de lançamento” permite que as configurações feitas para geração de lançamento de pagamento de profissionais sejam testadas. Ao clicar em “Testar geração de lançamento”, o Sistema realiza uma simulação de inclusão de lançamento a pagar conforme a parametrização feita nas abas anteriores, sendo necessário informar um “Cliente/Fornecedor” (Pessoa Física ou Jurídica) no campo correspondente.

# Forma de inscrição

Caminho: **Módulo Educacional> Processo Seletivo > Cadastro > Processo Seletivo > Aba: Forma de inscrição**

**Data do início/Data do término** - Define o período no qual o Sistema permite que sejam realizadas as inscrições do tipo. Quando o período definido expirar, o Sistema deixa de exibir essa forma inscrição tanto do formulário de inscrição Web (Portal) como via Sistema;

**Número de dias para vencimento** - Permite que seja especificado dentro de quantos dias o boleto de inscrição deve vencer a partir da sua emissão;

**Data limite de vencimento** - Limita o parâmetro “Número de dias para vencimento”, fixando uma data máxima para o vencimento. Isso possibilita que seja dado um prazo para que o candidato efetue o pagamento do boleto desde que esse prazo não extrapole determinada data. Por exemplo, pode ser definido que o boleto vencerá dentro de um período de quatro dias após a emissão, porém a sua data de vencimento não poderá extrapolar o término do período de inscrições;

**% Desconto** - Permite que seja configurado um valor de desconto para as inscrições feitas dentro da forma que está sendo criada. Quando for feita uma inscrição desse tipo, o desconto deve ser aplicado com este percentual sobre o valor da taxa de inscrição da área de interesse escolhida. Por exemplo, se for informado para este campo um valor de 50% e o candidato se inscrever em uma área cuja taxa de inscrição seja de R$60,00, o boleto será gerado para ele com o valor de R$30,00;

**Indicação de aluno** - Se esta opção for marcada, quando for feita uma inscrição, seja via Web (Portal) ou Sistema, pode ser informado o número de registro do aluno que estuda na instituição e indicou o Processo Seletivo para o candidato;

**Indicação de funcionário/professor** - Se esta opção for marcada, quando for feita uma inscrição, seja via Web (Portal) ou Sistema, pode ser informada a chapa do funcionário/professor que trabalha na instituição e indicou o Processo Seletivo para o candidato;

**Indicação de cliente/fornecedor** - Se esta opção for marcada, quando for feita uma inscrição, seja via Web (Portal) ou Sistema, pode ser informado o número de registro de algum cliente/fornecedor da instituição que tenha indicado o Processo Seletivo para o candidato.

**Disponível na Internet** - Se essa opção estiver marcada os candidatos podem optar por ela ao se inscreverem pelo Portal.

Todas as formas de inscrição estão disponíveis via Sistema independentemente dessa opção estar ou não marcada.

**Obrigatório ENEM** - Se essa opção estiver marcada e a área ofertada permitir utilizar o ENEM, é obrigatório o preenchimento dos parâmetros de ENEM (Número de inscrição e Ano de referência). Se essa opção estiver marcada e a área ofertada não permitir, o Sistema não deixará concluir a inscrição, solicitando a troca da forma de inscrição.

# Área de interesse ofertada

Nesta opção é detalhado o cadastro do “Processo seletivo”, sendo possível incluir e alterar a configuração das áreas de interesse ofertadas.

Compreende as informações adicionais relevantes na definição de uma área de interesse ofertada.

**Idiomas Oferecidos** - Nº Máximo e Nº Mínimo - Definem a quantidade mínima e máxima de idiomas que um candidato pode escolher caso defina esta área de interesse como sua primeira opção;

**Incide desconto** - Se estiver marcada, as configurações de desconto que forem parametrizadas na forma de inscrição escolhida serão aplicadas. Se não estiver marcada, a taxa de inscrição definida na guia identificação será cobrada integralmente independente da forma de inscrição escolhida;

**Utiliza ENEM** - Se esta opção estiver marcada, a nota de ENEM do candidato, quando for de sua vontade, será utilizada na classificação. A utilização de ENEM também impacta no serviço de inscrição do Portal, caso esteja marcada, estará disponível para preenchimento;

**Utiliza controle de faixa etária** - Permite que seja definida uma faixa etária para limitar a idade dos candidatos que podem se inscrever na área. Quando for marcado, os campos idade mínima e máxima serão habilitados para a entrada. Nesse caso a idade máxima deve ser maior que a idade mínima;

**Fórmula para cálculo de pontuação** - Permite que seja definida uma fórmula para ser aplicada no cálculo da pontuação durante o processo de classificação. Sempre que este campo estiver preenchido, a fórmula indicada será utilizada no lugar do cálculo padrão do Sistema.

Esta aba possui um único campo utilizado para configuração da conta/caixa que deve ser informada na geração do lançamento no momento da inscrição. A conta/caixa, de maneira geral, consiste nas informações referentes à conta, agência e banco que receberão as movimentações financeiras geradas nas inscrições do Processo Seletivo.

Esse campo é opcional na área de interesse ofertada. Caso não seja preenchido, o Sistema utilizará a informação cadastrada na conta caixa, localizada nas informações financeiras do Processo Seletivo.

O botão “**Testar geração de lançamento**” é similar ao encontrado no cadastro de Processo Seletivo, no qual, realiza um teste de geração de lançamento com as informações financeiras cadastradas no Processo Seletivo, substituindo a conta/caixa caso esta esteja cadastrada na área ofertada. Caso não exista conta/caixa configurada na área ofertada, o teste será idêntico ao encontrado no Processo Seletivo daquela área ofertada.

# Baixa manual do boleto de inscrição

**Caminho: TOTVS Processo Seletivo| Selecionar o Processo Seletivo desejado| Anexo>Candidato Inscrito>**

Selecionar o aluno que terá a taxa baixada manualmente, clicar na aba Inf. complementares

Clicar no número do lançamento, (você será direcionado para o Módulo do Backoffice: Financeiro) neste momento o usuário deverá seguir a baixa do lançamento;

Clicar em **Processo>Baixa>Baixa de Lançamentos**, abrirá a tela de assistente de baixa de lançamentos Financeiros. (Neste momento o DR deve agir de acordo com as orientações do Financeiro e Contabilidade da unidade.
