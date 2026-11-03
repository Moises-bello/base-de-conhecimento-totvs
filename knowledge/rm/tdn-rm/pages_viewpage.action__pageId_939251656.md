---
content_hash: 63393455c035c2fa05a0e13137da7d2dd1f1a6852b9e8afe949a6fe16d9e543d
fetched_at: '2026-06-29T00:12:09.093822+00:00'
page_id: '939251656'
product: rm
source: tdn-rm
title: Aluguel Complementar - Liberação de Faturamento Diario
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=939251656
version: 5
---

### Introdução

---

O processo de liberação de faturamento diário consiste em liberar períodos para inclusão de faturamento diário. Estes períodos serão liberados de acordo com os parâmetros definidos em: [Controle de Faturamento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105240#TotvsIncorpora%C3%A7%C3%A3oPar%C3%A2metrosAluguel-ControledeFaturamento)

Este processo deve ser agendado ou executado de forma manual, a critério do utilizador.

### Procedimentos para utilização

---

Parametrizar o sistema: Para a correta utilização do processo de liberação de faturamento diário, devemos primeiro definir os parâmetros que irão compor os períodos de liberação e bloqueio.

Liberar a permissão do menu: Para acesso ao menu de liberação de faturamento diário deve ser primeiro habilitada a permissão no perfil de usuário. Após isso, acessar o processo em *Contrato de Locação / Processos / Aluguel Complementar / Liberação de Faturamento Diário*

Ao executar o processo serão liberados os dias para inclusão de faturamento no [Portal do Lojista](https://tdn.totvs.com/pages/viewpage.action?pageId=673780881)

### Exemplo de utilização

---

Parâmetros:

* **Tolerância: 1 dias;**
* **Dia Base para Bloqueio: Quarta Feira;**
* **Periodicidade: Semanal**

**Competência 01/04/2025 - 30/04/2025**

**Data de execução do processo: 01/04/2025 (Terça Feira)**

**Após a execução do processo:**

**Dia liberado: [30/03/2025]  
Dia liberado: [31/03/2025]**

**Como ainda estamos no inicio do mês, existe a regra de mostrar os últimos dois dias da última competência, facilitando o preenchimento por possíveis esquecimentos.**

**Competência 01/04/2025 - 30/04/2025**

**Data de execução do processo: 02/04/2025 (Quarta Feira)**

**Após a execução do processo:**

**Dia liberado: [01/04/2025]  
Dia liberado: [02/04/2025]**

**Dia 2 é Quarta Feira e como definimos no parâmetro que é nosso dia de bloqueio, as competências serão bloqueadas e somente o período da semana estará aberto para preenchimento.**

**Competência 01/04/2025 - 30/04/2025**

**Data de execução do processo: 03/04/2025 (Quinta-Feira)**

**Após a execução do processo:**

**Dia liberado: [01/04/2025]  
Dia liberado: [02/04/2025]**

**Temos um dia de tolerância, então não haverão mudanças nos períodos liberados.**

**Competência 01/04/2025 - 30/04/2025**

**Data de execução do processo: 04/04/2025 (Sexta-Feira)**

**Após a execução do processo:**

**Dia liberado: [03/04/2025]**  
**Dia liberado: [04/04/2025]**  
**Dia liberado: [05/04/2025]**  
**Dia liberado: [06/04/2025]**  
**Dia liberado: [07/04/2025]**  
**Dia liberado: [08/04/2025]**  
**Dia liberado: [09/04/2025]**

**Como ultrapassamos o dia de tolerância, os próximos dias da semana são abertos, até o próximo dia base parametrizado: Quarta-Feira (09/04/2025)**

### Liberação Manual do Faturamento Diário

---

É possível também, através do menu *Anexos / Aluguel Complementar / Liberação de Faturamento Diário*, incluir ou remover registros de forma manual para uma determinada data.

Para incluir uma nova data de liberação basta clicar no botão de incluir e então, na tela, selecionar uma data onde será possível incluir determinado faturamento diário.

É importante frisar que essa inclusão manual deve ser utilizada em casos específicos, justamente onde um período já está bloqueado e o cliente ainda não conseguiu inserir seu faturamento, visto que, na próxima execução do processamento agendado, essa data, possivelmente será novamente bloqueada, se não estiver dentro dos critérios dos parâmetros.

É também possível excluir esse registro, bem como os registros de liberação automática selecionando os mesmos e clicando no botão "Excluir".

Quando um registro é excluído, automaticamente esse período é bloqueado no Portal do Lojista.
