---
content_hash: 119389665fdc6aaf109faf780b2a702b0d6b47e90caa7301eecdf360f9a3b854
fetched_at: '2026-06-29T00:09:34.863998+00:00'
page_id: '425459267'
product: rm
source: tdn-rm
title: 02 - Pesquisa ao Acervo
type: documentation
url: https://tdn.totvs.com/display/LRM/02+-+Pesquisa+ao+Acervo
version: 21
---

Para fazer uma pesquisa no acervo da biblioteca é necessário fazer algumas configurações, que estão descritas a seguir. Estas configurações são feitas no cadastro de parâmetros do sistema.

* Não diferenciar maiúscula/minúscula, acento e cedilha: caso este parâmetro esteja desmarcado, o sistema faz a pesquisa exatamente como foi digitada.
* Retornar exemplares baixados: se este parâmetro estiver marcado, os exemplares com data de baixa definida serão exibidos no resultado da pesquisa.
* Normalizar texto digitado na pesquisa pelo autor: esta opção é utilizada para normalizar o texto digitado antes de realizar a pesquisa. Deve ser marcada somente se a base for normalizada. Dessa forma, o usuário pode digitar o nome do autor de forma direta (nome + sobrenome) e a pesquisa será feita normalmente.
* Número máximo de registros para retorno da pesquisa: define quantos registros serão retornados pela pesquisa. O default é zero, que define um número indeterminado, ou seja, todos os resultados serão exibidos.
* As configurações de campos disponibilizados na pesquisa (**sistema e quiosque**), assim como os campos a serem exibidos no resultado da pesquisa são configurados por usuário. Dessa forma, cada usuário do sistema pode configurar a tela de pesquisa ao seu critério. Essas configurações devem ser definidas no menu "***Parâmetros/Configurações | sub-menu Configurações da pesquisa ao acervo***" (Nova MDI).
* As configurações de campos disponibilizados na pesquisa pelo portal (**pública e privada**), assim como os campos a serem exibidos no resultado da pesquisa são configuradas da mesma forma que a utilizada na pesquisa no sistema porém em outro local, acessando o menu "***Parâmetros/Configurações | sub-menu Parâmetros do sistema | Pesquisa | Pesquisa no portal***" (Nova MDI). A configuração dos campos definidas neste local será para todos os usuários que utilizarem a pesquisa pela Web.
* Os campos que serão disponibilizados para busca são:
  + Assunto
  + Autor
  + Categoria
  + Código auxiliar
  + Classificação
  + Editora
  + Grupo de publicação
  + SBN (Livro)
  + ISSN (Periódico)
  + Local da publicação
  + Subclassificação
  + Título principal
  + Título original
  + Título uniforme
  + Subtítulo
  + Ano
  + Artigo
  + Data de registro
  + Edição
  + Localização do exemplar
  + Número do tombo
  + Coleção
  + Série
  + Palavra chave
  + Notações – Não disponível para Oracle, pois é campo texto
  + Informações – Não disponível para Oracle, pois é campo texto
  + Disciplina Ensino Básico – Somente se tiver integração com o RM Classis Ensino Básico
  + Disciplina Ensino Superior – Somente se tiver integração com o RM Classis Ensino Superior
  + Disciplina Classis Net – Somente se tiver integração com o RM Classis Net
  + Sumário
  + Mês
  + Função do autor
  + Geral: Deve ser a opção padrão caso nenhuma outra seja selecionada como default. Esta opção permite que a pesquisa seja feita em todos os campos textuais da publicação.

  É possível também definir um desses campos como padrão. Desse modo, ao entrar na tela de pesquisa, este campo já estará selecionado.

**Resultado da pesquisa**

* Os campos da publicação e do exemplar que serão exibidos no resultado da pesquisa devem ser parametrizados. Nesta pesquisa, a visualização dos resultados é feita somente no modo **ficha**.

* Campos da publicação disponíveis para visualização ficha:
  + Tipo da Publicação
  + Classificação
  + Subclassificação
  + Coleção
  + Série
  + Volume da Coleção / Série
  + Assuntos . Autores
  + Cutter/PHA
  + Categoria
  + Grupo de publicação
  + Sumário
  + Título
  + Área do Conhecimento
  + Código da publicação
  + Editora
  + Título original
  + Título uniforme
  + Subtítulo
  + Autores/Função
  + Instituição
  + Notas de conteúdo
  + Notas bibliográficas
  + Notas de dissertação
  + Notas gerais
  + Síntese - Resumo/observação
  + Material anexo
  + Arquivo em anexo

