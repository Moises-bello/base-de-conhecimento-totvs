---
content_hash: d3d1d96cf59053efa29547f122297020a381549fa9db555e215721b202ac7b1f
fetched_at: '2026-06-29T00:11:36.052701+00:00'
page_id: '770956085'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Utilitários - Conversor de Base de Dados
  do Portal de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=770956085
version: 16
---

### Introdução

---

O conversor de base de dados do Portal de Imóveis tem como finalidade a integração e sincronização dos dados presentes nos bancos de dados do Portal de Imóveis e do banco RM. Esse processo é realizado por meio de algoritmos e técnicas de mapeamento e transformação dos dados, garantindo a consistência e a uniformidade das informações.

Através dessa integração, o sistema integrado passa a operar com um único banco de dados, eliminando a necessidade de consultas e atualizações em bancos de dados separados. Isso resulta em maior eficiência e velocidade nos processos, além de reduzir o risco de inconsistências e erros nos dados.

Esta unificação de bases está disponivel somente para alguns clientes Pilotos na versão 12.1.2310, depois dessa analise especifica disponibilizaremos para todo o mercado.

### Procedimentos para utilização

---

Antes de realizar a conversão, *pode ser necessário* realizar uma alteração no arquivo RM.HOST.config incluindo a chave: <add key="DBSCommandTimeout" value="1200" />

Saiba mais sobre este comando no link: [Aumentar o Timeout da execução das sentenças SQL](https://tdn.totvs.com/pages/viewpage.action?pageId=269437677)

Em seguida, ao acessar o sistema, será necessário conceder permissão ao processo "Conversor de Base de Dados do Portal de Imóveis" no perfil de usuário.

Após a permissão ser concedida, você deve acessar a seção "Utilitários" e selecionar a opção "Conversor de Base de Dados do Portal de Imóveis". Em seguida, siga os passos listados abaixo:

### Conexão

---

Para conectar ao banco externo do Portal de Imóveis iremos utilizar a conexão de banco de dados externo nativa do RM.

Para realizar essa configuração favor seguir os passos no [documento neste link (clique aqui)](https://tdn.totvs.com/pages/releaseview.action?pageId=239034160)

Com a configuração realizada e o banco ativo, teremos uma mensagem de confirmação ao clicar em avançar.

É importante ressaltar que, para realizar o processo de conversão para o RM, a base de dados do portal de imóveis deve ser migrada para a versão 12.1.2310. Para atualizar a base do portal de imóveis para essa versão, basta acessá-la por meio do portal de imóveis. Isso garantirá que suas tabelas sejam atualizadas para a versão mais recente.

Caso a base não esteja migrada, uma mensagem semelhante à imagem abaixo será exibida:

### Validação de Chave Estrangeira

---

Nesta etapa, o sistema irá realizar uma validação de dados referentes a chaves estrangeiras que possam, por algum motivo, estar ausentes no banco de dados. Esta verificação é obrigatória e necessita ser concluída antes de se iniciar o processo de migração. Não será possível iniciar a conversão sem antes ajustar essas inconsistências no banco de dados de origem. Esta etapa do processo visa destacar quais campos necessitam de ajustes, de forma transparente ao usuário.

A tela de validação é demonstrada na imagem abaixo:

Ao selecionar o botão "Iniciar Validação", o sistema iniciará a análise dos registros presentes no banco de dados de origem, identificando as tabelas que requerem ajustes.

É fundamental ressaltar que, ao avançar sem completar essa etapa de validação e pressionar o botão "Avançar", o sistema emitirá a seguinte mensagem:

Após a conclusão da conferência, o sistema exibirá as tabelas juntamente com seus registros, conforme ilustrado na imagem a seguir:

* **Tabela:** Refere-se à tabela em que a inconsistência de chave é identificada;
* **Chave Primária:** Corresponde à chave existente no banco de dados que está referenciando uma chave estrangeira inexistente;
* **Coluna:** Indica a coluna na qual a inconsistência ocorre;
* **Valor:** Representa o valor que não foi localizado no banco de dados;
* **Tabela Referenciada:** Indica a tabela na qual a chave estrangeira está inserida;
* **Coluna Referenciada:** Refere-se à coluna que faz referência ao valor não encontrado.

Na figura a seguir, podemos observar a seguinte situação:

Na tabela "pessoa", a chave primária é identificada como 1019. No entanto, na coluna "profissao\_id", o valor atribuído é 5, que não encontra correspondência na tabela referenciada "profissao", cuja coluna primária é denominada ".id".

Uma vez efetuados os ajustes necessários para solucionar os problemas identificados nesta fase, será necessário clicar novamente no botão "Iniciar Validação" para prosseguir para a próxima etapa. Em seguida, basta clicar em "Avançar" para continuar.

Nesta mesma tela, é importante notar a presença da opção "Exportar", que possibilita aos usuários extrair esses registros para um arquivo. Esse arquivo pode ser compartilhado posteriormente com a equipe de suporte para análise e, se necessário, correções. Além disso, a funcionalidade de pesquisa oferece a oportunidade de encontrar rapidamente registros na visualização.

### Tabelas de Migração

---

Neste processo serão apresentados as tabelas que serão migradas do Portal de Imóveis para o RM.

Salientamos que, por padrão, a importação das tabelas de log do Portal de Imóveis (AUDITTRAIL e LOG) não é realizada, visando uma conversão mais rápida. Caso necessite destas tabelas migradas, o campo "*Desejo considerar as tabelas de log do portal de imóveis no processo de migração*" deve estar marcado.

Durante a conversão, será apresentado o percentual de conversão atual e também em qual tabela o processo de migração se encontra, conforme a imagem abaixo:

Ao final será apresentado o LOG de conversão destas tabelas, com as quantidades de registros migrados.
