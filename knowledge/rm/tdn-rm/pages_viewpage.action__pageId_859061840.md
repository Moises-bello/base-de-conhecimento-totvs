---
content_hash: 32dd8c046b4be57b50c4628601a0f51a8626e80a0104e89ea6b598243f6dc3da
fetched_at: '2026-06-29T00:11:54.914666+00:00'
page_id: '859061840'
product: rm
source: tdn-rm
title: Processos Cirúrgicos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859061840
version: 54
---

## **CONTEÚDO**

1. **Visão geral**
2. **Exemplo de utilização - SAEP**
   1. **Pré-operatório**
   2. **Intra-operatório**
   3. **Pós-operatório**
   4. **Resumo**
   5. **Relatório padrão**
   6. **Suspensão/Cancelamento cirúrgico**
3. **Exemplo de utilização - Cirurgia segura (12.1.2506)**
   1. **Antibioticoprofilaxia cirúrgica**
   2. **Atalho para protocolos assistenciais**

SAEP1. Visão Geral

## **01. Visão Geral**

O menu de Processos Cirúrgicos foi desenvolvido para reunir em um único espaço funcionalidades que apoiam a equipe multiprofissional no cuidado perioperatório, com foco em segurança, eficiência e integração.

Disponível a partir da versão 12.1.2410,a Sistematização da Assistência de Enfermagem Perioperatória (SAEP) é um processo organizado e sistemático utilizado por enfermeiros para planejar, implementar e avaliar cuidados de enfermagem específicos durante o período perioperatório, incluindo as fases pré-operatória, intra-operatória e pós-operatória. A SAEP visa garantir a segurança do paciente, minimizar riscos e promover uma recuperação eficiente, por meio de uma abordagem centrada no paciente e baseada em evidências. A funcionalidade contemplará a avaliação inicial do paciente, planejamento da assistência, implementação de intervenções, avaliação e monitoramento do paciente durante todo o fluxo cirúrgico.  A nova funcionalidade será integrada na aba "Processos Cirúrgicos", no menu do prontuário eletrônico.

A partir da versão 12.1.2506, a funcionalidade deprescrição, checagem e suspensão de antibióticos profiláticos diretamente no card cirúrgico estará disponível no menu de processos cirúrgicos. Essa melhoria tem como objetivo aumentar a praticidade e agilidade no processo de administração de medicamentos, assegurando que os antibióticos necessários sejam conferidos, prescritos e administrados de forma correta e no tempo adequado. Além da prescrição de antibióticos, o card de procedimentos cirúrgicos também contará com o botão “Protocolos”, que funciona como um atalho direto para o módulo de Protocolos Assistenciais. Esse recurso foi desenvolvido para agilizar o acesso e acompanhamento de protocolos relacionados à segurança do paciente, permitindo que a equipe multiprofissional consulte ou registre protocolos diretamente a partir do contexto cirúrgico, reforçando as práticas de cuidado integrado e cirurgia segura.

2. Exemplo de utilização - SAEP

## **02. Exemplo de utilização - SAEP**

##### **Funcionalidade disponível a partir da versão 12.1.2410.**

Ao acessar a aba de “Processos cirúrgicos” no menu lateral do PEP, os procedimentos   serão exibidos em um card contendo a descrição do tipo de cirurgia, a data e hora agendadas para a realização da cirurgia, o nome do usuário responsável pelo agendamento, a data e hora da criação do agendamento, respectivamente.

Para acessar as etapas pré, intra e pós-operatório, clique na descrição “SAEP” do card. Cada etapa será preenchida de forma independente, garantindo a integridade das informações, rastreabilidade e otimização da comunicação entre os profissionais envolvidos.

a. Pré operatórioa. Pré-operatório

## **a. Pré-operatório**

A etapa pré-operatória da SAEP é crucial para garantir uma avaliação detalhada do estado de saúde do paciente, identificar e gerenciar riscos, planejar e preparar o paciente adequadamente para a cirurgia, facilitar a comunicação eficiente entre a equipe multidisciplinar e aumentar a segurança do paciente ao assegurar que todas as preparações necessárias sejam cumpridas conforme os protocolos estabelecidos. 

Ao acessar a aba da etapa pré-operatória, serão exibidas as seguintes seções para preenchimento:

Procedimentos

Os procedimentos previamente agendados serão exibidos em cards, contendo o nome do procedimento, local e lateralidade quando aplicável. O profissional poderá adicionar outros procedimentos, excluir ou editar essas informações, se necessário. Ao clicar no botão “Adicionar”, uma modal será exibida com os seguintes campos para preenchimento:

* Procedimento: Campo de busca por procedimentos cirúrgicos cadastrados.
* Local: campo de texto livre.
* Lateralidade: exibe uma lista com as opções: direito, esquerdo, estruturas múltiplas, níveis múltiplos, ambos e não se aplica.

Para finalizar a inclusão do procedimento, clique no botão “Salvar”. Os procedimentos adicionados ou com as informações alteradas na etapa pré-operatório serão também exibidos na etapa intra-operatório.

