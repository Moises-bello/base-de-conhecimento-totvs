---
content_hash: 39f4e1803c8a58ad36b050ecc9ab395a3c9e977e9db4fcb3d02302c6adf5c7f2
fetched_at: '2026-06-29T00:08:18.714765+00:00'
page_id: '266966451'
product: rm
source: tdn-rm
title: ER_CPTOP001-537_Reajuste_no_Contrato_de_Insumos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPTOP001-537_Reajuste_no_Contrato_de_Insumos
version: 27
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | CPTOP001 | **IRM1** |  |
| **Requisito1** | CPTOP001-537 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | |  |  | | --- | --- | | **Pré-requisitos para melhor entendimento da especificação** | | | **Entidade** | **Link** | | Reajuste de contrato de maneira diferenciada por tipo de serviço contratado | [ER\_PCREQ-8789\_Reajuste\_de\_Contrato\_de\_Maneira\_Diferenciada\_por\_Tipo\_de\_Servico\_Contratado](http://tdn.totvs.com/display/LRM/ER_PCREQ-8789_Reajuste_de_Contrato_de_Maneira_Diferenciada_por_Tipo_de_Servico_Contratado) | | Melhorias no Reajuste de Contrato por Item Associado | [ER\_CPTOP001-10\_Melhorias\_no\_Reajuste\_de\_Contrato\_por\_Item\_Associado](http://tdn.totvs.com/display/LRM/ER_CPTOP001-10_Melhorias_no_Reajuste_de_Contrato_por_Item_Associado) | | Contrato Extra Histograma | <http://tdn.totvs.com/display/public/LRM/TSRIJY_ER_Contrato_Extra_Histograma> | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Possibilitar que contratos do tipo **Contratos de Insumo, Contratos de Fornecimento de Material e Contratos Extra-Histograma**também possam ter os valores dos objetos associados, reajustados, através do processo de **Reajustar Itens Associados ao Contrato**e consequentemente a utilização das funcionalidades envolvidas.

## Definição da Regra de Negócio

Os contratos do tipo **Contratos de Insumo, Contratos de Fornecimento de Material**e **Contratos Extra-Histograma** também permitem que os objetos associados possam ter os valores reajustados através do processo de **Reajustar Itens Associados ao Contrato**. Para esse tipo de contrato algumas particularidades podem ser consideradas assim como:

**1 - Cadastro de Contratos**

* O tipo de reajuste "**Por Item Associado**" pode ser selecionado para contratos de insumo, de fornecimento de material ou extra-histograma, também com a obrigatoriedade de se informar o **Período de Reajuste** (Mensal ou Anual), a **Data Base de Reajuste**e a **Aplicação do Reajuste** (Valor Inicial Contratado ou Valor Atual) ().

**2 - Processo de **Reajustar Itens Associados ao Contrato****

* Na tela do processo, é possível visualizar os objetos (insumos) associados aos contratos, onde para cada objeto, poderá ser definido um percentual de reajuste ();
* Para definir o reajuste para um objeto, é necessário selecioná-lo na grid, especificar o percentual e e clicar em **Aplicar Percentual**;
* Para os contratos que utilizam objetos associados, não existem agrupadores por índices assim como existe para contratos de **Prestação de Serviços**;
* **Data de Reajuste**, **Períodos Disponíveis** e **Ano**, podem ser utilizados para a definição da Data de Reajuste que o processo utiliza;
* Ao executar o processo, todas as regras e consistências existentes para reajuste de contratos de Prestação de Serviços são consideradas, algumas principais como:
  + O **Valor Unitário Contratado** do objeto é reajustado;
  + Objetos em períodos consumidos (não utilizado para contratos de fornecimento de material): O consumo do objeto é recalculado, considerando o novo valor contratado;
  + Objetos em períodos liberados (não utilizado para contratos de fornecimento de material): Acontece o recálculo do resíduo que é a diferença do valor liberado em relação ao valor recalculado do consumo considerando o reajuste. Esse resíduo é ser tratado como valor consumido do objeto em um novo período de reajuste:  
    - É criado um consumo para o objeto, contendo apenas o resíduo do recálculo, como a quantidade 0(zero) ();
    - Para o período de reajuste não deve ser permitido consumir objetos, apenas consultar os consumos incluídos pelo sistema;
    - A situação do período de reajuste após sua criação é de "**Consumido**" sendo passível de liberação;
    - Apenas os processos de "**Liberar Período**", "**Gerar Integração com Suprimento/Faturamento**" e "**Cancelamento de Liberação**" estão disponíveis para o período de reajuste.
  + Aditivos contratuais também são considerados;
  + As demais regras de reajuste são as mesmas utilizadas para contratos de Prestação de Serviço;
  + Para contratos de fornecimento de material, o reajuste somente será possível se **NÃO** existirem consumos para o objeto selecionado, pois quem controla o consumo e liberação do período é o módulo de **"Geração de Pedidos"**, portanto, para esse tipo de contrato, o período de reajuste não será criado.

**3 - Consumir Objetos do Contrato** 

* No processo de consumir objetos do contrato um alerta é exibido para que o usuário saiba que os objetos do contrato são passíveis de um reajuste caso o mesmo não tenha sido realizado ();
* A inclusão e exclusão de consumo de objetos não é permitido para períodos de reajuste, onde as informações estarão disponíveis apenas para consulta na aba de Objetos Consumidos;
* O **Valor Contratado** do objeto que é exibido no processo, considera a data em que o reajuste foi realizado, pois, apesar de o valor ter sido reajustado, a informação que deve ser exibida deve respeitar o reajuste:
  + Ex.:

* **TOTVS HTML Framework**
  + A funcionalidade de Consumir Objetos em HTML tem o mesmo comportamento que o processo da MDI, onde a inclusão e exclusão não são permitidos para períodos de reajuste, onde o valor contratado deve obedecer os reajustes realizados e onde a mensagem de alerta deve ser exibida para períodos que tem objetos passíveis de reajustes.

**4 - Geração de Pedidos e Pedido Extra**

* No módulo de Geração de Pedidos e Pedido Extra, o valor do item do pedido (Preço), quando associado à um determinado contrato que sofreu reajuste, considera a data em que foi realizado o reajuste, assim como citado em relação ao processo de consumir objetos do contrato. Ao criar uma nova solicitação de pedido, o período do contrato é criado com as datas inicial e final igual à data de solicitação. Se o reajuste tiver sido realizado após a data de solicitação, o preço exibido deverá ser diferente do Valor Unitário Contratado, que já foi alterado pelo reajuste, pois o mesmo ainda não havia entrado e vigor.

**5 - Processo de Cancelar Último Reajuste de Objeto Associado**

* No anexo de **Objetos de Contrato** existe o processo de **Cancelar Último Reajuste de Objeto Associado** (). Basta apenas selecionar o(s) objeto(s) associado(s) ao contrato e executar o processo, nesse momento o último reajuste realizado para o objeto é excluído e os valores recalculados:
  + O Cancelamento acontece da seguinte maneira:  
    Objeto: M0001 - Areia Lavada  
    Valor Inicial: 100,00  
    Percentual de Reajuste: 10%  
    Valor Reajustado: 110,00  
    Ao cancelar o reajuste, é verificado se o valor atual do objeto é igual ao valor anterior reajustado, caso positivo, o valor é alterado para o valor anterior ao reajuste, e caso contrário, o cancelamento não é processado.

* Consistências necessárias ao processo que impedem a execução do mesmo:
  + Validar se o Tipo de Reajuste do contrato está definido como "Por Item Associado";
  + Validar se existem reajustes para serem cancelados;
  + Validar se o valor do objeto é igual ao valor anterior reajustado;
  + O cancelamento do reajuste do objeto somente é processado se não existir nenhum período principal liberado com a data de liberação maior ou igual à data do reajuste onde o mesmo está presente;
  + O cancelamento do reajuste do objeto somente é processado se não existir nenhum período complementar de reajuste liberado onde o mesmo está presente;
  + Período Consumido: Ao cancelar o reajuste realizado para o objeto, os consumos dos períodos reajustados são recalculados, pois o valor do objeto é alterado para o valor anterior ao reajuste. O recálculo é realizado, também, para todos os períodos consumidos que tem a data maior que a data de reajuste. Períodos de estorno não são considerados pois o mesmo não deve ser recalculado pelo fato de ser um valor predefinido que não deveria ser ajustado;
  + Período Principal Liberado: Ao cancelar o reajuste realizado para o objeto, o consumo no período de reajuste é excluído e caso não exista mais nenhum consumo no período, o mesmo também é excluído;
  + Para contratos de fornecimento de material, o reajuste somente será cancelado se **NÃO** existirem consumos que foram incluídos após o reajuste, para o objeto selecionado, pois quem controla o consumo e liberação do período é o módulo de **"Geração de Pedidos"**.

**6 - ****Anexo de Reajustes de Objeto Associado******

* No anexo de Objetos de Contrato, na tela de edição, é possível visualizar um outro anexo de "Reajustes do Objeto Associado" (). Nesse anexo são exibidos todos os reajustes que foram realizados para o objeto selecionado.

**7 - Deduções e Retenções**

* O período de reajuste (Ex.: 0001R001) é criado a partir de períodos principal e complementar que se encontram liberados. Assim como acontece com os rateios em contratos de serviços, as dedução e retenções também são incluídas nos novos períodos de reajuste e não somente para os contratos de serviços mas para todos os contratos que utilizam reajuste por item associado e que também permitem inclusão de deduções e retenções. Períodos de reajuste permitem a inclusão/alteração/exclusão de deduções e retenções a partir desta versão. Na inclusão das deduções e retenções que ocorre ao solicitar o reajuste de um determinado item, é feito o cálculo para encontrar a proporção de cada dedução ou retenção em relação ao resíduo. Uma mesma dedução ou retenção pode estar associada à um período principal e a um período complementar, sendo assim os valores no período de reajuste devem considerar essa possibilidade. Os detalhes podem ser verificados no exemplo a seguir:
* Ex.:
* O campo medido das deduções e retenções no período de reajuste é **Percentual** pois representa a proporção em relação aos períodos anteriormente liberados. O exemplo acima demonstra as deduções e retenções considerando um período principal 0001 e um período complementar 0001C001, ambos liberados. O cálculo do percentual acontece da seguinte forma:
  + Deduções:
    - Percentual no período de reajuste: Soma dos valores da dedução dos períodos, dividido pela soma dos valores da medição dos períodos:
      * Refeição: (125,00 + 85,00) / (2.500,00 + 1.700,00) = 5,000%
      * EPI: (50,00 + 34,00) / (2.500,00 + 1.700,00) = 2,000%
      * Vale Transporte: (17,00) / (1.700,00) = 1,000%
    - Valor no período de reajuste: Percentual vezes a medição do período de reajuste:
      * Refeição: 5,000% \* 420,00 = 21,00
      * EPI: 2,000% \* 420,00 = 8,40
      * Vale Transporte: 1,000% \* 420,00 = 4,20
  + Retenções:
    - Percentual no período de reajuste: Soma dos valores da retenção dos períodos, dividido pela soma dos valores da medição dos períodos menos o total das deduções se o parâmetro de projeto **"Permitir calcular retenção sobre o valor total"** estiver desmarcado:
      * ISS: (69,75 + 46,92) / ((2.500,00 + 1.700,00) - (175,00 + 136,00)) = 3,000%
      * INSS: (46,50 + 31,28) / ((2.500,00 + 1.700,00) - (175,00 + 136,00)) = 2,000%
      * Retenção Técnica: (15,64) / ((1.700,00) - (136,00)) = 1,000%
    - Valor no período de reajuste: Percentual vezes a medição do período de reajuste menos o total das deduções se o parâmetro de projeto **"Permitir calcular retenção sobre o valor total"** estiver desmarcado:
      * ISS: 5,000% \* (420,00 - 33,60) = 21,00
      * INSS: 2,000% \* (420,00 - 33,60) = 7,73
      * Retenção Técnica: 1,000% \* (420,00 - 33,60) = 3,86

**8 - Cálculo do Contrato**

* O cálculo do valor dos contratos de insumo, fornecimento de material e extra-histograma considera esse novo tipo de período de reajuste, porém desconsiderando a quantidade zero (0) consumida do mesmo, apenas o valor consumido. Esse valor do objeto no período de reajuste considera os consumos realizados acima de 100%, porém, no cálculo do projeto o mesmo valor não é considerado, assim como ocorre com os consumos até 100%. Para o período de reajuste é descontado o valor que ultrapassa os 100% do objeto contratado:
* Ex.:

**9 - Exclusão de Projetos**

* No momento da exclusão de um determinado projeto que possui reajustes realizados para objetos de contrato, os reajustes realizados são excluídos juntamente com os contratos.

**10 - Revisão de Projetos**

* Tanto para Revisão de Projetos quanto para Revisão Múltipla, os reajustes realizados para objetos de contrato são copiados para o novo projeto.

**11 - Backup e Restore**

* **A partir da versão 12.1.15**, o Backup e Restore copia os reajustes realizados para objetos de contrato, porém os períodos de reajuste não são copiados, pois, como no Restore os períodos liberados backupeados são considerados apenas como medidos, e os períodos de reajuste são criados a partir de um período liberado, os mesmos não são incluídos.

    **Importante:**

* **O processo "Reajustar Itens Associados ao Contrato" somente estará disponível para contratos do tipo "Prestação de Serviços", "Contrato de Insumo", "Contrato de Fornecimento de Material" e "Contrato Extra-Histograma";**
* **Alterações e exclusões de objetos associados e também de aditivos não são permitidos se os mesmos tiverem reajustes realizados;**
* **O contrato extra-histograma difere em alguns pontos do contrato de insumos e de fornecimento de material, como por exemplo em validações de quantidades e saldos. O detalhamento dessas informações podem ser encontrados na especificação de Contrato Extra-Histograma.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Contratos | [Alteração] | Controle -> Contrato -> Contratos | - |

## Protótipo de Tela

**Protótipo 01**

**Protótipo 02**

**Protótipo 03**

**Protótipo 04**

****Protótipo 05****

**Protótipo 06**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
