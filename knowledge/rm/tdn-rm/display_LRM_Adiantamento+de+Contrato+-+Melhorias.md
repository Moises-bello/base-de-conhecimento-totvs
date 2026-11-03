---
content_hash: 235d670201a7b33135b2f758f17c43258d45b6670885b0a35e4f7a49fd890a16
fetched_at: '2026-06-29T00:08:40.796730+00:00'
page_id: '286505454'
product: rm
source: tdn-rm
title: Adiantamento de Contrato - Melhorias
type: documentation
url: https://tdn.totvs.com/display/LRM/Adiantamento+de+Contrato+-+Melhorias
version: 114
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Contratos |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado/Ticket** | 682055 | | |
| **País** | Brasil e demais países da América Latina | | |

   

# Objetivo

Evoluir o funcionamento do Adiantamento nos Contratos para atender à demanda das empresas do segmento de Construção & Projetos, incluindo novos dados e consistências que permitam à empresa um controle efetivo e otimizado dos adiantamentos, bem como da sua correta dedução quando da liberação das medições contratuais.

Essa evolução irá contemplar tanto o backoffice RM como o backoffice Protheus.

Não constarão desse documento as funcionalidades relacionadas ao Adiantamento já existentes até a versão 12.1.17 do TOTVS Obras e Projetos, e que não sofreram nenhuma modificação devido às implementações que aqui serão descritas.

 

# Definição da Regra de Negócio

Como regra, um contratante deve efetuar o pagamento, somente após o cumprimento da obrigação pelo contratado, porém em contratos de obras e de fornecimento para entrega futura de bens ou de serviços, é prática comum a realização de adiantamentos de pagamentos.

Para proporcionar maior controle e tornar mais eficaz o Adiantamento já disponibilizado pelo TOTVS Obras e Projetos, estamos liberando algumas implementações, que iremos descrever a seguir.

# Criação de um Adiantamento de Contrato

No momento da criação de um adiantamento de contrato o sistema irá verificar e efetuar as seguintes consistências:

* Não permitir a criação de um adiantamento de contrato cujo valor seja superior ao valor do contrato, gerando mensagem específica;
* Não permitir a criação de um adiantamento de contrato cujo valor seja superior ao saldo do contrato, gerando mensagem específica;
* Não permitir a criação de um adiantamento de contrato cujo valor seja superior ao valor do saldo do contrato deduzindo o saldo dos adiantamentos já existentes para o contrato, gerando mensagem específica;
* O valor do adiantamento somente poderá ser alterado caso ainda não tenha sido efetuada nenhuma liberação para o adiantamento.

No Anexo de Adiantamento de Contrato será criado o campo Saldo, que apresentará o saldo atualizado do adiantamento.

Deverá existir tag de perfil específica para a criação/edição de um adiantamento.

# Liberação de um Adiantamento de Contrato

No momento da liberação de um adiantamento de contrato o sistema irá:

* Não permitir a liberação de um adiantamento de contrato cujo valor seja superior ao saldo do contrato, gerando mensagem específica;
* Não permitir a liberação de um adiantamento de contrato cujo valor seja superior ao valor do saldo do contrato deduzindo o saldo dos adiantamentos já existentes para o contrato, gerando mensagem específica;
* Bloquear o campo "Valor do Adiantamento";
* Atualizar o campo relativo à data de liberação do adiantamento;
* Atualizar o campo relativo ao Saldo do adiantamento;
* Alimentar a aba Detalhes do Adiantamento com as informações relativas à liberação efetuada;
* Gravar o usuário que efetuou a liberação do adiantamento.

Ao ser efetuada uma liberação de adiantamento, o TOTVS Obras e Projetos irá gerar o respectivo título financeiro no backoffice Protheus.

# Aba Detalhes do Adiantamento

No anexo de Adiantamentos de Contrato, ao editar um contrato, será apresentada a aba "Detalhes do Adiantamento" que estará disponível somente após a liberação do adiantamento.

Esta aba não permite edição e irá conter as seguintes informações:

* Data: Data em que foi liberado o adiantamento ou o período;
* Usuário: Deverá ser preenchido com o código do usuário que efetuou a Liberação do Adiantamento ou do Período;
* Operação: Deverá ser preenchido com "Liberação do Adiantamento", "Liberação do Período XXX" ou "Estorno da Medição do Período XXX" conforme o caso;
* Valor: Na liberação do adiantamento será atualizado com o próprio valor do adiantamento e na liberação do período será atualizado com o valor de dedução de adiantamento constante da mesma.

# Liberação do Período

No processo de Liberação do Período o nome da aba "Detalhamento das Retenções / Deduções" passa a ser "Detalhamento das Retenções / Deduções / Adiantamentos".

Nessa tela, da mesma forma que para a retenção, o adiantamento passa a ter grid específica com os mesmos campos da Retenção e Dedução. Assim, na grid do detalhamento das Deduções devem estar disponíveis somente detalhamentos do tipo D e na grid do detalhamento do Adiantamento devem estar disponíveis somente detalhamentos do Tipo A.

Caso nos defaults do contrato exista detalhamento do tipo adiantamento cadastrado, o sistema, automaticamente deverá apresentá-lo na tela do detalhamento do Adiantamento, efetuando o devido cálculo conforme o percentual cadastrado nos defaults.

Ainda na tela do Detalhamento, o botão "Calcular valor das retenções/deduções" terá seu nome alterado para "Calcular valor das retenções/deduções/adiantamentos" e o campo "Valor total retido/deduzido" terá seu nome alterado para "Valor total retido/deduzido/adiantado".

O valor total de adiantamentos constantes do detalhamento deve ser somado ao valor total das deduções e ao valor total das retenções para atualização do campo "Valor total retido/deduzido/adiantado" quando o botão "Calcular valor das retenções/deduções/adiantamentos" for acionado.

Deverá ser criada a tag de perfil "Liberar Período - Detalhar Adiantamento" e, somente usuários com essa permissão poderão ter acesso à grid do detalhamento do Adiantamento.

Na aba Medição da tela de Liberação do Período, o campo "Vlr.ret./ded. pdo." terá seu nome alterado para "Vlr.ret./ded./adiant.".

Ao ser executado o processo de liberação do período, o sistema irá efetuar as seguintes ações:

* Verificar se existe saldo de adiantamento a ser descontado no contrato, e em caso positivo, se não existir detalhamento de adiantamento informado para o mesmo, gerar mensagem em tela informando e questionando se o usuário deseja prosseguir a execução do processo;
* Não executar a execução do processo, caso a liberação do período faça com que o saldo a ser medido no contrato seja menor do que o saldo do adiantamento. Significa dizer que o sistema bloqueará medições que, se realizadas, farão com que a dívida do fornecedor seja maior do que o valor a ser medido pela empresa;
* Atualizar os Detalhes do Adiantamento;
* Atualizar o Saldo do Adiantamento.

Caso exista mais de um adiantamento para o contrato, e na liberação do período exista valor de adiantamento a ser deduzido, o sistema irá abatê-lo primeiramente do saldo do adiantamento mais antigo.

Da mesma forma que a Liberação do Período, tanto o Cancelamento da Liberação de Período como o Período de Estorno Automático, deverão atualizar o saldo do Adiantamento, sendo que no caso do estorno, a pasta Detalhes do Adiantamento também será atualizada.

Ao ser efetuada uma Liberação de Período na qual exista valor de adiantamento, o TOTVS Obras e Projetos irá gravar o valor do adiantamento no movimento gerado no backoffice Protheus para que seja efetuado o controle financeiro do mesmo.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
