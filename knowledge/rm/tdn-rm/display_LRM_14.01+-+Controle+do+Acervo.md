---
content_hash: a1dffc9a2c1bc565a28b3d31e0c511f0b86a928cf7fd424ecfd6f14324b7b9ad
fetched_at: '2026-06-29T00:09:34.554040+00:00'
page_id: '425459185'
product: rm
source: tdn-rm
title: 14.01 - Controle do Acervo
type: documentation
url: https://tdn.totvs.com/display/LRM/14.01+-+Controle+do+Acervo
version: 9
---

**14.01.01 - Publicação**

O objetivo desta etapa é definir as características do cadastro de publicações.  
   
**Tipo de classificação da publicação:** Este parâmetro define qual o tipo de classificação que será utilizado ao incluir uma nova publicação: CDD, CDU ou outra.  
   
**Tipo de referência ao autor:** Este parâmetro define qual o tipo de referência ao autor que será utilizado para a geração do código **CUTTER/PHA** no cadastro de publicações. Se será CUTTER, PHA ou Livre.  
   
**Valor default para máscara de volume:** Este parâmetro define a máscara padrão para geração automática de volumes da publicação. É obrigatória a informação da sequência **<%n>** na máscara de volume.  
   
**Exemplo**  
   
Supondo que a máscara informada no parâmetro é **Vol. <%n>** e que se queira gerar 3 volumes. Ao executar o processo gerar volume, localizado no cadastro de publicações, os 3 volumes gerados serão:  
   
Vol. 1  
Vol. 2  
Vol. 3  
   
**Número de dias a ser verificado as últimas aquisições no portal:** Define o número dias a ser visualizado no portal das publicações adquiridas pela biblioteca. Por exemplo, se o parâmetro estiver marcado 5 dias, no portal devem ser exibidas todas as publicações cadastradas até 5 dias atrás.  
   
**Cadastrar em maiúsculo título da publicação:** Este parâmetro define que ao incluir uma nova publicação, seu título principal será cadastrado em maiúsculo.  
   
**Utilizar área do conhecimento integrada com CDU/CDD:** Este parâmetro define que ao incluir uma nova área do conhecimento, a classificação da publicação será preenchida com o código da área. Caso seja incluída uma subárea do conhecimento, a subclassificação da publicação será preenchida com o código da subárea.  
Quando este parâmetro está habilitado, os campos Classificação e Subclassificação da publicação não ficarão editáveis.  
   
**Permitir cadastro duplicado de publicações (com mesmo título principal, autores, editora e subtítulo):** Este parâmetro define que o sistema permitirá o cadastro de publicações diferentes com o mesmo título principal, autores, editora e sub-título).  
   
**Bloquear inclusão de assuntos da publicação com remissiva de mesmo nome:** Este parâmetro define que o sistema não permitirá a inclusão de assuntos em uma publicação, cuja descrição do assunto seja igual à de uma remissiva já cadastrada no sistema.  
   
**Mostrar apenas fornecedores da publicação:** Este parâmetro define que no cadastro de exemplares, somente serão apresentados os fornecedores ou ambos (clientes e fornecedores) da publicação.  
   
**Considerar a ordenação por categoria na configuração de campos do resultado da pesquisa:** Este parâmetro permite determinar se os campos do resultado da pesquisa em configurações de campos serão ordenados por categorias.  
    
 **Publicação - Configuração de campos**  
    
Através desse processo é possível parametrizar por tipo de publicação os campos do cadastro da publicação e o resultado da pesquisa ao acervo.  
Ao selecionar o tipo de publicação é possível definir a visibilidade, obrigatoriedade e ordem dos campos das seguintes categorias:  
Identificação geral, Título, Publicação/Distribuição, Detalhes específicos, Descrição física, Série, Notas, Número normalizado, Controle interno e Informações adicionais. Além de configurar também a visibilidade, obrigatoriedade e a ordem das categorias de campos serão apresentadas na tela de cadastro de publicações.  
   
**Observação**

* Os campos Código da publicação, Tipo da publicação e Grupo de publicação são sempre visíveis e de preenchimento obrigatório, enquanto o campo Periódico é sempre visível.
* O campo Frase que representa a publicação sem título será sempre visível e de preenchimento obrigatório caso o campo Título principal não esteja configurado para preenchimento obrigatório e também não seja preenchido no cadastro da publicação.
* Os campos de controle interno Usuário responsável pela inclusão, Usuário responsável pela última alteração, Data/hora da inclusão e Data/hora da alteração serão sempre de preenchimento obrigatório, pois o sistema se encarregará de preenchê-los automaticamente de acordo com o evento ocorrido (novo cadastro ou alteração de um cadastro já existente).
* As categorias Identificação geral e Título serão sempre visíveis, pois são categorias de campos cujo preenchimento é sempre obrigatório.