As informações dos procedimentos adicionados e/ou alterados através do PEP, não serão repassadas para a**[agenda de cirurgias no RM](https://tdn.totvs.com/display/LRM/Agenda+de+Cirurgia).**

Atendimento

O usuário poderá visualizar e editar as informações referentes ao atendimento pré-operatório, para garantir que todos os detalhes estão corretos antes da cirurgia. Para incluir e/ou editar as informações clique no botão “Editar” e uma modal será exibida para preenchimento composta pelos campos:

* Campos “Unidade de atendimento”, “Sala” e “Profissionais”, estarão preenchidos de acordo com as informações inseridas na agenda cirúrgica e o usuário poderá alterar essas informações.
* Tempo de sala previsto: campo para preenchimento de hora e minutos do tempo de sala previsto.
* Grau de contaminação: o campo exibe uma lista com as opções: limpa, potencialmente contaminada, contaminada e infectada.
* Anestesia: o campo exibe uma lista com as opções: interna e externa.

Para finalizar a edição, clique no botão “Salvar” ou no botão “Cancelar” para fechar a modal.

Preparação

Para incluir e/ou editar as informações clique no botão “Editar” e uma modal será exibida para preenchimento composta pelos campos:

* Internação: exibe uma lista com as opções: unidade de internação, alta e UTI.
* Gestante: exibe as opções: sim e não.
* Termo de consentimento: exibe as opções sim e não, referente a assinatura do termo pelo paciente.
* Jejum de sólidos: o usuário poderá selecionar se o jejum de sólidos é necessário marcando as opções "Sim" ou "Não". Caso o usuário selecione a opção “Sim”, o campo "Tempo" será habilitado para indicar o tempo de jejum necessário.
* Jejum de líquidos: o usuário poderá selecionar se o jejum de líquidos é necessário marcando as opções "Sim" ou "Não". Caso o usuário selecione a opção “Sim”, o campo "Tempo" será habilitado para indicar o tempo de jejum necessário.
* Preparo: o usuário poderá selecionar se um preparo é necessário para realizar o procedimento marcando as opções "Sim" ou "Não". Caso o usuário selecione a opção “Sim”, o campo "Justificativa" será habilitado para descrever o preparo necessário.
* Adornos: o usuário poderá selecionar se o paciente está utilizando adornos marcando as opções "Sim" ou "Não". Caso o usuário selecione a opção “Sim”, o campo "Justificativa" será habilitado para descrever a justificativa.

Para finalizar a edição, clique no botão “Salvar” ou no botão “Cancelar” para fechar a modal.

Sinais vitais e glicemia capilar

Nesta etapa, se houver, serão exibidos nas tabelas os sinais vitais e glicemia capilar mais recentes registrados na , contendo a data e hora da liberação e o responsável pelo registro. Se não houver nenhum registro recente, a tabela será exibida em branco. Os sinais vitais e glicemia capilar adicionados na etapa pré-operatório também serão salvos na tabela de “Monitorização Geral”, em  , após a finalização do pré-operatório. 

Para incluir e/ou editar os sinais vitais e glicemia capilar clique no botão “Editar” na respectiva tabela. Será exibido para preenchimento a mesma modal de , composta pelos campos previamente cadastrados. Para finalizar a inclusão ou edição, clique no botão “Salvar” ou no botão “Cancelar” para fechar a modal.

Acesso rápido

O usuário poderá acessar os registros mais recentes realizados no  e , registrados na aba . Para acessar, basta clicar nos respectivos botões e uma página lateral exibirá as informações registradas, a data e hora da liberação e o responsável pelo registro. Essas informações não podem ser editadas, apenas visualizadas.

Prescrição de enfermagem

O(A) enfermeiro(a) poderá realizar o levantamento dos diagnósticos de enfermagem e intervenções a serem realizadas durante o intra-operatório, para garantir um plano de cuidados específico e eficaz para o paciente.

Para incluir e/ou editar a prescrição, clique no botão “Adicionar” e uma modal será exibida para preenchimento composta pelos campos:

* Padrão de diagnósticos: o campo exibe uma lista com os padrões de diagnósticos previamente cadastrados.  para saber mais sobre os padrões de diagnósticos.
* Diagnóstico: o campo exibe uma lista com os diagnósticos vinculados ao padrão de diagnóstico selecionado.
* Cuidado: o campo exibe uma lista com os cuidados previamente vinculados ao diagnóstico selecionado. O usuário poderá manter ou alterar a seleção de cuidados, clicando no checkbox do respectivo cuidado exibido na lista expandida.

Para finalizar a edição, clique no botão “Salvar”. Após salvar a inclusão, os diagnósticos serão exibidos em uma lista e ao expandir o accordion serão exibidos todos os cuidados adicionados. Para remover algum cuidado, o usuário poderá clicar no respectivo ícone de lixeira e confirmar ou cancelar a exclusão na modal que será exibida. Para incluir outros cuidados para o mesmo diagnóstico, basta selecionar o mesmo padrão e diagnóstico e adicionar os novos cuidados. Ao clicar em salvar a lista dos cuidados será atualizada e exibirá os cuidados adicionados anteriormente e os novos.

Complemento

Para registrar mais informações pertinentes ao pré-operatório, o usuário poderá utilizar o campo “Complemento”.

Finalização

Para finalizar o preenchimento da etapa, o usuário deverá selecionar um dos seguintes desfechos:

* Cancelar cirurgia: ao selecionar essa opção, uma modal será exibida solicitando a justificativa para o cancelamento da cirurgia. Após preencher a justificativa, as etapas intra e pós-operatório serão desabilitadas e o usuário será redirecionado para a tela de resumo.
* Suspender cirurgia: ao selecionar essa opção, uma modal será exibida solicitando a justificativa para a suspensão da cirurgia. Após preencher a justificativa, as etapas intra e pós-operatório serão desabilitas e o usuário será redirecionado para a tela de resumo.
* Encaminhar para o intra-operatório: ao selecionar essa opção, o usuário será redirecionado para a tela de resumo e as etapas intra e pós-operatório continuarão habilitadas para preenchimento.

Durante o preenchimento da etapa, o registro ficará salvo como rascunho e, no fim da página, terá a sinalização “Em rascunho”, com a possibilidade de excluir as informações.  Para excluir as informações inseridas nessa etapa, clique no botão “Excluir”. Após confirmar a ação, o usuário será redirecionado para a tela principal de processos cirúrgicos e o nome do profissional responsável pelo rascunho e as informações inseridas anteriormente serão apagadas sem possibilidade de recuperação dos dados. Para iniciar novamente o preenchimento, basta entrar novamente na respectiva aba da etapa logado com o usuário do profissional responsável pelo registro - após acessar a aba, mesmo que um usuário diferente acesse a etapa simultaneamente, ao tentar fazer uma alteração no formulário, uma mensagem de alerta será exibida informando que o preenchimento já foi iniciado por outro profissional.

Para confirmar o desfecho da cirurgia, selecione uma opção e clique no botão “Confirmar”. Após a confirmação, o usuário será redirecionado para o resumo. O nome e conselho do profissional responsável pelo preenchimento, data e hora da liberação e a justificativa, quando aplicável, ficarão registrados no fim da página após a confirmação e a situação do formulário será atualizada para “Finalizado”.

Após a finalização, não será mais possível excluir o registro, apenas suspender. Se for necessário alterar ou adicionar informações, o usuário poderá voltar à etapa e clicar no botão “Suspender” e em seguida “Habilitar edição”.  Ao habilitar a edição, os dados registrados em campos abertos e em outras seções serão recuperados para que o usuário faça a edição apenas nos campos necessários. As informações inseridas nas tabelas de sinais vitais através da SAEP serão suspensos e os sinais vitais que tiverem sua origem dos registros recentes da monitorização geral, não serão suspensos visando manter a rastreabilidade. Para salvar as alterações, selecione novamente o desfecho e clique no botão “Confirmar”.

Ao suspender a etapa, mesmo que não habilite a edição, os registros feitos nas tabelas de sinais vitais e glicemia capilar serão imediatamente suspensos nas tabelas do formulário da SAEP e também nas tabelas de "Monitorização geral" na aba "Controles de enfermagem". Se o usuário optar por habilitar a edição, todos os dados suspensos deverão ser registrados novamente. Ao finalizar novamente a etapa, os dados antigos serão mantidos como suspensos e os que foram adicionados durante a edição serão registrados como novos em controles de enfermagem, contendo o nome do profissional, conselho, data e hora da nova liberação.

b. Intra-operatório

## **b. Intra-operatório**

A etapa intra-operatório da SAEP é crucial para garantir o registro das informações durante a realização do procedimento cirúrgico, garantindo uma comunicação mais eficiente entre a equipe e a segurança do paciente ao assegurar que todas as informações foram registradas no prontuário.

Ao acessar a aba da etapa intra-operatório, serão exibidas as seguintes seções para preenchimento:

Procedimentos

Os cards de procedimentos na etapa intra-operatório virão preenchidos conforme as informações que constam no pré-operatório referente aos procedimentos que foram adicionados na etapa e/ou às alterações feitas. Contudo, as outras alterações feitas nesta etapa não refletem nos procedimentos já registrados no pré-operatório.

Nesta etapa, os cards têm a mesma descrição de procedimento, local e lateralidade quando aplicável. O profissional poderá adicionar outros procedimentos, excluir ou editar essas informações, se necessário.

Ao clicar no botão “Adicionar”, uma modal será exibida com os campos para preenchimento:

* Procedimento: Campo de busca por procedimentos cirúrgicos cadastrados.
* Local: campo de texto livre.
* Lateralidade: exibe uma lista com as opções direito, esquerdo, estruturas múltiplas, níveis múltiplos, ambos e não se aplica.

Para finalizar a inclusão do procedimento, clique no botão “Salvar”.

As informações dos procedimentos adicionados e/ou alterados através do PEP não serão repassadas para a**.**

Equipe

A equipe responsável pela cirurgia será exibida em uma tabela contendo o nome, conselho e função. A equipe é exibida na tabela na ordem da função: cirurgião, auxiliares, instrumentador, enfermeira e circulante. A tabela pode vir preenchida conforme as informações adicionadas durante o agendamento, com a opção de edição e exclusão. Para adicionar ou alterar a equipe, clique em “Visualizar” e uma modal será exibida com os campos para preenchimento:

* Nome: campo de busca com os profissionais cadastrados.
* Conselho: o campo é bloqueado para edição e ao selecionar o profissional, o campo é preenchido com o respectivo conselho cadastrado.
* Função: campo de busca com as funções cadastradas.

Para finalizar a inclusão ou edição da equipe, clique no botão “Salvar”. Para excluir qualquer profissional, clique em “Excluir” no respectivo ícone de opções na tabela.

A edição da equipe nesta etapa não reflete na etapa pré-operatória e na .

Cronograma

O usuário poderá registrar o cronograma da cirurgia. Para adicionar ou alterar o cronograma, clique no botão “Editar” e uma modal será exibida com os campos para preenchimento do horário:

* Admissão do paciente
* Início da anestesia
* Início da cirurgia
* Final da cirurgia
* Final da anestesia
* Saída do paciente

Para finalizar a inclusão ou edição do cronograma, clique no botão “Salvar”.

Situação

O usuário poderá registrar as informações referentes a situação do paciente e procedimentos da cirurgia. Para adicionar ou alterar a “Situação”, clique no botão “Editar” e uma modal será exibida com os campos para preenchimento:

* Posicionamento do paciente
* Assepsia da área cirúrgica
* Proteção de áreas de pressão
* Tipo de anestesia
* Técnica anestésica
* Campo complementar

Para finalizar a inclusão ou edição da situação, clique no botão “Salvar”.

Sinais vitais, dispositivos, equipamentos e ganhos e perdas

O usuário poderá registrar os sinais vitais, dispositivos, equipamentos e ganhos e perdas utilizados durante o intra-operatório para garantir que os dados sejam registrados com segurança. Nesta etapa, os sinais vitais registrados anteriormente na etapa pré-operatório ou controles de enfermagem não serão incluídos, a tabela será exibida em branco.

Para adicionar os itens clique no botão “Adicionar” na respectiva tabela e a modal exibida será a mesma utilizada em . Todas as informações registradas nessa etapa também ficarão registradas na aba Controles de Enfermagem. Em cada tabela, ao clicar no ícone de opções o usuário poderá visualizar, editar ou suspender cada item quando aplicável. 

Os dispositivos e equipamentos registrados na etapa poderão ser avaliados e/ou retirados através da tela de "Dispositivos e equipamentos", na aba de controles de enfermagem, após a finalização da etapa.

Cultura e Anátomo Patológico

O usuário poderá registrar as culturas e peças de anátomo patológico coletadas e enviadas ao laboratório para garantir que os dados tenham rastreabilidade. As informações serão exibidas em uma tabela contendo as colunas: Hora, Tipo, Material coletado, Local e Enviado ao laboratório.

Para adicionar os itens clique no botão “Adicionar” ” e uma modal será exibida com os campos para preenchimento:

* Tipo: exibe as opções “Cultura” e “Anátomo patológico”.
* Material coletado
* Local
* Horário
* Enviado ao laboratório: exibe as opções sim e não.
* N° de peças / fragmentos
* Total de frascos enviados
* Observação: campo de texto livre.

Para finalizar a inclusão ou edição, clique no botão “Salvar”. Ao clicar no ícone de opções o usuário poderá visualizar ou excluir o respectivo item.

Intercorrências

O usuário poderá registrar as intercorrências ocorridas durante o processo intra-operatório, para garantir que os dados sejam registrados e analisados posteriormente. As informações serão exibidas em uma tabela contendo as colunas: Hora, Qual e Ação realizada.

Para adicionar uma intercorrência, clique no botão “Adicionar” e uma modal será exibida com os seguintes campos para preenchimento:

* Horário: campo para registrar o horário em que ocorreu a intercorrência.
* Qual: campo de texto livre para registrar o ocorrido.
* Ação realizada: campo de texto livre para registrar a ação realizada durante a intercorrência.

Para finalizar a inclusão, clique no botão “Salvar”. Ao clicar no ícone de opções, o usuário poderá visualizar ou excluir o respectivo item.

Finalização

Para finalizar o preenchimento da etapa, o usuário deverá selecionar um dos seguintes desfechos:

* Cancelar cirurgia: ao selecionar essa opção, uma modal será exibida solicitando a justificativa do cancelamento da cirurgia. Após preencher a justificativa, a etapa pós-operatório será desabilitada o usuário será redirecionado para a tela de resumo.
* Suspender cirurgia: ao selecionar essa opção, uma modal será exibida solicitando a justificativa para a suspensão da cirurgia. Após preencher a justificativa, a etapa pós-operatório será desabilitada e o usuário será redirecionado para a tela de resumo.
* Encaminhar para UTI: ao selecionar essa opção, a etapa pós-operatório será desabilitada e o usuário será redirecionado para a tela de resumo.
* Óbito: ao selecionar essa opção, a etapa pós-operatório será desabilitada e o usuário será redirecionado para a tela de resumo.
* Encaminhar para RPA: ao selecionar essa opção, o usuário será redirecionado para a tela de resumo e a etapa pós-operatório continuará habilitada para preenchimento.

Durante o preenchimento da etapa, o registro ficará salvo como rascunho e, no fim da página, terá a sinalização “Em rascunho”, com a possibilidade de excluir as informações. Para excluir as informações inseridas nessa etapa, clique no botão “Excluir”. Após confirmar a ação, o usuário será redirecionado para a tela principal de processos cirúrgicos e o nome do profissional responsável pelo rascunho e as informações inseridas anteriormente serão apagadas sem possibilidade de recuperação dos dados. Para iniciar um novo preenchimento, basta entrar novamente na respectiva aba da etapa logado com o usuário do profissional responsável pelo registro - após acessar a aba, mesmo que um usuário diferente acesse a mesma etapa simultaneamente, ao tentar fazer uma alteração no formulário, uma mensagem de alerta será exibida informando que o preenchimento já foi iniciado por outro profissional.

Para confirmar o desfecho da cirurgia, selecione uma opção e clique no botão “Confirmar”. Após a confirmação, o usuário será redirecionado para o resumo. O nome e conselho do profissional responsável pelo preenchimento, data e hora da liberação e a justificativa, quando aplicável, ficarão registrados no fim da página após a confirmação e a situação do formulário será atualizada para “Finalizado”.

Após a finalização, não será mais possível excluir o registro, apenas suspender. Se for necessário alterar ou adicionar informações, o usuário poderá voltar à etapa e clicar no botão “Suspender” e em seguida “Habilitar edição”.  Ao habilitar a edição, os dados registrados em campos abertos e em outras seções serão recuperados para que o usuário faça a edição apenas nos campos necessários. Para salvar as alterações, selecione novamente o desfecho e clique no botão “Confirmar”.

Ao suspender a etapa, mesmo que não habilite a edição, os registros feitos nas tabelas de sinais vitais, dispositivos, equipamentos e ganhos e perdas serão imediatamente suspensos nas tabelas do formulário da SAEP e também nas respectivas tabelas da aba "Controles de enfermagem". Apenas os dispositivos avaliados e/ou retirados e equipamentos que foram retirados através da tela de dispositivos e equipamentos em controles de enfermagem serão exibidos como suspensos nas tabelas da SAEP, mas serão mantidos sem suspensão em controles de enfermagem para garantir a rastreabilidade. Se o usuário optar por habilitar a edição, todos os dados suspensos deverão ser registrados novamente. Ao finalizar novamente a etapa, os dados antigos serão mantidos como suspensos e os que foram adicionados durante a edição serão registrados como novos em controles de enfermagem, contendo o nome do profissional, conselho, data e hora da nova liberação.

c. Pós-operatório

## **c. Pós-operatório**

A etapa pós-operatório do SAEP é crucial para garantir uma avaliação detalhada do estado de saúde do paciente, identificar e gerenciar riscos, planejar e orientar o paciente adequadamente para a recuperação cirúrgica, facilitar a comunicação eficiente entre a equipe e aumentar a segurança do paciente ao assegurar que todos os cuidados necessários sejam cumpridos conforme os protocolos da instituição.

Ao acessar a aba da etapa pós-operatório, serão exibidas as seguintes seções para preenchimento:

Data de entrada e Hora de entrada

O usuário poderá registrar a data e o horário de entrada do paciente na sala de recuperação.

Escala de dor, scores e escalas, sinais vitais, glicemia capilar, dispositivos e ganhos e perdas:

O usuário poderá registrar a escala de dor, os resultados de scores e escalas, sinais vitais, glicemia capilar, dispositivos e ganhos e perdas utilizados e avaliados durante o pós-operatório, para garantir que os dados sejam registrados com segurança. Nesta etapa, os registros feitos na etapa intra-operatório não serão exibidos nas tabelas, todas deverão ser preenchidas com as informações referentes à etapa do pós-operatório.

Para registrar as avaliações, clique no botão “Adicionar” na respectiva tabela e a modal exibida será a mesma utilizada em  e . Todas as informações adicionadas nessa etapa também ficarão registradas na aba Controles de Enfermagem e Scores. Em cada tabela, ao clicar no ícone de opções o usuário poderá visualizar, editar ou suspender cada item, quando aplicável, alterando também as informações que ficam salvas na aba Controles de Enfermagem e Scores.

Os dispositivos registrados na etapa poderão ser avaliados e/ou retirados através da tela de "Dispositivos e equipamentos", na aba de controles de enfermagem, após a finalização da etapa.

Avaliação do curativo

O usuário poderá registrar as informações referentes aos curativos feitos no pós-operatório preenchendo os campos: Aspecto da ferida, Tipo de curativo e Descrição.

Intercorrências

O usuário poderá registrar as intercorrências ocorridas durante a etapa do pós-operatório, para garantir que os dados sejam registrados e analisados posteriormente. As informações serão exibidas em uma tabela contendo as colunas: Hora, Qual e Ação realizada.

Para adicionar uma intercorrência, clique no botão “Adicionar” e uma modal será exibida com os campos para preenchimento:

* Horário: campo para registrar o horário em que ocorreu a intercorrência.
* Qual: campo de texto livre para registrar o ocorrido.
* Ação realizada: campo de texto livre para registrar a ação realizada durante a intercorrência.

Para finalizar a inclusão ou edição, clique no botão “Salvar”. Ao clicar no ícone de opções, o usuário poderá visualizar ou excluir o respectivo item.

Complemento

Para registrar mais informações pertinentes ao pós-operatório, o usuário poderá utilizar o campo “Complemento”.

Data de saída e Hora de saída

O usuário poderá registrar a data e o horário de saída do paciente da sala de recuperação.

Finalização

Para finalizar o preenchimento da etapa, o usuário deverá selecionar um dos seguintes desfechos:

* Encaminhar para UI: ao selecionar essa opção, o usuário será redirecionado para a tela de resumo.
* Encaminhar para UTI: ao selecionar essa opção, o usuário será redirecionado para a tela de resumo.
* Retornar para sala cirúrgica: ao selecionar essa opção, o usuário será redirecionado para a tela de resumo.
* Óbito: ao selecionar essa opção, a etapa pós-operatório será desabilitada e o usuário será redirecionado para a tela de resumo.

Durante o preenchimento da etapa, o registro ficará salvo como rascunho e, no fim da página, terá a sinalização “Em rascunho”, com a possibilidade de excluir as informações. Para excluir as informações inseridas nessa etapa, clique no botão “Excluir”. Após confirmar a ação, o usuário será redirecionado para a tela principal de processos cirúrgicos e o nome do profissional responsável pelo rascunho e as informações inseridas anteriormente serão apagadas sem possibilidade de recuperação dos dados. Para iniciar um novo preenchimento, basta entrar novamente na respectiva aba da etapa logado com o usuário do profissional responsável pelo registro - após acessar a aba, mesmo que um usuário diferente acesse a mesma etapa simultaneamente, ao tentar fazer uma alteração no formulário, uma mensagem de alerta será exibida informando que o preenchimento já foi iniciado por outro profissional.

Para confirmar o desfecho da cirurgia, selecione uma opção e clique no botão “Confirmar”. Após a confirmação, o usuário será redirecionado para o resumo. O nome e conselho do profissional responsável pelo preenchimento, data e hora da liberação e a justificativa, quando aplicável, ficarão registrados no fim da página após a confirmação e a situação do formulário será atualizada para “Finalizado”.

Após a finalização, não será mais possível excluir o registro, apenas suspender. Se for necessário alterar ou adicionar informações, o usuário poderá voltar à etapa e clicar no botão “Suspender” e em seguida “Habilitar edição”.  Ao habilitar a edição, os dados registrados em campos abertos e em outras seções serão recuperados para que o usuário faça a edição apenas nos campos necessários. Para salvar as alterações, selecione novamente o desfecho e clique no botão “Confirmar”.

Ao suspender a etapa, mesmo que não habilite a edição, os registros feitos nas tabelas de escala de dor, scores e escalas, sinais vitais, dispositivos, ganhos e perdas serão imediatamente suspensos nas tabelas do formulário da SAEP e também nas respectivas tabelas da aba "Controles de enfermagem" e "Scores". Apenas os dispositivos avaliados e/ou retirados da tela de dispositivos e equipamentos em controles de enfermagem antes da suspensão serão exibidos como suspensos apenas nas tabelas da SAEP, mas serão mantidos sem suspensão em controles de enfermagem para garantir a rastreabilidade. Se o usuário optar por habilitar a edição, todos os dados suspensos deverão ser registrados novamente. Ao finalizar novamente a etapa, os dados antigos serão mantidos como suspensos e os que foram adicionados durante a edição serão registrados como novos em controles de enfermagem, contendo o nome do profissional, conselho, data e hora da nova liberação.

d. Resumo

## **d. Resumo**

Ao acessar a aba “Resumo” o usuário poderá consultar rapidamente um resumo dos registros realizados nas fases pré, intra e pós-operatório, possibilitando ao usuário visualizar as informações críticas sem necessidade de navegar pelos registros completos.

O resumo exibirá as seguintes informações, quando houver:

* Tempos registrados: tempo de sala previsto, tempo total de cirurgia, tempo total de anestesia e tempo de recuperação na RPA.
* Equipe envolvida no intra-operatório.
* Gráficos demonstrando a evolução dos sinais vitais registrados, quantidade de dispositivos utilizados, balanço hídrico e escala de dor.
* Escala de dor e Scores e Escalas preenchidos.
* Dispositivos utilizados e avaliações registradas nas etapas.
* Intercorrências registradas.
* Cultura e anátomo patológico registrados.

e. Relatório padrão

## **e. Relatório padrão**

Para cada etapa da SAEP foi elaborado um relatório padrão e, para que o documento seja gerado em PDF, é necessário configurar cada relatório na respectiva unidade de atendimento no RM: **RM > Cadastros > Unidade de atendimento > Selecione a unidade de atendimento utilizada > aba "Relatórios" > adicione cada relatório individualmente: pré, intra e pós > Clique no botão "Salvar" para finalizar.**

Ao finalizar uma etapa - e realizar a assinatura digital quando for parametrizada para a unidade - um relatório será gerado em seguida contendo as informações registradas no formulário, a assinatura digital e também um campo reservado para assinatura manual.

Após gerar o documento corretamente, será adicionado no fim do formulário da etapa um link para visualizar o respectivo relatório contendo a data da assinatura digital, quando aplicável. Se posteriormente a etapa for suspensa e tiver a edição habilitada, o link será excluído e, após a finalização da edição, um novo link será adicionado para exibir o relatório contendo as informações editadas.

f. Suspensão/Cancelamento cirúrgico

## **f. Suspensão/Cancelamento cirúrgico**

Após o registro de um processo cirúrgico, o usuário poderá cancelar ou suspender uma cirurgia. Ao realizar a ação, a informação será refletida no pré-agendamento e na agenda cirúrgica.

Ao selecionar a opção **Cancelar** ou **Suspender,** será exibida uma modal onde o usuário deverá preencher o motivo da ação. Os motivos devem ser previamente cadastrados em: **RM > Cadastros > Cuidados com o paciente > Cirurgias > Motivos de suspensão de cirurgia.**

Após a confirmação, o card do processo cirúrgico terá o status alterado para **Cancelado**ou **Suspenso**. O status da tela de pré-agendamento e agenda cirúrgica também serão alterados com as mesmas informações.

Suspensão do formulário após finalizar a etapa:

Após finalizar uma etapa e o usuário necessitar fazer alguma alteração nos registros do formulário, **ao suspender a etapa, mesmo que não habilite a edição, os registros feitos nas tabelas de escala de dor, scores e escalas, sinais vitais, dispositivos, ganhos e perdas serão imediatamente suspensos nas tabelas do formulário da SAEP e também nas respectivas tabelas das abas "Controles de enfermagem" e "Scores", do menu lateral do PEP.** Apenas os dispositivos avaliados e/ou retirados diretamente na tela de dispositivos e equipamentos em controles de enfermagem antes da suspensão da etapa serão exibidos como suspensos apenas nas tabelas da SAEP, mas serão mantidos sem suspensão em controles de enfermagem para garantir a rastreabilidade. **Se o usuário optar por habilitar a edição, todos os dados suspensos deverão ser registrados novamente.** Ao finalizar novamente a etapa, os dados antigos serão mantidos como suspensos e os que foram adicionados durante a edição serão registrados como novos em controles de enfermagem e scores, contendo o nome do profissional, conselho, data e hora da nova liberação.

3. Exemplo de utilização - Cirurgia segura (12.1.2506)

## **03. Cirurgia Segura**

##### **Funcionalidade disponível a partir da versão 12.1.2506.**

A nova funcionalidade permite que os profissionais de saúde prescrevam, chequem e suspendam antibióticos profiláticos diretamente pelo card do procedimento cirúrgico no prontuário eletrônico do paciente. Esta funcionalidade não substitui os fluxos padrões de prescrição e checagem, mas oferece um atalho otimizado dentro do contexto cirúrgico.

CIRURGIA SEGURAa. Antibioticoprofilaxia cirúrgica

## **a. Antibioticoprofilaxia cirúrgica**

Ao acessar a aba de “Processos cirúrgicos” no menu lateral do PEP, dentro de cada card de cirurgia agendada o usuário encontrará o ícone de pílula (antibiótico) e terá uma prévia se há ou não antibióticos prescritos através das cores e alertas do ícone: 

* **Cinza:** Nenhum antibiótico prescrito nas últimas 48h.
* **Vermelho:** Existem antibióticos prescritos, mas um ou mais ainda não foram administrados.
* **Verde:** Todos os antibióticos prescritos foramadministrados.

Para acessar a tela principal de controle de antibióticos basta clicar no ícone de pílula. As principais funções dessa tela foram descritas nos tópicos a seguir.

Tela principal de controle de antibióticos e ações disponíveis

Ao clicar no ícone de pílula dentro de um card o usuário será redirecionado para a tela de controle, onde serão exibidos os antibióticos prescritos nas últimas 48 horas (independentemente da vigência da prescrição) e quando não houver antibióticos prescritos nas últimas 48 horas, uma mensagem de alerta será exibida para o usuário. Além do  botão "+ Prescrever", para prescrever um novo antibiótico para o paciente.

Após a prescrição do antibiótico, a tabela será exibida contendo:  

* Status:
  + Aguardando análise farmacêutica: antibiótico prescrito e em análise farmacêutica (apenas antibióticos prescritos através da tela principal de prescrição médica serão enviados para análise farmacêutica).
  + Aguardando aprazamento: antibiótico prescrito, não aprazado e não checado.
  + Aguardando checagem: antibiótico prescrito, aprazado e ainda não checado.
  + Realizado: antibiótico prescrito e checado.
  + Não executado: antibiótico prescrito, aprazado e "Não executado" na modal de checagem.
  + Prescrito: status exibido  após a liberação da prescrição e apenas para unidades de atendimento que não utilizam aprazamento e checagem.
* Antibiótico
* Dose
* Via
* Data/Hora checagem: preenchido apenas quando a unidade utilizar checagem e após a checagem).
* Ícone com o nome e conselho do profissional responsável, data e hora da liberação da prescrição.
* Ícone de opções:
  + Checar: o botão ficará habilitado para unidades de atendimento que utilizam checagem e apenas para antibióticos com o status "Aguardando checagem".
  + Suspender: o botão ficará habilitado apenas para antibióticos prescritos através da tela de processos cirúrgicos. Para antibióticos prescritos através da tela principal de prescrição médica o botão permanecerá desabilitado e, se necessário, devem ser suspensos na tela de origem.

