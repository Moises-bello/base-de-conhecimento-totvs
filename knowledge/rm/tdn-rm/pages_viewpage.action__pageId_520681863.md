---
content_hash: 6caa54329f961b160856aa153f5edabaf58c607d0a24ef4e1362de644db5b0ba
fetched_at: '2026-06-29T00:10:31.201944+00:00'
page_id: '520681863'
product: rm
source: tdn-rm
title: Processo de Exclusão das Informações do Contribuinte (Produção Restrita)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520681863
version: 12
---

## Transmitir Exclusão

O processo "Transmitir Exclusão das Informações do Contribuinte" permiti excluir os dados de teste da base de dados.

Ao ser executado, envia um Evento R-1000 para a Receita solicitando a exclusão de todas operações do contribuinte no ambiente de **Produção Restrita**na Base de dados da Receita.

**Importante:** Esse processo também irá excluir todos os eventos da base RM.

Disponível em: RM -> Gestão Fiscal -> Obrigações Acessórias -> SPED -> EFD-Reinf -> Eventos Cadastrais.

**Regras:**

* O tipo do evento selecionado deve ser R-1000.
* O Ambiente do Evento R-1000 deve ser **Produção Restrita.**
* Para transmissão do Evento R-1000 é necessário que o mesmo esteja **Autorizado**.

## Consultar Evento

Se a transmissão da exclusão for OK, então o status do Evento R-1000 passará a ser **Pendente Exclusão.**

Após a transmissão, deverá ser executado o processo Consultar Eventos. O resultado da consulta poderá ser:

R-1000leftPendente

**Pendente:** Neste caso o processamento do Evento esta aguardando a transmissão do TSS para o ambiente da RFB. Basta Aguardar e realizar a consulte novamente.

Autorizado

**Autorizado:** Ao ser autorizado a exclusão, todos os Eventos filhos (R-1070, R-40xx, R-20xx) serão apagados da base de dados e o R-1000 voltará para o Status não transmitido.

Rejeitado

**Rejeitado:** O Evento foi rejeitado porque a RFB não aceitou a exclusão dos dados de teste.

Geralmente isto acontece quando os dados não estão mais disponíveis no ambiente da Receita. Neste caso basta fornecer as devidas permissão ao usuário, editar o Evento R-1000, mudar o status para Nãos transmitido, Salvar e excluir o Registro. Isto deverá ser feito para cada Evento Filho dependente.

Permissão de usuário necessária:

**Observação:** Apenas o Evento R-1000 selecionado permanecerá na base com o status **Não Transmitido** e somente com o histórico desta operação. Todos os demais Eventos serão excluídos da base de dados de forma definitiva.
