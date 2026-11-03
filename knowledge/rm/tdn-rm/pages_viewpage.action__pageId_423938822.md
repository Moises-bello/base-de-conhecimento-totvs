---
content_hash: 3ec7855f42686d17825883c2f8f04d102162dcf1b5d59179a34ccb089bcf493a
fetched_at: '2026-06-29T00:09:29.149392+00:00'
page_id: '423938822'
product: rm
source: tdn-rm
title: Produção (Estoque)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938822
version: 10
---

**Gera Ordem de Produção (TOTVS Planejamento e Controle da Produção)**: Este campo só será utilizado por quem trabalha com integração TOTVS Gestão de Estoques, Compras e Faturamento/TOTVS Planejamento e Controle da Produção.  
O TOTVS Gestão de Estoques, Compras e Faturamento habilitará para movimentos deste tipo uma data de programação e um status de programação.  
Toda vez que o TOTVS Planejamento e Controle da Produção programar um pedido o TOTVS Gestão de Estoques, Compras e Faturamento preencherá qual foi a data de programação. Os status possíveis para a programação dos pedidos são:

* **A Programar**: pedido incluído e ainda não programado pelo TOTVS Planejamento e Controle da Produção
* **Programado**: pedido incluído e já programado pelo TOTVS Planejamento e Controle da Produção
* **Inativo**: pedido incluído, mas que não pode ser programado pelo TOTVS Planejamento e Controle da Produção. Toda vez que o TOTVS Planejamento e Controle da Produção for programar um pedido inativo este não será considerado e sua data de programação (caso ele tenha sido programado anteriormente) será anulada.

***Observações***: Este campo somente aparecerá nos tipos de movimentos do grupo pedidos de venda [2.1]. O parâmetro "Criar com Status não processado" deverá está desmarcado para que esta funcionalidade esteja ativa.  
Se a ordem de produção já foi programada ou iniciada o movimento não poderá ser excluído ou faturado.

Sobre o vínculo do item de ordem de produção como o item de movimento, ao faturar um movimento que possui este vínculo, se houver desdobramento o movimento originado (desdobrado) terá também que possuir este vínculo.   
Quando existe este vínculo com o item de ordem de produção na tela de item de movimento (pasta Integração/Dados do item de ordem de produção (TOTVS Planejamento e Controle da Produção) são mostrados alguns detalhes deste item de produção: Status do item de produção, Quantidade efetivada, Data inicial prevista, Data final prevista, Data inicial efetivada, Data final efetiva e Responsável.  
Os parâmetros que integram o movimento ao TOTVS Planejamento e Controle da Produção também afetam as operações de Faturamento, Cancelamento e Exclusão, como segue:

* Faturamento: somente poderá ocorrer quando o "Status de Produção" estiver de acordo com o parâmetro "Status Permite Faturamento" do TOTVS Planejamento e Controle da Produção (veja TOTVS Planejamento e Controle da Produção/Opções/Parâmetros/Produção/pasta Integrações e TOTVS Gestão de Estoques, Compras e Faturamento/Status Permite Faturamento).
* Exclusão de movimento: somente poderá ocorrer pelo TOTVS Gestão de Estoques, Compras e Faturamento quando o "Status de Produção" for "A Programar" ou "Cancelado"; nos demais casos, deverá ser feita a partir do TOTVS Planejamento e Controle da Produção.

**Cancelamento de movimento**: Se o parâmetro "Permite Cancelar Movimento com Ordem de Produção" (do tipo de movimento) estiver habilitado, poderá Cancelar normalmente. Se este estiver desabilitado, somente poderá Cancelar se o "Status de Produção" for "A Programar" ou "Cancelado".

**Permite Cancelar Movimento com Ordem de Produção**: Com esse campo habilitado é possível cancelar movimentos, independente do seu status de produção. Ou seja, sem verificação da regra de cancelamento do Factor.

***Observações***: O parâmetro "Permite Cancelar Movimento com Ordem de Produção" somente é visível para movimentos de saída (pedido de venda que gera uma demanda de produção). Quando um movimento de ordem de produção é cancelada o sistema verifica o status da ordem de produção correspondente, para validar se a cancelamento poderá ser efetuado.   
Com o parâmetro "Permite Cancelar Movimento com Ordem de Produção" marcado o Sistema permitirá o cancelamento independente do status da ordem de produção.

**Entrada de produtos acabados a partir do TOTVS Planejamento e Controle da Produção**: Este campo somente será utilizado por quem trabalha com integração TOTVS Gestão de Estoques, Compras e Faturamento/TOTVS Planejamento e Controle da Produção. O TOTVS Planejamento e Controle da Produção controla a produção da fábrica, desta forma, quando um produto fica pronto na linha de produção, este deverá ser inserido no estoque. Para isto, marque esta opção se o tipo de movimento é um tipo para controle de produto acabado e desmarque se não.

---
