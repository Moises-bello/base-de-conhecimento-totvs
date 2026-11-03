---
content_hash: d36aae8c3d7da3e554bf15b961436ed263296541a431c6637eaf6985c6bda269
fetched_at: '2026-06-29T00:09:29.378486+00:00'
page_id: '425438974'
product: rm
source: tdn-rm
title: Alta de Paciente (old)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425438974
version: 17
---

# VALIDAÇÕES REALIZADAS

## EXECUÇÃO DA ALTA

O processo de alta do paciente *não* pode ser realizado caso:

1. Existam itens pendentes de checagem pela Enfermaria;
2. Se o sumário de alta não foi gerado;
3. Se o sumário da alta foi impresso;
4. Quando existirem itens de SADT lançados na cota com data superior a data definida no momento da alta;
5. Se existem requisições pendentes para a Farmácia;
6. Caso a data da alta não seja a mesma da data de vigência das parciais
7. Motivo de alta deve ser informado.
8. Se o motivo da alta for Óbito, deve informar a data de óbito.
9. Em caso de Óbito, a data de Óbito informada deve ser menor ou igual a data atual.
10. A data da alta deve ser menor ou igual a data atual.

O cid da alta deve ser informado quando marcado o parâmetro geral  CID Obrigatório na Alta:  
RMSaude.exe > Opções > Parâmetros > Parâmetros Gerais > Registro e Controle > CID Obrigatório na Alta  
  
  
  
Além disso, será exibido um alerta para o usuário caso existam autorizações pendentes no *Processo de Alta.*

## CANCELAMENTO

Para o cancelamento da alta, são realizadas as seguintes validações:

1. Verifica se a última parcial do atendimento existe e não está faturada. Caso esteja, o cancelamento não poderá ser realizado;
2. Alerta caso o paciente possua algum atendimento interno em aberto;
3. Verifica se o leito do paciente não esta atualmente bloqueado, ocupado ou inativo. Caso esteja, impede o cancelamento.

# FLUXO

## ALTA

O processo de Alta do internação se dá nas seguintes etapas:

1. Realiza a validação (itens mencionados anteriormente);

2.1.    Caso a validação retorne erro, exibe a mensagem para o usuário e aborta a operação;

2.2.    Caso a validação retorne mensagens de alerta, solicita confirmação do usuário;

2.3.    Caso a validação retorne Ok ou o usuário confirme a solicitação do item anterior (1.b), continua o processo;

2. Libera os itens relacionados ao *Processo de Alta*, caso a coligada o utilize;

3. Atualiza as datas finais das parciais da conta do atendimento que ainda não tenham sido fechadas.

4. Atualiza a data final do acompanhante associado ao atendimento.

6. Finaliza AIHs, caso o paciente esteja utilizando SUS e possua AIHs;

5. Verifica o processo de alta:

        5.1.     Caso exista o parâmetro definindo o uso do Workflow do processo de alta, insere na fila do processo;

        4.1.     Caso esteja desmarcado, realiza a liberação do leito do paciente;

6. Verifica se existem *Gastos Particulares* na conta do paciente e, caso existam, informa em alerta para o mesmo ao final da execução do processo.

7. Caso o paciente selecionado para dar alta tenha 1 ou mais RN (Recém Nascidos) vinculados, será apresentada uma tela para selecionar os RN que deverão ter alta juntamente com a mãe.

## CANCELAMENTO

1. Realiza as validações;
2. Ocupa o leito do paciente;
3. Remove a data final da última parcial do atendimento;
4. Remove as informações da alta no atendimento;
5. Apaga as informações complementares da alta.

# EXECUÇÃO

## PASSO A PASSO
