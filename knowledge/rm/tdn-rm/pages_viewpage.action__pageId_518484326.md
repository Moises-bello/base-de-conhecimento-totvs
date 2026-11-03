---
content_hash: 1005f080d0cece78c732ca3401c2cf1268560fd2eb1bbc3aa04ea3d135002191
fetched_at: '2026-06-29T00:10:30.050032+00:00'
page_id: '518484326'
product: rm
source: tdn-rm
title: Securitização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=518484326
version: 69
---

A securitização é o processo realizado pelas companhias securitizadoras que adquirem créditos imobiliários para lastrearem títulos imobiliários (Certificados de Recebíveis Imobiliários – CRIs) que serão negociados no mercado de capitais. Os certificados de recebíveis Imobiliários são títulos de crédito nominativos, escriturais e transferíveis, lastreados em créditos imobiliários. Estão previstos na Lei 9514/97, que disciplina o sistema de financiamento imobiliário.

Securitizar é transformar direitos creditórios - como os provenientes das vendas a prazo nas atividades comerciais, financeiras ou prestação de serviços - em títulos negociáveis no mercado. O Certificado de recebível imobiliário, assim, é uma securitização de direitos creditórios originados nos financiamentos imobiliários. A securitização pode ser estruturada em diferentes formatos. Em uma possível forma, o processo se inicia com um financiamento imobiliário, em que determinado cliente assume a obrigação de uma dívida. Essa dívida origina direitos creditórios à instituição financiadora. Em seguida, cria-se uma estrutura de securitização, como uma companhia securitizadora (Fundos de Investimento em Direitos Creditórios também têm sido utilizados).

Em resumo, é uma operação financeira em que a empresa (incorporadora) entrega o gerenciamento dos recebimentos para uma securitizadora e este lhe antecipa o valor acordado, cobrando uma taxa pela antecipação.

Ao acessar a visão do contrato de securitização será possível realizar todo o gerenciamento.

Para execução do processo, é necessário filtrar o contrato de securitização.   
Acesse a aba: **Recebíveis >>** **Securitização:**  
Dentre as opções disponíveis será possível filtrar os contratos de Securitização de **Venda** ou **Aluguel**. Após selecionar o contrato desejado, é necessário acessar o Menu Processos e selecionar a ação que deseja realizar **Efetivar** ou **Voltar** Situação do Contrato. 

Importante!

* Para acessar a Securitização o perfil associação ao usuário deve ter permissão na TAG: **[08.01] Securitização**
* Antes de efetivar o contrato é necessário preencher as informações para a geração do lançamento de securitização.
* Para voltar a situação do contrato ele precisa estar efetivado.
* Será possível voltar a situação do contrato apenas se o lançamento estiver em aberto.
* Caso o lançamento possua algum bloqueio ou restrição que impossibilite o seu cancelamento, será necessário ajustar a mesma antes de voltar a situação do contrato.
Informativo de Contrato encontra-se Securitizado ou não na visão de Contrato !

Tela de visão do Contrato mostra agora se está Securitizado - Securitização Marcado.

Caso a Securitização tenha sua Recompra .. Contrato não tenha mais Securitização , fica desmarcado !

Securitização - Venda e AluguelContrato SecuritizaçãoContrato Securitização |Contrato Securitização

* **Inclusão de Lançamentos no contrato de Securitização**

Após incluir o contrato de securitização será possível vincular os lançamentos que serão securitizados.   
Selecione o contrato cadastrado, vá ao **Menu>>Processos>>Inclusão de Lançamentos no Contrato de Securitização.** Será apresentado as vendas efetivadas com numero do contrato gerado que possuem lançamentos a receber disponíveis para securitização. É preciso selecionar a venda que será securitizada e clicar na opção **Avançar**.

Serão apresentados todos os lançamentos da venda que estão em aberto, é necessário selecionar os lançamentos que serão securitizados e clicar na opção "**Calcular Valor Securitizado**" os valores dos lançamentos serão atualizados para o valor presente,  após será possível **Executar** o processo. O campo **Valor Securitizado**, do contrato de securitização será preenchido com o valor calculado pelo processo de Inclusão de lançamentos no contrato de securitização.

Importante!

 Os títulos a receber provenientes dos contratos de venda que foram securitizados, poderão sofrer alteração da sua situação, caso haja a necessidade, as situações existentes hoje é: securitizado, repasse em atraso, recompra e devolução).  
