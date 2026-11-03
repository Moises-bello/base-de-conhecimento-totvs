---
article_id: 1500004330181
category: Integração RM
content_hash: ea10e3f8c485981e9ed0d0db7794e7e572a93132e0afb140f41180daf03bb39e
fetched_at: '2026-06-28T22:42:36.908575+00:00'
product: protheus
section_id: 360012117913
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Faturamento de O.S integrado ao BackOffice
  RM
type: support-article
updated_at: '2021-09-02T19:57:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004330181-Manufatura-Linha-Protheus-MNT-Faturamento-de-O-S-integrado-ao-BackOffice-RM
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023739612/time.png)** Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como é realizado o faturamento de **Ordem de Serviço - O.S** quando integrado ao **BackOffice RM**?  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Integração RM - Versão 12  
  
**Solução**A partir do módulo de **Manutenção de Ativos - SIGAMNT** quando executando a liberação de uma **Ordem de Serviço - O.S** será enviada a mensagem de **O.S** para o **BackOffice RM**. A **O.S** será enviada sem insumos, pois no **SIGAMNT** os mesmos tratam-se de previstos. O *status* nesse momento do processo no **RM** será **em andamento**.  
Seguindo neste processo, ao finalizar a **O.S** no **SIGAMNT**é enviada uma mensagem ao **Backoffice RM**. Nesse momento serão enviados os insumos e as informações atualizadas. O *status* **finalizada** no **SIGAMNT** torna-se para o **BackOffice RM** - **a faturar**.  
A partir da finalização da **O.S** pelo **SIGAMNT** é enviada uma mensagem ao **RM** permitindo que seja realizado o processo de **Faturamento**. Somente após este procedimento, tendo a **O.S** com *status* **finalizada** no **MNT** é que para sinalizar ao **BackOffice RM** o campo **TJ\_FATURA** é alterado para **1**. A partir deste momento, ainda, a **O.S** não poderá mais ser reaberta.  
Após prosseguir com o faturamento no **RM** é enviada mensagem única ao **Protheus** que procederá com a atualização das informações na **SD3 - Movimentações Internas e** na **STL - Detalhes da Ordem de Serviço**, ou seja, os custos relacionados aos produtos serão atualizados em seus relacionamentos no **Manutenção de Ativos**. O processo, a partir deste instante, tem similaridade com o recálculo do **Módulo de Estoque**.   
  
Passos para realizar o processo:

1. Acessar o **Configurador - SIGACFG**;
2. Ir em **Ambiente / Cadastros / Parâmetros - CFGX017**;
3. Configurar o parâmetro **MV\_NGMNTES - Integração com Estoque** para **S - Sim**;
4. Acessar o **RM** e em **Backoffice / Gestão contábil / Centro de custos**, cadastrar um **Centro de Custo**;
5. Em **BackOffice / Gestão de Estoque, Compras e Faturamento / Cadastros / Produto**, cadastrar um **Produto**;
6. Em **RH / Gestão de Pessoas / Funcionários**, cadastrar um **Funcionário**;
7. Em **BackOffice / Gestão de Estoque, Compras e Faturamento / Cadastros / Ferramentas,**cadastrar uma **Ferramenta**;
8. Em **BackOffice /** **Gestão de Estoque, Compras e Faturamento / Cadastros / Financeiros / Cliente - Fornecedor**, cadastrar um **Fornecedor**;
9. Acessar o **Manutenção de Ativos e Gestão de Frotas - SIGAMNT**;
10. Em **Atualizações / Controle de Oficina / Manutenção / Especialidade - MNTA010**;
11. Ir em **Atualizações / Controle de Oficina / Manutenção / Funcionários - MNTA020**;
12. Cadastrar um **Funcionário** vinculando ao funcionário anterior;
13. Ir em **Atualizações / Controle de Oficina / Ordem de Serviço / Corretiva - MNTA420**, incluir duas **Ordens de Serviço** com todos os insumos cadastrados **previstos**, **ferramenta**, **produto**, **mão de obra - funcionário cadastrado**, **terceiro fornecedor cadastrado** e **especialidade**;
14. Ir em **Atualizações / Controle de Oficina / Retorno de O.S. / Retorno Mod.2 - MNTA435**, filtrar as **O.S's** e buscar uma das **O.S** incluídas. Selecionar todos os insumos previstos e realizar.
