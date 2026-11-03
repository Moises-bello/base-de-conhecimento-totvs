---
article_id: 10844524588055
category: Materiais - Compras (SIGACOM)
content_hash: 81e2a9339f1f621f9fc8484c6eb540b0a590ae4aa5b5b3d5906ffec1fbe2c965
fetched_at: '2026-06-28T22:41:11.629516+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - É possível incluir
  Nota de Complemento de Preço no Compras (MATA103) quando a Origem é uma Nota de
  Importação ?
type: support-article
updated_at: '2022-12-09T18:45:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10844524588055-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACOM-%C3%89-poss%C3%ADvel-incluir-Nota-de-Complemento-de-Pre%C3%A7o-no-Compras-MATA103-quando-a-Origem-%C3%A9-uma-Nota-de-Importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível incluir Nota de Complemento (Preço, ICMS e IPI) no Compras (MATA103) quando a Origem é uma Nota de Importação ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**Por padrão, não há como incluir uma Nota de Complemento de Preço, quando a Nota de Origem é oriunda do módulo SIGAEIC.

O módulo SIGAEIC não possui uma rotina para inclusão de Nota de Complemento, caso haja alguma inconsistência na Nota de origem, é preciso prosseguir com a retificação da Declaração de Importação (DI) para que seja lançado no Sistema um Novo Documento seguindo as mesmas premissas da P.O original, conforme documentação: [Retificação da DI](https://tdn.totvs.com/x/2aMKDg), caso haja dúvidas quanto ao processo, verificar com o time do SIGAEIC.

A Nota do tipo Complemento no módulo Compras, rotina MATA103, abrange somente o processo de Compras para operação no âmbito nacional (compras nacionais), pois não tratamos as variações de câmbio, desembaraços aduaneiros, dentre outras situações que por padrão são tratadas diretamente pelo módulo de importação (EIC).

Reiteramos que por padrão todas as notas de complemento na rotina MATA103 ( documento de entrada), precisam ser uma nota de origem para ser vinculada, até por conta do cálculo do custo e outras atualizações que por ventura possam ocorrer.

No caso de uma Nota oriunda do módulo SIGAEIC, os impostos já são calculados no módulo referido, por isso o TES utilizado deve ser o mesmo, para não haver comprometimento dos cálculos e informações preenchidos no SIGAEIC, conforme documentação [Nota Fiscal de Importação](https://tdn.totvs.com/x/qLlc)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
