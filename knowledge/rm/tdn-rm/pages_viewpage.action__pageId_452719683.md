---
content_hash: 3986616f3708136f51fa08358f5ca5264a5d06b29ada68cd5b3557aca06546df
fetched_at: '2026-06-29T00:10:09.496285+00:00'
page_id: '452719683'
product: rm
source: tdn-rm
title: Transferência - Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719683
version: 9
---

Nesta etapa será configurada alguns comportamentos relacionados a transferência de funcionários.

**Considera data de transferência igual a data de demissão na transferência sem ônus**

Marcando este parâmetro, ao demitir um funcionário usando o tipo 5 - Transferência sem ônus para cedente, o sistema preenche o campo "data de transferência" com a mesma data informada no campo "Data de demissão". Deixando o parâmetro desmarcado, o sistema preenche a "Data de Transferência" um dia após a "Data de Demissão".  
   
**Não exibir funcionários com saída por transferência na visão de funcionários**  
Com o parâmetro marcado o sistema não irá exibir os funcionários com saída por transferência (código demissão 5 - Transferência sem ônus p/ Cedente e 6 - Transferência com ônus p/ Cedente) na visão de funcionário, exceto quando a transferência for dentro da competência atual.   
Para visualizar os funcionários transferidos entre filiais (registros anteriores), deverá acessar o anexo Histórico de transferência no cadastro do funcionário.

**Não inclui nova linha no histórico salarial em transferências sem alteração de salário**  
Com o parâmetro marcado, ao executar a transferência de um funcionário que não teve o salário alterado, não será informada novo registro no histórico salarial do funcionário ativo.

**Permite transferência tipo 5 de funcionários afastados ou de férias**  
Com este parâmetro marcado será possível transferir funcionários para outra coligada quando o mesmo estiver com afastamentos temporários, como férias, afastamentos do tipo T, P e O.

**Observação**  
Este parâmetro somente será permitido transferir quando o tipo de transferência for 5.  
Será lavando o histórico de afastamento mesmo que o parâmetro 'Transfere históricos' esteja desmarcado no processo de transferência.

**Transfere funcionário membro CIPA na rescisão coletiva do tipo 5**

Com este parâmetro marcado, sera possível transferir um ou mais funcionários que tenham estabilidade CIPA.

**Observação**

Quando se informa uma única chapa na rescisão coletiva o sistema entende que seja uma rescisão individual, neste caso o parâmetro não será considerado. 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Retornar para **Rescisão**
