---
content_hash: 16dc26b58bf1a4c67a51814577bd7c17a45738191aa9e214ec6ded0914726ae9
fetched_at: '2026-06-29T00:10:11.232781+00:00'
page_id: '452719997'
product: rm
source: tdn-rm
title: Período (PTO)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719997
version: 3
---

**Período**   
  
-**Trabalhar com base no próximo período mensal**  
Marcando este parâmetro os funcionários que possuem este grupo de acesso vão trabalhar com o próximo período mensal determinado no menu opções| Parâmetros| Próximo período mensal.

* **Observações:**  
  Este parâmetro só pode ser marcado se existir próximo período mensal.  
  o recálculo é feito no período do usuário que iniciou o server.
* **Importante:** Ao habilitar o parâmetro **Trabalhar com base no próximo período mensal** no grupo de acesso ao quiosque do Chefe e/ou Chefe externo, o parâmetro **[Permite chefe aprovar abono de subordinados em períodos diferentes](https://tdn.totvs.com/pages/viewpage.action?pageId=452720001)** passa a ser desconsiderado.

**-Não considera o saldo do último período quando não recalculado**  
Marcando este parâmetro os funcionários que possuem este grupo de acesso e são chefes ou supervisores,  irão visualizar o saldo do banco de horas do time no Meu RH não considerando o saldo do período anterior. Isto quer dizer que, caso não tenha sido efetuado o recálculo, o sistema irá exibir o saldo do período zerado, pois está configurado para não utilizar o saldo do período anterior.  Efetuando o recálculo o sistema passará a exibir o saldo atual. 

**Observações:**  
Este parâmetro só pode ser marcado se o parâmetro **Trabalhar com base no próximo período mensal** estiver marcado.   
Por padrão este parâmetro virá desmarcado. O comportamento neste caso será da seguinte maneira: Caso não tenha sido efetuado o recálculo, o sistema irá exibir o saldo do período anterior para não apresentar os valores zerados, caso no mês anterior tenha saldo. Após efetuar o recálculo o sistema passará a exibir o saldo atual.

**-Considera a primeira data do próximo período para edição de batidas**   
O sistema irá permitir editar a batida referente a primeira data do próximo período.
