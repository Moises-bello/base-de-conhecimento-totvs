---
content_hash: 43744f85f52c0bde8255e47754010f67c8347237cd56a9f5786c457a6b9ef623
fetched_at: '2026-06-29T00:10:32.601074+00:00'
page_id: '527386855'
product: rm
source: tdn-rm
title: Relação dos ID's de Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=527386855
version: 15
---

-1:  Parâmetro interno do sistema.

0 a 20: Id´s que representam os planos de contas contábil e gerencial.

21:  Refere-se a ao uso de código reduzido na conta contábil.

22: Parâmetro que permite ou não a edição do código reduzido na conta contábil.

23: Parâmetro que indica se o código da conta contábil possui digito verificador.

24:  Data Inicial do período contábil.

25: Data Final do período contábil.

26: Indica se o Lançamento contábil possui centro de custo ou não.

27: Parâmetro que indica se é obrigatório informar centro de custo ao incluir lançamento contábil ou não.

28:  Parâmetro não utilizado desde a versão 7.0.0.

29: Indica se é utilizado uma 2ª moeda no lançamento contábil. Quando marcado, ao colocar o valor do lançamento o sistema calcula automaticamente o valor que será lançado para a 2ª moeda parametrizada.

30 a 39: Parâmetros não utilizados.

40: Parâmetro que indica que ao realizar um lançamento contábil, caso a conta contábil tenha distribuição gerencial, uma janela de rateio será aberta automaticamente para confirmação dos dados.

41: Parâmetro que indica se a conta contábil é global.

42:  Indica se será possível colocar diferentes filiais para diferentes partidas dentro de um mesmo lançamento ou não.

43: Parâmetro que define se o preenchimento do Histórico Padrão  será obrigatório no lançamento contábil.

44: Indica qual a 2ª moeda que será utilizada no sistema.

45: Parâmetro não utilizado desde a versão 7.0.0.

46: Indica como será visualizado o Saldo nos relatórios, configuração com até 5 opções.

47: Parâmetro que indica o tamanho fixo do número do documento da partida referente a um lançamento contábil.

48 e 49: Parâmetros não utilizados.

50: Parâmetro que grava o último valor reduzido que foi gerado e cadastrado.

51: Grava o último número de conta contábil que foi cadastrado.

52: Parâmetro que define se o departamento será utilizado nos lançamentos contábeis.

53 a 67: Parâmetros não utilizados.

68: Este parâmetro define que na digitação do código do histórico, os valores serão adicionados de zeros a frente do código.

69: Quando o sistema está trabalhando com o código reduzido das contas, a ordenação é feita pelo reduzido. Este parâmetro estipula que, mesmo utilizando o reduzido, a ordenação seja feito pelo código.

70 : Quando habilitado, um novo número de documento será automaticamente gerado na inserção de um lançamento.

71: Parâmetro que define que ao criar um novo lote, o sistema irá verificar primeiro se já existe ocorrência de algum lote que utilizasse este mesmo código junto aos lançamentos integrados.

72: Para que usuário possa utilizar a tecla 'enter' como tecla 'tab', este parâmetro deve estar marcado.

73: Define qual o tipo do dígito da conta.

74: Parâmetro que define se contrapartidas serão utilizadas nos lançamentos contábeis.

75: Define se ao realizar a manutenção de um lançamento as regras (amarração de lançamento ou fórmulas) cadastradas serão verificadas ou não.

76: Parâmetro não utilizado desde a versão 10.60.0.

77: Define se irá utilizar amarração de campo complementar de lançamento no plano de contas contábil. Quando marcado, poderá ser cadastrado os campos complementares de lançamentos de cada conta.

78: Sinal que irá representar o Saldo nos relatórios contábeis.

79: Símbolo que irá representar a moeda corrente que será utilizada nos relatórios contábeis.

80: Define que será utilizado tamanho fixo das variáveis do complemento de histórico.

81: Parâmetro que define se será impresso as horas nos relatórios.

82: Parâmetro não utilizado.

83: O sistema permite que seja informado um código reduzido para o centro de custo. Este parâmetro tem como finalidade verificar se o usuário deseja trabalhar com o reduzido do centro de custo.

84 a 89: Parâmetros não utilizados.

90: Parâmetro que define data do fechamento do período contábil.

