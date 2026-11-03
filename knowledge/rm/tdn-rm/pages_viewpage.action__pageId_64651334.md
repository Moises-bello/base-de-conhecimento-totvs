---
content_hash: 9b767a1314062c919bea6a8f793bb6f97902aec3ce8cc9863e119632cd2d4316
fetched_at: '2026-06-29T00:11:11.190413+00:00'
page_id: '64651334'
product: rm
source: tdn-rm
title: RMCTB00002_Consistência de Lançamentos para conversão da Base de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64651334
version: 8
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | Totvs Gerstão Contábil - **Versão:** 11.52. |
| **Processo** | : | Consistência de Lançamentos. |
| **Subprocesso** | : | Processo de 'Consistência de Lançamentos' para conversão da base de dados. |
| **Data da publicação** | : | 05/07/2013. |

**INTRODUÇÃO**

O Novo Modelo BackOffice, envolve mudanças estruturais significativas nos produtos TOTVS Gestão Contábil e TOTVS Gestão de Estoques, Compras e Faturamento.   
  
Os clientes que iniciaram a implantação do produto na versão 10.80, já contemplam destas alterações. Os demais clientes terão acesso ao Novo Modelo BackOffice a partir da versão 11.40.   
  
**DESENVOLVIMENTO/PROCEDIMENTO**   
  
Para a execução desta conversão, deverá ser executada a rotina de 'Consistência de Lançamentos' dentro do sistema TOTVS Gestão Contábil, conforme mensagem apresentada durante a execução do RM Conversor.   
  
   
  
Nesse caso, antes da conversão da Base de Dados, é orientado acessar o RM Saldus e realizar a consistência de Lançamentos, marcando a opção: 'Preparar a base para a Conversão Novo Modelo BackOffice' e em seguida corrigindo as inconsistências apresentadas no Log.   
  
Obs.: 'RM Saldus' / 'Relatórios' / 'Consistência de Lançamentos';   
   
  
  
  
**OBSERVAÇÕES E DETALHAMENTO DO PROCESSO**   
  
Foram geradas versões do Sistema e da Biblioteca com atualizações, correções e otimizações referente ao processo de 'Consistência de Lançamentos', sendo assim, somente realize a processo de citado utilizando a última versão da Biblioteca, do executável do RM Saldus e do RM Conversor. Aplicativos necessários para essas atualizações disponíveis no Portal da Totvs: <http://suporte.totvs.com/home>   
  
  
Este processo deverá ser executado em todas as coligadas utilizadas na base de dados. Caso alguma coligada não execute tal processo, o sistema não permitirá a conversão da base para o Novo Modelo BackOffice.   
  
  
   
  
O processo de consistência irá preparar a Base de Dados para o Novo Modelo BackOffice, sendo assim, se você não conhece as novidades desse modelo não prossiga na conversão, para mais detalhes sobre o Novo Modelo BackOffice, faça o download do documento 'Novo Modelo BackOffice.zip' no Portal da Totvs: <http://www.totvs.com/suporte>   
  
Caso o sistema apresente inconsistências no Log da 'Consistência de Lançamentos', realize os devidos ajustes conforme orientações dos usuários do sistema. Após os ajustes necessários execute a 'Consistência de Lançamentos' novamente para a coligada em questão. Verifique a solução para as principais inconsistências no Blog da Totvs: <http://totvsconnect.blogspot.com.br/>   
  
Para verificar a efetiva realização do processo citado, acesse novamente o relatório de 'Consistência de Lançamentos', marque a opção 'Preparar a base para a Conversão Novo Modelo BackOffice', avance e verifique a através da coluna 'Status' as coligadas onde o processo foi executado com sucesso.   
  
   
  
Após a execução desta rotina de consistência, a Empresa tem 7 dias para executar a conversão, utilizando o RMConversor. Caso ultrapasse este prazo, o processo deverá ser executado novamente.

 **INFORMAÇÕES ADICIONAIS**  
   
Caso o cliente se encontre no Novo Modelo BackOffice, não será necessário gerar o processo de 'Consistência dos Lançamentos'.   
  
É recomendado que o processo citado seja realizado em base teste e somente após avaliação dos resultados aplicar em base de produção.

  **Para maiores informações:**

**COMUNIDADE** **R**[**@**](https://totvs.byyou.com/?space=rframework)[**Contábil**](https://totvs.byyou.com/?space=rcontbil)

**Canais** **de** **Atendimento:**   
**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)   
**Telefônico:** 4003-0015 Escolhendo as opções: 2 – (Software), 2 – (Suporte Técnico), 3 - (RM), 3 - (Fiscal), 3 - (Nota Fiscal Eletrônica)
