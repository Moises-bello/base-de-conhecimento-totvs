---
article_id: 360015913612
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 3e8f47887be397c235ffed722147a5a88c79c95cb62fb6e3b0df963bf6fd0d27
fetched_at: '2026-06-28T22:38:45.086043+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Série exclusiva
  por filial com tabela SX5 compartilhada
type: support-article
updated_at: '2023-08-30T21:19:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015913612-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-S%C3%A9rie-exclusiva-por-filial-com-tabela-SX5-compartilhada
---

**Dúvida**

Como utilizar uma série exclusiva por filial utilizando a tabela compartilhada?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as Versões  
  
**Solução**

Se o Faturamento é exclusivo (ou seja, registros na SF2 possuam o campo de Filial preenchido) então, é natural que a organização opte por séries **exclusivas**. Ou seja, cada Filial possui sua série e, consequentemente, uma sequência de numeração individual.

Para trabalhar com **séries exclusivas** e a SX5 compartilhada é necessário atentar-se às Premissas:

* Cada Filial deverá possuir um MV\_NUMITEN exclusivo
* Modo de Compartilhamento da *Tabela 01* da SX5 (SX5 compartilhada com Tabela 01 exclusiva):  
  Estando a SX5 compartilhada, utilizar o Ponto de Entrada [CHGX5FIL](https://tdn.totvs.com/x/79ZGJg) para passar o código da Filial logada para a SX5 a fim de localizar o registro exclusivo da Tabela 01 (veja aqui [Exemplo de uso com o Ponto](https://tdn.totvs.com/download/attachments/329024579/CHGX5FIL_exemplo.jpg?version=1&modificationDate=1539180998893&api=v2)). Deste modo a Tabela 01 será tratada como "exclusiva" apesar de a SX5 ser compartilhada.

ATENÇÃO: O controle via SX5 é o menos indicado, para melhor performance na emissão dos documentos, a TOTVS sugere o uso do [controle de numeração via SD9](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019923012-MP-FAT-Controle-de-numera%C3%A7%C3%A3o-da-nota-de-sa%C3%ADda-com-uso-de-SD9-MV-TPNRNFS-3-).

**Saiba mais:**

Controle de numeração em: [Controle de Numeração no Protheus](https://tdn.totvs.com/x/Q4ScEw)
