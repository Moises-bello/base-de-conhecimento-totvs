---
content_hash: 80be4fa87ba79d8499ee818dbd8d481c860bffa737d12663772e71381f4b31e4
fetched_at: '2026-06-29T00:08:08.994997+00:00'
page_id: '239018570'
product: rm
source: tdn-rm
title: ER_CPTOP001-12_Melhorias_e_Estabilizacao_da_Integracao_TOP_X_Protheus
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPTOP001-12_Melhorias_e_Estabilizacao_da_Integracao_TOP_X_Protheus
version: 151
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Integração TOP x Protheus |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | CPTOP001 | **IRM1** | CPTOP001-11 |
| **Requisito1** | CPTOP001-12 | **Subtarefa1** | CPTOP001-231 |
| **Chamado2** |  | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colômbia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *Não de aplica* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Especificar as demandas relacionadas a implantação da integração do TOTVS Obras e Projetos com o back-office PROTHEUS.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Configurador da Integração | Alteração | Integração -> Ferramentas-> Configurar | Configurador da Integração TOP X PROTHEUS |
| Conversor | Alteração | Integração -> Ferramentas-> Conversão -> Converter Integração | Conversor de Integração TOP x PROTHEUS |
| Projetos - Sincronismo | Alteração | Construção e Projetos -> Visão de Projetos-> Processos -> Sincronizar Projeto PROTHEUS | Projetos |
| Contratos | Alteração | Construção e Projetos -> Projeto -> Controle -> Básico -> Contrato -> Contratos | Contratos |
| Pedidos | Alteração | Construção e Projetos -> Projeto -> Planejamento-> Básico ->Geração de Pedidos | Pedidos |
| PROTHEUS - Produtos | Envolvida | SIGAEST -> Atualizações -> Cadastros -> Produto | PROTHEUS para RM |
| PROTHEUS - Cliente | Envolvida | SIGAFAT -> Atualizações -> Cadastros -> Cliente | PROTHEUS para RM |
| PROTHEUS - Fornecedores | Envolvida | SIGAFIN -> Atualizações -> Cadastros -> Fornecedor | PROTHEUS para RM |
| PROTHEUS - Nota Fiscal | Envolvida | SIGACOM -> Atualizações -> Movimentos -> Documento de Entrada | PROTHEUS para RM |
| Importação PINI | Alteração | Construção e Projetos -> Projeto -> Utilitários-> Conversão -> Integrar com Base PINI | Integrar com Base PINI |

* **Configurador da Integração TOP X PROTHEUS**

Parâmetro VERSAOPROTHEUS

Criar o parâmetro VERSAOPROTHEUS na tabela HCPARAMETROS. Com este parâmetro contendo o valor 11 (referente ao PROTHEUS 11), ao rodar o configurador algumas mensagens serão mapeadas com a versão diferente da atual. As mensagens e versões mapeadas para compatibilizar com o PROTHEUS 11 são:

|  |  |  |
| --- | --- | --- |
| **Descrição** | **Entidade** | **Versão** |
| Baixa na NF | INVOICE | 3.001 |
| Pedido de Compra | ORDER | 3.002 |
| Solicitação | REQUEST | 1.008 |

Inclusão do Parâmetro: Para integrar com o PROTHEUS 11 deve ser executa o comando SQL abaixo na base de dados:

*INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORSTR) VALUES (0,'VERSAOPROTHEUS','11');*

Tipo de Movimento Contratos

Criar um comando SQL no configurador para alterar os tipos de movimentos dos contratos. Todos os contratos da base de dados têm os valores defaults para geração de movimentos para suprimentos/faturamento alterados para:

|  |  |  |
| --- | --- | --- |
| **Tipo** | **Movimento** | **Movimento Retenção** |
| Pagar | 1.1.04 | 1.2.02 |
| Receber | 2.1.01 | 2.2.03 |

Mensagens Comuns com o TIN

Ao rodar o configurador do TOP, o sistema deve verificar se existe a mensagem mapeada na integração do TIN. Caso exista, não será mapeada na integração do TOP. As mensagens em comuns são:

|  |  |
| --- | --- |
| **Descrição** | **Entidade** |
| Centro de Custo | COSTCENTER |
| Cliente/Fornecedor | CUSTOMERVENDOR |
| Natureza Financeira | FINANCIALNATURE |
| Pedido de Compra | ORDER |

Permissão de Usuários a Movimentos

Criar um procedimento que dá permissão para usuários nos tipos de movimentos. Este procedimento deve ser executado no processo de configuração.

Criar uma TRIGGER que ficará na tabela de cadastro de usuários. Será executada a cada inclusão de usuários e dará permissão para o usuário cadastrado em todos os tipos de movimentos. Esta permissão ocorrerá somente se a integração TOP x PROTHEUS estiver ativa.

