---
content_hash: c8c6bf8da4496ce7a955e0fca323d55b573c63671d80a9c4cfe4aa0c2803800b
fetched_at: '2026-06-29T00:11:20.493866+00:00'
page_id: '685002188'
product: rm
source: tdn-rm
title: Agendamento por Sessão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=685002188
version: 29
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configuração**
3. **Utilização**

itensVisão Geral

## **01.****VISÃO GERAL**

Esta funcionalidade permite realizar atendimentos em série, seja eles de consulta normal ou por protocolos de oncologia.  
Para marcar agendamentos de consulta é necessário selecionar a especialidade, o profissional e o número de consultas e logo após selecionar as datas e horários livres, após o termino o sistema criará na data(s)/horário(s) selecionado(s) o compromisso.  
Para marcar agendamento de protocolos de oncologia é necessário selecionar o protocolo, a fase o ciclo e a unidade onde será realizado procedimento, a quantidade de agendamentos realizados será feita conforme configurado no protocolo.

## **Assista as pequenas guias!**

Configuração

## **02.** **CONFIGURAÇÃO**

**Agendamento Protocolo Oncologia**

Em Agendamento/Agenda selecione uma agenda observando se a unidade é a desejada e marque a opção **Utiliza Protocolo de Oncologia,** e o tipo da agenda tem que ser **SALA.**

Depois vá na agenda de atendimentos selecione a mesma agenda e adicione a especialidade de oncologia caso a mesma ainda na tenha sido adicionada.

**Agendamento de Consultas**  
Não exige nenhuma configuração específica.

Nas condições contratuais algumas informações tem que estar preenchidas

Para que a GUIA seja gerada o seguinte parâmetro deve ser marcado nos parâmetros gerais:

Utilização

## **03.** **UTILIZAÇÃO**

Acesse a agenda de atendimentos e clique no botão **Agendamento por Sessão.**

Será apresentada a tela principal do agendamento por sessão, selecione o paciente desejado.

Paciente, convênio e atividade são informações obrigatórias para gerar uma nova sessão.

Para visualizar uma sessão criada, selecione um item no grid e dê um clique duplo com o mouse.

Para excluir uma sessão, selecione um item no grid e clique no botão **Excluir Marcação**

Confira os dados, selecione as sessões e se tiver certeza clique no botão **Avançar**.

Pra este exemplo selecionei as sessões 4 e 5

Clique no botão **Executar**.

No final do processo de exclusão será exibido um resumo.

A marcação só poderá ser excluída caso o agendamento ainda estiver em aberto, ou seja, se existir um ou mais atendimentos para os compromissos selecionados da sessão será exibida uma mensagem.

Após a exclusão o resultado esperado:

Para criar uma nova marcação, selecione um paciente, informe os dados e clique no botão **Nova Marcação**.

Nesta tela o usuário seleciona o tipo de marcação que vai ser realizada, se é consulta por especialidade ou se é por protocolo de oncologia.

Na figura abaixo foi selecionado agendamento por especialidade, onde é obrigatório o campos Especialidade, depois informe o período ou número de consultas e clique no botão Ok e o sistema se encarrega de criar as linhas no grid.  
(caso tenha preenchido os dias da semana, horário, período, o sistema se encarregara de trazer as linhas preenchidas).

**IMPORTANTE:** Apenas os profissionais com credenciamento vigente para o convênio selecionado serão exibidos.

Caso tenha inserido os dias da semana, horário, período, o sistema se encarregara de trazer as linhas do grid preenchidas.

O sistema também alterar os valores preenchidos:

Clique na coluna data de uma determinada linha do grid o sistema exibe um calendário idêntico ao da agenda de atendimentos com as mesmas propriedades, selecione uma data.

Ainda na mesma linha do grid, porém na coluna hora será exibido uma lista com os horários disponíveis para o agendamento, selecione um e execute o mesmo processo para a segunda linha do grid

Depois clique em avançar e em seguida em executar e ao final do processo será exibido uma tela com o resumo.

Para o agendamento de protocolo de oncologia, selecione a opção em destaque na figura abaixo, onde são obrigatórios os campos Protocolo, Fase, Ciclo e unidade, o número de consultas vai ser determinado pelo ciclo.

No grid o sistema já se encarrega de preencher a datas no grid conforme intervalo configurado no ciclo e conta como data prevista a data atual

Para alterar a data prevista basta clicar no botão ao lado da mesma e selecionar uma nova data.

Depois de selecionada a nova data, clique no botão Ok e as datas do grid serão atualizadas.

Na coluna hora, para cada linha do grid será exibida uma lista com todos os horários e agendas disponíveis configurados na unidade que foi selecionada.

Selecione um horário para cada linha do grid.

Depois clique em avançar e em seguida em executar e ao final do processo será exibido uma tela com o resumo igual a do processo de agendamento de consulta.

Ao gerar os atendimento referentes a agenda de sessão vai ser possível acompanhar na aba "Informações →  Agenda de Sessões"

Apenas no primeiro atendimento será possível verificar a GUIA, os demais atendimentos a tela fica em branco. Cada atendimento gerado vai ser criado um registro na guia, e subsequentemente o registro na parcial.

O mesmo será o resultado ao acessar a elaboração de contas.
