---
article_id: 9480435238295
category: GESTOR
content_hash: f75fb21f5be94f1016ee15c39245f2f1908e049b80706b76320ecaeb708dc11e
fetched_at: '2026-06-28T22:44:35.537128+00:00'
product: protheus
section_id: 10299702833303
source: central-protheus
title: RH - Linha Protheus - Meu RH - GetStructure2 - Visão não encontrada
type: support-article
updated_at: '2026-06-23T21:04:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9480435238295-RH-Linha-Protheus-Meu-RH-GetStructure2-Vis%C3%A3o-n%C3%A3o-encontrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27599202966295) Tempo aproximado para leitura: **00:03:00 min** **Dúvida***GetStructure2* - Visão não encontrada  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Este *log* compreende-se como uma falha da configuração da "visão", ou da estrutura no **Módulo 70 - SIGAORG**, no Protheus.   
  
Também pode ocorrer, **quando é amarrada uma visão incorreta no menu do portal**.  
  
Logo, para corrigir a situação, deve ser realizado o vinculo da visão aos menus do Portal, **como Ponto Eletrônico, Férias, Pagamento, entre outros**, conforme print abaixo como exemplo:  
  
Acesse o Módulo SIGATCF > Atualizações > configurações > Menus![](https://totvssuporte.zendesk.com/attachments/token/GBOsDMMcKxmFPnugAmLWKaND6/?name=image.png)

O menu pode ser acessado no módulo 18 pelo menu **> Atualizações > Configurações > Menus**![](https://totvssuporte.zendesk.com/attachments/token/QX8CkWv6P47jxK5iXvqWNvKmG/?name=image.png)  
  
Posicione sobre o menu da rotina que está apresentando problema, e clique em Editar. Vá no campo **"Visão Aprova"** e vincule uma visão que realmente exista.   
Para verificar as suas visões existentes, você pode acessar o módulo **SIGAORG - Atualizações - Estrutura- Visões.**

![](https://totvssuporte.zendesk.com/attachments/token/O7JknzogK2MuIcXrmwTLfyIsu/?name=image.png)

O código da visão pode ser localizado no módulo 70.  
  
Outro ponto é verificar também se existe departamento amarrado ao colaborador.  
Após, reinicie o serviço do Protheus, acesse o MEU RH e faça novamente o processo devido.  
  
Abaixo, um artigo que fala sobre a configuração das visões e o fluxo de aprovação para melhor entendimento:  
[RH - Linha Protheus - PORTAL GCH - Fluxo de aprovação utilizando MV\_ORGCFG=2](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051101414-RH-Linha-Protheus-PORTAL-GCH-Fluxo-de-aprova%C3%A7%C3%A3o-utilizando-MV-ORGCFG-2)\*\*  
\*esse artigo foi criada para o portal GCH, porém é o mesmo processo no Meu RH.  
  
**Saiba Mais:**[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
