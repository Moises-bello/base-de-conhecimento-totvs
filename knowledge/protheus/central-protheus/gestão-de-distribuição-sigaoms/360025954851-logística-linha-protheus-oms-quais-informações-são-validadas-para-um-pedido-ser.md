---
article_id: 360025954851
category: Gestão de Distribuição (SIGAOMS)
content_hash: d93368701e68dee57f888d0c1f8613d394b12ebf54c6b395d6a297287ddd869a
fetched_at: '2026-06-28T22:45:50.088572+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Quais informações são validadas para um
  pedido ser apresentado na Montagem de Carga
type: support-article
updated_at: '2025-08-21T13:46:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025954851-Log%C3%ADstica-Linha-Protheus-OMS-Quais-informa%C3%A7%C3%B5es-s%C3%A3o-validadas-para-um-pedido-ser-apresentado-na-Montagem-de-Carga
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16204807226647) Tempo aproximado para leitura: **00:04:18 min****Dúvida**Quais informações são validadas para um **Pedido de Venda** ser apresentado na **OMSA200 - Montagem de Carga**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) – Todas as versões  
  
**Solução**Para que a **Montagem de Carga** de um **Pedido de Venda** seja realizada é necessário que:  
  
1. Ao preencher o campo **C5\_TRANSP - Transportadora** na inclusão do **MATA410 - Pedido de Venda,** o parâmetro **MV\_CGTRANS** deverá estar como **.T.** indicando que a **Montagem de Carga** deverá considerar os **Pedidos de Venda** que possuem transportadora informada.  
  
2. Na inclusão do **MATA410 - Pedido de Venda** o campo **C5\_TPCARGA - Carga** deverá estar  igual a **1 - Utiliza**.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000441662)**

3. O **filtro do Grupo de Perguntas** na **Montagem de Carga** deverá ser configurado de tal forma que  considere os **Pedidos de Venda** cadastrados no Sistema.

![Parametro_montagem_carga__3__print_.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024935971)

4. Verificar os **Perguntes** **Data de Entrega De/Até**, que devem ser informados de acordo com o preenchimento do campo **Data de Entrega - C5\_FECENT** dos **Pedidos de Venda**.

![Parametro_data_entrega__4__print___C5_FECENT.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024927032)

5. Os  **Perguntes** **Aglutina por Pedido ou Itens**, contém os seguintes comportamentos:  
**Pedido** - o Sistema irá considerar a **Data Entrega** do **Pedido**, que deverá estar preenchida no campo **Data de Entrega - C5\_FECENT.**  
**Itens** - o Sistema irá considerar a **Data entrega** do **Item** do **Pedido**, que deverá estar preenchida no campo **Data da Entrega -** **C6\_ENTREG.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000439402)

Se selecionado o **Perguntes** **Aglutina por Itens**, o parâmetro **MV\_CGTRANS** deverá estar configurado como **.T.**  
  
6. Verificar a informação do **Tipo de Carga do produto**.  
Para cada produto é possível associar um **Tipo de Carga** específico por intermédio do campo **Tipo Carga - B1\_TIPCAR**. Sendo assim, é necessário verificar sempre se os produtos associados aos **Pedidos de Venda** possuem o campo preenchido e analisar se a informação lançada neste campo de fato procede com um cadastro ativo no Sistema. Se os produtos não pertencerem a um determinado **Tipo de Carga** ou não possuírem o cadastro de **Modelo de Carga**, basta montar a carga sem selecionar esta característica.

![Imagem_montagem_carga_-_tipo_de_carga__5__print___.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360024936351)

7.Caso o ambiente esteja configurado para utilizar a funcionalidade **UBS – Unidade de Beneficiamento de Sementes**, do módulo **SIGAAGR – Gestão de Agroindústria**, é necessário definir o parâmetro **MV\_AGRUBS** com o valor **.T.** Além disso, existe o parâmetro **MV\_AGROEM2**, que indica se o Sistema deve utilizar a **Expedição Modelo 2** na integração com o **SIGAAGR**. Por padrão, esse parâmetro vem habilitado, com valor igual a **.T.** Se a integração com o **SIGAAGR** estiver ativa, mas a **Expedição Modelo 2** não for desejada, o parâmetro **MV\_AGROEM2** deverá ser configurado com o valor **.F.**   
8. Para o **Pedido de Venda** ser apresentado na **Montagem de Carga**, deverá estar **totalmente liberado**, não poderá conter nenhum **tipo de bloqueio na tabela SC9 - Pedidos Liberados**, como por exemplo: **estoque** e **crédito**.  
  
9. A **Montagem de Carga** irá considerar somente pedidos **Não Faturados**.  
  
**Importante**Quando o pedido tem serviço de **WMS - Warehouse Management System**, ele será integrado ao módulo. **Independentemente de montar ou não uma carga para esse pedido de venda, automaticamente será gerada uma ordem de serviço para o WMS** separar e/ou providenciar a montagem de volume, por exemplo. Somente após a finalização da movimentação dessa ordem de serviço no **WMS**, o bloqueio **C9\_BLWMS** será atualizado de **01 - Bloqueado** para **05 - Liberado**. Assim, **a rotina OMSA200 permite a inclusão de pedidos na carga com o bloqueio WMS**, pois o processo no **WMS** ocorrerá somente após a montagem da carga.  
  
**Saiba mais**Mais informações poderão ser acessadas nos *links*:  
[Montagem de Carga - OMSA200](https://tdn.totvs.com/pages/viewpage.action?pageId=551446517)   
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na rotina Montagem de Carga - OMSA200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000900021-Log%C3%ADstica-Linha-Protheus-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-rotina-Montagem-de-Carga-OMSA200)  
[Cross Segmentos - BackOffice Protheus - SIGAFAT - Códigos de Bloqueio gravados na tabela SC9 dos Pedidos de Venda Liberados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017467652-Cross-Segmentos-BackOffice-Protheus-SIGAFAT-C%C3%B3digos-de-Bloqueio-gravados-na-tabela-SC9-dos-Pedidos-de-Venda-Liberados)  
[Logística - Linha Protheus - WMS - Liberação do Bloqueio WMS no pedido de venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/235077668-Log%C3%ADstica-Linha-Protheus-WMS-Libera%C3%A7%C3%A3o-do-Bloqueio-WMS-no-pedido-de-venda)
