---
article_id: 360025347591
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: da2698464e4d39117afe1f5a82ee308b37bc090f6709f795ffaf94533bed7200
fetched_at: '2026-06-28T22:40:44.563943+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - ECD TRIMESTRAL
  UNIFICADA '
type: support-article
updated_at: '2024-05-21T12:29:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025347591-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-TRIMESTRAL-UNIFICADA
---

**Dúvida:**

Como gerar um único arquivo txt, da ECD, contendo todos os trimestres? Em caso de empresa de Lucro presumido ou lucro real trimestral?

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
  
**Solução**

A partir do Layout 7 para gerar 1 arquivo contendo os 4 trimestres é necessário:

* ![](https://centraldeatendimento.totvs.com/hc/article_attachments/23075012329623)Para gerar o arquivo da ECD de forma trimestral , é necessario que a apuração (zeramento da contas receita e despesa), sejam realizadas a cada trimestres ,**Sem utilizar** conta ponte . Desta forma o sistema irá gerar os registros trimestralmente.
* Para realizar a [apuração de resultado trimestralmente SEM conta ponte (Clique Aqui)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041554693-MP-SIGACTB-CTBA211-Exemplo-Apura%C3%A7%C3%A3o-Trimestral-Apura%C3%A7%C3%A3o-Sem-conta-PONTE?source=search)
* [Possuir o Calendário Contábil trimestral  (caso possua um calendário anual, deve incluir um calendário trimestral sem amarração da moeda rotina CTBA010).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028525872-MP-SIGACTB-ECD-CADASTRO-DE-CALEND%C3%81RIO-CONTABIL?source=search)
* [ECD, Geração de 5 demonstrativos quando arquivo trimestral unificado MV\_ECDTRIA.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6141626072855-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Gera%C3%A7%C3%A3o-de-5-demonstrativos-quando-arquivo-trimestral-unificado?source=search)

* Na rotina central de escrituração (CTBS001) informar na wizard:

Apuração do Exercício (L/P)? 31/12/20XX (última apuração do período)

Calendário? ( calendário trimestral)

Arquivo trimestral Unificado? SIM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14308634292887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14308711168407)

### Para mais detalhes acesse a documentação abaixo: **[Documentação - ECD 2019 - Trimestral](http://tdn.totvs.com/x/ygr7Gw)**

**Observação :** Esta funcionalidade só esta disponível a partir do Layout 7 , para o layout anteriores será necessário realizar o procedimento conforme documentação : [MP - SIGACTB - ECD– LAYOUT 1 ao 6  Como gerar o arquivo da ECD com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016231592-MP-SIGACTB-ECD-Como-gerar-o-arquivo-da-ECD-com-Apura%C3%A7%C3%A3o-trimestral?source=search)

**Saiba mais:**

**<http://tdn.totvs.com/display/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_7_00>**
