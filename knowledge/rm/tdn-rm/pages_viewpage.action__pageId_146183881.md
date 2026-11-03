---
content_hash: e1b38e635f3e8a5a5d870f912a17fcce27966f2103ee04aa18b4a412602e8e68
fetched_at: '2026-06-29T00:05:55.817734+00:00'
page_id: '146183881'
product: rm
source: tdn-rm
title: 'Mensagem: O resultado da pesquisa ultrapassou o limite máximo de registros
  para esta visão. O que fazer?'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=146183881
version: 8
---

| Produto | **RM** |
| --- | --- |
| **Sintoma** | **Ao acessar o menu Cadastros -> Funcionários, o sistema apresenta a seguinte mensagem: O resultado da pesquisa ultrapassou o limite máximo de registros para esta visão. O que devo fazer para conseguir visualizar todos os registros?** |
| Solução | **-** Acesse o menu Cadastro > Segurança > Administrativa > Servidores de Aplicação;  - Crie um filtro selecionando a opção ID do Server = is not null;  O sistema vai apresentar a tela de cadastro dos servidores de aplicação. Caso já tenha o ID do Server "FopFuncData", clique em editar e altere o número máximo de registros;  Caso não tenha este Id, inclua um novo e informe um número de registros que atenda sua demanda. Exemplo: 99999. |
