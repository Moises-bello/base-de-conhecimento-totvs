---
content_hash: 4e5d0ab93cf05d792f74b3ddebe06a2bcd537ef99c48abf65ab14be4f526e48a
fetched_at: '2026-06-29T00:09:16.366020+00:00'
page_id: '421385521'
product: rm
source: tdn-rm
title: Gerar Integração de Suprimento/Faturamento - FLUIG
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385521
version: 2
---

---

Através do FLUIG agora é possível efetuar a liberação do período de contrato que integra com o sistema de Suprimento/Faturamento gerando para o BackOffice (Protheus, TOTVS Gestão de Estoque, Compras e Faturamento, entre outros) um movimento com o tipo, o produto, condição de pagamento, filial, local de estoque e centro de custo selecionados ou de acordo com os valores definidos no cadastro do contrato.

Para realização desse processo, é preciso que tenha já os itens abaixo criados no sistema: • Ter um contrato criado. • Ter itens ou objetos associados. • Ter Períodos gerados para o contrato. • Ter Períodos medidos • Parâmetro de Integrado com Suprimento/Faturamentos habilitados em Parâmetros (F6) - Projeto.

Para Gerar Integração com Suprimento/Faturamento do TOTVS Obras e Projetos no FLUIG, foi criado uma página para tal processo para que isso seja possível, onde deverá entrar com seu usuário e senha.

O acesso ao processo se dá através das páginas de "Medição de Item de Contrato" e "Consumir Objetos do Contrato" onde na visão de períodos, está disponível a opção dentro do agrupador "Outras Ações" – "Liberar para Suprimento/Faturamento"

Ao escolher a opção de Liberar para Suprimento Faturamento, a página aberta, contém o Resumo da Liberação. Essa aba também é a presente na Liberação de Período para o Financeiro.

Essa aba contempla todos os dados necessários para gerar a integração com o suprimento faturamento.

Dentro do Resumo da Liberação, existe o painel Valor da Medição, que contém os campos vindos da medição daquele período. (Perc. Reajuste, Sem Reajuste, Com Reajuste, Valor Retido/Deduzido no Período, Valor retido item, Valor Retido Total e Valor Líquido).

* % reajuste: Percentual que pode ser informado para reajustar a medição do período na liberação;
* Com reajuste: Valor da liberação aplicado o percentual de reajuste;
* Sem reajuste: Valor se o reajuste aplicado;
* Valor Retido/Deduzido no Período: Valor total da retenções e deduções no período. Este campo estará habilitado somente se não existirem deduções ou retenções, e no caso de existir os valores e percentuais devem estar zerados;
* Valor Retido no Item: Valor da retenção informada na medição do período;
* Valor Retido Total: Valor da soma da retenção informada na medição do período e da retenção informada na liberação do período;
* Total da Liberação: Valor total da medição adicionando o reajuste e subtraindo a retenção.

Abaixo dos valores de medição, temos as informações para Reajustes, Deduções, Retenções, Campos Complementares e Observações conforme cada campo abaixo:

* Reajustes: Uma tabela com um cadastro de reajuste informado no cadastro do contrato;
* Deduções: Utilizado para informar os tipos e valores de deduções do período. Existe, também, a opção para informar os produtos faturados à dedução onde a dedução deverá ser associada;
* Retenções: Utilizado para informar os tipos e valores de retenções do período;
* Campos Complementares: Possui os campos complementares cadastrados no Menu Cad. Gerais | Campos Complementares | Detalhamento Medição. (Não disponível nesta versão);
* Observação: Observação da liberação.

Abaixo, temos o painel somente da Integração Suprimento/Faturamento, que solicita que seja preenchido através das pesquisas de cada campo as informações obrigatórias para o movimento, como:

* Movimento: Informações que serão atribuídas ao movimento gerado no Suprimento/Faturamento
* Tipo de Movimento a ser gerado: O valor default pode ser definido no cadastro do contrato ou informado no momento da geração.
* Local de estoque: O valor default pode ser definido no cadastro do contrato ou informado no momento da geração.
* Estado: Utiliza como valor default o estado do projeto ou informado no momento da geração.
* Município: Utiliza como valor default o município do projeto ou informado no momento da geração.
* Condição de Pagamento: O valor default pode ser definido no cadastro do contrato ou informado no momento da geração.
* Filial: O valor default pode ser definido no cadastro do contrato, porém é utilizado somente se não estiver integrado com o Protheus, caso integrado, verifica se o parâmetro "Permite alterar filial do contrato" está marcado, não estando, a filial utilizada será a do projeto;
* Centro de Custo: Utiliza como valor default o centro de custo do projeto ou informado no momento da geração.
* Produto: O valor default pode ser definido no cadastro do contrato ou informado no momento da geração.
* Produtos Associados: Essa opção somente será exibida se o contrato for do tipo "Insumo" ou "Extra Histograma" e se o parâmetro de projeto "Considerar produtos associados no faturamento de contratos de insumo" estiver marcado;

Observação;

* Tabelas Opcionais: Devem estar parametrizadas no Suprimento/Faturamento para utilização
* Valores Extras: Devem estar parametrizados no Suprimento/Faturamento para utilização

Além das informações citadas, a página contém a Data de Liberação, que somente estará disponível se o parâmetro geral "Permitir data retroativa no faturamento de contratos" estiver marcado. Contém a opção de apenas Salvar as informações sem liberar o período, nesse caso apenas as informações da aba "Resumo da Liberação" sem considerar as informações de Suprimento/Faturamento serão salvas. Por fim, contém e a opção de Liberar Integração Suprimento/Faturamento com todas as opções selecionadas.

Se o período já estiver liberado a página não abrirá e a mensagem "O período selecionado já se encontra liberado." será exibida. O mesmo acontece caso tente abrir a página de Liberar para Suprimento Faturamento em um período que não tenha medição.

**Cancelamento:** O cancelamento de um período gerado para Suprimento/Faturamento, é realizado através da visão de Períodos, com o filtro "Todos" selecionado, onde irão visualizar períodos liberados e pendentes para liberação no período que foi gerado, através de "Outras Ações" e Cancelar Liberação.

Veja Também

---