* Campos do exemplar disponíveis para visualização ficha:
  + Número do Tombo
  + Tomo
  + Volume
  + Edição
  + Ano
  + Filial
  + Unidade
  + Número de Chamada
  + Número do Exemplar
  + Código auxiliar
  + Data de devolução
  + Código do exemplar
  + Status do exemplar
  + Número de Páginas
  + ISBN
  + Mês
  + Volume/Conteúdo
  + Artigos Periódicos
  + Material anexo
  + Matéria Principal

* A pesquisa pública no portal e quiosque também pode ser parametrizada para as seguintes funcionalidades:

          - Utilizar uma barra de título para exibir um texto definido pelo usuário.  
          - Utilizar uma imagem para apresentação da tela de pesquisa.  
   
**Pesquisa Geral**

* Esta opção de pesquisa deve ser igual para os serviços de consulta pública e privada no portal, além da consulta no quiosque e no sistema.
* Deve disponibilizar as seguintes opções para pesquisa:  
  **1)** Permitir selecionar o campo que deseja utilizar para pesquisa.  
  **2)** Após realizar a pesquisa, na visualização dos resultados, o usuário pode realizar a ordenação do resultado da pesquisa.  
  **3)** Após realizar a pesquisa, na visualização dos resultados, o usuário pode selecionar em quais filiais/unidades a pesquisa será realizada.  
   **4)** Após realizar a pesquisa, na visualização dos resultados, o usuário pode selecionar quais tipos de publicação devem ser considerados na pesquisa.  
   **5)** Após realizar a pesquisa, na visualização dos resultados, o usuário pode selecionar quais coleções/séries devem ser consideradas na pesquisa.  
  **6)** Após realizar a pesquisa, na visualização dos resultados, o usuário pode realizar um filtro pelos autores das publicações encontradas.  
  **7)** Após realizar a pesquisa, na visualização dos resultados, o usuário pode realizar um filtro pelos assuntos das publicações encontradas.  
     
   **Pesquisa Avançada**
* Esta opção de pesquisa deve ser igual para os serviços de consulta pública e privada no portal, além da consulta no quiosque e no sistema.

Além dos itens da pesquisa geral, esta opção de pesquisa deve conter:  
**1)** Possibilidade de filtrar a pesquisa pelo ano da publicação.  
**2)** Possibilidade de filtrar a pesquisa por idioma.  
**3)** Outras opções de filtro, a saber:  
                   \* Contendo: busca todas as publicações/exemplares cujo campo da pesquisa contém o texto digitado. Este texto pode ser uma palavra ou parte de uma palavra.   
                   \* Não contendo: busca todas as publicações/exemplares cujo campo da pesquisa não contém o texto digitado.   
                   \* Começando com: busca todas as publicações/exemplares cujo campo da pesquisa começa com o texto digitado.  
                   \* Pesquisa exata: busca todas as publicações/exemplares cujo campo da pesquisa é exatamente o texto digitado, considerando espaços e caracteres especiais.    
                   \* Pesquisa por palavra: semelhante ao contendo, mas busca a palavra exata e não parte dela.   
**4)** Possibilidade de fazer uma pesquisa composta, também conhecida como pesquisa booleana. Este tipo de pesquisa permite filtrar por vários itens ao mesmo tempo. Por exemplo, é possível filtrar todos os livros com o assunto "direito" do autor "José da Silva". A pesquisa composta possui as seguintes opções:  
         \*\* Adicionar: começa a montar a consulta com a primeira expressão do filtro.  
         \*\* Adicionar E: adiciona outra expressão à consulta. A consulta retornará somente as publicações/exemplares que contemplam todas as condições.   
         \*\* Adicionar OU: adiciona outra expressão à consulta. A consulta retornará as publicações/exemplares que contemplam pelo menos uma das condições.

**Consulta ao Acervo - Detalhes da Publicação**

Na tela de detalhes da publicação da consulta ao acervo, serão informados os detalhes correspondentes à publicação consultada.

Disponibilidade dos Exemplares

A partir das versões 12.1.2402.228 e 12.1.2406.156, a informação referente à quantidade de exemplares existentes em cada unidade bibliotecária foi alterada. Agora serão exibidos os campos:

**Disponíveis no acervo**: mostra a quantidade de exemplares existentes no acervo para cada unidade.

**Disponíveis para empréstimo**: mostra a quantidade de exemplares disponíveis para serem emprestados. **Os exemplares que não possuem o campo "Situação do exemplar" preenchido no [cadastro do exemplar](https://tdn.totvs.com/display/LRM/Exemplar), também podem entrar na contagem dos exemplares disponíveis.**

Estes campos podem ter variação em seus valores, dependendo da configuração dos parâmetros do TOTVS Gestão Bibliotecária.

 Informações complementares

---

[Pesquisa Avançada](http://tdn.totvs.com/x/3v1bGQ)
