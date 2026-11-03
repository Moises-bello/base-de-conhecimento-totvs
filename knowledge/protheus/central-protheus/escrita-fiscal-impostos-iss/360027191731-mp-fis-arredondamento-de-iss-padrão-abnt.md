---
article_id: 360027191731
category: Escrita Fiscal - Impostos - ISS
content_hash: b652b37fee764fd98a78b7d035e29f4b4c5d4c427be316be279135e552a123a8
fetched_at: '2026-06-28T22:39:35.292736+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: MP - FIS - Arredondamento de ISS Padrão ABNT
type: support-article
updated_at: '2021-04-29T18:26:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027191731-MP-FIS-Arredondamento-de-ISS-Padr%C3%A3o-ABNT
---

**Dúvida**Procedimentos referente arredondamento de ISS Padrão ABNT.   
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**O provedor ISS.NET utiliza os critérios de arredondamento definidos na norma ABNT NBR 5891/77 e na resolução 886/66 do IBGE para validação do valor de ISS enviado nas notas de serviço.

Desta forma, estas regras se aplicam a **todas** as prefeituras que utilizam este serviço. Os critérios são:

|  |  |
| --- | --- |
| Critério | Exemplo |
| --- | --- |
| Quando o algarismo a ser conservado for seguido de algarismo **inferior** a 5, permanece o algarismo a ser conservado e retiram-se os posteriores. | 1,3333 arredondado à segunda decimal torna-se 1,33. |
| Quando o algarismo a ser conservado for seguido de algarismo **superior** a 5, soma-se uma unidade ao algarismo a ser conservado e retiram-se os posteriores. | 1,6666 arredondado à segunda decimal torna-se 1,67. |
| Quando o algarismo a ser conservado for seguido de algarismo **igual** a 5, seguido de **no mínimo um algarismo diferente de zero**, soma-se uma unidade ao algarismo a ser conservado e retiram-se os posteriores. | 4,8552 arredondado à segunda decimal torna-se 4,86. |
| Quando o algarismo a ser conservado for seguido de 5 e posteriormente de zeros, e for **ímpar**, soma-se uma unidade ao algarismo a ser conservado e retiram-se os posteriores. | 4,8550 arredondado à segunda decimal torna-se 4,86. |
| Quando o algarismo a ser conservado for seguido de 5 e posteriormente de zeros, e for **par**, permanece o algarismo a ser conservado e retiram-se os posteriores. | 4,8850 arredondado à segunda decimal torna-se 4,88. |

Para configurar este tratamento no sistema é necessário configurar o parâmetro **MV\_IBGE886** como ( **.T.**).Uma vez efetuada esta configuração, o cálculo do ISS será efetuado conforme descrito nos itens abaixo.

**Importante**

É importante ressaltar que a validação no momento da transmissão do documento ocorre sobre o valor **total**do ISS já que, mesmo que algumas prefeituras permitam a utilização de mais de um item no mesmo documento, o valor do ISS não é enviado item a item.

Utilizando-se o método abaixo garante-se que, além do arredondamento do total do ISS, a soma dos itens corresponda ao total do cabeçalho.

1. Calcula-se o ISS normalmente, item a item, considerando-se as configurações já existentes (**MV\_RNDISS** e **MV\_RNDSOBR**);

   Dica

   Recomenda-se a utilização do parâmetro **MV\_RNDISS**como **.T.**em conjunto com o **MV\_IBGE886**pois se todos os valores forem truncados é possível que a diferença em relação ao valor arredondado conforme a ABNT seja superior a 0,01 (1 centavo), e esta diferença será descarregada totalmente no último item do documento, o que pode ser interpretado como erro de cálculo.
2. Totaliza-se o valor de ISS de cada item no cabeçalho do documento;
3. No último item do documento, após aplicados os tratamentos citados no item 1, calcula-se novamente o ISS total do documento, e sobre este ISS são aplicadas as regras de arredondamento conforme a norma ABNT NBR 5891/77;
4. Se o valor total arredondado conforme os critérios da ABNT for diferente do valor já totalizado, o ajuste será feito no **último** item do documento. Normalmente será somado ou subtraído 0,01 (1 centavo) conforme o valor resultante;

   Importante

   O tratamento para efetuar o acerto no último item do documento aplica-se **somente** a documentos gerados via **pedido de venda** / **faturamento** pois nas demais rotinas de geração de notas fiscais não é possível determinar a quantidade de itens do documento, já que os itens são adicionados conforme a digitação. Nestas rotinas o tratamento é aplicado, porém item a item, assim como ocorre com os demais tributos.
5. Totaliza-se novamente o ISS considerando o valor do último item atualizado;

**Importante**

O arredondamento conforme configuração do parâmetro **MV\_IBGE886**não é considerado para movimento de **entrada**, apenas para **saídas**.

**Importante**

Além das configurações da norma ABNT para ISS existem outras possíveis configurações para arredondamento de Impostos:

[FIS00024\_Arredondamento\_de\_Impostos](https://tdn.totvs.com/display/PROT/FIS00024_Arredondamento_de_Impostos)

<https://tdn.totvs.com/display/public/PROT/FIS00024_Arredondamento_de_Impostos>

**Informações obtidas através do link:**

<http://tdn.totvs.com/pages/releaseview.action?pageId=446702089>
