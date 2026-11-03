---
content_hash: f7204d680279bcdc7bf479ae12d4093173fffa5c9a6b212dc0b1594c573abf1a
fetched_at: '2026-06-29T00:09:29.308924+00:00'
page_id: '423938872'
product: rm
source: tdn-rm
title: Recebimento Automático de NF-e
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938872
version: 14
---

O Recebimento NF-e Automático permite a importação automática das notas fiscais eletrônicas, através do processo do TOTVS Colaboração 2.0.   
Assim que o XML é processado, através do Serviço Totvs Colaboração Consulta o movimento é incluído.   
O atual processo responsável pelo recebimento da NF-e, exige a intervenção manual do usuário para resolver alguns conflitos, tais como, tradução dos produtos, seleção da natureza de operação, entre outros.   
A fim de simplificar este processo, foi implementado o recebimento automático da NF-e, o qual será capaz de solucionar todas estas questões, mediante uma prévia configuração, sendo que todas as validações/consistências executadas na criação manual do movimento serão também executadas no recebimento e criação automática da NF-e.  
O Recebimento Automático da NF-e está disponível apenas para o TOTVS Colaboração 2.0, mas as melhorias de performance e na usabilidade das telas também estão disponíveis para o TOTVS Colaboração 1.0.  
Para correto funcionamento da rotina de Recebimento Automático das NF-e é necessário que sejam executadas algumas parametrizações, que são:

* Tipo de Movimento para Recebimento Automático de NF-e;
* Natureza Fiscal e Natureza Inversa;
* Código do Produto no Fornecedor;
* Unidade de Medida do Produto no Fornecedor.

No processo de Recebimento Automático de NFe é necessário executar os seguintes procedimentos:

* Importação de Arquivos XML,
* e Serviço de Consulta de Arquivos XML.

O Serviço Totvs Colaboração Consulta é um Job responsável por validar o arquivo XML do documento enviado, de acordo com o tipo de documento em questão (CT-e, NF-e, NFS-e, etc.), através da chamada do serviço especifico para cada um deles.   
No caso do recebimento o sistema irá executar a 'Fórmula do Tipo de Movimento para Recebimento Automático de NFe' comparando-a com os dados do XML para verificar qual o tipo de movimento a ser utilizado na entrada automática da NF-e.   
Após encontrar o tipo de movimento a ser incluído o sistema passará à Tradução dos Dados do Arquivo XML.  
Caso através dessa fórmula para algum XML não seja possível definir o seu tipo de movimento esse XML será criado na base de dados com o status 'Inconsistente'.   
Para verificar o erro ocorrido, basta um duplo clique no registro para que seja exibido o seu Log onde o problema será demonstrado.   
Quando o arquivo está Inconsistente, é necessário corrigir a causa do erro para poder tentar incluí-lo no sistema.   
Após a correção do erro basta alterar o seu status para 'Pendente', através do processo Alterar Status do Arquivo e o Job tentará recebê-lo automaticamente novamente em sua próxima execução.   
Caso opte por não acertar o erro e receber o XML manualmente, o registro 'Inconsistente' deverá ser manualmente excluído da tela de "Importação de Arquivo XML".  
Depois de efetuar a tradução dos dados do XML o sistema verifica se há informação do Número do Pedido no Fornecedor.   
Assim, caso a tag xPed (Número do Pedido no Fornecedor) do XML esteja preenchida e exista na base de dados um pedido correspondente, o mesmo será selecionado, para realização do faturamento.   
Caso contrário, o sistema buscará por um pedido de compra com status pendente, emitido para o CNPJ do fornecedor e que seja um 'espelho' da NF-e em questão para realizar o faturamento.   
Se, de acordo com a regra acima, o sistema identificar mais de um registro, nenhum pedido será selecionado.  
Após verificar se o Número do Pedido no Fornecedor consta do XML o sistema irá identificar o Tipo de Recebimento NF-e a ser praticado para cada NF-e, pois dependendo do tipo o comportamento na inclusão é diferente.   
Para isso o sistema irá verificar se o emitente da mesma consta na tabela Definições de Cli/For - Importação de Arquivo XML e em caso positivo será utilizado o tipo de recebimento ali definido.   
Caso o emitente não conste nessa tabela o sistema irá utilizar o Tipo de Recebimento definido para a filial para a qual a NF-e foi emitida.  
Quando o tipo de recebimento é Inclusão Direta - status não processado ou Tipo de Recebimento de NF-e: Recebimento de pedido ou inclusão direta - status não processado ao incluir automaticamente o movimento, o status do mesmo ficará como Não processado e não serão geradas rotinas como financeiro, contábil e aprovação por workflow.   
Assim o usuário será obrigado a conferir o movimentos incluídos automaticamente. Para alterar o status e gerar as rotinas basta executar o processo Processar Movimento.

---

* [Produtos para Importação de XML (Estoque, Compras e Faturamento)](http://tdn.totvs.com/pages/viewpage.action?pageId=423938818)

Informações Adicionais

* # [Inclusão de Movimento através de XML (NF-e)](http://tdn.totvs.com/pages/viewpage.action?pageId=423937956)
* [Documento Técnico - Recebimento de NF-e](http://tdn.totvs.com/pages/releaseview.action?pageId=223159982)
