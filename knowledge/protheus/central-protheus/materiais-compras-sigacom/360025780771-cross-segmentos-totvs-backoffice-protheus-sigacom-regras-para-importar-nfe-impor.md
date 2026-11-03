---
article_id: 360025780771
category: Materiais - Compras (SIGACOM)
content_hash: 7ff63592875fc08c48f30e09198ecffae42a55d626d8e0f991e335a05b0688dc
fetched_at: '2026-06-28T22:41:10.437603+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Regras para importar
  NFe - Importador Xml
type: support-article
updated_at: '2025-06-11T22:53:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025780771-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Regras-para-importar-NFe-Importador-Xml
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23231110584599) Tempo aproximado para leitura: 00h05 min**

**Dúvida**Regras para importar NFe - Totvs Colaboração / Importador Xml  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12  
  
**Solução**Regra de importação dos arquivos XML de NF-e

*Definição da TAG <finNFe>:*

**Finalidade da NF-e:**

*1=NF-e Normal;*

*2=NF-e Complementar;*

*3=NF-e Ajuste;*

*4=Devolução de mercadoria*

Regra de importação dos arquivos XML de NF-e

*Definição da TAG <finNFe>:*

**Finalidade da NF-e:**

*1=NF-e Normal;*

*2=NF-e Complementar;*

*3=NF-e Ajuste;*

*4=Devolução de mercadoria*

* Caso a TAG <finNFe> esteja com o conteúdo 1 no XML da NF-e, o sistema tratará o tipo da nota da seguinte forma:

*- O tipo da nota será normal (tipo = N).*

**Maneira de mudar o tipo da nota nesse caso:**

1) Verifica se o ponto de entrada **A140ICFOP** está compilado no repositório, caso esteja, obtêm o tipo da nota do retorno do ponto de entrada e ignora o tipo normal e passa a importar a nota com o tipo retornado pelo ponto de entrada.

2) Caso o ponto de entrada **A140ICFOP** não seja utilizado, é verificado o parâmetro **MV\_XMLCFPC**, e caso o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Bonificação.

3) Caso o ponto de entrada **A140ICFOP** não seja utilizado, é verificado o parâmetro **MV\_XMLCFBN**, e caso o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Beneficiamento.

4) Caso o ponto de entrada **A140ICFOP** não seja utilizado, é verificado o parâmetro **MV\_XMLCFDV**, e caso o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Normal e importa a nota como tipo Devolução.

* Caso a TAG <finNFe> esteja com o conteúdo 2 no XML da NF-e, o sistema tratará o tipo da nota da seguinte forma:

*- O tipo da nota será complemento de preço (tipo = C).*

**Maneira de mudar o tipo da nota nesse caso:**

Não há disponibilidade de realizar essa ação.

**IMPORTANTE: Notas do tipo de complemento de IPI ou ICMS não são tratados pelo Totvs Colaboração.**

* Caso a TAG <finNFe> esteja com o conteúdo 3 no XML da NF-e, o sistema tratará o tipo da nota da seguinte forma:

**IMPORTANTE: Notas de ajuste não são tratadas pelo Totvs Colaboração.**

* Caso a TAG <finNFe> esteja com o conteúdo 4 no XML da NF-e, o sistema tratará o tipo da nota da seguinte forma:

*- O tipo da nota será devolução (tipo = D).*

**Maneira de mudar o tipo da nota nesse caso:**

1) Verifica se o ponto de entrada **A140ICFOP** está compilado no repositório, caso esteja, obtêm o tipo da nota do retorno do ponto de entrada e ignora o tipo Devolução e passa a importar a nota com o tipo retornado pelo ponto de entrada.

2) Caso o ponto de entrada **A140ICFOP** não seja utilizado, é verificado o parâmetro **MV\_XMLCFNO**, e caso o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Devolução e importa a nota como tipo Normal.

3) Caso o ponto de entrada **A140ICFOP** não seja utilizado, é verificado o parâmetro **MV\_XMLCFBN**, e caso o **CFOP** do produto esteja contido neste parâmetro, o sistema ignora o tipo Devolução e importa a nota como tipo Beneficiamento.

**Como o Totvs Colaboração trata as operações de beneficiamento**

Para entender melhor a operação de beneficiamento, primeiramente deve-se compreender que a empresa pode beneficiar um produto de terceiros e devolvê-lo pronto (PA) ou pode solicitar um beneficiamento a um fornecedor e este devolver o produto pronto para a empresa, ou seja, a empresa pode assumir o papel de realizar o beneficiamento ou solicitá-lo a terceiros.

No sistema ambos os processos podem ser realizados, utilizando o tipo da nota (Normal ou Beneficiamento). No caso onde a empresa realiza o beneficiamento, a matéria prima (MP) deve ser recebida via documento de entrada com tipo Beneficiamento, pois assim o sistema habilita o cadastro de clientes no documento de entrada, assim a saída do produto pronto (PA) se dará através de uma nota de saída do tipo Normal, todo o fluxo Fiscal, Financeiro (Contas a Receber), Estoque e demais módulos serão alimentados corretamente.

No caso da empresa solicitar o beneficiamento a terceiros, a matéria prima (MP) deverá sair através de um documento de saída do tipo Beneficiamento, pois desse modo o sistema habilita o cadastro de fornecedores no documento de saída, assim a entrada do produto pronto (PA) se dará através de uma nota de entrada do tipo Normal, todo o fluxo Fiscal, Financeiro (contas a pagar), Estoque e demais módulos serão alimentados corretamente.

Para que esse processo funcione normalmente, é necessário configurar seu sistema Protheus corretamente, os parâmetros descritos nos **Parâmetros ([Parâmetros](http://tdn.totvs.com/pages/viewpage.action?pageId=271662192))** deste documento deve ser lido e configurado com os CFOP's que indiquem o tipo de operação que se está realizando e assim o fluxo de notas com tipo (Normal ou Beneficiamento) ocorrerá conforme item **Regras NF-e**

**Observação 1**

**Preenchimento do campo Nota de Origem - Nota de Devolução ou Beneficiamento**

No processo de importação do XML, o sistema somente irá vincular o documento de origem, quando for "**conhecimento de frete**". Quando for "**devolução**" e "**beneficiamento**",  deve ser informado manualmente a nota de saída nos campo a seguir:

* **D1\_NFORI**
* **D1\_SERIORI**
* **D1\_ITEMORI**

**Observação 2**

Na importação de um documento CTE, quando a busca pelo documento de origem for realizada pelo numero do documento, o numero do documento deve estar incluído com zeros a esquerda.

Ex:

No XML, o numero está: 54060

No Sistema, o numero deve estar: 000054060

***Saiba Mais :***

[Totvs Colaboração identificação de documento de origem pelo numero do documento.](https://tdn.totvs.com/pages/releaseview.action?pageId=412879608)

***[SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML?source=search)  
[Pontos de Entrada](https://tdn.totvs.com/display/public/PROT/IX02+-+Pontos+de+Entrada)***

[IMPORTADOR XML E TOTVS COLABORAÇÃO GERAL - CENTRALIZADORA](https://tdn.totvs.com/pages/releaseview.action?pageId=540881619)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
