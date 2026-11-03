---
content_hash: 1ae12a9508e005223f8935917f4e2aea69b1651f0cbfc30baa8f40e7f11cf3f9
fetched_at: '2026-06-29T00:12:02.739770+00:00'
page_id: '904038185'
product: rm
source: tdn-rm
title: Cópia de Boletos Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=904038185
version: 1
---

---

Este menu tem como objetivo listar a relação de todos os boletos do aluno de acordo com a seleção do contexto.

 **Financeiro | Boletos**

O Aluno ainda contará com os seguintes filtros de acordo com a seleção do Período Letivo.

* **Pagos**: Lista a relação de todos os boletos pagos.
* **Pagos Parcialmente**: Lista toda a relação de boletos pagos parcialmente.
* **Em aberto**: Lista a relação de todos os boletos em aberto.
* **Cancelado**: Lista a relação de todos os boletos cancelados pelo setor financeiro.
* **Inativo:**Lista a relação de todos os boletos inativos. De acordo com as definições do TOTVS Gestão Financeira os boletos poderão assumir o status Inativo quando o valor total líquido do lançamento for baixado. Por exemplo, um lançamento vinculado a 3 boletos, onde um deles foi incluído com o valor total do lançamento e os outros dois com valores parciais para o mesmo lançamento. Ao baixar um boleto Parcial, a baixa deve ser realizada com o valor parcial que o boleto foi gerado, e ao realizar a baixa do boleto gerado com o valor integral, a baixa será realizada com o valor restante do lançamento. O boleto não baixado, terá o status alterado para inativo não podendo ser realizada nenhuma ação sobre ele.

O Filtro: "Boletos em aberto de todos os Períodos Letivos" lista a relação de todos os boletos em aberto em todos os Períodos Letivos.

O Usuário da Secretaria tem a opção de determinar a visualização dos boletos Cancelados e Pagos Parcialmente no portal através do parâmetro: TOTVS Educacional | Parâmetros | RM Portal | Portal Geral 7/10

* Não exibir boletos cancelados na tela de histórico Financeiro do aluno
* Possibilitar a impressão de boletos pagos parcialmente

Para os boletos com o Status: Em aberto, o aluno contará com a opção de Pagamento com Cartão de Crédito (através do ícone: Cartão), Pagamento com PIX ou por Boleto.

Quando os boletos forem de bolsas do **Novo FIES** não serão apresentados os boletos do aluno e nem do outro sacado (Banco Financiador), isso porque com o Novo FIES o aluno fará o pagamento da mensalidade para a Banco e essa fará o repasse para Instituição de Ensino.

Para mais informações sobres os meios de pagamento acesse a aba Boletos abaixo:

BoletosPagamento com CartãoPagamento com Cartão de Crédito - Cielo

O Aluno tem a opção de efetuar o pagamento dos Boletos com Cartão de Crédito no Totvs Portal Educacional.

Através do menu: Financeiro | Extrato Financeiro, onde é possível realizar o pagamento de mensalidade e outras taxas usando cartão de crédito, e agora permite também o parcelamento do valor e o uso da função débito da operadora de Cartão de Crédito CIELO.

A instituição irá definir se permite o pagamento por essas opções, e se afirmativo, o usuário poderá realizar o pagamento com cartão de crédito ( à vista ou parcelado) ou cartão de débito. O boleto pago já será baixado automaticamente no sistema.

**Configuração no Totvs Gestão Financeira**

No Totvs Gestão Financeira será necessário parametrizar a bandeira ( Visa / Master ) que será utilizado no processo e os dados do lojista.  
  
 **Contas a Receber | Baixas | Cartão de Crédito | Configurações Globais Cartão / Débito. Informar os dados do Lojista ( Código de afiliação / Chave de acesso e o Endereço de Acesso).**

* Selecionar a opção de Pagamento: BuyPage e ChekOut;
* Configurações Cartão Bandeira Visa. Permite ativar a função de Crédito e Débito;
* Configurações Cartão Bandeira Mastercard. Permite ativar a função Crédito.

Para ambas as bandeiras necessário informar : Conta Caixa, Meio de pagamento e o Número máximo de Parcelas.

**Configuração no Totvs Gestão Educacional**

