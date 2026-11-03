---
content_hash: 1de15ded02a5c40806808829299468da59f1c263aeac76f60530eb7bdb9ff7c6
fetched_at: '2026-06-29T00:09:02.349485+00:00'
page_id: '379305796'
product: rm
source: tdn-rm
title: Contabilização de Lançamento Padrão pela FRU – Protheus e Aglutinação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=379305796
version: 3
---

Configurando  Protheus

Criando Tabela SZA no Protheus

Tabela criada para controlar os campos que gravam o processo de contabilização dos lançamentos acessórios.

Na hora que é feita uma baixa, seja por CNAB ou manual, é feito Start através de parametrizações na contabilidade um evento chamado lançamento padrão.

Temos por exemplo um Lançamento padrão 520 que é responsável pelas baixas manuais.

Lançamento padrão 521 que é responsável pelo retorno de CNAB.

SIGACFG

Entrar com Administrador do Protheus

Base de Dados | Bases de Dados

Dicionário de Dados | Incluir

Criar Tabela ( SZA )

Informar Descrição : SALDOS CONTABILIZAÇÃO FRU

Selecionar Campos

Para criar os Campos da Tabela SZA que são :

* ZA\_FILIAL
* ZA\_PREFIXO
* ZA\_NUMERO
* ZA\_PARCELA
* ZA\_TIPO
* ZA\_CLIFOR
* ZA\_LOJA
* ZA\_SEQ
* ZA\_COD
* ZA\_VALOR
* ZA\_DATA
* ZA\_ESTORNO

Configuração dos Campos da Tabela ( SZA )

Configurando -  ZA\_PREFIXO

Configurando – ZA\_NUMERO

Configurando ZA\_PARCELA

Configurando ZA\_TIPO

Configurando ZA\_CLIFOR

Configurando ZA\_LOJA

Configurando ZA\_SEQ

Configurando ZA\_COD

Configurando ZA\_VALOR

Configurando ZA\_DATA

Configurando ZA\_ESTORNO

Cadastrando os Índices

Selecionar - Índices

Criando Índice com os campos:

ZA\_FILIAL – ZA\_PREFIXO – ZA\_NUMERO – ZA\_PARCELA – ZA\_TIPO – ZA\_CLIFOR – ZA\_LOJA – ZA\_SEQ – ZA\_COD

**Tabela FRU do Protheus**

Que vem do RM e é gravado no Protheus através de uma mensagem única chamada de FINANCING. Esta mensagem pega o título que foi criado no RM e traz este título para ser criado no Protheus e quando é um reajuste, ela traz o valor novo do RM para o Protheus alimentando este mesmo título criado.

Quando a FINANCING é criada ou alterada ela tem uma tabela chamada FRU do Protheus que mostra o que tem naquela parcela.

Exemplo, R$1.000,00 Reais um valor de um título, na FRU R$500,00 valor de X, R$200,00 valor Y, R$300,00 valor de Z e até os descontos terão os eventos e as baixas serão Rateadas. Podem ser cadastrados N componentes e o Rateio seria para o número definido.

Customização faz o seguinte, baseada em cada lançamento padrão que se tem vai na FRU, faz uma regra de Três do peso daquele Componente sobre o valor que está sendo baixado e contabiliza aquele componente específico de acordo com a regra do RM.

Localizar tabela FRU em seguida

FRU – Marcar uso Browse

Configurando Parâmetros do Protheus

Base de Dados | Bases de Dados

Parâmetros

Buscar

Configurar o Parâmetro – **FS\_LANCECE**

Especifico para o contabilização e é responsável por falar que a customização encontra-se ativa ou não.

**S** – Encontra-se ativo a customização

**N-** Encontra-se Inativa a customização

Configurando o Parâmetro – **FS\_PREFAG**L

Prefixo do Título Aglutinador no Protheus.

Este é responsável para criar o prefixo do título que será Aglutinado e neste exemplo o prefixo é (AGL).

Configurando o Parâmetro – **FS\_RATCCAG**

Informa se o título aglutinador se será utilizado meio de rateio de centro de custos por múltiplas naturezas.

Quando se cria um título novo com somatório de títulos antigos pode ser usado um rateio de centro de custo por múltipla naturezas.

Se estiver marcado este parâmetro, ele vai levar o rateio para o título aglutinador também para efeito de taxa, provisão de receitas.

**2** – Não utiliza

1 – Utiliza

**Criando Menus**

Ambiente | Cadastros | Menus

Somente deixar marcado o Financeiro e em seguida ( OK )

