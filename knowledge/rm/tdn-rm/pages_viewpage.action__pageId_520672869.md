---
content_hash: 0e1f08601d14a9b5a53240e6dc1afc1a7c3d2c4ff64dace066f462f16107ae8e
fetched_at: '2026-06-29T00:10:31.170133+00:00'
page_id: '520672869'
product: rm
source: tdn-rm
title: FISCAL01-11400 DT EFD-REINF Processo de Exclusão das Informações do Contribuinte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520672869
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Processo de Exclusão das Informações do Contribuinte |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11400 |

## **02. SITUAÇÃO/REQUISITO**

Conforme documentação abaixo é possível excluir todos os dados do contribuinte em **Produção Restrita** na Base de Dados da Reinf na Receita Federal.

Item 10.6: [Link Documentação: Reinf - Manual de Orientação do Contribuinte](http://sped.rfb.gov.br/estatico/5C/DAAE5A101549723F6671DFF44F33879B9DA235/ManualOrientacaoDesenvolvedor-REINF%20v1.04.01.pdf "Follow link").

Deverá ser implementado um processo para limpar os dados já enviados a receita referente a Reinf.

* O processo deve ser disponível quando o ambiente do evento R-1000 é **Produção Restrita**.

O usuário ao executar o processo selecionando um evento autorizado R-1000, o mesmo deverá se comportar da maneira abaixo:

* O processo deverá aceitar apenas um registro R-1000 com status **Autorizado**
* Transmitir Exclusão da Operação para a Receita
* O R-1000 deverá ficar com o status **Pendente Exclusão.**

           Ao realizar consulta do Evento R-1000 e retorno OK da Receita,  o processo deverá excluir todos os eventos cadastrados e periódicos enviados no ambiente de produção restrita. Caso retorno negativo o evento R-1000 deve voltar para o status Autorizado e o histórico do evento retratar o motivo do não aceite por parte da Receita.

## **03. SOLUÇÃO**

Foi implementado o processo "Transmitir Exclusão das Informações do Contribuinte" em RM -> Gestão Fiscal -> Obrigações Acessórias -> SPED -> EFD-Reinf -> Eventos Cadastrais.

Este processo ao ser executado envia um Evento R-1000 de Inclusão para a Receita que solicita a exclusão de todas operações do contribuinte no ambiente de **Produção Restrita** na Base de dados da Receita.

Validações:

* O tipo do evento selecionado deve ser R-1000
* O Ambiente do Evento R-1000 deve ser **Produção Restrita**
* Para transmissão do Evento R-1000 é necessário que o mesmo esteja **Autorizado**.

Se a transmissão da exclusão for OK então o status do Evento R-1000 passara a ser **Pendente Exclusão.**

Senão o status do Evento continua como **Autorizado** e será persistido no histórico do evento o motivo da rejeição da Exclusão.

Processo de Consulta Evento foi evoluído para excluir os eventos filhos como R-1070, R-5011 e R-20xx após aceite deste evento.

**Observação:** Apenas o Evento R-1000 selecionado persistira com status **Não Transmitido** e somente com o histórico desta operação.
