---
article_id: 38222273821079
category: Financeiro - Configurador de Tributos
content_hash: 45573453655d982bc9261ec6fdb9e8fb662a188539a581e6a4b60adab74a0588
fetched_at: '2026-06-28T22:37:46.188553+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - SIGAFIN - Identificação
  de cálculo de impostos via Consulta de Retenções (Configurador de Tributos) no modulo
  Financeiro
type: support-article
updated_at: '2026-02-06T19:59:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38222273821079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-SIGAFIN-Identifica%C3%A7%C3%A3o-de-c%C3%A1lculo-de-impostos-via-Consulta-de-Reten%C3%A7%C3%B5es-Configurador-de-Tributos-no-modulo-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38222273796247) Tempo aproximado para leitura: **00:02:min**  
  
**Dúvida**  
Após a entrada de uma Nota Fiscal com retenções, como identificar no Contas a Pagar (SE2) se os títulos financeiros dos impostos foram gerados pelas regras do Configurador de Tributos (FISA170) ou pelas configurações da TES (Legado)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210  
  
**Solução**  
Para identificar a origem da geração do título financeiro de retenção (se via TES ou Configurador de Tributos), é necessário realizar a conferência, realize os seguintes passos:

**Passos**

1. Acesse o módulo **Financeiro (SIGAFIN)**.
2. Acesse a rotina **Contas a Pagar (FINA050)**.
3. Localize e posicione o cursor sobre o **Título Principal** (o título gerado pela Nota Fiscal do fornecedor, e não os títulos de imposto).
4. Clique na opção **Visualizar**.
5. No menu superior, clique em **Outras Ações** e selecione a opção **Consulta Retenções**.
6. O sistema abrirá uma janela contendo duas abas principais:

   * **Emissão:** Exibe os impostos calculados com fato gerador na emissão
   * **Baixa:** Exibe os impostos calculados com o fato gerador (Caixa/Pagamento)
   * Campo **Tipo Imposto**: Irá trazer o Codigo da regra Financeira   
       
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38223320367895)

   **Análise:**

   * Se os impostos estiverem listados nesta tela (detalhando base e valor), significa que o cálculo foi realizado pelo **Configurador de Tributos**.
   * Caso a tela esteja em branco ou a opção não traga registros, indica que a retenção foi realizada pelo método legado (TES tradicional) ou não há regras de retenção vinculada a regra financeira para esse imposto.
