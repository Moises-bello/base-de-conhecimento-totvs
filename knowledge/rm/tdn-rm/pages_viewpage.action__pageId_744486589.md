---
content_hash: 3bfa11e2622b06b82a0d07d01c8d51ce1bb0c682a00c73f828dad50077f7d498
fetched_at: '2026-06-29T00:11:32.115350+00:00'
page_id: '744486589'
product: rm
source: tdn-rm
title: Configurações iniciais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=744486589
version: 57
---

Antes de começar a usar o módulo de caixa é importante definir algumas configurações iniciais que vão ajudar no uso do dia a dia dos recursos disponíveis.

Configure de acordo com a realidade da sua empresa, e altere quando achar necessário.

Menu: *Ambiente | Parâmetros | Gestão Financeira | Contas a Receber | Caixa | Módulo de Caixa.*

## *Etapa 1 - Gerais*

### Gerais

**Saída de Impressão** - Informe a impressora que será utilizada nas impressões realizadas na sessão, autenticação mecânica, recibos, comprovante TEF.

**Porta Impressora default** - Define qual a porta da impressora será carregada por default ao abrir uma nova sessão de caixa.

**Utiliza impressora padrão** - Se na saída de impressão for definido "Impressora Windows", esta opção define que será considerada a impressora padrão configurada no computador.

**Exibe a tela para edição de vínculos na baixa** - Durante a baixa do lançamento será apresentada a tela para vínculos.

Restrição

No Módulo de Caixa 2.0, focamos no registro do recebimento e na simplicidade. As telas foram simplificadas e não é possível realizar vínculo.

A sessão agora sendo aberta como aba, o vínculo pode ser realizado pela visão de lançamentos.

**Forma de rateio dos valores na baixa** - Define como os valores serão rateados ao realizar a baixa.

**Sangria e Suprimento**

* **Tipo Contábil** - Define o tipo contábil do extrato que será gerado ao incluir a sangria e suprimento de caixa.

### Permissões da abertura da Sessão de Caixa

Os parâmetros abaixo definem as configurações da abertura da sessão de caixa para todas as sessões que serão abertas para a coligada.

**Operação** - Define qual a natureza dos lançamentos que os caixas irão operar, dentre: recebimentos, pagamentos ou ambos.

**Emite relatório de encerramento do caixa**- Ao marcar esta opção, ao realizar o encerramento, o relatório de encerramento da sessão de caixa será emitido.

**Estorna Lançamento Baixado em outra Sessão**- Ao marcar esta opção será possível estornar lançamentos baixados em outra sessão de caixa.

Observações

Lançamentos que **não**foram baixados via módulo de caixa, poderão ser estornados independente desta opção estar marcada ou não.

O operador do caixa poderá estornar lançamentos baixados de outra sessão, independente do usuário que realizou a baixa.

**Habilita TEF** - Ao marcar esta opção ficará disponível nas sessões a opção de receber usando os meios de pagamento de cartão, conectado com a máquina TEF.

**Habilita PIX** - Ao marcar esta opção, utilizando um meio de pagamento de PIX, será gerado e exibido o QRCode.

Preferências de Usuário

