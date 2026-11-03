---
content_hash: bdfad15cfcda09dc88403dfc024906f88e3a102ea040c01dca564bd2fd16d8c4
fetched_at: '2026-06-29T00:09:26.140660+00:00'
page_id: '423938279'
product: rm
source: tdn-rm
title: Geração de Patrimônio por Lote 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938279
version: 16
---

Esta ferramenta tem como objetivo possibilitar a criação de vários patrimônios a partir de um único patrimônio. Um processo onde será possível replicar o patrimônio modelo em vários outros registros do mesmo, agilizando o processo de inclusão de patrimônios similares.

**Regras para geração de patrimônio por lote**

* A data de inclusão deve estar dentro do período de cálculo.
* Em caso de patrimônios com ocorrências, as ocorrências não serão replicadas nos novos patrimônios.
* O parâmetro de sistema "Não inclui bens em títulos inativos" será verificado. Caso o patrimônio esteja sendo inserido em um título inativo o processo será encerrado.
* O sistema irá verificar se é possível inserir a quantidade de códigos de patrimônios relevante à parametrização da máscara. Exemplo: Considerando a mascara 99.99.999, neste caso o valor máximo analítico dessa mascara é 999, caso exista 980 registros de patrimônios e o usuário queira utilizar o processo para adicionar 20 novas unidades de um determinado patrimônio, este valor subirá para 1000 registros, ultrapassando seu limite em 1. \[(980+20)- 999\] = 1 excesso.
* Caso o código atinja o limite essa mensagem é exibida: "Impossível gerar código seqüencial, pois o maior código corresponde ao maior código que pode ser gerado" e nenhum registro será criado.
* Caso o parâmetro de sistema "Geração de código de patrimônio = código do bem" estiver marcado o Patrimônio terá o mesmo valor do Código do Patrimônio do Patrimônio modelo sem os "separadores", exemplo: Código do Patrimônio: 01.01.001 Patrimônio: 0101001
* Verificar o parâmetro do sistema "Código de patrimônio único". Caso está opção esteja marcada o valor do campo patrimônio das replicas não serão o mesmo do Patrimônio Modelo. Será um novo seqüencial que pode ser alterado pela regra acima, caso ela esteja marcada.
* Verificar o parâmetro de sistema "Código de barras único", caso esteja marcado o código de barras será único, copiando o valor do Código do Patrimônio para ele.
* Verificar o parâmetro de sistema "Geração de Código de barras = código do patrimônio".  
  Marcado - o código de barras será preenchido com o valor do patrimônio (campo patrimônio)  
  Desmarcado – o código de barras será preenchido com o valor do Código do Patrimônio (campo código do patrimônio)
* Nenhum patrimônio replicado por esse processo é integrado com o Totvs Gestão de Compras, mesmo se o patrimônio modelo estiver integrado.

**Realizando a Geração de Patrimônios por Lote**  
A parametrização para geração de patrimônios por lote é realizada em apenas uma etapa (exceto quando parametrizado para realizar a cópia de garantia). Nesta etapa obrigatoriamente deve ser selecionado o patrimônio modelo e a quantidade a ser gerada. A Cópia dos dados adicionais (Centro de Custo, Departamento, Responsável e Localização) é opcional, salvo no caso dos parâmetros do sistema ("Tornar Centro de Custo obrigatório", "Tornar Departamento obrigatório", "Tornar Responsável obrigatório", "Tornar Localização obrigatória") estejam marcados, tornado assim a replica desses campos obrigatórios.

Existe também a possibilidade de copiar apólice de seguro, campos complementares, Contabilizar sendo que este parâmetros irá tratar da seguinte forma (Marcado) - Contabilização Pendente (Desmarcado) - Não Contabilizar

Garantias Garantias, sendo que neste caso os controles de garantias serão gerados seguindo a regra de gerar a garantia dos novos patrimônios X meses após a data de aquisição (o usuário informará o número de meses de garantia).

Veja Também
