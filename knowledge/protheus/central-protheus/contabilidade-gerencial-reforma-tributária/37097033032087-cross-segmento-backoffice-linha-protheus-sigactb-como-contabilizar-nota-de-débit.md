---
article_id: 37097033032087
category: Contabilidade gerencial - Reforma Tributária
content_hash: 756385e4d8cbf0c2812680ce2e82831b9ae5cb7b0a6f4d9f86c5c636e76d98ab
fetched_at: '2026-06-28T22:40:29.690701+00:00'
product: protheus
section_id: 37095816599831
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como contabilizar Nota
  de Débito e Crédito?
type: support-article
updated_at: '2026-06-05T18:18:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37097033032087-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-contabilizar-Nota-de-D%C3%A9bito-e-Cr%C3%A9dito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37097052519959) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
Como realizar a correta contabilização de Notas de Débito e Notas de Crédito no módulo de Contabilidade Gerencial (SIGACTB) do Protheus, garantindo a conformidade com a Reforma Tributária (IBS/CBS)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade gerencial - Todas as versões  
  
**Solução**  
As Notas de Crédito e Notas de Débito foram instituídas no âmbito da Reforma Tributária para formalizar ajustes relativos aos novos impostos IBS e CBS. A Nota de Crédito representa uma redução do imposto devido sob a ótica do emitente, enquanto a Nota de Débito representa um acréscimo.

Para a contabilização automática desses documentos via Lançamento Padrão (LP), utiliza-se o campo de finalidade do documento fiscal para diferenciar o tratamento contábil.

**Passos para parametrização:**

1. **Identificação dos Tipos de Documento:** Utilize o campo **D1\_TIPO** no Documento de Entrada ou **F2\_TIPO** no Documento de Saída para filtrar a contabilização no Lançamento Padrão:

   * D1\_TIPO ou F2\_TIPO = "5" → Nota de Crédito
   * D1\_TIPO OU F2\_TIPO = "6" → Nota de Débito  
       
       
     ![](https://tdn.totvs.com/download/attachments/1012945507/image-2025-11-7_16-4-35.png?version=1&modificationDate=1762542294150&api=v2)
2. **Configuração de Lançamentos Padrão (Documento de Entrada):** Os seguintes LPs são utilizados para o processamento das notas de ajuste na entrada:

   * **LP 645:** Contabilização do Documento de Entrada pelo Total para notas de Credito e Debito.   
     (Tabelas disponíveis SF1/SA2).
   * **LP 646:** Contabilização dos Itens do Documento de Entrada (Fornecedor) para notas de Credito e Debito  
     (Tabelas disponíveis SD1/SB1/SF4/SA2).
   * **LP 647:** Contabilização de Exclusão do Documento de Entrada - Total para notas de Credito e Debito.  
     (Tabelas disponíveis SF1/SA2).
   * **LP 648:** Contabilização de Exclusão dos Itens do Documento de Entrada para notas de Credito e Debito.  
     (Tabelas disponíveis SD1/SB1/SF4/SA2).  
       
       
     2.2 **Exemplo lançamento padrão (646) Nota Fiscal de Crédito**

     ![](https://tdn.totvs.com/download/attachments/1012945507/image-2025-11-7_16-11-31.png?version=1&modificationDate=1762542710460&api=v2)

     Dessa forma, quando o documento for do tipo Crédito "5" o lançamento padrão será acionado.

     2.3 **Exemplo lançamento padrão (646) Nota Fiscal de Débito**

     **![](https://tdn.totvs.com/download/attachments/1012945507/image-2025-11-7_16-17-4.png?version=1&modificationDate=1762543043473&api=v2)**

     Dessa forma, quando o documento for do tipo Débito "6" o lançamento padrão será acionado.

     2.4 **Exemplo utilização Documento de Entrada - Crédito**

     ![](https://tdn.totvs.com/download/attachments/1012945507/chrome_rnl8cWBJlF.gif?version=1&modificationDate=1764010020500&api=v2)
3. **Configuração de Lançamentos Padrão (Documento de Saída):** Para a saída, os registros seguem a estrutura dos LPs abaixo:

   * **LP 616:** Contabilização do Cabeçalho do Documento de Saída  
     (Tabelas SF2/SA1).
   * **LP 617:** Contabilização dos Itens do Documento de Saída  
     (Tabelas SD2/SB1/SF4/SA1).
   * **LP 618:** Contabilização de Exclusão do Documento de Saída- Total para notas de Credito e Debito.  
     (Tabelas SF2/SA1).
   * **LP 619:** Contabilização de Exclusão dos Itens do Documento de Saída para notas de Credito e Debito.  
     (Tabelas SD2/SB1/SF4/SA1).
4. **Uso de Fórmulas:** Recomenda-se a utilização da função **CTBVLTRIB** para retornar valores específicos de tributos durante a execução do Lançamento Padrão.  
     
   Para mais informações acesse a documentação abaixo:  
     
   [Cross Segmento - Backoffice Linha Protheus - SIGACTB - Como Contabilizar IBS, CBS e IS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/36639180648983-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-Contabilizar-IBS-CBS-e-IS)

**Saiba mais**  
[Reforma Tributária - Nota de Débito e Crédito](https://tdn.totvs.com/pages/releaseview.action?pageId=1010253803)

[Contabilização com Base na Classificação do Tributo](https://tdn.totvs.com/pages/viewpage.action?pageId=977835821)

[Contabilização com Base na Sigla do Tributo](https://tdn.totvs.com/pages/viewpage.action?pageId=977835583)
