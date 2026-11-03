---
article_id: 360058207174
category: RH - Ponto Eletrônico
content_hash: 350775b07f0f70098b409f792824ce7ec99859e29acecdb82721157dc3d4172c
fetched_at: '2026-06-28T22:44:58.285802+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como desmembrar horas negativas em eventos no banco
  de horas e na folha quando foram informadas
type: support-article
updated_at: '2021-09-13T18:59:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058207174-RH-Linha-Protheus-PON-Como-desmembrar-horas-negativas-em-eventos-no-banco-de-horas-e-na-folha-quando-foram-informadas
---

**Dúvida**Como desmembrar (demonstrar separado, separar) horas negativas em eventos no banco de horas e na folha quando foram informadas na rotina de Integrados -PONA280?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**A partir do momento que é informado manualmente um evento com a quantidade de horas no apontamento, é essa informação que irá ser considerada no cálculo mensal do **Ponto Eletrônico**. A diferença entre o que foi informado e o que foi calculado sera desconsiderada, pois justamente o objetivo dessa manutenção é desprezar o que o sistema calculou e apenas considerar o que foi informado.  
  
A partir do eventos com as horas informadas, existem duas alternativas para configuração dos eventos que serão adicionados no Banco de Horas e para aqueles que serão integrados com a **Folha de Pagamento**, sendo:

1. Definir uma quantidade máxima de horas a serem geradas no banco de horas e o que estiver acima ir para a Folha;
2. Definir um percentual que irá ser gerada no banco de horas e outro que irá ser gerada na Folha.

Caso a necessidade seja priorizar as horas para folha e o resto que estiver acima do limite ir para banco de horas, será necessário aplicar o ponto de entrada **PNM070BH01**.

Abaixo segue o Link do ponto de entrada **PNM070BH01**:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6082529>
