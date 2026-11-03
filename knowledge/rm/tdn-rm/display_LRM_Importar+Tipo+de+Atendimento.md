---
content_hash: d2b995c41d1161728ae833da8d00a60955e2238e48acf269d548e1b0a95c3036
fetched_at: '2026-06-29T00:11:10.285268+00:00'
page_id: '642973128'
product: rm
source: tdn-rm
title: Importar Tipo de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Importar+Tipo+de+Atendimento
version: 16
---

Ao final da importação desse tipo de atendimento com relatório,

Nos processos da visão do Tipo de Atendimento será possível importar um arquivo contendo um ou mais Tipos de Atendimentos. Esse arquivo é gerado através do processo de .

Siga os passos abaixo para importar tipo de atendimento:

1 - Selecione em "Processos" a opção "Importar Tipo de Atendimento":

2 - Em seguida, será exibida a tela de importação e para informar o local onde o aquivo a ser importado se encontra:

3- Selecione o arquivo:

4 - Para começar, será necessário informar se deseja criar um grupo de tipo de atendimento, conforme o informado no tipo de atedimento origem e que será importado; ou se deseja informar um grupo que já existe cadastrado no banco de dados:

5 - Nessa etapa, o usuário deverá validar algumas regras relacionadas ao tipo de repasse usado nas etapas do tipo de atendimento origem, que será importado.

Se o repasse ocorrer para um atendente específico, será necessário definir o atendente, que será o responsável por essa etapa no tipo de atendimento destino, que será criado ao final do processo:

Também pode haver etapa onde o repasse seja realizado através de um grupo de atendentes, nesse caso será necessário informar o grupo:

E por fim, repasses realizados atráves de fórmulas e SQL's. Nesse caso, as fórmulas e SQL's usadas serão listadas para conferência.

Se a fórmula ou SQL, não existir na base onde o tipo de atendimento está sendo importado, o usuário poderá revisar o texto e informar se deseja importar com o mesmo código ou codigo diferente:

Caso já exista fórmula ou SQL com o mesmo código no banco de dados, será exibida uma tela comparativa para que o usuário possa avaliar a diferença e decidir

* se irá manter a atual;
* importar substituindo;
* ou importar com outro código (Nova fórmula ou SQL).

**Tipos de Atendimentos com Relatórios**

Caso o tipo de atendimento origem possua algum relatório vinculado, ao exportar esse tipo de atendimento, o usuário receberá uma notificação ao final do processo; informando-o que será necessário exportar também o(s) relatório(s) e importar no destino, para então associá-lo(s) no tipo de atendimento destino, que será criado após a importação:

Ao final da importação desse tipo de atendimento com relatório, outra mensagem lembrará ao usuário de associar os relatórios (exportados e importados separadamente, através do módulo de serviços globais), ao tipo de atendimento e respectiva etapa onde estavam associados, agora no destino:

**Tipos de Atendimentos com Local de Entrega**

Um local de entrega, possui informações especificas por coligada e caso o tipo de atendimento tenha algum local definido, o tipo de atendimento será importado sem este vinculo. Neste caso, deve ser criado na coligada de destino e vinculado manualmente no tipo de atendimento.  O local de entrega é definido no anexo de "Local de Entrega" no cadastro do "Tipo de Atendimento", sendo possível a inclusão de um ou mais locais.
