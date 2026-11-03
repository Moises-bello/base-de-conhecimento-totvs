---
content_hash: 38d73fe9c15a5f7eae9fc53233ae5a81beb5e9ea18b7dfdaf594eb2b44f077fd
fetched_at: '2026-06-29T00:11:26.372770+00:00'
page_id: '716352843'
product: rm
source: tdn-rm
title: Regras Gerais - Eventos Periódicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716352843
version: 4
---

Todos os [eventos periódicos](https://tdn.totvs.com/pages/viewpage.action?pageId=506387451) seguem as regras abaixo.

* Quando o Evento estiver com status de "Pendente" ou "Pendente Exclusão" todos os campos vão ficar bloqueados para Edição;
* Quando o Evento estiver com status de "Excluído" o mesmo deverá ser bloqueado para Edição;
* Os campos **Cód. Coligada** e **Cód. da Filial**não são visíveis;
* Os campos **Identificador,** **Status,** **Tipo,** **Ambiente,** **Data da Última Transmissão, Número do Protocolo, XML de envio, XML de retorno** não são editáveis;
* O Evento Filho deverá obrigatoriamente estar compreendido no período do Evento Pai;
* O campo Data Inicial poderá ser alterado somente se o status do Evento for “Não Transmitido”, “Inconsistente” ou “Rejeitado”;
* O campo Data Final poderá ser alterado somente se o status for “Não Transmitido”, “Inconsistente”, “Rejeitado”, “Autorizado” ou “Alterado”;
* O campo **Id. Processo Judicial** só pode ser editado/incluído pelo Evento R-1070;
* O cadastro do Evento poderá ser excluído somente quando status for "Não Transmitido", "Inconsistente" ou "Rejeitado";
* O campo Status do evento pode ser editado, por usuário que possui permissão, para eventuais alterações de lançamentos que não afetem a rotina REINF;
* Não é possível excluir o evento após transmissão, mesmo alterando o status do evento, devido relacionamento entre as tabelas envolvidas.
* Ao ser incluído o Evento assumirá o Status de "Não transmitido";
* Durante a inclusão o sistema irá identificar o Evento Pai automaticamente e preenchê-lo no cadastro;
* Durante a Edição se o Evento estiver com Status de "Não Transmitido" o status não será alterado, quando o Evento estiver com o Status "Inconsistente" ou "Rejeitado" o Status será alterado para "Não Transmitido". Qualquer outro status o Evento assumirá o Status de "Alterado".
