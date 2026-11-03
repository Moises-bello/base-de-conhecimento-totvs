---
content_hash: a4e757021fa6cf4c30787c07d2440d4ed440b5c3de0e1bc7d5ba3101be2def0a
fetched_at: '2026-06-29T00:10:31.303262+00:00'
page_id: '521640096'
product: rm
source: tdn-rm
title: Transmissão e Consulta
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521640096
version: 13
---

O sistema possui duas alternativas de "Envio" e "Consulta" dos eventos periódicos.  
  
1 - A primeira alternativa está disponível na tela de eventos, sendo ideal para realizar envio e consulta de eventos específicos uma vez que é necessário selecionar os eventos.

**RM > Gestão Fiscal >****Obrigações Acessórias > SPED > EFD Reinf > Eventos Periódicos" - "Menu anexos > Eventos".**

2 - A segunda alternativa é executar o envio e consultar a partir do evento R-5011:

Desse modo o processo é executado para todos os eventos do período com as seguintes consistências:

* A transmissão pelo R-5011/R-9011 selecionará todos os eventos R-20XX filhos dele, a Transmissão pelo R-9015 selecionará todos os eventos R-40XX filhos dele, com status não transmitido, inconsistente ou rejeitado e transmitirá estes eventos.
* A consulta pelo R-5011/R-9011e R-9015 selecionará todos os eventos pendentes ou pendente exclusão, filhos dele, incluindo aí registros R-20XX, R-40XX com status pendente, R20XX, R-40XX com status pendente exclusão (que possuem R-9000), e eventos R-2099 e R-2098 pendentes.
* Também é possível selecionar mais de um registro R-5011/R-9011 e R-9015 ou não selecionar registros e executar para todos
* Além disso, se os registros R-5011/R-9011 e R-9015 não tiver filhos aptos a transmissão, o sistema vai emitir um alerta.

Selecione os eventos desejados e execute o processo de Transmissão, ao assumir o Status de **Pendente** os mesmos devem ser consultados.

No processo de Consulta do Evento na Receita, se o retorno for "OK" o Evento fica com o Status **Autorizado**. Senão o Evento ficara com Status **Rejeitado**.

**Atenção:**

Ao utilizar o Processo de **"Transmitir Evento"** dentro do Aenxo dos **Eventos Periódicos** não devem ser selcionados mais de 1.000 registros, devido a restrição das ferramentas de

Banco de Dados e Performance de Aplicação, neste caso, quando hoiver um volume maior de Eventos, deve-se utilizar o Processo de **"Transmitir Eventos Periódicos"** da visão de **Eventos Periódicos**

**Observações:**

* Na consulta OK do Evento R-2098 o Status do Evento Pai R-5011 é alterado para Status **Aberto**. Senão o Evento Pai R-5011 volta para Status **Encerrado**.
* Na consulta OK do Evento R-2099 o Status do Evento Pai R-5011 é alterado para Status **Encerrado.** Senão o Evento Pai R-5011 volta para Status **Aberto**.

**3 Camadas**  
  
Foi incluída a tela no processo de consulta para agendamento em 3 camadas:

Caso não seja selecionado nenhum R-5011 será exibida tela com opção de executar o processo para todos os registros:
