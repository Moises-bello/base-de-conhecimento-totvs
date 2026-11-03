---
article_id: 360021848932
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: 117dcc0f1efdb01f9d0e418c69cf36e55f5efd96bcda908a695bd88e08125d68
fetched_at: '2026-06-28T22:41:42.336986+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF : CTBAATF - CONTABILIZAÇÃO
  OFFLINE'
type: support-article
updated_at: '2022-11-22T11:50:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021848932-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-CTBAATF-CONTABILIZA%C3%87%C3%83O-OFFLINE
---

**Dúvida**

Funcionamento da rotina de contabilização CTBAATF

**Ambiente**Protheus  – Ativo fixo  – A partir da versão 12  
  
**Solução**  
Esta rotina realiza a contabilização off-line dos movimentos do [Ativo Fixo](https://tdn.totvs.com/pages/viewpage.action?pageId=312160200)

Esta contabilização é realizada de acordo com a configuração dos [Lançamentos padrões](https://tdn.totvs.com/x/KzGbEg) permitidas.

É possível visualizar o log de processamento na opção **Visualizar**.

|  |
| --- |
| ***Importante:***  Apenas são contabilizados os registros que estiverem com a flag**N4\_LA e NX\_LA** como **N ou em branco**. |

### 

### Divisão de contabilização em processamentos simultâneos (Múltiplas Threads)

É possível efetuar a contabilização off-line distribuindo os lançamentos contábeis em processos paralelos do sistema e efetuar o processamento de vários lançamentos contábeis ao mesmo tempo. Este processo pode ser executado somente sem exibir a tela de lançamentos contábeis na tela e sem a quebra da contabilização em documentos por lançamento padrão. Para esta funcionalidade é necessário configurar a pergunta **Considerar Filiais** como **Sim**.

 

---

### Requisito

Configurar o parâmetro [MV\_ATFCTHR](https://tdn.totvs.com/pages/viewpage.action?pageId=312160178) com a quantidade de Threads, limitada a **30**.

 

---

### Procedimentos

1. Na tela de Contabilização Off-line do Ativo clique em **Parâmetro**.

2. É apresentada a tela com as perguntas para contabilização.

3. Preencha-os conforme help de campo.

4. Confira os dados e **Confirme**.

**\*\* Observação**

**Não são todos os lançamentos padrão que contabilizam off-line**

**lançamentos padrões que contabilizam off-line:**

Código Descrição

801 - Aquisição de bem

802 - Aquisição - Reavaliação

803 - Aquisição - Adiantamento

804 - Aquisição - Lei 8.200

80A - Inclusão de outros tipos de ativo

80C - Aquisição de bem por conversão

810 - Baixa aquisição

811 - Baixa reavaliação

812 - Baixa adiantamentos

81A - Baixa de outros tipos de ativo

81C - Baixa por conversão

81E - Baixa de ativo: rateio de despesas

820 - Cálculo da depreciação

821 - Ampliação

823 - Cálculo de depreciação: rateio de despesas

827 - Ajuste inventário

835 - Aquisição por transferência

847 - Baixa Lei 8.200 (Tipo do Ativo á06)

850 - Ajuste por inflação - Cálculo do ajuste (Argentina)

**lançamentos contabéis abaixo somente contabilizam On-line:**

Código Descrição

805 - Exclusão Aquisição do bem

806 - Exclusão - Reavaliação

807 - Exclusão - Adiantamento

808 - Exclusão - Lei 8.200

80B - Exclusão de outros tipos de ativo

80D - Exclusão aquisição do bem por conversão

813 - Baixa Lei 8.200

814 - Cancelamento baixa aquisição

815 - Cancelamento baixa reavaliação

816 - Cancelamento baixa adiantamento

817 - Cancelamento baixa Lei 8.200

81B - Cancelamento da baixa de outros tipos de ativo

81D - Cancelamento baixa aquisição por conversão

81F - Cancelamento da baixa de ativo: rateio de despesas

822 - Cancelamento de ampliação

825 - Descálculo

828 - Estorno do calculo da depreciação: rateio de despesas

830 - Transferência contábil

831 - Transferência contábil enre filiais (origem)

832 - Transferência contábil entre filiais (destino)

836 - Cancelamento da aquisição por transferência

846 - Exclusão Lei 8.200

848 - Cancelamento da baixa (Tipo do ativo 04)

851 - Ajuste por inflação - Cancelamento do cálculo do ajuste (Argentina)

860 - Ajuste a valor presente - Constituição

861 - Ajuste a valor presente - Apropriação

862 - Ajuste a valor presente - Baixa de apropriação

863 - Ajuste a valor presente - Baixa

864 - Ajuste a valor presente - Realização

865 - Ajuste a valor presente - Baixa de realização

866 - Ajuste a valor presente - Diferença por revisão

870 - Apontamento de estimativa de produção

871 - Apontamento de revisão da estimativa de produção

872 - Apontamento de produção

873 - Apontamento de encerramento de produção

874 - Apontamento de complemento de produção

87A - Apontamento de produção com rateio

867 - Ajuste a valor presente - cancelamento de constituição

868 - Ajuste a valor presente - cancelamento de AVP - Baixa

875 - Estorno de apontamento de estimativa de produção

876 - Estorno de apontamento de revisão estimativa de produção

877 - Estorno de apontamento de produção

878 - Estorno de apontamento de encerramento de produção

879 - Estorno de apontamento de complemento de produção

87B - Estorno de apontamento de produção com rateio

880 - Baixa de provisão

881 - Movimentos de provisão

883 - Revisão de movimentos de provisão

882 - Estorno de movimentos de provisão

884 - Estorno de efetivação de realização

890 - Simulação depreciação - Bens reais

891 - Simulação depreciação - Bens modificadores

892 - Estorno simulação depreciação - Bens Reais

893 - Estorno simulação depreciação - Bens modificadores
