---
content_hash: 28e238cea7205e62c6bb6b9f7c90187b1dbcc32384abca568e3da744ab821b77
fetched_at: '2026-06-29T00:09:22.104067+00:00'
page_id: '422545969'
product: rm
source: tdn-rm
title: Cálculo do ISS Devido no Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545969
version: 3
---

Ao Encerrar o Período de Apuração, o sistema irá preencher os valores automaticamente.   
O sistema gera os valores da seguinte forma:  
Para períodos do Tipo ISS, o sistema agrupará os valores de ISS, criando vários registros, por alíquota referente aos Débitos do Imposto, Depósito Judicial e Retenção nas Entradas.  
Caso haja Débito de ISS nos Lançamentos de Saída, o sistema gerará registros para cada alíquota e município que o Contribuinte terá que recolher o imposto. Estes valores serão armazenados na Pasta Serviços, Subpasta Débito na Saída.  
Lançamentos Fiscais cancelados não serão considerados.

**Geram Débito do Imposto**

Lançamentos Fiscais de Saída cujo Tipo de Recolhimento é ISS devido. Lançamentos Fiscais de Entrada cujo Tipo de Recolhimento é ISS Retido ou ISS Retido Deduzido.  
 Os Lançamentos de Outros Débitos/ Créditos são considerados no cálculo do Débito do Imposto.  
 Na apuração do ISS não é considerado o tipo de recolhimento ISS Isento. Estes valores não afetam o débito do imposto  
 Lançamentos Fiscais de Saída cujo Tipo de Recolhimento é ISS Depósito em juízo, são totalizados à parte. Neste caso são agrupados por alíquota e dentro de cada alíquota por município.   
 Um vez Encerrado o Período de Apuração de ISS, o usuário pode optar por gerar as Guias de Pagamento de ISS. Estas Guias serão geradas de seguinte forma:  
 Agrupadas por alíquota que o contribuinte possuir débito, o sistema irá separar ISS Devido na Saída do ISS Retido na Entrada.  
 São geradas também as guias referentes ao depósito Judicial. Estas Guias são agrupadas por município que foi efetuado o depósito, independente da alíquota. Neste caso NÃO é preenchido o campo de alíquota na tela desta guia.  
 Um vez geradas as Guias de Pagamento do ISS , o usuário tem a opção de gerar Lançamento Financeiro para o TOTVS Gestão Financeira. O sistema agrupa todas as Guias de ISS e gera um único Lançamento Financeiro.

***Observação:***Somente deletando os Serviços por Alíquota existentes, os Lançamentos correspondentes já poderão ser alterados ou excluídos. Porém, isto só ocorrerá se não houver nenhuma Guia gerada para estes valores de alíquota e município.  
 Caso já exista uma Guia para um determinado município e com uma determinada alíquota, e incluído outro Lançamento com as mesmas características, os valores do Serviço por Alíquota serão atualizados, e uma nova Guia será gerada com o valor do ISS do novo Lançamento.  
 Não serão incluídas Guias repetidas automaticamente.

***Atenção!***Para as Filiais do Distrito Federal a Apuração do ISS será realizada da seguinte forma:

* Lançamentos Fiscais de Saída com incidência de ISS caso haja na pasta Outros Tributos do Lançamento Fiscal os Tipos de Recolhimento: Devido e Retido o sistema irá calcular o valor devido como sendo a diferença do valor do ISS Devido menos o valor do ISS Retido.
* ***Exemplo 1***

|  |  |
| --- | --- |
| Tipo do Lançamento Fiscal | Saída |
| Tipo de Recolhimento | ISS Devido |

**Valores**

|  |  |
| --- | --- |
| Base | 920,00 |
| Alíquota | 2% |
| Valor do ISS | 18,40 |

* ***Exemplo 2***

| Tipo do Lançamento Fiscal |  |
| --- | --- |
| Tipo do Lançamento Fiscal | Saída |
| Tipo de Recolhimento | Retido Fonte |

**Valores**

|  |  |
| --- | --- |
| Base | 920,00 |
| Alíquota | 1% |
| Valor do ISS | 9,20 |

No encerramento do período, no campo "Valor Devido na Saída" na apuração do tributo o valor será o seguinte:

R$9,20 (18,40  9,20 **=** 9,20)

***Observação:*** Para Notas Fiscais cujo Tipo de Recolhimento é só devido ou só retido não será efetuado o cálculo acima.
