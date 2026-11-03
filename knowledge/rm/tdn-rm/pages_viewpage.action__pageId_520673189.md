---
content_hash: 83bf7fc30e4cdbf2846a5c56015927a8bfed0191670f2223cac77bd6f59366e2
fetched_at: '2026-06-29T00:10:31.181779+00:00'
page_id: '520673189'
product: rm
source: tdn-rm
title: backup securitização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520673189
version: 1
---

**SECURITIZAÇÃO**

Securitização - Venda e AluguelContrato Securitização - VendaContrato Securitização - Venda |Contrato Securitização - Venda

Gerando contrato de Securitização - Venda

Liberar o Perfil do Usuário para Utilizar a Securitização []

Securitização | Contrato de Securitização – Venda

Novo contrato de Securitização

Criando novo contrato de Securitização

Inserir o Cliente da Securitizadora.

Selecionando o Contrato que será feita a Securitização  -  Avançar

Selecionar as Parcelas do Contrato que serão securitizadas

Selecionada neste exemplo = 8 Parcelas

Clicar em : Calcular Valor Securitizado

Valor das 8 Parcelas = R$22.687,31

**Executar**

Processada

Lançamentos incluídos no Contrato Securitizado

Inerir o Valor de Antecipação

Inserir a Data de Vencimento do Título Securitizado

**Processo | Efetivar Contrato**

Processado

Lançamento Gerado

Contrato Securitização - AluguelContrato Securitização - Aluguel |Contrato Securitização - Aluguel

**Contrato se Securitização Aluguel**

Contrato de Locação

Contrato de Securitização - Aluguel

Criando o Contrato

Processo | Inclusão de Lançamento no Contrato de Securitização

Selecionar o Contrato

**Avançar**

Parcelas do Contrato do Aluguel selecionadas - Calcular Valor Securitizado

Sistema mostra o valor das Parcelas selecionadas e em seguida - **Executar.**

Processado

Efetivando contrato Securitizado

Parcela criada .

SecuritizaçãoSecuritização |Securitização

Será possível atualizar o Status do Contrato de Securitização para contrato **Efetivado** e **Em Aberto**(Voltar Situação).

Importante:

* Antes de efetivar o contrato é necessário preencher as informações para a geração do lançamento de securitização.
* Para voltar a situação do contrato ele precisa estar efetivado.
* Será possível voltar a situação do contrato apenas se o lançamento estiver em aberto.
* Caso o lançamento possua algum bloqueio ou restrição que impossibilite o seu cancelamento, será necessário ajustar a mesma antes de voltar a situação do contrato.
* É possível remover os lançamentos do contratos de Securitização antes de efetivar o contrato.

Para execução do processo, é necessário filtrar o contrato de securitização.Acesse a aba **Recebíveis**, em seguida o menu **Securitização.** Dentre as opções disponíveis será possível filtrar os contratos de Securitização de **Venda** ou **Aluguel**. Apos selecionar o contrato desejado, é necessário acessar o Menu Processos e selecionar a ação que deseja realizar **Efetivar** ou **Voltar** Situação do Contrato.

Apuração Mensal de Lançamentos Em AtrasoApuração Mensal de Lançamentos Em Atraso |

Através do processo de apuração mensal, a empresa identificará o que foi não foi pago pelos clientes e que precisa ser pago à securitizadora. Serão apresentados os lançamentos em atraso do contrato de securitização que ainda não foram baixados no sistema.

Importante

* Somente os lançamentos que forem selecionados na execução do processo serão recomprados.
* Os Lançamentos que já se encontram baixados não serão considerados.
* Para realizar o processo de recompra o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.10] Apuração Mensal Lançamentos Em Atraso**
* Para consultar os lançamentos de repasse o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.12] Lançamentos de Repasse**

O processo se encontra na visão do Contrato de Securitização. Desta forma é necessário ir a aba **Recebíveis**>>Securitização>>Contrato de Securitização - Venda.

Para execução do processo deve ser selecionado o contrato de securitização ir ao menu Processos>>Apuração Mensal Lançamentos Em Atraso.

Neste processo apenas os lançamentos selecionados serão recomprados, desta forma é necessário selecionar o registros desejados e informar a '**Data de Pagamento**' em seguida clicar na opção '**Calcular Valor Securitizado**' e  confirmar a execução do processo. Ao termino do processo os lançamento selecionados serão retirados do contrato de securitização e será criado um lançamento de Repasse para a securitizadora. Para visualizar o lançamento criado é necessário editar o contrato de securitização e ir na pasta '**Lançamentos de Repasse**'

