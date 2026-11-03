---
content_hash: 405c14a7bffba120ce02a3d97e1d63395069aacce2065e22fb655ba6d73f8afb
fetched_at: '2026-06-29T00:11:55.767463+00:00'
page_id: '863921945'
product: rm
source: tdn-rm
title: 04 - Inscrição para vários membros da mesma Família com Controle de Vagas /
  Reserva
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=863921945
version: 25
---

# Sumário

---

Sumário

# Objetivo

---

Demonstrar o comportamento da Inscrição via **Portal TOTVS Processo Seletivo** com Controle de Vagas para vários Membros da Mesma Família

Quando o controle de vagas é utilizado, o usuário tem um tempo limitado para concluir a inscrição. Isso ocorre porque, após informar os dados do candidato e avançar no processo, a vaga é imediatamente reservada.

Para saber mais sobre como configurar essa funcionalidade,  [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=856934701). Para entender o funcionamento da reserva de vagas, [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=856936252).

Incrição Familiar para Estrangeiros

O serviço de reserva de vagas está apto a processar reservas para responsáveis que sejam estrangeiros. O sistema aceitará e fará a reserva com tipo de documento que foi parametrizado no processo seletivo (passaporte ou número de registro geral).

# Tipo do controle de vagas: Não permitir novas inscrições

---

Quando o processo seletivo estiver configurado com o parâmetro **"Utiliza Controle de Vagas"**, com o parâmetro **"Não permitir novas inscrições"** habilitado, o sistema deve se comportar da seguinte maneira, de acordo com à disponibilidade de vagas nas áreas de interesse selecionadas:

* Se durante o processo de inscrição uma ou mais áreas de interesse não tiverem mais vagas disponíveis, o sistema exibirá que *não existe vaga disponível para a(s) área(s) de interesse selecionada(s).* Nesta situação, o usuário não poderá continuar com a inscrição.
* Se o número de candidatos para uma vaga for maior que o número de vagas disponíveis e o usuário optar por continuar, apenas o candidato com o número de inscrição menor será inscrito.

  **Tempo Limite de Inscrição:**
* Quando o tempo limite para finalizar a inscrição expirar, um aviso sonoro será emitido e a seguinte mensagem aparecerá: '*Para inscrever os demais candidatos, por favor, reinicie o processo*.'
* Caso o usuário permaneça na tela de inscrição além do tempo determinado, sem finalizar o processo, será exibida a seguinte mensagem: *"Para inscrever os demais candidatos, por favor, reinicie o processo."* O usuário será obrigado a clicar em "OK", o que o redirecionará para a tela inicial de inscrição.Inscrição em um Processo Seletivo que Não Permite Novas Inscrições

  Inscrição de dois candidatos em um processo seletivo com uma única vaga disponível:

  Tempo Limite da Inscrição

# Tipo do controle de vagas: Permitir novas inscrições como excedente

---

Quando o processo seletivo estiver configurado com o parâmetro **"Utiliza Controle de Vagas"**, com o parâmetro **"Permitir novas inscrições"** habilitado, o sistema deve se comportar da seguinte maneira:

* Se durante o processo de inscrição uma ou mais áreas de interesse não tiverem mais vagas disponíveis, o sistema exibirá que *não existe vaga disponível para a(s) área(s) de interesse selecionada(s).* Nesta situação, o usuário poderá permitir continuar com a inscrição, alertando que os candidatos ficará como excedente.  
  **Tempo Limite de Inscrição:**
* Quando o tempo limite para finalizar a inscrição expirar, um aviso sonoro será emitido e a seguinte mensagem aparecerá: '*Para inscrever os demais candidatos, por favor, reinicie o processo*.'
* Caso o usuário permaneça na tela de inscrição além do tempo determinado, sem finalizar o processo, será exibida a seguinte mensagem: *"Para inscrever os demais candidatos, por favor, reinicie o processo."* O usuário será obrigado a clicar em "OK", o que o redirecionará para a tela inicial de inscrição. Se desejar não continuar com a inscrição, só clicar em finalizar.

Inscrição em um Processo Seletivo que Permite Excedentes

Inscrição de dois candidatos em um processo seletivo com apenas uma vaga disponível, que permite excedente:

Monitoramento e atualização da lista de excedente

O processo de inscrição utilizando o controle de vagas com reserva é bastante dinâmico, pois as vagas são reservadas imediatamente após a entrada dos dados dos candidatos. No entanto, diversos cenários podem permitir que um candidato excedente ganhe a vaga, tais como:

* O candidato que obteve a vaga não concluir a inscrição dentro do prazo estipulado.
* O candidato desistir de continuar com a inscrição durante o processo.
* O número de vagas ser aumentado para a oferta em questão.
* Cancelamento ou exclusão de inscrições por parte do operador do sistema no RM.

Durante ou após o período de inscrição, recomendamos utilizar o processo "[Atualização da lista de candidatos excedentes](https://tdn.totvs.com/pages/viewpage.action?pageId=546245734)" para monitorar esses eventos.

**Agendamento do processo**

É importante destacar que, em um ambiente de três camadas, esse processo pode ser agendado para execução periódica. Isso permite uma análise mais rápida da lista de reserva e das vagas disponíveis, possibilitando a alocação de vagas para candidatos excedentes durante o período de inscrição e não apenas após seu término.
