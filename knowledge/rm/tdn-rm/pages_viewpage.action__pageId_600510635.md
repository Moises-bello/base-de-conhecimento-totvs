---
content_hash: 0e24ad6d196020ad11e8aac4dba829d3e4163dcdae7dcf27ad3ab74bcb74d4d0
fetched_at: '2026-06-29T00:10:57.901048+00:00'
page_id: '600510635'
product: rm
source: tdn-rm
title: Copiar o(s) conteúdo(s) para outra(s) turma(s)/disciplina(s)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=600510635
version: 28
---

Selecione um ou mais **Planos de Aula** e clique na opção **“Copiar conteúdo para outras Turma(s)/Disciplina(s)”**.

Permissão de acesso

Para acessar a funcionalidade, o perfil do professor deverá ter a permissão em:  **Serviços Globais | Segurança | Acesso | Perfil | Sistema: Educacional | Educacional (Portal) | Professor | Diário de classe | Plano de aula | Permite ao professor copiar o conteúdo para outra turma/disciplina**

Campos replicados

O portal replicará apenas os campos selecionadas do plano de aula:

* Copiar conteúdo previsto;
* Copiar conteúdo realizado;
* Copiar lição de casa;
* Copiar arquivos.

**Observação:** Quaisquer outras informações do plano de aula não serão replicadas.

Desabilitar o campo "Copiar conteúdo previsto"

A opção **“Conteúdo previsto”** ficará **habilitada** conforme a regra definida no tópico **“Alteração dos campos Previsto”** da documentação

Desabilitar o campo "Copiar conteúdo realizado"

A opção **“Copiar conteúdo realizado”** ficará **habilitada** conforme a regra definida no tópico **“Alteração dos campos Realizado”** da documentação

Número da aula

O processo de **cópia de conteúdo** realizará a cópia para outra(s) **Turma(s)/Disciplina(s)** que possua(m) o **mesmo número de aula**, independentemente da data do Plano de Aula.

Exemplo

Segue um exemplo ilustrativo:

> Tenho a Turma/Disciplina **0202DT “Matemática”**, da qual desejo copiar os conteúdos (**Previsto, Realizado, Lição de Casa e Arquivos**) para a Turma/Disciplina **0202AD “Matemática”**.
>
> * A aula da Turma/Disciplina **0202DT “Matemática”** (origem) do dia **20/06/2023**, das **11:10 às 12:40**, está vinculada à **aula 52**.
> * A aula da Turma/Disciplina **0202AD “Matemática”** (destino) do dia **20/06/2023**, das **09:00 às 09:40**, está vinculada à **aula 50**.
> * A aula da Turma/Disciplina **0202AD “Matemática”** (destino) do dia **27/06/2023**, das **09:00 às 09:40**, está vinculada à **aula 52**.
>
> Ao executar o processo, a cópia será realizada para a Turma/Disciplina **0202AD “Matemática”** do dia **27/06/2023**, das **09:00 às 09:40**, vinculada à **aula 52**, que é o **mesmo número de aula** da Turma/Disciplina **0202DT “Matemática”** (origem).
>
> Observe que a cópia **não se baseia na data**, mas sim no **número da aula**. Dessa forma, o professor pode aplicar o mesmo conteúdo em dias e horários diferentes, contanto que o número da aula seja o mesmo para ambas as Turmas/Disciplinas.
>
> A informação do **número da aula** está disponível:
