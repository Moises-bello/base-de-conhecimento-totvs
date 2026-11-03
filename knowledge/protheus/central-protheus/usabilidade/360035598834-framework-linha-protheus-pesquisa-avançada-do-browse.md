---
article_id: 360035598834
category: Usabilidade
content_hash: deddfe3485476d97fd8ef3e54a24406de532bc71cf834aa86c11d001ff8808c6
fetched_at: '2026-06-28T22:42:17.274796+00:00'
product: protheus
section_id: 360000076807
source: central-protheus
title: Framework - Linha Protheus - Pesquisa Avançada do Browse
type: support-article
updated_at: '2026-01-26T19:40:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035598834-Framework-Linha-Protheus-Pesquisa-Avan%C3%A7ada-do-Browse
---

**Dúvida**  
Como funciona a pesquisa avançada do browse?  
  
**Ambiente**  
Protheus - Browse - A partir da versão 11  
  
**Solução**  
A **Pesquisa Avançada** (**Pesquisa por Coluna** no Protheus 12) é uma alternativa à pesquisa tradicional do **browse** que utiliza chaves de índices. O **browse** é a lista com colunas que surge ao acionarmos a maioria das opções de menu do sistema Protheus, exibindo o conteúdo de uma tabela.   
  
No modelo avançado de pesquisa, é possível pesquisar expressões contidas em campos, localizar textos independentemente da acentuação e da caixa alta / baixa (letras maiúsculas e minúsculas).  
A **pesquisa avançada** se diferencia da construção de filtros devido a maior agilidade no uso. A construção de filtros, por outro lado, permite a construção de expressões complexas contendo mais de um campo.    
A **pesquisa avançada** estará disponível apenas em tabelas gerenciadas pelo Top Connect (SQL), devido aos recursos avançados de busca que utiliza.   
  
**Procedimentos para Utilização:**  
**Para Protheus 11**:  
Para utilizar a pesquisa avançada, deve-se acionar o “combobox” localizado à direita do botão Pesquisar. Neste combobox é possível alternar entre a **pesquisa tradicional indexada** (“normal”) e a **pesquisa avançada** (“avançada”).  
  
![Pesq01.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047252893)  
  
Ao selecionar a opção **Avançada**, ocorre uma alteração no “combobox” de seleção de ordem de busca, mostrado abaixo. Ao invés de exibir as chaves de índices disponíveis para a tabela, passam a serem exibidos, separadamente, os campos elegíveis para busca. Por razões de desempenho, são exibidos apenas os campos que compõe alguma chave de índice. Isso dá mais alternativas para o banco de dados localizar rapidamente a informação  
  
![Pesq02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046391514)  
  
Deve-se selecionar o **campo desejado** e preencher o **campo de conteúdo**. Após o preenchimento deve-se clicar no botão Pesquisar. É possível informar expressões com acento e tanto os itens acentuados quanto os não acentuados serão localizados. Essa **pesquisa** também vai localizar itens em letras maiúsculas ou minúsculas.   
Tomemos como exemplo o cadastro de municípios, tabela CC2. Efetuaremos uma busca pela expressão “são PAULO”, utilizando para tanto o campo Município que contém o nome do município.   
  
![Pesq03.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046391734)  
  
Foram localizados todos os municípios que continham “São Paulo” no nome, independentemente da acentuação e das letras maiúsculas e minúsculas empregadas na busca.  
  
![Pesq04.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047253873)  
  
A **Pesquisa Avançada** também se diferencia da normal, pois após pesquisar são exibidos apenas os registros que se encaixam na busca, ou seja, possui característica de filtro. No **Pesquisar** normal continuam sendo apresentados todos os registros e o cursor é posicionado na linha encontrada.   
Para “**limpar**” a busca e voltar a visualizar todos os registros basta efetuar uma busca avançada com conteúdo em branco, como mostrado abaixo.   
  
![Pesq05.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047253993)  
  
