---
content_hash: e72f8045190e1a6c5b1fa7e9b8ccc927696aae88bedd0ecf6082b3128972a61c
fetched_at: '2026-06-29T00:09:33.836923+00:00'
page_id: '425459060'
product: rm
source: tdn-rm
title: Tesouraria
type: documentation
url: https://tdn.totvs.com/display/LRM/Tesouraria
version: 72
---

---

Estes parâmetros são necessários para o funcionamento correto dos processos de Tesouraria do sistema. O objetivo desta etapa é definir o comportamento do sistema em relação aos assuntos financeiros.

Tesourariageral1/2Geral 1/2

## **Acordo**

1
incomplete
Agrupar lançamentos de diferentes matrizes aplicadas:   
  Indica se lançamentos originados de contratos de diferentes matrizes aplicadas podem fazer parte do mesmo acordo.

2
incomplete
Agrupar lançamentos de serviços com tratamento diferente de inadimplência:   
  Ao ser marcado, gerará as parcelas no contrato do tipo "Acordo" conforme a parametrização do serviço para verificação de inadimplência.

Serviços parametrizado para verificar inadimplência:   
  As parcelas resultantes no contrato de "Acordo" terá o serviço parametrizado nesse campo se os lançamentos selecionados forem de parcelas com serviços que verificam inadimplência.

Serviço parametrizado para verificar NÃO verificar inadimplência:   
  As parcelas resultantes no contrato de "Acordo" terá o serviço parametrizado nesse campo se os lançamentos selecionados forem de parcelas com serviços que NÃO verificam inadimplência.

3
incomplete
Preenche mês/ano de competência da parcela com mês/ano do acordo:   
Indica se as parcelas do contrato do tipo "Acordo" terão o mês/ano de competência preenchidos.

## **Responsável Financeiro**

Máscara do código de Cliente/Fornecedor:     
  Máscara do cliente fornecedor parametrizada nos parâmetros do Totvs Gestão Financeira.

