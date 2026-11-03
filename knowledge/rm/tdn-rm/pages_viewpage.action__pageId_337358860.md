---
content_hash: 0f8e011f7b707ec4a7c71718b586794af22af97cff7262e4b493a452d30e78f1
fetched_at: '2026-06-29T00:08:51.671421+00:00'
page_id: '337358860'
product: rm
source: tdn-rm
title: Eventos com o status 2 - Transmitindo/Aguardando.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337358860
version: 14
---

Existem situações em que ao realizar a transmissão dos eventos do eSocial, alguns eventos não apresentam o retorno do governo na tela de monitoramento e ao acessar o detalhamento para acompanhar a situação do evento é apresentado o status **2 - Transmitindo/Aguardando**:

Nos releases anteriores do TOTVS Automação Fiscal - TAF, ao clicar no botão de inconsistências, o sistema não apresentava detalhes em relação a situação de eventos com o status **2 - Transmitindo/Aguardando.** O sistema apresentava apenas uma mensagem informando que não há mensagens de retorno para este registro:

**Obs**: Dessa forma era possível avaliar as inconsistências apenas habilitando o [rastro de processos pelo TSSINTEFACE](http://tdn.totvs.com/pages/viewpage.action?pageId=337358934).

Diante da necessidade de auxiliar o usuário na avaliação das inconsistências, a equipe de desenvolvimento liberou um patch com uma implementação que permite que o usuário visualize os logs de inconsistências em situações onde o status do evento está como  **2 - Transmitindo/Aguardando:**

**ATENÇÃO!** Para realizar o download do Patch liberado com a implementação da mensagem de inconsistência no Detalhamento [clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=663175).

Lembrando que os Patchs mais atuais estão listados na área "Atualizações Importantes" da página [eSocial | RM - Entregas Legais](http://tdn.totvs.com/display/LRM/eSocial+%7C+RM+-+Entregas+Legais)

 **Dicas:**

**IMPORTANTE!**

Para que os eventos sejam transmitidos com sucesso ao governo, é necessário realizar a liberação completa das URLs do Ambiente Nacional do eSocial no servidor que encontra-se o TSS. Verifique a regra de Firewall para as URLs abaixo:

<https://webservices.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc>

<https://webservices.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc>

<https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc>

<https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc>

<https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/consultarloteeventos/WsConsultarLoteEventos.svc>

<https://webservices.producaorestrita.esocial.gov.br/servicos/empregador/enviarloteeventos/WsEnviarLoteEventos.svc>
