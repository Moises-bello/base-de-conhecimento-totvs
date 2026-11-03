---
article_id: 29524199528215
category: Financeiro - Contas a Pagar - Comunicação Bancária Online
content_hash: ac992c5c59e01a6f966d4f45aee71a2b70d80fc797e150996c8870b2a1d00d49
fetched_at: '2026-06-28T22:37:49.966817+00:00'
product: protheus
section_id: 26656222001687
source: central-protheus
title: Cross Segmentos - TOTVS BackOffice (Linha Protheus) Contas a Receber - PIX
  - Como realizar a transmissão online via JOB FINA892 e retorno via FINA892A
type: support-article
updated_at: '2025-03-28T16:44:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29524199528215-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Contas-a-Receber-PIX-Como-realizar-a-transmiss%C3%A3o-online-via-JOB-FINA892-e-retorno-via-FINA892A
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29524199519383) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como realizar o envio dos títulos via PIX de forma online ao banco via JOB **FINA892** e também o retorno automático via **FINA892A**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir do release 12.1.2310  
  
**Solução**

A partir da configuração desta rotina é possível realizar o envio e o recebimento dos dados de forma on-line através dos agendamentos FINA892 e FINA892A. Para obter mais detalhes, acesse - Job para envio e retorno de registros em situação de cobrança PIX.

**Verifique o vídeo abaixo de como realizar a configuração / envio do PIX via JOB**

O JOB FINA892 tem o intuito de realizar transmissão dos títulos que estão em situação de cobrança PIX. Já o job FINA892A tem o intuito de realizar a baixa destes títulos previamente transmitidos, com base nas informações coletadas do banco em questão.

O schedule do job pode ser configurado através do módulo Configurador.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29524521640343)

**Configuração do JOB FINA892A**

**Importante**

A configuração do JOB deve ser única por Grupo de Empresas. Sendo necessário cadastrar apenas um agendamento para uma filial que consequentemente puxará as demais.

**Exemplo:**

Empresa T1

Filiais: D MG 01 , D MG 02 , D RJ 01 , D RJ 02 , D SP 01 , D SP 02

Apenas 1 cadastro de agendamento no schedule para 1 Empresa/Filial para que o schedule execute apenas 1 chamada e fique a cargo do job executar para o grupo de empresas todo.

Empresa/Filial = T1/D MG 01 ; → Correto

Empresa/Filial = T1/D MG 01 ;T1/D MG 02 ;T1/D RJ 01 ; → Incorreto

Empresa/Filial = T1; → Incorreto → schedule executa chamada para todas as filiais.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29524411358231)

O parâmetro **MV\_PIXDTHR** é preenchido pelo job FINA892 onde é gravado a data/hora da última execução para que a próxima requisição de dados on-line seja a partir do horário da última requisição.

O parâmetro **MV\_BCOPIX** define a forma de associação do banco, agência e conta com o PIX gerado e possui os seguintes conteúdos:

Igual 1: Pesquisa quantas chaves PIX ativas existem na tabela F70. Caso exista mais do que uma, deverá ser feita associação do banco de forma manual através do Monitor PIX (FINA890);

Igual 2: Forma de associação para banco configurado através da rotina Wizard PIX (FINA893);

Igual 3: não associa a nenhum banco, sendo necessário ser feita associação do banco de forma manual através do Monitor PIX (FINA890).

***IMPORTANTE***

A consulta para baixa dos títulos é encaminhar pelo parâmetro **MV\_PIXDTHR** onde faz a consulta De / Até, ou seja, ao processar o job FINA892A será validada a última data e hora do parâmetro até a data é hora do início do JOB FINA892A  
  
Exemplo:   
  De: 2025-02-28T12:05:01.000001"   
  Ate: 2025-02-28T15:05:01.000001"   
  
O protheus irá encaminhar uma requisição ao banco de 28/02 as 12:05 até 28/02 as 15:05

Os parâmetros mencionados acima são configurados na opção Configurar em Outras Ações na rotina Monitor PIX (FINA890).  
  
**Saiba mais**  
[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)  
[Job para envio e retorno dos títulos em situação de cobrança PIX.](https://tdn.totvs.com/pages/releaseview.action?pageId=742216400)
