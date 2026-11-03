---
content_hash: 47dba43749afeb905427bc08ea232256a32c78982f129ec9b7bd671c5cd88147
fetched_at: '2026-06-29T00:09:25.999549+00:00'
page_id: '423938220'
product: rm
source: tdn-rm
title: Cotação (Compras)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938220
version: 176
---

O processo inicia-se na criação de uma solicitação de compras onde é gerado um movimento do tipo 1.1.xx onde são solicitados os produtos que a empresa precisa comprar. Após a criação do movimento de solicitação, é iniciada então a Cotação, onde a relação dos produtos será enviada para determinados Fornecedores que darão a resposta do orçamento. É utilizado então o quadro comparativo para que seja definido qual é a compra que será mais benéfica para a empresa. Após o cálculo do quadro comparativo, temos o vencedor da cotação. A partir desse momento geramos a ordem de compras num outro movimento do tipo 1.1.xx. Este parametrizado para ser um "Pedido de compra" que posteriormente dará origem ao movimento final de compras do tipo 1.2.xx, neste tipo de movimento obrigatoriamente deverá ter um Fornecedor vinculado, este deverá ser cadastrado no sistema antes de iniciar o processo de compras.

Configuração de Movimento

Para trabalhar com cotação, devemos ter a seguinte parametrização nos tipos de movimento:

**Movimento de Solicitação de Compras**

Movimento do tipo 1.1.xx de solicitação de compras parametrizado da seguinte maneira:

* Compra/Venda – Características

Parâmetro "Gera movimento de compras" marcado.

Movimento gerado deafult: Informar um tipo de movimento parametrizado como "Pedido de compras".

* Compra/Venda – Outros Dados

Parâmetro "Tipo do movimento de compra" marcado como "Solicitação de compras".

**Movimento de Ordem de Compras**

Movimento do tipo 1.1.xx de ordem de compras parametrizado da seguinte maneira:

* Movimento - Identificação

Edita Numeração – "Mostra"

* Compra/Venda – Características

Parâmetro "Gera movimento de compras" marcado

* Compra/Venda – Outros Dados

Parâmetro "Tipo do movimento de compra" marcar "Pedido de compras"

Assistente de Cotação

Abrindo o assistente da cotação, temos as seguintes opções:

**Dados Iniciais da Cotação**

Devem ser preenchidos os campos Data da Cotação, Limite de resposta, Moeda, Funcionário responsável, coligada(s), filial(s) e tipo de movimento(s) que farão parte da cotação.

É possível selecionar todos as filiais/coligadas e tipos de movimento, clicando nos botões na parte superior das árvores de seleção e também é possível filtrar as Filiais/Coligadas e tipo de movimento utilizando o campo pesquisar.

***Observação***: A data de Limite de resposta não pode ser inferior a data da cotação. Não é permitido avançar etapa sem que todos os campos citados em negrito acima estejam sem preenchimento.

**Filtro de Produto**

