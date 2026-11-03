---
article_id: 37485247428503
category: Escrita Fiscal - Reforma Tributaria - CBS e IBS
content_hash: 27f94d5b0b895fa71bcda8d865b5a50c92cdb4c612d3770d9ecee89d4c4e6579
fetched_at: '2026-06-28T22:39:15.746119+00:00'
product: protheus
section_id: 33305945453079
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - FISA170 - Importação
  da Tabela de Indicador de Operação (IndOp) no Configurador de Tributos
type: support-article
updated_at: '2026-05-20T20:30:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37485247428503-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Importa%C3%A7%C3%A3o-da-Tabela-de-Indicador-de-Opera%C3%A7%C3%A3o-IndOp-no-Configurador-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37485223398679) Tempo aproximado para leitura: **10:00 min**  
  
**Dúvida**  
Como importar a tabela de Indicador de Operação (IndOp) no Configurador de Tributos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2410  
  
**Solução**  
Para incluir a tabela de indicador de operação no Configurador de Tributos, siga os passos abaixo:

#### **1. Download da tabela**

A tabela deve ser baixada no site oficial do Governo Federal, no endereço:

<https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/anexovii-indop_ibscbs_v1-00-00.xlsx/view>

#### **2. Conversão do arquivo**

Após realizar o download:

* Abra o arquivo no Excel ou software compatível;
* Salve o arquivo no formato **CSV (separado por vírgulas)**.

---

#### **3. Importação no Protheus**

1. Acesse o **Configurador de Tributos**;
2. Navegue até o menu:

   * **Cadastros > Tabela código indicadores de operação**
3. Clique em **Outras Ações > Importar Tabelas**;![](https://centraldeatendimento.totvs.com/hc/article_attachments/37485223399447)
4. Selecione o arquivo convertido no formato **CSV (separado por vírgulas)**;
5. Confirme a importação.

---

### **Resultado Esperado**

A tabela de **Indicadores de Operação** será importada com sucesso e ficará disponível para utilização nas parametrizações fiscais do Configurador de Tributos.

## **Utilização de um código IndOp via regra de escrituração (CJ2\_INDOP)**

Conforme estabelecido pela Lei Complementar nº 214/2025 e normatizado na Nota Técnica SE/CGNFS-e nº 004/2025, os documentos fiscais eletrônicos para serviços (NFS-e) são obrigados a informar o Código de Indicador da Operação (cIndOp) do IBS e CBS.

Portanto, foi disponibilizado o preenchimento desses códigos no Configurador de Tributos através da rotina **Regra de Escrituração**.

Foi criado o campo **Indic. Opera (CJ2\_INDOP)** para vincular os códigos vindos da tabela **Códigos Indicadores de Operação (CI1).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40622265186199)

## **Gravação do código Indop nos Livros Fiscais (CJ3\_INDOP)**

Após inclusão de um documento fiscal de serviço que utilizava uma **regra de escrituração** com o campo **"Indic. Opera" (CJ2\_INDOP)** preenchido, o **livro fiscal (CJ3)** do documento irá conter também o valor do **cIndOp**no campo **CJ3\_INDOP**.

Documentação relacionada:  
[CFGTRIB - Indicadores da Operação (IndOp)](https://tdn.totvs.com/pages/viewpage.action?pageId=1016684365)
