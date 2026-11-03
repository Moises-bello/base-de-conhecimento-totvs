---
content_hash: 348a20ccb6481936b07f95362c62bad89db8ad696cc18008f5c0e0204324a2bf
fetched_at: '2026-06-29T00:10:35.652038+00:00'
page_id: '531024003'
product: rm
source: tdn-rm
title: Elaboração de AIH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=531024003
version: 22
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Obstetrícia - Elaboração de AIH**
4. **Procedimentos - Elaboração de AIH**
5. **Mensagens de Erro**
6. **Rejeitar AIH/ Reverter AIH Rejeitada**
7. **CNES**
8. **Doc do Recebedor**

sumarioVisão Geral

## **01. VISÃO GERAL**

Nesta tela são exibidas as contas de AIHs geradas para os pacientes com cobrança de AIHs. As contas são exibidas de acordo com o status selecionado. 

## 

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Os status da AIH podem ser:

* AIHs Rejeitadas  
  Selecionado este status serão exibidas as AIHs que foram rejeitadas
* Em Elaboração  
  Selecionado este status serão exibidas as AIHs que estão em elaboração.
* Faturada  
  Serão exibidas as AIH's faturadas.
* Liberada  
  Serão exibidas as AIH's liberadas para faturamento.

Identificação - Elaboração de AIH

Identificação - Elaboração de AIH

* Nº AIH  
  Campo deverá ser preenchido com o número da AIH, esta informação é obrigatória na Liberação da conta.
* Data da Emissão  
  Campo deverá ser preenchido com a data da emissão da AIH.
* Procedimento Solicitado  
  Campo deverá ser preenchido com o código do procedimento inicial do paciente, constante do laudo médico para internação.   
  Caso esta informação seja registrada no momento da Internação do Paciente, em Informações Específicas SUS, este campo será preenchido automaticamente.
* Especialidade  
  Campo deverá ser preenchido com a especialidade em que o paciente está sendo internado.
* Caráter Atendimento  
  Campo deverá ser preenchido com o Tipo de Internação, por exemplo: Eletiva, Urgência, etc. Caso, em Informações Específicas SUS,   
  esta informação seja registrada no momento da Internação do Paciente, este campo será preenchido automaticamente.
* CID Diag Principal  
  Campo obrigatório que deverá ser preenchido com o código do CID principal do Paciente.
* Motivo Saída / Permanência  
  Campo deverá ser preenchido com o Motivo da Alta do Paciente. Exemplo: Alta Curado, Óbito e etc.  
  Quando o Motivo de Alta for 61, 62, 63, 64, 65, 66, 67 e 68, o Sistema exigirá os campos Nº AIH Posterior e Nº AIH Anterior.
* № AIH Anterior  
  Campo deverá ser preenchido quando o paciente possuir mais de uma AIH na mesma internação. Neste caso, informar o número da AIH Anterior a que está sendo preenchida. Em casos de RN retido, (motivo cobrança 7...), na AIH do RN, informar o número da AIH da mãe.
* № AIH Posterior  
  Campo deverá ser preenchido quando o paciente possuir mais de uma AIH na mesma internação. Neste caso, informar o número da AIH posterior a que está sendo preenchida. Em casos de RN retido, (motivo cobrança 7...), na AIH da mãe, informar o número da AIH do RN.
* Pessoa em situação de rua

O Campo será marcado com Sim ou Não

Fonte de Recurso

* Fonte Orçamentária

O Campo poderá ser preenchido com os valores da lista

* + 01-MOD.1 - SERVIÇO DE SAÚDE DA AES
  + 02-MOD.2 - EQUIPE VOLANTES DA AES
  + 03-CRÉDITO FINANCEIRO P. VENCIDAS E VINCENDAS
  + 04-CRÉDITO FINANCEIRO-TRANSAÇÃO TRIBUTÁRIAIdentificação Nacional de Equipe

* Identificação Nacional de Equipe

O Campo poderá ser apenas por  Números

Complemento - Elaboração de AIH

Complemento - Elaboração de AIH

* CID Diag Secundário  
  Campo que deverá ser preenchido com o código do CID secundário do Paciente.
* CID Associado  
  Campo que deverá ser preenchido com o código do CID associado ao procedimento em questão.
* Raça\Cor

Na tela de Elaboração de AIH, antes de salvar o registro, não permitindo que seja informada a opção "99 - Sem informação" no campo Raça/Cor.

Obstetrícia - Elaboração de AIH

## **03. OBSTETRÍCIA - ELABORAÇÃO DE AIH**

Resumo do Evento

* Pré - Natal  
  Campo deverá ser preenchido com o número de pré-natais realizados.
