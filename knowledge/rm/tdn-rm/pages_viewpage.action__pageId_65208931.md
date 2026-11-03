---
content_hash: 20033a5b13509a472ca86a9a88ca3f0d09fca8b5bf2118fca43c62b8ca18a3dc
fetched_at: '2026-06-29T00:11:12.271735+00:00'
page_id: '65208931'
product: rm
source: tdn-rm
title: RMCTB00003_Log da Consistência de Lançamentos para conversão da Base de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=65208931
version: 7
---

|  |  |  |
| --- | --- | --- |
| OLE\_LINK1OLE\_LINK2**Produto** | : | Totvs Gerstão Contábil - **Versão:** 11.52. |
| **Processo** | : | Consistência de Lançamentos para conversão da Base de Dados. |
| **Subprocesso** | : | Principais Inconsistências apresentadas na Consistência de Lançamentos para conversão da Base de Dados. |
| **Data da Atualização** | : | 14/01/2020 |

**INTRODUÇÃO**   
  
Antes de iniciar o processo de conversão da base de dados para o Novo Modelo BackOffice é necessário executar a 'Consistência de Lançamentos' no RM Saldus, conforme link abaixo:   
  
<http://tdn.totvs.com/pages/viewpage.action?pageId=64651334>   
  
Porém o Log correspondente poderá apresentar inconsistências que impedem a conversão, sendo necessário corrigi-las.   
Sendo assim, segue as principais inconsistências que impedem a conversão da Base de Dados e suas respectivas soluções.   
  
Foram geradas versões do Sistema e da Biblioteca com atualizações, correções e otimizações referente ao processo de 'Consistência de Lançamentos', sendo assim, somente realize o processo citado utilizando a última versão da Biblioteca, do executável do RM Saldus e do RM Conversor.   
  
**CAUSA/SOLUÇÃO**   
  
**LANÇAMENTOS QUE NÃO FORAM POSSÍVEIS ATUALIZAR O CAMPO APLICAÇÃO DE ORIGEM DE ACORDO COM LOTE.**   
  
Essa inconsistência é apresentada, pois existem Lançamentos Contábeis no Lote em questão que não possuem mais relacionamento com o aplicativo de origem (RM Nucleus).   
  
Nesse caso, é orientado realizar 1 (um) dos processos abaixo:   
  
a)Realize a Integração do Lote;  
b) Acesse o Lote, selecione os registros correspondentes e realize a exclusão dos Lançamentos Contábeis apresentados no 'Log da Consistência de Lançamentos'.   
  
**LANÇAMENTOS QUE NÃO POSSUEM RATEIOS EXIGIDOS**   
  
Essa inconsistência é apresentada quando existem Lançamentos em Lote ou na Manutenção de Lançamentos, onde o Rateio a Débito e (ou) Rateio a Crédito não foi preenchido.   
  
Nesse caso, acesse o(s) Lançamento(s) apresentado(s) no Log e realize o preenchimento citado.   
  
Dica: Este procedimento pode ser realizado através da edição dos lançamentos contábeis ou atráves da rotina 'Lançamentos Gerenciais Automáticos' disponível no menu 'Lançamentos'.   
  
**LANÇAMENTOS FORA DO PERÍODO CONTÁBIL – (DATA INICIAL DO PERÍODO) A (DATA FINAL DO PERÍODO).**   
  
Essa inconsistência é apresentada devido à Data de Fechamento indicada nos parâmetros do RM Saldus.   
  
Nesse caso, é orientado acessar o menu 'Opções' / 'Parâmetros' / 'RM Saldus' / 'Lançamentos' / '01.02.01 – Manutenção de Lançamentos' / 'Período Contábil' e alterar ou retirar a Data Fechamento informada.   
  
**SOMA DOS VALORES DO RATEIO A DÉBITO E (OU) A CRÉDITO COM VALOR DIFERENTE DO VALOR DO LANÇAMENTO**   
  
