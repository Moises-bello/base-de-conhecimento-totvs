---
article_id: 4406624236951
category: TAF - REINF
content_hash: 8431ed631d7f55f5d8f3dec7109ad35ee7828e917885f0e0d3534f739b4c56e8
fetched_at: '2026-06-28T22:41:34.745450+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - TAF - REINF - PAINEL REINF(TAFA552B)
  : R-9000 EVENTO DE EXCLUSÃO '
type: support-article
updated_at: '2023-03-31T16:43:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406624236951-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-PAINEL-REINF-TAFA552B-R-9000-EVENTO-DE-EXCLUS%C3%83O
---

**Dúvida**

Como gerar um evento de Exclusão R-9000 no PAINEL REINF (TAFA552B)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TAF - a partir da versão 25  
  
**Solução**

Em cada evento, na tela de acompanhamento de transmissão, na aba Autorizados, irá aparecer a opção de selecionar o registro e o botão “Excluir Evento R-9000”.

Neste botão haverá 2 opções: Apenas Excluir ou Excluir e Transmitir.

-Ao clicar no opção Apenas Excluir, será exibida uma mensagem para confirmar e prosseguir, através do transmitir no card R-9000 (conforme ilustração abaixo ).

-Ao clicar na opção Excluir e Transmitir, será exibida uma mensagem para confirmar e prosseguir, através do acompanhar no card R-9000.

![](https://tdn.totvs.com/download/attachments/501127780/apurar-exclusao.gif?version=1&modificationDate=1618340636380&api=v2)

Em todos os cards do eventos, irão constar a propriedade Excluídos (responsável pela contagem dos registros excluídos), exceto nos de totalizadores (R-5001 e R-5011) e no próprio R-9000.

![](https://tdn.totvs.com/download/attachments/501127780/image2021-4-13_17-12-6.png?version=1&modificationDate=1618344726873&api=v2)

### Como realizar a transmissão do evento R-9000

Caso o usuário tenha escolhido a opção 'Excluir e Transmitir', não será necessário executar esse passo.

Após a exclusão de algum evento transmitido, o próximo passo é voltar na tela inicial, consultar o período, clicar no card R-9000, opção pendentes e transmitir.

![](https://tdn.totvs.com/download/attachments/501127780/transmitir_exclusao.gif?version=1&modificationDate=1618344281833&api=v2)

**Informações adicionais:**

<https://tdn.totvs.com/display/TAF/EFD-Reinf#EFD-Reinf-EventoR-9000%E2%86%92Exclus%C3%A3odeEventos>
