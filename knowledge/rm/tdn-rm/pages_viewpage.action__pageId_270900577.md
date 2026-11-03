---
content_hash: 434de6f417b69a9a83ed84e67a8ae6c8b477eb8b774362587d921b46c397837b
fetched_at: '2026-06-29T00:08:24.704800+00:00'
page_id: '270900577'
product: rm
source: tdn-rm
title: 197233 MCP-1273 DT NF-e Nota Técnica 2016/001 - Unidade Tributável no Comércio
  Exterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270900577
version: 143
---

# NOTA TÉCNICA 2016/001 - UNIDADE TRIBUTÁVEL NO COMÉRCIO EXTERIOR

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Unidade | EstUndAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | FisNFeEnvioAction | Envio de NF-e | |
| **Tickets relacionados** | 197233 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | TPRODUTODEF - Definições dos Produtos  TUND - Unidade |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Esta melhoria tem como objetivo possibilitar que o TOTVS Gestão de Estoque, Compras e Faturamento atenda à Nota Técnica 2016/001 que adequa a NF-e ao Projeto do Portal Único do Comércio Exterior, padronizando a Tabela de Unidades de Medidas Tributáveis no Comércio Exterior, conforme o código NCM (Nomenclatura Comum do Mercosul) da mercadoria a que se refere, com base nas unidades recomendadas pela Organização Mundial de Aduanas (OMA).  

A Nota Técnica 2016/001 estabeleceu uma Tabela de Unidades de Medidas Tributáveis no Comércio Exterior, publicada na aba “Documentos”, opção “Diversos”, do Portal da NF-e, a qual relaciona, para cada código NCM, a unidade de medida que deverá ser obrigatoriamente utilizada na emissão de documentos fiscais, para quantificar os produtos a que se refiram, nos campos relativos à Unidade Tributável (uTrib) e Quantidade Tributável (qTrib) da Nota Fiscal Eletrônica – NF-e.

O disposto na NT 2016/001 aplica-se apenas aos contribuintes que operem no Comércio Exterior, relativamente às notas fiscais relacionadas a Operações de Exportação (tpNF=1-Saída e idDest=3) ou nas Operações vinculadas à Exportação (CFOP=1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505).

## Procedimento para Utilização

O primeiro passo para atender à Nota Técnica 2016/001 e implementar as Unidades de Medidas Tributáveis no Comércio Exterior em sua empresa é informar no cadastro de Unidades do TOTVS Gestão de Estoque, Compras e Faturamento, qual o Código da Unidade Tributável correspondente a cada unidade comercial utilizada na exportação.

Para isso, vá em **Cadastros | Mais... | Tabelas Auxiliares | Unidade**, e para as unidades que são tributáveis, forneça o código da respectiva Unidade Tributável que consta da tabela publicada na aba “Documentos”, opção “Diversos”, do Portal da NF-e, a qual relaciona, para cada código NCM, a sua respectiva unidade de medida tributável.

O campo Cód. Unidade Tributável somente estará habilitado para preenchimento, caso a unidade esteja configurada como Tributável, e neste caso o preenchimento do código é obrigatório.

Caso o campo Tributável esteja marcado e o Código da Unidade Tributável não esteja preenchido, o sistema não permitirá, apresentando, no momento da gravação do registro, a seguinte mensagem:

Da mesma forma, o sistema também não permitirá que o campo Código da Unidade Tributável esteja preenchido caso o campo Tributável não esteja marcado, apresentando a seguinte mensagem:

O fator de conversão informado na Unidade será utilizado no cálculo da quantidade na Unidade Tributária (campo qTrib da NF-e).

Ainda para atender à Nota Técnica 2016/001 também foram criados no cadastro de Produtos os campos:

* Unidade Tributável;
* Fator de Conversão Unidade Tributável.

Assim, caso sua empresa possua produtos nos quais, devido às suas características, deve ser utilizada uma unidade tributável específica, ou para o cálculo da sua quantidade na Unidade Tributável é necessário ser utilizado um fator de conversão específico, você poderá informá-los individualmente para cada um desses produtos.

Para preencher esses campos vá em **Cadastros | Produto |** **Controle Estoque**.

