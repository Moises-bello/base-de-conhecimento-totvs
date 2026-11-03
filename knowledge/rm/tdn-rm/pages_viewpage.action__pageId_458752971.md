---
content_hash: 75c943fa786b4a408ffa0836367baee5a242f57088488786492d0e1338cc3c36
fetched_at: '2026-06-29T00:10:13.403684+00:00'
page_id: '458752971'
product: rm
source: tdn-rm
title: Tipo de Aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458752971
version: 6
---

A finalidade deste cadastro é classificar os produtos que entrarão no Processo de Ressuprimento, pois o tipo de classificação é associado ao cadastro do produto.   
Ao calcular consumo, atributos ou curva abc o sistema verifica o tipo de aplicação associado ao produto para retornar as informações conforme configurado.  
Cada registro deste cadastro possui parâmetros que serão respeitados ao gerar as rotinas de Ressuprimento.   
Caso o tipo de aplicação associado ao produto não esteja configurado para “[x] Usar Gestão de Materiais” o produto será desconsiderado para o módulo de ressuprimento.   
No Cadastro do Tipo de Aplicação deve ser informado o numero de meses de consumo médio, para que ao calcular o consumo o sistema valide este dado com as movimentações do produto.   
Além desta informação, também pode ser associado o Grupo de Classe ABC e assim o produto que foi informado com o tipo de aplicação em questão, terá o Grupo de Classe ABC associado a ele de forma indireta, já que o Grupo de Classe ABC está presente no Tipo de Aplicação e não diretamente no produto.   
É importante não confundir Grupo de Classe ABC com a Classe ABC do produto, pois a Classe ABC do produto é calculada com base nos percentuais do Grupo de Classe ABC.  
Além de todos estes recursos informados acima, o Tipo de Aplicação também pode atualizar tempo de reposição de acordo com a nova classificação ABC do produto, se essa opção for parametrizada nos parâmetros gerais de ressuprimento.   
Essa atualização respeitará o parâmetro geral "Calcula Tempo de Reposição pela Classe".  
O cadastro do Tipo de Aplicação possui o recurso de atualizar automaticamente os dados de ressuprimento e utiliza de algumas fórmulas para o calculo, são elas:

| Tipo de Aplicação | Sigla¹ | Cálculo² |
| --- | --- | --- |
| Estoque Mínimo | **Emin** | **= CM \* TEMin** |
| Estoque Máximo | **Emax** | **= CM \* TEMax** |
| Ponto de Reposição | **PR** | **= (CM \*(TC + TF)) + EMin** |
| Lote de Compra | **LC** | **= CM \* TR** |
| Consumo Médio | **CM** | **= TRC/DC** |

**Onde¹ e Onde²**

|  |  |
| --- | --- |
| **Emin** | Estoque Mínimo |
| **Emax** | Estoque Máximo |
| **CM** | Consumo médio prático ou Consumo médio teórico(produtos sem histórico de consumo). |
| **TEMin** | Cobertura de estoque Mínimo: é a quantidade de dias ou meses que um determinado produto “sobrevive” em estoque mínimo. |
| **TEMax** | Cobertura de estoque máximo: é a quantidade de dias ou meses que um determinado produto “sobrevive” em estoque máximo. |
| **PR** | Ponto de Reposição |
| **TC** | Tempo de compra cadastrado para um determinado produto. |
| **TF** | Tempo de fornecimento cadastrado para um determinado produto |
| **LC** | Lote Econômico de Compras |
| **TR** | Tempo de Reposição do produto |
| **TCR** | Total de consume real em um período parametrizado. |
| **DC** | Dias de consume: Poderá usar a tabela de dias trabalhados ou usar a quantidade de dias nos meses que farão parte do cálculo. |

Opções para calcular a quantidade sugerida, ”Lote de Compra por Tempo de Reposição” ou “Estoque Máximo/Saldo”.  A quantidade sugerida pela opção “Lote de Compra por Tempo de Reposição “ utiliza a seguinte fórmula para o cálculo:

| Tipo de Aplicação | Sigla¹ | Cálculo |
| --- | --- | --- |
| Quantidade Prática Sugerida | **QPS** | **= CM \* LC** |
| Quantidade Teórica Sugerida | **QTS** | **= CM \* LC** |

**Onde¹ e Onde²**

|  |  |
| --- | --- |
| **QPS** | Quantidade Prática Sugerida; |
| **QTS** | Quantidade Teórica Sugerida; |
| **CM** | Consumo Médio Teórico\Prático; |
| **LC** | Lote Econômico de Compras; |

***Atenção!*** Se a quantidade sugerida pratica ou teórica, somado ao saldo total do produto for maior que o estoque máximo o sistema irá calcular da seguinte forma:

QTS = Emax – Saldo total senão LC  
QPS= Emax – Saldo total senão LC  
   
A quantidade sugerida pela opção “Estoque Máximo/Saldo” utiliza a seguinte fórmula para o cálculo:

| Tipo de Aplicação | Sigla¹ | Cálculo |
| --- | --- | --- |
| Quantidade Prática Sugerida | **QPS** | **= Emax – (SEM + SLE)** |
| Quantidade Teórica Sugerida | **QTS** | **= Emax – (SEM + SLE)** |

**Onde¹ e Onde²**

|  |  |
| --- | --- |
| **QPS** | Quantidade Prática Sugerida; |
| **QTS** | Quantidade Teórica Sugerida; |
| **Emax** | Estoque Máximo; |
| **SEM** | Saldo em Movimento; |
| **SLE** | Saldo em local de estoque; |

***Atenção!*** Se a quantidade sugerida pratica ou teórica, somado ao saldo total do produto for maior que o estoque máximo o sistema irá calcular da seguinte forma:

|  |  |
| --- | --- |
| QTS | **= Emax – Saldo Total** |
| QPS | **= Emax – Saldo Total** |
