---
content_hash: 3621382d0a84f693f5d6cb119b8973f9fefd02f22c1d0127e3550ecfcb7a7009
fetched_at: '2026-06-29T00:08:20.091670+00:00'
page_id: '268568675'
product: rm
source: tdn-rm
title: TVSDN5_Inclusao_lançamento_financeiro_via_webService
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268568675
version: 115
---

# Inclusão lançamento financeiro via webService

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Função:** | *Inclusão de lançamentos financeiro via WebService* |
| **Situação/Requisito:** | Ao realizar a geração de um lançamento financeiro diretamente pelo Web Service em que o mesmo está com o cadastro desatualizado, atingiu o limite de crédito dentre outras situações, o sistema  apresenta a mensagem que impede incluir o lançamento. |
| **Solução/Implementação:** | Evoluído o processo de inclusão de lançamentos contábeis via web Service para que seja possível informar a autorização no xml para quando ocorrer esse tipos de bloqueio. Lembrando que somente para usuário do tipo Supervisor será aplicado a evolução.    As tags são:  **CliForLimiteCredito**  Autoriza a inclusão/alteração de Lançamentos para Clientes/Fornecedores com Limite de Crédito excedido  **CliForLanAtraso** Autoriza a inclusão/alteração de Lançamentos para Clientes/Fornecedores com Lançamentos em Atraso  **CliForCadastroVencido**  Autoriza a inclusão/alteração de Lançamentos para Clientes/Fornecedores com o Cadastro Vencido  **CliForBloqueado** Autoriza a inclusão/alteração de Lançamentos para Clientes/Fornecedores Bloqueados  **OrcamentoExcedido** Autoriza a inclusão/alteração de Lançamentos com Orçamento excedido    **Exemplo de autorização:**    Autorização de inclusão do lançamento onde o cadastro do cliente esta vencido.  <lanAutoriza>CliForCadastroVencido</lanAutoriza>  Autorização de inclusão do lançamento onde o cadastro do cliente esta vencido e limite de credito foi atingido.  <lanAutoriza>CliForCadastroVencido,CliForLimiteCredito</lanAutoriza>  A autorização para inclusão do lançamento pode ser acumulativa.  <lanAutoriza>CliForCadastroVencido,CliForLanAtraso,CliForLimiteCredito</lanAutoriza>    **Exemplo de xml completo para inclusão de lançamento financeiro:**    <FLAN>  <CODCOLIGADA>1</CODCOLIGADA>  <IDLAN>-1</IDLAN>  <NFOUDUP>2</NFOUDUP>  <CLASSIFICACAO>0</CLASSIFICACAO>  <PAGREC>1</PAGREC>  <STATUSLAN>0</STATUSLAN>  <CODAPLICACAO>F</CODAPLICACAO>  <DATAVENCIMENTO>2015-02-10T00:00:00</DATAVENCIMENTO>  <DATAEMISSAO>2014-08-11T00:00:00</DATAEMISSAO>  <DATAPREVBAIXA>2014-09-10T00:00:00</DATAPREVBAIXA>  <VALORORIGINAL>10,00</VALORORIGINAL>  <CODCOLCFO>1</CODCOLCFO>  <CODCFO>C00314</CODCFO>  <CODCOLCXA>1</CODCOLCXA>  <CODCXA>0001</CODCXA>  <CODTDO>09</CODTDO>  <CODFILIAL>1</CODFILIAL>  <SERIEDOCUMENTO>@@@</SERIEDOCUMENTO>  <CODMOEVALORORIGINAL>R$</CODMOEVALORORIGINAL>  <USUARIO>mestre</USUARIO>  <USUARIOCRIACAO>mestre</USUARIOCRIACAO>  <PreencherRatCCusto>true</PreencherRatCCusto>  <PreencherRatDepto>true</PreencherRatDepto>  <VALORDEDUCAODEPENDENTES>0.0000</VALORDEDUCAODEPENDENTES>  <TIPOCONTABILLAN>0</TIPOCONTABILLAN>   **<lanAutoriza>CliForCadastroVencido,CliForLanAtraso,CliForLimiteCredito</lanAutoriza>**  </FLAN> |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | FIN000022 |

divs
