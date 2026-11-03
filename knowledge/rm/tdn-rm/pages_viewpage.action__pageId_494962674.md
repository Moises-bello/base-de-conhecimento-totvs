---
content_hash: 5408279c48e2b750eaf4a3474f656dab05fe8d3014dcf5ab90663a77f2f5ae63
fetched_at: '2026-06-29T00:10:21.911975+00:00'
page_id: '494962674'
product: rm
source: tdn-rm
title: Negociação Online - Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=494962674
version: 103
---

Os itens a seguir servirão de guia para a utilização da Negociação Online disponível no portal do Aluno. A partir da seleção dos lançamentos em abertos e de uma opção de acordo, o usuário pode fazer uma simulação da negociação e visualizar as novas parcelas, seus valores e respectivos vencimentos.

Serão exibidos para seleção os lançamentos em que o Cliente/Fornecedor esteja vinculado ao usuário no Educacional, que pode ser o próprio aluno ou o responsável financeiro. A simulação pode ser impressa e, seguindo as etapas do processo, o acordo será gerado com base nas informações fornecidas.

Para utilização da Negociação Online, a parametrização do Acordo no Educacional deve ser realizada (Processo 15.02 – Tesouraria | Geral 1/2) 

Atenção

Tivemos algumas alterações em relação ao acesso aos boletos elegíveis para "Negociação On-line":

* Ao logar com o usuário do Aluno, é necessário que usuário tenha o mesmo Nome e CPF do Responsável Financeiro, ou o Usuário de Acesso informado.
* Ao logar com o usuário do Pai ou Mãe, será aplicado a regra que só terá acesso caso o Responsável Financeiro tenho o Usuário de Acesso informado.

A seguir, apresentamos o exemplo para vincular corretamente o usuário ao responsável financeiro.

Quando o responsável financeiro é um familiar ou terceiro, verificamos se o usuário de acesso dessa pessoa está vinculado ao cadastro do Cliente/Fornecedor.

Importante!

Somente o responsável financeiro pelo boleto está autorizado a realizar acordos relacionados a ele.

**Atenção**: Para acessar a Negociação Online com segurança, é necessário habilitar a visualização no perfil do usuário no Portal.

Parametrização do Template de Acordo

