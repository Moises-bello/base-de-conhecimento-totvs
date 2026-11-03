---
content_hash: 067ca42f140cdb8bd4dd42fefaa6615a622dd58953ff728435a6f380850e50ee
fetched_at: '2026-06-29T00:10:59.153096+00:00'
page_id: '611627231'
product: rm
source: tdn-rm
title: Configuração - TOTVS Pagamento Instantâneo/Digital
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=611627231
version: 19
---

### **01. VISÃO GERAL**

Define as configurações gerais da integração com o TOTVS Pagamento Instantâneo, para cobrança via PIX.

### **02. PARAMETRIZAÇÃO**

Aba 'Credenciais':

* Solução de Pagamento

Define qual a solução a ser utilizada no sistema definido pelo contrato com a TechFin: TOTVS Pagamento Instantâneo (TPI) ou TOTVS Pagamento Digital (TPD).

* Dias após pagamento para gerar extrato de tarifa:

Define uma quantidade de dias a ser incrementada na data de pagamento e o resultado será a data do extrato de tarifa.

**Obs.: Parametrização disponível apenas para a solução de pagamento TOTVS Pagamento Digital (TPD)**

* Tenant

Define o nome da tenant gerada para acesso ao TOTVS Pagamento Instantâneo.

(Nome da instituição no link do RAAS)

* Usuário

Mesmo usuário de acesso ao portal do RAAS

* Senha

Deve ser a mesma senha do usuário de acesso ao portal do RASS

Aba 'Baixa (Previsão)/Conciliação (Liquidação)':

Conta/Caixa (**Se a solução escolhida for 'TOTVS Pagamento Digital (TPD)', este campo ficará desabilitado para alteração e será considerada a mesma Conta/Caixa utilizada na conciliação (liquidação)**)

Define a conta/caixa usada na baixa dos boletos. Esta é uma conta transitória criada apenas no sistema TOTVS, e não deve possuir vínculo bancário.

**Importante**:A partir dos patchs 12.1.2502.230, 12.1.2506.179 e 12.1.2510.112 da BibliotecaRM o sistema dispõe do tratamento de múltiplas chave PIX. Considerando que o TPI/TPD só permite utilizar uma conta bancária, agora o sistema permite trabalhar com várias contas, podendo utilizar a chave PIX que for informada na [aba 'TOTVS Pagamento Instantâneo' da conta/caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388837#ContaCaixa--669937268) associada no lançamento financeiro. Vale ressaltar que mesmo que, por default, a conta/caixa informada neste campo seja utilizada no item de baixa do lançamento baixado via PIX, será considerada a chave PIX que for informada na aba 'TOTVS Pagamento Instantâneo' da conta/caixa associada no lançamento financeiro.

* Meio de Pagamento

Define o meio de pagamento usado na baixa dos boletos.

* Taxa

Define a taxa, valor ou percentual, a ser cobrada por cada transação, conforme taxa contratada com o banco.

Conciliação (Liquidação):

* Conta/Caixa:

Define a conta/caixa a ser utilizada na conciliação dos recebimentos referente as transações.

Esta conta é a efetiva onde receberão os repasses, e deve ser necessariamente a mesma informada pelo representante legal no momento da abertura de conta com o Banco parceiro.

* Evento Contábil:

Define o evento contábil utilizado na geração do extrato de saque transferência na conciliação, caso a instituição trabalhe com evento.

Informações Complementares

* Na configuração da unidade de negócio no portal TOTVS Pagamento Instantâneo, o identificador do sistema externo deve ser informado da seguinte forma {CodColigada} ou {CodColigada-CodFilial} conforme seja feita a parametrização no TOTVS Gestão Financeira. **Exemplo**: 1 (caso tenha parametrizado para a coligada 1) ou 1-1 (caso tenha parametrizado para coligada 1 e filial 1.
* Na configuração do ponto de venda (virtual) no portal do TOTVS Pagamento Instantâneo, o identificador externo deve ser 01.
* Caso seja efetuada uma baixa utilizando o meio de pagamento PIX em um final de semana ou em um feriado, o processo de conciliação (solução **TPI**) gera o extrato de transferência da conta transitória para a conta efetiva com a data do **próximo dia útil**. Quando ocorrer com uma solução **TPD**, como não há contas transitórias, o extrato será gerado com a mesma data, porém, com a **data de compensação no próximo dia útil**.

[Documentação do TOTVS Pagamentos](https://tdn.totvs.com/display/public/TPD/TOTVS+Pagamentos)
