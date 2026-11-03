---
article_id: 360018384491
category: Financeiro - Cadastros
content_hash: 8d505f714ff827bb02e996fccba8607c59bfb1250e6caad2a5e3cee91fdb86a0
fetched_at: '2026-06-28T22:37:53.116460+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA490 -Motivo de baixa corrompido
type: support-article
updated_at: '2026-03-04T17:06:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018384491-Cross-Segmentos-Backoffice-Linha-Protheus-FINA490-Motivo-de-baixa-corrompido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37566907382423)** Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
Motivo de baixa corrompido.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Feche o sistema *Protheus*;  
2. Localize na pasta ***system*** do sistema *Protheus* o arquivo **sigaadv.mot**;  
3. Para backup, renomeie o arquivo **sigaadv.mot** para **sigaadv.mot.bkp**;  
4. Execute o sistema *Protheus*;  
5. Acesse a rotina **Contas a Pagar** > **Baixas Pagar Manual. Mesmo processo para o contas a receber.**  
6. Selecione um título > clique em **Baixar**;  
7. O arquivo **sigaadv.mot** será recriado com os motivos de baixa padrões do sistema, conforme realização dos processos de baixas.

**Importante**  
Caso tenha motivos de baixa diferentes do padrão criado pelo sistema *Proteus*, é necessário recriá-los.
