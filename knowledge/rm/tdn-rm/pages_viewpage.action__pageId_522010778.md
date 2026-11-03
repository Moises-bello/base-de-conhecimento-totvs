---
content_hash: f30aa49400071ce05a028361179822bda6e560ef55a963f443f813e6071c3793
fetched_at: '2026-06-29T00:10:31.890617+00:00'
page_id: '522010778'
product: rm
source: tdn-rm
title: Requisição - Relatório Gerencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=522010778
version: 10
---

No book de relatórios existe os relatórios sugeridos pelo o sistema conforme descrição abaixo:

* 17.001 – Requisição de Pessoal – Aumento de Quadro (REQ)
* 17.002 – Requisição de Pessoal – Desligamento (REQ)
* 17.003 – Requisição de Pessoal – Alteração de Dados Funcionais (REQ)
* 17.004 – Requisição de Pessoal – Transferência (REQ)
* 17.005 – Requisição de Pessoal – Transferência com Alteração de Dados (REQ)
* 17.006 – Requisição de Pessoal – Treinamento(REQ)

Caso necessário customizar os relatórios, a seguir encontra-se a lista com os parâmetros obrigatórios para geração do relatório:

* Substituição e Aumento de quadro
  + CODCOLIGADA; (Coligada da Requisição)
  + CODUSUARIO; (Código do Usuário)
  + TIPOREQUISICAO; (Tipo da Requisição)
  + CODFUNCAO; (Código da Função)
  + CODSECAO; (Código da Seção)

* Desligamento
  + CODCOLIGADA; (Coligada da Requisição)
  + CHAPA; (Chapa do Funcionário demitido)
  + CODPESSOA;  (Código da Pessoa demitida)

* Promoção, Transferência, Transferência com promoção, Treinamento, Abertura de turma
  + CODCOLIGADA; (Coligada da Requisição)
  + CODPESSOA;  (Código da Pessoa promovida e/ou transferida)

* Transferência em Lote
  + CODCOLIGADA; (Coligada da Requisição)
  + TIPOREQUISICAO; (Tipo da Requisição)

Para todas as Requisições acima existe a possibilidade de incluir o também o IDREQ (Identificador da Requisição), sendo esse obrigatoriamente o ultimo a ser acrescentado na lista dos parâmetros. (A partir da versão 12.1.24).

**Observação:** Os parâmetros devem ser inseridos na ordem acima para que os relatórios funcionem corretamente. Para saber se os parâmetros estão na ordem correta basta editar a estrutura e ir na aba Exibição e clicar em Pré-Visualizar, a ordem que os parâmetros são apresentados é como eles estão salvos no relatório.

Não é possível utilizar fontes de dados do tipo Tabelas da Base que não sejam aquelas já utilizadas nos relatórios nativos do sistema. Caso outras informações precisem ser buscadas será necessário criar uma sentença SQL que recebe os parâmetros acima.

Nas sentenças SQL os parâmetros passados tem de ter o mesmo nome dos parâmetros cadastrados.

Exemplo:

Caso estejam cadastrados os parâmetros **CODCOLIGADA** e **IDREQ**a consulta ficaria:

sqlExemplo de Consulta
