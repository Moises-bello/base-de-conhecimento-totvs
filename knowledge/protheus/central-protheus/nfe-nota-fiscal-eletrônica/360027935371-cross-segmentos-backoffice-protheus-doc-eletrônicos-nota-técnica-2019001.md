---
article_id: 360027935371
category: NFe - Nota Fiscal Eletrônica
content_hash: 5b23a520114407f8028d28c85453017b81334f03cb9696e748b98f002d8b5b64
fetched_at: '2026-06-28T22:40:03.675089+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Nota técnica 2019.001
type: support-article
updated_at: '2025-09-05T18:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027935371-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-t%C3%A9cnica-2019-001
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2019.001 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para a adequação à Nota Técnica 2019.001 Versão **(1.10, 1.20, 1.30, 1.40, 1.50, 1.51, 1.60, 1.61 e 1.62)**

1. Atualização do **ambiente TSS**

Atualizar o repositório do TSS:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)

2. **Aplicar o patch abaixo no RPO** **do Protheus:**

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download#detail/1124963>

12.1.2410: <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>

3. **Aplique o rdmake padrão atualizado no Protheus** e caso tenha ponto de entrada PE01NFESEFAZ desative para realizar a emissão da nota.

<https://suporte.totvs.com/portal/p/10098/download#detail/1152113>

Caso ocorra o erro na transmissão - **Invalid field name in Alias CDV->CDV\_TPLANC on RETABENEF(NFESEFAZ.PRW)**, entre em contato com suporte Fiscal para criação dos novos campos da tabela CDV, mais detalhes verifique a documentação abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=841173522>

Para gerar a tag cBenef temos o passo a passo da documentação abaixo:

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 930: CST com benefício fiscal e não informado o código de benefício fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033521654-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-930-CST-com-benef%C3%ADcio-fiscal-e-n%C3%A3o-informado-o-c%C3%B3digo-de-benef%C3%ADcio-fiscal)

**ATO DIAT Nº 031/2024**

Conforme publicamos em nosso blog fiscal, por meio do**ATO DIAT nº 059/2023**, o estado de Santa Catarina estabeleceu a  obrigatoriedade de preenchimento dos campos vICMSDeson e motDesICMS previstos na Nota Fiscal Eletrônica (NF-e), modelo 55, e na Nota Fiscal de Consumidor Eletrônica (NFC-e), modelo 65, para os contribuintes no regime normal de tributação nos seguintes grupos:

**I   – N04 (Grupo Tributação do ICMS = 20);**

**II  – N05 (Grupo Tributação do ICMS = 30);**

**IIi – N06 (Grupo Tributação do ICMS = 40, 41, 50);**

**IV – N09 (Grupo Tributação do ICMS = 70); e**

**V  – N10 (Grupo Tributação do ICMS = 90).**

A obrigatoriedade de preenchimento dos campos acima, inicialmente estava prevista para **1º de abril de 2024.** No entanto, **em março/23**, houve a primeira prorrogação para **1º de julho de 2024**.

Dia 28/06/2024, foi publicado o Ato Diat nº 031/2024, que prorroga novamente a data de obrigatoriedade para **1****º de Fevereiro de 2025**.

* **Atender as novas regras do Fisco Catarinense  ATO DIAT nº 35/2024, que informa os novos campos de preenchimento obrigatório relacionados ao crédito presumido.**

* Caso isenção, redução de base de calculo, diferimento e não incidência ou suspenção da exigibilidade do imposto, será realizado o preenchimento de acordo com o campo da TES (F4\_SITTRIB), caso (40, 51, 41, 50) será gerado o tag cBenef.

* Caso tenha credito presumido, informar TES (F4\_SITTRIB =00), (MV\_CODCST = SC) e (CDY\_TPLANC =1) sendo assim as tags geradas serão cCredPresumido, vCredPresumido e pCredPresumido e não será gerado cBenef.

* Para gerar as duas tags: cBenef e grupo gCred com as tags cCredPresumido, vCredPresumido e pCredPresumido é necessario que tenha dois cadastros para o mesmo código de beneficio na rotina FISA156, sendo um cadastro com campo CDY\_TPLANC em branco para gerar o cBenef e o outro cadastro com CDY\_TPLANC = 1 para gera o grupo gCred.

* Para gerar a tag cBenef com literal SEM CBENEF deve preencher o parâmetro MV\_CODCST = SC=00; lembrando que é apenas um exemplo, deve ser inserido a UF do seu estado, como exemplo coloquei a UF de Santa Catarina e o CST da minha operação.
