---
content_hash: 2a36cb5f9db10186c0bb2788d20bc0d2c46f82f3766a6ad8c599c8a996c88f17
fetched_at: '2026-06-29T00:09:10.380699+00:00'
page_id: '397382319'
product: rm
source: tdn-rm
title: Como gerar os eventos S-1200 e S-1210 para transportadores autônomos cadastrado
  no módulo de Gestão Financeira que tem desconto SEST e SENAT?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=397382319
version: 10
---

Para realizar a geração dos eventos S-1200 e S-1210 para transportadores autônomos discriminando os valores de SEST e SENAT, o usuário deve realizar as seguintes parametrizações:

1.Acesse o parametrizador e informe os eventos previamente cadastrados:

Códigos de calculo para os eventos de Desconto SEST/SENAT:

* [376 - SEST](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.SEST.aspx)
* [377 - SENAT](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.SENAT.aspx)

2. Acesse o cadastro de Cliente/Fornecedor e informe os dados do autônomo:

3. Antes de realizar a geração dos eventos S-1200 e S-1210, verifique se os lançamentos estão baixados com os valores que serão informados nos respectivos eventos:

265px500

4. Execute o processo de Gerar XML com o parâmetro Gerar Autônomos Fluxus/Externos marcado:

Serão gerados os eventos S-1200 e S-1210:
