---
article_id: 21154515818007
category: Originação de Grãos (OG)
content_hash: eedea20245814c6a4fa37be4dcfed9ae9248b99d2f16c3b94ed06223f2c8189c
fetched_at: '2026-06-28T22:45:45.297579+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Visão Geral - Função do Ponto de entrada OG250RDEL
type: support-article
updated_at: '2025-06-24T19:41:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21154515818007-Agro-Linha-Protheus-AGR-Vis%C3%A3o-Geral-Fun%C3%A7%C3%A3o-do-Ponto-de-entrada-OG250RDEL
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21154559443479) Tempo aproximado para leitura: **00:00:45 min  
  
Dúvida**Qual a função do ponto de entrada **OG250RDEL**? **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12 **Solução**Para solucionar essa dúvida, realize os seguintes passos:

**1.** Analise os Dados Gerais;

|  |  |
| --- | --- |
| Linha de Produto: | Microsiga Protheus |
| Segmento: | Agroindústria |
| Módulo: | SIGAAGR |
| Função: | OGA250R - Complemento de Romaneios |
| Requisito/História/Problema (informe o requisito relacionado) : | DAGROCCO-1102 |

**2.** Crie ponto de entrada para disponibilizar a filial e código do romaneio, na reabertura do romaneio;

**3.** Crie o Ponto de entrada **OG250RDEL** para ser utilizado com retorno esperado de a*rray* de 2 posições **Filial** , **Romaneio**.

Ex: 

**FUNÇÃO USUÁRIO OG250RDEL()**

**Local cFill := PARAMIXB[1]**  
**Local cRoman:= PARAMIXB[2]**

**Alert('Filial: '+cFill + 'Romaneio: ' + cRoman)**

**VOLTAR.T.**