* O Educacional não está integrado ao Protheus EAI 1.0 com pacote de integração 1012;
* O parâmetro do portal possibilitando o pagamento com cartão deverá estar ativo;

**Totvs Gestão Educacional | Configurações | Parâmetros | RM Portal | Portal Geral 7/10 - Pagamento dos boletos pode ser efetuado com Cartão de Crédito**

* A matriz aplicada do contexto não estiver configurada para não permitir pagamento com cartão;

Totvs Gestão Educacional | Currículo e Oferta | Matrizes Curriculares | 'Anexo' Matriz Aplicada

**Acesso ao portal com Login do Aluno e/ou Responsável Acadêmico / Financeiro**

 **Financeiro | Boletos e selecionar o botão: Cartão.**

Selecionar a opção de Pagamento: Cartão de Crédito ou Débito, e informar a quantidade de parcelas para pagamento.

Em seguida, o usuário será redirecionando para a página da CIELO para que seja informado os dados do Cartão de Crédito / Débito.

Desconto por meio de pagamento 

Foi disponibilizado a função de fórmula TIPOPAGAMENTO, ao definir essa função no desconto do **Parâmetros no TOTVS Financeira | Contas a Receber | Manutenção de Lançamentos | Lançamentos | Inclusão | Formulas / Valores Defaults para Desconto,**será aplicado esse desconto conforme o meio de pagamento selecionado no portal.  
  
**TIPOPAGAMENTO****0 = Crédito****1 = Débito**  
**2 = PIX  
Quando o tipo de pagamento é null ou não é informado, não será passado nenhum meio de pagamento default.**  
  
Exemplo de fórmula: Nessa fórmula será aplicado desconto se o meio de pagamento for crédito.   
SE TIPOPAGAMENTO = '0'  ENTAO 100 SENAO 0  
O valor do boleto é R$1.000, conforme a fórmula definida será aplicado um desconto de R$100 por pagamento com cartão de crédito. 

Após efetuar o pagamento, o boleto será baixado automaticamente, caso ocorra a mensagem: Aguardando Liberação do Setor Financeiro, executar o processo em:

 **Totvs Gestão Financeira | Movimentações Bancárias | Cartão de Crédito / Débito | Ajuste de Transações**

Para que os boletos sejam baixados e o status seja alterado no Portal.

Observações:

• Nossa aplicação trabalha somente com o ambiente da operadora Cielo.

