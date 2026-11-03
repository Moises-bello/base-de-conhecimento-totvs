---
content_hash: b0cb9be424dda648859745b25ba446fa0963a55ac56a6f32613a512a5e79fae8
fetched_at: '2026-06-29T00:11:33.233144+00:00'
page_id: '754617576'
product: rm
source: tdn-rm
title: Processo de Previsão de Alta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=754617576
version: 17
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Processo de Previsão de Alta**
3. **Tela Processo de Previsão de Alta**
4. **Permissão por Perfil**
5. **Parâmetro por Perfil**

sumarioVisão Geral

## **01. VISÃO GERAL**

A alta é a finalização do período de internação que ocorre pela melhora do estado do paciente ou óbito. Outros motivos podem gerar a alta hospitalar, como a alta a pedido pelo paciente ou responsável (desistência do tratamento), a necessidade de transferência para um hospital especializado e a evasão hospitalar. Essa rotina é responsável pelo registro da alta administrativa do paciente, onde é possível registrar algumas informações como Data/Hora de Saída, Motivo da Alta, Data e Hora do Óbito, destino do paciente em caso de alta, CID de Internação e CID de Alta.

Nessa rotina, além da alta do paciente, é possível cancelar ou ajustar informações de uma alta registrada.

Processo de Previsão de Alta

## **02. PROCESSO DE PREVISÃO DE ALTA**

* Neste tela é possível controlar a previsão de alta do paciente. É possível incluir uma previsão de alta, alterar a data de previsão ou cancelar a previsão de alta do paciente;
* Além da permissão por perfil do usuário, também faz necessário configurar o parâmetro "Criar processo de alta" em parâmetro RM Saúde por perfil;
* Também é possível criar uma comunicação de alta de forma automática, bastando ativar o parâmetro "Recebe comunicação de processo de alta" em "Parâmetro por Perfil" e sempre que for criado, alterado ou cancelado um processo de previsão de alta, o mesmo acontecerá com a comunicação de alta;

**Para incluir um processo de previsão de alta, se faz necessário:**

* + Ter permissão por perfil de incluir;
  + O parâmetro "Criar processo de alta" por perfil deve estar ativo;
  + Após clicar no botão "+"  e abrir a tela, informe a data de previsão e click no botão "..." para selecionar o paciente que terá alta.

**Para alterar uma data previsão de alta, se faz necessário:**

* + Ter permissão por perfil de editar;
  + O parâmetro "Criar processo de alta" por perfil deve estar ativo;
  + O processo de previsão de alta deve estar com status em aberto;
  + Basta selecionar o processo de previsão de alta que deseja alterar a data de previsão e clicar no botão "editar" ou clicar 2x. Neste caso só é possível alterar a data de previsão, não é permitido alterar o paciente;

**Para cancelar uma data previsão de alta, se faz necessário:**

* + Ter permissão por perfil de excluir;
  + O parâmetro "Criar processo de alta" por perfil deve estar ativo;
  + O processo de previsão de alta deve estar com status em aberto;
  + Basta selecionar o processo de previsão de alta que deseja cancelar clicar no botão "x". Neste caso só é possível cancelar, não é possível excluir definitivamente o registro;
Permissão por perfil

## **03. PERMISSÃO POR PERFIL**

**Para definir a permissão por perfil do processo de previsão de alta:**

* + Acesse a opção Serviços Globais => Segurança => Perfis;
  + Em acesso a menus, vá até Hospitais e Clinicas => Atendimento = Processo de Previsão de Alta.

Parâmetros por perfil

## **04. PARÂMETRO POR PERFIL**

**Para definir o parâmetro criar processo de alta:**

* + Acesse a opção Serviços Globais => Segurança => Perfis;
  + No menu em Anexos => Parâmetros RM Saúde.

**Para definir o parâmetro recebe comunicação de processo de alta:**

* + Acesse a opção Serviços Globais => Segurança => Perfis;
  + No menu em Anexos => Parâmetros RM Saúde.
