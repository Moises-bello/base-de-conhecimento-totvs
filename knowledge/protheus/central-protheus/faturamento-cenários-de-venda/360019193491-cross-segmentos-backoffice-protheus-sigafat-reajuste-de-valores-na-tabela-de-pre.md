---
article_id: 360019193491
category: Faturamento - Cenários de Venda
content_hash: 50ab59d53ba60215ac8e357e10ec3861aec59113ba56ac5938d357eebebe1a05
fetched_at: '2026-06-28T22:38:34.005765+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT -  Reajuste de Valores na Tabela
  de Preço, Preço Base e Pedidos em Aberto
type: support-article
updated_at: '2026-01-23T12:46:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019193491-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Reajuste-de-Valores-na-Tabela-de-Pre%C3%A7o-Pre%C3%A7o-Base-e-Pedidos-em-Aberto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37881310465559)** **Tempo aproximado para leitura:****00:03:30 min**

**Duvida**  
Na rotina Tabela de Preço **OMSA010** é possível reajustar os preços de forma automática?

**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

Para efetuar está ação siga os seguintes procedimentos:

* Entrar na rotina *Manutenção da Tabela de Preço* - **OMSA010**; Opção: *Outras Ações; Reajuste;* Escolha a opção *Parâmetros.*

Os parâmetros desta opção possuem preenchimento autos explicativos, no entanto, devem ser observados os seguintes dados:

**1 - Fator de Reajuste**

Deve ser informado o fator de reajuste dos preços. Os novos valores serão obtidos a partir da aplicação deste fator.

Deve ser informado o fator multiplicativo que será aplicado sobre o preço atual dos itens da tabela.

Os novos valores são calculados da seguinte forma:

**Novo Preço** = Preço Atual × Fator de Reajuste

**Importante:**  
O fator não representa diretamente o percentual, mas sim o total do preço após o reajuste, considerando que:

1,00 representa 100% do valor original

O valor acima ou abaixo de 1 indica acréscimo ou deságio

Regra geral

Fator = 1 + (Percentual de reajuste / 100)

Exemplo prático:

|  |  |  |
| --- | --- | --- |
| **Objetivo** | **Fator a informar** | **Interpretação do Reajuste** |
| Manter o preço | 1,00 | 100% do valor original |
| Aumentar 20% | 1,20 | 100% + 20% |
| Reduzir 20% | 0,80 | 100% − 20% |
| Dobrar o preço | 2,00 | 200% do valor original |

**2 - Número de Decimais**

Informe a quantidade de número de decimais que deve ser considerada na gravação do novo preço.

*Exemplo: Se informado 0 e o cálculo do novo valor for 46,74, será gravado 46,00 desconsiderando os centavos.*

*Este parâmetro define também, se o valor terá arredondamento, perante as casas decimais.*

**3 - Pedidos em Carteira**

Deve ser selecionada a opção Atualizar se os pedidos de venda em aberto devem ter seus preços reajustados, ou Manter, caso contrário.

**4 - Replicar Fator**

Caso escolha a opção Preço base o sistema replica o reajuste para o campo **B1\_PRV1**.

**5 - Atualiza preço base**

Se desejar atualizar o preço base **B1\_PRV1**, além de configurar o parâmetro Replica Fator = Preço base, deixe também este parâmetro como sim (Atualiza preço base).

**Observação:** Para atualizar os valores dos pedidos de vendas em aberto configure os parâmetros MV\_PVRECAL = .F. e Pedidos em Carteira =  Atualizar.

O parâmetro MV\_PVRECAL é utilizado para desabilitar (.T.) ou habilitar (.F.) o recálculo do preço dos itens do pedido de venda ao alterar o código da tabela de preço.

**Saiba mais:**

[Reajuste de valores na Tabela de preço (OMSA010)](https://tdn.totvs.com/x/MPQKDg)

[Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reajuste-de-Tabela-de-Preço-por-Planilha-de-Formação-de-Preço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018333411-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Reajuste-de-Tabela-de-Pre%C3%A7o-por-Planilha-de-Forma%C3%A7%C3%A3o-de-Pre%C3%A7o)

[Cross Segmentos- TOTVS Backoffice (Linha Protheus)- SIGAFAT-Reajuste-de-preço-através-da-rotina-MATA511B](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018663971-MP-FAT-Reajuste-de-pre%C3%A7o-atrav%C3%A9s-da-rotina-MATA511B)
