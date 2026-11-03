---
content_hash: fe1dfc6b6b2db0aca3b12685aed6bca52c6296b6b07e43e62ec5854415e6062f
fetched_at: '2026-06-29T00:11:11.724094+00:00'
page_id: '648418427'
product: rm
source: tdn-rm
title: Painel de atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Painel+de+atendimento
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

sumarioVisão Geral

## **01. VISÃO GERAL**

Recurso de classificação de risco, utilizando o mesmo critério de classificação do protocolo de Manchester.

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Após a realização do registro de atendimento no RM, caso a unidade selecionada possua triagem habilitada (conforme parâmetro do RM), os pacientes passam a ser exibidos no Painel de Urgência/Emergência para acompanhamento do fluxo assistencial.

No PEP RM, o caminho até o painel é "Painéis" -> "Urgência e Emergência".

* Nesta tela são listados todos os pacientes presentes no painel, independentemente do status atual do atendimento, respeitando os filtros aplicados
* Tem a possibilidade de visualizar apenas os pacientes que estão no status que correspondem à enfermagem, os que correspondem ao atendimento médico ou todos os pacientes.  
  Na regra de filtro, deverá ser considerado o usuário logado para a exibição inicial. Ex: Se o usuário possui o conselho do tipo CRM, deverá ser aberto com a visão Médico, com o filtro médico selecionado. Se o usuário possui o conselho do tipo COREN, deverá ser aberto com a da Enfermagem, com o filtro enfermagem selecionada.
* Tem a possibilidade de buscar por determinado paciente da lista que consta no painel.
* Botão de chamar próximo, que obedece a seguinte regra:   
  Se usuário de enfermagem estiver acessando e clicar no botão de chamar próximo, será chamado o próximo paciente da fila que estiver com o status de "aguardando triagem".  
  Se for o usuário médico, ao clicar em chamar próximo, será chamado o próximo paciente com o status de aguardando.
* Status:  
  Aguardando -> quando o paciente já passou pela triagem e está aguardando atendimento médico.  
  Em atendimento -> quando o paciente está em atendimento pelo médico.  
  Aguardando triagem -> quando o paciente está aguardando para realização da triagem  
  Em triagem -> quando iniciada a triagem do paciente, mas ainda não foi finalizada.  
  Em observação -> quando o paciente está no status de transição entre em atendimento e finalizado.  
  Finalizados -> quando o atendimento foi finalizado.

* Existem duas sinalizações em tela:   
  Quando a senha for prioritária, ela estará sinalizada de vermelho no painel.   
  Quando o tempo de espera ultrapassar o tempo definido no parâmetro, este também deverá ficar em vermelho.

* Ao clicar no ícone de informações da triagem, é possível visualizar dados adicionais como:

  + Convênio
  + Tipo de senha
  + Responsável pela triagem