Essa inconsistência é apresentado quando existem Lançamentos em Lote ou na Manutenção de Lançamentos, onde o valor do Rateio a Débito e (ou) do Rateio a Crédito não corresponde ao valor do Lançamento.   
  
Acesse o(s) Lançamento(s) apresentado(s) no Log e realize o preenchimento citado.   
Nota: Esta inconsistência não deverá ser impeditiva para a conversão.   
  
**LANÇAMENTOS QUE CONTÉM CAMPOS NULOS QUE SÃO OBRIGATÓRIOS NO NOVO MODELO.**   
  
Realize o preenchimento dos campos obrigatórios dos 'Lançamentos Contábeis' apresentados no Log, ou realize a exclusão do mesmo pela manutenção de Lançamentos ou pelo Banco de Dados caso seja necessário.   
  
Tabela: CLANCA   
Coligada: CODCOLIGADA  
Referência: LCTREF   
  
**EXISTEM RATEIOS COM CÓDIGO DA COLIGADA DIFERENTE DO CÓDIGO DA COLIGADA DA CONTA CONTÁBIL / GERENCIAL.**   
  
Entre em contato com o suporte, para que seja disponibilizado o script de correção.   
  
**LANÇAMENTOS QUE POSSUEM RATEIOS COM VALOR 0 (ZERO).**   
  
Informa todos os lançamentos que não tem registros de rateios, mas sua conta exige rateios.   
  
Nesta situação o sistema pode apresentar registros na tabela CRATEIOLC com valor de rateio igual a zero (campos VLRDEBITO e VLRCREDITO igual a 0), nesta situação deve-se fazer um select no banco de dados pela referência apresentada no relatório (CAMPO LCTREF) e verificar se o rateio deve ser excluído (via script). Se existir dois registros na CRATEIOLC, um correto e outro incorreto (valor=zero) para o mesmo LCTREF, o registro incorreto deverá ser deletado**.**   
  
**RATEIOS A DÉBITO PARA CONTA A CRÉDITO/ RATEIOS A CRÉDITO PARA CONTA A DÉBITO**   
  
Informa todos os rateios com contas de crédito que têm o valor de débito maior que zero.   
  
Na tabela de lançamentos (CLANCA) a conta que exige rateio foi informada no crédito, porém na tabela CRATEIOLC o campo VLRDEBITO está com valor maior que zero, isto está incorreto, pois o rateio exigido para a conta é a crédito, portanto o campo VLRDEBITO deveria estar igual a zero. Nestes casos realizar a alteração automática é inviável, então o acerto quando ocorrer será feito manualmente regravando o lançamento ou via script. Antes de executar o script deve ser feito select's para confirmar a inconsistência.   
  
Obs.: Regravar um lançamento contábil significa entrar no lançamento alterar as contas contábeis e salvar o lançamento. Após, altere novamente as contas contábeis conforme lançamento original e salve novamente. É importante anotar os dados do lançamento original para deixar o lançamento com as mesmas contas contábeis que se encontrava. Este procedimento na maioria das vezes regrava os dados na tabela de rateios (CRATEIOLC) e após os dados ficam corretos.   
  
**INFORMAÇÕES ADICIONAIS**   
  
Caso necessário, favor realizar os procedimentos de correção em base teste (backup) e somente após avaliar os resultados aplicar em base de produção.   
  
Foram geradas versões do Sistema e da Biblioteca com atualizações, correções e otimizações referente ao processo de 'Consistência de Lançamentos', sendo assim, somente realize o processo citado utilizando a última versão da Biblioteca, do executável do RM Saldus e do RM Conversor. Aplicativos necessários para essas atualizações disponíveis no Portal da Totvs: <http://suporte.totvs.com/home>   
  
  
 **Para maiores informações:**

  **COMUNIDADE** **R**[**@**](https://totvs.byyou.com/?space=rframework)[**Contábil**](https://totvs.byyou.com/?space=rcontbil)

**Canais** **de** **Atendimento:**   
**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)
