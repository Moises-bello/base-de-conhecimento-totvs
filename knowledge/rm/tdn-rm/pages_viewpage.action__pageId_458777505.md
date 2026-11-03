---
content_hash: d4ad7a89a7ee657ec57aeedbfbc10325531bd256368bbe795fa98d4b3b98fdd9
fetched_at: '2026-06-29T00:10:14.383683+00:00'
page_id: '458777505'
product: rm
source: tdn-rm
title: Rateio - Integração RM x Protheus - Item Contábil e Classe de Valor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458777505
version: 7
---

Expandindo a integração contábil dentro da interface RM x Protheus a partir da versão 12.1.24, os contratos de locação passam a exibir em seus rateios os [itens contábeis e classes de valor associados aos Imóveis do contrato](http://tdn.totvs.com/pages/viewpage.action?pageId=458762373).

**Procedimento para utilização**

* Os campos “Item Contábil” e “Classe de Valor” só estarão disponíveis caso exista integração ativa do TIN com o Protheus, no EAI 1.0. Estes campos também estarão disponíveis para o EAI 2.0 na versão do RM 12.1.31 e superiores.
* No Protheus, os adapters abaixo devem estar configurados:

|  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mensagem Única** | **Rotina** | **Mensagem** | **Envia** | **Recebe** | **Método** | **Operação** | **Canal** | **Alias** | Versão |
| Sim | CTBA040A | ACCOUNTINGITEM | Sim | Não | Síncrono | Todas | EAI | CTD | 1.000 |
| Sim | CTBA060 | CLASSVALUE | Sim | Não | Síncrono | Todas | EAI | CTH | 1.000 |

* Caso a integração esteja ativa, os campos "Item Contábil" e "Classe de Valor" serão também apresentados nos rateios de centro de custo do contrato de locação, como mostra a imagem abaixo:

* Caso a parametrização do rateio (Aluguel > Contrato de locação) seja  "Utilizar rateio manual no contrato de locação", será possível editar diretamente o rateio e seus valores, bem como alterar os itens contábeis e classe de valor diretamente na interface de rateio, dando duplo clique na linha do rateio selecionado:

* Caso o rateio esteja parametrizado para ser realizado automaticamente, opção "Utilizar rateio manual no contrato de locação" desmarcada, não será possível a edição dos campos como mostra a imagem acima.
* Caso o contrato de locação possua dois ou mais imóveis o sistema irá fazer o rateio de acordo com os itens contábeis e classes de valor respectivas para estes imóveis.
* À partir da versão 12.1.31, na geração de lançamentos, o sistema irá valer-se deste rateio para compor os lançamentos financeiros, como informado no contrato de aluguel. Veja a imagem abaixo onde o lançamento financeiro de aluguel já possui em seus rateios o item contábil e a classe de valor:
