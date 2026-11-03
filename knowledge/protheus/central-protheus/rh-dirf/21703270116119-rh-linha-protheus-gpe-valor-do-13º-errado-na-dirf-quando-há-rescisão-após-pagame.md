---
article_id: 21703270116119
category: RH – DIRF
content_hash: 7ed6a542b81b397e257cc409c3c5637838790a9a023266f34f9a03ec72fd52f2
fetched_at: '2026-06-28T22:44:07.827846+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Valor do 13º errado na DIRF quando há rescisão
  após pagamento da 2ª parcela
type: support-article
updated_at: '2025-06-16T20:19:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21703270116119-RH-Linha-Protheus-GPE-Valor-do-13%C2%BA-errado-na-DIRF-quando-h%C3%A1-rescis%C3%A3o-ap%C3%B3s-pagamento-da-2%C2%AA-parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21703238437911) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Valor do 13º errado na DIRF quando há rescisão após pagamento da 2ª parcela.  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Causa**Configuração de verbas.  
  
**Solução**Além das verbas de proventos de 13º estarem configuradas com **J-Rendimento 13º Salário**, a verba de ID 0247 (Desconto 13º 2ª Parcela Rescisão) também precisa estar configurada com **J** para que os valores de 13º neste cenário fiquem corretos na DIRF.

1. Para corrigir, entre na rotina **Verbas** pelo caminho **>Atualizações >Definições Cálculos >Verbas**, pesquise pelo ID **0247** e clique em Alterar;

2. Na aba **Anuais**, no campo **DIRF**, informe a incidência **J** conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21703270104855)

3. Salve a alteração e gere novamente a DIRF.  
  
  
**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para gerar dados/gerar Arquivo DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437012)   
[RH - Linha Protheus - GPE - Como realizar a configuração das verbas para a DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12278301317911)
