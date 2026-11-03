---
content_hash: e8bf4c518e23afeafcf603f69108e0bb095934ca14843c937568b865406e11e0
fetched_at: '2026-06-29T00:09:25.211985+00:00'
page_id: '423938064'
product: rm
source: tdn-rm
title: Índice de Majoração de Mão de Obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938064
version: 4
---

O índice de majoração será aplicado ao valor total da mão de obra utilizada nas ordens de produção para o rateio de custo indireto por majoração de mão de obra.   
***Observação:***Para utilizar o Índice de Majoração de Mão de Obra é necessário que o parâmetro "Majoração do Valor de Mão de Obra Direta" esteja habilitado.

*****Dica***:** É possível criar campos complementares para o cadastro de Índice de Majoração de Mão de Obra.

*****Atenção!***** Se for utilizado tempo de mão de obra inferior ao previsto, o valor majorado também será menor, o mesmo não ocorre quando for utilizado tempo de mão de obra superior ao previsto.

****Exemplo**:** Um operário X tem previsto:

| Atuação da Ordem de Produção Y | Custo Hora | Índice de Majoração |
| --- | --- | --- |
| 1 (uma) hora | R$10,00 | 0,1 (10%) |

Ao efetivar a ordem de produção o operário X trabalhou 2 (duas) horas ao invés de uma. Logo,

| Custo Hora | Índice de Majoração |
| --- | --- |
| Seu custo na ordem de produção passou de R$ 10,00 para 20,00 | Majoração permanece R$ 1,00, pois não se pode majorar além de 1 (uma) hora que estava previsto |

Observe que pode majorar a menos, ou seja, se trabalhar apenas 30 minutos a majoração na ordem de produção seria de R$ 0,50.
