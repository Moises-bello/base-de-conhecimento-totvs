---
article_id: 4411789897111
category: Financeiro - Contas a Pagar
content_hash: 7a3875f3394280664eddae9ef71f608f55b29446e7c67eb49b53a9f4ffd7300a
fetched_at: '2026-06-28T22:38:08.400264+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento BackOffice Linha Protheus - FINA100 - Transferência entre C/C
  gravando numero indevido de cheque '
type: support-article
updated_at: '2021-10-29T18:55:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411789897111-Cross-Segmento-BackOffice-Linha-Protheus-FINA100-Transfer%C3%AAncia-entre-C-C-gravando-numero-indevido-de-cheque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao realizar a transferência entre C/C está gerando indevidamente numero de cheque na tabela SEF, com isso demonstrando nos relatórios FINR400 e FINR480   
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro  - a partir da release 12.1.17  
  
**Causa**A ocorrência é devido o parâmetro **MV\_GERCHTB** está como "S", mesmo que o movimento bancário não seja realizado em cheque (Tipo CH, por exemplo), este campo é preenchido com o número do documento informado na tela. Essa é uma forma legada de verificar o processo de saída onde será gravado na tabela SEF o movimento da transferência.   
  
**Solução**Para não gravar na tabela SEF a informação da transferência é necessário ajustar o parâmetro **MV\_GERCHTB**para "**N**"

**Saiba mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=501480542#processos-5>
