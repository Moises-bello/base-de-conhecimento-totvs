---
content_hash: e54766344aba00d7df287a05940803cbf3e81a4d94816ee7a2d44e6512b941c1
fetched_at: '2026-06-29T00:10:01.516810+00:00'
page_id: '452718759'
product: rm
source: tdn-rm
title: Reembolso da Operadora de Assistência à Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718759
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Versões**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Nesta tela, você pode registrar os reembolsos pagos aos funcionários pela Operadora de Saúde.

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2302.231
* 12.1.2306.177
* 12.1.2310.112 e superiores

## **03. EXEMPLO DE UTILIZAÇÃO**

11Parametrização Parametrização 

1) Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em Acesso a Menus e permita o acesso **09.01.02.03 - Reembolso da Operadora de Assistência à Saúde**

2Cadastro - Reembolso Plano de SaúdeCadastro - Reembolso Plano de Saúde 

Acesse o  menu Anuais | DIRF/Informe de Rendimentos | Reembolso da Operadora de Assistência à Saúde

Nesse menu é possível visualizar todos os cadastros de reembolso realizados para os seus funcionários, bem como inserir manualmente os dados do reembolso do Plano de Saúde. Para adicionar um novo registro, clique na opção "Incluir".

**Aba Identificação**

Nesta tela deverá informar os seguintes campos:

* Indicativo da Origem do Reembolso (usado para o eSocial)
* Código da Operadora
* Número da chapa do funcionário
* Dependentes (caso existam)
* Evento
* Entidade (Prestador de Serviço)
* Ano Base
* Valor Ano Atual
* Valor Ano Anterior (caso aplicável)

**Atenção:**

1. 1. Os valores da aba "Valores Mensais" serão somados para uso no XML do eSocial versão 1.2
   2. Os valores da aba "Valores Mensais" serão considerados para a geração da DIRF.
   3. O campo "Operadora" é obrigatório, uma vez que este cadastro é utilizado tanto para o eSocial quanto para a DIRF. Na DIRF, é obrigatório o CNPJ da operadora. Porém na geração do XML do evento S-1210, foi tratado de modo a não incluir a tag <regANS> quando o indicativo da origem do reembolso tag <IndOrgReemb> for igual a "2".

**Aba Valores Mensais**

Nesta tela, você deverá fornecer detalhes dos valores mensais. O sistema realizará automaticamente a soma dos valores inseridos nesta aba e substituirá os campos "Valor Ano Atual" e "Valor Ano Anterior" com a soma dos valores mensais na aba de Identificação.

3Funcionário - Histórico de Reembolso Plano de SaúdeFuncionário - Histórico de Reembolso Plano de Saúde

Acesse o  menu Administração de Pessoal | Funcionários | Anexo | Movimento | Reembolso da Operadora de Saúde

Neste menu, é possível visualizar os registros de reembolsos feitos para seus funcionários, bem como inserir manualmente os dados do reembolso do Plano de Saúde. Você pode adicionar um novo registro clicando na opção "Incluir".

**Aba Identificação** 

Nesta tela deverá informar os seguintes campos:

* Indicativo da Origem do Reembolso (usado para o eSocial)
* Código da Operadora
* Número da chapa do funcionário
* Dependentes (caso existam)
* Evento
* Entidade (Prestador de Serviço)
* Ano Base
* Valor Ano Atual
* Valor Ano Anterior (caso aplicável)

**Atenção:**

1. 1. Os valores da aba "Valores Mensais" serão somados para uso no XML do eSocial versão 1.2
   2. Os valores da aba "Valores Mensais" serão considerados para a geração da DIRF.

**Aba Valores Mensais**

Nesta tela é necessário fornecer os detalhes dos valores mensais. O sistema realizará automaticamente a soma dos valores inseridos nesta aba e substituirá os campos "Valor Ano Atual" e "Valor Ano Anterior" com a soma dos valores dos meses na aba de **Identificação**.

4Atualização de dados - Reembolso do Plano de Saúde - AnualAtualização de dados - Reembolso do Plano de Saúde - Anual

Acesse o  menu Anuais | DIRF/Informe de Rendimentos | Informe de Rendimentos | Atualizar dados da DIRF | Reembolso do Plano de Saúde

Através desta opção, o sistema irá relacionar todos os funcionários com base no código do evento especificado, incluindo o valor total referente ao desconto ao longo do ano e período de competência indicado.

O usuário realizará a distribuição manual de acordo com a operadora, o prestador, o titular e os dependentes, caso haja reembolso.

**PONTOS IMPORTANTES:**

