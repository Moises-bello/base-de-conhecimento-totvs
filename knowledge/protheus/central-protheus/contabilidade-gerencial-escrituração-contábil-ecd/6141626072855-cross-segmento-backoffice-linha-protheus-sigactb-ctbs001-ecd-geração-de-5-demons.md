---
article_id: 6141626072855
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: b1137fe6ab4528dd6154939905001587b6813668d515bfdb020b83ddc5452b74
fetched_at: '2026-06-28T22:40:52.708164+00:00'
product: protheus
section_id: 1500001537561
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - ECD, Geração
  de 5 demonstrativos quando arquivo trimestral unificado
type: support-article
updated_at: '2024-02-19T17:40:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6141626072855-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Gera%C3%A7%C3%A3o-de-5-demonstrativos-quando-arquivo-trimestral-unificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21372985528727) Tempo aproximado para leitura: **HH:MM:SS min****Dúvida**

Na  ECD como é feita a geração de cinco conjunto de demonstrações contábeis quando utiliza arquivo trimestral unificado sendo que a ultima deve ser do período todo (anual)?

**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Contabilidade gerencial  - A partir versão P12.1.27

**Solução**Para solucionar essa dúvida, realize os seguintes passos:

Para esta funcionalidade o usuário deverá  via configurador criar parâmetro MV\_ECDTRIA.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6141523104663)

Para que a rotina gere o quinto conjunto de demonstrações contábeis, a empresa devera ser trimestral, ter o calendário trimestral informado e gerar o arquivo  arquivo trimestral unificado onde já se gera os demonstrativos para cada trimestre e após estes gerar um anual do período escriturado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6141478329239)

Saiba mais:

[ECD0044\_Fato Contábil - MV\_ECDTRIA , para que seja gerado o J215 para o período anual](https://tdn.totvs.com/pages/releaseview.action?pageId=773517445)

Para exibição das contas com saldos zerados no registro J210, ativar o parâmetro [MV\_CTBSLDZ](https://tdn.totvs.com/pages/viewpage.action?pageId=621605812) 

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - ECD TRIMESTRAL UNIFICADA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025347591-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-TRIMESTRAL-UNIFICADA-?source=search)

Saiba mais :

<https://tdn.totvs.com/display/public/PROT/ECD_SPED_CONTABIL_Alteracoes_para_Leiaute_7_00>

**Observação : Esta funcionalidade só esta disponível a partir do Layout 7 , para o layout anteriores será necessário realizar o procedimento conforme documentação : [MP - SIGACTB - ECD– LAYOUT 1 ao 6  Como gerar o arquivo da ECD com Apuração trimestral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016231592-MP-SIGACTB-ECD-Como-gerar-o-arquivo-da-ECD-com-Apura%C3%A7%C3%A3o-trimestral?source=search)**
