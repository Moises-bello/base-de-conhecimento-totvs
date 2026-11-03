---
article_id: 360055766854
category: Gestão de Frotas
content_hash: 29010ded19582ce5b257e13bc41a5f02cd09a3eabe2f59551dc5b08860e4d9fd
fetched_at: '2026-06-28T22:42:39.546841+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Parametrização necessária para rotina Ordens
  de Serviço em Lote
type: support-article
updated_at: '2021-08-13T19:22:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055766854-Manufatura-Linha-Protheus-MNT-Parametriza%C3%A7%C3%A3o-necess%C3%A1ria-para-rotina-Ordens-de-Servi%C3%A7o-em-Lote
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:30 min**  
**Dúvida**Qual a parametrização necessária para utilização da rotina **Ordens de Serviço em Lote - MNTA720**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Versão 12  
  
**Solução**Na rotina **MNTA720**, para que seja possível informar um **Fornecedor**, por meio do campo **Fornecedor - TR7\_FORNEC**, é necessário que não apenas esse esteja cadastrado através da rotina **Fornecedores - MATA020**, mas também na rotina de **Custo Fornecedor - MNTA250**.  
  
A mesma regra vale para o campo **Serviço - TR7\_SERVIC**, ou seja, não deve ser apenas cadastrado na rotina de **Serviços - MNTA040**, mas também na rotina de **Custo Fornecedor**. Além disso, no campo **Serviço**, poderão ser utilizados apenas serviços do tipo **Reforma** ou **Conserto de Pneus**, tais serviços são especificados no **Configurador** pelo usuário, através dos parâmetros **MV\_NGSEREF - Código do serviço para Reforma de Pneus** e **MV\_NGSECON - Código de serviço para conserto de pneus. Para utilizar mais de um serviço, separar por ';'.**  
  
A rotina de **Custo Fornecedor** se destina a relacionar **Serviços** com **Fornecedores** e seus custos e especialidades necessárias para realizá-las. Por isso, para que seja feito cadastramento de **Custo Fornecedor** é necessário que o usuário tenha cadastrado anteriormente um **Fornecedor**, um **Serviço** e uma **Especialidade**.  
  
Além disso, deve-se ter em mente que os **Serviços** listados na rotina de **Abertura de Ordens de Serviço em Lote**, são listados de acordo com o **Fornecedor** e **Loja** informados anteriormente, sendo impossível a inserção de qualquer **Serviço** antes de informar esses dois campos.  
  
**Exemplo**

* Acessar o **Configurador** e configurar os parâmetros **MV\_NGSEREF** e **MV\_NGSECON**.
* Acessar o módulo de **Manutenção de Ativos**.
* Em **Atualizações > Controle de Oficina > Cadastros Básicos > Fornecedores - MATA020**, informar um **Fornecedor**.
* Em **Atualizações > Controle de Oficina > Manutenção > Serviços -** **MNTA040**, informar um serviço do tipo **Conserto** ou **Reforma de Pneu**.
* Em **Atualizações > Controle de Oficina > Manutenção > Especialidade - MNTA010**, informar uma **Especialidade**.
* Em **Atualizações > Controle de Oficina > Manutenção > Custo Fornecedor -** **MNTA250**, informar um custo com o **Fornecedor**, **Serviço** e **Especialidade** gerados anteriormente.
* Agora é possível a utilização da rotina de **Abertura de OS em Lote - MNTA720**, informando o **Fornecedor**, **Loja** e **Serviço**.

**Saiba mais**Para informações complementares a respeito da rotina **MNTA720**, verifique o *link* [O.S em Lote (MNTA720 - SIGAMNT)](https://tdn.totvs.com/pages/viewpage.action?pageId=555874154)
