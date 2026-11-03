---
content_hash: ba43e3ecbb1b1252acc9b4a827ed63b9c8307a5a1a5b2b7858be28a39668f8fd
fetched_at: '2026-06-29T00:10:09.450794+00:00'
page_id: '452719672'
product: rm
source: tdn-rm
title: Eventos Periódicos - TAF/TSS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719672
version: 2
---

Através do eventos da folha - eSocial será possível monitorar os registros dos Eventos periódicos gerados, bem como seus status. Após a geração do XML ao editar os registros, poderá identificar informações como   
 o Tipo de Evento, o Status, o Tipo de Operação, e o cadastro a que ele se refere, além de erros de geração e informações da integração com TAF/TSS.  

**Observações:**

* Caso o gatilho seja incluído de forma manual na fila de eventos, a informação "Evento inserido manualmente" ficará destacada na tela do cadastro.
* Para os eventos **rejeitados pelo Governo**, o detalhamento da possível inconsistência poderá ser verificada na aba "Erros de integração" ao editar o registro na Fila de Eventos.
* A partir do registro da fila de eventos é possível Integrar com TAF, Gerar XML, Atualizar Status Integração TAF, gerar o Evento de Exclusão (S-3000) , Gerar Retificação Arquivo eSocial , Excluir Evento da Fila (Esse processo é IRREVERSÍVEL) e Validar S-1200 com Envelope dos registros selecionados.
* Para a atualização do status de uma grande quantidade de registros, não é recomendável utilizar a Fila de Eventos, deverá utilizar o processo "Atualizar Status Integração TAF" que encontra-se disponível no menu  "eSocial".
