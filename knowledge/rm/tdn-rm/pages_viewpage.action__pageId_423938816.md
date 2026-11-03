---
content_hash: 29621dc072abdad880e18bf52ed745eac0b05aa39711989a5f151bcac954fe7f
fetched_at: '2026-06-29T00:09:29.120986+00:00'
page_id: '423938816'
product: rm
source: tdn-rm
title: Processos (Análise de Requisitos de Qualificação)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938816
version: 4
---

Esse processo realiza o cálculo de pontuação dos [Requisitos de Qualificação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938226) definidos como calculados.

A pontuação será calculada de acordo com a fórmula cadastrada no requisito e o resultado será gravado no anexo [Requisito de Qualificação do Produto/Fornecedor](http://tdn.totvs.com/pages/viewpage.action?pageId=423938767) do cadastro do produto ou no anexo [Requisito de Qualificação do Fornecedor](http://tdn.totvs.com/pages/viewpage.action?pageId=423938761) do cadastro do Cliente/Fornecedor conforme a definição do tipo de aplicação do requisito.

Ao executar o processo, serão exibidas as seguintes opções:

* **Recalcular os requisitos definidos como calculados e que foram editados**: Ao marcar essa opção, os requisitos já inseridos no cadastro do fornecedor ou produto, porém que tiveram a pontuação editada serão calculados novamente de acordo com a fórmula do requisito.

* **Calcular para todos fornecedores que tenham requisitos relacionados:** O requisito será calculado e inserido para todos fornecedores ou produtos que tenham qualquer requisito relacionado.

* **Calcular para todos os fornecedores relacionados aos produtos:** O requisito será calculado e inserido no cadastro do produto para cada fornecedor que estiver relacionado ao produto dentro do anexo [Cliente/Fornecedor](http://tdn.totvs.com/pages/viewpage.action?pageId=423938261).
* **Fornecedores:** Se não estiverem marcados os dois parâmetros anteriores, é possível inserir manualmente os fornecedores para quais serão inseridos os requisitos selecionados.

***Observação***: Após a execução desse processo é possível alterar manualmente a pontuação calculada, quando alterada o status da pontuação ficará como editada.
