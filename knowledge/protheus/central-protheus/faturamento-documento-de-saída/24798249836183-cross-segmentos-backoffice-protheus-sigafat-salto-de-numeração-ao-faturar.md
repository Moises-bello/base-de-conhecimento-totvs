---
article_id: 24798249836183
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 62f4318003f868a5b2c269caa23bbd784afa0b7a81fb54e1d1883baa1049bd3b
fetched_at: '2026-06-28T22:38:45.367839+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Salto de numeração ao faturar
type: support-article
updated_at: '2024-07-10T20:33:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24798249836183-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Salto-de-numera%C3%A7%C3%A3o-ao-faturar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24798249795991) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**Como solucionar e investigar saltos de numeração ao faturar?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**1 - Certifique-se que na filial em que está faturando, já não existe a numeração faturada, por isso ele não salva o novo faturamento com a mesma numeração, pois já existe.

* Veja na tabela SD2 e SF2, os campos "Documento (D2\_DOC)" e "Documento (F2\_DOC)". Caso já exista com a numeração, o sistema não atribui a ela pois já está usada e marca na próxima disponível.

2 - Caso o passo 1 esteja tudo correto, cheque então, se o parâmetro do ambiente estiver com "MV\_TPNRNFS = 3" a tabela SD9, sendo a numeração do documento de saída.

* Veja no campo "Documento (D9\_DOC)" da filial, se já não está preenchido a numeração que está tentando usar ou que houve o pulo de numeração.

3 - Caso os dois passos anteriores estejam de acordo, veja nos títulos (a receber ou a pagar) gerados, se não há títulos com a numeração que quer faturar.

* Veja no campo "Documento (E1\_NUM)" da filial, já tem um título gerado com o mesmo da numeração que deseja faturar ou que saltou a numeração, pois, o mesmo numero que é gravado nas tabelas SD2 e SF2 é gravado na SE1. Se na SE1 a numeração já está gravada, ele sugere a próxima numeração para manter a integridade.

4 - Ajustar a numeração se ela estiver perdida para que ela siga uma sequência correta:  
Nesse passo, veja como está o seu parÂmetro MV\_TPNRNFS e siga a documentação respectiva:

* [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Controle de numeração via Tabela Genérica SX5](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020160271-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Controle-de-numera%C3%A7%C3%A3o-via-Tabela-Gen%C3%A9rica-SX5)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Controle de numeração da nota de saída via License Server (MV\_TPNRNFS = 2)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020160551-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Controle-de-numera%C3%A7%C3%A3o-da-nota-de-sa%C3%ADda-via-License-Server-MV-TPNRNFS-2)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Controle de numeração da nota de saída via SD9 (MV\_TPNRNFS = 3)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019923012-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Controle-de-numera%C3%A7%C3%A3o-da-nota-de-sa%C3%ADda-via-SD9-MV-TPNRNFS-3?source=search)

OBS: Caso alguma das tabelas acima (SE1, SD2 e SF2) estejam compartilhadas, a filial sempre será em branco, facilitando a concorrência pelo mesmo registro no banco de dados, ocorrendo o salto.

Caso necessite inutilizar uma numeração, orientamos que contate a Equipe SPED!
