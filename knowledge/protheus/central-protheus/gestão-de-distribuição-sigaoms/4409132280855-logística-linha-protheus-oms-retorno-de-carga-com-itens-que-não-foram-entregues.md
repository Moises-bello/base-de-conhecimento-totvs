---
article_id: 4409132280855
category: Gestão de Distribuição (SIGAOMS)
content_hash: 0463c2e90212c67c84407e4ad6ed1d745f13c11d12c91dabdf1cad5797c73def
fetched_at: '2026-06-28T22:45:50.146711+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: 'Logística - Linha Protheus - OMS - Retorno de Carga com itens que não foram
  entregues '
type: support-article
updated_at: '2022-12-01T11:09:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409132280855-Log%C3%ADstica-Linha-Protheus-OMS-Retorno-de-Carga-com-itens-que-n%C3%A3o-foram-entregues
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:18 min****Dúvida**Quais procedimentos no **TOTVS OMS** para **Retorno de uma Carga com itens que não foram entregues**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**No módulo **TOTVS OMS**, temos a **Prestação de Contas**, que ocorre nas rotinas **OMSA320** e **OMSA341**.  
  
Pode ocorrer de uma **carga retornar com itens que não foram entregues pelo motorista**, abaixo descrevemos os procedimentos indicados:

1. **Retorno da Carga**: no programa **OMSA320**, no botão **Outras Ações**, é possível executar a **Devolução**, selecionando a **Nota Fiscal** do produto que não foi entregue da referida **carga**.   
   Nesse processo de geração de **Nota Fiscal de Devolução** irá gerar uma **Nota Fiscal de Entrada** no Sistema, alimentando as tabelas **SF1-Cabeçalho das NF de Entrada** e **SD1-Itens das NF de Entrada.**Para que a geração da **Nota Fiscal de Devolução** ocorra, é necessário que no cadastro de **TES** no programa **MATA080**, na **TES** do tipo **Saída** utilizada na **geração do Pedido de Venda** no programa **MATA410**, tenha uma **TES** do tipo **Entrada** informada no campo **Tes Devol. - F4\_TESDV**.
2. Após a geração da **Nota Fiscal de Devolução**, realizar o retorno dos itens que foram entregues.
3. **Retorno Financeiro**: no programa **OMSA341**, é realizado o processo de **Prestação de Contas**, informando os valores recebidos e devolvidos.
4. Após os procedimentos acima, o **Pedido de venda** vinculado a **Nota Fiscal de Saída x Carga**, será atualizado com *status* igual a **Pedido de Venda Encerrado**.

**Importante**  
Caso desejar faturar novamente, será necessário incluir um **novo pedido** na rotina **MATA410**, em seguida inclui-lo em uma nova carga pela rotina **OMSA200**.**Saiba mais**Mais informações e detalhamento das rotinas citadas acima, poderão ser acessadas nos *link's*:  
[Logística - Linha Protheus - OMS - Quais funcionalidades compreende a rotina de Retorno de Cargas - OMSA320](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063841253-Log%C3%ADstica-Linha-Protheus-OMS-Quais-funcionalidades-compreende-a-rotina-de-Retorno-de-Cargas-)  
[Logística - Linha Protheus - OMS - Quais funcionalidades compreende a rotina de Retorno Financeiro - OMSA341](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027388152-Log%C3%ADstica-Linha-Protheus-OMS-Quais-funcionalidades-compreende-a-rotina-de-Retorno-Financeiro)  
  
**Glossário**  
**MATA080** - Tipos de Entrada e Saída  
**MATA410** - Pedido de Venda**OMSA200** - Montagem de Carga   
**OMSA320** - Retorno da Carga  
**OMSA341** - Retorno Financeiro  
**TES** -  Tipos de Entrada e Saída  
**TOTVS OMS** - Order Management System
