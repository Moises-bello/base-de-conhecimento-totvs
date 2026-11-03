---
article_id: 360058407953
category: GESTOR
content_hash: 5b48e3956fd4c79945f6346007c39b483f97be03498929e6adbf64e3ad061fd2
fetched_at: '2026-06-28T22:44:35.607297+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como funcionam os Níveis e o Fluxo de aprovação
  de Solicitações
type: support-article
updated_at: '2026-06-22T19:47:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058407953-RH-Linha-Protheus-MEU-RH-Como-funcionam-os-N%C3%ADveis-e-o-Fluxo-de-aprova%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%B5es
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17123650366231) Tempo aproximado para leitura: 00:06:00 min  
  
Dúvida**Como funcionam os Níveis e o Fluxo de aprovação de Solicitações  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Todas as **Solicitações** realizadas através do **MEU RH,** são encaminhadas para aprovação do RH da Empresa, estas **Solicitações** ficam disponíveis nos módulos envolvidos em **Miscelânea > Portal Protheus > Efetivar Solicitação Portal.**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17088328326423)  
  
É possível também visualizar o aprovador através do  **Meu RH**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19067620143639)  
  
Caso a solicitação já esteja para aprovação dentro do Protheus em **Miscelânea > Portal Protheus > Efetivar Solicitação Portal,** o *status* do responsável irá sair e ficará com o *status* de aguardando efetivação do RH  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/19067620153367)  
  
**Obs**: É importante ressaltar também que o campo **RH3\_MATAPR** (Matricula aprovadora) ficará em branco ao chegar no nível de aprovação do RH. Antes disso ele irá registrar a **matricula** do gestor/responsável em que a solicitação está **pendente** de aprovação.  
  
Verifique os artigos relacionados abaixo para saber como funciona cada tipo de **Solicitação** disponível no **App Meu RH:**  
**[MEU RH - Como registrar a marcação de Ponto através do MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050374233)**  
[**MEU RH - Como registrar a solicitação de Pré-Abono através do MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056545994)  
[**MEU RH - Como registrar a solicitação de Férias através do MEU RH?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058418633)  
**[MEU RH - Como incluir um atestado no MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050895593)**  
  
**IMPORTANTE**:   
Marcações realizadas por **geolocalização,** são efetivadas diretamente sem seguir esse Fluxo de aprovação, devido determinação da própria Portaria que o autorizou.  
  
É possível configurar o Sistema para que haja um ou mais níveis de aprovação antes da Solicitação chegar ao **RH** da Empresa, seguem os dois artigos de apoio para as formas possíveis de configuração:  
**[MEU RH - Como funcionam os Níveis e Fluxo de aprovação de Solicitações Sem Visão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044589134)**  
**[MEU RH - Como funcionam os Níveis e Fluxo de aprovação de Solicitações Com Visão?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047331074)**  
  
**No módulo 18 do Protheus - SIGATCF**, é possível definir quantos níveis de aprovação aquela requisição irá ter, para isso, acesse a rotina Menus.  
  
Selecione o Menu 000006 e em Outras Ações -> Menu.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17122225953559)  
  
Dentro da rotina, terá um menu de Solicitações.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17122300824471)  
  
Nesse submenu, é possível dentro de cada solicitação, cadastrar o **Nível Inicial e a Quantidade de Níveis de Aprovação**, que cada solicitação terá:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17122313859351)  
  
Os campos são:  
- **AI8\_INIAPV** (Nível Inicial): Qual o nível que a aprovação irá iniciar - conteúdo padrão 0  
- **AI8\_APRVLV** (Quantidade de aprovação): Quantas aprovações, aquela requisição precisará ter, antes de ir ao RH atender via rotina Efetivar Solicitação - TCFA040.   
  
**IMPORTANTE:**   
Antes de qualquer ajuste, é importante aprovar ou rejeitar todas solicitações pendentes  
(*Status* 1-EM APROVAÇÃO ou 4- EFETIVAÇÃO RH)  
  
Também sugerimos que não fique **Alternando** entre as duas formas de configuração, caso contrário, poderá ter **registros perdidos** ou encaminhados ao **aprovador errado**.  
  
A única exceção é o **Atestado Médico** que é encaminhado diretamente ao **RH.**  
  
**IMPORTANTE:**   
Caso entenda que o comportamento deva ser diferentes sugerimos que realize a solicitação de uma melhoria através do da **[Central Colaborativa TOTVS](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.  
  
É possível acompanhar as funcionalidades já disponíveis e o planejamento do que está por vir através do [**ROADMAP MEU RH - PROTHEUS**](https://tdn.totvs.com/display/public/NPR/Roadmap+-+Protheus).  
Para saber como criar uma sugestão de melhoria clique **[AQUI](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)**, e para cadastrar uma nova sugestão **[AQUI](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br).**  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
