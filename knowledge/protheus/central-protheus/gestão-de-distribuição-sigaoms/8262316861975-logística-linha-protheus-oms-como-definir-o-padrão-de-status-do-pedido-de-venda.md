---
article_id: 8262316861975
category: Gestão de Distribuição (SIGAOMS)
content_hash: 6cd626f7ab40d6f4b7f51438574e27b11dce68436893ce8d22c37eac5abdb93b
fetched_at: '2026-06-28T22:45:49.658640+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como definir o padrão de Status do Pedido
  de Venda para Desatualizar um Pedido de Venda integrado no TOL/TRE
type: support-article
updated_at: '2022-10-19T16:47:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8262316861975-Log%C3%ADstica-Linha-Protheus-OMS-Como-definir-o-padr%C3%A3o-de-Status-do-Pedido-de-Venda-para-Desatualizar-um-Pedido-de-Venda-integrado-no-TOL-TRE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:54 min** **Dúvida**Como definir o padrão de ***Status* do Pedido de Venda para Desatualizar um Pedido de Venda** integrado no **TOL/TRE**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**Na rotina **OMSXCPL6-Envio de Pedidos**, caso necessite **cancelar uma sequencia integrada ao TOL/TRE**, porém o **Pedido de Venda está com *status* igual a 3-Falha na Integração campo C6\_INTROT**, o Sistema contém uma trava que impede desatualizar a sequencia integrada.  
  
Para esse cenário,  temos um novo tratamento que possibilita optar por qual *status* será considerado no processo de **desatualização do Pedido de Venda integrado** com **TOL/TRE**, são eles:

* Campo **C6\_INTROT - Integração Roteirizador**
* Campo **DK3\_STATUS - *Status* da Integração**

O Sistema irá considerar o campo **C6\_INTROT** para desatualizar o **Pedido de Venda** no **TOL/TRE**.  
Para considerar o campo **DK3\_STATUS**, deverá utilizar o Parâmetro **MV\_CPLCDK3 = .T.**  
  
Exemplo de utilização:  
  
1.No **SIGACFG-Configurador do Protheus/Ambiente/Cadastros/****Parâmetros**, ative o Parâmetro **MV\_CPLCDK3 = .T.**2.Acesse a rotina **MATA410-Pedido de Venda**, crie um **Pedido de Venda** com 3 itens e quantidades Liberadas:

**![pedidovenda.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/8264093625495/pedidovenda.jpg)**

3.Acesse a rotina **OMSXPL6-Envio de Pedidos**, **altere a quantidade** a ser enviada na integração:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8270352457879/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8270390939031/mceclip2.png)

Nesse exemplo, será integrado quantidade total do item 01, quantidade parcial do item 02 e para item 03 não será integrado:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8270416092823/mceclip3.png)

4.Na rotina **OMSXPL6-Envio de Pedidos**, após confirmar as alterações acima, envie o **Pedido de Venda** para o **TOL/TRE**:

**![ok_envio_oscpl6.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/8270532996375/ok_envio_oscpl6.jpg)**

**5.**No **TOL/TRE, gere a Viagem** para o **Pedido de Venda** integrado e **libere para o Protheus.**  
  
**6.**Acesse a rotina **OMSXCPL07-Monitor de Cargas,** com a viagem liberada, **gere a carga**:

**![omsxcpl7.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/8270563377175/omsxcpl7.jpg)**

**7.**Acesse a rotina **MATA460A-opção de Estorna DOC's** e **exclua a liberação do item 03 quantidade 70**. Essa sequencia não foi integrada ao **TOL/TRE**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8270679293847/mceclip4.png)

8.Retorne para a rotina **OMSXCPL6-Envio de Pedidos**, selecione o **Pedido de Venda** e envie ao **TOL/TRE**. Nesse momento o *status* do **Pedido de Venda** será atualizado para **3-Falha de Integração**. Devido não existir a **SC9-Liberação de itens** para o item que tentou integrar ao **TOL/TRE**. Será apresentada a mensagem abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8270880360983/mceclip5.png)

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8270918103703/mceclip6.png)**

**9.**Acesse a rotina **OMSXCPL6-Envio de Pedidos**, desatualize o **Pedido de Venda** utilizando a opção **Desatualizar Pedido Posicionado - F4**:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8271016894743/mceclip7.png)

10.Após **confirmar a desatualização parcial do pedido**,  acesse o **Painel de Viagens do** **TOL/TRE** para verificar a **Viagem**. Poderá visualizar que a **Viagem** consta apenas com o **item 01 de 50**:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8271074029463/mceclip8.png)

11.Retorne a **rotina OMSXCPL6-Envio de Pedidos**, posicione no **Pedido de Venda** em questão e utilize o botão de **Outras Ações/Desatualizar Pedido Selecionado F2:**

**![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8271210422807/mceclip9.png)**

**![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8271269713943/mceclip10.png)**

**12.**Consulte o **Painel de Viagens do TOL/TRE** para verificar a **Viagem** foi **Excluída**:

**![apos_cancelar_total_no_oms_viagem_cancelada_TOL.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/8271372101399/apos_cancelar_total_no_oms_viagem_cancelada_TOL.jpg)**

**13.**No **OMSXCPL07-Monitor de Cargas**, a **Viagem** será atualizada com ***status* de cancelada** e a **carga será desfeita.**No exemplo acima, demonstramos **as duas formas de Desatualizar um Pedido de Venda integrado ao TOL/TRE**, utilizando as opções abaixo:

* botão de **Outras Ações/Desatualizar Pedido Selecionado F2**
* tela principal **OMSXCPL6-Envio de Pedidos botão Desatualizar Pedido Posicionado - F4**

**Saiba mais**Mais informações poderão ser acessadas nos ***link's*:**[14756060 DLOGWMSMSP-14447 DT TOTVS OMS x TOL - Desatualização de pedidos com o campo C6\_INTROT = 3](https://tdn.totvs.com/pages/viewpage.action?pageId=704924683)  
[Integração TOTVS OMS x TOTVS Otimização Logística Planejamento](https://tdn.totvs.com/pages/viewpage.action?pageId=268801735)  
[Logística - Linha Protheus - OMS - Cancelamento de Pedidos de Venda integrados ao TOL/TRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012128902-Log%C3%ADstica-Linha-Protheus-OMS-Cancelamento-de-Pedidos-de-Venda-integrados-ao-TOL)  
[Logística - Linha Protheus - OMS - Cancelar Viagem gerada no TOL/TRE, quando integrada ao TOTVS OMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409677400343-Log%C3%ADstica-Linha-Protheus-OMS-Cancelar-Viagem-gerada-no-TOL-quando-integrada-ao-TOTVS-OMS)  
  
**Glossário**  
**TOL** - TOTVS Otimização Logística   
**TRE** - TOTVS Roteirização e Entrega  
**TOTVS OMS** - Order Management System
