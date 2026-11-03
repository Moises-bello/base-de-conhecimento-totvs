---
content_hash: 3e8eea41e780cda3e16864c5916fe5bbb2c7947c26d092b315b47e3ce8f658a3
fetched_at: '2026-06-29T00:09:26.782340+00:00'
page_id: '423938429'
product: rm
source: tdn-rm
title: Vida útil da Ordem de Serviço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938429
version: 2
---

A vida útil controla o desgaste de uma peça em relação ao tempo de uso, km rodado, ciclos etc.   
Geralmente o tempo de vida útil de uma peça é recomendado pelo fabricante. É possível controlar a vida útil de um produto no RM Officina.   
Para visualizar a vida útil do item da Ordem de Serviço é necessário editar o item e clicar na aba Ordem de Serviço.   
Para que o sistema comece a controlar a vida útil de determinado produto é necessário realizar algumas parametrizações.   
Se o usuário necessitar de controlar a vida útil de uma correia dentada, por exemplo, ele terá que acessar o menu Cadastros | Produtos/Serviços, selecionar a correia dentada e no anexo deverá clicar em "Produtos – Informações de Manutenção" e informar o vencimento da vida útil nos campos referentes ao indicador de uso definido no Tipo de Objeto de Manutenção no qual se deseja controlar a vida útil.   
Se no objeto estiver marcado o indicador de uso Km, a vida útil da correia dentada também deverá ser controlada usando a mesma métrica, no caso deste exemplo, a vida útil da correia dentada deverá ser controlada por Km e assim por diante.   
Após fazer isso o usuário deverá vincular a correia dentada a um objeto de manutenção para que a vida útil seja então controlada.   
Acesse o cadastro do objeto de manutenção em Cadastros | Objetos de Manutenção selecione o objeto de manutenção e clique em Anexo | Produtos do Objeto de Manutenção e insira a correia dentada como produto deste objeto de manutenção.   
Quando os indicadores de uso alcançarem o valor que o usuário atribui para a vida útil da correia dentada o sistema saberá que a vida útil da peça venceu. Ao abrir uma OS para esse objeto de manutenção e a sua vida útil ainda não estiver vencido, o sistema emitira uma mensagem informando isso ao usuário, caso o usuário não tenha permissão para incluir itens cuja a vida útil ainda não venceu o sistema pedirá a senha de um usuário que tenha essa permissão, geralmente um supervisor ou um administrador do sistema.   
***Observação***: Para itens que tenham a sua vida útil controlada só é possível inserir uma unidade na ordem de serviço. Nesse caso, se o usuário tentar inserir duas correias dentadas o sistema não aceitará.  
O controle da vida útil pode ser feito somente através do RM Officina, acessando o movimento pelo TOTVS Gestão de Estoque, Compras e Faturamento essa funcionalidade não é visível.
