---
article_id: 36581426178711
category: Financeiro - Comissão
content_hash: 0124b7f74298273a40230b4f6666615fedc65ee946f888eaad70e35649e3104e
fetched_at: '2026-06-28T22:37:50.663671+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA440 - Como ajustar o valor
  da comissão?
type: support-article
updated_at: '2026-06-02T18:57:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36581426178711-Cross-Segmento-Backoffice-Linha-Protheus-FINA440-Como-ajustar-o-valor-da-comiss%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36581426161047) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como ajustar o valor da comissão que foi digitado errado?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Antes de efetuar a baixa do título, acione a tecla *F12* para habilitar os parâmetros. Em seguida, na opção “Mostrar comissão”, selecione “Sim”.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36581426162455)

2. Será exibida a tela de valores de comissão, na qual será possível ajustar os valores que deverão compor a comissão do vendedor.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36581463544599)  
Mesmo que a rotina de recálculo de comissão seja executada posteriormente, os valores ajustados manualmente nessa tela não serão alterados.

**Observação:**

A exibição da tela de comissões durante o processo de baixa ocorre devido à configuração dos parâmetros de rotina (Perguntas). Quando o sistema está parametrizado para exibir esses valores, a tela de manutenção de comissões é apresentada de forma automática para conferência ou ajuste, mesmo que o usuário não deseje interagir com ela naquele momento.

Para evitar que a tela seja aberta de forma indesejada, deve-se alterar a configuração da pergunta específica nos parâmetros da rotina de baixa (F12).

Caso deseje desativar a aparição da tela, basta alterar a pergunta 'Mostra Comissão?' para "Não".

**Importante**

Esta atualização foi implementada no backoffice em 11/12/2025.

Caso não seja possível efetuar o cancelamento da baixa do título, o ajuste da comissão não poderá ser realizado por meio das funcionalidades padrão do sistema.

Para atender a essa necessidade, será necessário implementar por meio do ponto de entrada:

[F440FLAGE3 Retorna nome de campo que conterá flag da tabela SE3 (Comissões)](https://tdn.totvs.com/pages/viewpage.action?pageId=877162116)

**Saiba mais**

[Financeiro - Comissão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/26655771327895-Financeiro-Comiss%C3%A3o)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA440 - Pontos de Entrada Recálculos Comissões](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017962152-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA440-Pontos-de-Entrada-Rec%C3%A1lculos-Comiss%C3%B5es)