Clicar em – Adicionar

Sim

Sim

Marcar – Miscelanea

Em seguida : Novo Grupo

Descrição -  LANÇAMENTOS ACESSÓRIOS

Selecionar o novo Grupo e em seguida – Novo Item

Em Programa: **FSCTB01C**

Descrição: Cod.Lanc.Acessórios

Módulo: Financeiro

Tipo: Função de Usuário

Criar e em seguida (OK)

Selecionar o novo Grupo novamente e em seguida – Novo Item

Em Programa: **FSCTB02C**

Descrição: Cont.Lanc.Acessórios

Módulo: Financeiro

Tipo: Função de Usuário

Criar e em seguida (OK)

Criado o Grupo e os Itens

**Exemplo da contabilização**

Módulo – SIGACTB

Atualizações | Entidades | Lançamento Padrão

Localizar o 520 que é responsável pela Baixa Normal

Criar um Filtro no Protheus para localizar o lançamento padrão 520

Cod Lanc Pad = 520 (Adicionar em seguida)

Salvar logo depois

Selecionar o Filtro criado e em seguida, Aplicar filtros selecionados

Contabilizando a FRU e o nome o Cliente informa o nome desejado.

 Visualizando

Código do lançamento padrão, sequência dele, que é 20 ou seja, terão 19 lançamentos padrões anteriores a este. Descrição, se está ou não ativo.

Se Credita ou Debita

Como é de Crédito, em entidades é informado Cta Crédito e C Custo Cred.

Observação Importante: Em valores é informado em Vlr Moeda um valor utilizando a Customização que está contabilizando e buscando o evento 26 da FRU.

**Exemplo de um Baixa norma**l

Módulo SIGAFIN

Atualizações | Contas a Receber | Funções Contas a Receber

Aplicar filtros selecionados

Selecionar o Título e em seguida: Outras Ações | Baixas | Baixar

Neste momento o Protheus vai no RM e o RM atualiza o Título e a FRU.

Salvar

Tela de Baixa contábil

Contabilização a Débito que vem tudo de lançamentos padrão, um lançamento padrão para cada linha.

Primeiro contabiliza a Débito no valor da Baixa e o restante tudo é crédito.

Juros que é cobrado do Protheus sobre o Valor baixado que o exemplo acima é de R$91,08 juros financeiro.

Este é um lançamento padrão que vai deixar de ter com a customização, por que está sendo visualizado então? Para o momento dos testes e verificar os valores se estão todos valores corretos e batendo, Pois o somatório de todos os valores tem que bater o Baixa que é R$946,42.

Neste exemplo tem baixa da FRU de evento 26 no valor de R$25,25

Baixa da FRU de evento 006 no valor de R$148,43 e o Título tem outros eventos na qual o valor tem que bater os R$946,42 fazendo com que o Total de Débito bata com Crédito.

**Para verificar a Contabilização gerada**

Módulo – SIGACTB

Atualizações | Movimentos | Lan Contab Automat

Filtro para buscar o lançamento gerado dia 29 de Junho

Lançamentos Contábeis enviados

**Rotina Aglutinação**

Aglutinação o Protheus não tem como criar boleto bancário encima de 2 ou mais títulos, pode se criar encima de apenas 1 título, ai se pega este dois ou mais títulos os une , soma e se gera um boleto único e só de pode ser feito em um mesmo contrato de um mesmo cliente e não se tem como se Aglutinar títulos de clientes diferentes e ou contratos diferentes.

Funções Contas a Receber

Outras Ações | Renegociar

Informar a Data do vencimento do Título que será criado

Informar o Cliente na qual será criado o Título

Marcar todos os títulos que deseja Aglutinar e em seguida - GRAVAR

Mostrado o valor do somatório dos Títulos e com vencimento desejado pelo cliente.

Borderô para o banco é obrigatório se fazer para informar qual banco será remetido.

Informar o Cliente e os Títulos

**REMETER O AO BANCO O NOVO TÍTULO AGLUTINADO**

Salvar

Título Aglutinado criado

Visualizar para ver os títulos com Status de RENEGOCIAÇÃO

Selecionar – Visualizar

Outras Ações | Posição

Motivo - REN

Informado o Título Aglutinador

**Baixando por CNAB**

Lendo o Arquivo CNAB

Outras Ações | CNAB | Le arq retorno

Localizar o Arquivo

**Baixa Normal**

Selecionar o Título Aglutinado

Outras Ações | Baixas | Baixar

Informado o Motivo de Baixa: **RENEGOCIA**

Baixado o Título
