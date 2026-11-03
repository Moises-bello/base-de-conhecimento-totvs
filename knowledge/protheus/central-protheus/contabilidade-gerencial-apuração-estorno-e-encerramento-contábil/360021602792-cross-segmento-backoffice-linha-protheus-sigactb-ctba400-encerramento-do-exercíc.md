---
article_id: 360021602792
category: Contabilidade Gerencial - Apuração, Estorno e Encerramento Contábil
content_hash: cf46f34c2cd0628b96f668d55b75e490a8c97ce61f32ec9e3faa48871845ab9d
fetched_at: '2026-06-28T22:41:05.090901+00:00'
product: protheus
section_id: 1500001548342
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA400 - Encerramento
  do Exercício
type: support-article
updated_at: '2025-01-22T22:34:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021602792-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA400-Encerramento-do-Exerc%C3%ADcio
---

**Dúvida**

Qual a funcionalidade da rotina CTBA400 (Encerramento do Exercício)?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - a partir da versão 11.8

**Solução**A rotina de Encerramento do Exercício tem por objetivo **fechar o Exercício Contábil**, está operação visa proteger os exercícios já efetivamente "batidos" e encerrados, não permitindo mais acesso à manipulação dos dados ali existentes.

Após utilizar esta rotina, os períodos do calendário contábil parametrizado para encerramento estarão com o **status fechado**, assim, o sistema não permitirá que para estes períodos hajam manipulação nas movimentações da contabilidade.

Caso deseje entender melhor o funcionamento do status do calendário, pode-se verificar a nossa documentação: [SIGACTB CTBA010 Help: CTG\_STATUS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020155591-MP-SIGACTB-CTBA010-Help-CTG-STATUS?source=search)

A rotina **CTBA400** deve ser processada **em modo exclusivo ao sistema**, garantindo assim a integridade do processo de fechamento e dos dados após o encerramento, este aviso é apresentado ao abrir a rotina:

![CTBA400.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018494431)

Outro ponto de aviso é referente ao **pré-lançamento ainda não efetivado**, este deverá ser efetuado, caso contrário não haverá mais possibilidade de manipulá-lo. Após a execução desta rotina, o status do calendário contábil passa a ser Fechado.

**SAIBA MAIS:**

**Help:** <http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba400.htm>

**TDN:** <http://tdn.totvs.com/pages/releaseview.action?pageId=334338624>