- Para que os títulos modifiquem a sua situação temos os seguintes processos e as descrições da aplicação de cada um deles dentro do sistema:  
1 - Apuração Mensal Lançamentos em Atraso:   
     - Situação após o processo: Repasse Em Atraso)  
2 - Devolução:  
     - Situação após o processo: Devolução  
3 - Recompra:  
     - Situação após o processo: Recompra

* **Efetivação do Contrato**:

  Importante!
  + O campo vencimento na aba identificação do contrato de securitização, preenchido determina que irá gerar o lançamento com o valor total do contrato de securitização, quando o contrato for efetivado, os dados utilizados para a geração do lançamento a receber da securitizadora virão do campo "Parâmetro de Integração Financeira - Securitização". A Situação dos títulos securitizados após o processo: *Securitizado*

Ao efetivar o contrato de securitização , será criado um lançamento financeiro a receber referente ao valor antecipado,  para a inclusão deste lançamento é preciso editar o cadastro do contrato de securitização e preencher o Valor Antecipado e a Data de Vencimento. O lançamento financeiro gerado com valor antecipado está disponível no anexo Lançamento Financeiro.

Os lançamentos securitizados terão a conta caixa modificada para a conta caixa informada no contrato de securitização.   
O contrato passa assumir o status de contrato efetivado, dessa forma não será permitido modifica-lo. Somente os campos ("Descrição", "Parâmetro de Integração Financeira - Apuração", "Parâmetro de Integração Financeira - Devolução", "Parâmetro de Integração Financeira - Recompra") poderão sofrer alteração após o contrato ter sido efetivado.  
Os lançamentos que forem securitizados só poderão ser baixados utilizando a mesma conta/caixa informada no contrato de securitização. Não é possível incluir um boleto para um lançamento securitizado. Nesse caso, é a securitizadora a responsável pelo gerenciamento de cobrança ao cliente.

Selecione o contrato desejado, é necessário acessar o Menu Processos **Efetivar do Contrato.**

* **Voltar a situação do contrato**:

Ao executar o processo de voltar a situação do contrato, o lançamento financeiro a receber será apagado e o contrato passa assumir o status de contrato **Em Aberto**.  Caso os lançamentos securitizados não estejam em aberto ou possua algum bloqueio/restrição que impossibilite o seu cancelamento, será necessário ajustar a mesma antes de voltar a situação do contrato.

Selecione o contrato desejado, é necessário acessar o Menu Processos e selecionar a ação que deseja realizar **Efetivar** ou **Voltar** Situação do Contrato. 

Contrato Securitização Venda |

Gerando contrato de Securitização - Venda

Securitização | Contrato de Securitização – Venda

Novo contrato de Securitização

Criando novo contrato de Securitização

Inserir oCliente da Securitizadora se o tipo é : Securitizadora ou Empresa que será responsável pelas parcelas do Contrato.

Selecionando o Contrato que será feita a Securitização  -  Avançar

Selecionar as Parcelas do Contrato que serão securitizadas

Selecionada neste exemplo = 8 Parcelas

Clicar em : Calcular Valor Securitizado

Valor das 8 Parcelas = R$22.687,31

**Executar**

Processada

Lançamentos incluídos no Contrato Securitizado

Tela desenvolvida na primeira versão do módulo.  
A tela que vem a seguir é a nova tela, está já apresenta o novo campo para controle de quem administra o contrato de securitização. Isto será importante para determinar o comportamento no momento da baixa dos títulos securitizados, quanto a possibilidade de trocar ou não a conta caixa no momento da baixa dos títulos securitizados.

Inserir o Valor de Antecipação  
Inserir a Data de Vencimento do Título Securitizado

**Processo | Efetivar Contrato**

Processado

Lançamento Gerado

Importante - Baixando Títulos Securitizados:

* Os títulos securitizados ficam amarrados ao contrato de securitização.
* O Campo 'Responsável pela Adm' que foi incluído na aba "Identificação" do cadastro do contrato de securitização, indicará se será permitido a troca de conta caixa no momento da baixa dos títulos securitizados. Contratos cujo o valor seja determinado com o valor do campo 'Responsável pela Adm' como "Securitizadora" a conta caixa utilizada para o contrato de securitização será obrigatoriamente exigida como sendo a mesma no momento da baixa dos títulos securitizados no contrato de securitização. No caso onde o valor do campo for "Empresa" (Incorporadora que é a proprietária do empreendimento) a conta caixa utilizada para o contrato de securitização NÃO será obrigatoriamente exigida como sendo a mesma no momento da baixa dos títulos securitizados no contrato de securitização.
Permitir Aditivar contrato Securitizado.Contrato Securitização Aluguel |

