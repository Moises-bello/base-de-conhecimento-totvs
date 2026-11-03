---
content_hash: e3df0cfd71ce59756f08ea90b2d7b6e80d26c73b24901cb7fea6eb311eb208bc
fetched_at: '2026-06-29T00:06:25.428919+00:00'
page_id: '224396690'
product: rm
source: tdn-rm
title: ER_PCREQ-9513_Egressos_poderem_fazer_inscrição_em_vagas_de_emprego
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224396690
version: 132
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | WBS\_R\_EDU016\_1219 | **IRM1** | PCREQ-9512 |
| **Requisito1** | PCREQ-9513 | **Subtarefa1** | PDR\_EDU\_EDU019-15 |
| **Chamado2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

O objetivo dessa implementação é permitir que alunos egressos possam fazer inscrição em vagas de emprego disponíveis para seu curso/habilitação concluído, através do módulo de emprego/estágio do RM Portal. 

## Definição da Regra de Negócio

**Para ser considerado egresso o aluno precisa ter a opção "Indica conclusão do curso" marcada, na aba "Status no curso" da "Situação de matrícula" do seu curso/habilitação.**

**Será feito ajuste para permitir que o aluno egresso consiga realizar inscrição em vagas de emprego que tenham seu "curso/habilitação" como público alvo dessa vaga.**

****O botão de "Inscrever" deverá aparecer ao lado das vagas de emprego listadas para que o aluno egresso possa efetuar sua inscrição, conforme protótipo abaixo.****

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Acompanhamento | [Alteração] | Portal RM -> Educacional -> Acadêmico -> Estágio/Emprego -> Acompanhamento | - |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
