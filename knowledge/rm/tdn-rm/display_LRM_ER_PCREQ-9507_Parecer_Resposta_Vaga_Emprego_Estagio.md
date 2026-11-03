---
content_hash: 1b1970a9b135be7427272051f76665027385ca335e00723f72dfa4be1c0816e7
fetched_at: '2026-06-29T00:06:24.164277+00:00'
page_id: '224113605'
product: rm
source: tdn-rm
title: ER_PCREQ-9507_Parecer_Resposta_Vaga_Emprego_Estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9507_Parecer_Resposta_Vaga_Emprego_Estagio
version: 128
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Educacional | **Módulo** | Educacional |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | WBS\_R\_EDU016\_1219 | **IRM1** | PCREQ-9504 |
| **Requisito1** | PCREQ-9507 | **Subtarefa1** | PDR\_EDU\_EDU019-2 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.10 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos)

## Objetivo

O objetivo dessa implementação é permitir que seja informado um parecer de resposta para vagas de emprego/estágio na tela de candidatos à vaga, do módulo de estágio do TOTVS Educacional. 

## Definição da Regra de Negócio

Será criado novo campo no cadastro de Candidatos à vaga (figura 1), conforme descrito no item dicionário de dados abaixo, para permitir que o usuário informe um parecer de resposta para a vaga de emprego/estágio que um determinado usuário tenha se candidatado.

Esse novo campo não será obrigatório.

Ao realizar a alteração do status da candidatura para "Selecionado", caso o parecer não tenha sido preenchido, uma mensagem será emitida para o usuário indicando que ele deve preencher o parecer caso queira enviar alguma informação adicional ao candidato.

Será realizada alteração nas seguintes mensagens de notificação, da central de notificações, para incluir nova TAG com esse campo de parecer (figura 2), para que o usuário tenha flexibilidade de utilizá-la ao notificar o candidato via e-mail ou fluig.

* Informar ao aluno que ele foi selecionado para a vaga de estágio na qual está inscrito.
* Informar ao aluno que ele NÃO foi selecionado para a vaga de estágio na qual está inscrito.

Esse novo campo de parecer também será exibido no portal (figura 3), para cada vaga do usuário que estiver sendo exibida no acompanhamento de estágio/emprego. O campo só será exibido no portal caso esteja preenchido.

Será feita alteração também nas novas telas da experiência 8 (figura 4) para incluir o campo de parecer na edição dos candidatos da vaga. Nesse caso, o campo também não será obrigatório.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Candidatos à vaga | [Alteração] | TOTVS Educacional -> Atividades Acadêmicas ->Acadêmico -> Estágio -> Candidatos à vaga | - |
| Central de Notificações | [Alteração] | TOTVS Educacional -> Atividades Acadêmicas -> Central de Notificações -> Mensagens de Notificação | - |
| Candidatos à vaga | [Alteração] | Fluig | - |
| Acompanhamento | [Alteração] | Portal RM -> Educacional -> Acadêmico -> Estágio/Emprego -> Acompanhamento | - |

## Protótipo de Tela

Figura 1

Figura 2

Figura 3

Figura 4

 

## Dicionário de Dados

|  |  |
| --- | --- |
| **Campo** | SVAGASCANDIDATOS.PARECER |
| **Tipo** | MEMO |
| **Tamanho** | MEMO |
| **Valor Inicial** | VAZIO |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Parecer de resposta para vagas de emprego/estágio |
| **Título** | Parecer |
| **Help de Campo** | Campo utilizado para informar o parecer de resposta para a vaga de emprego/estágio no módulo de estágio do TOTVS Educacional. |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
