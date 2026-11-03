---
article_id: 360028597732
category: Manutenção de Ativos (SIGAMNT)
content_hash: dea6b46de0743f83328907cd8d2c50c2122dab6632a78e9a96f1ebe54a6354b3
fetched_at: '2026-06-28T22:42:34.149669+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Informação do Contador obrigatória
type: support-article
updated_at: '2026-01-22T17:11:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028597732-Manufatura-Linha-Protheus-MNT-Informa%C3%A7%C3%A3o-do-Contador-obrigat%C3%B3ria
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37862655262359)* Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Quando é obrigatório informar o **Contador** no **SIGAMNT - Módulo Manutenção de Ativos**?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**  
Será obrigatório informar o contador sempre que:

* Na finalização de **Ordem de Serviço** quando existe uma manutenção preventiva **STF - Manutenção** controlado por Contador, **Tipo de Acompanhamento - TF\_TIPACOM**  igual à: **Contador**, **Tempo/Contador**, **Produção**, **Contador Fixo** ou **Segundo Contador**;
* Em processo de **Movimentação de Estrutura - MNTA470** onde será realizado o repasse de **Contador** para os componentes - **Entrada** ou **Saída.** Exemplo: **Rodízio - MNTA098** e **Movimentação de Pneus - MNTA471**;
* Controle de portaria;
* Abastecimentos;
* Rotinas de informe de contador: **Retorno de Produção - MNTA380**, **Informa - MNTA830**, **Quebra - MNTA840** e **Acerto - MNTA875**.

**Importante**  
Quando é digitado **0 - Zero** na posição do **Contador** é considerado como não informado, ou seja, não grava no histórico de contador.
