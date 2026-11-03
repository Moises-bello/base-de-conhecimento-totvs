---
content_hash: 2c8de5b1710fd33e57d0d3ac477b4ce7348c62aff503fab4e6f7a32c25751b36
fetched_at: '2026-06-29T00:09:15.456823+00:00'
page_id: '421385384'
product: rm
source: tdn-rm
title: Importar Preço de Insumos do Suprimento/Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385384
version: 19
---

ttruetrueLinha RM

O processo terá as seguintes opções:

**Preços habilitados**

Opções de preços que podem ser importados:

* Preço a Vista;
* Preço a Prazo;
* Preço Promoção;
* Preço em Dólar;
* Preço em Oferta;
* Custo Unitário;
* Custo Médio;

Caso seja selecionada uma das opções 'Custo Unitário' ou 'Custo Médio', irá aparecer o Passo 02 (segunda tela, para ser parametrizada de acordo com preferências do usuário).

**Observação:**

Para a utilização destes campos, eles devem estar habilitados nos parâmetros do Gestão de Estoque, Compras e Faturamento.

**Custo por Filial/Local**  
Ao selecionar 'Custo Unitário' ou 'Custo Médio' (do Passo 01), será exibido o local de estoque ou a filial conforme estiver parametrizado, para ser selecionado também.

* Se estiver parametrizado como Filial, será exibido a mensagem:
  + Seu custo está por Filial, escolha o correto.
* Se estiver parametrizado como Local, será exibido a mensagem:
  + Seu custo está por Local, escolha o correto.

**Opções de Conversão dos Preços**

* Converter preço para moeda do projeto sem manter a indexação:
  + O TOP irá buscar o preço do produto e converter a moeda corrente para a mesma moeda do projeto, modificando a moeda indexadora  igual  a do projeto.
* Converter preço para moeda do projeto e manter a indexação:
  + O TOP irá buscar o preço do produto e converter a moeda corrente para a mesma moeda do projeto sem alterar a moeda indexadora.
* Manter moeda do preço:
  + O TOP irá buscar o preço do produto e irá manter a mesma moeda cadastrada no produto.

**Descrição do Preço Importado**  
A descrição será de acordo com a opção a "opção de preço" selecionada.

* Exemplo: Caso tenha selecionado em preço habilitado, a opção "Preço a Vista" a descrição será: "Preço a Vista Importado de Suprimentos/Faturamento em 01/10/2015"
* Por padrão será disponibilizada esta descrição, mas ela pode ser editada pelo usuário.

**Sobrepor preço com a mesma descrição**  
É possível escolher se o preço a ser importado, sobrescrevera um preço existente, ou se será gera um novo registro para o insumo. Por padrão esta opção aparece marcada.  
**Ativar preço (habilitado) importado**  
Por padrão esta opção aparece marcada. O preço selecionado substitui o preço ativo no TOP.  
**Utilizar tabelas de preço**  
Por padrão esta opção aparece desmarcada. Se esta opção for marcada, será exibido o passo dois, com:

* As tabelas de prioridade de consulta das tabelas de preços (um produto pode estar associado a mais de uma tabela na mesma vigência, sendo necessário definir uma prioridade no movimento para determinar o preço a ser utilizado).
* O Cronograma de aplicação da vigência (O cálculo do cronograma do TOP utilizará o preço de acordo com os cronogramas selecionados).