Recompra de Lançamentos SecuritizadosRecompra de Lançamentos Securitizados |

Através do processo de recompra de lançamentos securitizados do cliente, a empresa identificará os clientes que tem dívidas superiores a um determinado prazo e irá recomprar os lançamentos desses clientes. É necessário informa um prazo para a verificação dos lançamentos e devem ser apresentados todos clientes (por contrato de securitização) que possuem lançamentos com vencimento superior ao prazo informado.

Para definir o prazo é necessário acessar os parâmetros do sistema, através da aba Ambiente>>Parâmetros>>Totvs Incorporação>>Integração Financeira>>Financeiro. Nesta etapa deve ser preenchido no parâmetro '**Período limite para recompra de lançamentos securitizados vencidos(Nro Meses):**'.

Importante

* O sistema irá consistir o contrato de securitização levando em consideração o período definido no parâmetro **"Período limite para recompra de lançamentos securitizados vencidos(Nro Meses):"**e caso um lançamento do cliente atenda os requisitos de vencimento todos os demais lançamentos serão retornados no processo.
* Neste processo deve ser selecionado todos os lançamentos para recompra
* Os Lançamentos que já se encontram baixados não serão considerados.
* Para realizar o processo de recompra o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.11] Recompra de Lançamentos Securitizados**
* Para consultar os lançamentos de repasse o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.12] Lançamentos de Repasse**

Apos definição do período será possível realizar a recompra. O processo se encontra na visão do Contrato de Securitização. Desta forma é necessário ir a aba **Recebíveis**>>Securitização>>Contrato de Securitização - Venda.

Para execução do processo deve ser selecionado o contrato de securitização ir ao menu Processos>>Recompra de Lançamentos Securitizados. Neste momento o sistema irá consistir se algum lançamento associado ao contrato de securitização selecionado se enquadra no período definido e retorna todos os lançamentos do cliente.

Neste processo todos os lançamentos serão recomprados, desta forma é necessário selecionar todos o registros e informar a '**Data de Pagamento**' em seguida clicar na opção '**Calcular Valor Securitizado**' e  confirmar a execução do processo. Ao termino do processo os lançamento selecionados serão retirados do contrato de securitização e será criado um lançamento de Repasse para a securitizadora. Para visualizar o lançamento criado é necessário editar o contrato de securitização e ir na pasta '**Lançamentos de Repasse**'

Troca de Conta Caixa ao Efetivar Contrato Securitização |

Ao efetivar o contrato de securitização, os lançamentos financeiros marcado como securitizados, passam a ter a conta caixa modificada pela conta caixa informado no contrato de securitização.

Para o contrato de securitização:

* O campo de conta caixa no contrato de securitização é obrigatório o seu preenchimento.

Recebíveis | Securitização | Contrato de Securitização – Venda

Contrato de Securitização

Contrato de Securitização com Conta Caixa : Caixa Economica Federal

Contrato selecionado

Parcelas selecionadas .. Calcular Valor Securitizado

Executar

Lançamentos do contrato,  enviados para = Lançamentos Securitizados.

Efetivando contrato securitizado.

Conta caixa selecionada no contrato Securitizado tem que ir para os lançamentos após efetivação do mesmo.

Lançamentos Securitizados

Nos lançamentos Securitizados , Alterada a Conta Caixa para o da Conta Caixa do contrato da Securitização.

ContabilizaçãoContabilização |

É possível realizar a contabilização do contrato de securitização através do processo '**Contabilizar/Estornar Securitização**'.

Importante

* Para realizar o processo de contabilização o perfil vinculado ao usuário deve ter permissão a TAG**[08.01.01.13] Contabilização do Contrato de Securitização**
* É necessário criar um Evento Contábil com o processo **Securitização**.

Durante o cadastro de um novo contrato de securitização ou edição de um contrato já salvo na base de dados será possível acessar a aba **Contabilidade**, onde deve ser informado o Evento Contábil que será utilizado para a criação da contabilização. Apos informar o Evento e salvar o contrato é necessário ir ao menu Processos>>Contabilizar/Estornar Securitização.

Deve ser selecionado o Tipo de Processo e a Data de Contabilização/Estorno e confirmar a operação.

Tipo de Processo

* Contabilizar - Criar a contabilização respeitando o Evento Contábil informado no contrato.
* Estornar - Realizar o estorno da operação contábil.
* Recontabilizar(Estornar e Contabilizar) Refaz a contabilização do contrato de securitização.
