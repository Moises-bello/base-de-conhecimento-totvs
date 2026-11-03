---
content_hash: 838ebd8c7289246581a91a38e102cbc2e7119286f03238e5b1f914cf55ea66c7
fetched_at: '2026-06-29T00:09:47.680063+00:00'
page_id: '435105045'
product: rm
source: tdn-rm
title: Novidades 12.1.2 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105045
version: 3
---

**Novidades da versão 12.1.2**    
**Múltiplas Tabelas de Preço**  
Este novo recurso consiste em melhorias na funcionalidade de tabela de preço, onde permitirá ao usuário do sistema trabalhar com várias tabelas vigentes para um mesmo imóvel.   
A funcionalidade de múltiplas tabelas de preço, foi pensada a partir da observação do mercado de incorporação que atua com uma ampla variação de precificação de imóveis.   
Com a nova funcionalidade de múltiplas tabelas de preço o usuário poderá configurar no sistema para trabalhar com a utilização de múltiplas tabelas de preço ou não, e será permitido também a associação de modalidade de venda a estas tabelas , dentre outras funções disponíveis para esta funcionalidade.   
Para maiores informações sobre Múltiplas Tabelas de Preço, clique:  
Tabela de Preço Parâmetros Vendas  
   
**Módulo Aluguel: Cadastro do Tipo de Evento Financeiro**  
Foi criado, no cadastro do "Tipo de Evento Financeiro", menu Aluguel > Cadastros > Tipo de Evento financeiro, a finalidade "Locação".  Os Eventos Financeiros desta finalidade não poderão ser incluídos manualmente. Apenas o processo "Gerar Lançamentos de Locação" poderá utilizar tais tipos de eventos.  
No campo 'Finalidade do Tipo de Evento' do cadastro do Tipo de Evento Financeiro, o nome da finalidade "Padrão" foi alterado para "Diversos".  
Foram incluídos os campos "Campo Integração" e "Campo Integração (Subtrai)", onde serão definidos os "Valores de Integração" que serão utilizados para os Eventos Financeiros com o tipo de cobrança "Agregado". Para este caso, será feita a validação se os valores de integração foram informados para o Evento Financeiro do tipo Agregado.  
   
**Módulo Aluguel: Evento Financeiro**  
Foi alterado o cadastro de eventos financeiros para que, manualmente, apenas eventos com a finalidade "Diversos" e "Luvas" poderão ser criados.  
Foi evoluída a "inclusão de lançamentos" dos "Eventos financeiros" para que sejam respeitadas as regras de vencimento do contrato de administração e de locação, quando estes estiverem associados ao "Evento Financeiro".  
A execução dos processos "Incluir lançamento financeiro" e "Excluir lançamento financeiro" não poderão ser realizados para Eventos financeiros agregados ou com tipo de lançamento que tenha a finalidade "locação".  
No cadastro de "Evento Financeiro", também foi incluído o anexo "Parcelas dos Eventos Agregados Integradas", para que seja possível verificar, para os eventos agregados, como está sua distribuição nos Eventos de locação.  
**Módulo Aluguel: Rateio por Centro de Custo**  
Foi incluído o rateio por centro de custo para todos os tipos de evento financeiro, seguindo a ordem de prioridade:  
Caso o usuário informe o Imóvel no Evento Financeiro: O sistema traz o centro de custo do imóvel;  
Se o imóvel não tiver centro de custo, o sistema traz o centro de custo do "Parâmetro de Integração Financeira" informado no Evento Financeiro;  
Caso o usuário informe o Contrato de locação e não informe o imóvel O sistema traz o rateio de custo definido no Contrato de Locação;  
   
Se o contrato de locação não tiver o rateio de centro de custo definido, o sistema traz o centro de custo do "Parâmetro de Integração Financeira" informado no Evento Financeiro;  
**Módulo Aluguel: Contrato de Locação**  
Foi criado o processo para excluir lançamentos de locação por período. A exclusão irá remover os lançamentos, parcelas e todos os componentes (resíduos e eventos agregados) que estejam relacionados aos eventos de locação que façam interseção com o período selecionado.  
Foi criado o anexo "Parcelas do Contrato de Locação" que lista os períodos, valores e vencimentos. Sua edição exibe, além dos dados básicos, os lançamentos financeiros e ainda possui um anexo ("Parcelas dos eventos agregados integradas") que exibe os eventos agregados que compõem tais lançamentos.  
**Módulo de Aluguel: Regra de Vencimento**  
O cadastro de Regra de Vencimento foi alterado afim de compatibilizar regras da geração dos lançamentos financeiros do contrato de locação, lançamentos de Repasse e demais processos derivados.  
O Campo de "Ação Divergência Vencimento" terá as opções "Fraciona e Acumula" unificadas.
