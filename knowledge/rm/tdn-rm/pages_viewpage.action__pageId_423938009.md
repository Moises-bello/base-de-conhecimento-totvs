---
content_hash: 080ce2783786e2a987011006179d1ae8f34379ebcaadd615ab97275f293db398
fetched_at: '2026-06-29T00:09:24.729349+00:00'
page_id: '423938009'
product: rm
source: tdn-rm
title: Exportação/Importação de Cotação via planilha Excel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938009
version: 27
---

O processo de exportação/importação de Cotação via planilha Excel visa agilizar o registro de Orçamento ou Negociação na Cotação. É possível enviar o pedido de Orçamento por planilha Excel para vários fornecedores e posteriormente importar todas planilhas devolvidas para registro dos orçamentos através de um único processo.

**Envio/Exportação da Planilha de Pedido do Orçamento**

Em Compras e Faturamento | Compras | Cotação ao utilizar o processo Comunicar Fornecedores, na tela de Seleção dos Principais Parâmetros, deverá ser utilizado o Tipo de Comunicação | Enviar orçamento via e-mail.  
Ao selecionar este tipo de envio, o usuário pode informar qual relatório e/ou planilha ele deseja utilizar para o envio do e-mail.   
É obrigatória a seleção de um relatório ou planilha, sendo possível o envio de ambos.  
Caso seja informada um modelo de planilha, também deverá ser informado qual o tipo de exportação a ser feito (Orçamento ou Negociação), desta forma o sistema irá realizar a exportação dos pedidos de orçamento e enviará uma planilha com essas informações no anexo do e-mail.  
***Observações***: Não é permitido o envio de negociação sem antes um registro de orçamento.  
O nome da planilha Excel enviada ao fornecedor é formado por: [Nome da Planilha Net no sistema] + [Código da Cotação] + [Código do Fornecedor] + [Tipo da Cotação(Orçamento/Negociação)].

**Planilha Net Modelo**

Um modelo de Planilha Net com as configurações padrões está disponível para utilização. Para importar a Planilha Net de modelo é necessário realizar a importação da Planilha "NUCPLA0003 - Exportação de Cotação.PlanNetTotvs" (Menu Gestão | Planilha Net | Importação de Planilha.NET).   
A Planilha se encontra disponível na Pasta C:\Totvs\CorporeRM\ObjetosGerenciais\Planilha (Caminho padrão de instalação da Biblioteca RM, que pode ser alterado conforme necessidade no momento da instalação).  
É possível customizar a planilha de modelo padrão conforme necessidade, desde que sejam mantidos os campos obrigatórios da planilha.  
Os campos da planilha que serão exibidos para os fornecedores ao enviar a planilha sofrerão alteração conforme a parametrização do sistema.   
Sendo assim, campos serão ocultos e/ou exibidos em diferentes abas.  
No momento em que o processo de Comunicar Fornecedores for executado, o sistema irá preencher a planilha com os dados relacionados a orçamento ou negociação, e fazer o envio da mesma no anexo do e-mail em formato Excel (.xlsx) para cada fornecedor.

**Planilha Excel de Pedido de Orçamento**

Ao receber a planilha Excel de Pedido de Orçamento via e-mail, o fornecedor irá visualizar as seguintes Abas e Campos na planilha:

**Aba COTACAO**

Campos referentes aos dados do Pedido:

* Nome da Empresa
* CNPJ da Empresa
* Endereço da Empresa
* Telefone de Contato da Empresa
* E-mail de Contato da Empresa
* Código da Cotação [Campo Obrigatório]
* Data do Pedido
* Data Limite de Resposta [Campo Obrigatório]
* Comprador

Campos referentes aos dados do Fornecedor:

* Fornecedor [Campo Obrigatório]
* CNPJ do Fornecedor
* Contato do Fornecedor
* Telefone do Contato do Fornecedor
* E-mail do Contato do Fornecedor
* Observação: Todos os campos referentes aos dados do Pedido e do Fornecedor são bloqueados para edição, não sendo possível sua alteração pelo fornecedor.

**Aba ITENS****ORÇAMENTO**

Campos referentes ao registro de Orçamento:

