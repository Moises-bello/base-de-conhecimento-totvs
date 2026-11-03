---
content_hash: 1ba1703c08bf633c36a9bd63b9383bf4ca027e9518f65fd196230df6d99acfd3
fetched_at: '2026-06-29T00:09:15.637506+00:00'
page_id: '421385431'
product: rm
source: tdn-rm
title: Integração de Calendários e Turnos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385431
version: 3
---

---

Para seleção do turno automática pelo intervalo do apontamento, torna-se necessário o envio do calendário de turno cadastrado no Manutenção de ativos para TOTVS Obras e Projetos. Este envio de dados do calendário será feito por WebService do Protheus e será informado em: **Parâmetros > Gerais > Mobilidade.**

Com WebService cadastrado, o usuário poderá executar o processo de sincronismo de calendário do equipamento, assim como no envio de apontamento o sistema irá verificar a data de atualização do calendário e de forma automática consultar o webservice e retornar o turno atual.

Depois que o calendário é sincronizado entre Manutenção de Ativos e TOTVS Obras e Projetos, o sistema identifica através do intervalo do apontamento, qual o turno do equipamento e consequentemente enviar essa informação na mensagem do apontamento para Manutenção de Ativos.

Existe um parâmetro de projeto que define a regra de negócio, caso o intervalo do apontamento esteja próximo ao período do turno.

Para o melhor entendimento, abaixo exemplo das regras que serão utilizadas:

**Cenário 1:**Apontamentodo coletor no intervalo de 1 turno

O TOTVS Obras e Projetos irá enviar o apontamento do equipamento com turno 01.

**Cenário 2:**Apontamentodo coletor no intervalo de 2 turnos

O TOTVS Obras e Projetos irá enviar o apontamento do equipamento com turno 01. Apesar do intervalo conflitar entre o apontamento, o sistema irá informar o turno que iniciou o apontamento.

**Cenário 3:** Apontamento do coletor no intervalo ultrapassado pela hora fim

O TOTVS Obras e Projetos irá enviar o apontamento do equipamento com turno 01. Apesar do intervalo de hora fim ultrapassar o horário do turno o TOTVS Obras e Projetos irá informar o turno que iniciou o apontamento.  
 **Cenário 4:**Apontamentodo coletor iniciando fora do intervalo de turnos

O TOTVS Obras e Projetos irá enviar o apontamento de acordo com a parametrização do processo. Será criado um parâmetro de projeto "Qual regra aplicar quando o início do apontamento não cumprir um intervalo valido", para definir o comportamento do TOTVS Obras e Projetos quando ocorrer o cenário acima, onde o início do apontamento está associado a um buraco no turno. Quando este cenário ocorrer o usuário tem a opção de definir pelo parâmetro se o sistema busca o turno anterior ao início do apontamento ou busca o turno posterior ao início do apontamento ou envia em branco.

**Cenário 5:**Apontamentodo coletor sem intervalo de turnos

O TOTVS Obras e Projetos irá enviar o apontamento sem turno. Provavelmente este apontamento poderá cair em acerto da parte diária no Manutenção de Ativos ou na Parte Diária caso exista um turno de 24 horas cadastrado de forma padronizada. 

**Cenário 6:**Apontamentodo coletor sem calendário de turnos sincronizado.

O TOTVS Obras e Projetos irá enviar o apontamento sem turno. Provavelmente este apontamento poderá cair em acerto da parte diária no Manutenção de Ativos ou na Parte Diária caso exista um turno de 24 horas cadastrado de forma padronizada.

**Sincronismo**

                O processo de sincronismo poderá ocorrer de duas maneiras, a primeira de forma manual e a segunda de forma automática.

                De forma manual o usuário terá que selecionar o processo de sincronismo e solicitar a execução, o Totvs Obras e Projetos irá realizar a chamada do serviço da manutenção de ativos e atualizará os calendários com os turnos.

                Já o processo automático será durante o envio do apontamento para a Manutenção de Ativos, onde o sistema no momento do envio irá verificar se a data de atualização do calendário é inferior a 1 dia, caso positivo, o sistema atualiza os calendários e turnos, já em caso negativo, o sistema utilizará o calendário cadastrado.

**Associação do Turno a Obra**

                Para a correta analise e seleção automática do turno para o apontamento de equipamento no Totvs Obras e Projetos, é necessário a associação do turno a obra. Para essa seleção, não será permitido a associação de turnos conflitantes em seus horários, sendo assim, ao associar um turno a obra não será possível associar um novo turno em que o horário gere um conflito com turno já associado, e para garantir essa integridade, será criada uma mensagem de aviso ao usuário que não será possível associar o calendário a obra.

                Para associar o turno a obra, é necessário que o usuário cadastre na obra os turnos que farão parte dos apontamentos e dos equipamentos.

                Essa associação estará disponível no menu Controle > Mobilidade > Equipamento > Associação do Calendário de Turno. Será possível realizar a associação do turno a obra, através do processo de "Incluir Turnos a Obra."

                Esse processo é possível selecionar os turnos que foram sincronizados pelo processo de sincronismo que farão parte da obra

**Envio de apontamento para o Manutenção de Ativos:**

                Nesse processo, vai ser buscado o turno do apontamento automaticamente de acordo com o intervalo do apontamento. Também será realizado um sincronismo com o Manutenção de Ativos caso os calendários estejam desatualizados em 1 dia.

                A informação do turno não será pré-requisito para o envio do apontamento para o Manutenção de Ativos, sendo assim, o apontamento poderá ser enviado normalmente mesmo com a informação de turno em branco.

   Informações Complementares

---

  Veja Também

---