Prescrição de antibióticos (modal de prescrição)

Para prescrever através da tela de processos cirúrgicos, o usuário poderá clicar no botão  "+ Prescrever" na tela de controle de antibióticos. Nessa tela, a modal foi adaptada para permitir um fluxo de prescrição mais fluido e específico, limitando a antibióticos com início imediato, sem envio do medicamento para análise farmacêutica e realizando o aprazamento automaticamente. Ao incluir o medicamento na modal de prescrição o aprazamento já será realizado em seguida, deixando o medicamento já disponível para checagem.

* A modal para prescrição nessa tela terá um filtro automático no campo de busca aplicado apenas para classe terapêutica de antibióticos, ou seja, apenas antibióticos serão exibidos na lista.
* O campo **"Frequência"** ficará habilitado para edição após a seleção do medicamento e seguirá a mesma regra da tela de prescrição médica:  quando há uma "Frequência de administração padrão" cadastrada para medicamentos no RM, o campo de "frequência" já será exibido preenchido com esse horário padrão e com isso, o campo de "início" já virá preenchido com a descrição "imediato". Se não houver esse cadastro, o campo de "Frequência" será exibido vazio e o campo de "Início" será exibido vazio e desabilitado, e, somente após o usuário selecionar uma frequência o campo será preenchido com a descrição "imediato". O campo "Frequência" também terá influência do cadastro de "Frequências de administração de medicamentos", sendo necessário verificar quais flags estão habilitadas para a respectiva frequência (ativo, dose única, ACM obrigatório, contínua e imediato)
* O campo **“Início”** permanecerá desabilitado para edição e sempre ficará com a descrição “Imediato” após a seleção de uma frequência, obedecendo a regra do campodescrita acima.
* O botão "Incluir" dessa modal tem a mesma ação do botão "Liberar" da prescrição médica, porém ao clicar o antibiótico já será incluído, liberado, aprazado e enviado para checagem, com apenas um clique.
* Após o usuário clicar no botão "Incluir" da modal, todos os dados preenchidos sempre ficarão registrados na tela principal de prescrição médica, além dos dados do profissional que prescreveu. Os relatórios de itens prescritos e de justificativa também poderão ser consultados e gerados no histórico da tela de prescrição médica.
* O medicamento será aprazado e liberado automaticamente para checagem, não sendo necessário realizar o aprazamento manualmente.
* O fluxo de prescrição por essa tela segue todas as regras padrões da prescrição médica:  
  + Validação de campos e dados obrigatórios: via, apresentação, quantidade/unidade, frequência, tempo de uso e duração do tratamento, alerta de interação medicamentosa cadastrada e alergias, alerta para medicamentos restritos pelo convênio e justificativa - se parametrizada como obrigatória para a unidade,
  + Checagem - para unidades de atendimento que utilizam checagem no PEP.

