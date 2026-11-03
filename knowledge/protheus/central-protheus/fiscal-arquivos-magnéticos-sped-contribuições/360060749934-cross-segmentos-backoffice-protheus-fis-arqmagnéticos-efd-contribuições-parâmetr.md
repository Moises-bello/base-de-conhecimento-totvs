---
article_id: 360060749934
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 05b0fb44eff721110b77d8501a571b4d0ae2a17701e88c840fdbb0ecca146603
fetched_at: '2026-06-28T22:42:05.239038+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Parâmetro Utilizado Para Habilitar MultiThread Na Apuração da EFD Contribuições
type: support-article
updated_at: '2023-01-04T18:08:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060749934-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Par%C3%A2metro-Utilizado-Para-Habilitar-MultiThread-Na-Apura%C3%A7%C3%A3o-da-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como habilitar MultiThread na apuração Efd Contribuições?  
  
**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**Para  habilitar **MultiThread** na apuração **Efd Contribuições**, realize os seguintes passos:

1- Verifique no **Configurador** o parâmetro:

**MV\_QTDTAEC** = Define a quantidade de Threads no processamento da apuração da EFD Contribuições. Se conteúdo for 0(zero) a rotina não será processado em **MultiThread**;

OBS: Para situações onde a quantidade de informações na base de dados do cliente for grande, e a rotina apresentar demora no processamento da apuração, é sugerido então que realize este processamento em **MultiThread**, dividindo assim a carga de processamento e gerando a apuração em menor tempo. Para poder habilitar **MultiThread**, deverá alterar o parâmetro **MV\_QTDTAEC**, neste parâmetro deverá informar a quantidade de Threads que irão processar a apuração, por padrão o conteúdo deste parâmetro é 0(zero), com este conteúdo a **MultiThread** está desabilitada, quando o conteúdo for maior que 1, então automaticamente será habilitada o processamento em **MultiThread**. Basta somente a alteração deste parâmetro, as demais perguntas e configurações se mantem.

Mais informações na documentação abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=212896468>
