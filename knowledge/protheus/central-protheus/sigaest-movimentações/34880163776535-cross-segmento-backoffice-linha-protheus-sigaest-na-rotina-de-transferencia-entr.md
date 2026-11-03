---
article_id: 34880163776535
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 190b1a489ce300e2ca7e35c87984164583c4623c77867044507c67c028b27b95
fetched_at: '2026-06-28T22:38:57.210608+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Na rotina de Transferencia
  entre filiais MATA310/MATA311 – Transmissão automática da NF-e é possível?
type: support-article
updated_at: '2025-09-12T12:04:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34880163776535-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Na-rotina-de-Transferencia-entre-filiais-MATA310-MATA311-Transmiss%C3%A3o-autom%C3%A1tica-da-NF-e-%C3%A9-poss%C3%ADvel
---

A rotina MATA310/MATA311 no Protheus não possui configuração padrão para transmitir automaticamente a NF-e gerada, pois funciona como um facilitador que chama internamente o ExecAuto do MATA410/MATA461 para criação do pedido e documento de saída. Como alternativa, é possível usar pontos de entrada no documento de saída (MATA461) para automatizar a transmissão da NF-e.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34880189646359) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
A rotina de transferência entre filiais – MATA310/MATA311 possui alguma configuração, job ou forma de que a nota de saída gerada seja transmitida automaticamente, sem que o usuário precise acessar manualmente a rotina NF-e Sefaz para realizar a transmissão?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
A rotina **MATA310/MATA311** atua como um **facilitador**, chamando internamente o **ExecAuto do MATA410/MATA461** para criação do Pedido e do Documento de Saída.  
Por esse motivo, o sistema **não possui configuração padrão** para transmitir automaticamente a NF-e gerada.

Como alternativa, é possível avaliar a utilização de **pontos de entrada no Documento de Saída (MATA461)** para chamar um **ExecAuto da Transmissão da NF-e**.  
Assim, o fluxo pode ser automatizado:

* O **MATA310** gera o Documento de Saída;
* O **Documento de Saída (MATA461)** chama automaticamente a **Transmissão da NF-e**.

[Referência:](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7224837938327-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pontos-de-Entrada-na-rotina-de-Prepara%C3%A7%C3%A3o-de-Documento-de-Sa%C3%ADda-MATA460-e-MATA461)  
[Cross Segmentos - Backoffice Protheus - SIGAFAT - Pontos de Entrada na rotina de Preparação de Documento de Saída (MATA460 e MATA461)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7224837938327-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Pontos-de-Entrada-na-rotina-de-Prepara%C3%A7%C3%A3o-de-Documento-de-Sa%C3%ADda-MATA460-e-MATA461)

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)

[*SIGAEST - MATA310/MATA311 - Transferência entre Filiais utilizando o parâmetro MV\_FILTRF*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011717052-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Transfer%C3%AAncia-entre-Filiais-utilizando-o-par%C3%A2metro-MV-FILTRF)

[*SIGAEST - MATA310/MATA311 - Como estornar Solicitações de Transferência entre Filiais?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12728743784087-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-estornar-Solicita%C3%A7%C3%B5es-de-Transfer%C3%AAncia-entre-Filiais-)

[*SIGAEST - MATA310 MATA311 - Como configurar tabela de preços para as Transferências?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8552373360023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-tabela-de-pre%C3%A7os-para-as-Transfer%C3%AAncias-)

[*SIGAEST - MATA310/MATA311 - Pontos de entrada da rotina Transferência entre Filiais*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003854082-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Pontos-de-entrada-da-rotina-Transfer%C3%AAncia-entre-Filiais)

[*SIGAEST - Help PV BLOQUEADO na rotina de Transferência entre Filiais (MATA310 e MATA311)*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024378631-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Help-PV-BLOQUEADO-na-rotina-de-Transfer%C3%AAncia-entre-Filiais-MATA310-e-MATA311-)
