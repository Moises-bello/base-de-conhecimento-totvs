---
article_id: 360019924132
category: Contabilidade Gerencial - Lançamento Padrão e Ponto de Lançamento
content_hash: 4c2e4e89a77de88100da03eb87292fca4dd3944a45ea5e518293560a8f15c035
fetched_at: '2026-06-28T22:40:34.109918+00:00'
product: protheus
section_id: 1500001549002
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA080 - Como usar
  múltiplos saldos no Lançamento Padrão (CTBA080) e Cópia de Saldos (CTBM300)
type: support-article
updated_at: '2024-02-12T12:45:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019924132-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA080-Como-usar-m%C3%BAltiplos-saldos-no-Lan%C3%A7amento-Padr%C3%A3o-CTBA080-e-C%C3%B3pia-de-Saldos-CTBM300
---

**Dúvida**

Como utilizar rotina cópia de saldos com a opção múltiplos saldos do Lançamento Padrão  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial - P12.1.17  
  
  
**Solução**

No cadastro do Lançamento padrão, existe a opção de informar múltiplos saldos em Outras Ações:

![um.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360015924871)

Dessa forma os lançamentos contábeis são gravados na contabilidade, com características específicas na tabela CT2 para uso de Múltiplos Saldos, no campo CT2\_MLTSLD, informando os saldos.

Essas informações tem funcionalidade na rotina **Cópia de Saldos (CTBM300).**

A rotina Cópia de Saldos (CTBM300) disponibiliza a funcionalidade de lançamentos contábeis com Múltiplos Tipos de Saldos.

A rotina possui dois modos de execução distintos:

***Saldos simples***: Funcionalidade original da rotina, que permite a cópia de movimentos contábeis ou saldos contábeis por nível de entidade, de um saldo origem para múltiplos tipos de saldo destino especificados nos parâmetros.  
***Múltiplos saldos:*** Avalia o controle de múltiplos tipos de saldos dos lançamentos contábeis, gerando automaticamente os novos movimentos para os saldos previamente especificados nos lançamentos padrões utilizados.

A primeira e a segunda pergunta estão relacionadas de forma que se o Método de cópia for Cópia Simples a Seleção dos saldos deve ser Parâmetros e, se o Método de Cópia for Múltiplos Saldos a Seleção dos saldos deve ser Mov. Multi Slds

**Cópia Simples -** os lançamentos são copiados de um tipo de saldo para um ou mais tipos de saldos diferentes informados no parâmetro Saldos Destinos.  
Método de cópia

Seleção dos saldos Cópia Simples -> Parâmetros Outros parâmetros relevantes na cópia Simples são as perguntas Tipo de Cópía Simples e Movimentos Copiados.   
Se os Movimentos Copiados forem Analítico os lançamentos gerados/copiados terão a data do lançamento origem e será gerado um lançamento para cada lançamento origem,não importa se o Tipo de Cópia Simples é Saldos ou Movimentos.  
Só serão gerados lançamentos sintéticos, lançamentos com data anterior ao range de datas informadas e saldos totalizados para as contas, quando o Tipo de Cópia Simples for Saldos e os Movimentos Copiados for Sintéticos.

**Múltiplos saldos –** Copia lançamentos de um tipo de saldo para 2 ou mais tipos de saldos diferentes.  
Método de cópia - Mov. Multi Slds: Estes lançamentos que terão os tipos de saldos copiados são os oriundos da contabilização através de lançamentos padronizados e terão no campo CT2\_MLTSLD os tipos de saldos para os quais o lançamento original será copiado.

Os tipos de saldos contidos no campo CT2\_MLTSLD são determinados no lançamento padronizado.   
Após a contabilização, o campo CT2\_MLTSLD aparecerá dessa forma: ‘0;1;2’ .   
Na cópia de múltiplos saldos, o sistema não considera o conteúdo da pergunta Saldos destinos.   
Nesta opção, o sistema sempre considera o conteúdo do campo CT2\_MLTSLD e a cópia é sempre analítica, gerando sempre um movimento no CT2 para cada um dos tipos de saldos contidos no campo CT2\_MLTSLD na data do movimento origem.

**Saiba mais:**

[Lançamento Padrão Partida Simples e Partida dobrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052503314-MP-SIGACTB-CTBA080-LAN%C3%87AMENTO-PADR%C3%83O-DE-PARTIDA-SIMPLES-E-PARTIDA-DOBRADA)

[Lançamento Padrão ctba080](http://tdn.totvs.com/pages/releaseview.action?pageId=344477626)

[Lançamento Padronizados](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba080_lanc_padronizados.htm)
