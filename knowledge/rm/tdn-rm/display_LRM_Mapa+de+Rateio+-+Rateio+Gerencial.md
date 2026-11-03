---
content_hash: 5875f1217514a97052930e41e67fef125da7851fa0fc14d8be216b5037d77c94
fetched_at: '2026-06-29T00:09:27.977041+00:00'
page_id: '423938598'
product: rm
source: tdn-rm
title: Mapa de Rateio - Rateio Gerencial
type: documentation
url: https://tdn.totvs.com/display/LRM/Mapa+de+Rateio+-+Rateio+Gerencial
version: 5
---

*Atenção!*  
   
Esta funcionalidade só está disponível para as bases já migradas para o Novo Modelo do BackOffice.  
   
O Rateio Gerencial tem como finalidade dar suporte em algumas operações onde não é possível determinar o critério de distribuição no momento do registro da operação, isso ocorre geralmente quando o critério para a distribuição só é obtido no final de um determinado período. Dessa forma a operação é registrada em uma conta gerencial transitória ou de apoio e no final do período é realizada a distribuição para as devidas contas gerenciais sem perder o histórico da operação anterior.  
Para isto deverão ser cadastrados os Mapas de Rateio que serão utilizados no Processo de Execução do Rateio Gerencial.  
Em cada Mapa de Rateio poderão ser selecionadas contas contábeis onde será possível definir novos critérios e regras para uma nova distribuição gerencial resultando em novos lançamentos conforme configuração definida. Cada regra de distribuição corresponde a um Item de Rateio diferente.

Na janela principal é possível visualizar o cadastro geral dos Mapas de Rateio.  
O Mapa de Rateio seguirá o critério de distribuição chamado Rateiro por centro de custo transitório.  
Através deste cadastro é possível controlar:  
**Identificação - Item de Rateio**

Neste cadastro podem ser incluídos vários itens de rateio onde em cada item será definido formas distintas para geração do novo rateio.  
Todas as contas contábeis informadas na Origem de um item de rateio serão distribuídas de acordo com a parametrização informada no Destino do rateio. Se as contas contábeis tiverem distribuições diferenciadas, para cada conta contábil deve ser incluído um novo Item de Rateio ou Mapas de Rateio distintos.

Cada item de rateio deverá ter um número Sequencial que determinará a ordem ou sequencia a ser seguida no momento de execução do processo onde os itens selecionados serão sempre executados em ordem crescente.  
Através deste cadastro é possível controlar:  
Origem

Destino
