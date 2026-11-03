---
content_hash: 68b256da7edeee612d945a7d9f4a6b73162d988decd570d8b69a16d65202586b
fetched_at: '2026-06-29T00:08:11.285962+00:00'
page_id: '242388956'
product: rm
source: tdn-rm
title: DT_Totvs_Business_Analytics
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Totvs_Business_Analytics
version: 110
---

# Totvs Business Analytics

 

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Educacional / Construção e Projetos |
| **Módulo:** | Integração |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cadastro do plano de extração | Cadastro do plano de extração | | Processo de execução do plano de extração | Processo de execução do plano de extração | | Histórico de Execução do plano de Extração | Histórico de Execução do plano de Extração | | Log de envio dos dados para o Totvs Smart Analytics | Log de envio dos dados para o Totvs Smart Analytics | |
| **Parâmetro(s):** | Parâmetros de extração por Área   * **Área Contábil** * **Área Financeira** * **Área Comercial e Materiais** * **Recurso Humanos** |
| **Requisito (ISSUE):** | TVAMQF / TVADKE |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas Utilizadas:** | *HCPLANO, HCPLANOITEM, HCPLANOHIST, HCLOGAGENT* |

# Descrição

O Totvs Smart Analytics é uma solução de inteligência de negócios, desenvolvida especificamente para empresas usuárias do ERP Totvs e contem conectores nativos para todas as linhas de produto. As informações abaixo são voltadas para o ERP Totvs da linha RM.

# Procedimento para Configuração

 A configuração da integração do TOTVS Business Analyticsproporciona aos clientes que importem todos os Conceitos a serem utilizados na integração fazendo uso de um recurso rápido e prático. O preenchimento da Stage Area irá acontecer via Conceitos. Para importar os mesmos o cliente irá entrar na visão de Configurar, apontar o diretório onde se localizam os Conceitos, preencher a conexão de Destino que será utilizada para configurar todos os Conceitos e concluir a importação. Abaixo segue mais detalhes da visão de Configurar:

Diretórios Conceitos: Apontar onde estão localizados os Conceitos de usoexclusivo para esta integração.Não importar Conceitos: Ao marcar esta opção o usuário está abstraindo de importar os conceitos, esta opção tem o intuito exclusivamente de atualizar as Views e as tabelas da Stage Area, é importante destacar que os conceitos já importados não serão alterados. Nos dados de configuração do banco de dados do BI, o usuário deve informar os dados da base referente a Stage Area, evitando assim que sejam criadas ou atualizadas as tabelas da Stage Area em outro banco.  
  
Vale ressaltar que quando está opção estiver desmarcada os Conceitos não serão duplicados e sim substituídos.

*Observação*: Para os usuários que não importaram os conceitos é obrigatórioa importação pela primeira vez.

Configurações do Banco de Dados RM:

Neste contexto são exibidos os parâmetros de configuração da base de dados da Linha RM, que são:

* + Tipo (Driver)
  + Nome do servidor
  + Nome do Banco
  + Usuário
  + Senha

Configurações do Banco de Dados do BI:

Tipo (Driver): Informar o tipo de banco de dados do BI. Pode ser selecionado Sqlserver ou Oracle.  
  
Banco de dados do tipo Sqlserver:

* + Nome do Servidor: Informar o nome ou endereço IP, onde está hospedado o banco de dados do BI.
  + Nome do banco: Informar a database que será utilizada pela integração.

Banco de dados do tipo Oracle:  

* Base de dados: Informar o Alias de conexão a base de dados Oracle.
* Usuário: Informar usuário.
* Senha: Informar senha do usuário.
* Testar Conexão: Recurso que autentica os dados de conexão.

Ao concluir a Configuração, a aplicação irá importar todos os Conceitos, tomando como base a conexão de destino informada na visão de “Configurar”. Também serão excluídas/criadas as Views na conexão de Origem e as tabelas referente a Stage Area na conexão de Destino.

É importante destacar que quando este processo de importação de Conceitos acontecer novamente, a aplicação irá substituir todos os Conceitos (Não serão duplicados os Conceitos).

Desta maneira, caso seja customizado algum Conceito relacionado à Integração TOTVS Business Analytics, é necessário que seja realizado o backup e o mesmo deve ser movido para o diretório onde serão importados. Além de realizar todas as parametrizações, a visão também cria as Views e as tabelas da Stage Area.

# Parâmetros

A parametrização da Integração TOTVS Business Analytics é obrigatória e deve ocorrer depois da execução do Configurador. Todas as áreas precisam da parametrização.

 Abaixo serão descritos todos os parâmetros disponíveis para a utilização na extração de dados ao BI.

