---
content_hash: 415b4f9a5f7955e263b6c975800bb03320817b3b6de78fb4f66972206f7f9d7f
fetched_at: '2026-06-29T00:09:34.608697+00:00'
page_id: '425459203'
product: rm
source: tdn-rm
title: Publicações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459203
version: 26
---

O cadastro da publicação é a representação formal do documento existente no acervo da biblioteca. Este impacta nas rotinas de  ,   e catalogação constituindo o eixo central de todas as movimentações da biblioteca. As publicações são cadastradas por coligada.

O sistema possui 36 [Tipo de Publicações](http://tdn.totvs.com/x/1-9bGQ). Para cada tipo, existe um parametrizador que configura os campos obrigatórios, sua ordem e ainda sua visibilidade na pesquisa, estas configurações podem ser realizadas no caminho: Parâmetros do Sistema | 14.01 - Controle do Acervo | 14.01.01 - Publicação | Configuração de Campos.   para acessar o help sobre configuração de campos da publicação.

O cadastro da publicação é dividido nas seguintes categorias:

**Identificação geral**  
Esta categoria é referente aos dados que identificam a publicação e impactam diretamente na organização dos [Exemplares](http://tdn.totvs.com/x/W-5bGQ)da biblioteca além de serem utilizados na pesquisa ao acervo. Os campos disponíveis para serem definidos como visíveis e obrigatórios são: imagem, classificação, subclassificação, categoria, periódico, CUTTER/PHA e tipo de classificação.  Já os campos "Código da publicação", "Tipo da publicação" e "Grupo de Publicação" serão sempre visíveis e obrigatórios.

* O preenchimento do campo de classificação é realizado com base no padrão de classificação utilizado pela   (CDD, CDU, entre outros). Este campo tem impacto direto na geração do número de localização de exemplares.
* É possível gerar o código CUTTER/PHA da publicação ao clicar no botão do campo CUTTER / PHA quando existe, pelo menos, um autor cadastrado e com função de autor principal.
* Em tipo de classificação define qual forma de classificação será utilizada: CDD, CDU ou outras. Uma classificação padrão pode ser informada no menu de parâmetros do sistema.

Caso o parâmetro Utilizar área conhecimento integrada com CDU/CDD esteja habilitado, a classificação e subclassificação serão geradas automaticamente, no momento em que forem inseridas uma área e uma subárea do conhecimento para a publicação. Caso esteja desabilitado, tais campos serão editáveis para informar os códigos manualmente.

**Títulos**  
Esta categoria é referente aos dados que denominam a publicação e impactam na movimentação, reserva e pesquisa ao acervo. Os campos disponíveis para serem definidos como visíveis e obrigatórios são: título principal, título original, título equivalente, título uniforme e subtítulo.  
O campo "Frase que representa publicação sem título" estará sempre visível e obrigatório caso a publicação não tenha título principal.

Título equivalente

O campo título equivalente segundo a regra NBR 6023:2018 é geralmente preenchido em idioma diferente do título principal, neste caso, sempre que ele estiver preenchido, mesmo que no mesmo idioma da publicação, será exibido na referência bibliográfica logo após o título principal separado pelo sinal de ' = '.

Exemplo: SANTOS, Maria. Gestão da inovação = Innovation management. São Paulo: Atlas, 2021.

**Publicação/Distribuição**

Esta categoria é referente as informações de edição e distribuição da publicação. Os campos disponíveis para serem definidos como visíveis são: local, editora, ano, idioma, país, estado e edição. Ao incluir/editar uma publicação é possível vincular uma editora através de suas remissivas.

**Detalhes específicos**

Permite que sejam configurados campos que são exclusivos para cada tipo de publicação. Esta categoria possui uma quantidade elevada de campos que visam oferecer um cadastro mais detalhado e personalizado para tipo de publicação.

Exemplo:

Para uma publicação do tipo Livro é interessante saber se este é ilustrado ou não, ao passo que, para uma publicação que seja do tipo Mapa, é sabido que todo mapa é ilustrado, portanto, este campo seria dispensável para este último, sendo necessário, por exemplo, ter o campo de dimensão e escala. Assim como o campo trilha sonora é interessante para as publicações do tipo DVD, elas não são usuais para o tipo Transparência.

**Descrição Física**

Esta categoria é referente aos dados da caracterização física da publicação. Os campos disponíveis para serem definidos como visíveis e obrigatórios são: descrição física, número de páginas, número de folhas, material anexo e material.  
  
 **Série**

Esta categoria permite informar a qual Coleção/Série a publicação está vinculada. Os campos disponíveis para serem definidos como visíveis e obrigatórios são: Coleção/Série e Volumes da Coleção/Série.

**Notas**  
Categoria especifica para anotações gerais sobre a publicação. Os campos disponíveis para serem definidos como visíveis e obrigatórios são: notas de dissertação, notas gerais, notas de conteúdo, notas bibliográficas, síntese, resumo/observação e informações adicionais. As notas da publicação são visualizadas através da ficha catalográfica do exemplar.

**Número normalizado**

Esta categoria identifica o número normalizado da publicação. Pode-se configurar o uso dos campos ISBN e ISSN.

O ISBN - International Standard Book Number - é um sistema que identifica numericamente os livros segundo o título, o autor, o país e a editora, individualizando-os inclusive por edição. O ISSN (International Standard Serial Number), sigla em inglês para Número Internacional Normalizado para Publicações Seriadas, é o código aceito internacionalmente para individualizar o título de uma publicação seriada. O ISSN é composto por oito dígitos distribuídos em dois grupos de quatro dígitos cada, ligados por hífen e precedido sempre por um espaço e a sigla ISSN.

**Controle Interno**

Esta categoria é responsável por armazenar registros das inclusões e alterações realizadas no cadastro da publicação. Ela irá conter os seguintes campos: produtos, usuário responsável pela inclusão, usuário responsável pela última alteração, data/hora da inclusão e data/hora da alteração. Os campos citados serão sempre obrigatórios, mas poderão ser definidos como visíveis ou não.

Observação:  O campo produto é utilizado para informar o produto do RM Nucleus ao qual se refere e para o qual será criada uma solicitação de compra, quando estiver parametrizado a integração com o RM Nucleus. Não será permitido informar o mesmo produto para publicações diferentes e quando a publicação possuir pelo menos um exemplar originado da integração, o produto não poderá ser alterado.

**Outras informações**

Nesta categoria permite cadastrar/visualizar informações complementares referente a publicação. Os campos disponíveis para serem definidos como visíveis e obrigatórios são: analítica de livro, idiomas de áudio/Legenda, arquivo digital anexo,   ,  ,  ,  ,   e Autores/Função. Existem também os seguintes campos que são utilizados para publicações do tipo periódico:

* **Ordem de leitura:**Nesta aba, é possível definir uma ordem(fila) que determina a prioridade de cada usuário para ler os periódicos recebidos das assinaturas cadastradas da publicação;
* **Assinatura:**A partir desta aba, é possível cadastrar assinaturas de periódicos, informando o período da assinatura, a periodicidade de recebimento dos periódicos, a data provável de recebimento destes, o número de exemplares a serem recebidos e a data provável de recebimento do primeiro exemplar. Quando os periódicos são gerados dentro do cadastro da assinatura, é possível controlar o recebimento de cada um, através da manipulação de seus status. Para efetuar o recebimento dos exemplares devemos executar o processo "Receber exemplar" que está localizado em Processos do cadastro da Publicação. Exemplo: Efetuando o recebimento de um exemplar Em Assinaturas de periódicos selecione a assinatura que desejar, posteriormente clique no botão "Carregar periódicos", será listado todos os exemplares corresponde a assinatura Selecionada, marque o exemplar que será recebido e clique no botão Executar. Ao acessar Anexos\Exemplares serão listados todos os exemplares da publicação. Poderá também ser associado um exemplar já existente ao periódico, selecionando um exemplar sem vínculo no registro. Se o exemplar não for selecionado, o processo irá gerar um novo exemplar para o periódico.
  + **Observação 1:** O processo de "Receber exemplar" só irá funcionar para as publicações do tipo periódico.
  + **Observação 2:** Na versão 12.1.23 em diante, foi disponibilizado um processo chamado "Alterar periódicos recebidos" que permite alterar a situação de um periódico recebido (para mais informações ).
* **Cadastro coletivo nacional (CNN):** Nesta aba, é possível identificar cada periódico no CCN, informando seu código de identificação, além da situação da publicação e o ano de encerramento desta;

Informações Complementares

---

[Número de exemplares cadastrados por tipo de publicação](http://tdn.totvs.com/x/Xf5bGQ)

 

 

[Autores](http://tdn.totvs.com/x/jP5bGQ)

[Exemplares](http://tdn.totvs.com/x/W-5bGQ)

[Referências Bibliográficas](http://tdn.totvs.com/x/x-9bGQ)

[Fornecedores](http://tdn.totvs.com/x/UP5bGQ)

 

[Volume](http://tdn.totvs.com/x/k-9bGQ)

 

[Exportação de dados de periódicos para o CNN](http://tdn.totvs.com/x/YP5bGQ)

[Importação padrão MARC21](http://tdn.totvs.com/x/Ev5bGQ)

Como Fazer

---

 

 

 

   
   
 

Veja Também

---

[Periódicos - Assinaturas](http://totvsconnect.blogspot.com/2010/03/totvs-gestao-bibliotecaria-periodicos) 

[Periódicos – Artigos por Exemplar](http://totvsconnect.blogspot.com/2010/02/totvs-gestao-bibliotecaria-periodicos)
