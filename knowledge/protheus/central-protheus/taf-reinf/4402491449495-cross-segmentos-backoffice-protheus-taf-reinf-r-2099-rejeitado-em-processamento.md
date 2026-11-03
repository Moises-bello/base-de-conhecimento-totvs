---
article_id: 4402491449495
category: TAF - REINF
content_hash: e3ef11aef8a4a2b06b6b807d920b923a21927b41ce285186d3035a506684bd09
fetched_at: '2026-06-28T22:41:33.585217+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF -  R-2099 Rejeitado - EM
  PROCESSAMENTO
type: support-article
updated_at: '2023-03-31T16:54:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402491449495-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-R-2099-Rejeitado-EM-PROCESSAMENTO
---

**Ocorrência**Ao transmitir o R-2099, ele retorna como **Rejeitado/Inconsistente** e ao visualizar a inconsistência, é exibido um XML escrito "EM **PROCESSAMENTO**".

**Ambiente**TAF - SIGATAF - A partir de 12.1.17  
  
**Causa**

Esse erro ocorreu devido a um incidente no TSS no qual foi corrigido com um patch pontual do TSS, liberado dia 11/06/2021.

**Solução**  
  
Para correção do R-2099 que foi transmitido **antes** da aplicação da Expedição Contínua do TSS de junho/2021, será necessário seguir rigorosamente o procedimento abaixo:

1 - Obrigatório possuir o pacote de Expedição Contínua Junho/2021 do TSS **+ Patch Pontual**, disponibilizado no RPO abaixo, basta apenas substituir o seu RPO atual pelo o do link abaixo:

* [MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)

2 - Acessar o Smartclient do TSS e executar o seguinte: u\_ajustaEv2099

![AJUSTAR2099.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4402491183895/AJUSTAR2099.png)

OBS: Caso o seu smartclient do TSS ocorra erro ao abrir, revisar as configurações do appserver.ini e smartclient.ini e se tudo estiver correto, atualizar o binário do TSS: <https://tdn.totvs.com/x/tGjNI>

3 - Após 5 minutos, acessar a rotina de monitoramento do Reinf  e monitorar novamente o evento.

SE: **o periodo estiver fechado no e-cac**

Caso o evento retorne com a inconsistência MS0037 OU MS1078, reabrir pelo e-cac e transmitir o evento novamente.

SE: no e-cac esteja em **aberto**, transmitir o evento R-2099 novamente.

Caso a solução acima não solucione o problema, abrir um chamado com a equipe TOTVS para análise do incidente, anexando as evidências necessárias.
