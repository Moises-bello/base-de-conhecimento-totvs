---
content_hash: ba478eb1cb93d96ae465b891d7e48aba31d47cc6314944774e04db47101f0164
fetched_at: '2026-06-29T00:10:58.008204+00:00'
page_id: '602629333'
product: rm
source: tdn-rm
title: Autorização da Instituição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=602629333
version: 15
---

A partir da versão 12.1.32 será possível informar as autorizações da instituição de ensino pelo anexo da instituição de ensino.

Esta mesma tela já estava presente no anexo do cadastro da Instituição do MEC, utilizada no  em versões anteriores.

Sendo aberta pela o anexo da Instituição de ensino, este cadastro permite informar o credenciamento e o recredenciamento da IES registradora do Diploma, quando a IES apenas emite e não registra diplomas. Caso ela seja utilizada pelo anexo da Instituição do MEC, o cadastro será utilizado para compor as informações do censo escolar.

Vale lembrar que apenas **um registro válido** será permitido para cada **ato regulatório.** Por exemplo, se já existir um registro com o ato regulatório **Credenciamento**e este está marcado com **última autorização válida**, ao tentar criar ou editar um registro e marcar para ser o último válido e salvar, o sistema exibirá uma mensagem informando que já existe outro registro marcado como última autorização válida e se deseja remover e atribuir como última autorização o registro atual. Caso o usuário clique em "Sim", o sistema irá atribuir como última autorização válida o registro atual e o antigo terá esse campo desmarcado.

Foi disponibilizados mais tipos de autorização / reconhecimento, conforme abaixo.

**Observação!!!** Com a finalidade de atender a legislação do MEC sobre o envio de dados do Diploma digital, foram realizadas adequações ao Layout do Diploma digital, assim os campos referente a **Tramitação** foram  incluídos na tela. Disponível apenas para o ensino superior.

A partir das versões **12.1.2502.222, 12.1.2506.169 e 12.1.2510.101**, foram implementadas as seguintes alterações na tela:

* O campo **“Modalidade”** foi renomeado para **“Nível de Ensino”**.
* Para o **Nível de Ensino Superior e Habilitação Tecnica**, as Autorizações MEC foram segregadas por **Modalidade** — *Presencial, À Distância ou Unificado*.
* O preenchimento do campo de **Modalidade** é **obrigatório**.

Com esta mudança, a regra do campo “Última autorização válida” passa a levar em conta a **Modalidade** quando se trata do Ensino Superior.

Dessa forma, o sistema irá validar o campo com base na combinação: Ato regulatório + Nível de Ensino + Modalidade, permitindo ter mais de uma “Última autorização válida” desde que as modalidades sejam diferentes.

**Exemplo:**

* Pode existir para uma instituição um Credenciamento de Ensino Superior – Presencial como “Última autorização válida”.
* E, ao mesmo tempo, um Credenciamento de Ensino Superior – EAD também como “Última autorização válida”.

Essa regra vale para os atos de Credenciamento, Recredenciamento e Renovação de Credenciamento.
