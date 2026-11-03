---
content_hash: ab37269008ea11f9965000692e21f5efae9cd1ae8977ea119d410875904ec085
fetched_at: '2026-06-29T00:09:54.773521+00:00'
page_id: '445647243'
product: rm
source: tdn-rm
title: Aba Identificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445647243
version: 14
---

Nesta janela são apresentadas informações sobre a identificação do lançamento financeiro.

CNPJ/CPF 

Ao digitar parte de um CNPJ/CPF e pressionar TAB o sistema localiza os registros que possuem o CNPJ/CPF correspondente ao valor digitado.

Número do Documento 

O número do documento do lançamento financeiro é gerado de acordo com a opção "Gera Número do Documento " do cadastro de Tipo de Documento.

Data de Emissão 

Se o Tipo Contábil do lançamento for Contábil e esta data estiver sendo utilizada nos parâmetros "Data Default de Inclusão a Pagar" ou "Data Default de Inclusão a Receber", ao alterar esta data o sistema sugere a atualização da Data da Contabilização de Inclusão.

Data de Vencimento 

Se o Tipo Contábil do lançamento for Contábil e esta data estiver sendo utilizada nos parâmetros "Data Default de Inclusão a Pagar" ou "Data Default de Inclusão a Receber", ao alterar esta data o sistema sugere a atualização da Data da Contabilização de Inclusão.

Data Previsão de Baixa 

Se o Tipo Contábil do lançamento for Contábil e esta data estiver sendo utilizada nos parâmetros "Data Default de Inclusão a Pagar" ou "Data Default de Inclusão a Receber", ao alterar esta data o sistema sugere a atualização da Data da Contabilização de Inclusão. Obs: A Data de Previsão de Baixa será atualizada com a Data de Vencimento somente na inclusão do lançamento financeiro, na edição essa atualização não ocorre já que trata-se somente de um facilitador de preenchimento dos campos na tela no processo de inclusão.

**Importante:**

Caso deseje que a data de vencimento ou data de previsão de baixa seja alterada para o próximo dia útil em caso de final de semana ou feriado é necessário alterar os parâmetros 'Aceita Vencimento a Pagar em finais de semana e feriados' e 'Aceita Previsão de Baixa a Pagar em finais de semana e feriados' para Primeiro Dia Útil Posterior

Ler dados de boleto

Disponível a partir do patch 12.1.2510.100 foi implementada uma funcionalidade para utilizar uma ferramenta de inteligência artificial a fim de automatizar o preenchimento de campos (Cliente/Fornecedor, datas de vencimento e emissão, valor, linha digitável, nosso número e QR-Code Pix "copia e cola") do lançamento financeiro **à pagar**. Saiba mais clicando [aqui](https://tdn.totvs.com/display/LRM/Ler+dados+de+boleto).
