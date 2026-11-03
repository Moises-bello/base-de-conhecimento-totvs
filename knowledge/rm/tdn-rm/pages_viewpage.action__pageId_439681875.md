---
content_hash: 1b858af0172e0dc9ca8e795f51f4dbfe1f2e57f59ea1c1757925a8ed8a690985
fetched_at: '2026-06-29T00:09:52.462997+00:00'
page_id: '439681875'
product: rm
source: tdn-rm
title: Cancelar último reajuste de item associado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=439681875
version: 3
---

Esse processo estará disponível nos anexos de **Reajustes do item associado** e **Itens do Contrato**, quando se tratar de contrato de serviço; ou nos anexos de **Reajustes do objeto associado** e **Objetos do Contrato**, se contrato de insumo.   
Será possível cancelar, o último reajuste aplicado, caso tenha efetuado vários reajustes para aquele item.  
O usuário deverá selecionar o (s) item (s) associado (s) ao contrato e executar o processo, nesse momento o último reajuste realizado para o item será excluído e os valores recalculados.  
O Cancelamento acontecerá da seguinte maneira:  
·         Item 001.01.01   
- Escavação:   
Valor Inicial: 500,00 Fator Reajuste: 10% Valor Reajustado: 550,00  
Ao cancelar o reajuste, será verificado se o valor atual do item é igual ao valor reajustado, caso positivo, o valor é alterado para o valor anterior ao reajuste, e caso contrário, o cancelamento não será processado.   
O processo de Cancelar Último Reajuste de Item Associado foi alterado para permitir o cancelamento de reajustes para períodos medidos ou liberados, obedecendo às seguintes regras:

* O cancelamento do reajuste do item somente será processado se não existir nenhum período principal liberado com a data de liberação maior ou igual à data do reajuste onde o item está presente;
* O cancelamento do reajuste do item somente será processado se não existir nenhum período complementar de reajuste liberado onde o item está presente;
* Período medido: Ao cancelar o reajuste realizado para o item, as medições dos períodos reajustados deverão ser recalculadas pois o valor do item será alterado para o valor anterior ao reajuste. O recálculo deverá ser realizado, também, para todos os períodos medidos que tem a data maior que a data de reajuste. Períodos de estorno não deverão ser considerados pois o mesmo não deve ser recalculado pelo fato de ser um valor predefinido que não deveria ser ajustado;
* Período Principal Liberado: Ao cancelar o reajuste realizado para o item, a medição do item no período de reajuste medido deverá ser excluída e caso não exista mais nenhuma medição no período, o mesmo também deverá ser excluído. Caso tenha um período de reajuste gerado e não liberado, se for efetuado o cancelamento do reajuste para o seu período principal que originou esse período de reajuste, o mesmo deverá ser excluído.

**Solicitações no processo que impedem a execução do mesmo:**  
Se o Tipo de Reajuste do contrato não estiver definido como "Por Item Associado" o cancelamento não deverá ser permitido. Caso exista medição para um período onde existe um reajuste para o item, não deverá permitir o cancelamento, deverá excluir a medição para efetuar o reajuste.
