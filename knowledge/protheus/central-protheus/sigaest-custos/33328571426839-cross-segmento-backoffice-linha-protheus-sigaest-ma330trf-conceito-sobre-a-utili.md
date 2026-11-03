---
article_id: 33328571426839
category: SIGAEST - CUSTOS
content_hash: 39a31ac9496b336aeb0b5539dd998beb063b688951868fb47652a7b654bc43c2
fetched_at: '2026-06-28T22:39:02.006169+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MA330TRF - Conceito
  sobre a utilização do Ponto de Entrada
type: support-article
updated_at: '2025-07-08T18:09:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33328571426839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MA330TRF-Conceito-sobre-a-utiliza%C3%A7%C3%A3o-do-Ponto-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33328543355159) Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**

Qual o conceito para utilização do **Ponto de Entrada MA330TRF**?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões   
  
**Solução**

O Ponto de Entrada MA330TRF é utilizado para **determinar o Custo** que será aplicado no **Destino** das Transferências entre filiais. Existem algumas particularidades que devem ser observadas para utilização desse Ponto de Entrada.

1. Para utiização desse Ponto de Entrada o **parâmetro MV\_M330TRF deve estar desabilitado**;
2. O ponto de entrada **somente será executado** quando a origem da transferência não for localizada no processamento. Caso, a origem da transferência esteja contemplada no processamento, será considerado este custo para aplicar no destino e o **Ponto de Entrada** ***não*** **será executado**. ***Por exemplo:*** Quando a origem da transferência ocorreu em um período anterior e o destino da transferência estiver sendo processado no período atual, o ponto de entrada será executado.
3. Caso o **parâmetro MV\_M330TRF estiver habilitado** (habilita busca pelo custo origem das Transferências entre Filiais em períodos diferentes) , este tratamento sobrepõe o retorno do ponto de entrada MA330TRF.

Documentações sobre o Ponto de Entrada veja nos links a seguir:

**PE MA330TRF - Permite determinar o custo que será aplicado no destino da transferência entre filiais**  
[**https://tdn.totvs.com/x/hxNgOQ**](https://tdn.totvs.com/x/hxNgOQ)

**Conceito sobre a utilização do PE MA330TRF**  
[**https://tdn.totvs.com/x/9iVgOQ**](https://tdn.totvs.com/x/9iVgOQ)

**Recálculo do Custo Médio sem concorrência com movimentações de Estoque**  
[**https://tdn.totvs.com/x/m9kSKw**](https://tdn.totvs.com/x/m9kSKw)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre CUSTOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[SIGAEST - MATA330 - Pontos de Entrada da rotina Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003970802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Pontos-de-Entrada-da-rotina-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

[SIGAEST - MATA038 - É possível configurar pontos de entrada com exibição de interface no Acompanha Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8823802604695-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA038-%C3%89-poss%C3%ADvel-configurar-pontos-de-entrada-com-exibi%C3%A7%C3%A3o-de-interface-no-Acompanha-Custos)
