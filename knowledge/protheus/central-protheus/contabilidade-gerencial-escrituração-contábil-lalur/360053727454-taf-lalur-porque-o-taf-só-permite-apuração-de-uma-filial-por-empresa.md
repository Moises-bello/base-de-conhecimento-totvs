---
article_id: 360053727454
category: Contabilidade Gerencial - Escrituração-Contábil-Lalur
content_hash: 84e6acecc04074cfb7f08ee260fafa8abcbf47ae47a76d19ac51b2057de3c6f8
fetched_at: '2026-06-28T22:40:40.316549+00:00'
product: protheus
section_id: 1500001548842
source: central-protheus
title: TAF_LALUR Porque o TAF só permite apuração de uma filial por Empresa?
type: support-article
updated_at: '2024-05-23T17:43:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053727454-TAF-LALUR-Porque-o-TAF-s%C3%B3-permite-apura%C3%A7%C3%A3o-de-uma-filial-por-Empresa
---

**Dúvida**Porque o TAF só permite apuração de uma filial por Empresa?  
  
**Ambiente**TOTVS – TAF – A partir da versão 11.80

**Solução**

**Conforme Legislação:**É facultado às pessoas jurídicas que possuírem filiais, sucursais ou agências manter contabilidade não centralizada, devendo incorporar ao final de cada mês, na escrituração da matriz, os resultados de cada uma delas (Lei 2.354/54, art. 2)

Esta necessidade decorre da apuração do resultado, pois para fins de tributação pelo IRPJ e CSLL, ao fim de cada período de incidência , o contribuinte deverá apurar o lucro líquido mediante a elaboração, com observância das disposições da lei comercial, do balanço patrimonial, da demonstração do resultado do período de apuração e da demonstração de lucros ou prejuízos acumulados ([Decreto-lei 1.598/1977](http://www.normaslegais.com.br/legislacao/tributario/dl1598.htm), art. 7, § 4°, e [Lei  7.450/1985](http://www.normaslegais.com.br/legislacao/tributario/art16a33_l7450.htm), art. 18).

**Esta tributação é consolidada na matriz da pessoa jurídica.**

**Como o TAF trata essa legislação?**

A marcação como "Matriz" só é permitida para uma filial dentro de cada empresa. ([TAF - COMPLEMENTO DE EMPRESAS )](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034688453-TAF-COMPLEMENTO-DE-EMPRESAS-Como-acessar-o-complemento-cadastral?source=search)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092088933/mceclip0.png)

Por questões de autonomia e das formas gerenciais que o cliente trata uma "filial" não é viável uma validação de CNPJ na estruturação do SIGAMAT.

obs. As formas gerenciais mencionada, são filiais que não possuem um CNPJ, mas internamente, são contabilizadas exclusivamente e no final do período são consolidadas com a Matriz.

**No SIGAMAT do Protheus, posso tratar uma filial como empresa?**

Não, independente da flexibilidade sistêmica que temos em relação as filiais gerenciais (que não possuem CNPJ) o número de Empresas do SIGAMAT deve corresponder a realidade do Grupo empresarial.

Dentro do Protheus, no geral, há situações e processos entre filiais que não são permitidos entre empresas.

Exemplo, Transferência de bens ATFA060, Apuração do Lalur entre outros.

**Implantei uma filial como empresa, como apurar o Lalur para a filial correta e para filial que é uma empresa?**

Deverá ser criado uma empresa no SIGAMAT e reestruturar toda movimentação da "Filial que é empresa" no cadastro novo.

Ou pode ser feito o processamento da rotina de CONSOLIDAÇÃO GERAL (CTBA220).

Esse processamento irá copiar cadastro e movimentos do contábil para a EMP/FIL destino.

O processamento deve ser periódico e a entrega da ECF e Lalur ser feito pela nova empresa configurada.

[MP - SIGACTB - Documentação Consolidação - CTBA220 - CTBA231](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014649651-MP-SIGACTB-Documenta%C3%A7%C3%A3o-Consolida%C3%A7%C3%A3o-CTBA220-CTBA231?source=search)

[MP\_SIGACTB- CTBA220 COMO CONFIGURAR O PARÂMETRO MV\_CONSOLD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052973934-MP-SIGACTB-CTBA220-COMO-CONFIGURAR-O-PAR%C3%82METRO-MV-CONSOLD?source=search)
