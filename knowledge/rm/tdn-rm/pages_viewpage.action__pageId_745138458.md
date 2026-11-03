---
content_hash: d6b804b5728dd36c2cec1e35b009fe006e68dd8fb2ac4bb226fe9af423aa2a84
fetched_at: '2026-06-29T00:11:32.159998+00:00'
page_id: '745138458'
product: rm
source: tdn-rm
title: FAQ - Erros na Contabilização por Competência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745138458
version: 21
---

---

Na Contabilização por Competência modelo antigo e modelo novo precisamos configurar eventos para tais contabilizações, abaixo vamos descrever alguns exemplos de erro e avaliações para corrigir e contabilizar os contratos

Diferença na soma das partidas contábeis de débito e crédito

Na execução do processo de geração de contabilização por competência do contrato, pode ocorrer diferença na soma das partidas contábeis. 

Essa diferença entre as somas das partidas pode ocorrer na execução do processo de geração de contabilização ou de estorno por competência.

**Solução:** Acessar os eventos contábeis configurados, eles devem ser cadastrados no menu Financeiro/Contábil | Geração | Eventos Contábeis e indicados para utilização nos parâmetros do sistema menu Ambiente | Parâmetros | Educacional | Integração | Contabilidade.

Este problema, na maior parte das vezes está ligado a eventos contábeis configurados de forma incorreta.

Seguem alguns passos para validação:

1. Acessar o cadastro de eventos contábeis em *Financeiro/Contábil | Geração | Eventos Contábeis.*
2. Editar o evento contábil que está gerando diferença. Na aba **Itens Evento,** validar se os itens de **Débito** e **Crédito** estão condizentes. 
   1. Caso existam mais itens de evento para **Débito**do que para **Crédito** pode ser um problema
   2. Existem casos onde os itens de evento de **Débito**utilizam configurações diferentes dos itens de **Crédito**, nestes casos é bom se atendar principalmente ao valor configurado.

Exemplo 1

Neste exemplo temos um cadastro de eventos contábeis simples, onde existe um item para **Débito** e um para **Crédito**

Ao fazer a comparação, a A**plicação** do evento de **Débito** é sobre o **Contrato,** a **Origem da Conta** contábil está vinculada a **Informar** **Conta,** e o valor do evento será **100% do Valor do Serviço**, 

Ao fazer a comparação, a A**plicação** do evento de **Débito** é sobre o **Contrato,** a **Origem da Conta** contábil está vinculada a **Informar** **Conta,** e o valor do evento será **100% do Valor do Desconto do Serviço**

Ao analisar esta diferença na configuração podemos constatar que ai está o problema.

**Análise:** O **Valor Serviço** dificilmente será igual ao **Valor Desconto do Serviço**. O valor de cada configuração vem de uma origem diferente o correto é que sempre tenham a mesma origem.

No exemplo citado, a soma do valor de desconto é **R$ 0,00** (partidas de crédito) já o valor do serviço é de **R$12.331,00** (partidas de débito).

Ao ajustar o **Valor** no Crédito para **Valor Serviço**, o processo para de dar erro.

Exemplo 2

Neste exemplo temos um cadastro de eventos contábeis, onde existe 2 itens para **Débito** e 3 para **Crédito**

No print acima temos um cenário onde nos itens de **Crédito** existem duas bolsas enquanto nos itens de **Débito** existe apenas um item de bolsa.

Neste caso é importante se atentar às colunas **Aplicar** e **Percentual**. Podemos ver que na lista de **Débito** temos uma aplicação de 100%, já na listagem de **Crédito** temos dois itens para **aplicar bolsa 100%.**

Este é um cenário onde a soma do valor de bolsas de **Crédito**será menor que o valor de **Débito,** gerando assim diferença na contabilização.

**A solução é que o cliente ajuste as configurações dos itens contábeis.**

Exemplo 3

Neste exemplo temos um cadastro de eventos contábeis, onde existe 2 itens para **Débito** e 3 para **Crédito**

Exemplo 4

Neste exemplo temos um cadastro de eventos contábeis configurado para buscar a conta contábil no Default.

Informei somente contas contábeis no default da Matriz Aplicada no crédito

No evento configuramos no **Débito** para buscar a conta contábil na **Matriz Aplicada** e obter default no **Débito**

**Análise:**

O **Valor Serviço** dificilmente será igual ao **Valor Desconto do Serviço**. O valor de cada configuração vem de uma origem diferente o correto é que sempre tenham a mesma origem.

No exemplo citado, a soma do valor de desconto é **R$ 0,00** (partidas de crédito) já o valor do serviço é de **R$12.331,00** (partidas de débito).

Na execução da contabilização irá dá erro, pois não encontrou conta contábil informada no Default de Débito

Se tivesse configurado no Débito não iria buscar nenhuma conta contábil e iria dar erro de débito e crédito. 

Para a Contabilização por Competência do Novo Modelo temos a opção de verificar o Log do Evento Contábil

---

## Artigos relacionados

[Contabilidade - Parâmetros](https://tdn.totvs.com/pages/viewpage.action?pageId=425459120)  
[Eventos Contábeis - Educacional](https://tdn.totvs.com/pages/viewpage.action?pageId=425458832)  
[Modelos de contabilização por competência](https://tdn.totvs.com/pages/viewpage.action?pageId=425459507)  
[Provisão Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=487391427)
