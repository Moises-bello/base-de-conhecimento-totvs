---
content_hash: 803bec75eac278450edbaddc820a4cb5df785e7f94f779d54c1c3cf80d98faaf
fetched_at: '2026-06-28T21:35:19.302580+00:00'
page_id: '201732539'
product: fluig
source: tdn-fluig
title: Scripts Condicionais
type: documentation
url: https://tdn.totvs.com/display/fluig/Scripts+Condicionais
version: 9
---

# Índice

none4.\*ndicetrue

# Objetivo

O objetivo desta página é esclarecer o uso de um script condicional do fluig.

# Script Condicional

O objetivo de um script condicional é verificar alguma informação que não pertence ao fluig que foi disponibilizada em algum webservice externo. Essa informação é dinâmica logo os eventos condicionais poderão ser programados para periodicamente executarem o script e verificarem se uma informação atingiu um determinado valor ou atingiu algum patamar estabelecido pelo negócio.

### Exemplo de utilização do script condicional

Um exemplo de uso de negócio seria criar um processo com uma atividade inicial condicional cujo script verifica o preço do dólar para compra. O preço do dólar pode variar durante o dia e neste caso poderíamos ter um processo workflow de compra de dólares que seria iniciado apenas se o preço do dólar atingisse um patamar aceitável para o negócio do cliente.

Os scripts condicionais são scripts javascript que possuem basicamente todos os recursos dos eventos de processo do fluig podendo combinar a consulta de webservices externos com dados do formulário. Quando este script conseguir retornar *true* então a solicitação workflow será iniciada ou movimentada de acordo com o elemento utilizado na modelagem.

**Exemplo de script acessando um webservice:**

Exemplo scriptjs solic) {
return true;
}
}]]>Observação

Embora seja possível realizar a alteração de dados e consulta de webservices internos do fluig dentro de um script condicional, alertamos que esta prática não é recomendada.

Em nossos exemplos estamos utilizando os próprios webservices do fluig apenas para facilitar a compreensão e implantação destes exemplos em ambientes de desenvolvimento do fluig.

### Processo Exemplo monitoramento de solicitações

Para este processo exemplo iremos monitorar a lista de tarefas pendentes de um usuário fluig escolhido no formulário do processo. Caso o número de solicitações pendentes seja superior ao número tolerado informado no formulário então será encaminhada para o administrador uma tarefa de "Aviso" em que o administrador poderá atuar com este usuário.

**Figura 1 - Diagrama do processo de exemplo com script condicional.**

### Procedimento para implantação do exemplo

samplesfalse0.5fade1truePasso 1

* Cadastre o DashBoardService utilizando o código fluigDashBoardService . A URL informada será a seguinte:

[https://(servidor): porta /webdesk/DashBoardService?wsdl](https://envinc.fluig.com/webdesk/DashBoardService?wsdl)

2Passo 2

* Importar o processo exemplo.
* Cadastrar o servidor destino no studio.

3Passo 3



+ Verificar a frequência de checagem do Job nas propriedades da atividade condicional no fluxo.

4Passo 4

* Exportar e liberar o processo junto com o formulário que está neste projeto.
* Iniciar uma solicitação e mover para a atividade condicional.

Após os procedimentos realizados acima você terá um exemplo de script condicional funcionando no seu ambiente.  e faça o download do projeto que contém o exemplo acima mencionado.

# Variáveis e funções suportadas em scripts condicionais

Segue a lista de variáveis e funções suportadas em scripts condicionais :

| Variável | Função |
| --- | --- |
| **log** | Impressão de mensagens dentro do log do Fluig. |
| **ServiceManager** | Objeto que permite a instância de objetos é métodos de webservices soap |
| **DatasetManager** | Objeto que permite carregar datasets entro das customizações. |
| **DatasetFactory** | O objeto **DatasetFactory** é a "porta de entrada" para o acesso a qualquer Dataset Maiores detalhes sobre este item se encontram no artigo sobre |
| **DatasetBuilder** | Permite a criação de datasets. Maiores detalhes sobre este item se encontram no artigo sobre |
| **ConstraintType** | Determina o tipo de constraint a ser utilizada em uma condição do dataset. Maiores detalhes sobre este item se encontram no artigo sobre |
| **notifier** | Permite realizar notificações extras em eventos e scripts. |
| **WKParams** | Coleção de parâmetros que podem ser utilizados dentro dos scripts como o WKCompany e WKUser. As outras variáveis e o que elas retornam podem ser encontradas no artigo sobre  . |
| **hAPI** | Contém operações relacionadas a solicitação workflow em andamento. Está disponível apenas para os scripts de eventos intermediários condicionais. Maiores detalhes sobre as funções da hAPI podem ser encontradas no artigo sobre . |
