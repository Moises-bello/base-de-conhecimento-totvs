---
content_hash: 7ee4538a6a884ae156a4f49319b20556c6dd4a202baf3177f0e55bad7b04df67
fetched_at: '2026-06-29T00:09:31.364714+00:00'
page_id: '425458655'
product: rm
source: tdn-rm
title: Matrícula de disciplina por substituição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458655
version: 4
---

O processo tem como objetivo substituir a matrícula atual do Aluno em uma turma/disciplina e alterá-la por outra que seja do seu interesse.   
Ao substituir uma matrícula na turma/disciplina, as disciplinas retornadas seguem as regra do SDD (O SDD é o conjunto de todas as disciplinas disponíveis para o aluno se matricular em um período letivo. Este conjunto de disciplinas é obtido de acordo com a parametrização do sistema).   
A execução do processo é alterada de acordo com a configuração do parâmetro **"Ativar matrícula por substituição durante a troca de disciplinas"**, que esta disponível nos parâmetros do TOTVS Educacional:

* **Parâmetro Marcado** (Deve ser parametrizado a situação de matrícula que indica lista de espera)

O processo não executa a substituição de forma imediata, ou seja, o sistema inclui a nova matricula na turma/disciplinas pretendida, e o status da matrícula estará de acordo com o status parametrizado na lista de espera. Neste caso para efetivar a substituição é necessário que o processo de "Matricula por lista de espera" seja executado.

* **Parâmetro Desmarcado**

O processo executará a substituição de forma imediata, porém só efetivada a substituição se a exclusão da matrícula origem e consequente inclusão da nova matricula não levantarem nenhum tipo de exceção as regras de matrícula. Caso haja que qualquer tipo de exceção, a troca é abortada e será gerado um log com o motivo.