91: Define se os lotes sem lançamentos de outros sistemas serão visualizados ou não.

92: Parâmetro que define se as máscaras de edição e impressão das contas contábeis e gerenciais serão diferentes.

93: Os históricos de fechamento, por padrão, são utilizados apenas na transferência de grupos contábeis. Habilitar este parâmetro significa que você esta permitindo a utilização desses históricos na inserção manual de lançamentos.

94: Define o sinal do saldo inverso nos relatórios.

95: Define se lançamentos originários do Financeiro terão a alteração barrada pelo sistema ou não.

96: Define se o preenchimento do número do documento será obrigatório no lançamento contábil ou não.

97: Define se o sistema irá utilizar mascara ou não nas contas contábeis.

98: Parâmetro que define o preenchimento obrigatório do histórico ou do complemento de histórico.

99: Define se utilizará numeração sequencial de páginas nos relatórios.

100: Define qual o número da página para os relatórios.

101: Parâmetro quando marcado, ao criar um novo lote, o sistema irá verificar primeiro se já existe ocorrência de algum lote que utilizasse este mesmo código junto aos lançamentos integrados.

102: Parâmetro não utilizado.

103: Define se irá quebrar por palavra na impressão do histórico contábil.

104: Define se o plano de conta que está sendo cadastrado será global ou não.

105: Define quais caracteres poderão aparecer no código do histórico padrão;

106 a 108: Parâmetros não utilizados.

109: Define se será permitido mais de um lançamento com diferença por usuário ou não.

110: Parâmetro que define se será permitido utilizar moedas diferenciadas no campo segundo valor dos lançamentos.

111 e 112: Parâmetros não utilizados desde a versão 7.0.0.

113 a 122: Parametrização de mascaras do plano de contas gerencial, do grupo 0 a 9.

123 a 132: Parametrização de mascaras que serão exibidas nos relatórios do plano de contas gerencial, do grupo 0 a 9.

133:  Parâmetro que define se alterações e exclusões de lançamentos originários da Folha de Pagamento serão barrados.

134: Parâmetro não utilizado.

135: Parâmetro que define se o sistema colocará zeros à esquerda do número do documento no lançamento contábil.

136: Parâmetro quando marcado, sempre que for feita a alteração do valor e/ou a data de cotação de um lançamento, o segundo valor deste lançamento será recalculado automaticamente de acordo com os novos dados informados.

137: Recurso que permite que na inclusão de uma conta o sistema informa automaticamente um código.

138: Parâmetro não utilizado.

139: Define se lançamentos em centro de custo inativo será barrado ou não.

140: Define se lançamentos em departamento inativo será barrado ou não.

142: Define se quando um valor de lançamento for alterado, o sistema irá calcular um novo valor de rateio automaticamente ou não (deixará o valor antigo).

143: Define se quando um valor de lançamento for alterado, o sistema irá calcular um novo valor de rateio automaticamente ou não (deixará o valor antigo) baseado no percentual.

144: Parâmetro não utilizado.

145: Parâmetro que define se exclusões de lançamentos originários do Financeiro serão barradas.

148: Parâmetro que define qual é a informação que deverá ser considerada para o preenchimento dos registros do SPED Contábil que tenha centro de custo.

149: Identifica qual é a classificação do País Conforme o Ato Cotepe, que será utilizado pelo processo de geração do SPED Contábil.

150: Identifica qual é a classificação do município conforme o IBGE, que será utilizado pelo processo de geração do SPED Contábil.

153: Identifica se deve ser verificado o bloqueio de contabilidade ou não.

156: Parâmetro não utilizado.

157: Parâmetro que define se o nome do usuário vai ser apresentado na visão de lançamentos contábeis.

158: Esta propriedade define se o serviço de agrupamento deve desconsiderar a validação de Fórmula.

159: Informa se a regra de validação de fórmula ou amarração de lançamento será aplicada no processo de integração de lote.

160: Identifica se existe segurança cadastrada para o campo data da tabela CPARTIDA.

161:  Parâmetro que define se irá gerar a contra partida nos lançamentos contábeis gerados no módulo Gestão Contábil.

162: Marcando este parâmetro, o sistema irá verificar se a soma das partidas de débito é igual a soma das partidas a crédito.