* Identificador do Movimento [Campo Obrigatório]: Campo bloqueado e não editável.
* Coligada Movimento [Campo Obrigatório] Campo bloqueado e não editável.
* Sequencial do Item [Campo Obrigatório]: Campo bloqueado e não editável.
* Produto: campo bloqueado e não editável.
* Descrição do Produto: campo bloqueado e não editável.
* Unidade [Campo Obrigatório]: campo bloqueado e não editável.
* Unidade Orçada: Este campo será exibido caso o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Permite alterar unidade de cotação) esteja marcado. Será permitido informar somente unidades cadastradas no sistema e que sejam compatíveis com a unidade que foi solicitada.
* Quantidade Solicitada [Campo Obrigatório]: campo bloqueado e não editável. Caso o fornecedor altere a Unidade Orçada, no momento da importação, a conversão de unidade será realizada e o valor da quantidade atualizado.
* Quantidade Orçada [Campo Obrigatório]: campo bloqueado e não editável. Será exibido apenas na Negociação.
* Condição de Pagamento [Campo Obrigatório]: se a parametrização estiver por item (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Condição de Pagamento), será habilitada a aba “COND\_PAGT\_ITENS” para que estes dados sejam informados. Nesta aba o usuário deverá copiar o ID Movimento, Coligada Movimento e Sequencial do Item obrigatoriamente (outros dados poderão ser copiados pelo fornecedor, para ajudá-lo na hora do preenchimento) e informar, por linha, a condição de pagamento para aquele item.
* Preço Unitário [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor.
* Valor Total [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar preço total no item) estiver desmarcado, ele não será exibido. Também não será exibido esse campo caso esteja marcado o parâmetro "Permite Alterar Unidade Orçada".
* Moeda [Campo Obrigatório]: será exibido conforme parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Moeda). O campo terá o valor da moeda padrão do sistema, sendo possível a alteração da mesma pelo fornecedor.
* IPI (%) [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar Tributo no Item de Orçamento (IPI)) estiver desmarcado, ele não será exibido. Este campo será preenchido com a informação que está na base de dados.
* ICMS (%) [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar ICMS no Item de Orçamento) estiver desmarcado, ele não será exibido. Este campo será preenchido com a informação que está na base de dados.
* ICMSST (%) [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar ICMS no Item de Orçamento) estiver desmarcado, ele não será exibido.
* Margem de Lucro ICMSST [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar ICMS no Item de Orçamento) estiver desmarcado, ele não será exibido.
* Desconto [Campo Obrigatório]: Pode ser valor ou porcentagem, de acordo com a parametrização (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa desconto no item de orçamento). Esse dado pode ser omitido pelo fornecedor.
* Despesa [Campo Obrigatório]: Pode ser valor ou porcentagem, de acordo com a parametrização. Se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 2/2 | Usa despesa no item de orçamento) estiver desmarcado, ele não será exibido. Esse dado pode ser omitido pelo fornecedor.
* Data Entrega: Este campo será preenchido com a Data Limite para Entrega, que é preenchido no processo de criar a Cotação.

***Observação***: Serão carregadas as informações que estão no item da cotação. Campo para preenchimento de dados adicionais sobre o orçamento do item.

* Indisponível: Deve ser informado "Sim" ou "Não" de acordo com a disponibilidade do produto pelo Fornecedor.
* Marca Solicitada: Campo bloqueado e não editável apresentado caso o parâmetro "Usar Marca de Produto na Cotação" estiver habilitado nos parâmetros de Cotação.

Campos referentes ao registro de Negociação

