---
content_hash: bbd28be6a8997a5b44f2fa02637769fd999cb6db77e5886c81585c14c12cf258
fetched_at: '2026-06-29T00:10:59.817645+00:00'
page_id: '616504287'
product: rm
source: tdn-rm
title: Mudança de Categoria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=616504287
version: 17
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configuração de parâmetros**
3. **Campos Obrigatórios**
4. **Validações**
5. **Exemplo de utilização**
   1. **Mudança Convênio/Plano/Subplano**
   2. **Mudança Unidade Atendimento/Faturamento**
   3. **Tabelas utilizadas**

sumarioVisão Geral

**01. VISÃO GERAL**

Esta implementação possibilita o controle na alteração do convênio, plano e subplano ou  da unidade de atendimento e faturamento, de um atendimento com base no perfil de acesso do usuário.

Atenção! Realizamos uma melhoria durante migração da rotina

 Durante a migração da rotina de Mudança de Categoria, foi realizada uma melhoria nos lançamentos de "Honorários" e "DTSs".

A rotina da nova MDI possui o seguinte comportamento:

* Quando a rotina não encontra a configuração de preço no convênio de destino para "Honorário", "DTS", o sistema irá estornar o item e criar uma mensagem de pendência na Parcial".

**Dessa forma, fica sob responsabilidade do Faturista o tratamento mais adequado aos lançamentos na parcial que não puderam ser precificados, se deverá realizar a configuração do preço do item ou manter o seu estorno. Para mais informações, consultar nossa documentação da rotina [Pendências na Conta](https://tdn.totvs.com/pages/viewpage.action?pageId=738951527).**

A rotina da MDI antiga possuía o seguinte comportamento:

* A rotina NÃO permitia a mudança quando não encontrava a configuração de preço no convênio de destino para "MATMED".
* A rotina ESTORNAVA o lançamento de forma sumária quando não encontrava a configuração de preço no convênio de destino para "Honorário" e "DTS" e os informava em um relatório ao término do processamento no quadro "Lançamentos não transferido para nova categoria".

A melhoria ocorreu por conta dos seguintes problemas identificados na rotina antiga e reportados por diversos clientes, sendo elas:

1. Os lançamentos ESTORNADOS pela rotina da Mudança de Categoria se misturavam com os demais itens que de FATO foram estornados na conta.
2. Os lançamentos estornados só eram exibidos no relatório ao término do processamento da rotina e se o mesmo NÃO fosse salvo ou impresso, perdiam-se as informações.
3. O setor que realizou a mudança não informar quais estornos foram realizados para o setor do Faturamento.
4. **A falta da inclusão dos itens estornados para correta cobrança gerava prejuízo financeiro ao Hospital.**
Configuração de Parâmetros

## **02. CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse **Serviços Globais/ Segurança / Perfis**.
2. Selecione um perfil.
3. Acesse**Anexos / Parâmetros RM Saúde**.
4. Acesse a aba**Geral 2**.
5. O controle de mudança de categoria por perfil realiza as mudança com base na origem da categoria do registro e no destino da categoria desejada, conforme as seguintes configurações:
   1. Origem:
      1. Ambos: Os registros selecionados para realizar a mudança podem ser tanto da categoria Convênio como Particular.
      2. Convênio: Os registros selecionados para realizar a mudança podem ser apenas da categoria Convênio.
      3. Particular: Os registros selecionados para realizar a mudança podem ser apenas da categoria Particular.
   2. Destino:
      1. Ambos: A nova categoria selecionada para a mudança do registro pode ser tanto Convênio como Particular.
      2. Convênio: A nova categoria selecionada para a mudança do registro pode ser apenas do tipo Convênio.
      3. Particular: A nova categoria selecionada para a mudança do registro pode ser apenas do tipo Particular.

## 

Campos Obrigatórios

## **03. CAMPOS OBRIGATÓRIOS**

Os campos de preenchimento obrigatório são:

* Atendimento
* Selecionar pelo menos uma parcial
* Mudança de convênio
  + Convênio e plano
* Mudança de unidade
  + Unidade de atendimento e faturamento

Verificações:

* Não exibir parciais: liberada, cancelada ou já faturada.
* Convenio: Não será exibido convênios que não estejam de acordo com o perfil do usuário.

1. O comportamento desta funcionalidade irá variar conforme parametrização realizada conforme a sessão **CONFIGURAÇÃO DE PARÂMETROS**.
2. Neste exemplo a parametrização segue as configurações abaixo:

Validações

## **04. VALIDAÇÕES**

* Mudança de categoria/plano/subplano

* + Convênio não pode estar bloqueado.
  + Plano não pode estar bloqueado.
  + Subplano não pode estar bloqueado.
  + Nova Categoria deve ser diferente a Categoria Atual.

* Unidade Faturamento/atendimento

* + Nova Unidade de Atendimento deve ser diferente da atual.
  + Parcial com NF já emitida.
  + Não existem condições contratuais para essa unidade de faturamento.
  + A unidade de atendimento de destino não realiza classificação de risco.

* Ambos:

* + A atendimento não pode possuir parciais com NF já emitida.
  + Convênio não credenciado ao prestador principal.
  + Convênio informado não está cadastrado ou está inativo.
  + O Plano não está definido no convênio.
  + O Subplano não está cadastrado.
  + Atendimento informado para mudança de categoria não existe.
  + Existirem itens de débito selecionados que já foram liberados.
Exemplos de Utilização

## **05. EXEMPLOS DE UTILIZAÇÃO**

No menu Atendimento > Internação > Outros > Mudança de Categoria

ou  Faturamento > Particular e Convênios > Outros > Mudança de Categoria

Deverá ser escolhido:

* Um tipo de mudança:
  + Categoria/Plano/Subplano
  + Unidade Atendimento/ Faturamento
* Um atendimento, em seguida selecionar a parcial inicial que sofrerá alteração, sendo que todas as parciais posteriores também serão alteradas.

**a. Mudança Categoria/Plano/ Subplano**

Clique no botão avançar:

* Informe pelo menos o Convênio e Plano
* O subplano, só será exibido se existir para plano selecionado.

**b.  Mudança Unidade Atendimento/ Faturamento**

Clique no botão avançar:

* Informe a Unidade de Atendimento e Faturamento.

Clique no botão avançar para executar o processo, se o processo for executado com sucesso será exibido a tela abaixo com os passos da alteração.

Após a mudança o sistema irá:

* Recalcular os itens do grupo de gastos.
* Alterar os dados da mudança de categoria no atendimento de forem alteradas todas as parciais.
* Se o atendimento vier de um agendamento será alterado também na tela de agendamento os dados da mudança de categoria.

Tabelas UtilizadasTabelas

## **06. TABELAS UTILIZADAS**

* SZAGENDAMENTO
* SZATENDIMENTO
* SZPARCIALATEND
* SZSENHACLASSIF
* SZCLASSIFICACAORISCO
* SZAPAC
* SZSUSBPALANC
* SZSUSAIHPROD
* SZCONTROLREPASSE
* SZATENDHONORARIO
* SZATENDDIARIAS
* SZATENDTAXASERV
* SZATENDMATMED
* SZATENDSADT
* SZATENDGASTOPARTIC