• Somente as bandeiras Visa e Mastercard podem ser configuradas.

 • Para a função débito no momento aceita somente a bandeira Visa ( Visa Electron) com cartões emitidos pelos bancos validados pela Cielo: Bradesco, Bando do Brasil, Santander e HSBC. Novos bancos certificados podem ser verificados no site [www.cielo.com.br](http://www.cielo.com.br/)

 • A digitação e validação dos dados do cartão ocorre no ambiente da Cielo (ByPageCielo) sem interferência do aplicativo.

Para saber mais sobre o pagamento de Boletos com Cartão de Crédito no Portal, acessar documento [Boletim Técnico - Integração Módulo E-Commerce](http://tdn.totvs.com/pages/viewpage.action?pageId=42043861)

WorkFlow do ProcessoAtenção

A partir dos patches **12.1.2302.195, 12.1.2306.138 ou superiores** com o pagamento do boleto via cartão de crédito será mostrado para usuário o tempo que falta para o fechamento da tela de pagamento com cartão da ChekOut Cielo. E após **30 minutos** a tela de pagamento de cartão de créditos da ChekOut Cielo será **fechada**.

Pagamento com Cartão de Crédito - GetNet

O Aluno tem a opção de efetuar o pagamento dos Boletos com Cartão de Crédito pelo *gateway* de pagamento da empresa GetNet.

## Parametrização Educacional

**Configuração no Totvs Gestão Educacional**

* O Educacional não está integrado ao Protheus EAI 1.0 com pacote de integração 1012;
* O parâmetro *"Habilitar pagamento com cartão (opção crédito/débito dependerá dos serviços ou da operadora)"* deve está marcado.

Menu Financeiro / Contábil > Serviços. Selecione o serviço do plano de pagamento do contrato.

O parâmetro Permite pagamento (Portal do Aluno) > Cartão de Crédito/Débito deve estar marcado.

Menu Matrizes curriculares, selecione a matriz curricular. A opção "Indisponível pgto. cartão de credito" deve está desmarcada.

Para informações da parametrização necessária do módulo financeiro, favor acessar <http://tdn.totvs.com/x/QeIdGQ>.

## Acesso ao portal com Login do Aluno e/ou Responsável Acadêmico / Financeiro

 **Financeiro | Boletos e selecionar o botão: Cartão.**

Validar os dados cadastrais referente ao Responsável Financeiro vinculado ao boleto em aberto.

Selecione *Continuar* após inserir/editar os dados.

Selecione *Pagar* após conferir os dados.

Observação: os campos são bloqueados para conferência.

Em seguida, o usuário será redirecionando para a página segura da GetNet para que seja informado os dados do Cartão de Crédito / Débito.

Desconto por meio de pagamento 

Foi disponibilizado a função de fórmula TIPOPAGAMENTO, ao definir essa função no desconto do **Parâmetros no TOTVS Financeira | Contas a Receber | Manutenção de Lançamentos | Lançamentos | Inclusão | Formulas / Valores Defaults para Desconto,**será aplicado esse desconto conforme o meio de pagamento selecionado no portal.  
  
**TIPOPAGAMENTO****0 = Crédito****1 = Débito**  
**2 = PIX  
Quando o tipo de pagamento é null ou não é informado, não será passado nenhum meio de pagamento default.**  
  
Exemplo de fórmula: Nessa fórmula será aplicado desconto se o meio de pagamento for crédito.   
SE TIPOPAGAMENTO = '0'  ENTAO 100 SENAO 0

O valor do boleto é R$1.000, conforme a fórmula definida será aplicado um desconto de R$100 por pagamento com cartão de crédito. 

Pagamento com cartão - eduCONNECT Pay

Para saber sobre pagamento com eduCONNECT Pay, consulte a documentação, [clicando aqui.](https://tdn.totvs.com/display/LRM/eduCONNECT+Pay)

Pagamento com PIX

Está disponível no sistema a opção de pagamento com PIX

Para que a opção Pix esteja disponível no portal é necessário a parametrização do cadastro de Serviços do TOTVS Educacional, para mais informações sobre o cadastro, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=425458880)

Ao clicar na opção PIX, será exibido o QR Code contendo as informações para realizar o pagamento.

Importante ressaltar que a confirmação do pagamento será processado após o retorno do banco.

A regra de processamento do QR Code e executado pelo TOTVS Financeira, para maiores informações veja os documentos [TOTVS Pagamento Digital](https://tdn.totvs.com/display/LRM/FIN+-+Contas+a+receber) e [PIX - Pagamentos instantâneo](https://tdn.totvs.com/pages/viewpage.action?pageId=572497578).

**A partir da versão 12.1.2306** está disponível também a opção Pix copia e cola, que trará mais facilidade para o usuário para copiar o QR code.

Desconto por meio de pagamento 

Foi disponibilizado a função de fórmula TIPOPAGAMENTO, ao definir essa função no desconto do **Parâmetros no TOTVS Financeira | Contas a Receber | Manutenção de Lançamentos | Lançamentos | Inclusão | Formulas / Valores Defaults para Desconto,**será aplicado esse desconto conforme o meio de pagamento selecionado no portal.  
  
**TIPOPAGAMENTO****0 = Crédito****1 = Débito**  
**2 = PIX  
Quando o tipo de pagamento é null ou não é informado, não será passado nenhum meio de pagamento default.**  
  
Exemplo de fórmula: Nessa fórmula será aplicado desconto se o meio de pagamento for PIX.  
SE TIPOPAGAMENTO = '2'  ENTAO 100 SENAO 0

O valor do boleto é R$1.000, conforme a fórmula definida será aplicado um desconto de R$100 por pagamento com PIX.

Emissão de BoletosParâmetros do Sistema

Este ícone só estará disponível, se o usuário parametrizar o relatório nos parâmetros do TOTVS Educacional, disponível em: **TOTVS Educacional |Configurações | Parâmetros | Tesouraria | Relatórios**

Para saber mais sobre configuração de boletos, acessar documento: 

Para a emissão dos boletos Pagos Parcialmente, é necessário que o usuário configure essa funcionalidade em: **TOTVS** **Educacional |Configurações | Parâmetros | RM Portal | Portal Geral 7/10**

Ainda na tela de visualização dos boletos com o status: Em Aberto ou Pago parcialmente, o Aluno / Responsável tem a opção de emitir os boletos para o pagamento através do ícone: Boletos 

Após configurar a emissão dos boletos, acessar o portal em: **Portal Educacional | Financeiro | Boletos | 'Ícone' Boleto**

Após clicar no ícone de Boleto, será exibido um popup com o boleto para o usuário conforme abaixo:

Após clicar em imprimir, o boleto será exibido para o usuário novamente com opção de impressão ou download.

ATENÇÃO

Se algum bloqueador de popup estiver bloqueando a emissão do boleto, será exibida a opção para salvar o boleto para posterior impressão caso seja necessário.

Boletos agrupados

Os lançamentos gerados para o aluno são gerado com seu respectivo boleto, quando o responsável financeiro solicita agrupar os boletos que contemplam a mesma data de vencimento do mesmo aluno, ou de alunos diferentes que ele é o mesmo responsável, é utilizado o processo de .

Quando acontece o agrupamento dos lançamentos em um único boleto dos alunos pelos quais é responsável, no Portal terá a opção de visualizar os boletos agrupados independente do contexto selecionado ou do aluno logado.

Exibição de opções de pagamento

Além das parametrizações necessárias (Vide [Pagamento com Cartão - e-Rede](https://tdn.totvs.com/pages/releaseview.action?pageId=515301823) em caso de dúvida), para que seja exibida uma opção de pagamento nesse extrato financeiro, será necessário que a respectiva opção de pagamento ("Cartão de crédito", "Cartão de débito", "Boleto" ou "PIX") esteja marcada em **TODOS** os serviços do boleto.

Se uma opção de pagamento estiver **DESMARCADA** em um dos serviços do boleto, a mesma não estará disponível para o boleto no extrato financeiro.

As opções estão localizadas no [Cadastro de serviços](https://tdn.totvs.com/pages/viewpage.action?pageId=425458880)

Simular nova data de vencimento

Está disponível no sistema a opção:

* **Quantidade limite de dias após o vencimento do boleto para permitir a alteração:** Essa opção permitirá que a instituição informe a quantidade limite de dias para que o aluno consiga realizar a simulação e alteração do vencimento do boleto. Essa opção permitirá que o aluno consiga simular uma nova data de vencimento para o boleto e alterar essa data através do Portal do Aluno, respeitando o limite de dias parametrizado.

1. No Portal do Aluno a opção de **Simular nova data de vencimento** só estará disponível se o parâmetro **Quantidade limite de dias após o vencimento do boleto para permitir a alteração** estiver marcado e a quantidade de dias informada for maior que '0'.
2. A data de vencimento considerada no limite de dias para alteração será a do **lançamento**.
3. Caso o aluno tente simular ou gerar boleto com a data alterada ultrapassando a quantidade de dias limite parametrizada o sistema não irá permitir, apresentando uma mensagem informativa.

Neste exemplo o limite está configurado para 30 dias. A data inicial de vencimento do boleto é  respeitando o limite de 30 dias, a data de vencimento pode ser alterada para vencer no máximo em .  
Caso o limite seja desrespeitado o sistema não permitirá a alteração.

**Obs.** Existe a possibilidade da data de vencimento do lançamento ser diferente da do boleto. Quando ocorrer tal diferença, a data considerada para a validação do limite de dias, será a do lançamento. 

Quando a opção do parâmetro **"Quantidade limite de dias após o vencimento do boleto para permitir a alteração"**, estiver marcada e com limite de dias maior que '0', no portal será disponibilizado a opção de "**Simular nova data de vencimento**".

Após a simulação com a nova data de vencimento considerando juros e multas (se parametrizados no sistema), o aluno terá a opção de "Gerar boleto", clicando nessa opção o boleto será atualizado com nova data de vencimento.  
Essa opção só será habilitada se o aluno clicar no ***[checkbox](https://www.google.com/search?rlz=1C1GCEU_pt-BRBR828BR830&q=checkbox&spell=1&sa=X&ved=2ahUKEwiE6bvnyKLsAhU0GbkGHcuZAtEQBSgAegQIHhAt "Follow link")*"Estou ciente, ao clicar em "Gerar Boleto", não será possível reverter a operação.**

A partir da versão 12.1.2205 para realizar a geração de boletos é de suma importância que os usuários do portal tenham as permissões necessárias na gestão financeira.

O sistema considerará a seguinte regra na geração de boleto com uma nova data de vencimento.

* Caso o boleto possua status de remessa igual a Registrado, Registrado Online ou Remetido essa remessa será cancelada.
* O boleto será cancelado e ficará vinculado ao lançamento.
* Será gerado um novo boleto com a nova data de vencimento.

* Só será possível alterar o boleto para uma data de vencimento superior a data do boleto.
* Não será permitida alterar a data de vencimento do boleto para uma nova data de vencimento que ultrapasse o limite parametrizado.
* Não será possível alterar o boleto para uma nova data de vencimento inferior a data atual.
* Boletos com status Baixados e Cancelados não terá a opção de Simular Nova Data de Vencimento
* Boletos já Remetidos ou Registrados ao banco mudarão seu status para "Pendente Remessa" na alteração da data de vencimento do boleto   
  É importante ressaltar que nos casos em que o TOTVS Educacional efetuar o cancelamento automático da remessa dos boletos já registrados ou remetidos ao banco, o cliente deverá, através do TOTVS Gestão Financeira, enviar para o banco a remessa de cancelamento dos boletos afetados. Este controle poderá ser realizado através do TOTVS Gestão Financeira filtrando os boletos com status igual "Pendente Remessa".
Cobrança Terceirizada

**A partir da versão 12.1.2302** os boletos que estiverem em **Cobrança Terceirizada** não terão as opções de pagamentos disponibilizadas no extrato, para mais informações, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=553906289)

Filtro para impressão de 2ª Via de Boleto

Utilizando o mecanismo de filtro padrão da linha RM agora é possível restringir a listagem de boletos / lançamentos da funcionalidade de extrato financeiro do Portal (EducaMobile, Corpore.Net e Novo Portal do Aluno).

O novo parâmetro encontra-se disponível em Parâmetros Educacional > RM Portal > Gerais > 9/15.

Tabelas disponíveis: FLAN, FBOLETO para filtro.

Importante

1. O extrato financeiro disponível no portal será filtrado de acordo com o filtro definido acima.  
2. O filtro é utilizado nos dados do boleto e no detalhe dos lançamentos associados ao boleto.  
3. A definição do filtro pode impactar negativamente na performance da funcionalidade de extrato financeiro.  
4. O filtro não será aplicado em funções de cálculo do IPTE e relatórios de demonstrativo e boleto.  
5. Garantir que o filtro utilizado não limite lançamentos pertencentes a um agrupamento por boleto.

Customização da visualização do extrato financeiro

O cliente pode realizar a customização de como será apresentado os botões de pagamento de boleto e/ou pagamento por cartão de crédito no novo portal do aluno.

Segue abaixo um exemplo de customização básica que só aparecerá o botão de pagamento de boletos caso o valor original do lançamento for menor que R$ 1000.00.

**Bloco de código original do produto**

Arquivo "~\FrameHTML\web\app\Edu\PortalEducacional\js\aluno\financeiro\lancamentos\lancamentos-list.view.html

jsCódigo do produtotrue

{{'l-boleto' | i18n : [] : 'js/aluno/financeiro/lancamentos'}}
]]>

**Bloco de código customizado baseado no produto.**

Arquivo "~\FrameHTML\web\app\Edu\PortalEducacional\js\aluno\financeiro\lancamentos\**custom**\lancamentos-list.view.html

jsCódigo customizadotrue

{{'l-boleto' | i18n : [] : 'js/aluno/financeiro/lancamentos'}}
]]>

Para saber mais sobre a customização do novo portal, acessar documento: [Customização](http://tdn.totvs.com.br/pages/viewpage.action?pageId=284880328)

Parâmetros sobre Boletos de cobrança registrada

Os parâmetros abaixo poderão ser utilizados para configurar a impressão e o registro online dos boletos:

* **Permitir imprimir boletos não registrados (válido para convênios do tipo de cobrança registrada)**
* **Serviços que permitem registrar boleto online**

Caminho: ***15.04 - RM Portal | 15.04.01 - RM Portal - Gerais | Portal - Geral 10/15***

Esse parâmetro deve ser marcado para permitir que boletos que não foram registrados sejam disponibilizados para impressão.

Caso o parâmetro esteja **DESMARCADO**, a opção de impressão de boleto só aparecerá se o boleto estiver registrado ou se o serviço educacional, vinculado ao boleto, estiver marcado no parâmetro "**"**. Essa parametrização permitirá que o boleto seja registrado ao clicar na opção de impressão de boleto.

Importante

O parâmetro para a definição de serviços é necessário para boletos **NÃO REGISTRADOS** e que estejam vinculados a convênios de cobrança **REGISTRADA**.

Para boletos de convênios de cobrança **NÃO REGISTRADA**, sempre será exibida a opção de impressão do boleto no extrato financeiro (antigo e novo), assim como no Widget *"Próximo vencimento"*, contudo não haverá registro do boleto mesmo com o respectivo serviço marcado no parâmetro "**".**

**servicos\_que\_permitem\_registrar\_boleto\_onlineServiços que permitem registrar boleto online**

Os boletos, cujo o serviço vinculado esteja marcado, serão registrados na impressão do boleto, caso não tenham sido registrados anteriormente.

Importante

Se o serviço do boleto estiver marcado e o convênio vinculado à conta caixa do boleto NÃO permitir registro online, será exibida uma mensagem para o usuário. Ex.:

Exemplo: com a configuração abaixo, quando o aluno solicita a impressão de um boleto que não esteja vencido e nem registrado, e cujo serviço seja MENSALIDADE ou SEGURO, o boleto será registrado antes da exibição do arquivo do boleto no portal.

**Permitir imprimir boletos vencidos não registrados com X dias para o próximo vencimento**

Este parâmetro permite que boletos vencidos ainda não registrados possam ser impressos pelo portal do aluno.

Para isso:

* o parâmetro **,** deve ter serviço(s) selecionado(s).
* este parâmetro deverá estar marcado
* a quantidade de dias, que será utilizada para calcular a próxima data de vencimento do boleto, preenchida;
* no parâmetro **,** o(s) serviço(s) selecionado(s) devem ter associados a eles a conta caixa com o registro online de boleto configurado.

Importante

2. Este parâmetro só será aplicado se o convênio do boleto utilizar valor líquido ou parcial no código de barras.

No exemplo abaixo, o portal do aluno permitirá a impressão de boletos vencidos apenas dos serviços MENSALIDADE e SEGURO e que utilizam valor líquido ou parcial no código de barras. Para calcular a nova data de vencimento serão adicionados à antiga data de vencimento 210 dias.

Relatório de Recibo (Demonstrativo)

Uma vez parametrizado corretamente o novo portal do aluno funcionalidade extrato financeiro para lançamentos baixados, será disponibilizado um botão de nome "Recibo".

O relatório de demonstrativo, deverá estar parametrizado junto ao parametrizador do TOTVS Educacional, opção Tesouraria > Relatório. O relatório vinculado deverá exclusivamente ser do RM Reports.

Este relatório deve possuir as Tabelas FBOLETO, FLANBOLETO, FLAN para o correto funcionamento.

Para mais informações clique no vídeo abaixo.

250

Definição de colunas e valores a exibir

É possível definir as colunas e os valores que serão exibidos no extrato financeiro, para isso é necessário acessar o parametrizador do TOTVS Educacional, em Educacional > RM Portal > RM Portal - Gerais > Portal - Geral 8/18, conforme a imagem abaixo:

O indicado é selecionar até 12 campos para não comprometer o layout da tela.

Dentre as colunas, é possível definir: **Situação, Serviço, Parcela, Cota, Competência, Data de Baixa, Valor Bruto, Juros, Multa, Desconto, Baixado, Acréscimo do Acordo, Juros do Acordo e Desconto do Acordo.**

Dentre os valores a exibir, é possível definir: **Bolsa condicional, Bolsa incondicional, Pagamento a maior, Pagamento a menor, Acréscimo cobrança retroativa, Desconto cobrança retroativa, Valor de perda desconto por antecipação e Valor de repasse de bolsa a menor**.
