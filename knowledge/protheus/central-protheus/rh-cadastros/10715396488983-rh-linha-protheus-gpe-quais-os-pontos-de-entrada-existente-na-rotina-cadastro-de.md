---
article_id: 10715396488983
category: RH - Cadastros
content_hash: 9383487e0aa5ac2033ddd302d29f4b132aa40218cf2549c644d1183fd0859b0d
fetched_at: '2026-06-28T22:43:25.962069+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Quais os Pontos de Entrada existente na rotina
  Cadastro de Tarefas GPEA190
type: support-article
updated_at: '2026-06-25T12:17:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10715396488983-RH-Linha-Protheus-GPE-Quais-os-Pontos-de-Entrada-existente-na-rotina-Cadastro-de-Tarefas-GPEA190
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16003755181591) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Quais os Pontos de Entradas existente na rotina **Cadastro de tarefas** (GPEA190*)?.*  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
Segue lista dos Pontos de Entradas existentes na rotina **Cadastro de tarefas** (GPEA190*).*  
  
1 - **Gp190VPE** - Este ponto de entrada permite validar a inclusão de determinada tarefa.

O *array aCols* contém todas as tarefas cadastradas e a variável **N** contem a posição do *array* que esta sendo validada.

Deverá ser retornado **.T.** para validar a inclusão da tarefa, ou **.F.**, para bloqueá-la. Convém retornar uma mensagem informando a razão do eventual bloqueio na inclusão

**Mais detalhes:** [Ponto de Entrada GP190VPE](https://tdn.totvs.com/display/public/PROT/DT_PE_GP190VPE_Validacao_Tarefa)  
  
2- **GP190TudOk** - Este ponto de entrada tem como objetivo permitir **criar validações ao confirmar a inclusão de uma tarefa**.

O ponto de entrada é executado ao final das validações padrões da função **GP190TudOk().**

**Mais detalhes:** [Ponto de entrada GP190TudOk](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051698014-RH-Linha-Protheus-GPE-Ponto-de-entrada-GP190TudOk)  
  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Como incluir uma tarefa GPEA190](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052465813-RH-Linha-Protheus-GPE-Como-incluir-uma-tarefa-GPEA190)  
[Artigos Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)  
[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
