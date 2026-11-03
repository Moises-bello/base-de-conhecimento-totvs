---
article_id: 360053306254
category: RH - Folha de Pagamento
content_hash: c5f8dfdffd54c2710fbf2fd20a524a3178b99a7c803ea602533d474d13e5612a
fetched_at: '2026-06-28T22:44:12.040132+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de auxílio doença e acidente de trabalho
  professores com tarefa variável
type: support-article
updated_at: '2024-09-13T17:17:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053306254-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-aux%C3%ADlio-doen%C3%A7a-e-acidente-de-trabalho-professores-com-tarefa-vari%C3%A1vel
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26355248433815) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**Como parametrizar as verbas de tarefa variável para que sejam consideradas como médias quando o funcionário professor é afastado e deverá ser calculado auxilio doença ou auxilio acidente?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - GPE - Todas as versões

**Solução**O sistema considerará as verbas de tarefa variável dos últimos 6 meses para o cálculo das verbas de auxilio doença (ID 0041) e auxilio acidente (ID 0042) em casos de afastamento de funcionários da categoria professor (categorias **I – Professor mensalista** ou **J – Professor aulista**), mas para isso, é necessário informar as verbas de Tarefas no **mnemônico P\_VBMEDAUX**.

Neste mnemônico deve ser informada apenas as tarefas, as verbas de ID 0033 e 0317 não devem ser informadas nele, pois serão consideradas automaticamente neste cálculo.  
  
Abaixo exemplo de como deve ser informada as verbas no mnemônico:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360089883613)  
  
**OBS.:** Essa parametrização é válida apenas para tarefas variáveis, para tarefas fixas, sistema deve considerar para cálculo dos 15 primeiros dias de afastamento as tarefas fixas.  
  
**Saiba mais**

[Cálculo\_do\_Auxilio\_doença\_e\_acidente\_de\_trabalho\_para\_professores](https://tdn.totvs.com/pages/releaseview.action;jsessionid=524D27456EAACAFFFF671FEA7E1DF2B0?pageId=233764108)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)

[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
