---
content_hash: 1ef0a376b0439ae54a9c6faa494e2ff0864e85387bbb801c864be156f00df853
fetched_at: '2026-06-29T00:10:47.613744+00:00'
page_id: '559498334'
product: rm
source: tdn-rm
title: INTEGRAÇÃO SSO X NUCLEUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=559498334
version: 5
---

**OBJETIVO**

Definir documentação necessária para a configuração dos Tipos de Movimento do TOTVS Gestão de Estoque (RM Nucleus) para a integração com o TOTVS Segurança e Saúde Ocupacional (RM SSO).

**ABORDAGEM**

**Configurações gerais**

1. Inicialmente iremos ver parametrizações gerais inerentes ao proc\_GoBackesso:

**TOTVS Gestão Fiscal**

* Definição do Exercício Fiscal
* Seleção do Exercício Fiscal

OBSERVAÇÕES

* Essas ações não são impeditivas para montagem do Tipo de Movimento.
* Essas ações impactam no ato de gerar movimentação quando das ações de Fornecimento, Devolução etc...

AÇÕES NECESSÁRIAS

* Exercício Fiscal.
  + Acessar o Contexto do BackOffice / Gestão Fiscal.
  + Acessar em Cadastros / Mais / Exercício:

* + Aqui os períodos tem que ser válidos para a data corrente.

**TOTVS Gestão de Estoque, Compras e Faturamento**

* Definição do Período de Movimentação
* Criação e Configuração dos Tipos de Movimento
* Criação de Produto/EPI

OBSERVAÇÕES

* Essas ações definirão como se dará o controle de estoque dos EPI's.

AÇÕES NECESSÁRIAS

* Período de Movimentação:
  + Acessar o contexto BackOffice / TOTVS Gestão de Estoque.
  + Acessar Ambiente / Parâmetros / TOTVS Gestão de Estoque.
  + Acessar Parâmetros Gerais / Definições Gerais:

* Definir aqui um período válido para movimentação.

* Criando os Tipos de Movimento:
  + Acessar Ambiente / Parâmetros / TOTVS Gestão de Estoque.
  + Acessar Gestão de Estoque / Controle de EPI.
    - Incluir um Novo Tipo de Movimento.
    - Na criação do Tipo de Movimento a máscara e as fórmulas, bem como série são irrelevantes e pode ser informado qualquer valor, basta apenas que série seja definida como principal.

* + - Obs.: Os Códigos deverão iniciar como:
      * Compras : ------------------------ 1.2.XX
      * Empréstimos: --------------------- 2.2.XX
      * Devoluções: ---------------------- 1.2.XX
      * Invalidar: -------------------------- 2.2.XX
      * Transferência: --------------------- 3.1.XX
      * Empréstimos (Descartáveis): ----- 2.2.XX
      * Devoluções (Descartáveis): ------- 1.2.XX
* Configurando os Tipos de Movimento:
  + Acessar Ambiente / Parâmetros / TOTVS Gestão de Estoque.
  + Acessar Gestão de Estoque / Controle de EPI.
    - Selecionar o Tipo de Ambiente e clicar em configurar:

* + - Abaixo listo configurações padrões para todos os movimentos:
      * Mov Identificação:
        + Classificação: Controle de EPI
        + Edita Numeração: Mostra
        + Buscar Número em: Geral
      * Mov Emitente/Destinatário
        + Para todos deverá ser Empresa no Emitente e Destinatário, exceto no movimento de compra que deverá ser informado no Emitente como Fornecedor.
      * Item - Identificação 1/2
        + Tipo de Item: Produto
      * Item - Preço
        + Aceita Preço Zero
      * Item - Lote/Grade/Num. Série
        + Aceita Número de Série
        + Editar Grade Numerada
        + Consiste Lote
        + Status: Ativo
      * Fis - Natureza
        + Natureza: Não Edita
        + Natureza 2: Não Edita
        + Seleção Automática da Natureza: Não Seleciona
    - Configurações de Entrada (Compra)

* + - Configurações de Empréstimos

* + - Configurações de Devolução de Empréstimo

* + - Configurações de Empréstimos (Itens Descartáveis)

* + - Configurações de Devolução de Empréstimo (Itens Descartáveis)

* + - Configurações de Invalidar Itens

* + - Configurações de Transferências

*Obs.: Caso escolha a opção de Edição do Local de Destino como "Mostra",   
deverá preencher os loockups que serão habilitados*

* Permissão aos Tipos de Movimento
  + Após Criar e Configurar os Tipos de Movimento, é necessário conceder permissão de acesso aos mesmos no cadastro de Usuários do Sistema:
    - Na visão de Usuários, selecione o(s) usuário(s) desejado(s) e vá em Anexos / Permissões por Tipo de Movimento:

**TOTVS Segurança e Saúde Ocupacional**

* Associação dos Tipos de Movimento para controle de estoque dos EPI's

OBSERVAÇÕES

* Essas associações definirão qual movimento chamar nas ações do EPI.

AÇÕES NECESSÁRIAS

* Parametrizar Integração com Nucleus.
  + Acessar o Contexto do RH / Segurança e Saúde Ocupacional.
  + Acessar Opções / Parametrizador

* + Acessar Configurações / EPI

Aqui será possível definir cada um dos Tipos de Movimentos configurados anteriormente, selecionando antes a opção Integração com RM Nucleus.

**TOTVS Gestão de Estoque, Compras e Faturamento**

* Criação de Produto (EPI)
* Geração de Movimentação de Compra

OBSERVAÇÕES

* Uma vez estabelecida essa parametrização a inclusão de EPI's passa a ser realizada através da execução do processo de Vincular EPI em um produto.
* A disponibilização de Lotes para criar itens de EPI se dá a partir da geração do movimento de Entrada (Compra) definido no primeiro exemplo dos Tipos de Movimento.

AÇÕES NECESSÁRIAS

* Vincular um produto a EPI.
  + Acessar o Contexto do BackOffice / Gestão de Estoque.
  + Acessar o cadastro de Produto.

Obs.: O produto tem que ser de Último Nível.

Acessar Processos / Vincular/Desvincular Produto a EPI

Após a Vinculação o Produto pode ser visualizado no Catálogo de EPI do SSO, cabendo sua edição e definição se é EPI ou EPC:

* Gerar Saldo através da Movimentação de Entrada (Compra)
  + Acessar Estoque / Mais / Controle EPI
    - Entrar com o Tipo de Movimento de Entrada (Compra)
    - Incluir um novo movimento:

Em Itens adicionar o item criado informando quantidade e valor unitário:

Em seguida Salvamos o Movimento e com isso podemos conferir no catálogo de epi em Anexo / Lotes a Serem Lançados o movimento adicionado no Nucleus:

A partir daqui é necessário selecionar o lote e executar o processo de Gerar Itens do EPI:

Ao término da execução o status passa para lote gerado e o ícone ficará em vermelho para sinalizar e no anexo EPI/EPC do Catálogo será possível visualizar os itens criados conforme a quantidade informada na compra:

CONCLUSÕES

* A partir daqui, as movimentações geradas no Assistente de Fornecimento(Empréstimo, Devolução, Descarte e Cancelamento) e também nos processos de Invalidar EPI e Acerto de Local de Estoque serão refletidas nas colunas de Saldo do SSO e também no Produto em Anexo / Saldos e Custos.