Para as tabelas de preços: Um produto pode estar associado a mais de uma tabela na mesma vigência, sendo necessário definir uma prioridade no movimento para determinar o preço a ser utilizado.  
**Para realizar a importação, siga as instruções abaixo:**  
Acesse o cadastro de insumos "Menu Orçamento | Insumos | Cadastro" >  Selecionar um ou mais insumo(s) > Clicar em "Processos" > "Importar Preços de Suprimentos/Faturamento" >  Marcar a opção do tipo do preço que deseja importar > Marcar a opção do tipo de conversão de moeda que deseja utilizar na importação > Informar a descrição do preço > Marcar ou não a opção de sobrescrever preço já existente com a mesma descrição > Marcar ou não a opção de ativar o preço importado > Marcar ou não a opção de utilizar tabela de preço (Se esta opção for marcada a de "Sobrescrever" será desabilitada) > "Avançar" o processo >  Selecione o filtro prioritário (Município, Estado, Filial e Condição de Pagamento) > Marcar ou não a opção Cronograma Planejado>  Marcar ou não a opção Cronograma Realizado> Marcar ou não a opção Cronograma Medido>"Executar" o processo. Após estes passos será gerada a mensagem de log.  
**Parâmetros:**  
·         Se o parâmetro de projeto Vigência de Preço, estiver como 'Não utiliza', a opção 'Utilizar tabelas de preço' será desabilitada;  
·         Se o parâmetro de projeto Vigência de Preço, estiver marcada a opção 'Aplicar preços em percentual',  os preços já existentes do insumo, poderão ser recalculados.  
·         Acesso: Parâmetros de Projeto (F6) >> Cálculo >> BDI >> Vigência de preço  
   
**Importante:**  
Para casos onde ocorrer erros durante a importação será registrado um Log, informando quais preços não foram importados devido a divergência de Unidade de Medida entre Insumo/Produto.  
Quando selecionada a opção "Utilizar tabelas de preço" não será possível sobrescrever preço pela descrição, pois o TOP poderá inserir vários preços com a mesma descrição, de acordo com as vigências dos produtos cadastrados nas tabelas de preço.  
A importação irá desconsiderar os insumos, cuja unidade seja diferente do seu produto associado, ou que não tiverem um produto associado. Para os demais insumos, a importação ocorrerá normalmente. 

Linha Protheus

A partir da versão 12.1.31, será possível efetuar essa importação a partir de uma base de dados do Protheus, quando o Backoffice utilizado for este.

**Preços habilitados**

Opções de preços que podem ser importados:

* Preço 1;
* Preço 2;
* Custo Unitário;
* Custo Médio;

Abaixo destacamos a correlação entre os preços (campo do Protheus e o correspondente na linha RM).

|  |  |
| --- | --- |
| B1\_PRV1 | TPRD.PRECO1 |
| BZ\_UPRC | TPRD.PRECO2 |

Com relação aos custos, estes serão consultados conforme a tabela abaixo:

|  |  |
| --- | --- |
| Pela chave SB1->B1\_COD + SB1->B1\_LOCPAD  E recuperado o SB2->**B2\_CM1** | TPRD.CUSTOMEDIO |
| BZ\_CUSTD | TPRD.CUSTOUNITARIO |

Caso seja selecionada uma das opções 'Custo Unitário' ou 'Custo Médio', irá aparecer o Passo 02 (segunda tela, para ser parametrizada de acordo com preferências do usuário).

**Observação:**

Para a utilização destes campos, eles devem estar habilitados nos parâmetros do Gestão de Estoque, Compras e Faturamento.

**Custo por Filial/Local**  
Ao selecionar 'Custo Unitário' ou 'Custo Médio' (do Passo 01), será exibido o local de estoque ou a filial conforme estiver parametrizado, para ser selecionado também.

* Se estiver parametrizado como Filial, será exibido a mensagem:
  + Seu custo está por Filial, escolha o correto.
* Se estiver parametrizado como Local, será exibido a mensagem:
  + Seu custo está por Local, escolha o correto.

**Opções de Conversão dos Preços**

* Converter preço para moeda do projeto sem manter a indexação:
  + O TOP irá buscar o preço do produto e converter a moeda corrente para a mesma moeda do projeto, modificando a moeda indexadora  igual  a do projeto.
* Converter preço para moeda do projeto e manter a indexação:
  + O TOP irá buscar o preço do produto e converter a moeda corrente para a mesma moeda do projeto sem alterar a moeda indexadora.