* Nascimentos
  + Vivos  
    Campo deverá ser preenchido com o número de RN Vivos.
  + Mortos  
    Campo deverá ser preenchido com o número de RN Mortos.
* Saídas
  + Alta  
    Campo deverá ser preenchido com o número de RN que receberam Altas.
  + Transf.  
    Campo deverá ser preenchido com o número de RN que foram Transferidos.
* Mortos  
  Campo deverá ser preenchido com o número de RN que tiveram Óbitos.

Procedimentos - Elaboração de AIH

## **04. PROCEDIMENTOS - ELABORAÇÃO DE AIH**

Nesta tela são cadastrados os procedimentos realizados.

* Procedimentos  
  Informe o procedimento realizado
* Executante  
  Quem executou o procedimento em questão
* Função  
  Função da pessoa (ou entidade) que executou o procedimento

Implementações realizadas no RM Saúde. Inserido a possibilidade de se informar o CNPJ do fabricante no lançamento de Órteses e Próteses na Elaboração de AIH.  
Quando um fabricante informado já possui um CNPJ cadastrado, automaticamente o sistema carregara do cadastro do mesmo o CNPJ.   
Caso não possua, o usuário poderá informar um CNPJ no momento de inserção do registro.

Validações

Na visão dos procedimentos, existem as colunas "Origem lançamento" e "Requisição".

Quando a coluna Origem Lançamento for "Evolução Clínica", e tentar excluir o registro ou alterar um dos campos "Quantidade", "Procedimento", "Data da Realização" ou "Executante", exibirá uma mensagem de confirmação informando que este lançamento possui origem no Prontuário Eletrônico, e que pode gerar algum tipo de divergência entre o lançamento excluído/editado e o registro original do PEP.

Ao clicar em não nada será feito, e ao clicar em sim permitirá a exclusão/edição.

Quando a coluna Requisição for "Sim", e tentar excluir o registro ou alterar o campo "Quantidade", exibirá uma mensagem impeditiva, informando que o item possui vínculo com o movimento de estoque, e que por isso não é permitida a exclusão/edição.

Mensagens de Erro

## **05. MENSAGEM DE ERRO**

Nesta tela serão exibidas em tempo real as situações de validações de AIH que ocorrem no momento do registro.

A cada inconsistência, será exibida a mensagem de alerta para o usuário.

A vantagem da exibição em tempo real do documento no momento da confirmação da gravação, eliminando-se o processo de validação do lote de documentos a serem enviados.

Rejeitar AIH/ Reverter AIH Rejeitada

## **06. REJEITAR AIH/ REVERTER AIH REJEITADA**

Uma AIH pode ser rejeitada ou reverter sua rejeição, através do processo que fica localizado na Elaboração da AIH.

* REJEITAR AIH

     Para rejeitar uma AIH, ela deve estar FATURADA.

Após execução, será exibida uma mensagem com os ids das AIHs que foram rejeitadas, se existir AIHs que não poderão ser rejeitadas será informado também seus ids.

* REVERTER AIH REJEITADA

   Para rejeitar uma AIH, ela deve estar REJEITADA.

Após execução, será exibida uma mensagem com os ids das AIHs que foram revertidas , se existir AIHs que não poderão ser revertidas será informado também seus ids.

CNES

## **07. CNES – Regras de Preenchimento no Procedimento da AIH**

Consultar nossa página para mais detalhes

Doc do Recebedor

## **08. Doc do recebedor**

Parâmetros SUS =>  Aba  **AIH**

O valor do Doc do recebedor, poderá ser preenchido manualmente ou automaticamente de acordo com as regras abaixo.

* Incluir um procedimento

Será preenchido com CNES Próprio, ou seja, do prestador do principal.

* Ao preencher o prestador executante
  + Se estiver marcado como CPF/CNPJ ou Identidade Profissional, o sistema irá buscar esta informação no cadastro do prestador.
  + Senão existir o tipo doc recebedor
    - Será feito uma buscar na tabela de credenciamento, filtrando o convênio, prestador e unidade faturamento para buscar o tipo de credencial.   
      E será preenchido irá preencher o valor do doc do recebedor correspondente ao campo.
    - Senão existir registro no credenciamento será preenchido o valor do doc :
      * Com o CNES do executante se ele existir e o tipo será CNEs terceiro
      * Senão será preenchido com o CNES do hospital e tipo será CNS Próprio
    - Se existir tipo do Doc do recebedor marcado ou for usado o combobox:
      * CNES Próprio – será preenchido o CNES do Hospital
      * CNPJ– CPNJ que estiver preenchido na tela
      * CNES Terceiro - CNES do prestador executante
      * CPF Profissional
        + Se competência estiver preenchida
          - Maior de 2011 – CNES credenciamento
          - CPF do executante
        + CPF do executante
