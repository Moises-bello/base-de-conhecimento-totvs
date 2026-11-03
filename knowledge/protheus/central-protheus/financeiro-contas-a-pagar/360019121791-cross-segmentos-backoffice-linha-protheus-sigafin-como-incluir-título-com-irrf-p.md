---
article_id: 360019121791
category: Financeiro - Contas a Pagar
content_hash: 9750eeae9a74261ff7abf9703ffc50d93a118da09a0df5cf494d90874dadd02f
fetched_at: '2026-06-28T22:38:08.500862+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Como incluir título
  com IRRF (Pessoa Jurídica) na emissão
type: support-article
updated_at: '2022-08-17T23:13:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019121791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Como-incluir-t%C3%ADtulo-com-IRRF-Pessoa-Jur%C3%ADdica-na-emiss%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como incluir título no financeiro com imposto IRRF (Pessoa Jurídica) na emissão?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Acesse o modulo **Financeiro** > **Atualizações** > **Cadastros** > **Naturezas(FINA010)** Inclua\altere uma natureza com retenção de IRRF, aba **Impostos >** campo **Calcula IRRF = S Sim**, informar o campo **Porc IRRF >** selecione **Confirmar** ;

2. **Atualizações** > **Cadastros** > **Fornecedores(MATA020)** altere cadastro do Fornecedor na aba fiscais para **Calc. IRRF = 1 Norma**l;

3. **Atualizações** > **Contas a Pagar** > **Contas a pagar(FINA050)** incluir título, selecione fornecedor e natureza para retenção do **IRRF**;

4. Ao **Baixar** o título o mesmo já será apresentado com o imposto **IRRF** retido
