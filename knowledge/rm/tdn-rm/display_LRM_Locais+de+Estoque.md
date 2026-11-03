---
content_hash: 7fc746d22ede7756274c47d27fc029fec7487afef470145ca8247a2787db1973
fetched_at: '2026-06-29T00:09:24.653454+00:00'
page_id: '423937980'
product: rm
source: tdn-rm
title: Locais de Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/Locais+de+Estoque
version: 16
---

Por esta opção cadastra-se a tabela de local de estoque por filial.  
O Local de Estoque não é um subprocesso do sistema, porém, trata-se de uma entidade principal para o correto controle de estoque. Definido na fase de implantação e após um levantamento dos processos da empresa. É criado conforme local de armazenagem dos produtos nas filais. Tem sua importância dentro do TOTVS Gestão de Estoque, Compras e Faturamento, pois  todo o  saldo dos produtos estará vinculado à filial/local de estoque da empresa. Permitindo assim a obtenção de informações por local de estoque ou consolidados.  
O cadastro de local de estoque tem a finalidade de armazenar os produtos cadastrados no sistema, com o objetivo de realizar um controle da quantidade de produtos esta sendo alocado em determinados locais de estoque.   
Temos a possibilidade de inativar um local de estoque e desta forma, o mesmo não será mais exibido para movimentações.  
***Observação**:*

* A descrição **Local de Estoque** para esta tabela é default do sistema, podendo ser alterada através do menu Assistente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Etapa 11 - Local de Estoque.
* Segue abaixo a descrição de determinados campos do cadastro de local de estoque:

* + **Campos obrigatórios**: Filial, Código, Nível de estoque (caso esteja habilitado)
  + **Campos não obrigatórios**: Descrição, Identificador da unidade de negócio, Endereço, Default Contábeis
  + **Código**: Informe o código do local de estoque, de acordo com a máscara parametrizada em menu Assistente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Etapa 11 - Local de Estoque. já descrita acima.
  + **Faixa do Nível de Estoque**: Informe em qual das 3 faixas este local irá buscar o estoque mínimo, o estoque máximo e o ponto de pedido, cadastrados nos produtos, na pasta controle de estoque.

* O campo **Nível de Estoque** só será visualizado caso o sistema NÃO esteja parametrizado para trabalhar com ressuprimento.
* Campos ESTOQUE MINIMO, ESTOQUE MAXIMO E PONTO DE PEDIDO só serão visualizados caso o sistema NÃO esteja parametrizado para trabalhar com o modulo de ressuprimento através do menu Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.04 Gestão de Estoque | 04.04.01 - Definições de Estoque.
* **Unidade de Negócio:** Para selecionar a unidade de negócio é necessário o seu cadastramento no TOTV Gestão Fiscal, através do Menu Cadastro / Tabelas Auxiliares / Unidade de Negócio.
* No cadastro de Local de Estoque somente é possível selecionar uma unidade de negócio após selecionar uma Filial.
* A unidade de negócio irá representar nos lançamentos fiscais, o estabelecimento de empresas preparadoras de refeições coletivas, cujo preparo e fornecimento seja efetivado nas dependências de outra empresa contratante.
* As Unidades de Negócio somente serão visualizadas no local de estoque quando cadastrado na filial correspondente, exemplo:  
  No Local de estoque 01 foi cadastrada a Filial Belo Horizonte, somente as Unidades de Negócio da filial Belo Horizonte estarão disponíveis para seleção.  
  Defaults Contábeis: Campo a ser informado as contas de debito e/ou credito referente a contabilização do movimento.   
  Endereço: Segue a inclusão dos dados referente ao endereço do local de estoque, caso este possua.
