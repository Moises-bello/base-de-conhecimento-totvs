---
content_hash: 2c4e7e262845ad9440776f88f3fd9b479a2552a452d3294d6c07bacf320880db
fetched_at: '2026-06-29T00:09:36.139466+00:00'
page_id: '425459473'
product: rm
source: tdn-rm
title: Conteúdo Geral Backoffice Protheus - Produto Global
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459473
version: 3
---

**Produto Global**

---

Um dos cadastros que a integração TOTVS Obras e Projetos (TOP) x BackOffice Protheus contempla é o cadastro de Produto, sendo este considerado local. Ou seja, um produto só está disponível na Empresa/Coligada na qual ele foi cadastrado/sincronizado.  
    
 A partir da versão 11.50 é possível transformar o produto em um produto global. Desta forma o produto estará disponível em todas as Empresas/Coligadas, independente de qual ele tenha sido cadastrado. Para isso é necessário realizar algumas configurações.   
    
 No lado RM é necessário apenas rodar um update na base de dados. Embora os produtos que já estavam cadastrados estejam visíveis os mesmos não poderão ser utilizados, pois foram cadastrados como produto local.  
    
 Do lado Protheus deverá ser configurado o compartilhamento do produto entre as empresas existentes. Existem dois cenários para realizar esta configuração: O primeiro é quando o Protheus utiliza o conceito de Empresa/Filial, e o segundo quando utiliza o conceito de Grupo de Empresas.  
    
    
 **Empresa/Filial**  
    
    
   
    
 **(1)** Antes de realizar o compartilhamento, cada empresa possui uma tabela de produto, e todas as filiais dentro dessa empresa apontam para essa tabela. É nessa tabela que os registros dos produtos são salvos. Cada um possui uma chave onde é informado dentre outras coisas a filial onde ele foi cadastrado e o código do produto.  
    
 ***Nota:*** *a chave apresentada na figura é apenas para ilustração do exemplo, sendo F representando a Filial e P representando o código do Produto.*   
    
 **(2)** O primeiro passo para que os produtos sejam globais é escolher uma tabela de produto como principal, e após fazer com que todas as filiais de todas as empresas apontem para ela.   
    
 As demais tabelas continuarão existindo mas sem nenhuma filial apontando para elas. Isso fará com que não seja possível visualizar ou utilizar os produtos cadastrados exclusivamente para cada filial. Os produtos que foram cadastrados na tabela selecionada poderão ser visualizados se esta for acessada com a empresa correspondente. Mas é importante entender que eles não poderão ser utilizados.  
    
 ***Nota: Nenhum*** *dos produtos cadastrados antes do compartilhamento poderão ser utilizados como produtos globais. Isso porque as configurações não transformam os produtos que já existem na base de dados em produtos globais*.  
    
    
   
    
 **(3)** O segundo passo é realizar o compartilhamento da tabela de produto selecionada para as demais filiais. Essa alteração é realizada no Dicionário de Dados no Protheus. É necessário fazer este procedimento em todas as filiais.   
    
 Realizada a configuração, todos os produtos cadastrados a partir de agora passam a ser enxergados por todas as filiais.   
 O registro do produto é salvo na tabela sem ter a informação da filial na chave, permitindo assim que ele seja global.   
    
 ***Nota:*** *Importante observar que estes produtos serão salvos na tabela escolhida anteriormente (no exemplo, Tabela Produto da Empresa A).*   
    
 **(4)** Caso sejam desfeitas as configurações, voltando o produto para local, todos os produtos globais cadastrados não poderão mais ser visualizados e nem utilizados. Os demais produtos que já existiam na base serão utilizados normalmente como produtos locais.  
    
    
    
 **Grupo de Empresas**  
    
    
   
    
 **(1)** No cenário de Grupo de Empresas existe uma tabela de produto para cada Grupo, e todas as filiais (independente da Empresa ou Unidade de Negócio) utilizam a mesma tabela. Cada produto cadastrado possui na chave a informação de qual filial ele pertence, fazendo assim com que ele seja visualizado apenas na filial onde foi cadastrado.   
    
 ***Nota:*** *a chave apresentada na figura é apenas para ilustração do exemplo, sendo F representando a Filial e P representando o código do Produto.*   
    
 **(2)** Para que o produto seja global é necessário realizar o compartilhamento do produto no Dicionário de Dados no Protheus. É necessário fazer este procedimento para todas as filiais.   
    
 Realizada a configuração, os produtos antigos continuam na tabela mas não poderão mais ser visualizados nem utilizados.   
    
    
   
    
 **(3)** Todos os produtos cadastrados a partir de agora não terão a informação da filial na chave. Dessa forma, serão vistos por todas as filiais, tornando-se um produto global.  
    
 **(4)** Desfazendo as configurações, os produtos antigos voltam a ser utilizados por suas respectivas filiais, mas os que foram cadastrados como globais não poderão ser visualizados e nem utilizados. Isso porque a chave do produto volta a ter a informação da filial, e os produtos globais não possuem a informação da filial.   
    
 **Atenção:**

Caso o cenário tenha mais de um Grupo de Empresas será necessário alterar primeiro o apontamento das filiais para uma mesma tabela, para depois realizar o compartilhamento no Dicionário de Dados. O procedimento neste caso será o mesmo que foi realizado no cénario Empresa/Filial.

---

Recursos Adicionais

[Boletim Técnico - Produto Global](http://tdn.totvs.com/download/attachments/82477574/Produto+Global+-+Boletim+T%c3%a9cnico.pdf?version=1&modificationDate=1381255613171)