163: Parâmetro que define se as ordens de gravação das Partidas devem ser conforme a ordem parametrizada no sistema.

164 a 166: Define qual é a ordem em que a Partida será gravada no Banco de Dados (Débito, Crédito ou Débito/Crédito).

167: Define qual é a ordem em que a Partida será gravada no Banco de Dados em relação ao Valor (Crescente ou Decrescente).

168: Define se as Partidas serão gravadas na ordem que foi digitada, isto quando a Partida for incluída diretamente no módulo Gestão Contábil.

169: Permite que o sistema tenha contabilização com centro de custo inativo parametrizada por módulo.

170: Permite que o sistema tenha contabilização com centro de custo inativo parametrizada por módulo ,porem esta item grava no texto os módulos permitidos.

171: Este parâmetro permite que o bloqueio seja realizado por lançamento, exemplo, ao integrar um lote, será bloqueado os lançamentos que estão sendo integrados e não mais lote, sendo assim, outro usuário poderá enviar informações para o lote, ou editar lançamentos que não estejam sendo integrados.

172: Permite alterar Conta Contábil de débito, crédito e contra partida nos Lançamentos estornados e estorno.

173: FCONT – Define se irá processar o saldo das contas de resultado antes do encerramento conforme o período informado e não conforme o encerramento realizado pela Transferência de grupos contábeis.

174: SPED - Parâmetro que quando marcado, o sistema irá verificar se a tabela existe, se não existir vai orientar ao cliente a entrar em contato com o suporte.

175: Permite alterar histórico e complemento nos Lançamentos estornados e estorno.

176: Identifica qual Centro de Custo o cliente quer que o sistema considere nas movimentações sem Centro de Custo ao gerar a ECF e SPED Contábil.

177: Parâmetro que quando marcado, permite enviar plano de contas transmitido para o SPED junto com os Livros Diários e Auxiliares,  e com os documentos da Escrituração Contábil Digital, com contas que não tenham saldo ou não tenha sido movimentadas no período.

178: Habilita controle de Moeda Funcional no SPED Contábil.

179: Parâmetro não utilizado.

180:  Marcando essa opção o reduzido é preenchido sequencialmente sem que as lacunas deixadas por alguma exclusão de conta sejam preenchidas.

181: Parâmetro "Não calcular/atualizar capa do lote automaticamente ao abrir a visão de lotes" : Indica se a capa do lote será calculada automaticamente ao abrir a visão de lote. Para mais informações .

182: Permite que o módulo selecionado use o código estruturado de centro de custo mesmo que o parâmetro 'usa reduzido' esteja marcado.

183: Permite que o sistema mostre o código estruturado do centro de custo mesmo quando se parâmetro 'usa reduzido' estiver marcado, porem esta item grava no texto os módulos permitidos.

184: Identificador do país que será utilizado para recuperar o código existente na classificação. Esta informação será utilizado pelo SPED Contábil na geração do registro k100.

185: Conta contábil crédito a ser utilizada em lançamentos cujos valores são relativos a ajustes decorrente de diferença do uso de multimoeda.

186: Conta contábil débito a ser utilizada em lançamentos cujos valores são relativos a ajustes decorrente de diferença do uso de multimoeda.

187: Histórico padrão a ser utilizada em lançamentos cujos valores são relativos a ajustes decorrente de diferença do uso de multimoeda.

188: Conta Contábil que receberá o lançamento a crédito para ajuste de conversão em multimoeda.

189: Conta Contábil que receberá o lançamento a Débito para ajuste de conversão em multimoeda.

190: Data de corte do novo modelo de eliminação. Após o preenchimento desta data só poderão ser criadas eliminações através da inclusão de partidas que possuam contrapartida de eliminação.

191: Habilita e desabilita utilização de Fluxo de Aprovação.

192: Centro de custo a ser utilizado em lançamentos cujos valores são relativos a ajustes decorrente de diferença do uso de multimoedas.

8867: (Parâmetro interno) Data de início parametrizada na execução da ferramenta de diagnóstico.

8868: (Parâmetro interno) Data final parametrizada na execução da ferramenta de diagnóstico.

9898: Identifica se os agendamentos de lançamentos contábeis foram convertidos para Lançamentos Periódicos.

9999: Identifica qual foi a data em que a consistência de lançamento foi executada pela ultima vez.
