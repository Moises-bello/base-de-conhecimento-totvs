---
article_id: 360052521873
category: RH - Cadastros
content_hash: 55bd7cab6e9fb0e4406157ff82e608cf296dbdf0ed2db878f9c35cd2da1a6bff
fetched_at: '2026-06-28T22:44:52.720865+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON -  Para que serve o campo de Turno Opcional no cadastro
  do Turno de Trabalho
type: support-article
updated_at: '2025-06-16T18:11:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052521873-RH-Linha-Protheus-PON-Para-que-serve-o-campo-de-Turno-Opcional-no-cadastro-do-Turno-de-Trabalho
---

**Dúvida**Para que serve o campo de Turno Opcional no cadastro do Turno de Trabalho?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O **campo de Turno Opcional** existente no **cadastro do Turno de Trabalho**, serve para que o funcionário associado ao turno principal, tenha a mobilidade de fazer também o horário previsto no Turno Opcional, sem que seja necessário realizar uma Troca de Turno, por exemplo:  
  
Funcionário está atrelado ao turno 01 que tem horário previsto na Tabela de Horário Padrão das 08h às 17h  
No cadastro do turno 01, informamos o turno 02 como opcional, que tem horário previsto na Tabela de Horário Padrão das 10h às 19h  
  
Se em um dia o funcionário realizar entrada às 09h30, por exemplo, o sistema automaticamente entenderá que este horário está mais próximo do horário previsto no Turno Opcional, portanto, será considerado neste dia a jornada e o horário das 10h às 19h, automaticamente.  
  
O **Turno Opcional** funciona também quando existem várias sequências com horários diferentes na Tabela de Horário Padrão, então neste caso, o próprio turno pode ser informado como opcional, por exemplo:  
  
No cadastro do turno 03, existem 02 sequências na Tabela de Horário Padrão, sendo:  
Sequência 01 - horário das 08h às 17h  
Sequência 02 - horário das 10h às 19h  
  
Informando o próprio turno 03 como turno opcional, quando o funcionário fizer entradas próximas do horário da sequência 01, o sistema entenderá que deve considerar esta sequência, quando o horário for próximo do previsto na sequência 02, o sistema entenderá que deve considerar esta.  
  
Para que o funcionamento do Turno Opcional ocorra, é necessário que o parâmetro MV\_TNOOPC esteja como S.

**Importante****:** Caso o turno não tenha duas sequencias cadastradas, não deverá ser atrelado.

**Informações complementares**<https://tdn.totvs.com/display/public/PROT/PON0029_Turnos_opcionais>  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
