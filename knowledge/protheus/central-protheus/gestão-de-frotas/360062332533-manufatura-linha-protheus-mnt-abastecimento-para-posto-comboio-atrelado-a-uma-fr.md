---
article_id: 360062332533
category: Gestão de Frotas
content_hash: 8f76ec526dfab4cc966b8bad48254b94d0b573fb9352c9dac1927eb264c8937e
fetched_at: '2026-06-28T22:42:39.246134+00:00'
product: protheus
section_id: 360012117873
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Abastecimento para Posto Comboio atrelado
  a uma frota
type: support-article
updated_at: '2021-10-29T11:27:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062332533-Manufatura-Linha-Protheus-MNT-Abastecimento-para-Posto-Comboio-atrelado-a-uma-frota
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:02:4****0 min**  
**Dúvida**Como realizar o controle de abastecimentos para o posto comboio atrelado a uma frota?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Gestão de Frotas - Versão 12

**Solução**Para realização de abastecimento para o posto comboio deverá ser realizado o procedimento abaixo:  
  
1. Acessar o módulo de **Manutenção de Ativos - SIGAMNT**.  
  
2. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Fornecedores**. Cadastre um **fornecedor**.  
  
3. Em **Atualizações / Controle de Oficina / Cadastros Básicos / Locais de Estoque**. Cadastre **locais de estoque** para os tanques do posto comboio.  
  
4. Em **Atualizações / Controle de Combustíveis / Cadastros Postos / Tipo Combustíveis**. Cadastre os **combustíveis**.  
  
5. Em **Atualizações / Controle de Oficina / Bens / Bens**. Cadastre um **bem** do tipo **frota não integrada ao TMS**, informando contador, placa e tanque.  
  
6. Em **Atualizações / Controle de Combustíveis / Cadastros Postos / Postos**. Cadastre um **posto comboio** informando no campo **Comboio? (TQF\_COMBOI) =1=Sim** e no campo **Frota- TQF\_FROTA** informar a frota no qual irá realizar os abastecimento, atrelar o fornecedor incluso.  
  
7. Em **Atualizações / Controle de Combustíveis / Cadastros Postos / Posto Interno**. Cadastrar **tanques** e **bombas** de acordo com as informações inclusas nos passos **3 e 4**.  
  
**Importante**1. O controle de estoque se dá pelo módulo de **Estoque**, onde segrega por produto e armazém.  
O saldo de estoque para comboio é igual ao posto fixo, ou seja, é necessário relaciona-lo a **Produto - SB1** e **Tanque - TQI**.  
Dependendo do contexto a nomenclatura para **tanque** poderá mudar, desta forma assume-se como sinônimo o termo almoxarifado, armazém ou local de estoque.  
A alimentação de saldo para o tanque do comboio pode se dar de várias formas, uma das rotinas que podem ser utilizadas é a rotina de **Transferência de Combustível - MNTA651**. Outras formas é utilizar a rotina de transferência de produtos no módulo de **Estoque/Custo - SIGAEST**.  
  
2. Além do local de estoque para o tanque que irá abastecer os demais veículos, deverá incluir outro para o tanque da própria frota.  
  
3. O processo é igual ao posto fixo, ou seja, registrar os abastecimentos ou saídas de combustível. Lembrando que cada posto/comboio deve ter os seus códigos de tanque distintos.   
  
4. Quando é realizado o abastecimento do tanque do veículo - o mesmo tanque relacionado no cadastro do veículo **TT8 - Tanque do Bem** deverá utilizar as rotinas de **abastecimento - MNTA655, MNTA656, entre outras**. Entretanto, no cenário de transferência do combustível para transporte ou abastecimento de outros veículos, deve-se utilizar a rotina de **Transferência - MNTA651**.
