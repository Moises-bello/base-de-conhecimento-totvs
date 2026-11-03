---
content_hash: cc6d1d9d51f240b63bc75dbd35cfdc3cfc495bf814ac86f556f911dd402f7efe
fetched_at: '2026-06-29T00:09:46.568192+00:00'
page_id: '435104842'
product: rm
source: tdn-rm
title: Componentes - Componente de Seguro por Empreendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Componentes+-+Componente+de+Seguro+por+Empreendimento
version: 40
---

O componente **Seguro por Empreendimento** é responsável por permitir a criação da taxa de Seguro em um Contrato de Venda.

Ao inserir este componente na Modalidade de Venda ou nas Condições de Financiamento da Venda, o sistema apresenta os seguintes campos:

**Percentual Seguro por Empreendimento**: informe o percentual mensal do Seguro por Empreendimento que incidirá sobre a opção definida no campo **Tipo Base Cálculo Seguro**. Este campo é obrigatório;

**Início**: Informe a Data de Início do Cálculo do Seguro;

**Fim**: Informe a Data de Término do Cálculo do Seguro;

**Tipo Base Cálculo Seguro**: Informe sobre qual valor o sistema irá aplicar o percentual definido no campo **Percentual Seguro por Empreendimento** para calcular o valor deste Seguro. As opções são:

* **Seguro sobre o Saldo Devedor do Grupo:** o sistema irá considerar o somatório dos valores de todas as parcelas em aberto, em relação à data definida na execução da geração do Seguro, no Grupo no qual este Componente está inserido para calcular o valor do Seguro;
* **Seguro sobre o Saldo Devedor de todos os Grupos:** o sistema irá considerar o somatório dos valores de todas as parcelas em aberto, em **todos os Grupos**, em relação à data definida na execução da geração do Seguro;
* **Seguro sobre o Saldo Devedor do Grupo de Parcelas Vincendas:** o sistema irá considerar o somatório dos valores de **todas as parcelas vincendas**, ou seja **que vencerão** após a data definida na execução da geração do Seguro, **no Grupo** no qual este Componente está inserido para calcular o valor do Seguro, com esta parametrização as parcelas em aberto que estão vencidas, ou seja em atraso, não serão consideradas para a geração do Seguro;
* **Seguro sobre o Saldo Devedor de todos os Grupos de Parcelas Vincendas:** o sistema irá considerar o somatório dos valores de **todas as parcelas vincendas de todos os Grupos** em relação à data definida na execução da geração do Seguro para calcular o valor do Seguro;

O [Valor de Integração](https://tdn.totvs.com/pages/viewpage.action?pageId=435105443) deste Componente deve ser parametrizado com a Ação **Acrescenta**.

O processo para [Gerar Seguro Por Empreendimento](https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Processo+-+Gerar+Seguro+Por+Empreendimento) está disponível no menu de Processo da visão de Cadastro de Vendas e também na tela de edição da Venda.
