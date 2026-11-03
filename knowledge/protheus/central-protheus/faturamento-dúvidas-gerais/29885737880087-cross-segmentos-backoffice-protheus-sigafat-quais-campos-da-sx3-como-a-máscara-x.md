---
article_id: 29885737880087
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d0ed625ca2dd34fb9f103ccb8e023371c2cce007047aa23d92d4e36b7d743648
fetched_at: '2026-06-28T22:38:33.058848+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Quais campos da SX3 como
  a Máscara (X3_PICTURE) são alterados ao Executar o UPDDISTR?
type: support-article
updated_at: '2025-02-18T14:18:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29885737880087-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Quais-campos-da-SX3-como-a-M%C3%A1scara-X3-PICTURE-s%C3%A3o-alterados-ao-Executar-o-UPDDISTR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29885737822231) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Quais campos da SX3 são alterados ao Executar o UPDDISTR?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Quando o cliente executa a ferramenta **UPDDISTR**, a qual atualiza os dicionários do sistema, a configuração original de alguns campos da **SX3** podem ser restaurados para a configuração nativa do dicionario. Isso ocorre porque certos campos não são liberados para personalização pelo usuário, causando reversões da modificação.

Exemplo:

No Protheus, o campo Máscara **(X3\_PICTURE)** é responsável pela formatação dos dados no Protheus, determinando como são armazenados e exibidos. Alguns campos por padrão possuem uma Picture numérica fixa (Exemplo o campo de 'Atendimento' **UA\_NUM** da rotina Orçamento Televendas - Picture padrão: 999999). Quando necessário armazenar valores alfanuméricos, é alterado manualmente a **Picture** desses campos para **@!**

Contudo, ao executar a ferramenta **UPDDISTR**, que atualiza os dicionários do sistema, a configuração original da Máscara **(X3\_PICTURE)** pode ser restaurada caso:

* O tamanho ou decimais tenham sido atualizados em campos de tipo numérico;
* O dicionário destino não permita a alteração de tamanho em qualquer tipo de campo.

**Saiba mais:**

[**Regras para atualização do dicionário SX3 - UPDDISTR e migrador de versão**](https://tdn.totvs.com/x/FZLYCg)
