---
content_hash: 1d140dcb420d34d0ed9feb4a4aca7fe4fe96cad329d31130b729ec403df6f270
fetched_at: '2026-06-29T00:12:00.770450+00:00'
page_id: '88900636'
product: rm
source: tdn-rm
title: Parametrização do Tipo de Movimento para geração de Comissão.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=88900636
version: 1
---

Veja como parametrizar o tipo de Movimento e Produto/Serviço para receber o Movimento de Comissão gerado pelo TOTVS Incorporações.

No SGI, acesse a de comissão e parametrize o tipo de Movimento e Produto/Serviço para receber o Movimento de Comissão gerado pelo TOTVS Incorporações.

No RM Nucleos, vá aos parâmetros e selecione o tipo de movimento referente a comissão e siga as informações abaixo:

Acesse *Gestão de Compras* (04.06) e *Solicitação de Compras* (04.06.01). O mesmo é necessário, pois a Comissão trata-se da Solicitação de um Serviço no qual o usuário Contrata o Corretor para vender o imóvel.

Acesse o Parâmetro, e inclua um novo Tipo de Movimento de Solicitação de Compras.

**Observe os seguintes aspectos na Criação de um Tipo de Movimento para Comissão:**

Os itens abaixo são os Requisitos Mínimos para a Geração do Tipo de Movimento que receberão o Movimento de Comissão do TOTVS Incorporações.

A Classificação do Movimento deverá ser **sempre** Solicitação de Compras (Gestão de Compras).

O Local de Estoque deve ser informado nos Parâmetros;

O Movimento Gerado deverá ser Ordem de Compra;

O Tipo de Movimento de Compra deverá ser Solicitação de Compras;

O Projeto deve ser parametrizado como ‘Não Informa’;

**Não pode** existir nenhum campo parametrizado como ‘Edita’ e ‘Obrigatório’ nos Parâmetros do Tipo de Movimento, ou seja, não pode ter nenhum parâmetro com Obrigatoriedade da informação na geração do Processo.

**Para parametrizarmos um Serviço, acesse: Cadastro - Produto**

Ao Criarmos um Serviço para receber a Comissão do TOTVS Incorporações o Tipo deve ser parametrizado como ‘Serviço’, e as informações devem estar completas.

Informe também o Preço e a Moeda utilizada(aba Preço);