Parâmetros por Coligada

Unificar o processo de parametrização por coligada entre as integrações do TOP e do TIN. Ao rodar o configurador os parâmetros por coligada serão os mesmos utilizados nas integrações.

Envio de Obras, Etapas e Tarefas

Criar o parâmetro PRJ\_EXPORTAVALORTRF na integração TOP x PROTHEUS que determinará se os valores referentes a Obra, Etapa e Tarefas, serão enviados ao PROTHEUS.

O parâmetro deve ser desabilitado na inicialização fazendo com que o sistema não envie os valores. Veja o  e .

Este parâmetro deverá ser tratado de forma que contemple todos os pontos de envio dos registros da planilha de atividades.

* **Conversor de Integração TOP x Protheus**

Marcar / Desmarcar Entidades

Criar menu POPUP para marcar/desmarcar todas as entidades. Veja o .

Parâmetro Tamanho do Código da Unidade de Medida

Criar o parâmetro TAMCODUNDPROTHUES para identificar o tamanho da unidade de medida no PROTHEUS. O tamanho default caso não exista o parâmetro é 2(dois). No RM o tamanho é até 5 e no PROTHEUS poderá ser alterado o tamanho do campo na tabela.

Não há necessidade de utilização deste parâmetro quando não existir unidades com o tamanho do código maior que 2 no cadastro do RM.

Inclusão do Parâmetro: O comando SQL para ajustar o tamanho do código é:

*INSERT INTO HCPARAMETROS (CODCOLIGADA, IDINTEGRACAO, PACOTEPADRAO, NOMECOLUNA, TIPOCOLUNA, VALOR) VALUES (0, 1002, 0,'TAMCODUNDPROTHUES','Integer', XXX);* Onde XXX é o tamanho para tratamento do código da unidade de medida.

Uma vez inserido o parâmetro o mesmo ficará disponível no anexo de parâmetros do cadastro da integração.

Conversão de Obras, Etapas e Tarefas

Devem ser enviados para pesquisa somente registro que forem do tipo planilha de atividades e cenário principal. Validar os projetos que são passíveis de envio, projetos em andamento, paralisados, revisados e cancelados não serão enviados.

Para evitar que ocorra um processamento sem controle para o envio de Obra, Etapa e Tarefa, o sistema deverá verificar em cada um dos processamentos se existe um de-para para a empresa e projeto. Caso exista o sistema não deverá enviar a pesquisa para o PROTHEUS. Caso o usuário necessite reprocessar um projeto, será necessário primeiro a exclusão dos de-paras via comando SQL.

Log de Conversão

Ajuste no registro de log do conversor para não exibir erro de duplicidade da chave primária.

Ajuste no conversor de produtos para utilizar no “corpo” da mensagem uma coligada e filial válida.

Ajuste no conversor para processar todos os locais de estoque, exceto 9999999 inserido pelo configurador da integração por mensagem única TOP x PROTHEUS.

* **Projetos**

Sincronizar Projeto PROTHEUS

Para projetos já sincronizados o sistema passa a verificar se a data de alteração esta superior a data de atualização do “DE-PARA”, se sim, a alteração é enviada ao PROTHEUS.

Quando for sincronizado um item da planilha de atividade que não contenha o nome e descrição será enviado como descrição “XXXX sem nome no TOP”, onde XXXX pode ser Obra, Etapa ou Tarefa.

Realizar ajustes nas consultas SQL do processo de sincronismo melhorando a performance.

Parâmetro TROCAFILIALPROTHEUSMU

Criar o parâmetro TROCAFILIALPROTHEUSMU. Este parâmetro foi criado com a finalidade de no caso de algum cliente tiver a tabela de projetos, obras, etapas e tarefas compartilhadas como exclusivo por filial e não for possível alterar, deverá habilitar este parâmetro. Para isto deve estar com o valor 1(UM). Com este parâmetro ativo, ocorrendo uma troca de filial no projeto, o sistema fará a exclusão do projeto e tarefas na filial antiga e inclusão na nova filial. Por isto o ideal é não utilizar o compartilhamento "exclusivo" de projetos e tarefas por filial.

Inclusão do Parâmetro: O comando SQL incluir o parâmetro é:

*INSERT INTO HCPARAMETROS (CODCOLIGADA, NOMECOLUNA, VALORINT) VALUES (0, 'TROCAFILIALPROTHEUSMU', 1);*

Integrar com base PINI

Ao realizar a importação de insumos que não possuem o código na PINI, o sistema não deverá gravar o insumo para o projeto e adicionar o motivo da não gravação no LOG.

A mensagem padrão para o LOG seguirá o seguinte exemplo: "***Insumo** [Escavadeira hidráulica sobre esteiras 162 HP 121 kW, capacidade 1,3 m³] **com unidade** [UN] **não possui código na PINI.***"

