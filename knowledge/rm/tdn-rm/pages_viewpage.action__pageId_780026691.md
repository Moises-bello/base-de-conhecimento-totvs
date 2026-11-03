---
content_hash: 9403f82de5b59296152dc459f848ca1d401daf4578a6a762345fd37670cd885d
fetched_at: '2026-06-29T00:11:37.923176+00:00'
page_id: '780026691'
product: rm
source: tdn-rm
title: Turnos (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780026691
version: 7
---

O uso do parâmetro de turno é uma funcionalidade que permitirá que para cada apontamento de [mão de obra](https://tdn.totvs.com.br/pages/viewpage.action?pageId=608171251), [equipamento](https://tdn.totvs.com.br/display/LRM/Equipamento) e [ciclo de transporte](https://tdn.totvs.com.br/display/LRM/Ciclos+de+Transporte), caso o parâmetro esteja habilitado, o sistema informe em qual turno de trabalho o apontamento foi realizado.

O parâmetro **Utiliza Turno** se encontra na seção de Parâmetros | Mobilidade.

Este parâmetro permite definir até 3 turnos diferentes para o registro de apontamentos no sistema.

Para começar a utilizar os turnos, basta marcar o campo correspondente na tela e informar os turnos de trabalho da sua empresa: 

Você pode definir até **3 turnos completos**, sendo necessário informar para cada turno:

* Nome do Turno (com no máximo 10 caracteres)
* Horário Inicial do Turno
* Horário Final do Turno

Ao habilitar o parâmetro é **obrigatório definir pelo menos um turno completo**, incluindo nome, horário inicial e horário final, quando o parâmetro estiver ativado.

Os horários de diferentes turnos **não podem coincidir.**

Exemplos de **utilização do turno:**

Turno 1 - 08:00 - 18:00  
Turno 2 - 18:01 - 07:59

Exemplo do que **NÃO pode ser definido:**

Turno 1 - 08:00 - 11:59  
Turno 2 - 12:00 - 18:00  
Turno 3 - 17:00 - 07:59

Nesse exemplo temos 2 turnos com o horário entre 17:00 e 18:00h, o que **NÃO é permitido pelo sistema**.

**Observações:**

* O sistema vem com o parâmetro **"Utiliza Turno" desmarcado por padrão**. Lembre-se de marcá-lo para ativar essa funcionalidade.
* Após realizar apontamentos com o parâmetro marcado, não será mais possível desabilitar a utilização do turno.