* Os medicamentos prescritos através da tela de processos cirúrgicos **não** serão enviados para análise farmacêutica - mesmo que a unidade de atendimento esteja parametrizada para utilizar análise, os antibióticos serão sempre enviados diretamente para checagem, sem executar essa etapa. Contudo, o fluxo de antibióticos prescritos via prescrição médica **não será alterado**:
  + Se a unidade de atendimento utiliza análise, após a liberação da prescrição o antibiótico será enviado para o painel de análise e o status na tela de processos cirúrgicos ficará como "aguardando análise farmacêutica". Não alterando também o fluxo de aprazamento/checagem. Se a unidade utiliza aprazamento/checagem depois da análise o antibiótico será enviado para aprazamento e depois checagem, normalmente. Se não utilizar aprazamento/checagem - depois da análise o antibiótico será enviado para o painel de dispensação.

* Caso o paciente ainda não possua uma prescrição vigente ou em rascunho, o sistema criará automaticamente a estrutura de prescrição antes de incluir e liberar o antibiótico.

Checagem de antibióticos (modal de checagem)

Para realizar a checagem através da tela de processos cirúrgicos, o usuário poderá clicar no botão "Checar" disponível no ícone de opções do respectivo antibiótico. Ao clicar no botão "Checar", será aberta amodal padrão de checagem de medicamentos, já com a descrição do antibiótico correspondente.

