---
content_hash: d2e5ea8e34e007d5c673d44c821744d6310aab247999b2ce9dbc46f24d1ec06a
fetched_at: '2026-06-29T00:08:21.697617+00:00'
page_id: '269069034'
product: rm
source: tdn-rm
title: DT_Melhorias_Boleto_Remessa_RegistoOnline
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Melhorias_Boleto_Remessa_RegistoOnline
version: 117
---

# COBRANÇA REGISTRADA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Financeira* |
| **Função:** | *Geração de Boleto, Remessa e Retorno Bancário, Registro Online de boletos no portal* |
| **Requisito (ISSUE):** | *EDUCTB002-112* |

**Descrição**

Esta implementação tem como objetivo preparar o TOTVS Gestão Financeira facilitar os processos de geração de boleto, remessa e retorno bancários além do registro online de boletos.

**Procedimento para Configuração**

1 - No Totvs Gestão Financeira, menu *Movimentações Bancárias | Controle Bancário | Convênio,* devem ser feitas as configurações do convênio para geração de boleto, esses valores são opcionais e quando informados são carregados no processo de inclusão do mesmo.

Outra opção nessa aba é o relatório default para impressão do boleto, quando informado será carregado automaticamente no processo realizado na visão do boleto. Nesse processo há uma trava para só executar caso o boleto seja de um convênio com tipo de cobrança "Registrada" esteja com o Status CNAB valorado como "Registrado".

*Figura 1- Configurações para defaults de boleto e impressão*

Na aba Remessa Bancária estão disponíveis configurações para facilitar a remessa bancária. Para cada um dos três processos (cobrança, débito automático e pagamento) é possível informar a composição do nome e extensão do arquivo de remessa, e o diretório destino onde ele será salvo.

*Figura 2- Configurações para remessa bancária*

2 - No Totvs Gestão Financeira, menu *Ambiente | Parâmetros | Gestão Financeira* acesse Contas a Receber | Integração Bancária | Cobrança Eletrônica (02.02.04.01) e no campo "Convênio Default para Registro Online de Boleto" informe o convênio usada no registro dos boletos nos portais Educacional e Processo Seletivo. Somente convênios com o flag "Permite registro de boleto online" marcado serão exibidos.

*Figura 3- Configurações para registro de boleto em portal*

No menu **Movimentações Bancárias | Controle Bancário | Convênio**devem ser feitas as configurações do convênio para registro do boleto, marcando o flag que permite o registro e informando as URLs dos serviços de registro e retorno do banco relacionado.

**Figura 4- Configurações de convênio para registro de boleto**

3 - No Totvs Educacional, menu *Ambiente | Parâmetros | Educacional,* acesse *RM Portal | RM Portal - Gerais (15.04.01)* e na aba Portal - Geral (8/8) defina quais serviços irão permitir o registro de boleto online no portal. Marcando a opção "Apresentar boleto de cobrança registrada ainda não registrado no Portal" todos os boletos, registrados ou não, serão exibidos e não estará disponível o registro online. Se não marcado, caso exista boleto registrado o mesmo será exibido como a segunda via, se não existe, o boleto precisará passar pelo processo de registro.

**Figura 5- Configurações para registro de boleto no portal**

**Procedimento para utilização**

1 - No menu *Contas a Pagar/Receber | Operações Financeiras | Lançamentos | Processos | Boleto | Inclusão de Boleto* foi criada opção para informar Conta Caixa e Convênio para geração do boleto diferentes do valor informado no lançamento. Caso opte por usar os existentes no lançamento marque a opção "Utilizar conta e convênio do lançamento". As informações no lançamento passam a ser apenas default para a geração de boletos, ou seja, não é necessário que o boleto possua o mesmo convênio do lançamento. Os defaults para CNAB, caso informados no Convênio, serão carregados.

*Figura 6 - Opções de conta caixa e convênio, defaults na inclusão de boleto*

2 - No menu *Contas a Pagar/Receber | Operações Financeiras | Boleto| Processos | Remessa* serão carregadas na tela, quando parametrizado no Convênio, as informações do diretório destino e arquivo criado pelo processo.

*Figura 7 - Carregamento de diretório destino remessa bancária*

3 - No Portal Educacional menu *Financeiro | Extrato Financeiro*para os boletos que permitem registro online, de acordo com os itens 2 e 3 de parametrização indicados acima, ao clicar no botão para emissão do boleto será exibida uma tela redirecionando para o serviço do banco que irá realizar o registro.

divs
