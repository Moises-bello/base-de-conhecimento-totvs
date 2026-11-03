---
content_hash: 3b8197d1dfb6b7da4e6a3907bdd7c1fededf5fb7ec9ada45fd5965fa9e9fe601
fetched_at: '2026-06-29T00:10:27.948904+00:00'
page_id: '517131243'
product: rm
source: tdn-rm
title: Regras para aplicação de Filtros por Perfil(s) e por Usuário(s)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=517131243
version: 34
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   Esclarecer o comportamento da aplicação quando são utilizados filtros por Perfil(s) e/ou por Usuário(s).

# Filtro por Usuário:

---

   O Filtro por Usuário é aplicado em qualquer query executada na aplicação, desde que a coligada do contexto do RM seja igual à coligada selecionada no cadastro do filtro.

Exemplo:

2Cadastro do Filtro

Para esse exemplo, foram criados 2 Perfis, sendo eles para os módulos **Folha de Pagamento** e **Inteligência de Negócios**. Após isso, foi criado um usuário ao qual os dois perfis foram associados.

Foi cadastrado um Filtro para esse usuário (disponível em Anexos | Filtro por Usuário), com o seguinte preenchimento: Na coligada 1, trazer da tabela de Funcionários (PFUNC), apenas os funcionários que possuem salário menor ou igual a 1000.

Em login para esse usuário, ao acessar a tela de Funcionários, no módulo Folha de Pagamento, mediante o filtro criado os seguintes registros serão exibidos:

Execução de consultas SQL

Para esse exemplo, foram criadas duas consultas SQL, nas aplicações BIS e Labore, trazendo os campos CODCOLIGADA, CHAPA, NOME e SALARIO da tabela de Funcionários (PFUNC).

Na execução das consultas SQL, foram trazidos apenas registros de funcionários que possuem o salário menor ou igual a 1000, devido ao Filtro por previamente cadastrado.

A aplicação do Filtro por Usuário ocorrerá independente do módulo em que o filtro foi cadastrado.

# Filtro por Perfil:

---

   O Filtro por Perfil só será aplicado em uma query mediante as seguintes condições:

1. **Associação de usuário ao perfil:**O usuário deve estar associado a um perfil que possui o filtro cadastrado
2. **Coligada:**A Coligada do contexto da aplicação é a mesma Coligada selecionada no cadastro do filtro
3. **Módulo utilizado:**O módulo selecionado no contexto da aplicação é igual ao módulo utilizado no cadastro do perfil que o usuário está associado.

# Filtro por Perfil em consultas SQL:

---

    O Filtro será aplicado na execução de consultas SQL quando atenderem aos requisitos 1 e 2 definidos acima.

Na nova MDI, o parâmetro "**Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis**" altera o comportamento dos filtros por perfis na execução das consultas SQL cadastradas.

Por padrão, ao executar uma consulta SQL são aplicados os filtros cadastrados nos perfis do mesmo módulo em que a consulta SQL está cadastrada.

      Caso o parâmetro **Ignorar o módulo de origem da consulta SQL ao aplicar filtros por perfis** esteja habilitado, ao executar uma consulta SQL serão aplicados todos os filtros por perfis cadastrados independentemente do módulo de origem do perfil e da SQL.

Para maiores informação, consultar o link .

Exemplo:

1Filtro por Perfil

Para esse exemplo, foram criados 2 Perfis, sendo eles para os módulos **Folha de Pagamento** e **Inteligência de Negócios**. Após isso, foi criado um usuário ao qual os dois perfis foram associados.

Para o Perfil criado no módulo **Folha de Pagamento**, foi adicionado um Filtro por Perfil (disponível em Anexos | Filtro por Perfil), com o seguinte preenchimento: Na coligada 1, trazer da tabela de Funcionários (PFUNC), apenas os funcionários que possuem salário menor ou igual a 1000:

Consultas SQL

Para cada módulo dos Perfis cadastrados (LABORE e BIS), foi criada uma consulta SQL, trazendo os seguintes dados:

sql

A utilização de UNION entre SELECTs de tabelas diferentes, **não é considerada uma boa prática**, pois pode distorcer os resultados e comprometer a aplicação correta dos filtros por usuário e/ou perfil.

Execução

Em login ao usuário criado, ao executar as duas consultas SQL, o seguinte resultado é obtido:

Módulo: **Folha de Pagamento**

    Na execução dessa consulta, são trazidos apenas os registros de funcionários que possuem o salário menor ou igual a 1000, devido ao Filtro por Perfil previamente cadastrado.

Módulo: **Inteligência de Negócios**

    Ao executar a consulta cadastrada nesse módulo, serão trazidos todos os registros da tabela de Funcionários, uma vez que o filtro cadastrado no módulo Folha de Pagamento não influencia em consultas executadas em outros módulos.

# Filtro por Usuário e Perfil no Delphi:

---

   O Filtro por Usuário e Perfil nas rotinas Delphi tem algumas diferenças em relação ao .NET, como por exemplo: A aplicação RMLabore.exe (delphi) não possue filtro por usuário, apenas filtro por perfil e contempla apenas as tabelas PFUNC e ANOTAC. Segue abaixo quadro com todas as aplicações e tabelas que são contempladas em cada um dos filtros:

**Filtro por Perfil**

| Aplicação | Tabela |
| --- | --- |
| RMTestis | BPROVA |
| RMLabore | PFUNC, PANOTAC |
| RMChronus | PFUNC |
| RMVitae | PFUNC, PTPANOTACAO, VEXAMES |
| RMFluxus | FLAN, FCFO, FCXA, FXCX, FFAT, FLANRATCCU, FLANRATDEP, FTIPOAPLFIN |

**Filtro por Usuário**

| Aplicação | Tabela |
| --- | --- |
| RMFluxus | FLAN, FCFO, FCXA, FXCX, FFAT, FLANRATCCU, FLANRATDEP, FTIPOAPLFIN |
| RMSaldus | CLANCA, CLCTLOTE, CORCAMENTO |
| RMBonum | IBEM |
| RMNucleus | TCCOTACAO, TCNT, TITMCNT, TITMMOV, TITMMOVRATCCU, TITMMOVRATDEP, TLAF, TMOV, TMOVRATCCU, TMOVRATDEP, TPRD, FCFO |
| RMOficina | OFOBJOFICINA, TMOV, OFPLANOMANUT, OFMAOOBRA, OFATENDIMENTO, OFCONTRATO, OFTIPOOBJ, OFVENCPLANOMANUT, OFVENCAGENDASERV, PFUNC, GFILIAL, GCCUSTO, TLOC, GDEPTO, OFAGENDASERV |
| RMLiber | FCFO |
| RMClassisNet | SMATRICPL, STURMADISC, SCURSO, SDISCIPLINAHIST, SPARTEHIST, SCURSOHISTORICO, SGRUPOHIST |
| RMTestis | BAREA, BPROVA, BQUESTAO |

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Filtro por Perfil/Usuário

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2019

false

**Autores:**