Código default para o responsável financeiro:   
  Máscara do cliente fornecedor a ser utilizada no cadastro do mesmo no Educacional. Utilizada, por exemplo, no cadastro do aluno como responsável financeiro.  
  Para mais informações sobre a máscara do cliente fornecedor, clique [aqui](https://tdn.totvs.com/display/public/LRM/FIN+-+Contas+a+receber)

Tipo de Cliente/Fornecedor:   
  Tipo do cliente/fornecedor que está sendo inserido pelo Educacional.  
  Para mais informações sobre tipo de cliente fornecedor, clique [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=421388694)

4
incomplete
**Cadastrar aluno como responsável financeiro:**Indica se o aluno será cadastrado automaticamente como responsável financeiro.

5
incomplete
**Verificar débitos do aluno em outras coligadas:**Indica se serão verificados débitos em outras coligadas na verificação de inadimplência

6
incomplete
**Mostrar valor original total na validação de inadimplência:**

Número de dias de carência para inadimplência:   
  Número de dias anteriores à data atual do sistema que o sistema não vai considerar o aluno como inadimplente mesmo que o vencimento seja anterior à data atual.  
  Ex.: Data do sistema (16/04/2023)          
        Número de dias informado para carência: 5 dias  
        Somente serão considerados para inadimplência, lançamentos com data de vencimento anterior à data 11/04/2023

Valor máximo de tolerância para inadimplência:  
  Quando informado, somente serão considerados para inadimplência, lançamentos com valor maior do que o valor informado no campo

Valor máx de conta corrente de tolerância para inadimplência:  
  Quando informado, somente serão considerados para inadimplência, valores em conta corrente com valor maior do que o valor informado no campo         

geral2/2Geral 2/2

## **Plano de Pagamento**

* **Modelo de plano de Pagamento:**
  + **Matriz Aplicada:** Todas as matriculas que utilizam a matriz aplicada configurada na  podem utilizar o plano de pagamento.
  + **Período da Matriz Aplicada:** Permite que os contratos que utilizam a matriz aplicada configurada na  e que o período da matricula esteja no intervalo de períodos configurados na Habilitação.
* **Gerar no contrato somente as parcelas do plano de pagamento com vencimento igual ou superior à data de inclusão do plano de pagamento no contrato:** Ao criar as parcelas no contrato do aluno a partir do plano de pagamento serão consideradas do plano de pagamento somente a parcela com data de vencimento a partir do mês que o plano de pagamento está sendo incluído no contrato.

Importante

É importante ressaltar que ao marcar esse parâmetros em função da data de inclusão do plano de pagamento no contrato, parcelas não serão consideradas, portando não serão cobradas, ou seja, esta funcionalidade não redimensiona os valores das demais parcelas do plano de pagamento.

Exemplo:

**Parcelas do Plano de pagamento selecionado:**

| Parcela | Data de vencimento | Valor |
| --- | --- | --- |
| 1º | 01/08/2021 | R$ 1.000,00 |
| 2º | 01/09/2021 | R$ 1.000,00 |
| 3º | 01/10/2021 | R$ 1.000,00 |

**Data execução da matricula no portal: 05/09/2021**

**Parcelas que serão incluídas no contrato**

| Parcela | Data de vencimento | Valor |
| --- | --- | --- |
| 2º | 01/09/2021 | R$ 1.000,00 |
| 3º | 01/10/2021 | R$ 1.000,00 |

* **Para parcelas com data de vencimento menor que a data de inclusão do plano de pagamento no contrato, a nova data de vencimento será  XX  dias após a data de inclusão do plano de pagamento no contrato:**Quando a data de vencimento da parcela do plano de pagamento for menor que a data de inclusão do plano no contrato, a nova data de vencimento será a data em que o plano de pagamento está sendo incluído no contrato mais a quantidade de dias informada aqui.

Exemplo

**Parcelas do Plano de pagamento selecionado:**

| Parcela | Data de vencimento | Valor |
| --- | --- | --- |
| 1º | 01/08/2021 | R$ 1.000,00 |
| 2º | 01/09/2021 | R$ 1.000,00 |
| 3º | 01/10/2021 | R$ 1.000,00 |

**Quantidade de dias parametrizado:3**

**Data execução da matricula no portal: 05/09/2021**

**Parcelas que serão incluídas no contrato**

| Parcela | Data de vencimento | Valor |
| --- | --- | --- |
| 1º | 08/09/2021 | R$ 1.000,00 |
| 2º | 08/09/2021 | R$ 1.000,00 |
| 3º | 01/10/2021 | R$ 1.000,00 |

Este comportamento será aplicado somente se o cadastro da parcela do plano de pagamento estiver com a opção “Data de vencimento flexível” marcada.

Para maiores informações**[clique aqui.](https://tdn.totvs.com/display/LRM/Parcelas+do+Contrato+Educacional)**

## **Casas decimais**

O usuário poderá parametrizar como serão exibidas as informações de créditos financeiros com número de casas decimais que lhe for mais conveniente. O número máximo de casas decimais que poderá ser parametrizado será quatro e o mínimo zero. *Importante:* Sempre que o número de casas decimais for alterado para menor, será possível definir como o sistema irá tratar o valor excedente das casas decimais. Para isto o usuário poderá irá definir como o sistema irá lidar: *Trunca*: o sistema irá desconsiderar o valor excedente de casas decimais. *Arredonda*: o sistema irá verificar o valor excedente e aplicar regra de arredondamento. Como exemplo de créditos financeiros definido com o valor 12,127. Após executado o parametrizador e selecionado a opção *Trunca* o valor assumido será 12,12 e se for a opção *Arredonda* o valor será 12,13.

geral3/4Geral 3/4

## **Meu eduCONNECT/Portal**

## **Recorrência**

7
incomplete
Permitir habilitar pagamento automático  

## **Extrato Financeiro**

**Mensagem informativa sobre boletos enviados para cobrança terceirizada:** ao clicar no boleto que tenha cobrança terceirizada a mensagem padrão ou a mensagem que for definida pelo cliente irá aparecer no fim da tela do app.

geral4/4Geral 4/4

## **Integração TOTVS Assinatura Eletrônica**

Onde será definido o usuário e senha de servidor para acessar o TAE

## **Fiador**

**Quantidade máxima de fiador(es) permitida**: este parâmetro permite definir mais de um fiador para o aluno.

**Permite pagamento somente para os alunos que já tiverem o fiador ativo e aprovado**: Quando estiver marcado e não existir Fiador para o aluno ou o Fiador não está aprovado, não será exibido as formas de pagamento no portal e Mobile (boleto, pix e cartão de crédito)

relatórioRelatório

**-Tipo de relatório de Contrato/Boleto:**  
Escolha entre Gerador de Relatório (Antigo) ou RM Reports e em seguida informe os relatórios, conforme o tipo escolhido, que serão indicados como default para a impressão dos Contratos, Boletos e Recibos respectivamente. Clientes com contratos novos não poderão utilizar o Gerador de Relatório Delphi (Antigo) e deverão definir os relatórios RM Reports que serão indicados como default para a impressão dos Contratos, Boletos e Recibos respectivamente.

**- Utilizar filtro do relatório antigo (delphi) na impressão do boleto:**

**- Permite a impressão de boletos não registrados:**  
Parâmetro responsável por controlar a impressão de boletos realizada diretamente no Educacional. Este parâmetro será usado para permitir ou não a impressão de boletos provenientes de convênios de cobrança registrada mas que ainda não tenham sido registrados nos bancos.  
Se esta opção estiver ***marcada*** o sistema irá permitir que todos os boletos sejam impressos, mesmo que os boletos sejam provenientes de convênios com cobrança registrada e que ainda não tenham sido registrados nos bancos e, para estes casos, antes da impressão será exibida uma mensagem alertando sobre esta situação. Se esta opção estiver ***desmarcada***, o sistema permitirá a impressão somente dos boletos que estiverem devidamente registrados nos bancos e, caso ainda não tenham sido registrados, será exibida uma mensagem informando a situação dos boletos.
