---
article_id: 1500012128902
category: Gestão de Distribuição (SIGAOMS)
content_hash: fedd41faae5df9e7c78544e448756c25d34585e523d1036f06423c206b475faf
fetched_at: '2026-06-28T22:45:49.580103+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Cancelamento de Pedidos de Venda integrados
  ao TOL/TRE
type: support-article
updated_at: '2022-12-01T11:02:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012128902-Log%C3%ADstica-Linha-Protheus-OMS-Cancelamento-de-Pedidos-de-Venda-integrados-ao-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:04:42 min**  
**Dúvida**Como realizar o **Cancelamento de Pedidos de Venda,** utilizando a rotina **Envio de Pedidos de Venda - OMSXCPL6**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**A rotina **Envio de Pedidos de Venda - OMSXCPL6,** permite que os pedidos de venda sejam **cancelados** no **TOL/TRE** de forma **Parcial** ou **Completa**, utilizando as seguintes opções:

* **Desatualizar Pedido Posicionado - F4:** Permite selecionar a sequência que terá a integração cancelada. Também permite efetuar o cancelamento parcial de uma sequência de integração pela digitação da Quantidade do Cancelamento.
* **Desatualizar Pedidos Selecionados - F2:** Permite efetuar o cancelamento de todas as sequências de integração, de todos os pedidos selecionados no **browse**.

Uma vez o pedido integrado ao **TOL/TRE**, ao realizar o cancelamento por uma das opções acima, o **TOTVS OMS** dependerá da resposta retornada pelo **TOL/TRE**, **permitindo ou não o cancelamento.**  
Os parâmetros abaixo interferem no cancelamento do pedido:

* **MV\_CPLATVG** - Atualiza viagem no **TOL/TRE** ao cancelar a integração do pedido.
* **MV\_CPLESCG** - Permite estorno automático da carga ao cancelar ou reprogramar viagem.

Os parâmetros acima, requerem configurações por parte do **TOL/TRE**.  
  
Caso o parâmetro **MV\_CPLATVG**, estiver ativo em conjunto com as devidas parametrizações do **TOL/TRE**, **todas as viagens** das sequências de integração selecionadas serão canceladas automaticamente. Por este motivo, **recomenda-se cautela ao utilizar a opção de cancelamento de todos os pedidos selecionados**.  
Exemplo de utilização:**Cancelar a Integração de Pedidos em Lote**Na tela **Envio de Pedidos de Venda - OMSXCPL6**, selecione os Pedidos cuja integração serão canceladas. Confira os Pedidos selecionados e clique em **Desatualizar Pedidos Selecionados - F2**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019824141/mceclip0.png)

**Cancelar ou Alterar a Integração do Pedido ou Quantidade Específica**Na tela **Envio de Pedidos de Venda - OMSXCPL6**, posicione o cursor sobre o Pedido que será alterado ou cancelado. Selecione os itens cuja integração será cancelada. Também é possível editar o campo **Qtd. Cancelamento**, caso seja necessário cancelar apenas uma parte do item. Observe que, por padrão, a opção para **marcar todos os itens da sequência selecionada**, no canto inferior esquerdo da tela, encontra-se **ativa**, contudo é possível editá-la de acordo com a necessidade. Confira os itens e as quantidades selecionadas e confirme o cancelamento.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019828301/mceclip4.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500019828221/mceclip3.png)

Nos processos descritos acima, no final do processamento será apresentado um resumo do cancelamento do Pedido no **TOL/TRE**. Este resumo alertará se ocorrer alguma inconsistência no cancelamento, sendo que este também será gravado na **tabela DJW - Registro de Falhas CPL**. Para consultar as inconsistências ocorridas, clique em **Consultar Registro de Falha - F7**.  
  
Ao efetivar o cancelamento, as seguintes **tabelas** sofrerão **alterações** ou **inclusões**:  
  
**DK3 - Tabela de Sequência de Integração do Pedido:** será atualizado o campo **status da sequência de integração -** **DK3\_STATUS** para **3-Cancelado Parcial**, quando apenas parte da sequência é cancelada, ou então para **2-Cancelado**, quando toda a quantidade da sequência é cancelada no **TOL/TRE**.  
  
**SC6 - Itens do Pedido de Venda:** será atualizado o *status* do campo **Status da Integração - C6\_INTROT** para igual a **1-Não Integrado**, quando apenas parte do item teve a integração cancelada, será atualizado o *status* igual a **4-Integrado Parcial**, quando parte da quantidade do item permanecerá integrada.  
  
**Saiba mais**  
Mais informações poderão ser acessadas nos *link's*:  
[Logística - Linha Protheus - OMS - Como definir o padrão de Status do Pedido de Venda para Desatualizar um Pedido de Venda integrado no TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8262316861975-Log%C3%ADstica-Linha-Protheus-OMS-Como-definir-o-padr%C3%A3o-de-Status-do-Pedido-de-Venda-para-Desatualizar-um-Pedido-de-Venda-integrado-no-TOL?source=search)  
[Envio de Pedidos de Venda - OMSXCPL6](https://tdn.totvs.com/pages/releaseview.action?pageId=549492947)  
[Logística - Linha Protheus - OMS - Envio de Pedidos do TOTVS OMS para TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011610682-MP-OMS-Envio-de-Pedidos-do-TOTVS-OMS-para-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Integração Protheus TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061123194-MP-OMS-Integra%C3%A7%C3%A3o-Protheus-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
[Logística - Linha Protheus - OMS - Como habilitar geração de arquivo de LOGs na integração do TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060684834-MP-OMS-Como-habilitar-gera%C3%A7%C3%A3o-de-arquivo-de-LOG-na-integra%C3%A7%C3%A3o-do-SIGAOMS-x-Cockpit-Log%C3%ADstico-Neolog)  
[Logística - Linha Protheus - OMS - Pontos de Entrada disponíveis na Integração TOTVS OMS x TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003568682-MP-OMS-Pontos-de-Entrada-dispon%C3%ADveis-na-Integra%C3%A7%C3%A3o-TOTVS-OMS-x-TOTVS-Otimiza%C3%A7%C3%A3o-Log%C3%ADstica)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
