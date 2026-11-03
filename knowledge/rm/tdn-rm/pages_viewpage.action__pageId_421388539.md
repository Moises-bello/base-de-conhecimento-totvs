---
content_hash: 33015a0299b5c74a830b364b0d90855cdb3e8aea4431c38f059163aa5475793a
fetched_at: '2026-06-29T00:09:16.956001+00:00'
page_id: '421388539'
product: rm
source: tdn-rm
title: Processos específicos para Geração do Código de Barras/IPTE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388539
version: 5
---

Para a geração do Código de Barras/IPTE de alguns bancos é necessário realizar algumas configurações especificas.

Banco Citibank S.A. – 745

O número do portfólio utilizado pelo cedente deverá ser digitado no campo Carteira.  
A Conta Cosmos deverá ser digitada no campo Código Cedente.

Banco Cooperativo do Brasil S.A. – BANCOOB – 756

Para gerar o código de barras é necessário preencher o campo "Código do Cedente" e o "Dígito do Cedente", que estão disponíveis no cadastro de conta corrente.  
O campo "Dígito do Cedente" é obrigatório para a geração do código de barras.

Banco Bilbao Vizcaya Argentaria Brasil S.A. – 641

Para gerar o código de barras é necessário preencher o campo "Código do Cedente" e o "Dígito do Cedente", que estão disponíveis no cadastro de conta corrente.  
O campo "Código do Cedente" deve possuir "6" dígitos para que seja gerado o código de barras do banco Bilbao.

Banco Itaú S.A. – 341

Carteiras 106, 107, 122, 142, 143, 195, 196 e 198 (Nosso Número com 15 posições)  
Para a composição do Código de Barras e IPTE é necessário o "Código do Cliente (Fornecido pelo Banco)", essa informação deve ser preenchida no campo "Código do Cedente" no cadastro de Conta Corrente.

Banco Safra S.A. – 422

Para gerar o código de barras para cobrança "Registrada" é necessário preencher o campo "Dígito da Conta" que está disponível no cadastro de conta corrente.

Banco Santander Banespa – 033

Para a geração do código de barras do banco Santander, é necessário informar:  
Informar o Código do Cedente (código informado pelo Banco) no campo "Código do Cedente" (cadastro de Conta Corrente | pasta Dados Adicionais);

Para "Cobrança Simples Rápida COM Registro" (101)

Marcar a opção "Tipo de Cobrança – Registrada" (cadastro de Conta Corrente | pasta Dados Adicionais)

Para "Cobrança Simples SEM Registro" (102)

Marcar a opção "Tipo de Cobrança – Não Registrada" (cadastro de Conta Corrente | pasta Dados Adicionais)

Para "Penhor Rápida Com Registro" (201)

Informar o valor "201" no campo "Tipo Carteira" (cadastro de Conta Corrente | pasta Dados Adicionais)

**Observações**

Para a modalidade "Penhor Rápida Com Registro (201)", não importa qual a opção de "Tipo de Cobrança" marcada, o que o sistema verifica é a informação do campo "Tipo Carteira".

Se nenhuma opção de "Tipo de Cobrança" estiver marcada e não existir informação no campo "Tipo Carteira, o sistema considera a modalidade "Cobrança Simples SEM Registro (102)".

Banco Daycoval

De acordo com o manual do banco para a a carteira 121 o campo livre da linha digitável, ompreende o número da operação (contrato) do Cliente junto ao Banco.
