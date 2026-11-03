---
article_id: 16457477649303
category: PCO - Movimentos
content_hash: 8e236af7070d3d7eda0aa2c1aa731de437d300ef856c43219c064be82ba8f9f8
fetched_at: '2026-06-28T22:37:09.527869+00:00'
product: protheus
section_id: 1500001550962
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA530 - Erro ao solicitar
  contingência no momento de integração com PCO: Type mismatch on compare on PCOA530ALC.'
type: support-article
updated_at: '2023-08-01T18:54:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16457477649303-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA530-Erro-ao-solicitar-conting%C3%AAncia-no-momento-de-integra%C3%A7%C3%A3o-com-PCO-Type-mismatch-on-compare-on-PCOA530ALC
---

**Ocorrência:**

No momento de integração dos módulos com o PCO, ao tentar gerar uma contingência de PCO o sistema gera error.log abaixo:

**Type mismatch on compare on PCOA530ALC(PCOA530.PRW)**

**Ambiente**Cross Segmento - Backoffice Linha Protheus - Planejamento Orçamentário – A partir da versão 12.

**Causa**Esta ocorrência ocorre devido à configuração do incorreta do  parâmetro MV\_PCOWFCT, que geralmente esta com o tipo C- Caractere, porem o mesmo deve ser do tipo N-Numérico :

![parâmetro2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/16457464794391)

**Solução**Para solucionar esta ocorrência, siga os seguintes passos:  
  
1. Acesso a rotina de parâmetros no módulo configurador;  
  
2. Certifique-se de que o parâmetro **MV\_PCOWFCT** seja do N - Numérico, caso contrário, você precisará excluí-lo e recriá-lo com o tipo correto;  
  
![para3.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/16457448091287)  
  
3. Acesso o Protheus e valide novamente a rotina de integração e gere novamente a contingência do PCO, verifique se o error.log não é gerado.

**Saiba mais:**

**[Parâmetros SIGAPCO](https://tdn.totvs.com/pages/releaseview.action?pageId=312175430)**
