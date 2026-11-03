---
content_hash: 355e3d6f5543e5ed5f0453515fe84ae250b7906d0f5df452e8b1db21961bf4e6
fetched_at: '2026-06-29T00:11:42.954920+00:00'
page_id: '799869473'
product: rm
source: tdn-rm
title: Extrato Financeiro.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=799869473
version: 37
---

**A partir da versão 12.1.2306** foram criadas novas politicas para visualização dos boletos no extrato financeiro, algumas configurações devem ser validadas para seu funcionamento. [(Nota) Acesso aos boletos do extrato financeiro 12.1.2306](https://tdn.totvs.com/display/LRM/8+-+%28Nota%29+Acesso+aos+boletos+do+extrato+financeiro+12.1.2306)

Acesso à visualização com a listagem de títulos vencidos, a vencer e pagos além de outras funcionalidades contidas na descrição do funcionamento abaixo nesse documento.

| Boletos vencidos | Boletos a vencer | Boletos pagos |
| --- | --- | --- |

Após acessar o menu de pagamentos, serão exibidas as listagens de títulos vencidos, a vencer e pagos.

Poderão ter acesso aos títulos as pessoas abaixo:

* Aluno
* Responsável Financeiro do Aluno
* Responsável Acadêmico do Aluno
* Pai / Mãe
* Responsável Financeiro do Contrato

Através da tela do extrato financeiro, temos também acesso às seguintes funcionalidades:

* Seleção de títulos
* Pagamento de títulos
* Negociação
* Gerenciamento da Carteira Digital
* Gestão da Recorrência
* Visualização de comprovante de pagamento

Seleção de títulos

Títulos **vencidos** e **a vencer** podem ser selecionados para pagamento. Já os títulos **pagos** podem ser selecionados para emissão do comprovante de pagamento.  
A seleção de títulos mostrará a quantidade de registros selecionados de acordo com a situação do título: **vencido**, **a vencer** ou **pago** em sua respectiva aba conforme abaixo:

| Seleção de boletos vencidos ou a vencer | Seleção de boleto pago |
| --- | --- |

**Observações:** Só será permitida a seleção de um título pago de cada vez já que o comprovante é individual.  
A seleção de registros **vencidos** ou **a vencer** anula a seleção de registro **pago**, se existir.   
O contrário também acontece, ou seja, a seleção de um registro **pago** também anula a seleção de registros **vencidos** ou **a vencer** selecionados.

Atenção

Somente será permitido selecionar um boleto por vez para pagamento.    
Negociação será permitida para mais de um boleto.  
Caso seja selecionado mais de um boleto para pagamento, será exibido um alerta para o usuário.

Pagamento de títulos

Ao selecionar algum título para pagamento e clicar no botão "**Efetuar pagamento**" exibido no final da listagem dos títulos, serão exibidas as opções de pagamento.

Após selecionar uma opção de pagamento, será exibido o valor líquido do título selecionado e posterior finalização do pagamento conforme opção de pagamento.  
  
  

Dica

O valor líquido do título poderá ser tratado por uma fórmula associada ao lançamento no TOTVS Gestão Financeira com regra de acordo com a opção de pagamento selecionada.

[Pagamento com PIX](https://tdn.totvs.com/x/8sZhM)

[Pagamento com Cartão](https://tdn.totvs.com/x/RKYyN)

[Pagamento com Boleto](https://tdn.totvs.com/x/gqNhM)

Desconto por meio de pagamento

Foi disponibilizado a função de fórmula TIPOPAGAMENTO, ao definir essa função no desconto do **Parâmetros no TOTVS Financeira | Contas a Receber | Manutenção de Lançamentos | Lançamentos | Inclusão | Formulas / Valores Defaults para Desconto,**será aplicado esse desconto conforme o meio de pagamento selecionado no portal.  
  
**TIPOPAGAMENTO****0 = Crédito****1 = Débito**  
**2 = PIX  
Quando o tipo de pagamento é null ou não é informado, não será passado nenhum meio de pagamento default.**  
  
Exemplo de fórmula: Nessa fórmula será aplicado desconto se o meio de pagamento for PIX.  
SE TIPOPAGAMENTO = '2'  ENTAO 100 SENAO 0

O valor do boleto é R$1.000, conforme a fórmula definida será aplicado um desconto de R$100 por pagamento com PIX.

Boletos cancelados e inativos

Boletos cancelados e inativos serão exibidos se o parâmetro "**Não exibir boletos cancelados na tela de histórico financeiro do aluno**", presente em Configurações | Parâmetros | RM Portal |RM Portal Gerais | Portal - Geral 8/18 estiver **desmarcado**.

Não terão as opções de pagamentos disponibilizadas no extrato e nem será permitida a seleção destes títulos. Boletos cancelados e inativos serão exibidos conforme a imagem abaixo: 

Cobrança Terceirizada

O parâmetro "**Parâmetros -> Educacional -> Tesouraria -> Geral 3/4 -> Mensagem informativa sobre boletos enviados para cobrança terceirizada**" não terá efeito no eduFlow (somente no Meu eduCONNECT).  

Também é possível definir uma mensagem em [Parâmetros -> Educacional -> Tesouraria -> Geral 3/4 ->](https://tdn.totvs.com/display/LRM/Tesouraria) **Mensagem informativa sobre boletos enviados para cobrança terceirizada,** ao clicar no boleto que estiver com cobrança terceirizada essa mensagem irá aparecer no fim da tela do app.         

Boletos que estiverem em **Cobrança Terceirizada** não terão as opções de pagamentos disponibilizadas no extrato e nem será permitida a seleção destes títulos, para mais informações, [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=553906289)

Boletos em "Cobrança Terceirizada" serão exibidos conforme abaixo:

Negociação

Possibilidade de fazer uma negociação de títulos. Para mais informações [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=874598653).

Gerenciamento da Carteira Digital

Inclusão / exclusão de cartões na carteira digital do usuário. Para mais informações [clique aqui](https://tdn.totvs.com/display/LRM/eduFlow21+-+Carteira+Digital).

Gestão da recorrência

Listagem, exclusão e informações de como realiza novas recorrências. Para mais informações acesse  e 

Visualização do comprovante de pagamento

Visualização de dados referentes ao pagamento do título selecionado. Para mais informações [clique aqui](https://tdn.totvs.com/display/LRM/eduFlow+11.9+-+Comprovante+de+pagamento).

]]>
