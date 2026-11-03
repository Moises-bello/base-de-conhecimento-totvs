---
article_id: 360062309054
category: MDT - Atendimento Médico
content_hash: d1c435121b05fb6ee2b923c89d600dc76db0154fefeadf19bef3cd617744ba7d
fetched_at: '2026-06-28T22:44:20.599753+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Como enviar workflow de Aviso em casos de  Transferência
  da Consulta
type: support-article
updated_at: '2025-09-02T17:00:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062309054-RH-Linha-Protheus-MDT-Como-enviar-workflow-de-Aviso-em-casos-de-Transfer%C3%AAncia-da-Consulta
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27571104204695)**Tempo aproximado para leitura: 00:02:00 min  
Dúvida**Como enviar workflow de Aviso em casos de Transferência da Consulta?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Deverá acessar o **Configurador,** localizar e ativar o parâmetro **MV\_NG2CTRC** conforme exemplo abaixo.  
  
![Ao66ctdGdW.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360102859874)  
  
Ao transferir um atendimento médico através da rotina  Agenda Médica Modelo 2 (**MDTA076**), após confirmar os dados de transferência de atendimento podendo ser: o Médico, o dia ou horário, será enviado um e-mail ao **Médico** e ao **Funcionário**.   
  
Importante ressaltar que no cadastro do Usuário Sesmt  o Medico relacionado ao processo deverá ter  seu e-mail informado através do preenchimento do campo (**TMK\_EMAIL)** .

E no cadastro da **Ficha Médica** envolvida no processo deverá estar relacionado a uma **matricula** e o campo (**SRA\_EMAIL**) deve estar preenchido.  
  
O parâmetro **MV\_NG2COMA** deverá estar em branco.

Demais informações sobre configurações de disparo de Workflow consulte [aqui](https://tdn.totvs.com/display/PROT/TUYU89_DT_WF_Comunicacao_SESMT).  
  
Exemplo de cadastro e disparo de Workflow.  
  
![XhltVMv8KF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360102863794)  
  
**Importante**: Esta funcionalidade para disparo de workflow, está disponível apenas para Fichas Médicas vinculadas a matricula. Caso seja uma ficha médica relacionado a um candidato, não será disparado o Workflow.   
  
**Saiba Mais**[Artigos sobre Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT)  
[Artigos sobre Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico)
