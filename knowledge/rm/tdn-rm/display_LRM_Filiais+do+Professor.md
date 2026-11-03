---
content_hash: ac005364969829b4d8e7ef635ad1a35adcaf163b206f7c02fe8a9ca4fd027afa
fetched_at: '2026-06-29T00:10:26.763278+00:00'
page_id: '514731639'
product: rm
source: tdn-rm
title: Filiais do Professor
type: documentation
url: https://tdn.totvs.com/display/LRM/Filiais+do+Professor
version: 7
---

Nesta tela é possível realizar o cadastro das filiais que o professor tem acesso dentro do sistema.

A flag "Ativo", existente nesse cadastro, define se o cadastro está ativo ou não para o professor na filial selecionada no campo "Cód.Filial".

Um ponto importante sobre a desmarcação dessa flag está relacionado ao vínculo que ela possui com a flag "ativo" do cadastro do usuário. Ao desmarca-la, o usuário também será desativado, caso nenhuma das seguintes condições sejam verdadeira:

* Possuir cadastro ativos para outras filiais.
* Possuir matrícula ativa (ou seja, ser aluno ativo na instituição).
* Ser funcionário ativo (PFUNC).
* Caso o professor for responsável de algum aluno.
  + **Obs.:** Para a validação do **Responsável Financeiro (SALUNO.CODCFO)**, o sistema irá verificar as seguintes situações:
    1. O Professor possuir o mesmo CPF que um Cliente/Fornecedor associado a um aluno.
    2. A "Pessoa" do Professor estiver relacionada a um Cliente/Fornecedor **(FCFOPPESSOA.CODPESSOA)** associado a um aluno.

Chapa

O anexo Chapa, permite vinculo de chapas independente da filial.  
  
Cenários possiveis: 

* Professor 1 - Filial selecionada 1 - Chapa vinculada a Filial 1 = deve salvar normalmente sem intercorrências.
* Professor 1 - Filial selecionada 1  - Chapa vinculada a Filial 2 = emite um aviso informando que a chapa selecionada não pertence a filial, somente aviso, pois permite salvar normalmente.
