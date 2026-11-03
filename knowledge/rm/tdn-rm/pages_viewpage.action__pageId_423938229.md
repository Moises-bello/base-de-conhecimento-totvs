---
content_hash: 41b52716080c18f413ba2c5c2a71799214a39ae4734c74627ddc322674ea3797
fetched_at: '2026-06-29T00:09:26.044555+00:00'
page_id: '423938229'
product: rm
source: tdn-rm
title: Cadastros Integração ERP TOTVS X Portal de Compras Paradigma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938229
version: 13
---

**Objetivo**

Permitir que o usuário realize a sincronização dos cadastros necessários para a integração do ERP TOTVS (linha RM), com o Portal de Compras Paradigma (WBC - Web Business Center).   
A integração dos cadastros sempre irá ocorrer no sentido ERP TOTVS para Paradigma quando ocorrer as ações de inclusão ou alteração de registros ou quando for executada a carga inicial.  
Os cadastros integrados são:

* Coligada
* Filial
* Unidade de Medida
* Moeda
* Condição de Pagamento
* Centro de Custo
* Departamento
* Fornecedor
* Categoria de Produto
* Produto
* Produto x Fornecedor
* Usuário
* Categoria x Fornecedor

Ao realizar um novo cadastro ou altera-lo no ERP TOTVS o mesmo será sincronizados para o Portal de Compras Paradigma (WBC - Web Business Center) automaticamente desde que o ERP esteja parametrizado para integrar com o portal Paradigma.  
***Observação***: Os cadastros Coligada, Filial, Transportadora e Fornecedor, serão gravados como empresa no portal de compras paradigma. Os demais cadastros terão o seu próprio menu dentro do portal.

**Fornecedores**: Caso o sincronismo não tenha sido realizado, o comportamento será o seguinte:

Quando parametrizado no Gestão Financeira, na etapa "Parâmetros Gerais do Cliente/Fornecedor", para CPF e/ou CNPJ Único. 

* Fornecedor cadastrado no RM (CNPJ ou CPF) e que ainda não possui DE/PARA:  Caso o Fornecedor seja o vencedor, será realizado o vinculo automaticamente entre o WBC e ERP TOTVS;

Quando **NÃO** parametrizado no Gestão Financeira, na etapa "Parâmetros Gerais do Cliente / Fornecedor", para CPF e/ou CNPJ Único.

* Fornecedor cadastrado no RM ((CNPJ ou CPF)) e que ainda não possui DE/PARA: Caso o Fornecedor seja o vencedor, será cadastrado um novo fornecedor no ERP TOTVS, uma vez que, com esta parametrização, permite cadastrar mais de um CLIENTE/FORNECEDOR com mesmo CPF/CNPJ. Caso possua esta parametrização e não deseje que seja criado um novo registro, sugerimos que realize o processo de SINCRONISMO para o Fornecedor em questão.

Em ambas as parametrizações, caso não possua registro do CPF/CNPJ do fornecedor, no ERP TOTVS, o cadastro e DE/PARA serão realizados automaticamente.

**Produto**: Quando o sistema estiver parametrizado com a opção de Máscara de Produto "Controla Níveis de Máscara" acessando Parâmetros Gerais | Tabelas | Produtos | Definições Gerais, somente poderão ser integrados ao Portal de Compras Paradigma produtos definidos como de Último Nível.

**Exclusão**: Registros integrados com o Paradigma não poderão ser excluídos no ERP TOTVS, assim se houver uma tentativa de exclusão de algum registro já sincronizado com o portal Paradigma o sistema irá exibir uma mensagem informando que o mesmo está sincronizado com o portal e não poderá ser excluído.

**Fórmulas Visuais**: A sincronização entre o ERP TOVS e o Portal Paradigma é realizada pela fórmula visual, sendo assim as mesmas deverão ser importadas, uma para cada cadastro, para que a sincronização funcione corretamente.  
Para importar as fórmulas será necessário acessar o módulo TOTVS Gestão de Estoque, Compras e Faturamento | Gestão | Fórmulas Visuais.  
  
**Parametrização**

Para que a integração possa ser utilizada, a mesma deverá estar ativa dentro do ERP TOTVS.   
Para parametrizar a integração é necessário:   
Acessar o módulo TOTVS Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Integrações | Paradigma , e marcar a flag "Integrado com Paradigma" e configurar o caminho do WebService onde se encontra o servidor do paradigma.  
Acessar TOTVS Gestão de Estoque, Compras e Faturamento | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | Parâmetros Gerais | Tabelas, ao acessar a tela vá em Classificação e no campo Tipo de Produto fornecido pelo fornecedor, marcar a tabela de classificação do produto que será usada como categoria do Produto.

**Carga Inicial**

Utilizando a carga inicial o usuário terá a opção de sincronizar os registros que já estão na base de dados do ERP TOTVS. Na tela de Carga Inicial o usuário tem acesso às seguintes opções:

1. **Sincronizar todos os registros**: Esta opção sincroniza todos os registros do cadastro selecionado.
2. **Somente os não enviados**: Esta opção sincroniza apenas os registros que não foram sincronizados com o Portal Paradigma, manualmente ou em uma carga inicial anterior.
3. **Selecionar Registros**: Esta opção permite ao usuário selecionar apenas os registros que ele deseja sincronizar.

Marcando a opção "Interrompe Integração em caso de erro", em caso de ocorrer erro na sincronização de algum registro, o processo é interrompido e nenhum registro é enviado, já deixando essa opção desmarcada, se ocorrer erro em algum registro todos os outros são sincronizados exceto o registro que apresentou problema.A carga inicial pode ser acessada no módulo TOTVS Gestão de Estoque, Compras e Faturamento | Integrações | Carga inicial

***Importante!*** O processo de Carga Inicial poderá ser agendado.
