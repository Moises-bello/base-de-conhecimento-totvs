---
content_hash: da2b6c212537d20386aebc079953cf747892d7734d2635982ffe5baeedfe0e69
fetched_at: '2026-06-29T00:09:25.840888+00:00'
page_id: '423938176'
product: rm
source: tdn-rm
title: Compara Tributos do Tipo de Movimento Parametrizado com o do XML Importado
type: documentation
url: https://tdn.totvs.com/display/LRM/Compara+Tributos+do+Tipo+de+Movimento+Parametrizado+com+o+do+XML+Importado
version: 6
---

**Objetivo**

Permitir ao usuário confrontar os valores de tributos de uma Nota Fiscal enviada pelo fornecedor (arquivo .XML) com os valores calculados pelo sistema, de acordo com as parametrizações e dados do movimento.

**Definição do Processo**

Os valores dos tributos de uma Nota Fiscal de entrada, criada e enviada por um fornecedor, podem diferir dos valores esperados pelo cliente, para aquele tipo de transação.   
O Fornecedor pode errar nos cálculos, ou ainda a base de cálculo configurada no sistema pode estar errônea.   
Como a SEFAZ não valida todas as informações da NF-e, não podemos considerar que a Nota recebida pelo ERP, via Totvs Colaboração, esteja sempre com os valores dos tributos corretos.   
Dessa forma, o sistema deverá verificar as diferenças e exibi-las ao usuário no momento da gravação do movimento, para que o mesmo defina quais os valores devem ser prevalecidos.

**Base de Cálculo e Alíquota de IPI**

Quando é importado uma [Devolução de Compra para Industrialização com IPI](https://tdn.totvs.com/pages/viewpage.action?pageId=396362395) é informado o valor de Devolução do IPI, porem não é informado a base de cálculo e alíquota, sendo assim usamos o que está parametrizado no Tipo de Movimento em questão.

Para isso é aconselhado que seja usado o parâmetro "Comparar com XML" em IPI na etapa de  "Fis - Tributação - Item" para que ao salvar o movimento seja exibido uma tela para se comparar o que foi calculado pelo sistema e o que foi importado do XML.

Na tela de comparação abaixo ao marcar campo "Valor" como "XML", os campos "Base de cálculo" e "Alíquota" como "Calculado" o sistema usa o Valor do XML e a B.C e Alíquota do tipo de Movimento.

\*Caso opte por não usar o parâmetro ele deverá preencher a Base de cálculo e Alíquota Manualmente em todos itens ou usar o  valor que for calculado pelo sistema.

---
