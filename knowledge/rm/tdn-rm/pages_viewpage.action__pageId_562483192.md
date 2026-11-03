---
content_hash: c2ea4f9c3975f5e8f65b82bdc64a6c9eaff91a5bb196b61aa22aac5a19f50242
fetched_at: '2026-06-29T00:10:50.665082+00:00'
page_id: '562483192'
product: rm
source: tdn-rm
title: DT- SEFIP - Base 13 Salário Contrato Intermitente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562483192
version: 2
---

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | RH |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | SEFIP |
| **Situação/Requisito:** | Ajuste na Rotina Sefip para tratamento do 13º Salario Intermitente.  O arquivo de importação para o SEFIP gerado no RM Labore, não está carregando o valor da base de cálculo para o 13º salário do empregado na categoria 04 - Intermitente. |
| **Solução/Implementação:** | Feito o tratamento nos campos 17 e 22 do relatório SEFIP.RE para informar valor do  13º salário intermitente. Para isso será necessário:  1) O funcionário é considerado intermitente se a flag "Regime de Trabalho Intermitente" no cadastro de funcionário estiver marcada. A categoria do eSocial será 111 - Empregado - contrato de trabalho intermitente e categoria do sefip 4 - Emp. sob contrato de trab. por prazo det./Intermitente (Lei n°.9.601/98 e 13.467/17).  2) Para a flag do intermitente aparecer os parâmetros abaixo devem estar marcados: - "Usa Trabalho Intermitente" em "Folha de pagamento / Funcionário / Trabalho Intermitente" - "Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017" em "Folha de Pagamento / Folha Normal / Geral". |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | [FOPCALCULO01-10932](https://jiraproducao.totvs.com.br/browse/FOPCALCULO01-10932) |
| **Documento de Referência:** | [SEFIP](https://tdn.totvs.com.br/display/public/LRM/SEFIP+.Net) |
| **Pacote:** | N/A |
