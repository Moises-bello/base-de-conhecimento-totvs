---
article_id: 360043287854
category: GESTOR
content_hash: 2b194e399db334ed662bebda48ea37b7a636f004e0892c2ded99bd102b15b036
fetched_at: '2026-06-28T22:44:35.630945+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Fluxo de aprovação com controle de posto
type: support-article
updated_at: '2026-06-19T14:39:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043287854-RH-Linha-Protheus-MEU-RH-Fluxo-de-aprova%C3%A7%C3%A3o-com-controle-de-posto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24770474322071) Tempo aproximado para leitura: 00:07:00 min**  
  
**Dúvida**  
Como configurar o aplicativo Meu RH para trabalhar com fluxo de aprovação através do controle de posto?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
1- Configurar o parâmetro **MV\_ORGCFG = 1**

![](https://totvssuporte.zendesk.com/attachments/token/Y87S344UU33cUCJIKHJvJAhdC/?name=inline1203433147.png)

2- Realizar a criação do posto  
  
SIGAORG Atualizações > Movimento > Departamento

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059437233)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058532914)

3- Realizar a ocupação destes postos

SIGAORG Atualizações > Movimento > Posto

Selecione o posto clique em atualizar > Outras Ações > Ocupar, aponte o funcionário que irá ocupa-lo

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058533194)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058533274)

4- Cadastre uma visão do tipo 2 comunicação, importante saber que para vagas geradas com controle de posto precisa ser do tipo 2 comunicação.

SIGAORG Atualizações > estrutura > Visão  
Cadastre os posto relacionados

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360058533554)

Após confirmar o cadastro , posicione na visão criada e selecione Outras Ações > Estrutura

Neste momento deve ser apontado quem se reportar a quem .

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059437933)

Dando duplo clique no item da visão é possível visualizar sua alocação.  
  
O meu líder é a matricula do Fabio

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059438073)  
  
Minha alocação funcionário Luís![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059438113)

5- Esta visão deve ser apontada no menu , para isso acesse SIGATCF atualizações > configurações > Menu > portal RH > outras ações > Menu

Neste exemplo estarei usando esta visão para aprovação de abono e marcação do ponto, porém a empresa pode utilizar e qualquer rotina de solicitação.

![](https://totvssuporte.zendesk.com/attachments/token/0m1S2t4TWQZrEQKu3wPuzJotm/?name=inline-331116907.png)

![](https://totvssuporte.zendesk.com/attachments/token/VL9Gj4RNFl8CJqTDcnU1UMfiY/?name=inline-2054234334.png)

6- Realizando uma solicitação pelo aplicativo  
  
Realizado o login com meu funcionário Luis , que irá se reportar ao Fabio  
![](https://totvssuporte.zendesk.com/attachments/token/zHcGjbjuWCq4NM49t6JsF1FOD/?name=inline766916342.png)

Faço minha solicitação

![](https://totvssuporte.zendesk.com/attachments/token/3GcbExqtUniIkVsS1mMIlXKak/?name=inline302317242.png)

![](https://totvssuporte.zendesk.com/attachments/token/CoTgMChpTREy19HnmuVIcGtLj/?name=inline1093738195.png)

7- Gestor ( superior ) irá logar para atender a solicitação  
  
Veja que está notificado a aprovação a ser atendida, gestor selecionar a opção de aprovar.![](https://totvssuporte.zendesk.com/attachments/token/DR8Cqm5sB6Hrop3t8ikyaURhV/?name=inline488959053.png)

Confirma esta aprovação

![](https://totvssuporte.zendesk.com/attachments/token/YnZ5JThKZlGo3PdEUCfl10MFK/?name=inline-231741969.png)

Sistema processa corretamente

![](https://totvssuporte.zendesk.com/attachments/token/7UsiuGwIAaK8rPZlRz9Sy3OUZ/?name=inline2060490620.png)

Se tivesse outras pessoas no fluxo de aprovação o sistema daria continuidade, porém como não existe superior ao Fabio Gestor, o sistema irá direcionar a aprovação do RH.  
  
Para consultar acesse SIGAPON > miscelânea > Portal Protheus > efetivar solicitação.  
  
Posicionar na solicitação gerada > aprovar > conferir se esta correto e > outras ações > aprovar.

![](https://totvssuporte.zendesk.com/attachments/token/kTLD6Hd6bw56weQaczzFljQB3/?name=inline1567847494.png)  
  
Após isso o responsável pelo ponto deverá reapontar o período para que este abono seja considerado nas marcações do funcionário.  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
