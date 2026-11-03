---
content_hash: 345a18fa9ebaebb23828c17c7b204d94ea3911b92ee7c11e3d51fb253cb7ddbd
fetched_at: '2026-06-29T00:10:35.694441+00:00'
page_id: '531028670'
product: rm
source: tdn-rm
title: Leitos
type: documentation
url: https://tdn.totvs.com/display/LRM/Leitos
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Telas utilizadas**

sumarioVisão Geral

## **01. VISÃO GERAL**

Nesta funcionalidade devem ser cadastrados todos os leitos existentes no Hospital, vinculando cada um deles com a respectiva Diária constante na Tabela de Diárias, Taxas e Serviços Padrão (que vem pré-carregada na instalação do Sistema) e ao Centro de Custo/Resultado (previamente cadastrados), relacionado com o leito.

## **02. EXEMPLO DE UTILIZAÇÃO**

Na funcionalidade ainda, será permitido Ativar e Inativar um leito através do botão "Ativar/Inativar".Se o leito estiver ocupado, o mesmo não poderá ser inativado até que esteja desocupado.O mesmo ocorrerá quando o leito possui outros leitos associados a ele. Ao desativar o leito principal, todos esses leitos associados a ele serão automaticamente inativados. Com esta nova situação do leito, o leito que estiver inativo não aparecerá nas telas de seleção, até que seja ativado novamente.

Telas Utilizadas

## **03. TELAS UTILIZADAS**

* No TOTVS Gestão Hospitalar acesse o menu**Cadastros> Registro e Controle> Leitos**para cadastrar um leito.

* Clique no ícone de **Novo** para cadastrar novo leito.

* Preencha todos os campos a seguir. Se atente ao campo **Número do Leito** pois é obrigatório o preenchimento e é o identificador do leito, também o status para Internação.

* Determine o tipo de acomodação deste leito para fins de controle e custo clicando nos **"..."** do campo **Classes de Leitos.**

* No campo **Cód. Centro de Custo** clique nos **"..."** e selecione a unidade de faturamento que deseja vincular e clique em OK.

* Essa gade preencha para fins de faturamento, caso não seja SUS deixar em branco. Selecione a **Unidade de Atendimento** clicando nos "..." e clique em **Salvar / OK**.

* Leito cadastrado, estará disponível para vinculo com paciente.

Processos

## **04. PROCESSOS**

Acerta Leito

## **04.1 ACERTA SITUCAÇÃO DOS LEITOS**

**Ambiente**

TOTVS Gestão Hospitalar 12.1.2506 e superiores.

A rotina Acerta Situação dos Leitos realiza a **verificação dos leitos,** caso seja encontrada alguma inconsistência realiza a correção.

Algumas das inconsistências que podem ser encontradas e corrigidas são:

* Um paciente recebeu alta, mas o leito continua constando como ocupado pelo paciente;
* Foi realizada a internação de um paciente, mas o leito continua constando como livre;

Para executar a rotina, realize os passos a seguir:

1. No**TOTVS Gestão Hospitalar**acesse **Cadastros** **> Registro e Controle > Leitos > Processos > Acerta leitos.**

Obs.

O processo de acerta leito afeterá leitos selecionados na tela, caso não seja selecionado nenhum leito, o processo será aplicado para todos os leitos cadastrados.
