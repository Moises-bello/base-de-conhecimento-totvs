---
content_hash: e60859c7e546cfc344ebbdcdb09ff1d85ab187661351f581c384300b73580878
fetched_at: '2026-06-29T00:11:37.363071+00:00'
page_id: '776535847'
product: rm
source: tdn-rm
title: Orçamento para Clientes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=776535847
version: 19
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Incluindo um Orçamento**
3. **Incluindo Item de Kit de Lançamento**
4. **Associando um orçamento no Registro do Atendimento**
5. **Desconto para Orçamento**
6. **Configuração do Movimento de Orçamento**
7. **Realizando o Movimento de Orçamento**
8. **Parametrização do Orçamento**

sumarioVisão Geral

## **01. VISÃO GERAL**

Est rotina é utilizada para gerar um orçamento para o paciente, indicando os valores estimados associados à realização de um determinado procedimento. O orçamento pode incluir despesas como diárias, materiais, medicamentos, procedimentos, taxas, entre outros.

Incluindo um Orçamento

## **02. INCLUINDO UM ORÇAMENTO**

Dica

Disponibilizamos uma rotina de **cópia de orçamento**, ideal para situações em que o orçamento expirou ou quando é necessário reaproveitar um orçamento para outro paciente ou prestador.

Durante o processo de cópia, caso existam novas tabelas vigentes, os valores do orçamento serão automaticamente atualizados com base nas tabelas mais recentes.

A rotina de **Orçamento para Clientes** está acessível no menu: **Faturamento > Particular e Convênios > Orçamento para Clientes.**

Na primeira aba, é necessário preencher os campos exibidos na tela, como informações do paciente, convênio, entre outros.

Em seguida, na próxima aba, devem ser adicionados os itens que compõem o orçamento, como honorários, exames, diárias, entre outros.

Os valores do orçamento serão calculados com base nos valores do convênio e do plano informados na primeira aba do orçamento.

Além disso, quando o exame possuir apenas um item de débito, este será preenchido automaticamente pelo sistema.

falseRelease 12.1.2602

A rotina de **Orçamento para Clientes** pode ser acessada no menu:   
**Faturamento > Particular e Convênios > Orçamento para Clientes**.

Na aba **Orçamento** é necessário preencher os campos exibidos na tela, incluindo informações do paciente, convênio, entre outros dados relevantes.

Na parte inferior da tela, devem ser adicionados os itens que compõem o orçamento, como:

* Materiais
* Medicamentos
* Diárias
* Exames
* Honorários
* Entre outros.

Os valores dos itens do orçamento serão calculados automaticamente com base nos valores do convênio e do plano informados, conforme preenchido no orçamento.

 (Cálculo automático do Valor Unitário)

(Alteração do Valor Total com base na quantidade)

Na Aba de **Observação** possui um campo descritivo para preenchimento do usuário.

Incluindo Item de Kit de Lançamentos

## **03. INCLUINDO ITEM DE KIT DE LANÇAMENTOS**

Neste processo é possível incluir itens cadastrado no Kit de Lançamentos. O Cadastro de Kits de Lançamentos encontra-se no menu **Cadastro / Outros Cadastros / Kits de Lançamentos** . Após o cadastros dos itens no Kit, estes itens estarão disponíveis para serem lançados no orçamento.

1 - Acesso através de Processos / Inserir Itens Kit Lançamentos

2 - Neste processo é possível inserir itens de um ou múltiplos kits simultaneamente.

3 - Após a execução do processo, os itens cadastrados no kit serão inseridos na aba de Itens do orçamento.

Os valores dos itens são oriundos das tabelas de preços, conforme vigência do contrato na data do orçamento.

Associando um orçamento no Registro do Atendimento

## **04. ASSOCIANDO UM ORÇAMENTO NO REGISTRO DO ATENDIMENTO**

É possível carregar todos os itens de um orçamento ao abrir o Registro de Atendimento do paciente. Para isso, acesse a tela de Registro de Atendimento, preencha os dados solicitados, como em um atendimento convencional, e salve o registro.

Ao salvar, o sistema verificará a existência de um orçamento associado ao paciente e perguntará se deseja vinculá-lo ao atendimento.

