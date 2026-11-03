---
article_id: 360035973613
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: f65ed1c4a187e40420c722a276cd5b1f1d093bad888dd4f0a0a337794fc54017
fetched_at: '2026-06-28T22:40:34.129682+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA080 - Não valida
  o campo fórmula
type: support-article
updated_at: '2021-08-31T17:54:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035973613-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA080-N%C3%A3o-valida-o-campo-f%C3%B3rmula
---

**Ocorrência**A rotina de **Lançamento Padrão(CTBA080)**não está validando as funções e campos utilizados nas fórmulas da rotina, permitindo a entrada de qualquer caractere ao cadastrar um Lançamento Padrão.  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - A partir da versão 12.1.17

**Causa**   
Esse incidente ocorre devido ao conceito atual da rotina, onde a validação não ocorre mais, esta tratativa foi retirada do produto padrão para que a rotina possa ser utilizada exclusivamente para cadastrar os Lançamentos Padrão do sistema.  
  
Como a rotina anteriormente executava e verificava as funções contidas no Repositório de Objetos, essas eram chamadas no momento da validação, desta forma podia-se usar a rotina para fins que não eram do seu conceito - Criação dos Lançamentos Contábeis para integração de informações ao ambiente de Contabilidade Gerencial -

Um exemplo de Utilização indevida da rotina era a utilização da função *CHKFILE()* para forçar a criação de tabelas no banco de dados via rotina **CTBA080**.

Para manter a integridade do sistema e manter as validações conforme a documentação: [Conceito CTBA080,](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba080.htm) não será possível realizar a validação da fórmula.

Veja mais:   
[MP - SIGACTB - LANÇAMENTOS PADRÃO - CTBA080](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018601071-MP-SIGACTB-LAN%C3%87AMENTOS-PADR%C3%83O-CTBA080?source=search)[MP - SIGACTB - Erros na função DETPROVA ou TRANSLCTA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000146787-MP-SIGACTB-Erros-na-fun%C3%A7%C3%A3o-DETPROVA-ou-TRANSLCTA?source=search)
