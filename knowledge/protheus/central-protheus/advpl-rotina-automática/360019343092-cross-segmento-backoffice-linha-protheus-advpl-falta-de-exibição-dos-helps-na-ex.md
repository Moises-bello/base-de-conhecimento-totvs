---
article_id: 360019343092
category: ADVPL - Rotina Automática
content_hash: d1f7c9be1cc807c6b1f3fbcd3771bcd84f22356bebc05f360468f4a3b682ff2f
fetched_at: '2026-06-28T22:40:24.101827+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Falta de Exibição dos
  Helps na ExecAuto Mata103 via tela
type: support-article
updated_at: '2021-12-29T15:09:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019343092-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Falta-de-Exibi%C3%A7%C3%A3o-dos-Helps-na-ExecAuto-Mata103-via-tela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao utilizar a rotina Automática MATA103 os Helps de Campos não são apresentados na tela.  
  
**Ambiente**Protheus – ADVPL – A partir da versão 11.80  
  
**Solução**Ao utilizar a rotina Automática da Mata103 com abertura de tela ( Ou seja, com o ultimo parâmetro igual a true) não será exibido os Helps padrões da rotina Padrão, pois mesmo que a rotina esteja abrindo tela, sua validação deverá ocorrer na customização.

O componente Help, utilizado nas validações de campos, possuem uma característica diferente quando a rotina é executada via rotina automática (Execauto). Durante a execução, todos os helps apresentados são acumulados e gravados em um arquivo de log, que é apresentado ao confirmar a inclusão.
