---
article_id: 41292583610775
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5c5ffd1e6a770371b842236b12ac2a40425bc9eccec7b424be314771c6b8bcd4
fetched_at: '2026-06-28T22:38:58.515356+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - NOFUNCW A265VLDEND
  ao acessar MATA265
type: support-article
updated_at: '2026-06-17T20:00:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41292583610775-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEST-NOFUNCW-A265VLDEND-ao-acessar-MATA265
---

O erro "NOFUNCW A265VLDEND" na rotina MATA265 ocorre por desatualização do código-fonte anterior a 06/04/2026, que não inclui a função A265VLDEND, causando falha e travamento. A solução é atualizar o fonte MATA265 para a versão de 06/04/2026 ou superior, aplicando o último pacote acumulado da linha Backoffice.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41292587603863) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Ao acessar ou executar a rotina de Endereçamento (MATA265), o sistema apresenta o erro de compilação ou log "NOFUNCW A265VLDEND" acompanhado da mensagem: InterFunctionCall: cannot find function A265VLDEND in AppMap on {|| Vazio() .Or. (ExistCpo("SBE",M->DA\_LOCAL+M->DB\_LOCALIZ) .And. BloqEndWMS() .And. A265VldEnd())}.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAEST - Todas as versões  
  
**Causa**  
Este incidente ocorre devido à desatualização do código-fonte da rotina MATA265. O arquivo com data anterior a 06/04/2026 não contempla a nova função A265VLDEND, o que ocasiona a falha de validação e o travamento durante a execução do endereçamento.  
  
**Solução**  
A correção definitiva e a função exigida estão contempladas a partir da atualização do fonte MATA265 com data igual ou superior a 06/04/2026. Para regularizar a rotina, é indispensável a aplicação do último pacote acumulado da linha Backoffice.(Não possui o patch pontual do fonte MATA265 com essa data)

[Acumulado BackOffice conforme sua versão](https://tdn.totvs.com/x/2hgdHw) - Aplicar o pacote de expedição contínua e executar o compatibilizador de dicionário (UPDDISTR).

**Saiba Mais**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Travamento na rotina Endereçamento(MATA265).*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36755668788119)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Download do pacote acumulado estoque custos*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29523353602967-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Download-do-pacote-acumulado-estoque-custos)

[*SIGAEST - Movimentações*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
