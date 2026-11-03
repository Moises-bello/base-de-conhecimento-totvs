---
content_hash: 9ee25a64a46e8617881a3a84fe8cd8dc43f468cca90c04f614108fab0223fe85
fetched_at: '2026-06-29T00:09:12.727167+00:00'
page_id: '417700476'
product: rm
source: tdn-rm
title: Antibiótico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=417700476
version: 1
---

**Antibiótico**   
Importador de antibiótico   
**Para as consistências:**

* Para uma droga pertencer a um pedido de antibiótico existente, este pedido de antibiótico precisa conter esta droga sem data de fim informada.
* Caso a droga não exista em pedido de antibiótico algum, ou só exista com data de fim informada, um novo pedido de antibiótico será criado.
* Na criação de um novo pedido de antibiótico, ele deve conter todas as drogas que compõe o mesmo pedido de dispensação.
* As consistências de antibiótico devem ser feitas em cima da substância química (Principio ativo), e não do nome comercial importado.  
  Se as consistências acima não forem respeitadas no momento da importação será gerado log com mensagem de AVISO.  
  **Observação**  
  Estas consistências servem apenas para determinar se um registro de dispensação devera resultar em um novo pedido de antibióticos ou se devera ser incluído em um pedido existente.   
  Dando continuidade as consistências, Será gerado log com mensagem de erro:
* O registro ou prontuário terá que corresponder a um prontuário valido já lançado no sistema. Caso contrário exibira mensa-gem de erro.
* O nome do paciente do pedido de antibiótico tem que corresponder ao nome do paciente lançado na base Janus. Caso contrário exibirá mensagem de erro.
* A data do pedido de antibiótico tem que estar dentro de uma internação valida do paciente. Caso contrário exibirá mensagem de erro.  
  Para as consistências abaixo, será gerado log com mensagem de AVISO e o campo onde estiver nulo (desde que não seja obrigatório) ou que não tenham valores validos para a base Janus, após importação o campo ficara em branco. O restante do registro será importado normalmente.