**14.01.02 - Exemplar**  
    
O objetivo desta etapa é definir as características do cadastro do exemplar.  
   
**Número do tombo**  
   
**Utilizar número do tombo por tipo de publicação:** Este parâmetro define que o cálculo automático do número do tombo será realizado por tipo de publicação, da seguinte forma: (Código do tipo de publicação do exemplar) juntamente com (Número sequencial de números do tombo gerados para o tipo de publicação).  
   
**Utilizar número do tombo global:** Este parâmetro define que o número do tombo seja gerado de forma global, ou seja por coligada.  
   
**Exemplo**  
   
Supondo que o código do tipo de publicação **Livro** é 1 e o do tipo **Periódico** é 4 e que o último número do tombo cadastrado para livros é 12 e para periódicos é 43. Supondo ainda que o último número do tombo cadastrado de forma global (sem considerar o tipo de publicação) é 50.  
Caso o parâmetro esteja habilitado, ao informar um número do tombo para um exemplar de uma publicação do tipo **Livro**, o número gerado será **13**. Para o tipo **Periódico** será 44.  
Caso o parâmetro esteja desabilitado, em qualquer uma das situações, o número gerado será **51**, pois não será considerado o tipo de publicação, e sim o último número do tombo gerado de forma global.  
   
**Importante:** Quando o parâmetro "Utilizar número do tombo por tipo de publicação" ou "Utilizar número do tombo global" não estão habilitados, o número do tombo é gerado por unidade bibliotecária.  
   
**Preenchimento obrigatório:**Permite configurar por tipo de publicação se o número do tombo será obrigatório ao incluir exemplares.  
   
**Default para máscara de exemplar:** Este parâmetro define a máscara padrão para geração automática de exemplares da publicação. É obrigatória a informação da sequência **<%n>** na máscara de exemplares.  
   
Exemplo  
   
Supondo que a máscara informada no parâmetro é **Ex. <%n>** e que se queira gerar 3 exemplares.  
Ao executar o processo Cadastro rápido de exemplares, localizado no cadastro de publicações, os 3 exemplares gerados serão:  
   
Ex. 1  
Ex. 2  
Ex. 3  
   
**Utilizar código auxiliar como campo chave:** Este parâmetro define a obrigatoriedade de preenchimento do campo Código auxiliar no cadastro de exemplares.  
   
**Gerar automaticamente o controle de leitura ao receber novo periódico:** Este parâmetro define que ao receber um novo periódico, o sistema irá gerar a fila de reservas desse, de acordo com a ordem de leitura cadastrada na assinatura que contém o periódico.  
   
**Exibir mensagem de alerta para duplicação do campo nº exemplar:** Este parâmetro define que ao informar um número de exemplar já existente na publicação, o sistema apresenta uma mensagem informando a duplicação do número do exemplar.

**Criar exemplar com o campo 'Número de chamada (Localização)' preenchido com o Cutter/Pha da publicação:** Este parâmetro define que ao criar um exemplar, o campo "Localização" será automaticamente preenchido com o Cutter/Pha da publicação, se estiver preenchido na publicação.

Informação

Este parâmetro está disponível para as versões 12.1.25.269, 12.1.26.214, 12.1.27.165 e 12.1.28.102, para versões anteriores, o comportamento do sistema já é preencher o campo Localização com o Cutter/Pha da publicação caso esteja preenchido.

   
**Preencher novo exemplar com situação default:** Define que ao incluir um novo exemplar o campo situação do exemplar do cadastro de exemplar será preenchido com situação informada em situação default do exemplar.  
   
  
**14.01.03 - Cadastros auxiliares**  
   
O objetivo desta etapa é definir as características gerais dos cadastros auxiliares do sistema, que são utilizados pelos demais processos.  
   
**Permitir Duplicação de Entidades:** Este parâmetro define quais entidades (Assuntos, Autores, Coleção/Série, Editora, Idioma, Local da publicação, Categoria) poderão ter registros com descrição duplicada no sistema.  
   
**Bloquear inclusão quando houver remissiva de mesmo nome:** Este parâmetro define quais cadastros (Assuntos, Autores, Editoras) o sistema irá bloquear a inclusão de entidades quando a descrição delas for igual a de alguma remissiva cadastrada no sistema.  
   
**Cadastrar em maiúsculo:** Este parâmetro define quais descrições de entidades (Categoria, Assunto, Grupo de publicação, Nome do autor) serão cadastradas em maiúsculo, após sua inclusão.  
   
**Normalizar nome do autor ao incluir registro:** Este parâmetro define que os nomes dos autores incluídos, serão cadastrados na forma normalizada.  
   
**Exemplo**  
   
Supondo que se queira cadastrar um autor com o nome **Machado de Assis**. Ao salvar o cadastro o nome do autor será normalizado da seguinte forma: **ASSIS, Machado de**
