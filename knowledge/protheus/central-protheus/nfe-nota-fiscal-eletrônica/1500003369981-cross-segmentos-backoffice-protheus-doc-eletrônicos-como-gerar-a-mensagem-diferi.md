---
article_id: 1500003369981
category: NFe - Nota Fiscal Eletrônica
content_hash: 61f52e175775bf2c00050714fa5a64bb63a28ca2dcacd476332702fc436932f2
fetched_at: '2026-06-28T22:40:05.705512+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar a mensagem
  "Diferimento Parcial conforme Anexo VIII, Art. 28 do RICMS/PR - Decreto 7871/2017.
  ICMS Diferido em % no valor de R$"
type: support-article
updated_at: '2025-06-16T17:00:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003369981-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-mensagem-Diferimento-Parcial-conforme-Anexo-VIII-Art-28-do-RICMS-PR-Decreto-7871-2017-ICMS-Diferido-em-no-valor-de-R
---

**Dúvida**Como gerar a mensagem "Diferimento Parcial conforme Anexo VIII, Art. 28 do RICMS/PR - Decreto 7871/2017. ICMS Diferido em % no valor de R$"  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução****No Protheus há 7 tipos de configuração de ICMS diferido conforme o link abaixo:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Cálculo de Diferimento de ICMS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418030442775-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-de-Diferimento-de-ICMS?source=search)

1- Para Esta mensagem deve ser utilizada opção 5:

Atenção: **A opção 5** se refere ao diferimento parcial do ICMS próprio previsto no artigo **108 do RICMS-PR/2012,** para maiores informações verifique o parecer tributário disponível no link: <http://tdn.totvs.com/x/E5lICw.> Ao utilizar essa opção o diferimento só se aplicará ao cálculo do ICMS próprio, **não se estendendo ao ICMS-ST.**

**Cálculo Diferimento - Alíquota Diferida**

A regra de cálculo do Diferimento do ICMS não prevê a geração de uma alíquota diferida, e sim da aplicação do % de Diferimento sobre o ICMS total calculado, desta forma o cálculo será realizado da seguinte forma:

* Configurações necessárias:

**F4\_ICM:** Definido como SIM.

**F4\_ICMSDIF:** Definido como 5

**F4\_PICMDIF:** Informar o Percentual de Diferimento:

**F4\_SITTRIB:**10

É necessário cadastrar exceção fiscal com alíquota interna do ICMS com valor da alíquota reduzida pelo Diferimento, e para calculo do ICMS ST informe alíquota do destinatário. Por exemplo:

**F7\_ALIQINT =** 12 - alíquota com Diferimento.

**F7\_ALIQDST =**18 - Alíquota do destinatário para cálculo do ICMS ST

Exemplo com Percentual de Diferimento igual a **33,33%**

**Atenção:** Não foi realizado um exemplo com diferimento de 100%, pois o cálculo é efetuado pelo usuário diretamente na alíquota e já informado na exceção fiscal a alíquota reduzida.

Dados complementares:

Valor: R$ 100,00

Alíquota de ICMS: 18%

Percentual de Diferimento: 33,33%

* **Como chegar ao valor da alíquota com Diferimento:**

Alíquota com Diferimento: Alíquota de ICMS \* (Alíquota de ICMS + Percentual de Diferimento)

Alíquota com Diferimento: 18 - (18 \* 33,33) = (18 - 5,9994) = 12,00

* **Como chegar ao valor do ICMS Devido:**

Valor do ICMS Devido: Valor \* Alíquota com Diferimento

Valor do ICMS Devido: R$ 100,00 \* 12% = R$ 12,00