**A opção “qualquer campo”**  
Ao selecionar a opção de **Pesquisa Avançada** são carregados os campos que compõe chaves de índice e são elegíveis para busca. No entanto, o primeiro campo da lista é um item especial. O item **“qualquer campo**” permite que seja efetuada uma busca no **browse** considerando qualquer coluna (campo). Diferentemente da busca pelos campos normais, essa busca **não filtra** o resultado da pesquisa, mas posiciona o cursor (linha selecionada) ao encontrar um resultado. Nesse aspecto, assemelha-se à **pesquisa normal,** usando chaves de índice.  
 Ao utilizar a pesquisa avançada “**qualquer campo**” podem ser configuradas opções de pesquisa. Para isso deve-se clicar no botão localizado à direita do campo de conteúdo.  
  
![Pesq06.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046393134)  
  
**Para Protheus 12:**  
Para utilizar a**Pesquisa por Coluna (**Pesquisa Avançada), deve-se clicar no ícone em forma de 3 barras ao lado do campo de pesquisa (imagem abaixo), e então clicar em**Coluna**.  
  
![Pesq07.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047254913)  
  
Ao selecionar a opção **Avançada**, ocorre uma alteração na listagem de seleção de ordem de busca. Ao invés de exibir as chaves de índices disponíveis para a tabela, passam a serem exibidos, separadamente, os campos elegíveis para busca. Por razões de desempenho, são exibidos apenas os campos que compõe alguma chave de índice. Isso dá mais alternativas para o banco de dados localizar rapidamente a informação.  
Deve-se selecionar o campo desejado e preencher o campo de Pesquisa. Após o preenchimento deve-se clicar no botão **Pesquisar** (lupa). É possível informar expressões com acento e tanto os itens acentuados quanto os não acentuados serão localizados. Essa pesquisa também vai localizar itens em letras maiúsculas ou minúsculas.  
Tomemos como exemplo o cadastro de municípios, tabela CC2. Efetuaremos uma busca pela expressão “são PAULO”, utilizando para tanto o campo “Município” que contém o nome do município.  
  
![Pesq08.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047255273)  
  
Foram localizados todos os municípios que continham “São Paulo” no nome, independentemente da acentuação e das letras maiúsculas e minúsculas empregadas na busca.

![Pesq09.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047255433)  
  
A **pesquisa avançada** também se diferencia da normal, pois após pesquisar são exibidos apenas os registros que se encaixam na busca, ou seja, possui característica de filtro. No pesquisar normal continuam sendo apresentados todos os registros e o cursor é posicionado na linha encontrada.  
Para “limpar” a busca e voltar a visualizar todos os registros basta efetuar uma busca avançada com conteúdo em branco.  
Para “**limpar**” a busca e voltar a visualizar todos os registros basta efetuar uma busca avançada com conteúdo em branco.  
  
**A opção "Todas as colunas da tabela"**  
Ao selecionar a opção de **pesquisa avançada**, são carregados os campos que compõe chaves de índice e são elegíveis para busca. No entanto, acima dos campos da lista existe um item especial, o item “**Todas as colunas da tabela**”, que permite que seja efetuada uma busca no browse considerando qualquer coluna (campo). Diferentemente da busca pelos campos normais, essa busca não filtra o resultado da pesquisa, mas posiciona o cursor (linha selecionada) ao encontrar um resultado. Nesse aspecto, assemelha-se à pesquisa normal, usando chaves de índice.  
Ao utilizar a pesquisa avançada “**Todas as colunas da tabela**” podem ser configuradas opções de pesquisa. Ao marcar a caixinha “**Todas as colunas da tabela**” fica disponível para habilitar a opção "**A partir desse ponto**". Se marcar essa opção, a busca somente será feita nos registros que estiverem **abaixo** do atual registro selecionado, ignorando os que estiverem acima.  
  
![Pesq10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046394694)  
  
**A opção "Considera Maiúsculas/Minúsculas"**  
Por padrão a **pesquisa avançada** pode ser feita digitando-se maiúsculas ou minúsculas, e qualquer resultado contendo a string será trazido. Se a opção "**Considera Maiúsculas/Minúsculas**" for marcada, apenas o resultado exato, levando-se em consideração o que foi digitado no campo de pesquisa, será retornado.  
  
Veja também: [Campos da pesquisa avançada do browse com asterisco](http://tdn.totvs.com/pages/viewpage.action?pageId=235596076)
