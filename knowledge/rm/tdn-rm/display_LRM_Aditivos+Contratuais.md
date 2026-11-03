---
content_hash: 73884ce91dce88b6137e7ef878617942e01a37b3097795ed2624b35d8a80ff59
fetched_at: '2026-06-29T00:09:14.185443+00:00'
page_id: '421385145'
product: rm
source: tdn-rm
title: Aditivos Contratuais
type: documentation
url: https://tdn.totvs.com/display/LRM/Aditivos+Contratuais
version: 38
---

Aditivos contratuais são conhecidos por retratar a deficiência em partes do processo produtivo e na gestão durante a construção de uma obra.

Devido ao alto risco econômico financeiro, tendo em visto que o custo de um projeto previsto no orçamento inicial depende de fatores imprevisíveis, que surgem durante a condução das obras ou serviços.

Assim, muitos projetos, planilhas e serviços podem conter equívocos ou necessitam de ajustes, que só serão constatados durante a execução da obra.

Essa possibilidade de revisão de contratos e condições contratuais tem embasamento legal e deve ser processada através do instrumento adequado chamado 'Aditivo de contrato' ou 'Aditamento de contrato".

Os Aditamentos contratuais implementados levam a efeito alterações como:

* Redução ou aumento de quantitativos
* Prorrogação de prazo de execução
* Modificação do valor contratual

**Passos:**

Para incluí-lo é necessário informar na aba Identificação:

**Número:** Número do aditivo, não sendo permitido a inclusão de mais de um código para um mesmo aditivo ou inclusão de códigos repetidos.

Na inclusão de aditivos com modificação do valor contratual,  o campo Valor do Aditivo será calculado com base nos registros associados.

Na prorrogação de prazo de execução, o campo Data do Aditivo será preenchido quando a data excedente for informada.

**Data da Prorrogação: Informar a data que o aditivo será prorrogado.**

A partir da versão 12.1.29 conforme previsto em lei (8.666/93, capitulo III, incluindo os art. 54 ao art. 80) o sistema permitirá a redução de prazo de contrato. Permitindo a criação de aditivo com data antecipação  menor que a data término com aditamento.

Exemplo: Contrato com data de início em 01/06/2020 e data termino com aditamento para 01/10/2020. O sistema permitirá que a data seja reduzida para 01/09/2020 fazendo as devidas validações para períodos liberados e medidos.

**Data de Utilização:** Informa quando e em qual período, os registros que modificam o contrato estarão disponíveis para medição/consumo. Preenchendo este campo, os dados passarão a vigorar a partir desta data, ou seja, o item do aditivo será impresso somente em períodos em que a data vigente seja maior ou igual a data definida.

**Status:** Este campo informa o status em que se encontra o aditivo.

**Descrição:** Descrição do aditivo criado.

Na aba "Campos complementares de Aditivos de Contrato" pode se definir um valor previsto para o aditivo.

Ao criar um aditivo, o mesmo é criado com o status inicial definido para contrato. Para cada status teremos as seguintes de acordo com  o  .

Será possível visualizar o detalhamento do aditivo nos anexos de contrato e ao editar o aditivo .

Atenção

Para excluir um aditivo de contrato que possua itens associados e medido, é necessário remover as medições desses itens, para só então excluir o aditivo de contrato.  
Em caso de remoção dos itens associados ao aditivo contratual, será gerado um novo atendimento para o TAA. O atendimento deverá ser concluído com aprovação para que os itens associados sejam excluídos.

Atenção

Nos itens do aditivo, é possível ajustar o valor da coluna "Valor Total", com a quantidade sendo calculada automaticamente. Contudo, para isso, é imprescindível que o parâmetro de contrato "Grandeza principal de medição de contrato" esteja definido como "Valor", ou que o parâmetro correspondente no projeto, na aba Contratos/Medição, também esteja definido, caso o do contrato não esteja. 

Ao calcular o contrato, o valor informado será considerado, não se restringindo apenas à quantidade definida no item do aditivo.

 

        [Novo Item](http://tdn.totvs.com/display/LRM/Novo%20Item) 

[Alteração de Item Contratado](http://tdn.totvs.com/pages/viewpage.action?pageId=421385121)

  Gerar Workflow de Aprovação

           Cancelar Workflow de Aprovação

Quando o projeto estiver integrado com o TAA (TOTVS Aprovações e Atendimento), antigo RM Agilis, e estiver parametrizada a aprovação de adiantamentos de contratos , ao criar um adiantamento estarão disponíveis nos processos do adiantamento as opções para gerar ou cancelar o workflow de aprovação. 

Anexos

  

[Detalhamento de Aditivo](http://tdn.totvs.com/display/LRM/Detalhamento+do+Aditivo?moved=true)

[Histórico de Aditivo](http://tdn.totvs.com/pages/viewpage.action?pageId=421385482)
