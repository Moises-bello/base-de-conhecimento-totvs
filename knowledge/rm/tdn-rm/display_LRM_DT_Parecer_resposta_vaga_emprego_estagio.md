---
content_hash: 2dd74685d561ef8abde7193b86e4dad25634ec9c4d2e26ddde0115296fd71016
fetched_at: '2026-06-29T00:06:24.988806+00:00'
page_id: '224128422'
product: rm
source: tdn-rm
title: DT_Parecer_resposta_vaga_emprego_estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Parecer_resposta_vaga_emprego_estagio
version: 121
---

# Parecer de resposta para vaga de emprego/estágio

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *TOTVS Educacional* |
| **Módulo:** | *Estágio/Emprego* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro candidatos à vaga | Cadastro candidatos à vaga | | Central de notificações | Central de notificações | | Acompanhamento Estágio/Emprego (Portal) | Acompanhamento Estágio/Emprego (Portal) | | Candidatos à vaga (Experiência #8 - FLUIG) | Candidatos à vaga (Experiência #8 - FLUIG) | |
| **Requisito (ISSUE):** | PCREQ-9507 |
| **País(es):** | *Brasil* |
| **Tabelas Utilizadas:** | *SVAGASCANDIDATOS* |

## Descrição

O objetivo dessa funcionalidade é permitir que seja informado um parecer de resposta para vagas de emprego/estágio na tela de candidatos à vaga, do módulo de estágio do TOTVS Educacional.

## Procedimento para Utilização

Foi criado novo campo no cadastro de Candidatos à vaga (figura 1), para permitir que o usuário informe um parecer de resposta para a vaga de emprego/estágio que um determinado usuário tenha se candidatado.

Esse novo campo não será obrigatório.

Foram alteradas as seguintes mensagens de notificação, da central de notificações, para incluir nova TAG com esse campo de parecer (figura 2), para que o usuário tenha flexibilidade de utilizá-la ao notificar o candidato via e-mail ou fluig.

* Informar ao aluno que ele foi selecionado para a vaga de estágio na qual está inscrito.
* Informar ao aluno que ele NÃO foi selecionado para a vaga de estágio na qual está inscrito.

Esse novo campo de parecer também será exibido no portal (figura 3), para cada vaga do usuário que estiver sendo exibida no acompanhamento de estágio/emprego. O campo só será exibido no portal caso esteja preenchido.

As novas telas da experiência 8 (figura 4) também sofreram alteração, para incluir o campo de parecer na edição dos candidatos da vaga. Nesse caso, o campo também não será obrigatório.

Figura 1

 

Figura 2

Figura 3

Figura 4

divs