* Manter moeda do preço:
  + O TOP irá buscar o preço do produto e irá manter a mesma moeda cadastrada no produto.

**Descrição do Preço Importado**  
A descrição será de acordo com a opção a "opção de preço" selecionada.

* Exemplo: Caso tenha selecionado em preço habilitado, a opção "Preço a Vista" a descrição será: "Preço a Vista Importado de Suprimentos/Faturamento em 01/10/2015"
* Por padrão será disponibilizada esta descrição, mas ela pode ser editada pelo usuário.

**Sobrepor preço com a mesma descrição**  
É possível escolher se o preço a ser importado, sobrescrevera um preço existente, ou se será gera um novo registro para o insumo. Por padrão esta opção aparece marcada.  
**Ativar preço (habilitado) importado**  
Por padrão esta opção aparece marcada. O preço selecionado substitui o preço ativo no TOP.  
**Utilizar tabelas de preço**  
Por padrão esta opção aparece desmarcada. Se esta opção for marcada, será exibido o passo dois, com:

* As tabelas de prioridade de consulta das tabelas de preços (um produto pode estar associado a mais de uma tabela na mesma vigência, sendo necessário definir uma prioridade no movimento para determinar o preço a ser utilizado).
* O Cronograma de aplicação da vigência (O cálculo do cronograma do TOP utilizará o preço de acordo com os cronogramas selecionados).

Para as tabelas de preços: Um produto pode estar associado a mais de uma tabela na mesma vigência, sendo necessário definir uma prioridade no movimento para determinar o preço a ser utilizado.  
**Para realizar a importação, siga as instruções abaixo:**  
Acesse o cadastro de insumos "Menu Orçamento | Insumos | Cadastro" >  Selecionar um ou mais insumo(s) > Clicar em "Processos" > "Importar Preços de Suprimentos/Faturamento" >  Marcar a opção do tipo do preço que deseja importar > Marcar a opção do tipo de conversão de moeda que deseja utilizar na importação > Informar a descrição do preço > Marcar ou não a opção de sobrescrever preço já existente com a mesma descrição > Marcar ou não a opção de ativar o preço importado > Marcar ou não a opção de utilizar tabela de preço (Se esta opção for marcada a de "Sobrescrever" será desabilitada) > "Avançar" o processo >  Selecione o filtro prioritário (Município, Estado, Filial e Condição de Pagamento) > Marcar ou não a opção Cronograma Planejado>  Marcar ou não a opção Cronograma Realizado> Marcar ou não a opção Cronograma Medido>"Executar" o processo. Após estes passos será gerada a mensagem de log.  
**Parâmetros:**  
·         Se o parâmetro de projeto Vigência de Preço, estiver como 'Não utiliza', a opção 'Utilizar tabelas de preço' será desabilitada;  
·         Se o parâmetro de projeto Vigência de Preço, estiver marcada a opção 'Aplicar preços em percentual',  os preços já existentes do insumo, poderão ser recalculados.  
·         Acesso: Parâmetros de Projeto (F6) >> Cálculo >> BDI >> Vigência de preço  
   
**Importante:**  
Para casos onde ocorrer erros durante a importação será registrado um Log, informando quais preços não foram importados devido a divergência de Unidade de Medida entre Insumo/Produto.  
Quando selecionada a opção "Utilizar tabelas de preço" não será possível sobrescrever preço pela descrição, pois o TOP poderá inserir vários preços com a mesma descrição, de acordo com as vigências dos produtos cadastrados nas tabelas de preço.  
A importação irá desconsiderar os insumos, cuja unidade seja diferente do seu produto associado, ou que não tiverem um produto associado. Para os demais insumos, a importação ocorrerá normalmente.

**Antes de executar o processo descrito, certifique-se de que a integração está devidamente parametrizada.**

**As informações necessárias, encontram-se no link abaixo:**

<https://tdn.totvs.com/display/public/INT/3+-+PROCESSOS>