Diferente das demais unidades do cadastro, nas quais na seleção podem ser apresentadas todas as unidades cadastradas, na seleção da Unidade Tributável, o sistema lhe apresentará apenas as unidades que estão configuradas como Tributável, ou seja, apenas aquelas que no cadastro de Unidades estão com o campo Cód. Unidade Tributável preenchido.

Após selecionar a Unidade Tributável, informe o Fator de Conversão Tributável a ser aplicado sobre a mesma para o cálculo da Quantidade na Unidade Tributável (qTrib) na NF-e.

No momento da gravação do registro do Produto o sistema irá verificar, e caso a unidade base da Unidade Tributária informada seja diferente da unidade base da Unidade de Controle do produto, o sistema não permitirá, sendo exibida a seguinte mensagem:

Entretanto, para alguns clientes o fator de conversão dos produtos não é fixo, devido a características físico/químicas destes produtos. É o caso por exemplo das empresas que vendem pedras, pois no Mercado Nacional as pedras são controladas por m² ou m³ e no Comércio Exterior por kg. Nesse caso, a cada venda para o Comércio Exterior haverá um fator de conversão específico. Pensando neste cenário, foi criado nos parâmetros de tipo de movimento em Fis – NF-e, no groupbox NF-e Estadual, o parâmetro do tipo checkbox “Habilita Quantidade Tributável”. Por default esse parâmetro esta desmarcado.

Caso esse parâmetro esteja marcado, na tela de item de movimento, no menu “Integrações”, opção “Fiscal”, será exibido um campo para que o usuário informe a “Quantidade Tributável” do produto que está sendo vendido. Esse campo segue o padrão de casas decimais definido nos “Parâmetros Gerais”. Se o parâmetro estiver desmarcado, o campo “Quantidade Tributável” não será exibido.

Na geração do arquivo XML das NF-e relacionadas a Operações de Exportação (tpNF=1-Saída e idDest=3) ou nas Operações vinculadas à Exportação (CFOP=1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505), o sistema irá:

* Identificar o código da Unidade Tributável de cada item da NF-e conforme a seguinte prioridade:
  + Cadastro de Produtos - verificará o preenchimento do campo Código da Unidade Tributável e caso o mesmo esteja preenchido, irá enviar o seu conteúdo para o campo uTrib do XML da NF-e;
  + Cadastro de Unidades - caso o produto não tenha unidade tributável cadastrada, será verificado no cadastro de Unidades o preenchimento do campo Código da Unidade Tributável da unidade utilizada no item de movimento e caso o mesmo esteja preenchido, irá enviar o seu conteúdo para o campo uTrib do XML da NF-e;
  + Unidade Base - caso nem o produto e nem a unidade utilizada no item de movimento possuam unidade tributável informada, o sistema irá verificar a unidade base da unidade do item de movimento, e caso a unidade tributável da mesma esteja preenchida, irá enviar o seu conteúdo para o campo uTrib do XML da NF-e. Se a unidade base não estiver configurada como unidade tributável, será enviado o próprio código da unidade base.
* Identificar o Fator de Conversão a ser utilizado no cálculo da quantidade na unidade tributável conforme a seguinte prioridade:
  + Caso o produto possua Unidade Tributável configurada, o sistema irá verificar se o Fator de Conversão Tributável também foi informado, e em caso positivo, o sistema utilizará o mesmo para o cálculo e gravação da quantidade na unidade tributável (campo qTrib do XML da NF-e);
  + Caso o produto possua Unidade Tributável mas o Fator de Conversão Tributável não esteja informado, o sistema utilizará o Fator de Conversão cadastrado para a Unidade Tributável parametrizada no produto;
  + Caso o produto não possua Unidade Tributável e a unidade utilizada no item de movimento seja tributável, o sistema utilizará o fator de conversão = 1;
  + Caso o produto não possua Unidade Tributável e a unidade utilizada no item de movimento também não seja tributável, o sistema utilizará o fator de conversão = 1.
  + Caso o campo “Quantidade Tributável” estiver preenchido no item de movimento, não será necessário fazer o cálculo da Quantidade na Unidade Tributável (qTrib) que será informada no XML, bastando apenas copiar a informação desse campo. O campo Unidade Tributável (uTrib) deverá ser informado no XML com o resultado da divisão do “Valor Líquido” do item pela “Quantidade Tributável” do item.

