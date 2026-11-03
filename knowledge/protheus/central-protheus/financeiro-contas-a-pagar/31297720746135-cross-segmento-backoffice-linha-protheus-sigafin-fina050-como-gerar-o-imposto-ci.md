---
article_id: 31297720746135
category: Financeiro - Contas a Pagar
content_hash: de6ca9fc3c312d48d738d47aa17d4f7f5c5faaf47eda2f57c4d6ff5b5774f377
fetched_at: '2026-06-28T22:38:06.962758+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Como gerar
  o imposto CIDE no Financeiro
type: support-article
updated_at: '2025-04-09T20:41:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31297720746135-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Como-gerar-o-imposto-CIDE-no-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31297706926871) Tempo aproximado para leitura: **00:05 min****Dúvida**Como gerar o imposto CIDE no Financeiro?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**Parâmetros que envolvem o **CIDE**:

**MV\_FORCIDE** - Código do fornecedor padrão dos títulos de CIDE.  
**MV\_CIDE** - Naturezas para contribuições manuais CIDE  
**MV\_RATCIDE**   
[**MV\_FGCIDE** -](https://tdn.totvs.com/pages/releaseview.action?pageId=525810447) Define o fato gerador do imposto CIDE. 1 = Baixa ou 2 = Emissão

**Procedimento para Configuração:**

**1.** Acesse o **Cadastro de Fornecedores**, inclua ou altere no cadastro de um Fornecedor.

Na pasta **Outros**, o campo **Recolhe CIDE** deve ser preenchido com **Sim**, que corresponde à aplicabilidade do **CIDE**.

**2.** Acesse o **Cadastro de Naturezas** e inclua uma Natureza com os campos preenchidos conforme abaixo:

O campo **ED\_CALCCID** como SIM.  
O campo **ED\_BASECID** deve ser definido caso exista Base de Cálculo para o Imposto  
O campo **ED\_PERCCIDE** também deve ser definido, pois se refere ao percentual a ser utilizado no cálculo.

**3.** Acesse o Cadastro de Fornecedores e defina a natureza cadastrada/alterada no cadastro do fornecedor  
  
**Procedimento para Utilização**:

1. Inclua um título no contas a pagar para o Fornecedor configurado anteriormente.  
  
**Saiba mais  
[6670406 DSERFINP-26172 DT CIDE na baixa do titulo](https://tdn.totvs.com/pages/releaseview.action?pageId=525012883)[FIN0068\_CPAG\_Como\_Calcular\_o\_CIDE](https://tdn.totvs.com/display/public/PROT/FIN0068_CPAG_Como_Calcular_o_CIDE)**
