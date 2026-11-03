---
article_id: 37340653063959
category: Ativo fixo - Reforma Tributária
content_hash: bfb26673321bdc4667acb711f3245dd26cca99210a7d9074caff224b3428cdd1
fetched_at: '2026-06-28T22:41:35.561071+00:00'
product: protheus
section_id: 37095895776791
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - Como informar a Alíquota
  de Majoração na Nota Fiscal de Ativo?
type: support-article
updated_at: '2025-12-30T14:31:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37340653063959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Como-informar-a-Al%C3%ADquota-de-Majora%C3%A7%C3%A3o-na-Nota-Fiscal-de-Ativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37340653060119) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como informar a alíquota de Majoração de PIS/COFINS na Nota Fiscal de entrada de Ativo Imobilizado, considerando a descontinuação dos campos da tabela SF4 (TES)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - Todas as versões  
  
**Solução**  
Com a implementação do projeto de descontinuação de campos da tabela SF4 (TES), os campos F4\_MALQPIS e F4\_MALQCOF deixarão de ser utilizados. Atualmente, o preenchimento dessas informações é necessário para que os campos  N1\_ALIQPIS e N1\_ALIQCOF sejam integrados corretamente entre Compras e Ativo Fixo, considerando os valores de majoração.

Para realizar essa configuração através do **Configurador de Tributos**, siga os procedimentos abaixo:

1. **Cadastro NCM x Produto:** Para que o lançamento da Nota Fiscal de Entrada reconheça a alíquota, a mesma deve estar associada ao NCM desejado, considerando a origem do produto.  
     
   ![](https://tdn.totvs.com/download/attachments/979032685/chrome_uljYBt9lX4.gif?version=1&modificationDate=1755806835400&api=v2)
2. **Regra de Base de Cálculo:** Definir a regra para Majoração.  
     
   ![](https://tdn.totvs.com/download/attachments/979032685/chrome_FPMkYEmrZf.gif?version=1&modificationDate=1755806834557&api=v2)
3. **Regra de Alíquota:** Cadastrar a alíquota correspondente para Majoração de PIS e Majoração de COFINS.  
     
   ![](https://tdn.totvs.com/download/attachments/979032685/aliquota%20PIS.gif?version=1&modificationDate=1755806833387&api=v2)
4. **Regra de Cálculo (Documentos Fiscais):** Criar a regra de cálculo apontando para as regras de base e alíquota criadas anteriormente.  
     
   ![](https://tdn.totvs.com/download/attachments/979032685/regra%20doc%20fiscais%20maj%20pis.gif?version=1&modificationDate=1755807136680&api=v2)
5. **Vinculação na Regra Principal:** O passo fundamental para que o sistema calcule a majoração automaticamente é realizar o vínculo dentro da regra principal do tributo:  
     
   ![](https://tdn.totvs.com/download/attachments/979032685/vinculo%20PIS.gif?version=1&modificationDate=1755808083803&api=v2)  
     
   Repita todo o processo para o **COFINS.**

**Exemplo de Cálculo:** Considerando uma Nota Fiscal de Entrada com os seguintes dados:

* **Valor da Mercadoria:** R$ 1.000.000,00

**Cálculo da Majoração PIS:**

* Alíquota de Majoração PIS (Cadastro NCM): 0,30%
* Base de Cálculo: R$ 1.000.000,00 × 0,30% = R$ 3.000,00
* Índice Auxiliar de Majoração: 1%
* **Valor Majorado PIS:** R$ 3.000,00 × 1% = **R$ 30,00**

**Cálculo da Majoração COFINS:**

* Alíquota de Majoração COFINS (Cadastro NCM): 0,10%
* Base de Cálculo: R$ 1.000.000,00 × 0,10% = R$ 1.000,00
* Índice Auxiliar de Majoração: 1%
* **Valor Majorado COFINS:** R$ 1.000,00 × 1% = **R$ 10,00**

**Importante** Os exemplos apresentados são meramente ilustrativos. Recomenda-se que cada empresa avalie seus próprios cenários e valide as alíquotas junto à legislação vigente.

**Saiba Mais**

[Como Informar a Alíquota de Majoração na NF de Ativo - Reforma Tributária](https://tdn.totvs.com/pages/viewpage.action?pageId=979032685)  
[Cross Segmento - Backoffice Linha Protheus - SIGAATF - Reforma tributária](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35706771532567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Reforma-tribut%C3%A1ria)  
[Cross Segmento - Backoffice Linha Protheus - SIGAATF - Como realizar a contabilização de Estorno de crédito CBS/IBS na baixa do Ativo Imobilizado?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37339763079703-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Como-realizar-a-contabiliza%C3%A7%C3%A3o-de-Estorno-de-cr%C3%A9dito-CBS-IBS-na-baixa-do-Ativo-Imobilizado)
