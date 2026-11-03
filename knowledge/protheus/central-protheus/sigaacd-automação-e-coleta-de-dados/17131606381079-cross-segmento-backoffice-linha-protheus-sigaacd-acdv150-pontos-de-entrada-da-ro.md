---
article_id: 17131606381079
category: SIGAACD - Automação e Coleta de Dados
content_hash: d147252b1ae38a631edd8e22a2288425f93d0c033572c109fe8187be505e18bd
fetched_at: '2026-06-28T22:39:11.305856+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV150 - Pontos
  de Entrada da rotina de Transferência (Com Controle de Endereço) '
type: support-article
updated_at: '2023-08-29T22:35:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17131606381079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV150-Pontos-de-Entrada-da-rotina-de-Transfer%C3%AAncia-Com-Controle-de-Endere%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17131591110295) Tempo aproximado para leitura: **00:01:30min** **Dúvida**Quais os Pontos de Entrada da rotina de Transferência Com Controle de Endereço?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**

- **[ACD150ME](https://tdn.totvs.com/pages/releaseview.action?pageId=6091047)****- Manipula Armazém/Endereço;**

-**[ACD150VE](https://tdn.totvs.com/pages/releaseview.action?pageId=6090966)  - Complementa Validação do Endereço;**

-**[V150PROD](https://tdn.totvs.com/pages/releaseview.action?pageId=6090967)  - Validação do Produto;**

- **[AV150VPR](https://tdn.totvs.com/pages/releaseview.action?pageId=6090992)- Complementa Validação do Produto;**

-**[V150FArm](https://tdn.totvs.com/display/public/PROT/TTCSB1_ACD_DT_Ponto_de_Entrada_V150FArm) - Após todas as validações do Get de Produto, não apaga o conteúdo dos outros Gets e permite forçar o foco no Get de Armazém de Destino;**

-**[AV150ARR](https://tdn.totvs.com/pages/releaseview.action?pageId=550324389)  - Manipulação das Informações das Etiquetas Lidas, em Memória, para Transferência Permitindo Alteração;**

**- [AV150CF](https://tdn.totvs.com/pages/releaseview.action?pageId=6090990) - Grava Transferência 1;**

**- [V150AUTO](https://tdn.totvs.com/pages/releaseview.action?pageId=6091022) - Grava Transferência 2;**

**- [ACD150GR](https://tdn.totvs.com/pages/releaseview.action?pageId=6090964) - Atualiza Tabelas Específicas;**

**- [ACD150OK](https://tdn.totvs.com/pages/releaseview.action?pageId=6090965) - Monta ou Grava Tabelas Específicas;**

**- [AV150EST](https://tdn.totvs.com/display/public/mp/AV150EST+-+Valida+o+Estorno+das+Etiquetas++--+16933) - Valida o Estorno das Etiquetas;**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
