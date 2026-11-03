---
article_id: 23231167980567
category: Materiais - Compras (SIGACOM)
content_hash: b2fcf404d1b0fc8321fae76aa7a246d522218e645c0006f8a5a0bf584821b419
fetched_at: '2026-06-28T22:41:24.367667+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Regras para importação
  de NFe - Importador XML
type: support-article
updated_at: '2024-05-06T20:18:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23231167980567-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Regras-para-importa%C3%A7%C3%A3o-de-NFe-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23231167968919) Tempo aproximado para leitura: **00h05 min**

**Dúvida**Quais são as regras para importar notas fiscais do tipo NFe no Importador XML?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12

**Solução**Para identificar qual tipo da nota que será importado, a rotina Importador XML utiliza como base a tag *finNFe* do arquivos XML da NF-e

**Definição da TAG <finNFe>:**

1= NF-e Normal;

2= NF-e Complementar;

3= NF-e Ajuste;

4= Devolução de mercadoria

Abaixo disponibilizamos algumas informações sobre a tag **<finNFe>:**

--------------------------------------------------------------------------------------------------------------------

**- TAG <finNFe> esteja com o conteúdo 1 (Tipo Normal):**

- Como alterar o tipo da nota no momento da importação do XML?

1) Através ponto de entrada **A140ICFOP;**

2) **Tipo** **Bonificação:** Caso não utilize o ponto de entrada **A140ICFOP**, é verificado o parâmetro **MV\_XMLCFPC**: Se o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Bonificação.

3) **Tipo Beneficiamento:** Caso não utilize o ponto de entrada **A140ICFOP**, é verificado o parâmetro **MV\_XMLCFBN**: Se **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Beneficiamento.

4) **Tipo Devolução:** Caso não utilize o ponto de entrada **A140ICFOP**, é verificado o parâmetro **MV\_XMLCFDV**: Se o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Devolução.

--------------------------------------------------------------------------------------------------------------------

**- TAG <finNFe> esteja com o conteúdo 2 (Tipo Complemento):**

- Como alterar o tipo da nota no momento da importação do XML?

1) Não é possivel alterar o tipo da nota complemento, nem mesmo por ponto de entrada!

**IMPORTANTE**: Notas do tipo de complemento de IPI ou ICMS não são tratados pelo Totvs Colaboração.

--------------------------------------------------------------------------------------------------------------------

**- TAG <finNFe> esteja com o conteúdo 3 (Tipo Ajuste):**

**IMPORTANTE**: Esse tipo de nota não é importado pela rotina Importador XML!

--------------------------------------------------------------------------------------------------------------------

**- TAG <finNFe> esteja com o conteúdo 4 (Tipo Devolução):**

- Como alterar o tipo da nota no momento da importação do XML?

1) Através ponto de entrada **A140ICFOP;**

2) **Tipo** **Bonificação:** Caso não utilize o ponto de entrada **A140ICFOP**, é verificado o parâmetro **MV\_XMLCFPC**: Se o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Bonificação.

3) **Tipo Beneficiamento:** Caso não utilize o ponto de entrada **A140ICFOP**, é verificado o parâmetro **MV\_XMLCFBN**: Se **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Beneficiamento.

4) **Tipo Devolução:** Caso não utilize o ponto de entrada **A140ICFOP**, é verificado o parâmetro **MV\_XMLCFDV**: Se o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Devolução.

**-------------------------------------------------------------------------------------------------------------------**

**Informação Complementar:** Como o Importador XML trata as operações de beneficiamento?

Para entender melhor a operação de beneficiamento, primeiramente deve-se compreender que a empresa pode receber um produto de um cliente para beneficiá-lo ou receber um retorno de beneficiamento de um fornecedor.

**1-) Recebendo um produto para ser beneficiado em sua empresa.**  
No papel de industrializador sua empresa recebe produtos beneficiá-los, seja transformá-los em PA efetivo ( produto acabado ), ou mesmo efetuar alguma melhoria no produto recebido (como pintura, etc). Nesse cenário, na entrada dessa nota utiliza-se o tipo B, buscando o cadastro de clientes e incluí-se a nota, onde no TES utilizado há o controle de poder de terceiros. O retorno desse processo ocorrerá pela rotina do pedido de vendas e geração da nota de saída, pelo módulo do faturamento.

**2-) Quando sua empresa efetuou uma remessa de um produto para ser beneficiado em um fornecedor, ele executou o beneficiamento e agora está retornando.**  
Nesse cenário, como a operação trata um fornecedor, e, por ser que o fornecedor emita na mesma nota a cobrança do serviço que foi executado, a entrada da nota será com o tipo N ( normal ) e um item deverá contemplar o retorno do produto que foi remetido anteriormente, também controlando o poder de terceiros e, pode haver um outro item na nota referente a cobrança desse serviço. Nesse caso, o título a ser gerado no financeiro, contas a pagar, ocorrerá somente com o valor do item referente ao serviço.  
Para que esse processo funcione normalmente, é necessário configurar seu sistema Protheus corretamente, os [parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=271662192) descritos neste [documento](https://tdn.totvs.com/pages/viewpage.action?pageId=271662192) devem ser lido e configurados com os CFOP's que indiquem o tipo de operação que se está realizando e assim o fluxo de notas com tipo (Normal ou Beneficiamento) ocorrerá conforme item Regras NF-e

**Observação**

**Preenchimento do campo Nota de Origem - Nota de Devolução ou Beneficiamento**

No processo de importação do XML, o sistema somente irá vincular o documento de origem quando for "**conhecimento de frete**". Quando for "**devolução**" e "[**beneficiamento**](https://tdn.totvs.com/pages/viewpage.action?pageId=745128660)",  deve ser informado manualmente na pré-nota em Outras ações > Origem > Preenchendo os campos:

* **D1\_NFORI**
* **D1\_SERIORI**
* **D1\_ITEMORI**

***Saiba Mais :***

[IMPORTADOR XML E TOTVS COLABORAÇÃO GERAL - CENTRALIZADORA](https://tdn.totvs.com/pages/releaseview.action?pageId=540881619)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
