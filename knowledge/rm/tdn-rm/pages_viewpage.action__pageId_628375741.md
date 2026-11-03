---
content_hash: 0c1e2f3da129c95a75d4f8f75fc6935fb4a52bc9cd1b0bab8850cae2f9ed7557
fetched_at: '2026-06-29T00:11:05.219603+00:00'
page_id: '628375741'
product: rm
source: tdn-rm
title: LGPD - Anonimização de Dados Sensíveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=628375741
version: 6
---

A anonimização visa atender ao Art. 18 Inc. IV / VI da LGPD e consiste na utilização de meios técnicos razoáveis e disponíveis no momento do tratamento, por meio dos quais um dado perde a possibilidade de associação, direta ou indireta, a um indivíduo.

Por isso foram criados no TOTVS Gestão Financeira, alguns provedores de proteção de dados com o objetivo de anonimizar dados sensíveis dos cadastros de Cliente/Fornecedor, Contato de Cliente/Fornecedor e Dados de Pagamento, esses provedores levarão em consideração algumas obrigações legais e de regra de negócio para permitir ou impedir algum dado ser anonimizado.

Iremos detalhar nesse documento cada uma dessas implementações.

Importante

A anonimização dos dados sensíveis do produto TOTVS Gestão Financeira estarão disponíveis a partir da versão 12.1.29.

## TPD - TOTVS Privacidade de Dados

O TPD auxilia os clientes que utilizam produtos TOTVS a estarem em conformidade com os requisitos da Lei Geral de Proteção de Dados (LGPD), para mais detalhes sobre o serviço e sua utilização [clique aqui](https://totvs.app/doc/private/services/support-elements/SGDP/).

## Provedores disponíveis no TOTVS Gestão Financeira

Foram criados os provedores de Cliente/Fornecedor, Contato de Cliente/Fornecedor e Dados de Pagamento, detalhados a seguir.

### Cliente/Fornecedor

Através do provedor de proteção de dados do Cliente/Fornecedor, será possível realizar a anonimização de dados cadastrados a partir do CPF/CNPJ.

Contudo, algumas regras de natureza legal e/ou de negócio poderão impedir a realização da anonimização e no caso dos dados do Cliente/Fornecedor serão observadas as seguintes regras:

* Dados de Cliente/Fornecedor que estiverem relacionados a lançamento a pagar ou a receber que esteja com status "Em Aberto" ou "Parcialmente Baixado" não poderão ser anonimizados.
* Dados de Cliente/Fornecedor que estiverem relacionados a lançamento que possua obrigatoriedade de envio no [LCDPR - Livro de Caixa Digital do Produtor Rural](https://tdn.totvs.com/display/LRM/Livro+de+Caixa+Digital+Produtor+Rural+-+LCDPR) não poderão ser anonimizados. Para isso será observado o critério do tempo de guarda definido por lei que atualmente é de 5 anos). Importante observar que essa validação é específica para as coligadas que possuem parametrização como "Produtor Rural", considerando atualmente os lançamentos com baixa total ou parcial a partir de 2019 e que tenham os campos referentes ao envio da LCDPR preenchidos.

Essas validações já estão implementadas e refletirão na permissão ou impedimento da anonimização do dado, gerando um log de alerta.

### Contato de Cliente/Fornecedor

Através do provedor de proteção de dados do Contato de Cliente/Fornecedor, será possível realizar a anonimização de dados cadastrados a partir do e-mail do contato.

Para esse caso a única validação realizada é a existência do nome do contato conforme informado pelo solicitante da anonimização.

### Dados de Pagamento

Através do provedor de proteção de dados de pagamento, será possível realizar a anonimização de dados cadastrados a partir do CPF/CNPJ do Favorecido.

Contudo, será realizada a validação da existência de lançamentos com status "Em aberto" ou "Parcialmente baixado", o que impedirá a execução da anonimização dos dados de pagamento.

## Configuração da Proteção de Dados - RM

Em complemento à informação dos recursos disponibilizados pelo RM como forma de proteção de dados, é importante conhecer o cadastro de informações referentes à proteção de dados, para mais detalhes e orientações de como realizar as configurações, acesse à documentação disponível [clicando aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=527375989).
