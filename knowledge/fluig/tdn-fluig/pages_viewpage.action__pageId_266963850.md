---
content_hash: 187aa7599a8b4b95b7798fd9fd6f99aa63b96440b50264716871f8efb488ce4e
fetched_at: '2026-06-28T21:35:23.846571+00:00'
page_id: '266963850'
product: fluig
source: tdn-fluig
title: BPM 070 - Como importar processos de forma que seja selecionada a empresa correta?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266963850
version: 5
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** fluig

# Ocorrência

* Nossa empresa padrão é de número 1.
* Criamos a empresa número 2.
* Exportamos os processos da empresa 1 e tentamos importá-los na empresa 2 via Eclipse.

Acontece que, ao tentar importar os processos, o Eclipse apresenta o erro "Formulários estão vinculados a outro servidor". Como faremos para definir ou selecionar a empresa 2 no ato da importação (Eclipse) ou mesmo o seu servidor?

# Causa

Formulário está apontando para servidor da empresa "1".

# Solução

Quando importado um projeto de um servidor "1" o formulário fica atrelado a este servidor, por padrão. Para poder exportar para um servidor "2" é necessário acessar o processo no Eclipse → *Properties* → Formulário → Definição do formulário (Alterar para Local) → selecionar o formulário e salvar.  
  
 Após você pode exportá-lo para o servidor.