**Contrato se Securitização Aluguel**

Contrato de Locação

Contrato de Securitização - Aluguel

Criando o Contrato

Processo | Inclusão de Lançamento no Contrato de Securitização

Selecionar o Contrato

**Avançar**

Parcelas do Contrato do Aluguel selecionadas - Calcular Valor Securitizado

Sistema mostra o valor das Parcelas selecionadas e em seguida - **Executar.**

Processado

Efetivando contrato Securitizado

Parcela criada .

ContabilizaçãoContabilização |

É possível realizar a contabilização do contrato de securitização através do processo '**Contabilizar/Estornar Securitização**'.

Importante:

* Para realizar o processo de contabilização o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.13] Contabilização do Contrato de Securitização**
* É necessário criar um Evento Contábil com o processo **Securitização**.

Durante o cadastro de um novo contrato de securitização ou edição de um contrato já salvo na base de dados será possível acessar a aba **Contabilidade**, onde deve ser informado o Evento Contábil que será utilizado para a criação da contabilização. Apos informar o Evento e salvar o contrato é necessário ir ao menu Processos>>Contabilizar/Estornar Securitização.

Deve ser selecionado o Tipo de Processo e a Data de Contabilização/Estorno e confirmar a operação.

Tipo de Processo:

* Contabilizar - Criar a contabilização respeitando o Evento Contábil informado no contrato.
* Estornar - Realizar o estorno da operação contábil.
* Recontabilizar(Estornar e Contabilizar) Refaz a contabilização do contrato de securitização.

Para visualizar a contabilização do contrato é necessário selecionar o contrato ir ao menu Anexos>>**Consultar Operação Contábil**.

Inserir o Evento contábil no cadastro da Venda:

Apuração Mensal de Lançamentos Em AtrasoApuração Mensal de Lançamentos Em Atraso |

Através do processo de apuração mensal, a empresa identificará o que não foi pago pelos clientes e que precisa ser pago à securitizadora. Serão apresentados os lançamentos em atraso do contrato de securitização que ainda não foram baixados no sistema.  
O objetivo do processo "Apuração Mensal Lançamentos em Atraso" é permitir que os títulos que se encontram em atraso possam ser recomprados pela incorporadora, ainda que já tenham sido enviados boletos para os compradores responsáveis pelo pagamento com informações bancarias de boleto da securitizadora. Essa funcionalidade permite manter os títulos em atraso sobre controle da incorporadora, sendo devolvidos pela securitizadora.  
Caso o título recomprado por motivo de atraso, já tenha sido enviado a banco pela securitizadora, a incorporadora pode efetuar o processo de "Apuração Mensal dos Lançamentos em Atraso" e, em seguida, utilizar o processo "Devolução do Valor Pago a Securitizadora".

Este processo utiliza o campo "Parâmetro de Integração Financeira - Apuração" para preenchimento dos dados necessários na geração do título a pagar para a securitizadora (Lançamento de Repasse).

Importante:

* Somente os lançamentos que forem selecionados na execução do processo serão recomprados.
* Os lançamentos que já se encontram baixados não serão considerados.
* Para realizar o processo de recompra o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.10] Apuração Mensal Lançamentos Em Atraso**
* Para consultar os lançamentos de repasse, o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.12] Lançamentos de Repasse**

 Para execução do processo deve ser selecionado o contrato de securitização ir ao menu **Processos>>Apuração Mensal Lançamentos Em Atraso**.

Neste processo apenas os lançamentos selecionados serão recomprados, desta forma é necessário selecionar o registros desejados e informar a '**Data de Pagamento**' em seguida clicar na opção '**Calcular Valor Securitizado**' e  confirmar a execução do processo. Ao termino do processo os lançamento selecionados serão retirados do contrato de securitização e será criado um lançamento de repasse para a securitizadora. Para visualizar o lançamento criado é necessário editar o contrato de securitização e ir na pasta '**Lançamentos de Repasse**'

Devolução do Valor Pago à SecuritizadoraDevolução do Valor Pago à Securitizadora |