O template de Acordo deve ser previamente cadastrado na Gestão Financeira, para mais informações sobre o cadastro, [clique aqui.](https://tdn.totvs.com/display/public/LRM/Template+de+Acordo)

Acesse: **Contas a Pagar/Receber | Acordo | Template de Acordo.** 

Apenas os modelos com a opção 'Disponível para Web' marcada serão exibidos no Portal do Aluno para uso na negociação.

Ao cadastrar o Template, atenção para os dois itens:

1. Informar no Anexo "Matriz Aplicada" do cadastro do template de acordo, as matrizes para as quais o template deve ser apresentado para utilização pelo aluno.

2. O perfil de usuário vinculado ao aluno também deve ser parametrizado para permitir a visualização do template. Isso é realizado associando o template de Acordo ao perfil, através do Anexo "Templates de Acordo Financeiro".

O template de acordo possui um anexo para cadastro de serviços, considerando as seguintes regras:

* Os templates que possuírem algum serviço cadastrado serão restritivos apenas àqueles serviços, sendo que esses serviços estão relacionados ao serviço informado na parcela.
* Para que o template esteja disponível a todos os serviços basta não informar nenhum serviço no cadastro.
* Caso o aluno selecione no portal duas parcelas ou mais parcelas que possuam serviços diferentes, será mostrado apenas template que contemplem os dois serviços, ou template que não possuem cadastro de serviço.

No Portal a Negociação Online está disponível no menu: "Negociação on-line".

Na aba **Introdução**o cliente poderá parametrizar um texto para o aluno ou responsável financeiro.

Na aba **Débitos Financeiros** o usuário deverá selecionar os lançamentos/boletos que deseja negociar. 

Caso o aluno possua lançamentos/boletos que incluam bolsa do tipo **Novo FIES**, tanto os lançamentos/boletos do aluno quanto os do outro sacado (banco financiador) não serão exibidos durante a negociação. Isso ocorre porque o aluno não tem a possibilidade de negociar diretamente com a instituição, mas sim com o sacado que fará o repasse para Instituição de Ensino.

Na aba **Opções de Acordo** é apresentado o total dos lançamentos/boletos selecionados na aba anterior e, a partir da seleção do template de acordo desejado, será possível realizar a simulação para verificar como ficará o acordo.

Os templates de acordos exibidos estão diretamente relacionados à matriz aplicada ao template de acordo. Apenas os modelos que têm a mesma matriz aplicada serão mostrados quando mais de um lançamento/boleto for selecionado.

As informações relacionadas aos valores de multas e juros devem ser configuradas diretamente no template de acordo disponibilizado para a negociação online.

O usuário poderá imprimir a simulação realizada através do botão "Imprimir simulação"

Na aba seguinte **Confirmação**, caso esteja parametrizado será apresentado o termo de aceite para que o usuário leia e aceite.

Caso o usuário queira, poderá imprimir o termo de aceite através do botão **Imprimir.**

Após o aceite, o usuário poderá confirmar a negociação.

Após confirmar a negociação, será exibida mensagem ao usuário indicando que o acordo foi realizado com sucesso, e dando opção para que o mesmo possa realizar o pagamento.

Confirmação da Negociação

Na aba **Confirmação** será exibido as opções de pagamento disponiveis para o aluno, saiba mais acessando [Extrato Financeiro - (Menu Exibição de opções de pagamento)](https://tdn.totvs.com/x/auhvI)

A tela de confirmação da negociação será desconsiderada e o usuário será redirecionado automaticamente para a tela de pagamento com cartão de crédito/débito, ao final da negociação. Caso todas as condições abaixo for atendidas:

* Possuir apenas um template de acordo disponível para web;
* Ter a quantidade máxima de parcelas desse template de acordo igual a um;
* O serviço vinculado ao lançamento do acordo está com apenas a opção de pagamento com cartão de crédito/débito marcada;
* O parâmetro "Habilitar pagamento com cartão (opção crédito/débito dependerá dos serviços ou da operadora)" deve está marcado (Ambiente | Parâmetros | Educacionais | RM Portal  | Gerais | 11/15).
* A opção de "Indisponível pgto. cartão de credito" deve está desmarcada na matriz aplicada
Atenção

* O tipo de pagamento (cartão de crédito, débito, PIX e boleto) será disponibilizado conforme o cadastro do serviço vinculado a parcela do contrato proveniente da "Negociação on-line".
* As parcelas provenientes do contrato da "Negociação on-line" serão gerada considerando o serviço configurado nos parâmetros do TOTVS Educacional
* O tipo de contábil dos lançamentos das parcelas provenientes do contrato da “Negociação on-line” via **Portal do Aluno** e via **Meu eduCONNECT** será definido considerando o tipo contábil cadastrado no serviço configurado nos parâmetros do TOTVS Educacional somente quando o parâmetro de sistema “**Tipo contábil por serviço**” estiver marcado.

É importante ressaltar que se o campo "Tipo contábil" do serviço utilizado nas parcelas do acordo não estiver preenchido, o TOTVS Educacional irá manter regra de preenchimento do tipo contábil conforme o TOTVS Financeiro (para maiores informações [clique aqui](https://tdn.totvs.com/display/LRM/FIN+-+Acordo))

O parâmetro de sistema “**Tipo contábil por serviço**” está presente na etapa “” no configurador de parametrização do TOTVS Educacional.

Cobrança Terceirizada

Os boletos que estiverem em **Cobrança Terceirizada** não serão disponibilizados para Negociação Online, para mais informações, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=553906289)

Desconto por meio de pagamento

Foi disponibilizado a função de fórmula TIPOPAGAMENTO, ao definir essa função no desconto do **Parâmetros no TOTVS Financeira | Contas a Receber | Manutenção de Lançamentos | Lançamentos | Inclusão | Formulas / Valores Defaults para Desconto,**será aplicado esse desconto conforme o meio de pagamento selecionado no portal.  
  
**TIPOPAGAMENTO****0 = Crédito****1 = Débito**  
**2 = PIX  
Quando o tipo de pagamento é null ou não é informado, não será passado nenhum meio de pagamento default.**

Deverá ser tratado na fórmula do desconto quando se tratar de lançamento gerados por negociação.

Exemplo de fórmula: Nessa fórmula será aplicado desconto após a negociação, quando for pagamento com crédito será considerado R$10 de desconto.

SE  TIPOPAGAMENTO = '0' ENTAO 50 SENAO 0  
ENTAO  
SE TIPOPAGAMENTO = '1' ENTAO 70 SENAO 0  
ENTAO  
SE TIPOPAGAMENTO = '2' ENTAO 100 SENAO 0  
ENTAO  
SE **TABLANBAIXAACORDOORIGEM**('IDACORDO','V') <= 0

O valor do boleto é R$150, conforme a fórmula definida será aplicado um desconto de R$50 por pagamento com cartão de crédito após realizar a negociação.
