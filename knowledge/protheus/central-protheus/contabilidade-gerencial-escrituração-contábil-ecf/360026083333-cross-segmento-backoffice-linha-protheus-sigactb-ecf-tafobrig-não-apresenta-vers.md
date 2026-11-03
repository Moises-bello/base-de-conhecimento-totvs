---
article_id: 360026083333
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: bdd15a61e6a039549b7b4b22edc012fc0b7142030ee6866051209d440a63a16c
fetched_at: '2026-06-28T22:40:48.705300+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - TAFOBRIG NÃO APRESENTA  Versão
  "108" O LAYOUT 8
type: support-article
updated_at: '2022-06-08T15:15:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026083333-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-TAFOBRIG-N%C3%83O-APRESENTA-Vers%C3%A3o-108-O-LAYOUT-8
---

**Dúvida**

Layout 0005 não está apresentado na rotina TAFOBRIG

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041291493/mceclip1.png)  
  
**Ambiente**Microsiga Protheus – Contabilidade – A partir da versão 11.80  
  
**Solução**

Para que o layout 5 seja criado , se faz necessário atualizar autocontida

**OBSERVAÇÃO [Importante]**O procedimento indicado abaixo deve ser realizado após o sistema está devidamente atualizado, conforme artigo:

[MP - SIGACTB - ECF - Como realizar a atualização do ECF?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-MP-SIGACTB-ECF-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ECF-)

1. Limpe o conteúdo do parâmetro **MV\_VAUTCON**

2. Acesse o módulo **TAF (TOTVS Automação Fiscal)**

3. Acesse a rotina **Wizard de Configuração TAF (TAFLOAD)**

4. Execute o **Processamento** das Autocontidas para todas as empresas.

5. Após este procedimento aparecerá a opção "108" referente ao Layout 8.00 do ECF

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040459554/mceclip0.png)
