---
article_id: 360051595774
category: TAF - eSocial - eSocial do Futuro
content_hash: dac017b43fa94e93a3a9af7a41bd0f568480fc8f2f1ab4533c807b215a7b27d6
fetched_at: '2026-06-28T22:45:15.868439+00:00'
product: protheus
section_id: 1500001537001
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Como configurar o TAF do
  Futuro (TAF Full/Esocial do Futuro) para a nova tela de monitoramento do e-Social
type: support-article
updated_at: '2024-05-24T19:37:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051595774-RH-Linha-Protheus-TAF-eSocial-ATUALIZA%C3%87%C3%83O-Como-configurar-o-TAF-do-Futuro-TAF-Full-Esocial-do-Futuro-para-a-nova-tela-de-monitoramento-do-e-Social
---

**Dúvida**

Como configurar o TAF do Futuro (eSocial do Futuro/ TAF Full) ?

**Ambiente**

RH - Linha Protheus - TAF - eSocial - À partir da release 12.1.33

**Requisitos**

A rotina do TAF Full (TAF do Futuro) só acessado em Sistemas Operacionais Homologados de acordo com o TDN abaixo:

[SmartClient - Sistemas operacionais homologados](https://tdn.totvs.com/display/tec/SmartClient%2B-%2BSistemas%2Boperacionais)

Se a rotina do TAF Full não funcionar, recomendamos o UPGRADE do seu sistema operacional ou replicar o SmartClient para o sistema operacional homologado:  
[TAF - CONFIGURAÇÃO - Replicando o SmartClient do servidor para outras estações de trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043647533)

**Solução**

1 - Para configurar o TAF Full (TAF do Futuro), o seu ambiente precisar estar atualizado com os últimos pacotes do acumulado. Verifique se seu ambiente está atualizado conforme as últimas expedições e verifique se o sistema esteja com o binário Lobo Guará ou Harpia:

[Automação Fiscal - Atualização - Expedição contínua](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4484557005207)

[Automação Fiscal - ATUALIZAÇÃO - Como atualizar o TAF e o TSS via atualizador? (SEGREGADO)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020127812)

2 - Após certificar que o TAF está atualizado, deverá ativar a porta Multi Protocolo (MPP) de acordo com a documentação abaixo:

[Automação Fiscal - Configuração - Como ativar a porta multi protocolo no TAF - MPP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4477439959063)

**Observação:** Com a configuração do ***MultiProtocolo (MPP)*** não há necessidade de configurar os parâmetros ***MV\_GCTPURL*** e ***MV\_BACKEND***.

Se estiver preenchido as URL's nos parâmetros, **deixe-os em branco** acessando o configurador:  
[TAF - CONFIGURADOR - Como acessar os parâmetros do sistema?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036109233)

Clientes Cloud (T-Cloud) do TOTVS, precisam solicitar a configuração da Porta MultiProtocolo (MPP) para o Cloud:

[Automação Fiscal - Como solicitar suporte TOTVS para o produto, TSS ou Cloud](http://hc/pt-br/articles/4413617765783)

**Outras documentações relacionadas :**

[TAF - CONFIGURAÇÃO - TAF do Futuro – Erros para configurar ou acessar a rotina do TAF do Futuro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405166201623)

[Automação Fiscal - Configuração - Como criar serviço REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413012525591)