Através do processo de 'Devolução do Valor Pago à Securitizadora', a empresa identificará as parcelas que foram pagas pelos clientes, devido a recompra delas por parte da empresa, seja parcelas em atraso ou por outro motivo.   Desta forma, a empresa tem que receber esses valores por parte da securitizadora, uma vez que recomprou essas parcelas e o cliente as pagou para a securitizadora.

A devolução será utilizada para gerar título a receber da securitizadora, com o intuito de aguardar o recebimento de um título que foi recomprado pelo processo de apuração mensal, mas que quem irá receber o mesmo ainda será a securitizadora e assim que receber, irá pagar a incorporadora.  

Este processo utiliza do campo "Parâmetro de Integração Financeira - Devolução" para preenchimento dos dados necessários na geração do título a receber da securitizadora.

Importante:

* Somente os lançamentos que forem selecionados na execução do processo serão calculados.
* Somente os Lançamentos que já se encontram baixados serão considerados.
* Para realizar o processo de recompra o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.14] Devolução do Valor Pago à Securitizadora**
* Para consultar os lançamentos de repasse o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.12] Lançamentos de Repasse**

 Para execução do processo deve ser selecionado o contrato de securitização ir ao menu **Processos>>Devolução do Valor Pago à Securitizadora**.

Neste processo apenas os lançamentos selecionados serão calculados, desta forma é necessário selecionar o registros desejados e informar a '**Data de Pagamento**' em seguida clicar na opção '**Calcular Valor Securitizado**' e  confirmar a execução do processo. Ao termino do processo os lançamento selecionados serão retirados do contrato de securitização "Repasse em Atraso" e será criado um lançamento de repasse do tipo "Devolução" a receber da Securitizadora.   
Para visualizar o lançamento criado é necessário editar o contrato de securitização e ir na pasta '**Lançamentos de Repasse**'

Recompra de Lançamentos SecuritizadosRecompra de Lançamentos Securitizados |

Através do processo de recompra de lançamentos securitizados do cliente, a empresa identificará os clientes que tem dívidas superiores a um determinado prazo e irá recomprar os lançamentos desses clientes. É necessário informa um prazo para a verificação dos lançamentos e devem ser apresentados todos clientes (por contrato de securitização) que possuem lançamentos com vencimento superior ao prazo informado.

A "Recompra de Títulos Securitizados" traz uma maior flexibilidade de gestão da carteira dos títulos securitizados, tendo como objetivo a recompra (reintegração) dos títulos para a carteira de recebíveis da incorporadora, nos casos em que julgar necessário e/ou compensatório financeiramente.

Este processo utiliza do campo "Parâmetro de Integração Financeira - Recompra" para preenchimento dos dados necessários na geração do título a pagar para a securitizadora.

Para definir o prazo é necessário acessar os parâmetros do sistema, através da aba Ambiente>>Parâmetros>>Totvs Incorporação>>Integração Financeira>>Financeiro. Nesta etapa deve ser preenchido no parâmetro '**Período limite para recompra de lançamentos securitizados vencidos(Nro Meses):**'.

Importante:

* O sistema irá consistir o contrato de securitização levando em consideração o período definido no parâmetro **"Período limite para recompra de lançamentos securitizados vencidos(Nro Meses):"**e caso um lançamento do cliente atenda os requisitos de vencimento todos os demais lançamentos serão retornados no processo.
* Neste processo deve ser selecionado todos os lançamentos para recompra
* Os Lançamentos que já se encontram baixados não serão considerados.
* Para realizar o processo de recompra o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.11] Recompra de Lançamentos Securitizados**
* Para consultar os lançamentos de repasse o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.12] Lançamentos de Repasse**

Para execução do processo deve ser selecionado o contrato de securitização ir ao menu **Processos>>Recompra de Lançamentos Securitizados**. Neste momento o sistema irá verificar se algum lançamento associado ao contrato de securitização selecionado se enquadra no período definido e retorna todos os lançamentos do cliente.

Neste processo todos os lançamentos serão recomprados, desta forma é necessário selecionar todos o registros e informar a '**Data de Pagamento**' em seguida clicar na opção '**Calcular Valor Securitizado**' e  confirmar a execução do processo. Ao termino do processo os lançamento selecionados serão retirados do contrato de securitização e será criado um lançamento de Repasse para a securitizadora. Para visualizar o lançamento criado é necessário editar o contrato de securitização e ir na pasta '**Lançamentos de Repasse**'

Desfazer Recompras/Devoluções |

