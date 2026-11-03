---
content_hash: ffdfbdc74d3f4ff2fcb3f352379e3faa1fe918c4be666524ef49f65e901071b6
fetched_at: '2026-06-29T00:08:11.415849+00:00'
page_id: '242392480'
product: rm
source: tdn-rm
title: DT_Recebimento_com_cartão_no_módulo_de_caixa_TEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242392480
version: 119
---

# RECEBIMENTO COM CARTÃO NO MÓDULO DE CAIXA - TEF

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Sessão de Caixa - Abrir* | *Sessão de Caixa - Abrir* | | *Sessão de Caixa - Ativar* | *Sessão de Caixa - Ativar* | | **Sessão de Caixa - Caixa** | *Sessão de Caixa - Caixa* | |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Requisito (ISSUE):** | PCREQ-10571 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle.* |
| **Tabelas Utilizadas:** | *Informe as tabelas utilizadas.* |

## Descrição

Esta implementação tem como objetivo fazer o recebimento de lançamentos (a receber) com cartão de crédito ou débito no módulo de caixa via TEF, utilizando a solução SiTef da empresa Software Express

## Procedimento para Configuração

1 - No menu Ambiente | Parâmetros | TOTVS Gestão Financeira, acesse na etapa 02.02.05.01 - Módulo de Caixa, a aba TEF para informação dos seguintes parâmetros:

* + Usa TEF - define se habilitará o TEF no módulo de caixa
  + Código da Loja - código da loja no SiTef
  + Endereço IP - endereço ip do servidor do SiTef
  + Porta default PinPad - porta default do PinPad
  + Mensagem Padrao PinPad - mensagem padrão que será escrita o visor do PinPad.
  + Liberar estorno de transações com a senha de supervisor - define se o estorno da baixa realizada via TEF será liberado com senha de supervisor ou usuário autorizado.

2 - No menu Ambiente | Parâmetros | TOTVS Gestão Financeira, acesse na etapa 02.02.02.01 - Manutenção de Baixas, a aba Baixa a Receber para informação dos seguintes parâmetros:

* + Valor mínimo por parcela - define o valor mínimo por parcela ao informar um meio de pagamento com cartão de crédito
  + Número máximo de parcelas - define o número máximo de parcelas ao informar um meio de pagamento com cartão de crédito.

3 - Ao abrir uma sessão de caixa deverão ser configurados os seguintes parâmetros:

* + Habilita TEF - define se a sessão de caixa habilita o pagamento de cartão de crédito ou débito via SiTef. Campo será habilitado caso o "Usa TEF" estiver marcado.
  + Porta PinPad - define a porta onde o PinPad está configurada. Campo será habilitado caso o Habita TEF estiver marcado.
  + Porta Impressora - define a porta onde a impressora está configurada para impressão dos comprovantes do SiTef. Campo será habilitado caso o parâmetro "Saída de Impressão" seja "Porta LPT1".

## Procedimento para Utilização

1 - Sessão de Caixa - Ativar

Ao ativar uma sessão de caixa que esteja configurada para habilitar o TEF será chamada uma função para configuração do SiTef e verificada a existência de um PinPad conectado.

2 - Caixa | Baixa

Na tela de meio de pagamento quando o usuário informar um meio de pagamento com o tipo primitivo "Cartão" e o tipo de transação "Crédito" será apresentado ao usuário uma opção de parcelamento de acordo com o parâmetro de "Número máximo de parcelas" e ao confirmar será validado de acordo com o parâmetro "Valor mínimo por parcela".

Ao clicar no botão "Executar", na tela do processo de Baixa, e tiver sido informado algum meio de pagamento for do tipo primitivo “Cartão” ou "Cartão de Débito" será iniciada uma transação no SiTef.

Caso ocorra algum problema na transação do SiTef será exibida uma mensagem perguntando o operador do caixa se deseja continuar com o processo de baixa normalmente, sendo necessário escolher outro meio de pagamento (diferente de 'Cartão'). Se a transação com o SiTef for concluída com sucesso, a mesma somente será confirmada se no processo de baixa não ocorrer nenhum problema.

**Importante**: A partir do patch 12.1.34.214 o comportamento citado acima foi alterado. Caso ocorra algum erro no processo de baixa do lançamento financeiro, a transação SiTef não será mais cancelada. Neste caso, o pagamento será efetivado junto a operadora e o lançamento financeiro ficará com o campo BAIXAPENDENTE igual a 'Pendente Sitef' até que a ocorrência exibida no log da baixa seja resolvida. Ao corrigir o problema que impediu a baixa do lançamento, será necessário executar o processo "Ajustar Transação", localizado no menu 'Movimentações Bancárias - Histórico de Transações", para que a baixa seja realizada com sucesso e o status da transação relacionada atualize de "Pagamento confirmado" para "Pagamento Concluído". Vale ressaltar que, considerando que o ambiente esteja configurado em N camadas, o processo de ajuste de transação pode ser agendado, evitando a intervenção do usuário para tal.

Os comprovantes do SiTef serão impressos após o processo de baixa, e após a autenticação mecânica caso esteja parametrizado. Caso o parâmetro "Saída de Impressão" seja "Impressora Windows", no momento da impressão dos comprovantes o operador de caixa deverá selecionar a impressora, caso contrário serão impressos na impressora configurada na Porta Impressora definida na sessão de caixa.

Quando a transação e a baixa forem concluídas com sucesso, os dados das transações SiTef serão armazenados no sistema para futura conciliação, na tabela FINTEGRACAOCARTAO e FINTEGRACAOXCX.

**Observação**: No processo de baixa quando tiver alguma transação com SiTef e o parâmetro "Não interromper o processo de baixa, caso algum lançamento apresente inconsistência na baixa" estiver marcado o mesmo deverá ser desconsiderado.

3 - Caixa | Estorno

Ao estornar a baixa de lançamentos realizadas pelo SiTef, caso o parâmetro "Liberar estorno com senha do supervisor" estiver marcado  e a permissão para usuário "Liberar estorno transação SiTef" estiver sem permissão de acesso, será solicitado a senha do usuário supervisor ou usuário com permissão.

Ao clicar no botão "Executar", na tela do processo de Cancelamento de Baixa, será iniciada uma transação de cancelamento com o SiTef onde serão informados os dados necessários gravados pelo sistema no momento da baixa.

Para o cancelamento é solicitado a inserção do cartão no PinPad.

Caso a transação seja realizada com sucesso pelo SiTef e processo de baixa ocorra algum erro, o estorno da baixa deverá ser feita normalmente novamente.

****SITEF via**Terminal Server**

Para possível utilização do SITEF com Terminal Server, é necessário que seja realizado configurações na conexão da Área de Trabalho Remota, compartilhado as configurações dos dispositivos e recursos locais de porta, para que o RM realize a comunicação com o PinPad, em *Recursos locais* no botão *Mais*:

* Como em ambiente local, as dlls do SITEF de comunicação com o PinPad, devem ser inseridas no ambiente do RM no servidor do Terminal Server. O drive do PinPad deve estar instalado no terminal em que está conectado.

**Observação:** Importante que o estabelecimento mantenha uma boa conexão de rede para que não haja perda de comunicação no momento da transação.

divs
