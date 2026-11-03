---
article_id: 360051754474
category: GPE - eSocial - Não Periódicos
content_hash: 87263c1c9952d2492d8fe2bd64cbca597f4c10c9e2ff999a48b2cfe4e6d58915
fetched_at: '2026-06-28T22:45:04.323729+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - Error log  rescisão: T3Gxxx: DB error (Insert):
  -37 File: T3Gxxx - Error : 2601 (23000) (RC=-1) - [Microsoft][SQL Server Native
  Client 11.0][SQL Server]Cannot insert duplicate key row in object ''dbo.T3Gxxx''
  with unique index'
type: support-article
updated_at: '2026-06-16T13:01:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051754474-RH-Linha-Protheus-GPE-Error-log-rescis%C3%A3o-T3Gxxx-DB-error-Insert-37-File-T3Gxxx-Error-2601-23000-RC-1-Microsoft-SQL-Server-Native-Client-11-0-SQL-Server-Cannot-insert-duplicate-key-row-in-object-dbo-T3Gxxx-with-unique-index
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41261152162071) Tempo aproximado para leitura: 01:00 min**  
  
**Ocorrência**  
Ao tentar gravar uma Rescisão, através da rotina **GPEM040**, é apresentado o *error log:*  
**T3Gxxx:** ***DB error*** **(*****Insert*****): -37 File: T3Gxxx -** ***Error*** **: 2601 (23000) (RC=-1) - [Microsoft][SQL** ***Server Native Client*** **11.0][SQL** ***Server*****]*****Cannot insert duplicate key row in object*** **'dbo.T3Gxxx'** ***with unique index*** **'T3Gxxx\_UNQ'.** ***The duplicate key value is*** **(xxxx, xxxxxx, xxxxxxxxxxxxxx, Rxxxxxxxxxxxx                , xxxxxx, xxxxxx, x). (** ***From tISAMFile::Write*** **).**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Este erro ocorre devido a parametrização incorreta das verbas com os identificadores 0015 e 0066 para empresas que efetuam o pagamento no último dia do mês  
  
**Solução**  
**1.** Este erro ocorre devido a parametrizações incorretas das verbas com os Identificadores de cálculo **0015** e **0066** nas empresas que efetuam o pagamento do salário no último dia do mês (regime de competência). Para solucionar essa ocorrência, necessário acessar a rotina de **Cadastro de Verbas**, em **GPEA040**, efetuar a busca pelas verbas com os identificadores citados acima e efetuar a exclusão de dados do campo **V. Mes Segui**. Estes campos devem ser preenchidos quando as empresas efetuam o pagamento por **Regime de Caixa**, para que sejam geradas as verbas de Base de Imposto de Renda Mês Anterior e Desconto de Imposto de Renda Mês Anterior que serão utilizadas no cálculo de Imposto de Renda do roteiro ADI, Adiantamento.  
**2.** Em seguida deverá efetuar a exclusão da sujeira gerada pela rotina de **Fechamento Mensal**, **GPEM120** no mês anterior, das verbas com os identificadores de cálculo **0106** e **0107** nas tabelas **SRC/SRD** e **RGB**.  
  
**Saiba Mais**  
Para saber mais consulte os *links*abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[*TOTVS Informa*](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "**Eventos**".*
