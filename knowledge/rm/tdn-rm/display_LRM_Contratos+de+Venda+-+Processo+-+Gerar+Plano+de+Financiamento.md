---
content_hash: 4cbd581672667e18f91ab2057b4a1eb65ea029ec62cdab96a50fca0c25b307f1
fetched_at: '2026-06-29T00:09:48.344935+00:00'
page_id: '435105128'
product: rm
source: tdn-rm
title: Contratos de Venda - Processo - Gerar Plano de Financiamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Processo+-+Gerar+Plano+de+Financiamento
version: 7
---

Esse processo é o responsável por gerar os Lançamentos Financeiros do Plano de Financiamento da Venda, conforme valores, quantidades e datas parametrizadas nas Condições de Financiamento da mesma.

Importante!

Caso durante a execução deste processo o sistema exiba a mensagem abaixo, é preciso habilitar o[***controle de histórico de alterações***](https://tdn.totvs.com/pages/viewpage.action?pageId=421388636) no módulo financeiro, para dar continuidade ao reajuste das vendas.

*Para executar o processo, o parâmetro [Habilitação do Controle de Histórico de Alterações de Lançamentos/Extratos de Caixa] deve estar configurado como [Habilita controle para todos os módulos] ou [Habilita controle somente para Totvs Incorporação].*

*O caminho para acessar e ajustar este parâmetro é:*  
*Módulo BackOffice > Gestão Financeira > Utilitários > Habilitação Histórico de Alterações*

Esta ação é necessária para garantir a consistência das informações no sistema.

Os lançamentos financeiros podem ser gerados Bloqueados ou Provisionado, conforme escolhido no parâmetro "Tipo de bloqueio venda", que se encontra no seguinte caminho: *Ambiente | Parâmetros | Totvs Incorporação | Integração Financeira | Bloqueio de lançamentos venda*.

Para desbloquear os lançamentos após o Contrato estiver efetivado, basta executar o processo "Desbloquear Lançamento Financeiro".  
Ao executar esse processo, será aberta a janela Gerar o Plano de Financiamento que possui as abas Plano de Financiamento, Componentes da Regra e Log.

**Plano de Financiamento:**  
Nesta aba exibe a simulação das parcelas do Plano de Financiamento, conforme realizado o cadastro das Condições da Venda.

**Componentes da Parcela:**  
Nesta aba exibe a simulação dos componentes da parcela do Plano de Financiamento, conforme realizado o cadastro das Condições da Venda.

**Log:**  
Nesta aba são exibidas as seguintes informações:

* **Cálculo:** Exibe informações sobre o cálculo do plano de financiamento, tais como:
  + Número total de vendas selecionadas
  + Número total de vendas processadas
  + Número de vendas com erros
  + Número de vendas com avisos
  + Tempo total de Cálculos, etc;
* **Erro:** Exibe as mensagens de erro da Geração do Plano de Financiamento;
* **Alertas**: Exibe as mensagens de alerta da Geração do Plano de Financiamento;

falseNa existência de componentes de Juros ou CM na regra do plano de financiamento, obrigatoriamente deve-se incluir um componente do Tipo Principal. Por exemplo (Mensal, Anual, Conclusão)... Isso se faz necessário, pois somente os componentes do tipo principal podem receber reajuste monetário. Os componentes do tipo entrada, como o Sinal, não sofrem reajuste, para alterar o valor do componente de Sinal basta realizar um reajuste de alteração de valor de parcela ou renegociação de contrato.false

Veja Também

---
