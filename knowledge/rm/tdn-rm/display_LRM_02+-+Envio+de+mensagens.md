---
content_hash: a0d466e175f870cd72b2808fa7a42fffc3378fee9c09e9f6f38d9340e436cc19
fetched_at: '2026-06-29T00:12:03.367384+00:00'
page_id: '906848019'
product: rm
source: tdn-rm
title: 02 - Envio de mensagens
type: documentation
url: https://tdn.totvs.com/display/LRM/02+-+Envio+de+mensagens
version: 150
---

# Sumário

Sumário

# Objetivo

---

O envio de mensagens tem como objetivo permitir que o usuário realize a comunicação com diferentes públicos por meio de e-mails ou do aplicativo **eduCONNECT**.   
É possível enviar mensagens para diversos grupos, como alunos, pais, responsáveis acadêmicos e financeiros, coordenadores e professores.

Informações Importantes

* Para acessar a funcionalidade de envio de mensagens, o usuário deve estar associado a uma [**Regra de Comunicação**](https://tdn.totvs.com/pages/viewpage.action?pageId=898441783) ou a um perfil que esteja vinculado a uma regra de comunicação.
* A **[Regra de Comunicação](https://tdn.totvs.com/pages/viewpage.action?pageId=898441783)** associada deve possuir a opção **"Texto Livre"** configurada no campo **"Tipo de mensagens permitidas"**.
Configuração de Acesso ao Menu da Central de Comunicação

Para que o menu da Central de Comunicação seja exibido no Portal Gestão Educacional, é necessário acessar o **Cadastro de Perfis** e conceder a permissão correspondente.

Somente os usuários autorizados terão acesso ao menu e à tela de envio de mensagens.

**Processo Guiado**

A tela do envio de mensagens será organizada em etapas sequenciais, representadas por **steps**. O usuário deverá preencher as informações de cada etapa e clicar no botão **"Avançar"** para prosseguir até a etapa final, onde a mensagem será enviada.

O botão **"Avançar"** ficará habilitado somente quando todas as opções obrigatórias da etapa atual forem preenchidas corretamente.

Exemplo:

Mudança na ordem dos passos de criação de mensagem

A partir da versão 12.1.2602 o passo de publico alvo passa a ser o primeiro passo para a criação de mensagems

As versões posteriores  ficaram com seguinte formato:

# Mensagens

---

Nesta etapa, o usuário deverá preencher todas as informações que irão compor a mensagem, incluindo:

* **Assunto:** Título ou tema da mensagem.

Ao utilizar a opção 'Meu eduCONNECT', atenção ao inserir tag no campo **assunto**, pois o campo é limitado a **100 caracteres**. O conteúdo da tag também conta para esse limite.

* **Mensagem:** O campo de mensagem permite que você insira o conteúdo principal do e-mail. Ele oferece dois modos de edição: Modo Básico e Modo Avançado.
* Na parte inferior do campo de mensagem, será exibido um **contador de caracteres**, indicando a quantidade atual de caracteres digitados. Esse contador é válido tanto para o Modo Básico quanto para o Modo Avançado de edição.

* O envio de imagens no corpo da mensagem para o Meu eduCONNECT está disponível apenas no modo avançado(HTML), para mais informações .
* Quando o Meu eduCONNECT estiver habilitado, ao inserir uma imagem no campo **Editor de mensagem**, a imagem será removida e uma notificação será exibida na tela.

* Ao marcar a opção Para Meu eduCONNECT o íconenão será mais exibido
* Ao utilizar a opção "Meu eduCONNECT", será exibido o **contador de caracteres**, indicando a **quantidade atual** e o **limite máximo permitido de 4.000** caracteres. Caso o texto ultrapasse esse limite, o texto ficará vermelho, e o botão "Avançar" ficará desabilitado até que a quantidade de caracteres seja ajustada para o valor máximo permitido (4.000).
* **Atenção ao utilizar o editor de texto e formatações**: O editor de mensagens utiliza códigos de estrutura que ficam totalmente ocultos na tela. Esses códigos invisíveis — que são gerados ao aplicar formatações (como negrito, cores e quebras de linha) ou em ações diárias como **copiar e colar textos de outras fontes** — também consomem espaço e são contabilizados pelo sistema.  
  Por esse motivo, em algumas situações, o **limite de 4.000** caracteres pode ser atingido muito antes do esperado, mesmo que o texto visível na tela pareça pequeno. Caso o contador fique vermelho repentinamente, recomendamos limpar a formatação do texto ou digitá-lo diretamente no campo.

* **Anexo:** Arquivos adicionais que poderão ser incluídos, se necessário.
* **Outras Informações Complementares:** Configurações ou detalhes adicionais relevantes ao envio.

Certifique-se de que todas as informações estejam devidamente preenchidas antes de prosseguir para a próxima etapa.

A opção "Para o Meu eduCONNECT"  ficará habilitada somente quando a instituição possuir integração com o Meu eduCONNECT e também a regra de comunicação permitir a utilização desta opção.

Utilização de TAGs na Mensagem

Durante a criação da mensagem, é possível utilizar **TAGs de informações dinâmicas**, que serão substituídas automaticamente durante o envio. Por exemplo, ao inserir a TAG **[NOMERESPONSAVEL]**, ela será substituída pelo nome do responsável do aluno no momento do envio.

Como Utilizar as TAGs:

* Para visualizar as TAGs disponíveis, basta começar a digitar o caractere **"["**. Uma lista com todas as opções será exibida.

* As TAGs podem ser utilizadas tanto no **assunto** quanto no **corpo da mensagem**.
* À medida que o texto correspondente à tag for digitado, o sistema exibirá apenas as tags compatíveis com o que foi inserido.
* A seleção das TAGs deve ser feita clicando com o mouse sobre a tag desejada ou pode se usar as setas do teclado e a tecla Enter para selecionar a Tag.

Essa funcionalidade permite personalizar as mensagens de forma prática e eficiente, garantindo uma comunicação mais direcionada.

Anexo

Para que a funcionalidade de anexar arquivos fique habilitada, o **RM** deve estar devidamente configurado com:

* As **extensões de arquivos permitidas**.
* O **tamanho máximo total** para os anexos.

Para anexar um arquivo, clique na opção 'Selecionar arquivos' e carregue o arquivo desejado.

Regra do Tamanho Máximo Total para Anexos

A configuração do **tamanho máximo total para anexos** define o limite em **kilobytes (KB)** que todos os arquivos anexados, somados, podem atingir.

**Como funciona?**

Você pode anexar a **quantidade de arquivos que desejar**, desde que o tamanho total combinado de todos os anexos não ultrapasse o limite configurado no sistema.

**Exemplo:**

* **Tamanho máximo configurado:** 10.000 KB (10 MB).
* Arquivos anexados:
  + Arquivo 1: 3.000 KB.
  + Arquivo 2: 4.000 KB.
  + Arquivo 3: 2.500 KB.

**Total:** 9.500 KB.

Nesse caso, os anexos são permitidos porque o total (9.500 KB) é menor que o limite configurado (10.000 KB).

Se você tentar adicionar um quarto arquivo que eleve o total para mais de 10.000 KB, o sistema não permitirá o envio até que o total fique dentro do limite estabelecido.

Caso essas configurações não estejam definidas, será exibida uma mensagem de aviso ao usuário, como no exemplo abaixo:



Essa configuração é essencial para garantir o correto funcionamento do envio de mensagens com anexos.

* Para configurar as informações acesse os parâmetros do Educacional seguindo **RM Portal > Portal Gestão Educacional > Central de Comunicação**
Modo de edição

**Modo Básico (Texto)**  
No Modo Básico, você pode criar e formatar o conteúdo do e-mail de forma intuitiva, utilizando ferramentas de edição que permitem adicionar formatações como negrito, itálico, listas, links e muito mais. Esse modo é ideal para usuários que desejam criar mensagens de forma rápida e sem necessidade de conhecimentos técnicos.

**Modo Avançado (HTML)**

O Modo Avançado é destinado a usuários que possuem familiaridade com HTML. Neste modo, você pode digitar ou colar diretamente o código HTML que será utilizado como corpo da mensagem.

Aviso

Ao utilizar o Modo Avançado, é importante que você saiba exatamente o que está fazendo. O sistema não valida ou garante que o HTML inserido será renderizado corretamente em todos os clientes de e-mail. Dependendo do código utilizado, o layout e a exibição do e-mail podem variar significativamente entre diferentes provedores de e-mail (como Gmail, Outlook, etc.). Portanto, recomendamos que esse modo seja utilizado apenas por quem possui conhecimento técnico em HTML e entende as limitações de renderização em e-mails.

Pré-visualização

A pré-visualização permite que você veja como sua mensagem ficará antes de ser enviada, de acordo com o(s) método(s) de envio escolhidos. Para ativá-la, selecione 'Como deseja enviar sua mensagem?' e preencha os campos 'Assunto' e 'Corpo da mensagem'.

Quando as opções **Por e-mail** e para o **Meu eduCONNECT** estiverem marcadas, será aberto um modal com a possibilidade de visualizar ambas as opções:

Ao clicar no botão pré visualização, será exibido um modal contendo o preview da mensagem conforme o print abaixo:

Pré-visualização **Meu eduCONNECT**:

Aviso

A pré-visualização não garante que o e-mail será exibido exatamente como visto, pois a renderização varia entre clientes de e-mail (como Gmail, Outlook, etc.). O layout pode mudar dependendo do cliente de e-mail que receberá a mensagem.

Detalhes do Meu eduCONNECT

Seleção da imagem que será apresentada como destaque na mensagem enviada para o Meu eduCONNECT

**Importante:**

* O sistema **aceita apenas arquivos nos formatos PNG e JPG**.
* O tamanho máximo permitido para cada arquivo é **100KB**. Dimensão sugerida da imagem 750x320px.
Histórico de Envios de E-mail

É possível parametrizar o **RM** para manter o **histórico de envios de e-mails** e seus respectivos anexos.

Para mais informações, clique [aqui](https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM#EnviodeemailLINHARM-Configura%C3%A7%C3%A3odateladeenviodee-mails:).

Envio de e-mails por pacotes

É possível parametrizar no **RM** o envio de e-mails em lotes utilizando a mesma conexão SMTP, reduzindo a sobrecarga causada pela reabertura da conexão a cada mensagem enviada.  
Essa opção pode melhorar o desempenho em ambientes com alto volume de envios.

Para mais informações, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=1021200817).

# Assistente de IA TOTVS

---

**Em breve novidade!!!** A partir da versão **12.1.2606**, será disponibilizado o **Assistente de IA TOTVS**. Crie, revise e aprimore seus comunicados com inteligência artificial de forma instantânea. [**[Confira todos os detalhes aqui!](https://tdn.totvs.com/pages/viewpage.action?pageId=1061173574)**]"

# Enquete

---

A partir da versão **12.1.2602**, os usuários já podem utilizar o recurso de enquetes.

A opção **“Enquete”** permite ao usuário criar e enviar mensagens no formato de votação, oferecendo aos destinatários a possibilidade de escolher entre alternativas previamente definidas.

A opção **“Enquete”** somente estará disponível quando a regra de comunicação vinculada ao usuário permitir o envio desse tipo de mensagem. Quando habilitada, o usuário poderá configurar perguntas e opções de resposta, visualizar um preview de como a enquete será exibida e enviá-la aos públicos autorizados.

Exemplo da tela do cadastro da regra de comunicação:

Mensagens do tipo *Enquete* só podem ser enviadas pelo **Meu eduCONNECT**. Por isso, ao selecionar esse tipo de mensagem, a opção **“Por e-mail”** será automaticamente desabilitada.

Além disso, caso a regra de comunicação do usuário permita **apenas** o tipo *Enquete*, as opções **“Meu eduCONNECT”** e **“Enquete”** já serão exibidas **marcadas e desabilitadas**.

Ao marcar a opção **“Enquete”**, a aba **“Opções da Enquete”** será habilitada. Nessa aba será possível adicionar as alternativas de votação que comporão a enquete. Lembre-se de que são necessárias, no mínimo, duas opções para prosseguir com o envio da mensagem.

Existe uma limitação na quantidade total de caracteres que compõem todas as opções de votação. Essa quantidade máxima varia de acordo com o número de opções adicionadas.  
Como facilitador, foi incluído um rotulo informativo exibindo a quantidade de caracteres ainda disponível.

Por meio da opção **“Pré-visualizar”**, será possível visualizar, de forma simulada, como a enquete será apresentada no aplicativo.

# Público-alvo

---

Nesta etapa, deve-se identificar o **público-alvo** das mensagens, ou seja, quais **papéis** (alunos, pais, responsáveis, coordenadores, professores, etc.) irão receber a mensagem.

Além disso, é nesse momento que são configurados os **filtros** para determinar os usuários específicos que receberão a mensagem. Esses filtros permitem segmentar o público com base em critérios previamente estabelecidos.

É importante ressaltar que as opções de público-alvo apresentadas serão habilitadas de acordo com as permissões definidas nas [regras de comunicação](https://tdn.totvs.com/pages/viewpage.action?pageId=898441783).

#### **Filtro Predefinido**

São consultas SQL previamente cadastradas no RM, que retornam um conjunto específico de usuários que receberão a mensagem.  
Ao marcar essa opção, será habilitado um campo para que o usuário selecione o(s) filtro(s) predefinido(s) que deseja utilizar.

Filtro predefinido

Para mais informações sobre como habilitar e disponibilizar os filtros, consulte a documentação das [regras de comunicação](https://tdn.totvs.com/pages/viewpage.action?pageId=898441783#id-01Regrasdecomunica%C3%A7%C3%A3o-Regradecomunica%C3%A7%C3%A3o)

Os **filtros predefinidos** são consultas SQL previamente cadastradas no RM, que retornam um conjunto de usuários que receberão a mensagem enviada.

Principais Funcionalidades

* É possível selecionar **um ou vários filtros** para a mensagem.
* Caso seja um filtro **que não exige parâmetros**, o sistema adiciona-o com um ícone verde na frente, permitindo que o usuário prossiga com o envio da mensagem.
  + O filtro com parâmetros só pode ser **adicionado uma única** vez aos filtros da mensagem.
* Caso seja um filtro **que exige parâmetros,** será exibida uma tela para que os valores necessários sejam informados antes de aplicar o filtro.  
  + Caso os valores necessários não sejam informados, o filtro será adicionado com um ícone amarelo indicando que o filtro requer parametrização, impedindo que o usuário prossiga com o envio da mensagem.
  + O valor pode ser adicionado editando o filtro.
  + O filtro com parâmetros pode ser **adicionado várias vezes** aos filtros da mensagem.
* Caso o filtro apresente algum erro ao selecionar, somente ele será mostrado a mensagem "Ocorreu um erro ao carregar o filtro predefinido:", na parte inferior da tela e o filtro não será adicionado.

* Em caso de uma seleção **de múltiplos filtros.**
  + O filtro **que não exige parâmetros** é exibido com o indicado verde mostrado anteriormente.
  + O filtro **que exige parâmetros,**não carrega a tela para adicionar os valores exigidos, assim que é incluído. Nesse caso é necessário editar o filtro, clicando no ícone de lápis, para adicionar os valores necessários.
  + Caso seja **adicionado algum filtro com erro,** ele será adicionado com um ícone vermelho indicando que o filtro deve ser removido para poder prosseguir.
  + Só será possível prosseguir com o envio da mensagem removendo os filtros com erro, caso exista algum, e todos os filtros estejam com o ícone verde indicado nas imagens acima.
* Apó1836pxs adicionar o filtro, o sistema permite **visualizar o resultado** correspondente.

**Importante:**  
Todas as consultas SQL cadastradas e disponibilizadas para uso na Central de Comunicação devem obrigatoriamente retornar as seguintes colunas:

* `CODUSUARIO`
* `EMAIL`
* `CODCOLIGADA`
* `CODTIPOCURSO`
* `CODFILIAL`

**Exemplos**:

#Consulta SQL Com Parâmetro#

select  P.NOME, P.EMAIL, P.CODIGO, P.CODUSUARIO, A.RA, HF.CODFILIAL, HF.CODCOLIGADA, HF.CODTIPOCURSO   
from SALUNO A   
INNER JOIN PPESSOA P ON P.CODIGO = A.CODPESSOA   
INNER JOIN SMATRICPL MPL ON MPL.RA = A.RA    
INNER JOIN SHABILITACAOFILIAL HF ON MPL.IDHABILITACAOFILIAL = HF.IDHABILITACAOFILIAL WHERE A.RA = :RA AND HF.CODCOLIGADA = :CODCOLIGADA

#Consulta SQL Sem Parâmetro#  
select top 20 P.NOME, p.EMAIL, P.CODIGO, P.CODUSUARIO, A.RA  
from SALUNO A   
INNER JOIN PPESSOA P ON P.CODIGO = A.CODPESSOA

#Consulta SQL Defeito#

select top 20 P.NOME, p.EMAIL, P.CODIGO, P.CODUSUARIO, A.RA,  
from SALUNO A   
INNER JOIN PPESSOA P ON P.CODIGO = A.CODPESSOA

Caso a opção **"Meu eduCONNECT"** esteja marcada, será necessário também retornar a coluna:

* `IDCATEGORIA`

Essas informações são essenciais para que o sistema aplique corretamente as parametrizações baseadas no contexto. Além disso, a coluna `IDCATEGORIA` é necessária para identificar a categoria do destinatário nas mensagens enviadas para o **Meu eduCONNECT**.

**Exemplo**:

select P.NOME, p.EMAIL,P.CODIGO,P.CODUSUARIO,A.RA,HF.CODFILIAL,HF.CODCOLIGADA,HF.CODTIPOCURSO,SCT.IDCATEGORIA  
from SALUNO A  
INNER JOIN PPESSOA P ON P.CODIGO = A.CODPESSOA  
INNER JOIN SMATRICPL MPL ON MPL.RA = A.RA   
INNER JOIN SHABILITACAOFILIAL HF ON MPL.IDHABILITACAOFILIAL = HF.IDHABILITACAOFILIAL  
INNER JOIN SCATEGORIANOTIFICACAO SCT ON SCT.CODCOLIGADA = HF.CODCOLIGADA AND   
SCT.CODFILIAL = HF.CODFILIAL AND  
SCT.CODTIPOCURSO = HF.CODTIPOCURSO  
WHERE A.RA = :RA AND SCT.NOMECATEGORIA = :NOMECATEGORIA

Observações Importantes

* Fique atento ao resultado dos filtros, pois eles podem retornar um **volume elevado de dados**.
* Em casos de resultados muito grandes, o processamento pode levar algum tempo para ser concluído.

**Exemplos (GIFs):**

* Adicionando um filtro predefinido **sem parâmetro**.

* Adicionando um filtro predefinido **com parâmetro**.

* Adicionando múltiplos filtros simultaneamente.

#### **Filtro Avançado**

Para os demais públicos-alvo, será disponibilizado o recurso de **filtro avançado**, que permite a seleção de um conjunto de filtros personalizados para determinar quem receberá a mensagem.

Filtro (avançado) 

O envio de mensagens permite segmentar o público-alvo por meio de filtros, garantindo que a comunicação seja direcionada às pessoas corretas. Os filtros são exibidos de forma encadeada, facilitando a seleção das informações. Por exemplo, ao selecionar um período letivo, serão exibidos apenas os períodos ativos relacionados à coligada, filial ou nível de ensino escolhidos anteriormente.  
Caso nenhuma dessas opções tenha sido previamente definida, o sistema listará todos os períodos letivos ativos disponíveis, respeitando as permissões de contexto ou com os **[filtros definidos na regra de comunicação](https://tdn.totvs.com/pages/viewpage.action?pageId=898441783#id-01Regrasdecomunica%C3%A7%C3%A3o-Regradecomunica%C3%A7%C3%A3o)**.

**Importante:**

Caso os filtros estejam habilitados, será **obrigatório** o preenchimento do **período letivo** para prosseguir para a próxima etapa.

Ressaltamos a importância de conferir e definir adequadamente os filtros selecionados, para garantir que as mensagens sejam enviadas corretamente aos destinatários. Por exemplo, se for selecionado apenas o **período letivo** e o **público-alvo** for **alunos** e **responsáveis**, todos os matriculados no período letivo selecionado receberão a mensagem enviada.

Validação do Filtro 

A validação dos filtros tem como objetivo garantir que todos os filtros selecionados estejam completos, consistentes e devidamente relacionados.

A inconsistência ocorre quando um filtro dependente não possui todas as informações exigidas por um filtro anterior.

Como o filtro opera em multi-contexto, esse tipo de inconsistência pode acontecer, por exemplo, quando o usuário seleciona um **período letivo das coligadas 1 e 2**, mas, nos filtros seguintes, informa dados relacionados apenas à **coligada 2**. Nesse cenário, ao processar a solicitação, **apenas os filtros completos da coligada 2 serão considerados**.

Ao clicar no botão **“Avançar”**, caso sejam encontradas inconsistências, será exibida uma tela de confirmação explicando que há filtros inconsistentes.

O usuário poderá então escolher:

* **Sim:** prosseguir com o envio. Neste caso, os filtros inconsistentes serão automaticamente desconsiderados no processamento da mensagem.
* **Não:** interromper o envio, permitindo que o usuário revise e ajuste os filtros antes de continuar.

**Essa validação tem como finalidade assegurar que os dados utilizados no envio sejam coerentes, evitando falhas no processamento e garantindo que a comunicação atinja corretamente o público-alvo desejado.**

Exemplo 1:

**Filtro selecionado** **Curso:**Direito, Sistemas de Informação, Veterinária e Administração.  
**Habilitação:** Recursos Humanos.

Após preencher o campo habilitação e clicar em **"Avançar"**, o seguinte modal será exibido:

**Inconsistência:**

Exemplo 2:

**Filtro selecionado****Período letivo:** "2025/2" (coligada 6) e "2019" (coligada 1).  
**Curso:** Sistemas de Informação (coligada 1).

Após preencher o campo curso e clicar em **"Avançar"**, o seguinte modal será exibido:

**Inconsistência**

**Exemplo preenchimento do filtro avançado (GIF):**

Matriz Aplicada

O filtro de matriz aplicado não retornará registros inativos; serão exibidas apenas as matrizes atuais ou ativas.

Regra de Comunicação

A regra de comunicação permite o cadastro de **filtros personalizados**, que serão respeitados durante a seleção de filtros aqui na Central de Comunicação.  
Ou seja, se uma regra de comunicação possuir filtros definidos, as informações disponíveis para seleção estarão limitadas de acordo com esses filtros.

Para entender todos os comportamentos e regras envolvidos, recomendamos consultar a [**documentação da regra de comunicação**](https://tdn.totvs.com/pages/viewpage.action?pageId=898441783#id-01Regrasdecomunica%C3%A7%C3%A3o-Regradecomunica%C3%A7%C3%A3o).

Carregamento e Busca nos Filtros

Todos os filtros serão carregados automaticamente ao clicar na lupa . A primeira consulta é limitada a uma quantidade fixa de registros. Caso existam mais resultados, será exibida a opção **"Carregar mais resultados"** .

Se precisar buscar por um filtro utilizando o código ou a descrição, digite o termo desejado no campo de pesquisa e pressione **Enter** ou clique no **ícone da lupa**.

* **Busca por código:** O sistema retornará todos os registros que **iniciam** com o termo digitado. Por exemplo, ao buscar por "A001", serão exibidos os códigos "A001", "A0010", "A0011", etc.
* **Busca por descrição/nome:** O sistema retornará todos os registros que **contenham** o termo digitado em qualquer parte do nome ou da descrição.
Dependências dos Filtros

Abaixo estão as dependências entre os filtros:

* **Curso** –  depende do Período Letivo.
* **Habilitação** – depende do Período Letivo e Curso.
* **Matriz Aplicada** –  depende do Período Letivo, Curso e Habilitação.
* **Turno** – depende do Período Letivo, Curso, Habilitação e Matriz Aplicada.
* **Turma** – depende do Período Letivo , Curso, Habilitação, Matriz Aplicada e Turno.
* **Coordenador** – depende do Período Letivo.
* **Aluno e Professor** — dependem do **Período Letivo**. No entanto, caso algum filtro esteja preenchido, ele será considerado na listagem de alunos ou professores.  
  Por exemplo, se o filtro de **Turma** estiver preenchido, serão exibidos apenas os alunos matriculados nessa turma.

* **Visualização de Filtro avançado aplicado**

Foi implementada a melhoria na visualização dos filtros que definem o público-alvo das mensagens. Agora, tanto o aprovador quanto o criador conseguem visualizar de forma clara e detalhada todo o público para o qual a mensagem foi direcionada. A visualização proporciona maior transparência e controle sobre o alcance das mensagens, facilitando a conferência e validação dos públicos-alvo antes do envio.

**Onde visualizar:**

* Durante a criação de uma nova mensagem;
* Ao utilizar uma mensagem como modelo;
* Durante a visualização de uma mensagem existente.

**Ao criar, editar ou utilizar uma mensagem como modelo, o sistema exibirá os filtros aplicados conforme os critérios selecionados, apresentando-os da seguinte forma:**

# Meu eduCONNECT

---

Importante

**Exibição da opção "Meu eduCONNECT"**

* Para que a opção **Meu eduCONNECT** seja exibida no PGE, é necessário ativar a integração com eduCONNECT (Educacional > eduCONNECT), e habilitar na **Regra de Comunicação**.
* Se o usuário marcar a opção **"Para o Meu eduCONNECT"**.
* Quando o usuário selecionar somente a opção do **Filtro predefinido** na etapa Público-alvo, a etapa **Meu eduCONNECT**  **não será exibida**, pois a categoria deverá ser identificada na consulta SQL do filtro predefinido (deverá existir uma coluna IDCATEGORIA).

Ao selecionar algum filtro no **Filtro Avançado**, a etapa **Meu eduCONNECT** será habilitada. Nessa etapa será obrigatório informar a categoria.

Conforme o filtro selecionado será apresentado por contexto um campo para selecionar a categoria que deverá ser considerada.

**Exemplo (GIF): etapa Meu eduCONNECT.**

Categoria com Validade

É possível definir, no cadastro de categorias, um prazo de validade para as mensagens, ou seja, o tempo que elas **ficarão** disponíveis para visualização na linha do tempo do aplicativo.

Para mais informações sobre o funcionamento, [[clique aqui]](https://tdn.totvs.com/display/LRM/Cadastro+de+categorias).

Quando a categoria selecionada possuir validade, será exibido um ícone indicando esse comportamento. Ao passar o mouse sobre ele, será possível visualizar o período configurado.

**Exemplo (GIF): Envio de Mensagem quando etapa Meu eduCONNECT está habilitada ao selecionar Filtro avançado.**

Validade das mensagens 

A partir da versão **12.1.2602**, será possível definir um período de validade para as mensagens durante a criação da categoria. Como é demonstrado no .

# Finalização

---

Nesta etapa final do fluxo de envio, são definidas algumas informações essenciais, como:

Informações do remetente

Será necessário identificar, no campo **"Remetente"**, as informações do responsável pelo envio da mensagem. Para isso, serão disponibilizadas as seguintes opções:

1. **Usuário (Usuário Autenticado):**

   * O remetente será o próprio usuário autenticado no Portal Gestão Educacional.
   * O e-mail do usuário será utilizado como remetente da mensagem.
2. **Coligada:**

   * As informações da coligada onde o envio está sendo processado serão utilizadas como remetente.
3. **Coligada Global:**

   * Serão consideradas as informações configuradas nas parametrizações globais da coligada.
4. **Personalizado:**

   * Permite selecionar remetentes com e-mails previamente configurados no RM.
   * Além disso, é possível definir um **nome personalizado** para o remetente.

Exemplo:

Os e-mails que poderão ser selecionados como **remetente personalizado** devem ser previamente configurados nos parâmetros do TOTVS Educacional, acessando o caminho: **Educacional >> Secretaria**.

Confira o exemplo na imagem abaixo:

Agendamento

Para agendar o envio da mensagem, selecione a opção **“Deseja agendar”** como **Sim** e preencha as informações necessárias para que o sistema identifique o momento exato para o disparo da mensagem.

Caso não opte pelo agendamento, o envio será realizado **imediatamente**.

Abaixo, você pode conferir um GIF demonstrando as opções disponíveis e o processo de envio da mensagem:

O recurso de **agendamento de mensagens** estará disponível **somente** para sistemas configurados no **modelo de 3 camadas**.

O agendamento pode ser com recorrência, para maiores informações [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=944706219#id-03Gest%C3%A3odeMensagens-EnviodeMensagemcomRecorr%C3%AAncia)

Após a confirmação do envio/Solicitação de envioEnvio de mensagem com aprovação 

Caso a mensagem exija aprovação, um e-mail será encaminhado aos usuários designados como aprovadores.

Exemplo:

O botão **"Acessar Central"**, exibido no e-mail, facilita o acesso direto ao portal e só estará disponível se a URL do portal for configurada em *Ambiente > Parâmetros Globais > Frame HTML*. Caso contrário, o usuário aprovador receberá apenas a notificação por e-mail, sem o botão.

Status de Finalização e Processamento do Envio

Todo envio de mensagem, **agendado ou não**, é processado por um **JOB,** ou seja, a mensagem enviada entra em uma **fila de processamento** e é disparada conforme a ordem desta fila.

Portanto o status de finalização e processamento do envio da mensagem será enviado para o e-mail do usuário autenticado no **Portal Gestão Educacional**, ou seja, para o e-mail do responsável pelo envio.

**Mensagem Enviada com Sucesso:**

* Assim que o sistema processar o envio da mensagem, o usuário receberá um e-mail informando o status do envio.
* Este e-mail incluirá:

+ Um **log do processamento**, contendo informações como os usuários que receberam a mensagem.

**Falhas no Envio:**

* Em caso de falha no envio, será enviado um e-mail contendo o **log de erros**, detalhando o problema ocorrido.

# Processamento do Envio de Mensagens

---

Abaixo, explicamos como o sistema realiza o processamento e envio das mensagens. Este entendimento é importante, pois a central de comunicação é **multi-contexto**, ou seja, permite o envio de mensagens para várias coligadas, filiais ou níveis de ensino simultaneamente.

Levando isso em consideração, podemos ter uma alto volume de dados que serão processados, e com isso o envio de mensagens será segmentado conforme o tipo de filtro, filtro(avançado) ou filtro predefinido:

* **Filtros avançados**:  A separação dos pacotes de processamento será feita por contexto, ou seja, o envio de mensagens pode ser afetado pela seleção de múltiplos contextos. Cada contexto selecionado resultará em um processamento separado.

Exemplo

Suponha que um usuário da central de comunicação precise enviar uma mensagem para diferentes coligadas, filiais e níveis de ensino ao mesmo tempo. O filtro avançado foi configurado para abranger três contextos distintos, conforme os seguintes parâmetros:

* **Contexto 1**: Coligada 1, Filial 2, Nível de Ensino: Superior
* **Contexto 2**: Coligada 1, Filial 3, Nível de Ensino: Pós-Graduação
* **Contexto 3**: Coligada 2, Filial 1, Nível de Ensino: Técnico

Quando o filtro avançado é aplicado, o sistema dividirá o envio da mensagem em três execuções separadas, pois ele precisa processar as informações para cada contexto individualmente. O usuário que disparou o envio, após o processamento receberá **três e-mails** contendo as informações do envio, cada um relacionado a um dos contextos:

1. **E-mail 1**: Contém a mensagem com as informações de **Coligada 1, Filial 2, Nível de Ensino: Superior**.
2. **E-mail 2**: Contém a mensagem com as informações de **Coligada 1, Filial 3, Nível de Ensino: Pós-Graduação**.
3. **E-mail 3**: Contém a mensagem com as informações de **Coligada 2, Filial 1, Nível de Ensino: Técnico**.

Isso acontece porque o sistema segmenta o processamento conforme os diferentes contextos, garantindo que a mensagem seja enviada corretamente para cada grupo específico de destinatários.

* **Filtro predefinido:** A separação dos pacotes de processamento será feita para cada filtro predefinido informado.

Considerando o exemplo acima, se, além desse filtro avançado, forem adicionados mais três filtros pré-definidos, o processo será dividido em seis execuções no total, pois cada filtro pré-definido será executado separadamente.

**Conceito de Processamento Apenas para Filtros Completos**

Como a seleção de filtros é um recurso genérico e multi-contexto, com o objetivo de auxiliar o usuário e evitar envios indevidos, somente os filtros que estiverem totalmente preenchidos serão considerados para o envio.

Isso significa que, se um filtro não for completamente especificado, ele será descartado durante o processamento.

Exemplo de Processamento Somente para Filtros Completos

* **Exemplo 1:**

  + **Período letivo selecionado**: todos da filial 1 (coligada 1) e 2025 da filial 12 (coligada 6).
  + **Cursos selecionados**: Apenas cursos da coligada 6.
  + **Resultado:** O períodos letivos referente a coligada 1 serão descartados, pois não há cursos associados a ele.

* **Exemplo 2:**

  + **Cursos selecionados**: X e Y.
  + **Habilitações especificadas**: Apenas do curso X.
  + **Resultado:** O curso Y será descartado, pois não tem habilitações associadas.

Após o processamento do envio da mensagem, será enviado um anexo intitulado "Informações" no e-mail, contendo um log do processo, no qual estarão registrados os detalhes dos filtros considerados.

# Notificação de Envio

Sempre que ocorrer uma ação de **solicitação de aprovação**, **aprovação**, **reprovação** ou **conclusão de processamento** na Central de Comunicação, será gerada uma **notificação interna** com o objetivo de **enviar um e-mail ao usuário do sistema**. Para saber mais sobre a notificação de envio [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=965444172).
