---
article_id: 360020815391
category: Meu RH - Ponto
content_hash: 256ddbd1e0ddd63d8a6bc4e870d08b3834eeabb5b8a40697011ed1683a0dbcc2
fetched_at: '2026-06-28T22:47:30.431065+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Como Habilitar a Inserção de Batidas por Geolocalização
  Portaria 373/2011
type: support-article
updated_at: '2025-03-06T14:31:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020815391-RH-RM-Meu-RH-Como-Habilitar-a-Inser%C3%A7%C3%A3o-de-Batidas-por-Geolocaliza%C3%A7%C3%A3o-Portaria-373-2011
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22275561159703) Tempo aproximado para leitura: 00:06:45 min**

**Dúvida**  
Como realizar a inserção de batidas por geolocalização utilizando Meu RH?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH – 12.1.22  
  
**Solução**Para realizar a inserção de batidas por geolocalização no app **Meu RH**, siga os passos abaixo.

1. No módulo de **Automação de Ponto** da Biblioteca RM, é necessário marcar a opção **Utiliza entrada de batidas da Portaria 373/2011 com geolocalização** no **Parametrizador do Sindicato** para os sindicatos associados aos funcionários que realizarão as marcações pelo app **Meu RH**.  
     
   ![2018-12-11_09_18_10-Assistente_de_Implanta__o_de_Processos__Processo__08.02_-_Parametros_Sindicato__.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360017134271)
2. No perfil associado aos funcionários, é necessário conceder as permissões para a **Portaria 373/2011**. Os menus de permissões podem ser acessados no módulo de **Serviços Globais**, na guia **Segurança** e menu **Perfis**.
3. Selecione o módulo de **Automação de Ponto** na tela de **Perfis** e conceda a permissão à **Portaria 373/2011**, conforme abaixo.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22275652530583)
4. Acessar o Cadastro do funcionário Clicar em **Processos > Utilizar o cartão de ponto** informar a data de inicio da utilização do cartão de ponto. Para mais informações sobre Cartão de Ponto acesse : [Utilizar o Cartão de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004113861-RM-PTO-Utilizar-cart%C3%A3o-de-ponto?source=search)  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013017022)
5. Acesse o app **Meu RH** e selecione a opção **Ponto**.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22275652543127)
6. Com a localização ativada, a tela apresentará link com sua localização atual (coordenadas). Se a localização estiver bloqueada, é apresentada mensagem "**Geolocalização não disponível**", porém **não impede** o registro.
7. Clicando sobre o link é apresentada a localização aproximada através do mapa.
8. Para registrar o ponto, pressione e deslize o botão **Bater Ponto** até a margem indicada.
9. A batida será salva quando o botão apresentar mensagem **Batida Realizada**.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22275699127959)![](https://centraldeatendimento.totvs.com/hc/article_attachments/22275652562839)
10. Para consultar a batida, acesse a função **Espelho de Ponto**.

**Aviso:**

É necessário que tenha uma integração entre os módulos Labore e Chronus, dessa forma acesse **Folha de pagamento| Ambiente| Parâmetros| Integrações entre os sistemas** e verifique a integração entre **RM CHRONUS E RM LABORE,** após marcar a integração reiniciar o host e IIS  para validar a parametrização. **![](https://totvssuporte.zendesk.com/attachments/token/mG7rGeAbQyeSgVwt9rLLLzYJd/?name=inline680345596.png)**

Pré-requisitos técnicos para acesso:

1. Localização habilitada no smartphone.
2. Implementação dos certificados **"HTTPS"** e **"SSL"** no servidor.
3. Android 7.0 ou superior.
4. iOS 9.0 ou superior.

Pré-requisitos legais para utilização:

1. Autorização via Convenção ou Acordo Coletivo de Trabalho.

**Saiba Mais** [Clique aqui Relógio Batidas Remotas - Portaria 373/2011](http://tdn.totvs.com/pages/releaseview.action?pageId=284477421).
