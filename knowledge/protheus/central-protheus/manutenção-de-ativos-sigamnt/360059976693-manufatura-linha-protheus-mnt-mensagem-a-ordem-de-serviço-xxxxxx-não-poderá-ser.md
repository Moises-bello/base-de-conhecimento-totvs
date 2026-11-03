---
article_id: 360059976693
category: Manutenção de Ativos (SIGAMNT)
content_hash: 96259079f33064036f571e906e00e57f844ba95cbb36f8951cd4c31bb26be9c7
fetched_at: '2026-06-28T22:42:34.240017+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: 'Manufatura - Linha Protheus - MNT - Mensagem: A Ordem de Serviço XXXXXX não
  poderá ser finalizada, pois não existe Ordem de Produção para a mesma'
type: support-article
updated_at: '2025-05-26T17:50:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059976693-Manufatura-Linha-Protheus-MNT-Mensagem-A-Ordem-de-Servi%C3%A7o-XXXXXX-n%C3%A3o-poder%C3%A1-ser-finalizada-pois-n%C3%A3o-existe-Ordem-de-Produ%C3%A7%C3%A3o-para-a-mesma
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:00 min**  
**Ocorrência**Ao finalizar uma **O.S. - Ordem de Serviço** é apresentada a mensagem **A Ordem de Serviço XXXXXX não poderá ser finalizada, pois não existe Ordem de Produção para a mesma.**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Versão 12  
  
**Causa**Esse incidente ocorre, pois a parametrização do Sistema está incorreta. Quando é utilizada a integração com **Estoque** e o parâmetro **MV\_NGMNTES - Integração Manutenção (MNT) com Estoque (EST)** precisa ser igual a **S - Sim**, é obrigatório que o parâmetro **MV\_****NGMNTPC - Integração Manutenção (MNT) com Planej. e Contr. da Produção (PCP)** esteja igual a **S - Sim**.  
Desta forma, toda **O.S** deve estar vinculada a uma **OP - Ordem de Produção**. Caso não esteja ocorrerá a situação mencionada nessa solicitação.   
  
**Solução**Para correção, é necessário cadastrar uma **OP** na rotina de **MATA650 - Ordens de Produção**, com as seguintes informações:

* **Numero da OP**: o mesmo número da **O.S.**
* **Item**: **OS**
* **Sequencia**: **001**
* **Produto**: **MANUTENCAO**
* **Centro de custo**: o mesmo em que a **O.S.** foi solicitada
* **Quantidade**: 1
* **Previsão Ini**: mesma informação da **O.S.**
* **Entrega**: mesma informação da **O.S.**

Outra alternativa é o cancelamento da **O.S** e criação de uma nova com as mesmas características, pois com o parâmetro supracitado habilitado a **OP** deve ser gerada automaticamente.
