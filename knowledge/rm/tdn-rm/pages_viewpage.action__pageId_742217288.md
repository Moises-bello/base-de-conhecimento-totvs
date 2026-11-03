---
content_hash: 25e737e5b60b84055628bd61d06fb91c70657aa56eb044e62c0ca0f0d19ec93c
fetched_at: '2026-06-29T00:11:32.001700+00:00'
page_id: '742217288'
product: rm
source: tdn-rm
title: Visão de Recursos Smart View no RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=742217288
version: 14
---

# Introdução

---

O objetivo dessa página é mostrar o funcionamento do menu Smart View disponibilizado no RM.

# Menu Smart View

---

Após realizar a  é possível acessar o Menu Smart View.

O acesso ao Menu Smart View é feito através da aba Gestão, em Ferramentas de Análise:

Segurança

Para habilitar o Menu Smart View, é necessário configurar a permissão de acesso nos perfis.

  

# Inclusão de recursos do Smart View no RM

---

Para criar um novo relatório na visão, basta clicar no ícone de incluir e adicionar as informações necessárias:

A partir da versão 12.1.2406

Imagem a partir da versão 2406:

1. **Código do Recurso:** Nome do recurso que será exibido no RM.
2. **Visível a todas a coligadas:** Define se o relatório será visível por todas as coligas, ao habilitar essa opção o relatório estará alocado na coligada global.
3. **Recurso Smart View:** Exibe todos os recursos criados no SmartView. Deve adicionar um recurso para visualização do mesmo no RM.

   Caso o recurso já tenha sido mapeado, ele não será exibido na lista.A partir da versão 12.1.2406
4. **Tipo do Recurso:** Após preencher o "recurso Smart View" este campo é preenchido automaticamente conforme tipo do recurso escolhido.
5. **Aplicação:** Sistema onde o relatório será criado.
6. **Tipo:** Define o local específico no produto onde o relatório poderá ser listado para uso.
7. **Categoria:** Funcionam principalmente como controladores de permissão do recurso. [Clique aqui](https://tdn.totvs.com/display/LRM/Categorias+de+Recurso+no+RM) para mais informações.

Após preencher os campos e clicar em Salvar, os recursos serão exibidos na visão, separados por aplicação conforme as outras visões do sistema.

A partir da versão 12.1.2406A partir da versão 12.1.2502

A partir da versão 12.1.2502, os recursos disponíveis no Smart View, mas ainda não integrados ao RM, também serão exibidos na lista.

# Visualização rápida do Recurso

---

Após o mapeamento do recurso Smart View no RM, é possível visualizá-lo rapidamente ao clicar com o botão direito em cima do recurso na visão e acessar: **Outras Informações → Execução de Recurso no Smart View:**

Parâmetros com as seguintes nomenclaturas (indiferente entre minúsculas e maiúsculas) serão resolvidos e ocultados automaticamente utilizando o contexto do usuário que estiver acessando a visão:

falsecardParametersslideVersão 12.1.2506 e posteriores

* **SYS\_CODUSUARIO →** Usuário Atual
* **SYS\_CODCOLIGADA →** Coligada Atual
* **SYS\_CODFILIAL →** Filial Atual
* **SYS\_CODSISTEMA →** Sistema Atual
* **SYS\_IDPRJ →** Projeto Atual
* **SYS\_EXERCICIOFISCAL →** Exercício Fiscal Atual

* **VAR\_CODIGORELATORIO →** Código do Recurso no mapeamento feito no RM
* **VAR\_DESCRICAORELATORIO →** Nome do Recurso no Smart View
* **VAR\_IDENTIFICADORRELATORIO →** Identificador único do Recurso no mapeamento feito no RM
* **VAR\_VERSAO →** Versão em execução do RM
* **VAR\_NOMECOLIGADA →**Nome da Coligada atrelada ao Contexto em Execução
Versão 12.1.2406 e posteriores

* **SYS\_CODCOLIGADA →** Coligada Atual
* **SYS\_CODFILIAL →** Filial Atual
* **SYS\_CODSISTEMA →** Sistema Atual
* **SYS\_IDPRJ →** Projeto Atual
* **SYS\_EXERCICIOFISCAL →** Exercício Fiscal Atual

* **VAR\_CODIGORELATORIO →** Código do Recurso no mapeamento feito no RM
* **VAR\_DESCRICAORELATORIO →** Nome do Recurso no Smart View
* **VAR\_IDENTIFICADORRELATORIO →** Identificador único do Recurso no mapeamento feito no RM
* **VAR\_VERSAO →** Versão em execução do RM
* **VAR\_NOMECOLIGADA →**Nome da Coligada atrelada ao Contexto em Execução

Abaixo o arquivo utilizado no relatório demonstrado como exemplo na imagem acima:

250

Versão 12.1.2402 e anteriores

* **$codColigada →** Coligada Atual
* **$codFilial →** Filial Atual
* **$codSistema →** Sistema Atual
* **$idprj →** Projeto Atual
* **$exercicioFiscal→** Exercicio Fiscal Atual
A partir da versão 12.1.2406

Após o mapeamento do recurso Smart View no RM, é possível visualizá-lo rapidamente ao clicar com o botão: **Mais Ações → Executar no Smart View:**

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2306

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