Vamos detalhar abaixo, através de exemplos, a forma como o sistema irá executar a gravação da Unidade Tributável (uTrib) e da Quantidade na Unidade Tributável (qTrib) no XML da NF-e:

**Exemplo 1:**

Vamos utilizar as unidades M3 (unidade comercial) e KG (unidade tributável determinada pela NT 2016/001), supondo que 1 M3 corresponda a 1,5 KG.

Neste caso tanto a Unidade Tributável como o Fator de Conversão Tributável estão informados no Produto e portanto seus dados serão utilizados na geração do XML.

Assim, para gerar o XML, o sistema, através da Unidade Tributável do produto, irá ao cadastro de unidades e preencherá o campo uTrib com o Cód. Unidade Tributável informado na Unidade Tributável cadastrada para o produto, ou seja, neste caso, KG.

Para o cálculo da quantidade tributável (qTrib) o sistema irá efetuar a conversão entre a unidade origem (comercial = M3) e a unidade destino (tributável = KG/M3), ou seja será utilizado para o cálculo da quantidade tributária o resultado da divisão do Fator de Conversão da Unidade Origem pelo Fator de Conversão da Unidade Destino, no caso desse nosso exemplo 1/1,5 = 0,6667.

Neste caso para cada M3 vendido teremos 0,6667 KG vendido.

**Exemplo 2:**

Neste caso o sistema utilizará o cód. unidade tributável da Unidade Tributável informada no Produto (KG).

Para o cálculo da quantidade tributável (qTrib) o sistema irá efetuar a conversão entre a unidade origem (comercial = M3) e a unidade destino (tributável = KG/M3), ou seja será utilizado para o cálculo da quantidade tributária o resultado da divisão do Fator de Conversão da Unidade Origem pelo Fator de Conversão da Unidade Destino, no caso desse nosso exemplo 1/2 = 0,5.

Neste caso para cada M3 vendido teremos 0,5 KG vendido.

**Exemplo 3:**

Neste caso, o Fator de Conversão Tributável informado no Produto não será considerado, já que a Unidade Tributável do mesmo não está informada.

**Exemplo 4:**

Neste caso, como não existe Unidade Tributável específica no Produto, o sistema irá procurá-la na Unidade informada para o item de movimento.

Caso a Unidade do item de movimento esteja configurada como Tributável, o sistema irá gerar o XML com o Cód. Unidade Tributável informado para a mesma (KG), e o Fator de Conversão (1) no cálculo da quantidade na unidade tributável.

**Exemplo 5:**

Neste caso, como não existe Unidade Tributável para o Produto, o sistema irá procurá-la na Unidade informada para o item de movimento.

Como a Unidade do item de movimento (PC) não é Tributável, o sistema irá para a sua Unidade Base (UN) e como ela é uma unidade tributável, os seus dados é que serão utilizados na geração do XML da NF-e.

Caso a Unidade Base da Unidade do item de movimento também não esteja configurada como Tributável, será enviado o seu próprio código para o campo unidade tributável (uTrib) do XML, sendo utilizado o  Fator de Conversão (1) para o cálculo da quantidade na unidade tributável (qTrib).

**Exemplo 6:**

Caso o campo “Quantidade Tributável” estiver preenchido no item de movimento, não será necessário fazer o cálculo da Quantidade na Unidade Tributável (qTrib) que será informada no XML, bastando apenas copiar a informação desse campo. O campo Unidade Tributável (uTrib) deverá ser informado no XML com o resultado da divisão do “Valor Líquido” do item pela “Quantidade Tributável” do item.

Neste caso a Quantidade na Unidade Tributável (qTrib) será 25. O campo Unidade Tributável (uTrib) será igual a (100 x 50) / 25 = 200.

**Para realizar a implantação da funcionalidade na versão 12.1.14, é necessário executar os scripts EXECSQLTOTVSGESTAODEESTCOMPFATMCP-1273.ZIP e MCP-1573\_1200.ZIP****disponíveis no pacote, já para as versões superiores à 12.1.14 não há necessidade de execução de nenhum script específico.**

****Para utilizar o parâmetro "Habilita Quantidade Tributável" é necessário realizar a utilização da versão 12.1.18. Para as****versões inferiores não há possibilidade de utilização da funcionalidade.****

divs