* Unidade Negociada [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Este campo será exibido caso o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Permite alterar unidade de cotação) esteja marcado. Será permitido informar somente unidades cadastradas no sistema e que sejam compatíveis com a unidade que foi solicitada.
* Quantidade Negociada [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Campo bloqueado e não editável. Caso o fornecedor altere a Unidade Negociada, no momento da importação, a conversão de unidade será realizada e o valor da quantidade atualizado.
* Condição de Pagamento Negociada [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Se a parametrização (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Condição de Pagamento) estiver por item, haverá uma aba para que estes dados sejam informados. Nesta aba o usuário deverá copiar o ID Movimento, Coligada Movimento e Sequencial do Item obrigatoriamente (outros dados poderão ser copiados pelo fornecedor, para ajudá-lo na hora do preenchimento) e informar, por linha, a condição de pagamento para aquele item.
* Preço Unitário Negociado [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor.
* Valor Total Negociado [Campo Obrigatório]: esse dado pode ser omitido pelo fornecedor. Se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar preço total no item) estiver desmarcado, ele não será exibido. Também não será exibido esse campo caso esteja marcado o parâmetro "Permite Alterar Unidade Orçada".
* Desconto Negociado [Campo Obrigatório]: Pode ser valor ou porcentagem, de acordo com a parametrização (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa desconto no item de orçamento). Esse dado pode ser omitido pelo fornecedor.
* Despesa Negociada [Campo Obrigatório]: Pode ser valor ou porcentagem, de acordo com a parametrização. Se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa despesa no item de orçamento) estiver desmarcado, ele não será exibido. Esse dado pode ser omitido pelo fornecedor.

***Observação***: o sistema exibe os itens iguais agrupados na planilha, conforme a parametrização de agrupamento de itens iguais na cotação (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Movimento 1/2 | Não agrupa itens iguais na cotação).

**Aba****ORÇAMENTO**

* ICMS/ISS (%): será exibido conforme parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usa Tributo no Orçamento (ICMS/ISS)). Esse dado pode ser omitido pelo fornecedor.
* ICMSST (%): esse dado pode ser omitido pelo fornecedor. (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usa Tributo no Orçamento (ICMS/ISS))
* Número Doc. Fornecedor
* Moeda: será exibido conforme parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Moeda). O campo terá o valor da moeda padrão do sistema, sendo possível a alteração da mesma pelo fornecedor.
* Condição de Pagamento [Campo Obrigatório]: se a parametrização (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 1/4 | Condição de Pagamento) estiver por orçamento, será exibida essa coluna.
* Frete: se o parâmetro (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Definições Gerais 2/4 | Usar Valor do Frete) estiver marcado, será por valor, caso não esteja, será por %. Esse dado pode ser omitido pelo fornecedor.
* Tipo de Frete: esse dado pode ser omitido pelo fornecedor.
* Transportadora: esse dado pode ser omitido pelo fornecedor.
* Desconto: Pode ser valor ou porcentagem, de acordo com a parametrização (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa desconto no orçamento). Esse dado pode ser omitido pelo fornecedor.
* Desconto Negociado: Pode ser valor ou porcentagem, de acordo com a parametrização (Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Orçamento 1/2 | Usa desconto no orçamento). Esse dado pode ser omitido pelo fornecedor.
* Despesa: Por valor. Esse dado pode ser omitido pelo fornecedor.
* Prazo Validade (dias).
* Prazo de Entrega (dias): O valor informado pelo Fornecedor nesse campo, ao realizar a importação da planilha, será somado a Data da Cotação, resultando assim a Data de Entrega do Orçamento. [Campo Obrigatório]

***Importante!*** Os campos definidos como “[Campo Obrigatório]” sempre devem existir na planilha, pois são campos chaves para o processo de importação de preços orçados, ou seja, mesmo se não houver necessidade do fornecedor informar dados nesses campos, eles devem existir vazios na planilha.

Os demais campos são opcionais e podem ser estruturados conforme necessidade.  
Observação: Todos os campos da planilha de orçamento ou negociação terão valores defaults de acordo com o que existe no sistema.

Colunas com Listas de Dados

* Os dados de algumas colunas são dados predefinidos vindos do sistema, evitando assim possíveis erros no momento da digitação pelo fornecedor. As colunas com dados predefinidos são:
* Transportadora: é exibida uma lista de transportadoras cadastradas no sistema.
* Moeda: é exibida uma lista com as moedas cadastradas no sistema.
* Tipo de Frete: é exibida uma lista com os tipos de frente existentes no sistema.
* Condição de Pagamento: é exibida uma lista com as condições de pagamento cadastradas no sistema.
* Unidade de Medida: é exibida uma lista com as unidades de medida cadastradas no sistema.
* Indisponível: são exibidas as opções "Sim" ou "Não".
* Marca Solicitada: são exibidas todas as marcas ativas associadas ao produto (apresentado caso o parâmetro "Usar Marca de Produto na Cotação" estiver habilitado nos parâmetros de Cotação).
* Marca Negociada: são exibidas todas as marcas ativas associadas ao produto (apresentado caso o parâmetro "Usar Marca de Produto na Cotação" estiver habilitado nos parâmetros de Cotação).

