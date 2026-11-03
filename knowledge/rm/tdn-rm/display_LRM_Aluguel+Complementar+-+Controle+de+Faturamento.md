---
content_hash: 186666b7afb562e79fe581c20242224c4678e0257710d8491951ed51b68f8716
fetched_at: '2026-06-29T00:10:31.025702+00:00'
page_id: '520659292'
product: rm
source: tdn-rm
title: Aluguel Complementar - Controle de Faturamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Aluguel+Complementar+-+Controle+de+Faturamento
version: 12
---

---

false

## ⚠️ IMPORTANTE

A partir da **Versão 12.1.2506**, os parâmetros necessários para a geração do aluguel complementar nos cenários abaixo foram migrados diretamente para as **[**Faixas de Faturamento**.](https://tdn.totvs.com/pages/viewpage.action?pageId=874192688)**

## 🔹 Finalidade do Anexo

Este anexo tem como função registrar as medições do faturamento do Locatário, para que sirva de insumo para o **Aluguel por Faturamento**.  
Para usar os recursos de medições, é necessário que tenham cadastradas também as informações de **Aluguel Complementar**, pois **Aluguel Complementar** e **Medições** são informações utilizadas para a geração de Aluguel Complementar.

---

## 🔹 Campos exibidos ao incluir um registro

Ao incluir um registro nesse anexo, são exibidos os seguintes campos:

⚙️ **Código da medição**  
Campo de identificação da medição, preenchido automaticamente pelo sistema.

⚙️ **Situação**  
Este campo exibe a situação da medição. Podem ser exibidos os seguintes valores:

* **Pendente**: Será exibida essa situação quando a medição não tiver gerado um lançamento financeiro.
* **Integrada**: Será exibida essa situação quando a medição tiver gerado um lançamento financeiro.

⚙️ **Data/Hora de criação**  
Exibe a data e hora da criação do registro no sistema.

⚙️ **Contrato locação**  
Exibe o Contrato de Locação que a Medição está associada.

⚙️ **Data de medição**  
Exibe a data a qual foi realizada a medição cadastrada.

⚙️ **Competência de cobrança**  
Mostra a qual Mês/Ano será cobrado a medição.  
O sistema não permite cadastrar mais de uma medição para a mesma competência.

⚙️ **Data de vencimento**  
Data calculada pelo sistema para o vencimento do lançamento a ser gerado. O valor da data é obtido através da Regra de Vencimento indicada no Contrato de locação.

⚙️ **Valor do faturamento**  
Possibilita o usuário inserir o valor de faturamento do Locatário.

⚙️ **Valor do bomboniere**  
Possibilita o usuário inserir o valor de faturamento do bomboniere quando um contrato é do tipo Cinema.

⚙️ **Valor do aluguel utilizado no cálculo**  
Exibe o valor do aluguel relativo à competência indicada na Medição. Este campo será preenchido automaticamente no momento do cálculo do aluguel complementar (ao executar o processo **"Gerar Aluguel Complementar"** e selecionar a medição em questão).  
O valor utilizado poderá ser o valor de aluguel padrão, mas este valor poderá ser alterado dependendo das operações feitas no contrato, por exemplo, caso exista um escalonamento para a mesma competência do faturamento, então será considerado o valor do escalonamento. Além disso, aditivos, reajustes e aluguel em dobro também podem influenciar neste valor.

⚙️ **Percentual do faturamento**  
Exibe o percentual de faturamento de acordo com o que foi registrado no cadastro de Aluguel Complementar.

⚙️ **Valor Bruto do faturamento**  
Permite registrar o valor total da receita gerada por esses contratos, mas apenas para contratos específicos determinados pela equipe de gerenciamento de vendas do Shopping.  
Ao marcar a opção **"Informar valor bruto faturamento"** no menu **"Aluguel complementar"** durante a edição do contrato, o campo será exibido ao incluir uma medição diária.  
Este campo é informativo, não sendo possível a utilização de fórmulas.

⚙️ **Percentual do bomboniere**  
Exibe o percentual de faturamento do bomboniere de acordo com o que foi registrado no cadastro de Aluguel Complementar.

⚙️ **Código do evento**  
Exibe o Evento Financeiro utilizado para a geração do lançamento financeiro. Esse campo é preenchido quando a medição é integrada.

false

📌 **Observação**  
Clicando no link do Evento Financeiro, o usuário poderá visualizar a memória de cálculo do Aluguel Complementar gerado, com todo o detalhamento necessário para o entendimento do cálculo.

⚙️ **Ref. Lançamento**  
Exibe o lançamento vinculado à medição. Esse campo é preenchido quando a medição é integrada.

---

## 🔹 Geração do Aluguel Complementar

Após o preenchimento de uma medição, é possível gerar o Aluguel Complementar.  
Para isso, basta acessar o menu **Aluguel | Contrato de Locação | Gerar Aluguel Complementar** ou então o menu **Aluguel | botão Gerar Aluguel Complementar**.

---

## 🔹 Regeração do lançamento

Em caso de necessidade de regerar o lançamento do aluguel complementar com novos dados, o usuário deverá acessar o cadastro de **Medição**, alterar qualquer campo editável na tela conforme desejado e salvar.

O sistema irá solicitar uma confirmação de regeração do lançamento. Após a confirmação, o lançamento antigo será cancelado e excluído, e o novo lançamento será criado e vinculado à medição.

⚠️ Este procedimento não é possível de ser realizado quando o lançamento estiver baixado.

---

🔹 **Cancelamento do Aluguel Complementar**

Para cancelar o lançamento do aluguel complementar, basta utilizar o processo [**Cancelar Aluguel Complementar**.](https://tdn.totvs.com/display/LRM/Aluguel+Complementar+-+Cancelar+Aluguel+Complementar)

## 🔹 Obtenção do percentual do faturamento

O percentual do faturamento é obtido pelas **faixas de faturamento** cadastradas no contrato de locação após o sistema detectar qualquer alteração no valor de faturamento informado na medição.

O percentual é obtido seguindo os critérios abaixo:

* A data da medição informada deverá estar entre as datas de início e fim da faixa.
* O valor do faturamento deverá estar entre os valores iniciais e finais da faixa.
* Ao aplicar o reajuste em um período onde já exista uma medição com lançamento gerado, o sistema irá regerar o lançamento do aluguel complementar utilizando o valor do aluguel reajustado para o cálculo.

---

## 🔹 Contratos rescindidos ou distratados

Para contratos rescindidos ou distratados, será possível inserir medições, contanto que sejam cadastradas em períodos que compreendam o tempo de vigência do contrato de locação.