Se houver mais de um orçamento disponível, será exibida uma tela para que o usuário selecione o orçamento que deverá ser associado.

Caso já existam itens de débito registrados na Parcial do Paciente, o sistema apresentará uma tela para selecionar os itens do orçamento a serem associados.

Caso essa etapa não seja concluída, um novo registro será gerado na Parcial.

Os itens do orçamento serão automaticamente alocados em suas respectivas abas de grupos de gastos, conforme a configuração da faixa de codificação.

Desconto para Orçamento

## **05.** **DESCONTO PARA ORÇAMENTO**

A rotina **"Desconto para Orçamento"** foi desenvolvida para aplicar descontos diretamente no orçamento, com a possibilidade de associá-los posteriormente durante o registro de atendimento.

Existem duas modalidades de aplicação do desconto:

* + **Por Item do Orçamento**: O desconto é lançado individualmente para cada item, gerando um registro com o código do item e valor negativo na conta do paciente.

Importante!

No grupo de gasto específico, é lançado um valor negativo, representando o desconto sobre um lançamento já existente.

Na guia **Lançamento Especial**, o sistema só aceitará o **Tipo de Lançamento = Desconto** se o código do procedimento já estiver registrado na aba **Elaboração** e coincidir com o mesmo centro de custo e prestador.

Caso essas condições não sejam atendidas, será exibida uma mensagem de erro.

Além disso, o lançamento que receberá o desconto não pode possuir repasse.

* + **Sobre o Valor Total do Orçamento**: O desconto é aplicado através da inclusão de um registro 99.99.9999 com o valor total do desconto.

Importante!

Ao associar um orçamento com desconto sobre o valor total a um atendimento, o desconto não é aplicado automaticamente nas parciais. Nesse caso, é necessário inseri-lo manualmente por meio do **Lançamento Especial**, disponível na tela de **Elaboração de Contas**, conforme detalhado na documentação .

Na tela de **Orçamento para Clientes**, selecione o orçamento desejado, clique em **Processos** e, em seguida, escolha a opção **"Desconto para Orçamento"**.

O desconto atribuído será aplicado à conta do paciente durante a utilização do orçamento no **Registro de Atendimento** (conforme descrito no **ITEM 03 desta documentação**), por meio da associação do orçamento ao atendimento.

Configuração do Movimento de Orçamento

## **06.** **CONFIGURAÇÃO DO MOVIMENTO DE ORÇAMENTO**

Antes de executar o movimento do orçamento, é necessário realizar a configuração descrita abaixo para garantir o funcionamento da integração entre o movimento do orçamento e o Backoffice.

Atenção!

Os dados apresentados neste manual são fictícios e possuem caráter ilustrativo. Não os utilize como dados reais. Consulte o seu ambiente de trabalho para obter as informações corretas e aplicáveis.

Na tela de **Parâmetros do Backoffice**, insira o código do movimento que será utilizado pela rotina de orçamento.

No **RM nova MDI**, verifique se a parametrização está correta, conforme demonstrado nas imagens a seguir.

|  |  |
| --- | --- |
|  |  |
|  |  |
|  |  |

Realizando o Movimento de Orçamento

## **07.** **REALIZANDO O MOVIMENTO DO ORÇAMENTO**

A rotina de gerar um Movimento de Orçamento é acessada através da tela de Orçamento para Clientes, siga as etapas abaixo para gerar o movimento.

* + Na tela de **Orçamento para Clientes** selecione o Orçamento, clique em **Processos**e depois clique na opção "**Movimento de Orçamento**".
  + Selecione o "**Tipo de Movimento**" e confirme a operação.
  + Aguarde o processamento...
  + Para conferir o resultado, após a conclusão vá até a aba **Vendas / Pedido de Venda**.

|  |  |
| --- | --- |
|  |  |
| --- | --- |
|  |  |
|  |  |

Parametrização do Orçamento

## **08.** **PARÂMETROS DO ORÇAMENTO**

Nos **parâmetros gerais do sistema**, é possível configurar se os itens do orçamento serão lançados na aba de **Gastos Particulares**. Esse parâmetro aplica-se apenas a convênios do tipo **Privado**.

Para convênios classificados como **Particular**, todos os gastos são automaticamente incluídos nas respectivas abas, conforme o grupo de gasto correspondente.
