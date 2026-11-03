---
content_hash: bc5e2c25759931f3d663ebde153e964acdca19f826c2ceac0e3416a09f876233
fetched_at: '2026-06-29T00:05:53.278954+00:00'
page_id: '1068948756'
product: rm
source: tdn-rm
title: Exclusão de dados do Meu eduCONNECT
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1068948756
version: 7
---

Com o crescimento dos dados do Meu eduCONNECT é importante assegurar a integridade e a performance da base de dados. Este processo consiste noexpurgo de dados do Meu eduCONNECT. Ele atua sobre notificações, dispositivos e geolocalização, removendo dados que excedam o período de retenção estabelecido. Essa manutenção previne o crescimento desordenado do volume de dados, garantindo que o sistema permaneça ágil e eficiente.

VersãoEste processo estará disponível à partir da versão 12.1.2602.155

# Permissão

Para acessar o processo é necessário que o usuário tenha a permissão abaixo:

# Processo

O processo está disponível no menu:

A primeira etapa do processo é o a definição do agendamento, se será executado uma única vez ou se será definido recorrência. 

A segunda etapa consiste na definição dos dados do processo.

O processo possui três campos:

* **Manter dados dos últimos (dias)**: este campo define o valor que será utilizado para o cálculo da data que será utilizada no processo para apagar os dados, ou seja, dados anteriores a esta data serão removidos.   
  + Exemplo:
    - o processo está sendo executado no dia 15/05/2026
    - o valor definido no campo foi de **365** dias
    - A data calculada será **15/05/2025**
    - **Resultado**: todos os dados anteriores a **15/05/2025** serão excluídos.
  + Os dados removidos envolvem os dados das tabelas SMENSAGEMCOMUM, SMENSAGEMINDIVIDUAL, SMENSAGEMANEXOS, SIMAGEMMENSAGEM e SRESPOSTAENQUETE.
* **Excluir dados de geolocalização**: define se os dado de geolocalização dos usuário também serão removidos (SGEOLOCALIZACAOUSUARIO).
* **Excluir dados de dispositivos dos usuários**: define se os dados de dispositivos de usuários também serão removidos (SDISPOSITIVOUSUARIO).

Ao finalizar o processo será exibida a mensagem:

**DICA:** levando em consideração o alto volume de dados do Meu eduCONNECT, é interessante que este processo seja executado com uma certa frequência e que sua execução seja fora do horário comercial para evitar impactos e lentidão na base de dados que pode impactar outras rotinas da organização.

# Log do processo

Este processo utiliza um novo padrão visual da TOTVS e por ser um processo agendado o log do processo não ficará visível no próprio processo, somente no gerenciamento de jobs.

O log irá mostrar a quantidade dias do processo, a data calculada e a quantidade de notificações, dispositivos e geolocalização excluídos.
