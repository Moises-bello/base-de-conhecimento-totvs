---
content_hash: 7917f67fefb2a1e2a810b8d360548bdecb4faee4d52302c7888cf9ddddb62de9
fetched_at: '2026-06-29T00:09:53.642139+00:00'
page_id: '440846267'
product: rm
source: tdn-rm
title: FIN - Novidades da versão 12.1.13
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440846267
version: 5
---

**12.1.13 - Adicionado o processo "**[**Ajustar Valores do Crédito de Adiantamento para Vínculo**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388549)**"**  
Na baixa do lançamento de adiantamento com retenção, o sistema gerava o lançamento de crédito de adiantamento com o valor original constituído pela soma do valor líquido mais o valor das retenções do lançamento de adiantamento.  
A partir da versão 12.1.13, o valor original do lançamento de crédito de adiantamento, gerado pela baixa do lançamento de adiantamento com retenção, será composto somente pelo valor líquido do lançamento de adiantamento.  
Desta forma, este processo percorrerá todos os lançamentos de crédito de adiantamento gerados pela baixa do lançamento de adiantamento com retenção, revisando o seu valor original e consequentemente o seu valor vinculado, caso o lançamento esteja vinculado.  
**12.1.13 - Melhoria no processo de impressão de Boletos Registrados com a nova legislação**[**Febraban**](https://www.febraban.org.br/Acervo1.asp?id_texto=2660&id_pagina=85&palavra=)**.**  
Otimizado a impressão de boletos Registrados, para convênios onde o tipo de Cobrança é Registrado, de acordo com a nova norma Febraban. Os portais do Educacional/Processo Seletivo e Bibliotecário, também foram otimizados para atender a legislação.  
**12.1.13 - Integrado ao**[**Modulo de Caixa a solução SiTef**](http://tdn.totvs.com.br/pages/viewpage.action?pageId=421388560)**para recebimento de lançamentos a receber com cartão de Crédito e Débido, emitindo comprovantes Não Fiscal.**  
Para facilitar o recebimento de parcelas a receber, o Módulo de Caixa foi integrado com a solução SiTef da Software Express, validando a baixa de lançamentos a receber com cartões de Crédito e Débito, com transações através do SiTef em integração com PinPad, permitindo a emissão de comprovantes não fiscais.  
**12.1.13 - Melhoria no processo de cancelamento do item de baixa de lançamentos com tipo de documento "Adiantamento".**  
Melhoria no processo de cancelamento de item de baixa com vários meios de pagamento, para lançamentos com tipo de documento "Adiantamento". Caso seja feito o cancelamento de um item de baixa, o sistema irá carregar os demais itens de baixa daquele lançamento de adiantamento para que também sejam cancelados.  
**12.1.13 - Melhoria no processo de vínculo de lançamentos.**  
Melhoria no processo de vínculo de lançamentos para que o valor da retenção vinculado não fique no mesmo campo.  
**12.1.13 - Foram adicionados campos na aba "Dados opcionais" na tela de baixa de lançamento.**  
Na tela de baixa de lançamentos, etapa Edição de lançamento os campos Datas Opcionais, Alfas Opcionais, Filial, Departamento e Centro de Custo ficam disponíveis para serem informados.  
Para mais informações consulte "informar um link"  
**12.1.13 - Melhoria no processo de baixa de lançamentos com tributos.**  
Na seleção de dois ou mais lançamentos com tributos na baixa e com filiais diferentes a validação do período de apuração em aberto é feita somente para a primeira filial do primeiro lançamento.  
**12.1.13 - Melhoria para permitir alterar data de vencimento em lançamentos a pagar do educacional.**  
Melhoria para permitir alterar a Data de Vencimento em Lançamentos a Pagar oriundos do Totvs Educacional.  
**12.1.13 - Otimizado o processo de "Baixar Créditos/Devoluções vinculadas"**  
Otimizada a tela de valores do lançamento, no processo "Baixar Créditos/Devoluções vinculadas", para exibir o valor de baixa 0 (zero) no item de baixa do lançamento.  
**12.1.13 - Melhoria na inclusão de borderô de pagamento para que a barra de progresso seja concluída.**  
Melhoria no processo de inclusão de borderô para que a barra de progresso esteja sendo preenchida corretamente.  
**12.1.13 - Otimizado o campo EMAIL FISCAL.**  
Otimizado o tamanho do campo E-mail Fiscal do cadastro de cliente/fornecedor da aba Dados fiscais | outros dados para 250 caracteres.  
**12.1.13 - Nova permissão para alterar o campo histórico de lançamentos de Nota de credito.**  
A partir desta versão será permitido a alteração do campo histórico em lançamentos de Nota de Crédito de Adiantamento.  
**12.1.13 - Melhoria na inclusão de borderô de pagamento.**  
Melhoria no sistema nos processos de Inclusão de Borderô de Pagamento.  
**12.1.13 - Inclusão de parâmetro para definir se a autenticação mecânica será apresentada antes ou depois da impressão de relatório.**  
O parâmetro "permite imprimir autenticação mecânica após impressão do relatório/recibo" define que, ao realizar a baixa ou estorno do lançamento será apresentada primeiro a tela de autenticação mecânica.  
****12.1.13 - Pequena melhoria para não alterar os dados de boleto remetido ou registrado ao alterar o lançamento.****Melhoria no sistema para não alterar os dados de Boletos Remetidos ou Registrados quando é alterado o lançamento.
