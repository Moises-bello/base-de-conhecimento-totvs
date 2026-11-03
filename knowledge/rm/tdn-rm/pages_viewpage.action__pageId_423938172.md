---
content_hash: c2101bba588e67f098bccd8b9079daa4310806a597ef155855973619b0054010
fetched_at: '2026-06-29T00:09:25.822945+00:00'
page_id: '423938172'
product: rm
source: tdn-rm
title: Combustível
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938172
version: 7
---

Para as empresas do segmento de comércio varejista de combustível que utilizam o sistema TOTVS, deverão ser feito os devidos cadastros dos itens abaixo, onde é de suma importância o preenchimento de cada um deles para que os movimentos (venda, compra e ajuste de estoque) sejam relacionados ao [SPED Fiscal](http://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+1) corretamente:

* Bomba
* Bico
* Lacre
* Volume de Vendas

***Observação***.: Os dados dos cadastros devem ser alimentados conforme as necessidades dos clientes.  
 Após o cadastro destes itens, deverá ser configurada uma FILIAL, onde ela será o seu "posto de combustível". Também deverá ser cadastrado os produtos que serão comercializados de uma forma específica para o correto funcionamento da operação.  
 O local de estoque deve ser tratado como um  tanque de combustível, que deverá receber movimentações de um único tipo de produto/combustível. Caso a empresa comercialize mais de um tipo de combustível, a mesma deverá cadastrar mais de um local de estoque, ou seja, um estoque para cada tipo de combustível.  
 Os tipos de movimentos de [perda](http://tdn.totvs.com/pages/viewpage.action?pageId=423938808)e [ganho](http://tdn.totvs.com/pages/viewpage.action?pageId=423938165)de combustível devem ser classificados quanto ao tipo de "Operação de Ajuste" que deverá ser [parametrizado](http://tdn.totvs.com/pages/viewpage.action?pageId=423938826) conforme a necessidade do tipo de movimento. É aconselhável parametrizar estes movimentos como um tipo de movimento de ajuste de estoque ou inventário, pois não pode-se confundir este processo como de compra ou venda.  
Para conferência das movimentações, poderá ser utilizada a ficha física financeira de estoque. E após tudo isso o setor Fiscal estará apto a gerar o arquivo do SPED, utilizando todo o agrupamento destas informações.

---