* Ao inserir o código do evento e clicar em "Carregar", o sistema exibirá todos os funcionários que receberam o evento em sua ficha financeira durante o ano e o período de competência especificado.
* Ao lado do nome de cada funcionário, no campo direito da tela, o sistema exibirá o valor total do reembolso durante o ano.
* Deverá fornecer o código da operadora relacionado ao Reembolso, mesmo quando o **Indicativo da origem do reembolso** for igual á "**2- Reembolso efetuado pelo empregador como benefício do próprio empregador",** uma vez que este cadastro é utilizado tanto para o eSocial quanto para a DIRF. Na DIRF, é obrigatório o CNPJ da operadora. Porém na geração do XML do evento S-1210, foi tratado de modo a não incluir a tag <regANS> quando o indicativo da origem do reembolso tag <IndOrgReemb> for igual a "2".
* Informe a Entidade (Prestador de Serviço) para a qual o funcionário realizou a consulta particular (nome do médico ou clínica).
* Indique se o valor se refere ao funcionário e/ou a seu dependente.
* Forneça o Reembolso Anual atual.
* Forneça o Reembolso do Ano Anterior se aplicável, por exemplo, se o funcionário consultou em 2016 e recebeu o reembolso em 2017.
* Se o valor a ser distribuído for somente para o titular, marque a opção "Lançamento para o titular" e preencha os campos de valores conforme necessário. Em seguida, clique em "Incluir/Atualizar".
* Se o reembolso for para o dependente, informe o nome do dependente e o valor correspondente. Clique em "Incluir/Atualizar".
* O campo "Incluir/Atualizar" deve ser marcado sempre que um valor for inserido, tanto para o dependente quanto para o titular.
* Ao adicionar o valor restante para o Titular, o sistema reconhecerá que o valor restante será atribuído ao Titular.
* Certifique-se de adicionar os valores até que o campo "Valor não distribuído" esteja igual a "0,00".

**ATENÇÃO:**

Caso não tenha concluído os lançamentos de todos os funcionários, haverá uma opção para "Visualizar apenas registros com valor não distribuído". Ao selecionar essa opção, o sistema mostrará apenas os funcionários que ainda não tiveram o valor distribuído para o titular e/ou dependentes.

true5 Atualização Reembolso Despesas Médicas MensaisAtualização Reembolso Despesas Médicas Mensais

Acesse o  menu eSocial | Operadora Saúde | Atualização Reembolso Despesas Médicas Mensais

Através desta opção, o sistema irá relacionar todos os funcionários com base no código do evento informado, apresentando o valor total do desconto correspondente ao mês e ano registrados no caixa.

A distribuição deve ser realizada manualmente, levando em consideração a operadora, o prestador, o titular e os dependentes, no caso de reembolso.

Nesta tela, selecione o mês e o ano desejados.

Para inserir um novo basta clicar em incluir.

**PONTOS IMPORTANTES:**

* Ao inserir o código do evento e clicar em "Carregar", o sistema exibirá todos os funcionários que receberam o evento em sua ficha financeira durante o ano e o período de competência especificado.
* Ao lado do nome de cada funcionário, no campo direito da tela, o sistema exibirá o valor total do reembolso durante o ano.
* Deverá fornecer o código da operadora relacionado ao Reembolso.
* Informe a Entidade (Prestador de Serviço) para a qual o funcionário realizou a consulta particular (nome do médico ou clínica).
* Indique se o valor se refere ao funcionário e/ou a seu dependente.
* Forneça o Reembolso Anual atual.
* Forneça o Reembolso do Ano Anterior se aplicável, por exemplo, se o funcionário consultou em 2016 e recebeu o reembolso em 2017.
* Se o valor a ser distribuído for somente para o titular, marque a opção "Lançamento para o titular" e preencha os campos de valores conforme necessário. Em seguida, clique em "Incluir/Atualizar".
* Se o reembolso for para o dependente, informe o nome do dependente e o valor correspondente. Clique em "Incluir/Atualizar".
* O campo "Incluir/Atualizar" deve ser marcado sempre que um valor for inserido, tanto para o dependente quanto para o titular.
* Ao adicionar o valor restante para o Titular, o sistema reconhecerá que o valor restante será atribuído ao Titular.
* Certifique-se de adicionar os valores até que o campo "Valor não distribuído" esteja igual a "0,00".

**ATENÇÃO:**

Caso não tenha concluído os lançamentos de todos os funcionários, haverá uma opção para "Visualizar apenas registros com valor não distribuído". Ao selecionar essa opção, o sistema mostrará apenas os funcionários que ainda não tiveram o valor distribuído para o titular e/ou dependentes.

6Operadora de Saúde - Histórico de Reembolso Plano de SaúdeOperadora de Saúde - Histórico de Reembolso Plano de Saúde

Acesse o menu eSocial | Operadoras de Saúde | Cadastro de Operadoras de Saúde | Anexos | Reembolso da Operadora de Assistência à Saúde

Nesta aba, você pode visualizar todos os registros de reembolso feitos para os seus funcionários vinculados à operadora de saúde selecionada, bem como inserir manualmente os dados do reembolso do Plano de Saúde para a operadora em edição.

**Aba Identificação**

Nesta tela deverá informar os seguintes campos:

* Indicativo da Origem do Reembolso (usado para o eSocial)
* Código da Operadora
* Número da chapa do funcionário
* Dependentes (caso existam)
* Evento
* Entidade (Prestador de Serviço)
* Ano Base
* Valor Ano Atual
* Valor Ano Anterior (caso aplicável)

**Atenção:**

1. 1. Os valores da aba "Valores Mensais" serão somados para uso no XML do eSocial versão 1.2
   2. Os valores da aba "Valores Mensais" serão considerados para a geração da DIRF.

**Aba Valores Mensais**

Nesta tela, é necessário inserir o detalhamento dos valores por mês. O sistema automaticamente realizará a soma dos valores digitados nesta seção e substituirá os campos de "Valor Ano Atual" e "Valor Ano Anterior" pela soma dos meses na Aba de Identificação.

## **03. TABELAS UTILIZADAS**

PFREEMBOLSOOPERADORA, PFREEMBOLSOOPERADORAMENSAL

## **04. Informações Complementares**

Operadoras de Saúde

---