* A checagem por essa tela ficará habilitada apenas para antibióticos prescritos nas últimas 48h e não checados.
* Apenas o próximo horário imediato será exibido na tabela da tela inicial. Os próximos horários de administração de antibióticos prescritos com frequência diferente de dose única, deverão ser checados na tela principal de checagem.
* O registro da checagem segue o padrão já existente no sistema:  
  + Identificação do profissional
  + Data/hora da administração
  + Vínculo com o item prescrito
* As regras referentes as permissões para checagem seguem o padrão:  
  + Apenas perfis autorizados podem checar
  + A administração deve respeitar horários permitidos
* A funcionalidade de checagem de medicamentos com código de barras do produto e identificação do paciente através da leitura da pulseira de identificação podem ser utilizadas se a unidade de atendimento estiver parametrizada no RM.
* Após o usuário clicar no botão "Executar" ou "Não executar" da modal, todos os dados preenchidos sempre ficarão registrados na tela principal de checagem, além dos dados do profissional que checou. Os relatórios de checagem também poderão ser consultados e gerados na tela principal de checagem.

Suspensão de antibióticos

Para realizar a suspensão de um antibiótico através da tela de processos cirúrgicos, o usuário poderá clicar no botão "Suspender" disponível no ícone de opções do respectivo antibiótico. Ao clicar no botão "Suspender", será aberta umamodal para confirmação ou cancelamento da ação. Ao confirmar a suspensão, o medicamento seguirá o fluxo padrão de suspensão na prescrição, aprazamento, painel de dispensação e checagem.

