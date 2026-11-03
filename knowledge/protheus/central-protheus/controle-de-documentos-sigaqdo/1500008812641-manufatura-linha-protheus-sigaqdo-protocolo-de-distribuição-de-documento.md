---
article_id: 1500008812641
category: Controle de Documentos (SIGAQDO)
content_hash: b3046fe3ea9b7184b9213cfd14bea705769c2827417cafbc1a583d2538d54850
fetched_at: '2026-06-28T22:42:29.258121+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Protocolo de Distribuição de Documento
type: support-article
updated_at: '2021-05-03T13:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008812641-Manufatura-Linha-Protheus-SIGAQDO-Protocolo-de-Distribui%C3%A7%C3%A3o-de-Documento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Quais os protocolos são impressos durante a distribuição do documento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Solução**Existem 2 tipos de protocolos que podem ser impressos quando realizada a distribuição do documento por meio da rotina **QDOA110 - Distribuição**:

* Protocolo de entrega
* Protocolo de recolhimento

Para ambos os protocolos temos parametrizações que indicam se serão ou não impressos quando realizado a distribuição do documento:

* **MV\_QPROT - Define se a distribuição do documento deverá emitir o protocolo de entrega de documentos**.
* **MV\_QPROTRE - Define se a distribuição do documento deverá emitir o protocolo de recolhimento de documentos**.

Além disso, ainda é possível customizar estes protocolos, caso opte por utilizar a impressão do protocolo.

* Quando o parâmetro **MV\_QPROT** estiver como **S-Sim**, será verificado a existência do **PE - Ponto de Entrada QDORP27**. Se existir, será considerado este **PE** para listagem, caso contrário, será exibida a listagem padrão do **QDOR060 - Protocolo de Entrega**.
* Quando o parâmetro **MV\_QPROTRE** estiver como **S-Sim**, será verificado a existência do **PE QDORP28**. Se existir, será considerado este **PE** para listagem, caso contrário, será exibida a listagem padrão do **QDOR063 - Protocolo de Recolhimento**.

**Saiba mais**  
Abaixo, temos a documentação destes dois **PEs**:

* [QDORP27 - Relatório em Substituição](https://tdn.totvs.com/x/Jspn)
* [QDORP28 - Relatório em Substituição](https://tdn.totvs.com/pages/releaseview.action?pageId=6801959)