Através deste processo é possível desfazer a recompra, o repasse e a devolução dos contratos securitizados que estão efetivados. É importante ressaltar que os registros que irão ser cancelados passam por todas as validações já existentes no sistema para cancelamento, desta forma caso seja identificado algo que impossibilite o cancelamento do registro não será possível realizar o processo de Desfazer até que a situação seja regularizada.

## Regras para a utilização do processo

* O Usuário poderá selecionar qualquer tipo de repasse, desde que a esta parcela esteja em aberto.
* **Devolução**:   
  Só poderá ser cancelado a devolução se os lançamentos associados a este lançamento estiverem em abertos (desfazer as baixas securitizadas antes de iniciar este processo)   
  Ao cancelar a parcela de devolução, os lançamentos associados a este lançamento de repasse voltarão para o status em Repasse Em Atraso.
* **Recompra/Repasse em Atraso:**   
  Só poderá ser cancelado se não existir a devolução da parcela.  
  Ao cancelar a parcela de repasse/recompra, os lançamentos associados a este lançamento de repasse voltarão para o status em securitização.

#### Processo

Para executar o processo é necessário filtrar e selecionar o contrato de securitização efetivado ir ao menu Processos>>Desfazer Recompras/Devoluções. O sistema ira listar o processos que o contrato selecionado possui, conforme exemplo a seguir:

Após realizar a abertura da visão do processo será possível selecionar o processo desejado(Ou todos o processos) e prosseguir com o cancelamento. Lembrando que será possível prosseguir apenas se o processo(s) selecionados(s) atender aos requisitos de cancelamento.

Alterar conta caixa e convênio |

## **Versão 12.1.32 em Diante !!!**

##### Antes, quando um contrato de securitização encontrava-se efetivado, não era possível realizar o ajuste da conta caixa e do convênio dos lançamentos securitizados.

##### Agora passou a ser possível o ajuste, mesmo o contrato securitizado encontrando-se efetivado.

##### Criado um processo para alterar a conta caixa e convênio na tela de securitização e alterar os lançamentos com status securitizados, que estejam **em aberto** e sem boleto gerado e ou já baixados.

##### Abaixo o processo:

**1: Habilitar o perfil para usar o novo Processo:**

09.01.0.1.16 - Alteração Global Contrato de Securitização

Contrato de Securitização Gerado ( Conta Caixa : Caixa Econômica Federal ).

Lançamentos securitizados com a Conta Caixa.

Contrato securitizado Efetivado.

Selecionar o contrato Securitizado e em seguida: Processos | Alteração Global de Contrato de Securtização

Selecionando nova Conta Caixa : Neste exemplo ( Banco Bradesco ).

Ao marcar opção Nulo - Ocorre a troca apenas da Conta Caixa e convênio fica em branco.

* Ao marcar uma Conta/Caixa e ( NÃO MARCAR ) Nulo , mas não selecionar um Convênio e executar , o processo irá validar se o convênio já existente também faz parte da nova Conta/Caixa .

,

Ao executar o processo , é realizada a troca da Conta/Caixa e Convênio.

Feita a Troca da Conta/Caixa.

Observação!

Relembrando que : Não se tem como alterar dados de lançamentos que se encontram com situação diferente de ( EM ABERTO ) ou diferente de ( NÂO REMETIDO ).

Securitização de AditivosPermitir Aditivar contrato Securitizado.

Ao efetivar o aditivo de renegociação de um contrato que tenha alguma parcela securitizada (paga ou em aberto), as novas parcelas serão incluídas automaticamente na securitização, com o 'status atual" securitizado e as parcelas que foram canceladas serão canceladas do contrato de securitização, ficando com o "status atual" cancelado via aditivo. Caso este aditivo seja desfeito, o sistema irá desfazer as ações acima e as parcelas geradas por este aditivo serão removidas da securitização.

É permitido alterar o vencimento das parcelas quando a securitização for da empresa, desde que não ocorra alteração no valor.

Existe um parâmetro para definir se permiti ou não aditivar os contratos, mantendo o valor da securitização, independente do responsável, desmarcado o parâmetro, o processo será bloqueado para os contratos que estiverem securitizados.

**Efetivando Aditivo de um Contrato ( SECURITIZADO ) PARÂMETRO DESMARCADO!!**

**Efetivando Aditivo de um Contrato ( SECURITIZADO ) PARÂMETRO MARCADO!!**
