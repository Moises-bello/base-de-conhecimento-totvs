---
article_id: 360021162431
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: f1dbf9ad7769eb07df3fb02a567a0a8784832c16237bef8d0719e93a7807f1aa
fetched_at: '2026-06-28T22:39:36.843140+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Valor de IPI na
  base de cálculo do PIS e COFINS
type: support-article
updated_at: '2022-04-18T17:10:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021162431-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Valor-de-IPI-na-base-de-c%C3%A1lculo-do-PIS-e-COFINS
---

**Dúvida**Quais os procedimentos para retirar e incluir o valor de IPI na base de cálculo de PIS e Cofins apuração?  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

# Para somar o IPI na base do Pis/Cofins

**Parâmetros:**

MV\_DEDBPIS= P

MV\_DEDBCOF= P

 Configure na TES o campo **Credita IPI (F4\_CREDIPI) = NÃO**

Exemplo: R$1.000,00 produtos + R$50,00 IPI

**Base de Cálculo** = R$ 1.050,00

# Para não somar o IPI na base do Pis/Cofins

**Parâmetros:**

MV\_DEDBPIS= P

MV\_DEDBCOF= P

Configure na TES o campo **Credita IPI (F4\_CREDIPI) = SIM**

O sistema simplesmente não vai somar o IPI na base do Pis/Cofins.

Exemplo: R$1.000,00 produtos + R$50,00 IPI

**Base de Cálculo**= R$1.000,00 (apenas produtos)

Neste caso, é possível também, configurar os parâmetros da seguinte forma:

MV\_DEDBPIS= N

MV\_DEDBCOFS= N

O sistema não irá somar o valor do IPI independente da configuração do campo Credita IPI na TES, podendo utilizá-lo igual a "sim" ou "não".

**Observação:**  
  
Preenchendo os parâmetros e cadastrando os campos na TES conforme indicado, é possível considerar ou não o IPI na base de cálculo do PIS/COFINS.

Observar o campo Ded. PIS/COF (A2\_DEDBSPC)  no cadastro do Fornecedor, pois o mesmo tem impacto no cálculo.   
  
**Ded. PIS/COF (A2\_DEDBSPC)**

Informe o(s) tributo(s) que deve(m) ser deduzido(s) da base de PIS/COFINS nas aquisições deste fornecedor.

As opções são:

1 - Legado: Deduz conforme parâmetros

MV\_DEDBPIS e MV\_DEDBCOF.

2 - ICMS e IPI: Deduz ICMS e IPI.

3 - ICMS: Deduz apenas o ICMS.

4 - IPI: Deduz apenas o IPI.

5 - Nenhum: Não deduz nem o ICMS e nem o IPI.

6 - Soma IPI
