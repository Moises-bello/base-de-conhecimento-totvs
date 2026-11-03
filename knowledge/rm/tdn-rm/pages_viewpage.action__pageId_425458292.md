---
content_hash: c25a813520e6e83b6266a8b705191b807ac41d6f839540dead89230a4db52eac
fetched_at: '2026-06-29T00:09:29.817198+00:00'
page_id: '425458292'
product: rm
source: tdn-rm
title: Alterar Status da opção do candidato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458292
version: 4
---

O candidato possui um status de opção para cada uma das áreas ofertadas na qual ele se inscreveu. Este processo permite alterar o status desta opção de inscrição na área ofertada caso necessário. É possível alterar o status da opção do candidato para as opções abaixo:

* Inscrito para seleção
* Ausente em dia de prova
* Desclassificado por entrevista
* Desclassificado por insuficiência de perfil
* Desclassificado por uso de meios ilícitos

Caso o candidato esteja em algum status abaixo, que são os status que definem que o candidato foi chamado, este não poderá ter o status de opção alterado:

* Em chamada
* Compareceu à chamada
* Não compareceu à chamada
* Convocado para outra opção

Se a lista de candidatos selecionados contiver candidatos com status **“Inscrito (pendente de confirmação de pagamento)”**, **“Excedente”** ou **“Cancelado”**, a mensagem abaixo será exibida ao abrir o processo.

**Lembrando** que estas descrições citadas podem ser redefinidas caso necessário no menu Status da opção em Tabelas auxiliares do Processo seletivo.

Funções auxiliares:

* Botão "Limpar alterações" serve para limpar o valor do campo "Novo status" de todas as opções no grid que tiveram status alterado de uma única vez.
* Botão "Alterar todos para" serve para definir um mesmo valor para o campo "Novo status" em todas as opções que é permitido alterar no grid de uma única vez.

Importante

Para áreas ofertadas que possuem mais de uma etapa:

Não será possível alterar o status de opção de um candidato caso ele esteja "Classificado para a próxima etapa" e a etapa atual for a 2ª ou superior, ou seja, o candidato para ter o status retornado para "Inscrito para seleção", deverá estar "Classificado para a próxima etapa" sendo que a etapa atual deve ser a **1ª**.

Aviso

A alteração do status de opção de um candidato "Classificado para chamada" para "Inscrito para seleção", poderá ocasionar em lacunas na **ordem de classificação atual**, sendo que mesmo que o candidato seja reclassificado, o mesmo não retornará para posição de classificação em que estava, será incluído na sequência da lista de classificados.   
  
Exemplo:

**Ordem de classificação** antes da alteração de status:

| Candidato | Status da opção | Ordem de classificação |
| --- | --- | --- |
| Candidato 1 | Classificado para chamada | 1 |
| Candidato 2 | Classificado para chamada | 2 |
| Candidato 3 | Classificado para chamada | 3 |
| **Candidato 4** | **Classificado para chamada** | **4** |
| Candidato 5 | Classificado para chamada | 5 |
| Candidato 6 | Classificado para chamada | 6 |

Será alterado o status do Candidato 4 para "Inscrito para seleção, observe que na ordem de classificação ficou uma lacuna entre a classificação e 3 e 5.

| Candidato | Status da opção | Ordem de classificação |
| --- | --- | --- |
| Candidato 1 | Classificado para chamada | 1 |
| Candidato 2 | Classificado para chamada | 2 |
| Candidato 3 | Classificado para chamada | **3** |
| Candidato 5 | Classificado para chamada | **5** |
| Candidato 6 | Classificado para chamada | 6 |

O Candidato 4 será novamente classificado, observe que ele será classificado na última posição da área:

| Candidato | Status da opção | Ordem de classificação |
| --- | --- | --- |
| Candidato 1 | Classificado para chamada | 1 |
| Candidato 2 | Classificado para chamada | 2 |
| Candidato 3 | Classificado para chamada | 3 |
| Candidato 5 | Classificado para chamada | 5 |
| Candidato 6 | Classificado para chamada | 6 |
| **Candidato 4** | **Classificado para chamada** | **7** |
