---
article_id: 360025250712
category: ADVPL - Classe e Função
content_hash: a93b9e9e77936243109d71ecd60f1a56b09fd5f8f1a4ae8c921d090ea3900fbb
fetched_at: '2026-06-28T22:40:17.102939+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Quais as funções
  para realizar a leitura das SXs dicionários?
type: support-article
updated_at: '2024-07-04T18:32:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025250712-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Quais-as-fun%C3%A7%C3%B5es-para-realizar-a-leitura-das-SXs-dicion%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24321532975383)Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**  
Ao tentar migrar não é mais possível a leitura da tabelas **SXs** (Dicionários). Quais as funções para realizar este processo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.23  
  
**Solução**Existem algumas funções que realizarão este processo:

**Listagem das documentações de funções relacionadas ao Dicionário de Dados:**

* [FWGetSX5](https://tdn.totvs.com/display/framework/FWGetSX5)
* [FwPutSX5()](https://tdn.totvs.com/pages/viewpage.action?pageId=286016719)
* [FWX2Nome](https://tdn.totvs.com/display/framework/FWX2Nome)
* [FWX2Unico()](https://tdn.totvs.com/pages/viewpage.action?pageId=330137969)
* [PUTMV()](https://tdn.totvs.com/pages/viewpage.action?pageId=24347029)
* [FWX3Titulo](https://tdn.totvs.com/display/framework/FWX3Titulo)
* [FWSchdByFunction](https://tdn.totvs.com/display/PROT/FWSchdByFunction)
* [FWSchdEmpFil](https://tdn.totvs.com/display/framework/FWSchdEmpFil)
* [FWSIXUtil](https://tdn.totvs.com/display/framework/FWSIXUtil)
* [FWSX1Util](https://tdn.totvs.com/display/framework/FWSX1Util)
* [FWSX2Util](https://tdn.totvs.com/display/framework/FWSX2Util)
* [FWSX3Util](https://tdn.totvs.com/display/framework/FWSX3Util)
* [FWSX6Util](https://tdn.totvs.com/display/framework/FWSX6Util)
* [FillGetDados](https://tdn.totvs.com/display/public/framework/FillGetDados)
* [FWAliasInDic](https://tdn.totvs.com/display/framework/FWAliasInDic)
* [FWModeAccess - Retorna o modo de compartilhamento](https://tdn.totvs.com/display/framework/FWModeAccess+-+Retorna+o+modo+de+compartilhamento)
* [FWX2CHAVE()](https://tdn.totvs.com/pages/viewpage.action?pageId=317304054)
* [FWX2Unico()](https://tdn.totvs.com/pages/viewpage.action?pageId=330137969)
* [FWX3Titulo](https://tdn.totvs.com/display/framework/FWX3Titulo)

**Saiba mais**

* É proibido abrir o arquivo de Empresa(**SIGAMAT**) com **DBUseArea**, deve-se utilizar **[OpenSm0](https://tdn.totvs.com/display/framework/OpenSm0)** ou **[OpenSm0Excl](https://tdn.totvs.com/display/framework/OpenSM0Excl)**;
* É proibido abrir os arquivos de dicionário com **DBUseArea**.

**[Migração do Dicionário de Dados para o Banco de Dados](http://tdn.totvs.com/pages/releaseview.action?pageId=360450442)**

* O dicionário de dados pode ser alterado diretamente por **SQL**?  
  Não pode ser alterado nem pelo banco e nem pelo fonte; apenas pelo configurador do Protheus.

**Montagem de tela**A **[FWSX3util](https://tdn.totvs.com/display/public/framework/FWSX3Util)**devolve os campos necessários para montagem de telas (exemplo a **[MsNewGetDados](https://tdn.totvs.com/display/public/framework/MsNewGetDados)**) que são cobertos por funções do padrão, uma vez que o acesso direto ao dicionário de dados é um ofensor de performance no sistema e impeditivo para a migração ao banco de dados.  
No caso em questão (uso de **SX3**seja para **[MsNewGetDados](https://tdn.totvs.com/display/public/framework/MsNewGetDados)**)  pode utilizar a função **[FillGetDados](https://tdn.totvs.com/display/PROT/FillGetDados)**, que já cria o **aHeader**e **aCols**.  
  
**Saiba mais****[Release 12.1.23 - Expedição em Fevereiro/2019 - FAQs](http://tdn.totvs.com/pages/viewpage.action?pageId=461919278)  
[Funções auxiliares de Dicionários](http://tdn.totvs.com/pages/releaseview.action?pageId=353290193)  
[PutHelp, PutSx1Help e PUTSX1](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027435691)**
