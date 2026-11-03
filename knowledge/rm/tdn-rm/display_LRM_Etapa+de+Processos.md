---
content_hash: 8a9fa399c45684f22dad49c6d2ba1f97d84498f1030602c9d434572bd2c9aa63
fetched_at: '2026-06-29T00:11:32.903236+00:00'
page_id: '750401608'
product: rm
source: tdn-rm
title: Etapa de Processos
type: documentation
url: https://tdn.totvs.com/display/LRM/Etapa+de+Processos
version: 52
---

No processo de importação e gravação do XML o sistema irá executar os seguintes procedimentos:

* Importação de Arquivo XML
* Serviço de Consulta de Arquivo XML
* Inclusão de Movimento Através de XML

Detalharemos cada um deles a seguir.

---

Processos da Importação do XMLIdProcessoImportXMLIdImportacaoXMLImportação de Arquivo XML

É o processo responsável por buscar os documentos armazenados na pasta de recebimento (diretório para armazenamento dos arquivos XML, que foi definido conforme orientação na etapa de Parâmetros) e distribuí-los entre as coligadas da base.

Para executá-lo, no TOTVS Gestão de Estoque, Compras e Faturamento, acesse o menu *"Integrações > Monitor de Arquivos >Importação de Arquivo XML*".

Durante a execução deste processo serão validados os padrões de nomenclatura (prefixos) e tag’s dos arquivos. Somente serão importados os XML que obedeçam totalmente a todos os requisitos do schema definido pela SEFAZ.

Após finalização do processo, os documentos lidos serão exibidos na tela, com o status “Pendente” (até que seja executado o processo de consulta).

Caso ocorra algum problema, o XML será criado na base de dados com o status 'Inconsistente'. Para verificar o erro ocorrido, basta um duplo clique no registro para que seja exibido o Log onde o problema será demonstrado. Quando o arquivo está “Inconsistente”, será necessário corrigir a causa do erro para poder tentar incluí-lo no sistema. Após a correção do erro basta alterar o seu status para 'Pendente', através do processo *“Alterar status do arquivo”.*

Os documentos lidos durante a execução deste processo, serão automaticamente excluídos da pasta de recebimento (diretório onde estavam armazenados os arquivos xml).

O ideal é que a execução deste processo seja agendada, assim, periodicamente o mesmo será executado de forma automática, buscando os XML disponibilizados.

