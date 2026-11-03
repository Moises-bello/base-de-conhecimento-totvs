---
content_hash: 646fb872fbd5fc441617654faa3f1d78bf85c95c89ac8212ae4df3e5f55cfdbe
fetched_at: '2026-06-29T00:09:18.542915+00:00'
page_id: '421388719'
product: rm
source: tdn-rm
title: FIN - Tabelas Opcionais
type: documentation
url: https://tdn.totvs.com/display/LRM/FIN+-+Tabelas+Opcionais
version: 15
---

Através deste módulo você controla o cadastro das tabelas opcionais.

Tabelas opcionais são cinco cadastros de informações que o TOTVS Gestão Financeira disponibiliza para que você possa aumentar o seu gerenciamento financeiro.  
Com estas tabelas é possível criar mais cinco cadastros além dos cadastros já existentes no aplicativo. Através do Assistente de Implantação de Processos você pode definir quais tabelas utilizar, um nome, máscara para o código dos registros que serão incluídos na tabela e a obrigatoriedade do preenchimento destas tabelas em outros cadastros.

Na janela principal é possível visualizar de forma simplificada, informações de um ou de vários registros da tabela opcional. Você define quantos e quais registros serão apresentados, criando filtros através do Gerenciados de Filtros (localizado na barra de ferramentas).

Ao executar um filtro cada registro será apresentado em uma linha e as informações em colunas.

**Dicas**

A permissão para visualização de informações ou realização de processos deste módulo pode ser configurada por usuário ou por perfis, no menu Segurança dos Serviços Globais. Na inclusão de um novo registro é possível que algumas informações já sejam apresentadas por default, para isso, edite um cadastro já existente, clique com o botão direito do mouse sobre a informação desejada, posicione o cursor do mouse sobre a opção "Valor Default" e clique sobre a informação.

As informações de alguns campos podem ser obrigatórias, para isso, clique com o botão direito do mouse sobre o campo e clique sobre a opção "Preenchimento Obrigatório". Ao clicar sobre o nome de algumas informações a janela de edição do cadastro da informação é apresentada. Você pode definir quais colunas serão apresentadas na janela de visão dos registros utilizando a funcionalidade "Configurar Colunas", ícone localizado na barra de ferramentas.

**Identificação**

Nesta pasta são apresentadas informações que identificam o registro da tabela opcional. Informação sobre alguns campos:

Código

Você pode definir uma máscara para o preenchimento deste código através do parâmetro "Máscara" (Assistente de Implantação de Processos | etapa Tabelas Opcionais do Financeiro).  
Na inclusão de um novo registro o código será validado se o parâmetro estiver preenchido.

Campo Livre

Este campo pode ser utilizado para a digitação de qualquer informação sobre o registro. A capacidade de armazenamento deste campo é de 255 posições.

Filial, Departamento e Centro de Custo

Estas informações podem ser utilizadas na tabela opcional 1.

Cadastrar Cheque

Esta informação pode ser utilizada na Tabela Opcional 2. Para realizar o processo de Cadastramento de Cheque no módulo TOTVS Gestão de Estoque, Compras e Faturamento é necessário que esta opção esteja marcada e esta tabela seja selecionada nos parâmetros do Movimento.

**Eventos Contábeis**

Quando uma dessas tabelas for indicada como default para evento através do parâmetro Assistente de Implantação de Processos | Integração Contábil | Contabilização do Financeiro | Tabela Default para Evento, ao acessar o menu Cadastros | Tabelas Opcionais e editar uma existente ou incluir uma nova, serão exibidos campos para inclusão de eventos contábeis default para:

* Evento Contábil para Inclusão
* Evento Contábil para Baixa
* Evento contábil para Baixa Contábil
* Evento Contábil para Extrato
* Baixa por Acordo
* Baixa de gerados por Acordo
* Evento Contábil para Liquidação Duvidosa
* Evento Contábil para Baixa em lançamento com liquidação duvidosa
* Evento Contábil para Baixa por Acordo em Lançamento com Liquidação Duvidosa
* Evento contábil para baixa de Crédito de Adiantamento: saiba mais em

**Observação**:

O campo de Evento Contábil para Baixa de Crédito de Adiantamento, estará disponível a partir da release 12.1.24. A contabilização será somente na baixa.

**Dicas**

A permissão para visualização de informações ou realização de processos deste módulo pode ser configurada por usuário ou por perfis, no cadastro de Segurança (menu Cadastros).

Na inclusão de um novo registro é possível que algumas informações já sejam apresentadas por default, para isso, edite um cadastro já existente, clique com o botão direito do mouse sobre a informação desejada, posicione o cursor do mouse sobre a opção "Valor Default" e clique sobre a informação.

As informações de alguns campos podem ser obrigatórias, para isso, clique com o botão direito do mouse sobre o campo e clique sobre a opção "Preenchimento Obrigatório".

Ao clicar sobre o nome de algumas informações a janela de edição do cadastro da informação é apresentada.

As tabelas opcionais também podem ser utilizadas como "Tabela Default para Evento", ou seja, selecionando uma tabela no parâmetro "Tabela Default para Evento" (Assistente de Implantação de Processos | processo Integração Contábil | etapa Contabilização do Financeiro), no cadastro dos seus registros são apresentados campos para a seleção de "eventos contábeis". Ao utilizar o registro da tabela na edição de um lançamento financeiro, o sistema busca automaticamente o evento contábil.

Você pode definir quais as colunas que serão apresentadas na janela de visão dos registros, utilizando a funcionalidade "Configurar Colunas", ícone localizado na barra de ferramentas.

 Veja Também
