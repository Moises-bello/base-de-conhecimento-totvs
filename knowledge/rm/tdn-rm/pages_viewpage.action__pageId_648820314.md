---
content_hash: 343fb8117ae413699de4b6b167bbf40a10aa5d49cff59251a71844e8c9898837
fetched_at: '2026-06-29T00:11:11.753905+00:00'
page_id: '648820314'
product: rm
source: tdn-rm
title: Controle de latência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=648820314
version: 3
---

Para auxiliar na identificação de lentidão no sistema, a nova funcionalidade de verificação de latência de comunicação de rede foi implementada a partir da versão 12.1.34. Essa ferramenta analisa a conexão entre o Client RM e o(s) Host(s) através da porta 8050.

Se a latência exceder os padrões definidos pela TOTVS, uma mensagem de alerta será exibida, informando sobre possíveis problemas na conexão. Esta funcionalidade é útil para determinar se a lentidão percebida deve-se a problemas no processamento do sistema ou a oscilações na rede.

Instabilidades na conexão podem ocorrer em redes que utilizam TCP ou em situações onde o Host e o Client RM estão localizados no mesmo ambiente. Além disso, pode haver lentidão quando o Host está sobrecarregado e não responde adequadamente dentro do tempo esperado de 60ms à porta 8050, verificada via conexão Socket.

**Métodos de avaliação**

Esta verificação é feita baseada na Latência¹ da requisição, basicamente é o tempo que a requisição demora para chegar ao servidor, e não o tempo do processamento no servidor.  
Importante lembrar que a Largura de Banda² não é levada em consideração neste momento.

**Parâmetro** **avaliado pela TOTVS**

* *Latência¹*: Ideal é abaixo de 60 milissegundos. Conexões que responderem acima desse valor irão disparar o alerta em tela durante o período de instabilidade.   
  Este valor não é configurável, nem passível de desabilitação, a mensagem é apresentada para que o usuário tome alguma providência em relação ao consumo de rede e/ou avalie com administrador do sistema as melhorias a serem avaliadas.

**Documentos de referência para conceitos de comunicação:**

1. Latência - <https://pt.wikipedia.org/wiki/Lat%C3%AAncia>
2. Largura de Banda - <https://pt.wikipedia.org/wiki/Largura_de_banda>