* + Área Contábil  
    Contas contábeis que irão compor os indicadores gerenciais.  
    Histórico de fechamento que serão desconsiderados na extração do indicador gerenciais.
  + Área Financeira  
    Tipos de documento a Pagar que serão considerados na extração.  
    Tipos de documento a Receber que serão considerados na extração.
  + Área Comercial e Materiais   
    Tipos de movimentos que serão considerados na extração. (Nota fiscal de compras, Devolução de Compras, Carteira de compras, Ordem de Compras, Solicitação de compras, Aprovação de Ordem de Compras, Carteira de Vendas, Vendas, Faturamento, Devolução de vendas.)
  + Recurso Humanos  
    Faixa Etária, Tempo de Casa, Tempo de Cargo, tipo de benefício Bolsa.  
    Eventos: Proventos de Folha, Desconto de Folha, Base de Cálculo Custo de Folha, Custo de Folha, Hora trabalhada do Custo da Folha, Hora Extra do Custo da Folha, Eventos especiais do Custo de Folha, Benefícios pagos pelo Colaborador, benefícios pagos pela Empresa.  
    Encargos: Pagos pelo Colaborador, Pagos pela Empresa.

# Plano de Extração

O cadastro do plano de extração é uma definição de um plano de trabalho para a extração dos dados do Totvs-RM. Ele permite que a extração dos dados seja realizada de forma seletiva, onde é possível extrair somente as áreas, fatos e dimensões relevantes para o tipo de análise que se deseja realizar.

* Tipo de Período  
    
  Os períodos de extração são filtros de data que serão considerados na extração das informações do ERP-RM. Ao realizar o cadastro do plano de extração é necessário informar qual será o tipo de período de extração. O tipo de período de extração pode ser:  
  Sem período: É utilizado quando o tipo de extração for definido apenas com dimensões, onde não é necessário ser informado filtro por período.  
    
  Período Fixo: É muito comum a utilização do período fixo quando o plano de extração dos dados for de carga inicial, ou seja ao implantar o Totvs Smart Analytics comTotvs-RM.  
    
  Período Variável: Utilizando o período de extração variável, será considerado, o intervalo de data de extração variável conforme os valores informados, levando em consideração sempre a data atual menos um dia. Esta opção é comumente utilizada em cargas incrementais.
* Tipo de seleção do Extrator  
  Para proceder com a extração dos dados do ERP Totvs-RM de forma segmentada é necessário informar qual será o tipo de extração para o plano, podendo ser por:  
  Dimensões  
  Controladoria  
  Financeiro  
  Comercial  
  Materiais  
  Recursos Humanos  
  Educacional  
  Personalizado: Permite ao usuário realizar a extração apenas dos fatos que julgar necessário.

# Execução do Plano de Extração

Após a definição dos parâmetros e do cadastro do plano de extração, basta executar o processo do plano de extração. Para executá-lo acesse o*menu RM->Integração->GoodData->Processo do Plano de Extração*.  
Caso seu ambiente esteja configurado em três camadas é possível realizar o agendamento da execução do plano de extração conforme sua necessidade.

Ao executar o processo de extração, o processo identifica, os planos em comum ao plano selecionado. Dessa forma, o processo emite ao usuário um alerta informando que houve em outro momento uma extração dos dados em comum ao plano selecionado, cabendo ao usuário decidir se conclui ou não o processo de extração.

Quando o processo entra em execução é inicializado a limpeza das tabelas envolvidas (dimensões e fatos) conforme o tipo de extrator definido no cadastro do plano. Todas as vezes em que um plano for executado será gerado um histórico para que o usuário possa acompanhar a movimentação da extração dos dados.

Ao concluir a execução do processo do plano de extração, os dados foram extraídos, tratados, padronizados e então carregados no Fluig Smart Data. A partir deste ponto, os dados deverão ser transportados até a nuvem, para o Data Warehouse do TOTVS Smart Analytics. 

# Histórico do processo do Plano de Extração

Esta opção permite que sejam visualizadas as informações referentes a todos os planos de extração executados em sua base de dados permitindo que seja efetuado analise sobre a cada item de extração do plano. Poderão ser consultadas informações tais como o período de extração, quantidade de registros extraído de cada item do plano, usuário que executou o processo, o tempo de extração por item e o status do plano de extração. O status do item do plano de extração representa a ação que está ou foi executado, São eles:

* Plano em Execução
* Plano Executado
* Erro na Extração
* Enviando para GoodData
* Enviado para GoodData

# Processo de envio dos dados para o Totvs Smart Analytics

O processo de envio, identifica os dados que foram extraídos, através da conclusão do processo do plano de extração e executa em background o **Agent** que é quem envia os dados da Stage Area para o Totvs Smart Analytics. Antes de executar o processo de envio dos dados é necessário informar alguns parâmetros. Para isto acesse *menu Integração->Ferramentas-> Parâmetros -> TOTVS Business Analytics*e informe os parâmetros:

* Caminho do my.properties
* Caminho do Agent
* Caminho do Java.exe

**Importante:**Antes de executar o processo de envio, certifique-se que o my.properties (arquivo de configuração do **Agent**) já esteja devidamente configurado para o envio.  
Para mais detalhes de como configura-lo consulte: [Onde encontro o download do Agent?](http://tdn.totvs.com/pages/viewpage.action?pageId=165283518) [Como preencho o arquivo my.properties do Agent ?](http://tdn.totvs.com/pages/viewpage.action?pageId=165283537)

divs
