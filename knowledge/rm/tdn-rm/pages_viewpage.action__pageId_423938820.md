---
content_hash: e63e65c7b8a79f076e86e6fa9218b40b335e59ba4b96451a515ae4ae741c0971
fetched_at: '2026-06-29T00:09:29.146810+00:00'
page_id: '423938820'
product: rm
source: tdn-rm
title: Processos (Ressuprimento)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938820
version: 20
---

O processo de ressuprimento é responsável por calcular o consumo, classe ABC e atributos de todos os produtos exibidos no processo. Os produtos que são exibidos no assistente afetam estoque, possuem um [Tipo de aplicação](https://tdn.totvs.com/pages/viewpage.action?pageId=458752971) associada e podem ter sido movimentados em tipos de movimento parametrizados para o processo de ressuprimento, seja Geração de Movimento, Cálculo de Consumo, Saldos ou Devolução de Consumo.

**Calcular Consumo**

O sistema calcula o Consumo para todos os produtos que fazem parte do filtro inicial do assistente do processo. Serão analisados todos os tipos de movimento de saída e que a gestão de ressuprimento esteja configurada como saldos.  
Para calculo do consumo é necessário definir qual será o tipo de consumo: Normal, Anormal ou Ambos. Esta definição será responsável por filtrar os produtos que serão calculados, uma vez que o tipo de consumo é definido no tipo de aplicação associado a cada produto, por meio do [Grupo Classe ABC](http://tdn.totvs.com/display/LRM/Grupo+de+Classe+ABC). Além do tipo de consumo, é necessário informar um período em que o sistema levará em consideração para calcular o consumo.  
Outra opção disponível ao calcular consumo, é “Calcular Ponto de Reposição”, não sendo obrigatório marcar esta opção ao executar o calculo do consumo.  
   
**Calcular Classe ABC**  
  
Ao executar o processo marcando a opção “[x]Calcular Classe ABC” o sistema define  a classe de cada produto envolvido na gestão de ressuprimento, conforme percentual presente no cadastro do Grupo de Classe ABC e movimentações de consumo. A classe ABC do produto é inserida em informações de estoque do produto em questão.

**Calcular Atributos**

É definido como atributos do processo de ressuprimento: Estoque Mínimo, Estoque Máximo, Ponto de Reposição, Lote Econômico de Compras e Sugestão de Compras. Estoque mínimo é a menor quantidade de material a ser mantida em estoque capaz de atender a um consumo superior ao estimado para certo período ou para atender a demanda normal em caso de entrega da nova aquisição.

**Emin = CM \* TEMin**

Emin = Estoque Mínimo;  
CM = Consumo médio prático ou Consumo médio teórico;  
TEMin = Cobertura de estoque mínimo: é a quantidade de dias ou meses que um determinado produto “sobrevive” em estoque mínimo;

Estoque máximo é a maior quantidade de material admissível em estoque, suficiente para o consumo em certo período, devendo-se considerar a área de armazenagem, disponibilidade financeira, imobilização de recursos, intervalo e tempo de aquisição, perecimento, etc.

**EMax = CM \* TEMax**

Emax = Estoque Máximo;  
CM = Consumo médio prático ou Consumo médio teórico;  
TEMax = Cobertura de estoque máximo: é a quantidade de dias ou meses que um determinado produto “sobrevive” em estoque máximo;

Ponto de Reposição Nível de Estoque que, ao ser atingido, determina imediata emissão de um pedido de compra, visando a completar o Estoque Máximo.

**PR = (CM \*(TC + TF)) + EMin**

PR = Ponto de Reposição;  
CM = Consumo médio prático ou Consumo médio teórico;  
TC = Tempo de compra cadastrado para um determinado produto;  
TF = Tempo de fornecimento cadastrado para um determinado produto;  
Emin = Estoque mínimo;

Lote Econômico de Compras é igual à quantidade média prevista para consumo em determinado período de tempo.

**LC = CM \* TR**

LC = Lote Econômico de Compras;  
CM = Consumo médio prático ou Consumo médio teórico;  
TR = Tempo de reposição do produto;

Ao calcular atributos com a opção "[x] Sugestão de Compra" marcada, o sistema irá gerar uma sugestão caso o saldo do produto esteja abaixo do ponto de reposição. A quantidade sugerida irá respeitar o estoque máximo definido em informações de estoque do produto. Após gerar a sugestão e se o sistema estiver parametrizado para "[x] Usa Envio de Email para Sugestão de Compra", será enviado um e-mail para o Funcionário associado ao produto (Cadastro de Produto | Anexo Funcionários/Responsáveis). O e-mail tem a finalidade de avisar que existe uma sugestão não analisada para um produto de sua responsabilidade.

A partir da versão/patch **12.1.2310.108** a rotina de ressuprimento passa a ser um processo **multicoligada**, ou seja, é possível executar o processo para várias coligadas diferentes, sem ter que fazer a troca de contexto.

---