* O botão "Suspender" ficará habilitado apenas para antibióticos prescritos através da tela de processos cirúrgicos e que ainda não foram checados. Para antibióticos prescritos através da tela principal de prescrição médica o botão permanecerá desabilitado e, se necessário, devem ser suspensos na tela de origem.

* Em unidades que não utilizam aprazamento e checagem, a opção de "Checar" ficará desabilitada e apenas a opção de "Suspender" será habilitada.

b. Atalho para protocolos assistenciais

## **b. Atalho para protocolos assistenciais**

Ao acessar a aba “Processos cirúrgicos” no menu lateral do PEP, o card de cirurgia passa a exibir o botão“Protocolos”, posicionado ao lado do botão SAEP.

Esse novo atalho tem como objetivo facilitar o acesso do profissional à tela de , permitindo que sejam rapidamente abertos e acompanhados durante o período perioperatório.

**Exemplo de utilização:**

Ao clicar no botão "Protocolos", o usuário será redirecionado para o menu "Protocolos assistenciais" para visualizar a listagem dos protocolos vinculados ao paciente. 

O usuário poderá realizar as ações já existentes no módulo de Protocolos assistenciais, como:

* Criar novo protocolo (**+** Novo)
* Abrir, preencher e finalizar o protocolo em andamento
* Filtrar protocolos registrados
