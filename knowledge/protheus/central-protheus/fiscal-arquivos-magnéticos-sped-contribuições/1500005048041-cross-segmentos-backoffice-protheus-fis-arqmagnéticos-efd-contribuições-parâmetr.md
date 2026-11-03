---
article_id: 1500005048041
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 33498023f5f69dead05e98f2572592d1e05d1f2c3681b25c50ec4c96f763678a
fetched_at: '2026-06-28T22:42:06.624392+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  parâmetros de Multithread da Rotina
type: support-article
updated_at: '2025-09-16T11:37:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005048041-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-par%C3%A2metros-de-Multithread-da-Rotina
---

**Dúvida**  
Como habilitar *Multithread* para geração do arquivo Efd Contribuições?  
  
**Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**Para  habilitar *Multithread* na geração do arquivo **Efd Contribuições**, realize os seguintes passos:

1- Verifique no **Configurador** o parâmetro:

**MV\_QTAEC** = Parâmetro define a quantidade de *Threads* que serão utilizadas no proc. *Multithread* do **arquivo da EFD Contribuições**

Para situações onde a quantidade de informações na base de dados do cliente for grande, e a rotina apresentar demora na geração do arquivo **EFD Contribuições**, é sugerido então que realize este processamento em *Multithread*, dividindo assim a carga de processamento e gerando o arquivo em menor tempo.   
Para poder habilitar *Multithread*, deverá alterar o parâmetro **MV\_QTAEC**, neste parâmetro deverá informar a quantidade de *Threads* que irão utilizar na geração do **arquivo txt**, por padrão o conteúdo deste parâmetro é 0 (zero), com este conteúdo a *Multithread* está desabilitada, quando o conteúdo for maior que 1, então automaticamente será habilitada o processamento em *Multithread*.   
Basta somente a alteração deste parâmetro, as demais perguntas e configurações se mantem.

Para habilitar *Multithread no* processamento da Apuração do **EFD Contribuições**, realize os seguintes passos:

1- Verifique no **Configurador** o parâmetro:

**MV\_QTDTAEC** = Parâmetro define a quantidade de *Threads* que serão utilizadas no proc. *Multithread* do **Processamento da Apuração da EFD Contribuições**