Ao avançar etapa temos que filtrar e selecionar os itens que serão cotados. Através do filtro é possível buscar todos os itens pendentes das filiais selecionadas na etapa anterior para fazerem parte da cotação.   
Na seleção do **Filtro de Produto** que fará parte da cotação, é possível filtrar os Produtos de um determinado [Grupo de Produtos](https://tdn.totvs.com/display/public/LRM/Grupo+de+Produtos).

Ao criar uma cotação se algum produto selecionado estiver inativo, ao tentar avançar a etapa no assistente de cotação o sistema exibirá uma mensagem informando que há produto inativo, que não pode ser cotado e deve ser removido.   
Como a mensagem não mostra quais produtos estão inativos, há a coluna Produto Inativo para o usuário identificá-los. Esse mesmo comportamento é apresentado quando o usuário tentar incluir numa cotação já existente um item inativo.  
Para acessar as informações do produto basta clicar no link disponível na Descrição do Produto.  
Os campos Cód. Marca e Marca Solicitada serão exibidos quando o parâmetro [Usar Marca de Produto na Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938121) estiver habilitado. Estes campos exibirão o código e descrição da marca informados no item do movimento de solicitação de compras.   
Quando não for informado marca no item da solicitação de compras, será exibida a marca default informada no cadastro de produto. Estes campos são apenas para visualização.  
Através do campo Permite Fornecedor Trocar Marca será possível definir se o fornecedor poderá ou não fazer a troca de marca do produto na cotação no caso em que o orçamento/negociação for enviado para o fornecedor através de planilha de exportação. Este campo será exibido quando o perfil do usuário logado possuir permissão para Trocar Marca dos Produtos na Cotação e quando o parâmetro [Usar Marca de Produto na Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938121) estiver habilitado. Esta opção estará marcada por padrão, mas poderá ser desmarcada conforme opção do usuário, caso seja desmarcada, não será permitido ao fornecedor alterar a marca de um produto que está sendo solicitado no orçamento ou negociação.

**Escolha de Fornecedores**

Após a seleção dos produtos, selecionamos os fornecedores que irão participar do processo de cotação. Há possibilidade de filtrar os fornecedores através de vários campos, sendo que, o campo CNPJ/CPF é o default de filtro.

**A partir da versão 12.1.2606,** na seleção do **Filtro de Fornecedor** que fará parte da cotação, é possível filtrar os fornecedores de um determinado [Grupo de Produtos](https://tdn.totvs.com/display/public/LRM/Grupo+de+Produtos) ou o [Estado de Fornecimento](https://tdn.totvs.com/display/LRM/Estados+de+Fornecimento).

Para estes registros filtrados, será exibido o valor do campo usado no filtro (código do grupo de produto ou estado do fornecimento).

Conforme permissões de acesso do usuário é possível cadastrar e editar Fornecedores no momento da seleção dos Fornecedores que irão participar da Cotação.  
Existe um limite máximo e mínimo de fornecedores para ser selecionado. Este limite é estabelecido nos parâmetros da cotação.

**Informações Gerais**

Com os fornecedores selecionados, avançamos para a última etapa do processo de inclusão da cotação onde preenchemos a Condição de pagamento, Transportadora, Data Limite para Entrega da Mercadoria, se na cotação será considerado crédito de IPI e ICMS no cálculo da melhor oferta e Tipo de julgamento da melhor oferta (este parametrizado ou não).

Cotação

Após conclusão do processo de Assistente de Cotação é criado o movimento a Cotação que é apresentado os principais dados que foram preenchidos como a Data Cotação, Data de limite de resposta, Comprador responsável etc..

Ao editar Cotação é possivel ter acesso aos dados da Cotação.

CotaçaoOrçamentos

Nessa grid são apresentados todos os Orçamentos dos Fornecedores selecionados, nessa tela é possivel Incluir ou Excluir Fornecedores na Cotação.

Itens de MovimentoPropriedades Campos Complementares

**A partir da versão 12.1.2606,** foi criado o Campo Complementar da Cotação, para saber mais [clique aqui.](https://tdn.totvs.com/x/ushEGQ)

Comunicar Fornecedores

Este processo tem por objetivo informar aos fornecedores presentes na cotação, sobre a existência da mesma, e assim, solicitar que seja enviado o orçamento dos produtos cotados. Existem três formas de comunicar aos fornecedores:

* **Imprimir Orçamento**: O sistema permite a impressão de um pedido de orçamento. O conteúdo do relatório impresso será de acordo com o relatório parametrizado. Para que se possa dar continuidade à cotação a opção "Impressão Definitiva" deve estar marcada, pois ao imprimir o orçamento com esta opção desmarcada, o sistema não habilita a cotação para a próxima etapa, que seria registrar orçamento.
* **Enviar Orçamento via E-mail**: É enviado um e-mail para o fornecedor com o pedido de orçamento.  O conteúdo do e-mail será de acordo com o relatório parametrizado, ficando a critério do usuário enviar o relatório como anexo ou no corpo do e-mail em formato texto. Exportar Planilha de Orçamento/Negociação: ao utilizar essa opção é possível enviar via e-mail para os fornecedores uma planilha do Orçamento/Negociação da Cotação em questão, na qual os fornecedores devem informar suas cotações para os produtos. Após receber a planilha de volta dos fornecedores, deve-se importar a mesma no sistema e desta forma será atualizado o Orçamento/Negociação da Cotação com as informações inseridas pelos fornecedores na planilha. Para mais informações sobre o processo de Exportação/Importação de Cotação via Planilha [clique aqui](http://tdn.totvs.com/pages/viewpage.action?pageId=423938009). Antes de enviar o e-mail é possível marcar a opção "Cópia para Comprador" que consiste em enviar um e-mail  não só para os fornecedores, mas também para o comprador da cotação em questão. Outra opção para o envio do e-mail seria "E-mail somente p/ Contatos", que consiste em enviar o e-mail apenas para os contatos do fornecedor que são informados no anexo do cadastro do cli/for.
* **Exportar Orçamento p/ Web**: Conforme "Enviar Orçamento dia E-mail" é enviado um e-mail para o fornecedor com o conteúdo estipulado pelo relatório. Além do conteúdo do relatório, é enviado ao fornecedor, login e senha.  Este login e senha serão utilizados pelo fornecedor para acessar o portal e informar o orçamento para os produtos da cotação. Exportando o orçamento para Web, o comprador não terá condições  de registrar orçamento para os fornecedores que receberem o orçamento via Web. Para esses fornecedores, o comprador somente terá condição de dar continuidade ao processo após vencimento da data limite de resposta.  Uma vez que a cotação atingiu o limite para resposta, o comprador poderá executar os processos do Server, e assim, importar os dados do portal para a cotação.
  + Informação do remente utilizado pode ser verificado no link: 
    - A informação especifica "Funcionário Logado" aqui representa o usuário responsável pela cotação, utiliza como e-mail do remente o e-mail cadastrado na tabela PPESSOA que está vinculado ao vendedor (TVEN) da cotação.

***Atenção!***Caso a data limite esteja inferior a data do sistema, ou seja, inferior a data do banco de dados, o sistema não permite a execução do processo "Comunicar Fornecedores".

Relatório do Book

* **Imprimir Orçamento**: 04.002 – Pedido de Orçamento
* **Enviar Orçamento via E-mail:** 04.007 – Pedido de Orçamento
* **Exportar Orçamento p/ Web:** 04.008 – Exportação Cotação WEB

Durante a criação de um relatório customizado (tendo como base o relatório do Book), aconselha-se que seu grupo principal contenha a tabela **TCITMORCAMENTO** e o respectivo campo **CODCOTACAO**. No caso de orçamento para Cotação via Web, deverá ser utilizada como tabela principal do relatório a **TWORCAMENTO**, para que o relatório possa ser filtrado pelo código da cotação e/ou do fornecedor.

***Atenção!***

* O processo de comunicar fornecedores pode ser executado múltiplas vezes:
  + Cada fornecedor pode ter uma forma de comunicado diferente.
  + Pode-se mudar a forma de comunicado do fornecedor.
  + Se é um fornecedor comunicado via WEB e declinou de participar da cotação, nos dados do fornecedor isso fica claro com a informação [DECLINADO PELO FORNECEDOR]
* A comunicação do fornecedor pela WEB tem algumas regras
  + É exclusiva, se comunicar novamente o mesmo fornecedor usando outro meio de comunicação vai desabilitar o acesso da cotação via portal.
    - Quando isso for feito, o cliente passa a poder registrar o orçamento.
    - Se o fornecedor preencher parte da cotação essa vai estar imediatamente disponível.
  + Uma cotação com orçamento enviado via WEB só pode ter os valores de orçamento e negociação alterados pelo fornecedor através do portal do fornecedor.
  + Uma cotação com orçamento enviado via WEB pode ser declinada pelo fornecedor, neste momento ele pode informar o motivo de não participar da cotação.
  + Ao comunicar novamente um fornecedor que tenha declinado da cotação tanto o declínio quanto a justificativa são removidos.
* O fornecedor passa a ter um único login/senha e acesso a todas as cotações por esse login/senha. Ao comunicar o mesmo fornecedor uma segunda vez, na senha vai apenas um aviso de que deve-se usar a mesma ou solicitar ao comprador a regeração de senha em caso de esquecimento. Caso o comprador queira fazer a regeração de senha, ele deve marcar a opção de "Regerar senha" no processo de comunicação, desta forma a senha será trocada e os dados de acesso serão reenviados ao fornecedor.
* As tabela de dados TW\* responsáveis por guardar os dados para posterior importação deixam de ser utilizadas, todo dado informado pelo fornecedor e registrado diretamente na cotação.
* A importação WEB deixa de ser utilizada para as novas cotação/exportações web feitas a partir da versão 12.1.34.
* Os dados embora sejam gravados diretamente na cotação continuam sem permissão de visualização e registro de orçamento devido a lisura do processo.
Inserir Item sem Solicitação

**Disponivel a partir da versão 12.1.2610**

Inserir item sem solicitação de compra

Permite inserir itens avulsos na cotação. Os itens estarão associados a um novo movimento configurado do tipo **Solicitações de Compras**.

Somente é permitido adicionar item sem solicitação com a devida permissão do perfil do usuário, bem quando a cotação está em negociação, composição ou aguardando resposta fornecedor. 

Os campos disponíveis são:

* **Filial (obrigatório):**Filiais ativas da coligada corrente;
* **Local de Estoque (não obrigatório):** Local de estoque do produto/serviço. (serão listados locais de estoque pertencentes a coligada/filial informada)
* **Tipo Movimento (obrigatório):** O tipo do movimento que o itens estarão associados. (serão listadas tipo de movimento classificados como **Solicitações de Compras**, da coligada corrente e que o usuário possui permissão)
* **Centro de Custo (não obrigatório):** Centro de custo corresponde ao produto/serviço informado. (serão listadas centro de custos ativos e que permitam lançamento)
* **Projeto (não obrigatório):**Projetos da coligada corrente. (visível quando integrado com o **RM SOLUM**)
* **Tarefa (não obrigatório):** Tarefas da coligada corrente e pertencentes ao projeto informado. (visível quando integrado com o **RM SOLUM**)

É necessário informar um ou mais produto/serviço, eles serão adicionados como itens do movimento a ser criado.   
Para isso, é necessário informar os seguintes campos:

* **Produto (obrigatório):** Produtos/serviços ativos da coligada corrente.
* **Unidade (obrigatório):** Unidade corresponde ao produto/serviço informado. Informado um produto será preenchido automaticamente com a unidade de compra padrão.
* **Quantidade (obrigatório):** Quantidade (valor numérico) corresponde ao produto informado.

Será valido se o produto/serviço informado já foi inserido na cotação anteriormente pelo processo de **Inserir Item sem Cotação.** Caso positivo, não sendo possível a sua inclusão.

Não é permitido excluir os itens sem solicitação através dos processos "Excluir Item(s)" ou "Excluir Produtos não Cotados". Para fazê-lo, utilize o processo **Excluir item sem Solicitação.**

Excluir Item sem Solicitação

**Disponivel a partir da versão 12.1.2610**

Excluir itens incluídos sem solicitação de compra

Permite selecionar um produto incluído através da operação "Inserir Item sem Solicitação" e excluir o item correspondente. Só é permitido excluir um item de cotações com status de Composição, Aguardando Resposta de Fornecedores e Negociação.

Após a execução, o item correspondente será removido da aba "Itens de Movimento" e também dos itens de orçamento, como no exemplo a seguir:

Substituir Item no Orçamento

**Disponivel a partir da versão 12.1.2610**

Substituir um item de orçamento da cotação com um outro produto.

Na tela do processo é necessário indicar qual produto será substituído nos itens de orçamento, bem como o produto substituto, juntamente com a unidade e quantidade total do substituto.

 

Todos os itens de orçamento com o produto a substituir serão ajustados, trocando por aquele informado, atualizando a unidade e quantidade. Caso exista itens de orçamento com produto repetido, a quantidade informada do substituto será rateada entre os itens proporcionando de acordo com a quantidade original do item de orçamento, já considerando também cenários onde as unidades nos itens de orçamento originais são diferentes.

O item de orçamento ajustado terá uma marcação específica, com uma imagem indicando que passou pelo processo de substituição, assim como um novo campo de nome I*tem Substituído* indicando as informações do produto substituído.

Caso um produto já tenho sido substituído no orçamento não poderá ser incluído somo substituto numa outra substituição.

Além de ajustar os itens de orçamento, os itens de movimento das solicitações de compra vinculadas serão alteradas com a troca do produto, unidade e quantidade (de forma proporcional), além de zerar o valor unitário.

Na visualização dos itens de orçamento (botão *Itens do Orçamento*) passa a exibir também os registros substituídos, com uma marcação específica através de uma imagem.

Ordenar Itens de Orçamento na Cotação

**Disponivel a partir da versão 12.1.2610**

Ordenar os itens de orçamento da cotação. 

Com as setas é possível mover para baixo ou para cima os itens de orçamento, ao executar o processo, a ordem será salva conforme organizado.

 

Os itens ordenados serão exibidos nas telas:

* Anexo Itens Orçamento e tela de

* Produtos da cotação

Registrar Orçamento

Esta etapa da cotação, basicamente, tem por objetivo informar preço e condição de pagamento para cada produto a ser cotado, além de ser possível cadastrar os Produtos para Tradução (). A permissão no perfil do usuário para Editar/Alterar/Deletar Produtos para Tradução, é a mesma segurança do cadastro de Produto. Ao registrar orçamento o comprador poderá informar Data de Entrega, Prazo de Validade, Data de Recebimento, Contato, Transportadora, Moeda, Despesa, Desconto, Frete(Valor), o Tipo do Frete, alíquota para ICMS/ISS e/ou ICMSST. Estes dados podem ser diferentes por fornecedor e as informações contidas neste processo serão base para o calculo da melhor oferta.  
Copiar dados de outra cotação: Essa funcionalidade é utilizada para copiar os dados de orçamento de uma cotação que possua os mesmos fornecedores e produtos da cotação que está sendo criada. A opção de cópia está disponível quando a cotação está com status "Aguardando Resposta Fornecedores" e pode ser acessada ao clicar com o botão direito do mouse sobre a grid de fornecedores na aba de Orçamentos.

IdentificaçãoIdentificaçãoData de Entrega e Prazo de Entrega

Os campos Data de Entrega e Prazo de Entrega estão disponíveis na tela de registro de Orçamento.

Ao informar um valor para o campo Prazo de Entrega, a Data de Entrega será calculada automaticamente, exemplo:  
Data da Cotação: 10/06/2016  
Prazo de Entrega: 5 dias  
Data de Entrega: 15/06/2016  
Caso o usuário opte por informar a Data de Entrega, o campo Prazo de Entrega será preenchido com "-1".

Desconto, Despesa e FreteFiscalValores Financeiros

Será possivel cadastrar valores extras na tela do Registro de Orçamento, esse campo pode ser por Percentual ou Valor. Configurar em [Parâmetros - Cotação | Valores Financeiros](https://tdn.totvs.com/x/SchEGQ)

Esse valores deverão ser importados para o movimento de Ordem de Compra caso os campos estejam habilitados no movimento, de acordo com as regras abaixo:

* Cotação parametrizado com Valor Extra = Percentual  -> Movimento parametrizado com Valor Extra = Percentual ou Ambos
* Cotação parametrizado com Valor Extra = Valor  -> Movimento parametrizado com Valor Extra = Valor ou Ambos

Os valores financeiros extras configurados terão caráter apenas informativo, não influenciando os cálculos de definição do vencedor da cotação (Quadro Comparativo) nem sendo apresentados no Portal do Fornecedor.

Os valores extras de 1 a 10 estão disponíveis a partir da versão 12.1.2606.

Produtos

Na grid **Produtos** do Orçamento da Cotação temos alguns campos editaveis, são eles: 

IPI%Desconto%Condição de PagamentoAplicar em Selecionados

Ao clicar nessa opção é aplicado os valores de IPI, Desconto e Condição de Pagamento para os itens selecionados.

Aplicar nos itens

Ao clicar nessa opção é possível replicar para os itens de orçamento as informações de Data de Entrega e Prazo de Entrega.

Marca

Quando o parâmetro [Usar Marca de Produto na Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938121)estiver habilitado os campos Cód.Marca, Marca Solicitada, Marca Orçada serão exibidos na pasta Produtos.

Estes campos terão o seguinte comportamento:

* **Cód.Marca e Marca Solicitada:** exibirão o código da marca e a descrição da marca respectivamente, informados no item do movimento de solicitação de compras . Os campos são apenas para visualização.

* **Marca Orçada**: Este campo permitirá edição somente quando o perfil do usuário possuir permissão de Trocar Marca dos Produtos na Cotação. Caso o comprador deseje escolher ou trocar a marca do produto orçado ele deverá editar este campo e informar a marca.  
  ***Observações***: Não será possível informar uma marca inativa no campo Marca Orçada.

**Seleção de Marca ao utilizar agrupamento**

Caso a cotação esteja parametrizada para agrupar itens iguais pode-se utilizar o campo para seleção da marca na parte superior da aba Produtos (Registro de Orçamento/Negociação). A marca selecionada nesse campo é aplicada aos itens do orçamento selecionados ao clicar no botão "Aplicar em Selecionados". Caso seja aplicada a mesma marca a itens iguais, será realizado o agrupamento dos itens. Ao acessar esse campo sem nenhum registro selecionado são exibidas somente as marcas ativas comuns a todos itens, caso seja selecionado somente um item são exibidas para seleção todas as marcas ativas associadas a esse item no cadastro de produto.

**Restrição**

 Quando utilizada Cotação com Central de Compras não é realizado agrupamento de itens com marcas iguais.

**Alterar Marca do Produto**

Na grid de orçamentos da tela de edição da cotação, será exibido o botão Alterar Marca do Produto. Este botão irá respeitar as seguintes regras:

* **Visível**: o perfil do usuário deve possuir permissão para trocar marca na cotação e a cotação deve estar configurada para Usar Marca na Cotação (Parâmetros de Cotação).
* **Habilitado**: quando status da cotação for Composição, Aguardando Resposta Fornecedores ou Negociação da Melhor Oferta.

Será necessário selecionar pelo menos um fornecedor na grid de Orçamentos. Ao clicar no botão será aberto a janela do processo de Alterar Marca do Produto para que o usuário escolha a nova marca e selecione para quais itens serão aplicados a nova marca. Na pasta Produtos, serão apresentados os seguintes status:

* **Cotado**: o status do produto será cotado quando for inserido um valor para o campo Preço Cotado.
* **Não Cotado**: quando não foi inserido valor para o campo Preço Cotado.Não sendo considerado no cálculo do Quadro Comparativo, sendo apresentado apenas como Não cotado.
* **Não fornece**: deverá ser selecionado quando se tratar de um produto não fornecido. Não sendo considerado no cálculo do Quadro Comparativo, sendo apresentado apenas como Não Fornece.
* **Indisponível**: deverá ser selecionado quando se tratar de um produto não disponível no momento. Não sendo considerado no cálculo do Quadro Comparativo, sendo apresentado apenas como Indisponível.
* **Desqualificado:** deverá ser selecionado quando o produto não corresponder ao critérios definidos.

***Observações**:* Quando o produto tiver seu status alterado para Indisponível o preço cotado será zerado, assim como é feito com o status Não Cotado. O campo Status só pode ser alterado durante a edição de um orçamento. Para visualizar as informações do produto clique no link de Descrição do Produto.

Composição de Preço

Na grid de Registro de Orçamento será exibido o botão "Composição de Preço".

Esse recurso permite que cada produto possa ter mais de uma condição de pagamento para um mesmo fornecedor.  
Parametrizando a condição de pagamento por item, a tela de composição de preços apresentará dois botões: "Seleção Manual da Melhor Oferta" e "Cálculo Automático da Melhor Oferta" sendo suas funções respectivamente:

* **Seleção Manual da Melhor Oferta**: Será possível forçar para que a condição selecionada na grid seja considerada no cálculo da melhor oferta.
* **Cálculo Automático da Melhor Oferta**: Será calculado através das fórmulas do sistema, utilizando o mesmo recurso do cálculo do quadro comparativo.

Exemplo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Produto** | **Valor** | **Cond. Pagto Demonstrada** | **Sel. Manual da melhor oferta** |
| X | R$150,00 | A vista | A vista |
|  |  | Entrada /30/60 |  |
|  |  | 15 vezes |  |

Mesmo selecionando a pior condição de pagamento (A vista), ela será a escolhida porque a seleção manual pode forçar qualquer condição de pagamento.

|  |  |  |  |
| --- | --- | --- | --- |
| **Produto** | **Valor** | **Cond. Pagto Demonstrada** | **Cálc. Automático da melhor oferta** |
| Y | R$150,00 | A vista |  |
|  |  | Entrada /30/60 |  |
|  |  | 15 vezes | 15 vezes |

Já no cálculo automático da melhor oferta, o sistema sempre trará a melhor condição de pagamento para a cotação, utilizando o mesmo recurso do cálculo do quadro comparativo de preços.

Na visão dos **Itens** do Orçamento da Cotação existem campos padrões que podem ou não ser editados.

* **Status:** é atualizado assim que informado valor no campo Preço Cotado.
* **Cód. Produto e Descrição:** Campos informados no item do movimento de solicitação de compra.
* **Unidade Solicitada:** Unidade informado no item do movimento de solicitação de compra.
* **Quantidade Solicitada:** Quantidade informado no item do movimento de solicitação de compra.
* **Preço Cotado:** podemos informar o preço manual, pelo processo de Composição de Preço, Portal do Fornecedor e Importador por Planilha.
* **IPI**
* **Desconto e %Desconto**
* **Valor Despesa e Despesa**
* **Data Entrega**
* **Prazo Entrega**
* **Cod.Condição de Pagto**
* **Observação**
* **Motivo Desqualificação**
* **Coligada Movimento**

**Campos gerencias (Disponivel a partir da versão 12.1.2606)**

* **Valor Liberado:** Este valor será composto pela soma de todos os valores dos itens das solicitações de compras que compõem o item da cotação.
* **Preço Unitário:** Valor Liberado / Quantidade Solicitada.
* **Desvio:** O desvio é calculado com base no campo(Preço unitário - Preço Cotado). Desvio positivo:  valor do fornecedor abaixo do Preço Unitário -> **Cor Verde**  
  Desvio negativo: valor do fornecedor acima do Preço Unitário -> **Cor Vermelha**
* **Economia (%):** calculado entre o Preço Cotado e o Preço Negociado de cada item da cotação, encontrando o percentual de ganho na negociação.

No registro do Orçamento os campos que não podem ser editados são apresentados com o aspecto na cor cinza.

Anexos

Este recurso é exclusivo editar e excluir para arquivos anexados através do [Portal do Fornecedor](https://tdn.totvs.com/display/LRM/Recursos+-+Portal+do+Fornecedor).

A quantidade de arquivos em anexo, extensões de arquivos permitidas e tamanho máximo dos arquivos podem ser configuradas através dos [Parâmetros da Cotação](https://tdn.totvs.com/pages/viewpage.action?pageId=423938121#Defini%C3%A7%C3%B5esGeraisDeck-717899609) (Definições Gerais 6/6).

Campos Complementares

**A partir da versão 12.1.2606,** foi criado o Campo Complementar do Orçamento da Cotação, para saber mais [clique aqui.](https://tdn.totvs.com/x/ushEGQ)

Quadro Comparativo 

Acesso o Quadro Comparativo clicando no ícone  e para saber mais sobre, [clique aqui.](https://tdn.totvs.com/x/O8nHIw)

Vale ressaltar que é necessário clicar na botão Calcular, para que o sistema realize os cálculos e defina quem foi o vencedor da cotação.

Registrar Negociação

Uma vez registrado o orçamento não é possível alterar o valor cotado dos produtos presentes na cotação.

Para esta situação, existe o processo para alterar que seria o processo de **Registrar Negociação**, porém focando no valor negociado junto ao fornecedor, o valor utilizado para calcular a melhor oferta deixa de ser o preço cotado e passa a ser o valor negociado.

Na visão dos **Itens** do Negociação da Cotação além dos campos padrões do Orçamento, existem os campos abaixo que podem ou não ser editados.

* **Unidade Negociada:**
* **Quantidade Negociada:**
* **Preço Negociado:** É preenchido com o mesmo Preço Cotado
* **Preço Tot. Neg.:**
* **Valor Despesa Negociada e % Despesa Negociada**
* **Desconto Negociado e % Desconto Negociado**

**Campos gerencias (Disponivel a partir da versão 12.1.2606)**

* **Desvio:** O desvio é calculado com base no campo(Preço Unitário - Preço Negociado). Desvio positivo: negociou abaixo do Preço Unitário -> **Cor Verde**  
  Desvio negativo: negociou acima do Preço Unitário -> **Cor Vermelha**
* **Ecomonia (%):** é a econômia financeira obtida na compra de um produto ou serviço, calculada pela diferença do valor orçado inicial e o valor final negociado.

No registro da Negociação os campos que não podem ser editados são apresentados com o aspecto na cor cinza.

Valores Financeiros

Será possivel cadastrar valores extras na tela do Registro de Negociação, esse campo pode ser por Percentual ou Valor. Configurar em [Parâmetros - Cotação | Valores Financeiros](https://tdn.totvs.com/x/SchEGQ)

Esse valores deverão ser importados para o movimento de Ordem de Compra caso os campos estejam habilitados no movimento, de acordo com as regras abaixo:

* Cotação parametrizado com Valor Extra = Percentual  -> Movimento parametrizado com Valor Extra = Percentual ou Ambos
* Cotação parametrizado com Valor Extra = Valor  -> Movimento parametrizado com Valor Extra = Valor ou Ambos

Os valores financeiros extras configurados terão caráter apenas informativo, não influenciando os cálculos de definição do vencedor da cotação (Quadro Comparativo) nem sendo apresentados no Portal do Fornecedor.

Os valores extras de 1 a 10 estão disponíveis a partir da versão 12.1.2606.

Campos ComplementaresCampos Complemetares

Foi criado o Campo Complementar do Negociação da Cotação, para saber mais sobre, [clique aqui.](https://tdn.totvs.com/x/ushEGQ)

Alteração de Preço Cotado/Negociado:

No Registro de Orçamento ou Negociação ao selecionar um produto na grid e clicar com o botão direito do mouse é exibida a opção "Alterar Preço Cotado/Negociado".

Ao utilizar essa opção é exibida uma janela onde pode ser informado um valor ou percentual a aumentar ou diminuir no preço cotado/negociado.

Para aumentar o preço basta informar o valor ou percentual diretamente no campo, para diminuir deve-se informar o sinal de negativo  antes do valor ou do percentual, exemplo:

Produto com preço cotado/negociado de 10,00. 

Por valor: na alteração de preço cotado/negociado se for informado o valor "2,00" o preço cotado/negociado será alterado para 12,00, se for informado "-2,00" será alterado para 8,00.

Por percentual: na alteração de preço cotado/negociado se for informado o percentual "2,00%" o preço cotado/negociado será alterado para 10,02, se for informado "-2,00%" será alterado para 9,80.

Para visualizar as informações do produto, acesse a pasta Produtos e clique no link de Descrição do Produto.

Interferência

Após a geração do quadro comparativo e analise do mesmo, o comprador pode optar por não gerar as ordens de compra conforme melhor oferta, estipulando quais produtos, quantidade de produtos e para quais fornecedores serão gerados as ordens de compra. Este processo é chamado de interferência e podemos ter três tipos diferentes de interferência:

1. **Interferência Sobre Todos os Itens**: Esta opção permite que seja alterado o fornecedor para qual será gerado as ordens de compra, desconsiderando a melhor oferta calculada pelo quadro comparativo.

* + **Por Fornecedor**: Ao acessar o menu Interferência|Fornecedor no Quadro Comparativo é apresentada a tela de Interferência, onde após ser selecionado o fornecedor, são exibidos todos os produtos cotados por aquele fornecedor, não sendo permitido alteração da quantidade a ser gerada ou efetivada dos produtos (conforme utilização do parâmetro "Permite Cotação Parcialmente Gerada), ou seja, a interferência é realizada com a quantidade total de todos produtos.
  + **Por Produto**: Na Interferência por produto (Menu Interferência|Produto no Quadro Comparativo), ao selecionar o fornecedor são exibidos todos os produtos cotados pelo fornecedor, porém é possível escolher qual produto sofrerá interferência, isso é definido informado a "Quantidade a ser gerada" (conforme utilização do parâmetro "Permite Cotação Parcialmente Gerada) para cada produto.

2. **Interferência por Item**: A cada item presente no quadro comparativo se pode estipular a quantidade a ser gerada, a este processo, podemos chamar de interferência por item, para acessa-lo deve ser realizado duplo clique no item desejado no Quadro Comparativo e no Novo Quadro Comparativo.

* + Interferência no empate: Na visualização do empate, a interferência neste processo funcionará conforme a interferência sobre todos os itens. O sistema aponta o item e os fornecedores empatados e o comprador irá escolher por um deles.
  + No processo de interferência não será permitido realizar a troca de marca de produto. O campo marca negociada apresentada na grid é informativo e não pode ser alterado. Caso o comprador deseje alterar a marca do produto ele deverá utilizar o Registro de Negociação

No caso onde houve interferência na cotação, para que seja possível gerar outra(s) Ordem(ns) de Compra usando a quantidade restante dos itens, novas interferências são necessárias, apontando qual o Fornecedor desejado e a Quantidade a Ser Gerada.

Ordem de Compra

**Gerar Ordem de Compra**

Consistem em gerar a ordem de compra dos itens cotados conforme a solicitação de compra. Trata-se do ultimo processo da cotação e a geração das ordens de compra pode ser realizada integralmente ou parcialmente. Antes de gerar as ordens de compra, o comprador pode optar por alterar o tipo de movimento das ordens de compra, selecionar os itens que serão gerados ou incluir o item em uma ordem de compra já existente, desde que a cotação esteja parametrizada para este recurso.

A partir da versão 12.1.2606 os campos de Valor ou Percentual Extra (1 a 10), do registro de orçamento do Fornecedor vencedor, serão copiados para o movimento gerado caso o valor extra esteja configurado no tipo de movimento. Também os campos complementares da cotação e do orçamento serão copiados para o campo complementar de mesmo nome e tipo no movimento.

**Marca**:  
Deverá ser observado se houve a troca da marca do produto na cotação. Caso isso tenha ocorrido, a marca do item da ordem de compra deverá corresponder à marca que foi negociada na cotação.

* Quando o movimento de ordem de compra estiver parametrizado para agrupar itens repetidos será adotado o seguinte comportamento: o primeiro item a ser agrupado será utilizado como base, ou seja, os itens serão agrupados e a marca que prevalecerá será a do primeiro item.
* Ao Incluir itens em uma ordem de compra de um fornecedor já existente, os itens iguais que possuam marcas não serão agrupados, ainda que o movimento esteja parametrizado para agrupar itens repetidos.

**Data de Entrega**

Se o tipo de movimento de ordem de compras estiver parametrizado para usar Prazo de Entrega o sistema calculará a Data de Entrega do Movimento a partir da data que estiver informada no parâmetro [Data Prazo de Entrega](http://tdn.totvs.com/display/LRM/Datas), somando ao prazo de entrega do orçamento. Exemplo:

* Data Prazo de Entrega = Data de Emissão = 15/06/2016
* Prazo de Entrega do Orçamento - 5 dias
* Data de Entrega calculada no movimento = 20/06/2016

**Itens de Movimento**  
Por essa visão é possível visualizar e acessar a edição das solicitações e ordem de compras relacionadas a Cotação, pode-se acessar a edição desses movimentos por meio de duplo clique no registro apresentado.  
Para visualizar as informações do produto clique no link disponível na Descrição do Produto.

**Permite Fornecedor Trocar Marca**

Serão apresentados na visão dos Itens de Movimento, o botão e o campo Permite Fornecedor Trocar Marca, ambos com mesmo nome. Estes serão apresentados quando o perfil do usuário logado possuir permissão para Trocar Marca dos Produtos na Cotação e quando o parâmetro [Usar Marca de Produto na Cotação](http://tdn.totvs.com/pages/viewpage.action?pageId=423938121) estiver habilitado. Através desta opção será possível definir se o fornecedor poderá ou não realizar a troca da marca na cotação, nos casos em que o orçamento/negociação for enviado para o fornecedor através de planilha de exportação.  O campo, exibe por produto a informação selecionada no Assistente de Inclusão de Cotação, na etapa de filtro de produto, apenas para visualização. Ao selecionar um item e clicar no botão é possível alterar a seleção do campo, marcando ou desmarcando, caso queira permitir ou proibir que o fornecedor realize a troca de marca no orçamento/negociação por planilha.

Cancelar, Excluir ou Concluir Cotação

**Cancelar Cotação**

O sistema permite que uma cotação seja cancelada apenas quando o status da mesma for diferente de "Pedido de Compra" ou "Ordem de Compra Parcialmente Gerada", nestas situações a ação cancelar fica desabilitada e o usuário deverá cancelar a ordem de compra gerada, fazendo com que a cotação esteja apta a ser cancelada.

**Exclusão da Cotação**

Este processo tem por objetivo retirar do banco de dados cotações que não iram mais gerar ordens de compra ou que a cotação deixou de ser necessária devido a algum processo interno de sua empresa. Para que uma cotação possa ser excluída o status da mesma deve estar como "Cancelado".

**Conclusão da Cotação**

Tem por objetivo concluir os itens que não serão mais cotados. Esta opção só fica disponível caso o status da cotação seja "Ordem de compras parcialmente gerada". Ao selecioná-la, os itens que ainda estão pendentes são baixados em suas respectivas solicitações.

Repositório de Arquivos

A visão de Cotação passa a exibir a nova funcionalidade [Repositório de Arquivos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=784778828), onde poderá ser anexado arquivos na Cotação.

Na visão da cotação, existe o anexo do repositório de arquivos, que permite anexar arquivos para uma pasta previamente configurada no drive. A partir da versão 12.1.2410, os arquivos anexados aos movimentos que forem utilizados para compor uma cotação, serão copiados para o anexo do repositório de arquivos da respectiva cotação. No entanto, caso sejam anexados novos arquivos à cotação, estes não serão enviados às ordem de compra geradas, pois as cópias de arquivos entre movimentos só ocorrem dos movimentos de origem e destino, e não a partir da cotação.

A partir da versão 12.1.2410, passa a ficar disponível o anexo de Itens da Cotação, no qual poderão ser anexados arquivos ao repositório de arquivos, controlados a nível de item, e não apenas ao nível da cotação de forma geral. Os anexos associados aos itens dos movimentos de origem que forem utilizados para compor uma cotação, serão copiados para os itens correspondentes da cotação através deste novo recurso. Porém, assim como citado anteriormente, as cópias de arquivos entre itens de movimentos só ocorrem dos movimentos de origem e destino, e não a partir da cotação. Por isso, caso novos arquivos sejam anexados aos itens da cotação, estes não serão copiados para as ordens de compra geradas a partir da cotação.

---

Cotação Integrada com Paradigma

* [Pré-Requisitos](http://tdn.totvs.com/pages/viewpage.action?pageId=423937972)
