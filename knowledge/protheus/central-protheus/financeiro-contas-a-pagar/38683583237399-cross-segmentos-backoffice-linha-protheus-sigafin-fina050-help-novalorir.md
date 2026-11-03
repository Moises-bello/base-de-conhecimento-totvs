---
article_id: 38683583237399
category: Financeiro - Contas a Pagar
content_hash: f7239990983ad7e222ec9504f4f62363999d7689384944b3ea8f19e6aedad4a2
fetched_at: '2026-06-28T22:38:08.570516+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - HELP: NOVALORIR'
type: support-article
updated_at: '2026-03-30T13:31:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38683583237399-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-HELP-NOVALORIR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38683583221655) Tempo aproximado para leitura: **00:07:00 min**  
  
**Dúvida**  
Ao excluir um título do tipo TX incluído manualmente, aciona o help NOVALORIR.

![NOVALORIR.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38683588570647)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS SIGAFIN - Todas as versões  
  
**Solução**  
O HELP é uma **trava de integridade relacional e financeira**. Ele é disparado pelo sistema quando a rotina de exclusão ou processamento identifica a seguinte combinação exata de fatores no banco de dados:

1. **Conflito de Chaves (Sobreposição de Numeração):** A rotina rastreia a base de dados em busca de registros financeiros que compartilhem exatamente a mesma trinca de identificação do título manipulado: **Filial**, **Prefixo** e **Número**.
2. **Detecção de Retenção Ativa:** Ao encontrar esses registros com chaves coincidentes, o sistema inspeciona o campo de valores de imposto. Se o sistema identificar que o valor contido nesse campo é **maior que zero** (ou seja, existe retenção financeira real calculada e amarrada àquela numeração), a rotina aborta a operação e dispara o Help.

A trava detalhada acima é aplicada estritamente a títulos que o sistema interpreta como **Títulos Principais**.

Quando o título `TX` é incluído manualmente, o campo `E2_TITPAI` fica vazio. Estruturalmente, um título sem "pai" é lido pelo ERP como um título principal. Ao tentar excluí-lo, o sistema bloqueia a ação para impedir a quebra de integridade dos valores de IR que ele encontrou amarrados àquele mesmo número. Ou seja, para seguir coma  exclusão, o campo `E2_TITPAI`  deve estar preenchido.

**Observação:**

Recomendamos orientar a área de negócios a não incluir títulos de impostos manualmente. Se houver necessidade de corrigir ou refazer um imposto, o procedimento padrão e seguro no Protheus é estornar o processo do título pai (NF) e refazer o fluxo, garantindo a amarração sistêmica nativa.