**Importação da Planilha de Pedido do Orçamento (versão 12.1.27 e anteriores)**

Pelo menu Compras e Faturamento | Compras | Cotação | Processos | Importar Planilha de Orçamento/Negociação é possível realizar a importação da(s) planilha(s) devolvida(s) pelo(s) fornecedor(eres).

Ao acessar esse processo é exibida a etapa de Seleção de Conceito, na qual é necessário selecionar o Conceito "CONMOV0006 - Importação de Cotação". Esse conceito deve ser importado através do modulo Integração | Conceito | Processos | Importar Conceito. O conceito está disponível na Pasta C:\Totvs\CorporeRM\ObjetosGerenciais\Conceito (Caminho padrão de instalação da Biblioteca RM, que pode ser alterado conforme necessidade no momento da instalação).

Importante! O conceito disponibilizado já se encontra com as ligações padrões prontas de acordo com a planilha net modelo disponibilizada, então caso a planilha seja customizada com campos diferentes, será necessário editar o conceito e fazer a ligação dos novos campos, lembrando que o parâmetro "Não agrupar itens iguais na cotação" deverá estar habilitado.

Na etapa seguinte a Seleção do Conceito deve-se informar o diretório onde estão salvas as planilhas devolvidas pelos fornecedores. É possível importar uma ou mais planilhas de orçamento/negociação ao mesmo tempo, para isso basta que todas planilhas estejam na mesma pasta (informada na escolha do diretório).

Para agilizar a importação das planilhas, pode-se agendar jobs para execução do processo de importação de cotação de forma automática. Visando facilitar esse processo após realizar o processo de importação, as planilhas processadas serão renomeadas com o ID do Job executado, permitindo assim a identificação do job que processou a planilha para posterior verificação do log de importação.

A renomeação das planilhas também impede que na próxima execução do processo de importação a mesma planilha seja processada novamente, entretanto, caso seja necessário importar a mesma planilha novamente basta renomear a mesma com o final .xlsx.  
Atenção! Para realização do processo de importação da planilha em um máquina que não possua o MS Office instalado é necessária a instalação do componente Microsoft Access 2013 Runtime, esse componente pode ser baixado gratuitamente no site da Microsoft clicando aqui.

Recurso removido do sistema na versão 12.1.2306 e posteriores.

A partir da 12.1.2306 deve-se utilizar o processo **Importar Planilha de Orçamento/Negociação (Novo!)**

**Novo processo (versão 12.1.28 e próximas) - Importar Planilha de Orçamento/Negociação (Novo!)**

O novo processo pode ser localizado no mesmo menu citado no tópico anterior, com o nome de "Importar Planilha de Orçamento/Negociação (Novo!)".

Para esta opção, não será mais necessária a utilização de um conceito, bastando apenas a parametrização de um caminho padrão de onde as planilhas serão buscadas para importação. Este parâmetro pode ser encontrado em: Parâmetros | Gestão de Estoque, Compras e Faturamento | Gestão Compras | Cotação | Etapa 3 - Definições Gerais 3/5 | Grupo 'Importação de Planilha'. **Observação:**este parâmetro indica apenas um caminho padrão que será buscado de acordo com a Coligada atual (contexto) e pode ser alterado antes da execução do processo.

***Importante!***

1. Ao contrário do método antigo, este novo processo não renomeia as planilhas após sua execução (independente se apresentou sucesso ou falha). Desta forma, a fim de evitar novas importações desnecessárias, deve-se alterar o local dos arquivos desejados manualmente. Lembrando também que, esse novo processo já contempla o conceito de agrupamento de itens na cotação.

* [Importar Planilha de Orçamento/Negociação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019491211-RM-CMP-Importar-Planilha-de-Or%C3%A7amento-Negocia%C3%A7%C3%A3o)
* [Edição do Conceito de Importação de Cotação ao alterar Nome da Marca](http://tdn.totvs.com/pages/viewpage.action?pageId=423938197)
