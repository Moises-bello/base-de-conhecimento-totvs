---
content_hash: 1d32f12d98dfee8d027924aec99f9b062d0cab403cf8ab126d345cd6822b3e45
fetched_at: '2026-06-29T00:05:56.372089+00:00'
page_id: '149881856'
product: rm
source: tdn-rm
title: COMO FAZER - Roteiro para Transferir Funcionário de Seção e Coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=149881856
version: 1
---

Transferências de funcionários para seções/entidades que impliquem em mudança de CNPJ são tratadas no sistema como rescisões.

Como proceder:

1. Na visão do Cadastro de Funcionários, clique na linha correspondente ao funcionário desejado e, em seguida, clique no botão de Rescisão
2. O sistema perguntará: Confirma demissão deste funcionário? Sim/Não. Clique em Sim.
3. Será aberta a janela de pasta demissão.

Todos os campos devem ser preenchidos da forma mais apropriada à transferência. Contudo, o Tipo de Demissão deverá necessariamente conter um dos seguintes valores:

* Transferência sem ônus para cedente: Significa que o cedente do funcionário, ou seja, a empresa, filial ou seção de onde o funcionário está sendo transferido, não arcará com o pagamento das verbas rescisórias. Neste caso, não haverá cálculo da rescisão.
* Transferência com ônus para cedente: Inversamente ao caso anterior, neste tipo de transferência o cedente do funcionário arcará com o pagamento das verbas rescisórias. O sistema fará ou não o cálculo da rescisão dependendo do critério do usuário que poderá optar por realizá-lo depois.

      4. Ao se estabelecer um destes tipos para o campo de Tipo de Demissão, será exibido um quadro com opções específicas para transferência:

* + Realiza transferência para a mesma coligada: Transferências para outras coligadas não possibilita a migração de dados da ficha financeira do funcionário para a coligada destino. Contudo, o usuário poderá optar por transferir os históricos.
  + Realiza transferência para outra base de dados: Trata-se de uma situação específica e desaconselhada para a maioria dos usuários. Poderá ser utilizada para determinar que o funcionário foi transferido para outra coligada que encontra-se em uma outra base de dados não interligada.
  + Altera chapa do funcionário demitido: Quando de transferências, o usuário poderá determinar um novo número de chapa para o funcionário. Por esta opção, o usuário poderá determinar se o registro do funcionário demitido ou se do ativo transferido que receberá a nova chapa.

      5. Após clicar em Salvar ou OK para confirma o cadastramento da rescisão, o sistema verificará da necessidade de cálculo das verbas rescisórias conforme detalhamento do item 3.

      6. Caso exista um registro de usuário associado ao funcionário, o sistema questionará sobre a desativação ou não deste registro de usuário.

      7. Em seguida, será exibida a janela para preenchimento dos dados de transferência onde deverão ser preenchidos os dados referentes ao novo registro de funcionário a ser criado na empresa, filial ou seção de destino.

      8. Caso o tipo de demissão tenha sido "5" (Transferência sem ônus para o cedente) o tipo de admissão deverá ser necessariamente "T" (Entrada por transferência sem ônus para o cedente). Caso o tipo de demissão tenha sido "6" (Transferência com ônus para o cedente) o tipo de admissão correspondente será o "E" (Entrada por transferência com ônus para o cedente). Estas combinações: 5-T e 6-E, são importantes para o perfeito funcionamento do sistema.

     9. Após confirmação desta função e nenhuma inconsistência tenha sido apurada, o processo de transferência estará concluído.

É importante ressaltar que o processo de transferência duplica o cadastro de funcionário, ou seja, será criado um novo cadastro na empresa, filial ou seção de destino sem que o cadastro antigo seja excluído.
