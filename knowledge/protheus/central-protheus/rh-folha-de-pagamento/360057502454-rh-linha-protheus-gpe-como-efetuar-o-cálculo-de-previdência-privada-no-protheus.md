---
article_id: 360057502454
category: RH - Folha de Pagamento
content_hash: e91c8bb0058c804049006932ff73f01f326a2956b081c900b8f928d537a81027
fetched_at: '2026-06-28T22:44:13.458920+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o cálculo de previdência privada no
  Protheus
type: support-article
updated_at: '2025-04-15T14:40:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057502454-RH-Linha-Protheus-GPE-Como-efetuar-o-c%C3%A1lculo-de-previd%C3%AAncia-privada-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26250960668695) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como efetuar o cálculo de **previdência privada** no Protheus?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse o cadastro de verbas **GPEA040**  **Atualizações -> Definições de Cálculo -> Verbas** e crie verbas para os identificadores de cálculo abaixo;  
     
   **0215** - Base Previdência Privada Folha

   **0216** - Base Previdência Privada Férias

   **0302** - Base Previdência Privada 13o Salário

   Exemplo verba com id 0215:  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12746750052503)

   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12746729188631)
2. Efetue o lançamento manual da verba em **Atualizações - Lançamentos - Por Funcionário** e posteriormente faça o cálculo do roteiro FOL;  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27704604034199)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/27704604036375)

**Resumo do cálculo:**

Imagem 1 - > Verba C63 corresponde ao **lançamento do valor da previdência privada.**

Imagem 2 -> A verba de **base do Imposto de renda considerando o modelo de tributação completo** sofre o abatimento da verba C63

**Observações:**

Atualmente, as formas disponíveis para cálculo das verbas de Previdência Privada são:

- **Lançamento manual** conforme exemplificado neste artigo

- **Geração de verbas.** Ao invés de lançar manualmente, acesse Miscelânea - Cálculos - Geração de Verbas e gere a verba de Previdência para uma gama de funcionários maior, conforme parâmetros da rotina.

- **Roteiro de cálculo específico.** Para esta opção, orientamos o agendamento de um analista in loco para configurar conforme necessidade, pois o Suporte não auxilia em customizações

|  |
| --- |
| Obs. A Previdência Privada não é uma determinação da CLT, por isso não há uma forma de cálculo automático deste benefício por padrão. |

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