A partir da liberação da versão 12.1.2402 na Abertura de Sessão através da nova tela, não será considerado o item *Fluxo de Caixa | Salvar os parâmetros utilizados* que está disponível nas *Preferências do Usuário*, o sistema passa a considerar os dados gravados nos parâmetros *"Permissões de abertura da sessão de caixa"* como padrão para carregamento dos campos existentes no grupo "*Permissão*" na criação de uma nova sessão. Para mais detalhes da nova tela [acesse esse link](https://tdn.totvs.com/pages/viewpage.action?pageId=781205618).

### Permissões do operador

Os parâmetros abaixo definem quais as permissões o operador terá ao operar uma sessão de caixa.

**Permite alterar as permissões na abertura da sessão** - Ao marcar esta opção, todas as permissões desta sessão (Permissões da abertura da Sessão de Caixa) e a Porta Impressora default ficarão disponíveis para alteração do usuário ao abrir uma nova sessão de caixa.

Quando essa opção estiver marcada, todas as permissões de abertura da sessão parametrizadas serão carregadas por default ao abrir uma nova sessão.

**Permite encerrar sessão** - Com esta opção marcada, o usuário operador do caixa poderá encerrar a sua sessão, caso contrário somente o operador supervisor poderá realizar o encerramento.

Observações

Existem três formas de realizar o encerramento da sessão, é importante que os gestores analisem e definam as permissões de acesso corretas a este recurso. [Saiba mais](https://tdn.totvs.com/pages/viewpage.action?pageId=781216399)

**Permite consultar os saldos** - Ao marcar esta opção, o operador de caixa poderá consultar os saldos atuais da sessão de caixa.

---

## *Etapa 2 - Autenticação Mecânica*

**Usa Autenticação Mecânica** - Ao marcar esta opção, após a conclusão do recebimento, é apresentada a possibilidade de realizar autenticação mecânica.

**Permite não imprimir autenticação** - Ao marcar esta opção, a autenticação passa a ser opcional.

**Permite reimprimir autenticação** -  Ao marcar esta opção será possível reimprimir a autenticação mecânica no caixa.

Restrição

No Módulo de Caixa 2.0, uma vez definido o uso da autenticação mecânica, sempre será possível realizar a reimpressão ou optar por não realizar. Desta forma as parametrizações acima não são consideradas, e em breve serão descontinuadas.

**Obrigatória a impressão de abertura do caixa** - Ao marcar esta opção a autenticação na abertura da sessão de caixa será obrigatória, não será possível fazer nenhuma movimentação na sessão sem que a mesma seja executada.

Restrição

No estudo para a construção do Módulo de Caixa 2.0, identificamos que este parâmetro não é utilizado por nossos clientes, desta forma o mesmo não está sendo considerado e em breve será descontinuado.

**Permite imprimir autenticação mecânica após impressão do relatório/recibo** - Ao marcar este parâmetro, a ordem de impressão da autenticação e do recibo são alteradas.

Restrição

No Módulo de Caixa 2.0, a opção de imprimir a autenticação mecânica e o recibo são apresentadas no mesmo momento. Desta forma este parametrização não é considerada, e em breve será descontinuada.

---

## Etapa 3 - Configuração Layout

Nesta etapa é possível definir quais as informações que serão impressas na autenticação de abertura, baixa e estorno, sua posição, o formato e o tamanho em caracteres.

---

## Etapa 4 - Numero Autenticações

Nesta etapa é preciso selecionar onde será impresso a autenticação do caixa, se em documento ou em bobina.

---

## Etapa 5 - Relatórios do Caixa

Nesta etapa são definidos os relatórios usados nas impressões realizadas na sessão. **OBS:** Somente relatórios RM Reports são permitidos.

**Balanço de Sessão de Caixa** - Relatório utilizado para emissão do encerramento da sessão de caixa.

**Usa Recibo** - Ao marcar esta opção, após a conclusão do recebimento, é apresentada a possibilidade de realizar impressão de recibo.

---

## Etapas 6 e 7 - TEF e TEF Filial

Nesta etapa são realizadas as parametrizações da integração do SiTef com o PinPad, essas configurações são utilizadas durante os pagamentos com cartões de Crédito e Débito através da Sessão de Caixa.

É possível definir uma parametrização global, ou específica por filial.

**TEF na sessão de Caixa** - permite definir se *Usa*, *Não Usa* ou *Uso Obrigatório* do TEF:

* *Usa* - Define se o TEF será habilitado no módulo de caixa, ao configurar essa opção o usuário poderá definir na abertura da sessão de caixa, se a opção "Habilita TEF" será usada ou não, marcando ou desmarcando a opção.
* *Não Usa* - Define que o TEF não será usado na sessão de caixa e ao abrir uma nova sessão de caixa a opção "Habilita TEF" será apresentada desmarcada e o sistema não permitirá alteração.
* *Uso Obrigatório* - Define que o uso do TEF será obrigatório, a opção "Habilita TEF", na abertura da sessão será apresentada marcada e não permitirá que o usuário altere a configuração definida nos parâmetros do sistema.

**Modelo TEF** - Definição do modelo de integração para recebimento via TEF.

Restrição

A integração Adyen foi descontinuada e em em breve será retirada do sistema.

**Informações SiTEF** - Informações técnicas específicas de configuração e comunicação do modelo em questão

**SiTef**

* *Código da Loja* - Este código é de controle do estabelecimento definido junto a operadora do SiTef na instalação do PinPad.
* *Endereço IP* - Define o endereço IP do servidor SiTef.

**PinPad**

* *Porta default* - Define a porta default de comunicação do PinPad.
* *Mensagem Padrão* - Define uma mensagem padrão no visor do PinPad.

**Liberar estorno de transações com a senha de supervisor** - define se o estorno de uma baixa que foi realizada no SiTef será liberado com a senha de um usuário do RM que seja supervisor.

**Imprime comprovante TEF** - Ao marcar esta opção, após a conclusão do recebimento, é apresentada a possibilidade de realizar impressão do comprovante TEF, podendo escolher entre as vias Logista, Portador e Ambas.

## *Etapa 8 - Meios de Pagamento*

Essa etapa tem por objetivo permitir a realização de configurações referentes aos Meios de Pagamento que estarão disponíveis para uso no Módulo de Caixa 2.0.

O recurso visa permitir ao usuário definir quais são os meios de pagamento que serão exibidos no Módulo de Caixa 2.0 e para cada um deles realizar a configuração da Conta/Caixa desse pagamento, bem como a forma de compensação dos extratos gerados por esse meio de pagamento.

A partir do momento em que se opta por utilizar as configurações de Meios de Pagamento, somente os itens incluídos nesse parâmetro serão exibidos na lista da tela de Recebimento via Módulo de Caixa 2.0, os itens que não forem inclusos na parametrização deixarão de ser considerados como opção para uso.

Em cada cadastro teremos:

**Meio de Pagamento** - Meio de pagamento cadastrado que será disponibilizado no Módulo de Caixa 2.0.

**Conta/Caixa** - Caso deseje informar uma conta/caixa diferente da configurada na abertura da sessão do caixa para registro das baixas, informe uma Conta/Caixa específica que passará a ser utilizada nas baixas por esse Meio de Pagamento quando elas forem realizadas através do Módulo de Caixa 2.0. Caso não seja informada uma Conta/Caixa específica para esse Meio de Pagamento, o sistema continuará considerando a Conta/Caixa configurada na abertura da Sessão.

Importante: A exceção à regra descrita acima é quando a coligada está parametrizada para utilizar a [solução de pagamento "TOTVS Pagamento Instantâneo (TPI/TPD)"](https://tdn.totvs.com/pages/viewpage.action?pageId=577622236) e o pagamento é realizado via PIX. Neste caso, se a solução de pagamento "TOTVS Pagamento Instantâneo (TPI)" for marcada, o sistema sempre irá considerar a conta/caixa de 'Baixa (Previsão)', definida [nos parâmetros do TOTVS Pagamento Instantâneo](https://tdn.totvs.com/pages/viewpage.action?pageId=611627231). Logo, é esta conta/caixa que será gravada no item de baixa do lançamento baixado via sessão de caixa.   
Caso seja definida a opção "TOTVS Pagamento Digital (TPD)" como solução de pagamento, o sistema considera a conta/caixa definida no lançamento financeiro. Se no lançamento financeiro não existir uma conta/caixa associada, o sistema passa a considerar a conta/caixa da 'Conciliação (Liquidação)', definida no mesmo parâmetro citado acima e também a utiliza no item de baixa do lançamento.

**Gera extrato compensado na baixa** - Configura se o extrato gerado por esse Meio de Pagamento no Módulo de Caixa 2.0 será incluído como compensado ou não.

Orientação

Todas essas configurações refletirão somente em baixas realizadas com esses Meios de Pagamento no Módulo de Caixa 2.0.

---

Se você usa algum dos parâmetros que não estão sendo considerados no Módulo de Caixa 2.0 e serão descontinuados, [compartilhe conosco](https://docs.google.com/forms/d/e/1FAIpQLSfhk_esNFQZK8Za0XbeAK4GjGgbG27nRqazmuoHrPJtXDfWpQ/viewform).

0solid

[Voltar para o Menu Principal](https://tdn.totvs.com/pages/viewpage.action?pageId=744486517)
