---
article_id: 39444395619607
category: Financeiro - Contabilização
content_hash: 1c9dd6b517e86bd846a9fcdbda90622a40f45f23dbae994f6f27a65387bfd2bc
fetched_at: '2026-06-28T22:38:05.289207+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Ajuste da numeração
  do lote financeiro na contabilização
type: support-article
updated_at: '2026-04-01T14:05:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39444395619607-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Ajuste-da-numera%C3%A7%C3%A3o-do-lote-financeiro-na-contabiliza%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39444395597207)Tempo aproximado para leitura: 00:06 min**

**Dúvida**  
Como funciona a geração e o ajuste da numeração do lote, sublote e documento na contabilização do módulo Financeiro?  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39444411389591)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Financeiro - Todas as versões  
  
**Solução**  
A numeração do lote contábil é controlada por parâmetros específicos e tabelas de sistema. A capa do lote serve como o identificador principal para a localização posterior dos lançamentos.

1. **Configuração do Lote (MV\_LOTECON):**

* Se o parâmetro **MV\_LOTECON** estiver configurado como **T**: O número do lote é gerado automaticamente a partir da **Tabela 09** (SX5). No caso do Financeiro, verifique a chave **FIN** com o conteúdo correspondente.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39444395601303)
* Se o parâmetro **MV\_LOTECON** estiver configurado como **U**: O sistema busca o último número de lote utilizado no arquivo de Lançamentos Contábeis (CT2) e soma 1 para a data informada.

2. **Configuração do Sublote (MV\_SUBLOTE):**

* Se o parâmetro **MV\_SUBLOTE** estiver preenchido, o conteúdo é gravado automaticamente sem intervenção do usuário.
* Se o parâmetro estiver em branco, o campo fica disponível para digitação manual na rotina.

3. **Configuração do Documento:**

* O número do documento é sugerido pelo sistema com base no último número digitado acrescido de 1, facilitando a sequência cronológica dos lançamentos.

  Saiba Mais:

  [Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Ajuste da numeração do lote financeiro na contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019073652-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-CTBA101-Campos-da-capa-do-Lote-cont%C3%A1bil?source=search)

  [PE CT102ACAP](https://tdn.totvs.com/display/public/PROT/PE+CT102ACAP)