* **Contratos**

Gerar Integração com Suprimentos / Faturamento

Atualizar o campo identificador de integração dos movimentos gerados com o “DE-PARA” retornado pelo PROTHEUS.

Retirar o envio de projeto e tarefa para retenções de contratos a receber de serviços.

Alterar o configurador para adicionar um valor default para os parâmetros discriminar retenção e enviar retenção como desconto. Os comandos adicionados no configurador são:

UPDATE MPARAMETRO SET VALORINT = 0 WHERE CODCOLIGADA = 1 AND IDPRJ = 9 AND PARAMETRO = 'DISCRIMINARVALORETENCAODEDUCAO'

UPDATE MPARAMETRO SET VALORINT = 1 WHERE CODCOLIGADA = 1 AND IDPRJ = 9 AND PARAMETRO = 'ENVIARRETENCAODESCONTO'

Nos casos em que a data de vencimento calculada for inferior a data de hoje, o sistema passa a assumir a data corrente do servidor.

No envio de retenção o sistema passa a não enviar para o PROTHEUS, rateios que ficarem com valor zerado no título de provisão da retenção.

Parâmetro de Projeto Permite Alterar Filial

Criar o parâmetro “Parâmetro de Projeto Permite Alterar Filial” e se marcado, será possível alterar a filial e local de estoque default no contrato e no momento de gerar a integração com suprimentos / faturamento.

Contratos de Insumo

Ajuste na pesquisa da associação de objetos no contrato para considerar o número do aditivo ao validar o parâmetro de projeto que permite associar acima de 100%.

* **Pedidos**

Geração de Pedidos

Atualizar o campo identificador de integração dos movimentos gerados com o “DE-PARA” retornado pelo PROTHEUS.

Parâmetro MAXITEMGERPEDPROTHEUS

Criar o parâmetro MAXITEMGERPEDPROTHEUS. Este parâmetro tem por finalidade ajustar o tamanho da mensagem quando o ambiente do PROTHEUS não suportar o trafego de mensagem muito extensas (tamanho em bytes) por possuírem muitos itens.

Determina a quantidade máxima de itens que serão processados para gerar o pedido / solicitação. Será considerado se maior que 0(zero).

O comando SQL de inclusão do parâmetro é:

*INSERT INTO HCPARAMETROS (CODCOLIGADA, IDINTEGRACAO, PACOTEPADRAO, NOMECOLUNA, TIPOCOLUNA, VALOR) VALUES (0, 1002, 0,'MAXITEMGERPEDPROTHEUS','Integer', XXX);* XXX é a quantidade de itens a enviar por mensagem.

Uma vez inserido o parâmetro o mesmo ficará disponível no anexo de parâmetros do cadastro da integração.

Geração de Pedidos Extras

Quando integrado com o PROTHEUS, o sistema não permitirá o envio itens relacionados a obras e etapas. Sendo enviado somente tarefas de último nível.

A consistência será realizada no momento que o usuário clicar em gravar/salvar o item. Veja o .

Quanto integrado com o PROTHEUS o parâmetro "Exibe obras e etapas para pedido extra" localizado nos parâmetros de   
projetos em "Integração | Suprimentos / Faturamento | Geral" deverá ser desmarcado e desabilitado.

Atualizar o campo identificador de integração dos movimentos gerados com o “DE-PARA” retornado pelo PROTHEUS.

* **PROTHEUS para o RM**

Produto

Ajustar o código fonte da mensagem ITEM da integração TOP x PROTHEUS para verificar se existe o DE-PARA de filial e caso não exista apresentar uma mensagem intuitiva ao usuário.

Cliente e Fornecedores

Ajuste para truncar o número do endereço do cliente e fornecedor compatibilizando com o tamanho 8 do RM.

Nota Fiscal - Documento de Entrada no PROTHEUS

Ajustado a forma de identificar a coligada do produto no recebimento da nota fiscal no RM.

Atualização de Saldos

Ajuste para não considerar projeto 0(zero) se integrado por mensagem única e seja tipo de movimento (4.1.04) de atualização de custos. A atualização de custos ocorre em vários processos de movimentação de estoque do PROTHEUS. Um exemplo é uma nota fiscal relacionado a um pedido de material onde o tipo de entrada e saída (TES) movimenta o estoque. Neste caso irá enviar do custo no momento de registro da nota de entrada.

***Tabelas Utilizadas***

* *Não se aplica*

## Protótipo de Tela

**Protótipo 01 - Conversor de Integração - Step de Escolha de Entidades**

****Protótipo 02 - Parâmetros da Integração TOP x PROTHEUS****

******Protótipo 03 - Item do Pedido Extra******

************Protótipo 04 - XML envio Obra************

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
