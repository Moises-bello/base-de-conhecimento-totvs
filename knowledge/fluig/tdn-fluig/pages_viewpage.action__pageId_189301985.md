---
content_hash: 1ec537f8f8497e894366cb7b9a664393115315c85d59fdbdcd8c2e24df4e8142
fetched_at: '2026-06-28T21:35:19.027478+00:00'
page_id: '189301985'
product: fluig
source: tdn-fluig
title: FORM 005 - Por que datas em registros de formulários estão perdendo formatação
  em formatos distintos na base de dados?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189301985
version: 15
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:**Fluig

**Ambiente:** Fluig Studio

**Versão: Todas**

# Ocorrência

Ao salvar registros de formulários que contenham datas, ou movimentar solicitações com formulários que contenham datas, em algumas situações as datas estão sendo salvas nas metalistas/registros de formulário (tabela única) com padrões diferentes.

# Causa

Isso ocorre quando o navegador utilizado pelos usuários diverge entre Chrome e Firefox/IE. No Chrome, toda e qualquer data é persistida com o padrão americano (yyyy-mm-dd) caso seja utilizado o campo do tipo "date". No caso do Firefox/IE, campos do tipo "date" são substituídos por campos do tipo "text" e então é adicionado a função datePicker do jQuery para os mesmos, sendo assim o campo fica com o padrão brasileiro e é persistido como tal.

# Solução

Caso seja utilizada a versão 1.4.12 ou superior do sistema e o formulário fora criado pelo sistema (através do gerenciamento de processos), basta salvar o formulário novamente (editar e salvar) pra que o formulário inclua o evento inputFields com a formatação de data por padrão. Caso seja um formulário próprio do cliente, pode-se utilizar o evento de formulário inputFields conforme exemplificado no link a seguir: [Exemplo de uso de inputFields](http://tdn.totvs.com/pages/viewpage.action?pageId=75270483#DesenvolvimentodeFormulários-InputFields):

jsCódigo para Datas
