---
content_hash: faf17c393b88ce497e1c83afc1dd24037df72d0ce05beffb4591c23d9b5d4a68
fetched_at: '2026-06-29T00:09:48.433437+00:00'
page_id: '435105152'
product: rm
source: tdn-rm
title: Novidades 11.00 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105152
version: 2
---

**Novidade da Versão 11.0.0**   
   
**11.0.0 - Cadastro de Agente Complementar na Venda**  
Foi criado os campos Data Inclusão e Data Exclusão na edição do Agente complementar na Venda.   
Ao realizar um Aditivo de troca de Agente Complementar, o sistema irá inserir a data no campo Data Exclusão e o Agente Complementar antigo não será excluído da Venda.  
**11.0.0 - Histórico do Cálculo da Tabela Price**  
   
Foi aprimorado o Histórico do modelo de Cálculo da Tabela Price.  
**11.0.0 - Reajustar parcelas enviadas a banco em até: X dias:**  
Se marcarmos o parâmetro "Não reajustar parcelas enviadas a banco no modelo de cálculo PADRÃO", as parcelas não serão reajustadas a não ser que seja informado um valor no parâmetro abaixo.  
Foi criado um parâmetro novo "Reajustar parcelas enviadas a banco em até: X dias".  
Para reajustar as parcelas enviadas a banco vencidas. O status CNAB será alterado para 0 - Não Remetido, caso o vencimento da parcela ultrapasse X dias em relação ao dia primeiro do mês em que estiver sendo realizado o reajuste.  
**11.0.0 - Modelo de Cálculo SACRE**  
Implementado o Modelo de Cálculo SACRE no sistema.  
**11.0.0 - Atualização em Lote de Sub-unidades**  
Foi aprimorado o processo de Atualização em Lote de Sub-unidades.  
**11.0.0 - Processo de Seguro por Empreendimento**  
Foi aperfeiçoado o processo de Seguro por Empreendimento. A partir desta versão, poderemos selecionar quais vendas serão calculadas o Seguro por Empreendimento.  
**11.0.0 - Implementado o Modelo de cálculo de Juros Pro Rata Dia**  
Pro rata die" é o mesmo que "em proporção ao dia" isto é juros incidentes "por dia". É a cobrança proporcional (calculada por dia), feita quando a data do vencimento da parcela não compreende a todo o período estipulado do cálculo de reajuste do contrato  
Foi criado 2 modelos para o cálculo. São eles:  
   Modelo 0 - Cálculo dos Juros Pro Rata Proporcional ao numero de dias do Mês  
                            - Juros Simples: (Gráfico Linear)  
                            - Juros Composto: (Gráfico Exponencial)  
   Modelo 1 - Cálculo dos Juros Pro Rata Proporcional a 30 dias  
                            - Juros Simples: (Gráfico Linear)  
                             - Juros Composto: (Gráfico Exponencial)  
**11.0.0 - Implementado o Modelo de cálculo de Correção Monetária "Pro-Rata Dia":**  
Pro rata die" é o mesmo que "em proporção ao dia" isto é Correção Monetária incidentes "por dia".   
É a cobrança proporcional (calculada por dia), feita quando a data do vencimento da parcela não compreende a todo o período estipulado do cálculo de reajuste do contrato  
Foi criado 2 modelos para o cálculo. São eles:  
  Modelo 0 - Pro-Rata Temporis (Gráfico Exponencial)  
  Modelo 1 - Pro-Rata Proporcional (Gráfico Linear)  
**11.0.0 - Implementado campo Ignorar Deflação**  
Foi implementado um novo parâmetro "Ignorar deflação" na regra de Correção Monetária para ignorar variação mensal negativa.  
Se este parâmetro estiver marcado, quando o reajuste de Correção Monetária detectar deflação, o valor da Correção Monetária será zero.  
**11.0.0 - Implementado campo Aplicar Coeficiente Mensalmente**  
Foi implementado um novo parâmetro "Aplicar Coeficiente Mensalmente" na regra de Correção Monetária para aplicar mensalmente o valor do coeficiente no cálculo da Correção Monetária.  
Se este parâmetro estiver marcado, quando o reajuste de Correção Monetária for realizado, o sistema irá somar o percentual informado no campo "Coeficiente" ao percentual calculado da Correção Monetária no mês e depois calcular o valor da parcela. No reajuste dos meses seguintes, o sistema irá acrescentar o percentual do coeficiente em cada mês calculado.  
Já com o parâmetro desmarcado, quando o reajuste de Correção Monetária for realizado, o sistema irá calcular a Correção Monetária do mês, somar com o valor principal e depois aplicar o percentual informado no campo "Coeficiente".  No reajuste dos meses seguintes, o sistema irá acrescentar o percentual do coeficiente somente no final do cálculo da Correção Monetária de todos os meses somado ao valor principal.  
**11.0.0 - SGI - Fluxo de Caixa**  
Foi implementado no SGI os campos Natureza Financeira a Pagar e Natureza de Financeira a Receber nas telas de Parâmetros, Parâmetros em Tipo de Parcela, Empreendimentos e nos componentes geradores de parcelas nas Condições de Vendas, sendo que essa é mais uma integração entre o SGI e o Financeiro. Com isso, o SGI passa a enviar informações de Fluxo de Caixa para o Financeiro.  
**11.0.0 - Inserção de Cônjuge no cadastro de Cliente/Fornecedor**  
Foi aprimorada a consistência de CPF na inserção de Cônjuge presente nos Anexos do cadastro de Cliente/Fornecedor.  
**11.0.0 - Cadastro de Vagas**  
Foi aprimorado o cadastro de Vagas em Sub-unidades. Agora no código de Vagas é possível informar um código de até 15 caracteres.
