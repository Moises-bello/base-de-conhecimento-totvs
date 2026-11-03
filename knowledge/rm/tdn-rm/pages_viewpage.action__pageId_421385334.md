---
content_hash: af4a3f50b69edee7e1129edf7c68424ada0320a935604120a14f52d6074ce479
fetched_at: '2026-06-29T00:09:15.281535+00:00'
page_id: '421385334'
product: rm
source: tdn-rm
title: Cotação de Insumos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385334
version: 1
---

**Cotação de Insumos**   
O módulo de Cotação de Insumos foi criado para atender a cotação de preços de insumos para um ou vários projetos. Quando existir um projeto no contexto (projeto aberto) o processo é executado somente para aquele projeto. Quando não existir um projeto aberto o primeiro passo do processo é escolher para quais projetos se deseja realizar a cotação. A Cotação de Insumos tem um limite de ser executada somente por Coligada.  
O processo está disponível através do menu Orçamento | Insumos | Cotação.  
Passo a Passo  
1º) Na primeira tela do Assistente de cotação de preços de insumos, aparecerá um filtro por grupo de custo.  
Serão exibidos todos os grupos de custo do projeto (projeto aberto) e os grupos de custo globais (projeto global). Selecione os grupos de custo que terão os insumos cotados.  
Marque a opção "Somente os insumos utilizados no projeto" e o sistema exibirá apenas os insumos que possuem um dos grupos de custo selecionados e que estejam sendo utilizado no projeto (Curva ABC de Insumos).  
Os insumos não ficam disponíveis para cotação, quando:  
- Os insumos só estão inseridos em tarefas desativadas;  
- Os insumos só estão inseridos em tarefas que possuem preço cotado e ele está ativo;  
- Os insumos estão desativados nas composições que estão sendo utilizadas no projeto;  
- os insumos possuem unidade %.  
2º) Na segunda tela do Assistente de cotação de preços de insumos, aparecerá a listagem de insumos, incluindo os que ainda não têm preço, de acordo com o filtro selecionado e ordenado pela coluna 'Total no Projeto' (valor total do insumo no projeto). Isso não impede que você faça outras ordenações.  
Para preencher o campo 'Total no Projeto' o sistema considera os valores da curva abc de insumos. Dessa forma, a cotação de insumos, está sendo exibida e ordenada de acordo com a curva abc de insumos. Por essa razão, se a curva abc de insumos não foi calculada nenhuma vez, é necessário calculá-la para que os valores dos insumos apresentados estejam atualizados.  
Se houver alterações de preços, a curva abc de insumos deve ser recalculada.  
Nas colunas dos insumos, estarão disponíveis para alteração o preço cotado e o preço improdutivo dos insumos (no caso do preço improdutivo, apenas para insumos do grupo A – Equipamentos). Pode-se alterar também a unidade e a moeda de cotação.  
**Criar Novo Preço** - caso esta opção esteja marcada, será criado um novo preço para o insumo, caso não esteja marcada, o preço será o preço ativo atual do insumo.  
**Ativar o novo preço** – ativa o novo preço criado.  
**Descrição do novo preço** – nome para o novo preço criado. Caso este campo não seja preenchido no momento da criação do novo preço, a descrição do preço será "Preço em" + <Data atual>.  
Caso os novos valores dos preços de todos os itens tenham um aumento em percentual igual, pressione o ícone "Aplicar fator nos preços", preencha com um valor o campo "Multiplicar preços marcados por" e confirme a alteração, que todos os preços serão alterados, isto é, serão multiplicados por este valor. Depois, se desejar, pode-se alterar os preços que não estiverem dentro deste valor.  
Caso você opte por utilizar vigência de preços, pressione o ícone "Aplicar vigência nos preços", e no campo Período, informe a data de vigência (validade) do preço do insumo, em seguida marque as aplicações desejadas (Previsto, Realizado, Medido) e confirme a alteração pressionando o ícone "Aplicar Vigência", que todos os preços dos insumos selecionados serão atualizados.  
**Exemplo:**  
Selecione um insumo.  
No campo Preço Cotado, informe o valor do novo preço do insumo correspondente.  
No campo Vigência, informe a data de vigência (validade) do preço do insumo no cronograma indicado.  
No campo Aplicação, informe, em qual cronograma (Previsto, Realizado, Medido) a vigência do preço do insumo.  
Marque a opção de "Criar Novo Preço".  
Preencha a descrição do novo preço e em seguida Clique no botão "Avançar".  
Clique em "Concluir".  
**Observações:**  
Sempre que você quiser avaliar o resultado da mudança de um preço na coluna 'Total no Projeto' recalcule a curva abc de insumos.  
Não é permitido cadastrar duas ou mais vigências com o mesmo período e aplicação para um insumo.  
Se o insumo não tiver nenhum preço cadastrado, será realizado o preenchimento automático da unidade de cotação com a unidade do insumo e a moeda de cotação com R$ (real).  
A unidade sugerida para o preço cotado é a unidade do insumo e não é permitido que passe para a cotação de outro insumo sem informar a moeda em que o preço está sendo cotado.  
A cotação de insumos globais é feita criando-se um preço local ou atualizando um preço local que já estiver ativo. Se o insumo global não possuir um preço local e não for solicitada a criação, a cotação não será efetivada.  
Na moeda do preço insere a moeda do projeto.

|  |  |
| --- | --- |
|  | Veja Também |

---

Automatização do Processo de Cotação de Insumos
