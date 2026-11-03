---
content_hash: bce9e51eddf3b7bed67460a35eebeb49694ac5309adb777deef5059aeb2a9eb7
fetched_at: '2026-06-29T00:11:13.149635+00:00'
page_id: '656816895'
product: rm
source: tdn-rm
title: TPC - TOTVS Pagamento com Cartão - Análise de transações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656816895
version: 13
---

Manual do usuário

Ao acessar o módulo **Gestão financeira,** acesse: 

**Movimentações Bancárias > Histórico de Transações.**

Nesta rotina será possível visualizar todas as transações. 

Note, que há diversas colunas trazendo as informações pertinentes ao pagamento e cada linha corresponde a uma tentativa de pagamento realizada pelo usuário. 

Para iniciar o processo de conferência, localize a coluna **Status** e verifique qual o status da transação. 

false

**Pagamento confirmado**: Pagamento foi aprovado pelo cartão de crédito do usuário e houve alguma divergência durante a baixa automática. 

**Pagamento Concluído:** Pagamento foi aprovado e a baixa realizada com sucesso.

**Falha no pagamento com cartão de crédito:** Houve alguma inconsistência na tentativa de pagamento, ou seja, não houve a conclusão da transação e o pagamento continua em aberto.

**Cancelamento pendente:** Houve uma solicitação de cancelamento e o sistema está aguardando retorno da REDE sobre o cancelamento. 

Para entender o comportamento do sistema nas transações e até mesmo validar seu status, basta clicar em:

**Anexos>Histórico de transações.** 

Dessa forma, abrirá uma janela a direita da tela, com as informações pertinentes.

Clicando na linha que deseja analisar, as informações do anexo são atualizadas.

Após o pagamento confirmado e a baixa realizada de forma automática, são criadas no **Extrato de Caixa** duas linhas:

1- corresponde ao valor bruto do lançamento e a

2- referente a previsão de taxa. 

false

*Caso o parâmetro do eduCONNECT PAY esteja direcionado para criar a previsão de taxa no momento da baixa.*

Se necessário conferir os parâmetros, acesse o TDN e selecione a aba:  **Parametrização TOTVS Gestão Financeira**:

<https://tdn.totvs.com/pages/releaseview.action?pageId=572743730#Parametriza%C3%A7%C3%A3o-1283789794>

Falando mais sobre o **Extrato de Caixa,** para analisarmos uma transação específica do histórico de transações, copie o TID e, em seguida, filtre o estrato de caixa por TID.

Veja:

A próxima análise será sobre a conciliação de venda, que acontecerá 24h após a transação ser baixada.

É uma conciliação de transação, ou seja, a confirmação do recebimento do valor pela REDE. 

false

Se houver dúvidas de como realizar a importação do arquivo de conciliação, acesse o TDN e clique na aba:

**Processo de Conciliação - CyberSource** 

<https://tdn.totvs.com/pages/releaseview.action?pageId=572743730#Parametriza%C3%A7%C3%A3o-1781740665>

Após realizada a conciliação, será possível analisar os arquivos recebidos.

Atente-se a coluna **Tipo de Extrato***,* pois será nela que entenderá sobre qual arquivo se trata aquela linha selecionada. 

E para analisar vá em: **Anexos>Operações de venda.**

Além da coluna **Status de Conciliação,** nesta rotina de conciliação, será possível validar a situação da *conciliação de venda* em cada transação realizada, veja como:

Acesse novamente o*histórico de transação* e quando executada a conciliação 24h após a transação, será possível identificar na coluna **Status Conciliação** o preenchimento como *conciliado*. 

Partindo para análise final, 30 dias após a transação realizada e devidamente baixada, a conciliação trará o arquivo de extrato financeiro, onde serão criadas mais duas linhas no extrato de caixa das transações inclusas neste arquivo:

3- Valor líquido depositado na conta transitória 

4- Valor líquido transferido da conta transitória para a conta destino. 

E a transação será *compensada*, bem como, a coluna **Status conciliação do cartão** apresentará a informação: pago, de forma automaticamente.