Para maiores detalhes acesse [http://tdn.TOTVS.com/display/public/LRM/CLB\_0002\_Jobs](https://tdn.totvs.com/display/public/LRM/CLB_0002_Jobs)

A partir da versão 12.1.2310, o download dos arquivos XML também pode ser feito manualmente, para os seguintes tipos: NF-e, CT-e e seus respectivos eventos de cancelamento. Bastando colocar os arquivos na pasta IN, do caminho mapeado.

A partir da versão 12.1.2410 esse processo só faz o processamento de 900 registros a cada execução. Para que mais registros sejam processados deve ser feito o cadastro de Segurança de Jobs Fracionáveis para o processo. Consulte a

Serviço de Consulta de Arquivo XML

O Serviço de Consulta de Arquivo XML será acessado a partir do TOTVS Gestão de Estoque, Compras e Faturamento, menu *"Integrações > Monitor de Arquivos >Serviço de Consulta de Arquivos XML*".

Este processo realiza as validações específicas de cada XML de acordo com o documento em questão (NF-e, NFS-e, CT-e). Caso o documento esteja válido e com o status *"Pendente"*, o registro do arquivo é excluído do monitor de arquivos, e passa a ser exibido na tela de cadastro dos XML (*"Compras > Importação de Arquivo XML - Cadastro XML"*), indicando que o mesmo foi incluído no sistema com sucesso.

Caso o status do documento seja "*Inconsistente",* será necessário corrigir a causa da inconsistência (conforme citado no tópico <*Importação de Arquivo XML*>) e somente após alterar o status do documento para "*Pendente"*, o Serviço de Consulta de Arquivo XML conseguirá fazer a validação do mesmo.

O ideal é que a execução deste processo seja agendada, assim periodicamente o mesmo será executado de forma automática.

A partir da versão 12.1.2410 esse processo só faz o processamento de 900 registros a cada execução. Para que mais registros sejam processados deve ser feito o cadastro de Segurança de Jobs Fracionáveis para o processo.  Consulte a

Inclusão de Movimento Através de XMLO **processo de Inclusão de Movimento a partir de um XML** poderá ser acessado tanto a partir da visão dos movimentos de entrada como a partir da tela do cadastro de XML (*Compras > Importação de Arquivo XML - Cadastro XML") .*

Detalharemos cada um deles clicando nos tópicos abaixo:



Os **dados e procedimentos da "Inclusão de Movimento Através de XML - NF-e"** independem de onde o processo foi acionado e iremos descrevê-los a seguir.

Aba Identificação

A aba *“Identificação”*, apresentará as informações gerais do movimento selecionado. Serão apresentados os seguintes dados:

* Destinatário / Filial – Filial do movimento;
* Emitente / Fornecedor – Fornecedor dos produtos;
* Chave de Acesso da NF-e;
* Série da NF-e;
* Número do Documento - Número da NF-e;
* Data de Emissão da NF-e;
* Tipo de Movimento no qual a NF-e foi inserida.

Estes dados, em sua maioria, são importados do XML e nenhum deles poderá ser alterado.

Será possível vincular o XML a um movimento de pedido existente na base de dados, bastando para isso que você marque o campo 'Receber Pedido' e clique no ícone "Incluir" para informar o(s) pedido(s) que será(ão) recebido(s) para este XML.

O sistema apresentará uma tela de filtros para que você selecione o(s) pedido(s) a ser(em) vinculado(s) ao movimento, sendo que o sistema filtrará apenas os pedidos que geram movimentos do tipo de movimento que será criado.

No nosso exemplo, como o movimento que será gerado é do tipo 1.2.12, somente os pedidos que podem ser faturados para este tipo de movimento estarão disponíveis para realizar o vínculo. Marque os pedidos que serão vinculados com a NF-e e clique em "OK".

Ao informar o(s) pedido(s), o sistema imediatamente efetuará o vínculo entre a NF-e e o(s) mesmo(s), caso as informações de ambos sejam correspondentes.

Outros pedidos de compras poderão ser adicionados a qualquer momento.

Na aba*"Identificação"*será informado ainda se a tela de edição do movimento será aberta ao fim do processo e se, consequentemente, o movimento poderá ser editado nesse momento. Assim, caso queira optar por abrir o movimento automaticamente logo após a sua tradução basta deixar que o campo 'Abrir a Edição do Movimento', permaneça marcado, visto que o mesmo já virá assinalado por default.

Caso este campo seja desmarcado, o sistema efetuará a inclusão através do XML  e retornará para a tela do cadastro de XML ou para a visão de Movimentos conforme a tela de onde o processo foi acionado.

Regras para vinculo de PedidoxXML

Este vínculo é feito com base no Produto informado no cadastro "**Produtos para Importação de XML**". Caso seja identificado um produto com o mesmo IDPRD na lista de pedidos, o sistema cria o relacionamento. Quando existem vários pedidos para o mesmo produto da NF-e, o sistema cria o relacionamento para cada um utilizando a seguinte regra:

* Ao criar o primeiro relacionamento com o item do pedido, o sistema automaticamente verifica se ainda existe saldo do produto em questão para a realização de novos vínculos. Caso exista, é realizada uma busca por itens de pedido que possuam o **mesmo** preço unitário do item já vinculado.
* Em situações onde o preço do(s) produto(s) no(s) pedido(s) possam variar, foi criada a possibilidade de utilizar o recurso de tolerância, ou seja, pode ser definido no cadastro de produto uma tolerância inferior e/ou superior para o preço. Desta forma o sistema utilizará esta margem na pesquisa pelo(s) produto(s) no(s) pedido(s). Segue configuração necessária:

**Importante:**

* A tolerância é um recurso já existente para o processo de faturamento, ou seja, deve ser analisado se o mesmo pode ser utilizado.
* O Tipo de movimento de NF-e "**movimento de destino**" deve ser parametrizado para utilizar tolerância por "Preço" ou "Quantidade e Preço".
* No cadastro do produto devem ser preenchidos os campos Tolerância Preço (%) → Inferior e/ou Superior. Lembre-se que este campo se refere ao percentual que será utilizado no cálculo
* Durante o recebimento da NF-e este percentual será aplicado ao preço unitário do item do pedido relacionado ao produto da nota. Exemplo:  
    
  Pedidos  
  1º Pedido - Produto X, Quantidade 1 UN, Preço R$ 10,00  
  2º Pedido - Produto X, Quantidade 1 UN, Preço R$ 10,96  
  3º Pedido - Produto X, Quantidade 1 UN, Preço R$ 10,96  
  4º Pedido - Produto X, Quantidade 1 UN, Preço R$ 10,97  
  5º Pedido - Produto X, Quantidade 1 UN, Preço R$ 11,00  
    
  Nota Fiscal  
  Produto X, Quantidade 5 UN, Preço R$ 10,50  
    
  Caso **não** seja utiliza a tolerância, o sistema vai relacionar o item da nota ao Item do primeiro pedido, ficando ainda um saldo de 4 UN a serem traduzidas.  
  Caso **seja** utilizada uma tolerância superior e inferior de 10%,   o sistema realizará a pesquisa pelos produtos utilizando a seguinte margem:  
    
  1º Pedido - Produto X, Quantidade 1 UN, Preço entre R$ 9,00 e R$ 11,00   
  2º Pedido - Produto X, Quantidade 1 UN, Preço entre R$ 9,864 e R$ 12,056   
  3º Pedido - Produto X, Quantidade 1 UN, Preço entre R$ 9,864 e R$ 12,056   
  4º Pedido - Produto X, Quantidade 1 UN, Preço entre R$ 9,873 e R$  12,067  
  5º Pedido - Produto X, Quantidade 1 UN, Preço entre R$ 9,90 e R$ 12,10   
    
  Desta forma todos os itens dos pedidos serão relacionados ao produto da NF-e.

Regra de Vínculo do Pedido via Xml no TOTVS Colaboração

**Regra de Vínculo entre Pedido e Produto com informações de pedido presente no XML**

O sistema verifica a tag **"xPed"** e **"nItemPed"** no XML, que representa o **Número do Pedido** no fornecedor e **Número do Item do Pedido.**

* Se as tags **"xPed"** e **"nItemPed"** estiverem preenchidas e houver um pedido correspondente na base de dados, ele será selecionado

Senão atender essa regra o fluxo vai cair na regra debaixo.

**Regra de Recuperação de Movimento, caso as informações de pedido não esteja informado no XML**

Se não existir um pedido correspondente, o sistema procurará por um **pedido de compra pendente** que:

* Foi emitido para o CNPJ do fornecedor da nota.
* Contém os mesmos produtos e mesmas quantidades da nota fiscal.
Aba Tradução dos Itens

Na aba *"Tradução de Itens"* serão apresentados os dados relativos aos itens da NF-e.

Caso o XML não esteja vinculado a um pedido o sistema apresentará além dos dados do item no XML, a Unidade para Importação de XML, o Código e o Nome do Produto para Importação de XML, ou seja os dados do produto correspondente em sua base de dados. O sistema verificará essas informações nas tabelas "Unidades para Importação de Arquivo XML" e "Produtos para Importação de Arquivo XML".

Caso ao verificar estas tabelas o sistema não encontre os dados correspondentes aos produtos constantes do XML, você poderá neste momento efetuar manualmente a tradução dos itens e as informações fornecidas por você serão automaticamente inseridas nestas tabelas.

Para informar qual é o produto da sua base de dados que é correspondente ao produto constante do XML clique no campo 'Produto Tradução' e clique na seta da lista de opções. O sistema abrirá um lookup onde você poderá selecionar o produto desejado através da informação do código ou do nome do mesmo.

Conforme a informação fornecida o sistema lhe apresentará a lista dos produtos disponíveis na sua base de dados e que atendem à seleção informada.

O produto selecionado irá para a tela de*"Tradução de Itens"* e automaticamente será gravado pelo sistema na tabela*"Produtos para Importação de XML"*.

O mesmo processo poderá ser efetuado para as unidades de medida existentes no XML e que não tenham sido traduzidas pelo sistema.

Além de incluir produtos e unidades que não foram traduzidos você poderá alterar os dados que o sistema trouxe na tradução optando por um outro produto ou unidade diferentes daqueles indicados pelo sistema, bastando para isso clicar nos campos 'Unidade Tradução' ou 'Produto Tradução' e fornecer as informações desejadas.

Caso o XML esteja vinculado a pedido(s) os campos 'Código do Produto de Tradução' e 'Produto Tradução' permanecerão em branco e o sistema apresentará além dos dados do item no XML, os campos relativos ao Pedido. Estes dados também serão preenchidos com base no conteúdo das tabelas "Unidades para Importação de Arquivo XML" e "Produtos para Importação de Arquivo XML".

Assim, caso o campo "Receber Pedido" esteja marcado, os quatro campos referentes ao pedido (Número do Pedido, Código do Produto do Pedido, Número Sequencial do Item no Pedido e o Nome do Produto do Pedido) serão exibidos na aba*"Tradução de Itens".*

Caso durante o processo de Inclusão do Movimento via XML, o campo "Receber Pedido" seja, em algum momento, desmarcado, os campos referentes ao pedido (Número do Pedido, Código do Produto do Pedido, Número Sequencial do Item no Pedido e o Nome do Produto do Pedido) não mais serão apresentados em tela, já que não haverá a necessidade de utilização dos mesmos.

Você poderá alterar o produto do pedido que foi informado pelo sistema, bastando para isso, selecionar o item cujo produto do pedido deseja alterar, clicar no campo 'Produto no Pedido' e clicar na seta da lista de opções para que os produtos dos pedidos vinculados ao XML sejam apresentados.

Clique então no botão do lookup do produto.

O lookup exibirá o(s) produto(s) do(s) pedido(s) de compra vinculado(s) ao XML, e que ainda possuem saldo a receber, para que você selecione um deles.

Se nesse momento ainda existir algum item no XML cuja tradução ainda não consta da tabela*"Produtos para Importação de XML"*o sistema não conseguirá localizá-lo nos pedidos vinculados, mas você poderá informar a tradução diretamente nesta tela.

Caso selecione o produto a partir do campo  'Produto Tradução' o sistema exibirá todos os registros da base para que você possa definir qual produto será utilizado na amarração, já se o produto existir em um dos pedidos vinculados clique no campo 'Produto do Pedido' e o lookup exibirá todos os produtos do(s) pedido(s) de compra vinculado(s) ao XML, e à medida em que a tradução estiver sendo realizada, o sistema irá consumir o saldo dos pedidos até que os mesmos sejam zerados.

Outro recurso disponível na aba *"Tradução de Itens"*é o botão "Múltiplos".

O botão Múltiplos poderá ser utilizado quando o pedido selecionado pelo sistema não possuir quantidade suficiente para realizar a tradução do produto. Assim, ao clicar no botão "Múltiplos", será criada uma réplica da linha selecionada para que o produto possa ser associado a outro registro.

Aba Tributação

Na aba *“Tributação de Itens”* serão exibidos todos os tributos parametrizados no tipo de movimento do movimento que será gerado.

Na parte superior da tela, em *“Tributação da Nota”* serão carregadas as informações relativas aos tributos do movimento.

Na parte inferior da tela a visão contida no grupo*“Tributação dos Produtos”*será responsável por exibir os impostos dos produtos (itens de movimento).

O preenchimento dos valores relativos aos tributos (base de cálculo, alíquota e valor) será efetuado obedecendo à configuração do campo 'Busca Valores Imp XML’. Para verificar a sua configuração vá em*"Ambiente > Parâmetros > Gestão de Estoque, Compras e Faturamento > 04.06 - Gestão Compras > 04.06.05 - Recebimentos de Materiais"*e no tipo de movimento desejado consulte este campo em*"Fis - Tributação - Item" ou 'Fis - Tributação - Movimento"*.

O sistema informará os valores, conforme o preenchimento do campo, com uma das opções a seguir:

* XML: Esta opção deverá ser selecionada caso deseje que os valores do tributo sejam aqueles recebidos do arquivo XML da NF-e, sem a necessidade de comparação com o tipo de movimento;
* Tipo de Movimento - Não comparar com XML: Esta opção deve ser selecionada caso deseje que todas as informações do tributo sejam calculadas/buscadas pelo sistema conforme a parametrização do tipo de movimento, sem a necessidade de comparação com os valores advindos do arquivo XML;
* Tipo de Movimento - Comparar com XML: Esta opção deve ser selecionada caso deseje que todas as informações do tributo sejam calculadas/buscadas pelo sistema, mas elas devem ser comparadas com as informações advindas do XML. Caso tenha optado por executar esse processo sem abrir a edição do movimento, caso existam diferenças entre os tributos calculados e os constantes do XML, ao final da execução o sistema irá lhe apresentar uma mensagem com essa informação, bastando que você vá à edição do movimento se quiser alterar os valores que foram calculados. Já caso tenha optado por executar esse processo e 'Abrir a Edição do Movimento' quando for solicitada a gravação do movimento, o sistema abrirá a tela com a diferença dos tributos caso existam.

  Atenção

  Na importação do XML da NFS-e através de pedido, o sistema abre o movimento de destino para edição, com os valores calculados conforme o pedido de origem, exceto os valores de base de cálculo que são editáveis ou caso informado a opção "Calculado" no campo "Manter Valor" da linha dos tributos o sistema vai considerar a fórmula da base de cálculo no momento de salvar o movimento.  
    
  Se o valor da base de cálculo do tributo ISS no pedido for diferente da base de cálculo informada no XML o sistema apresenta a seguinte mensagem de alerta: "Identificado valores de base de cálculo diferentes do XML importado", dessa forma o usuário pode ajustar o pedido ou o movimento de destino gerado.  
    
  Se o tipo de movimento de destino não possuir todos os tributos informados no XML importado também será apresentado um alerta informando sobre os tributos que não serão importados conforme imagem abaixo:

  Obs.: A configuração do campo "Busca Valores Imp XML" não se Aplica ao recebimento de NFS-e via XML.

  Imagem
