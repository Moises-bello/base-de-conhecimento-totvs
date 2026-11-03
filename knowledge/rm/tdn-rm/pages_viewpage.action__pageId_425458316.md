---
content_hash: 0c6746a804f40aee84c2be2004b01bd20ae0cba20b121e08e27c1f596eade5cd
fetched_at: '2026-06-29T00:09:29.856730+00:00'
page_id: '425458316'
product: rm
source: tdn-rm
title: RM Portal - Parâmetros Gerais 16/18
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458316
version: 20
---

**Termo de consentimento de uso de imagem e voz - 1/3**

Nesse passo da parametrização será possível habilitar o uso do termo, habilita somente a opção de aceite, bloqueio do acesso aos portais, relatório para o termo, versão e o responsável por aceitar/revogar o termo quando o aluno for menor de idade.

* **Habilitar uso do termo**

Essa opção habilita todas as funcionalidades referentes ao uso do termo de consentimento de imagem e voz. Uma vez habilitado, será obrigatório preencher os campos marcados em negrito neste e nos passos seguintes referentes a parametrização do termo.

* **Habilita somente opção de aceite**

Essa opção, quando habilitada, somente será possível aceitar o termo e não haverá a possibilidade de revogação em nenhum momento.

* **Bloquear acesso ao portal para aceite/revogação do novo termo**

Quando habilitado, será realizado o bloqueio do acesso ao portal até que o aluno aceite/revogue o termo. Caso esteja habilitado a opção "**Habilita somente opção de aceite"**, o acesso ao portal ficará bloqueado até o aceite do novo termo.

* **Relatório do termo de consentimento**

Campo para inserção do documento do termo de consentimento de uso de imagem e voz.

Informações

Na execução do relatório será passado parâmetros com informações do contexto selecionado pelo aluno, para que estes dados possam ser utilizados você poderá criar os parâmetros abaixo nos relatórios:  
CODCOLIGADAPARAM, CODFILIALPARAM, CODTIPOCURSOPARAM, CPFPARAM E CPFRESPONSAVELPARAM, RAPARAM.  
  
**Observação(1):** Caso o termo de aceite seja utilizado no TOTVS Processo Seletivo na matrícula via Central do Candidato, provavelmente o RAPARAM **não** estará preenchido, pois o candidato pode não ser um aluno ainda.

**Observação(2):**O CPFRESPONSAVELPARAM é o CPF do responsável que realizou o aceite(usuário autenticado no portal).

* **Versão**

Este campo realiza o controle de versionamento do termo. Somente é possível incrementar a versão e não há nenhuma forma, após alterado, retornar a versão anterior. Portanto quando incrementado será mostrado uma mensagem informando que após concluído a parametrização, não será possível retornar a versão anterior e que todos os alunos terão que realizar o aceite/revogação do novo termo, em caso de aceite obrigatório o aluno poderá somente aceitar o novo termo.

* **Responsável por aceitar/revogar termo quando aluno for menor de idade**

Essa listagem relaciona todos os papeis que poderão executar o aceite ou revogação do termo de consentimento de uso de imagem e voz quando o aluno for menor de 18 anos.
