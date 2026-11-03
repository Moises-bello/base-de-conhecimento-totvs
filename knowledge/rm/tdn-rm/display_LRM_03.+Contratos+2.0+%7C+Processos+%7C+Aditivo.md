---
content_hash: cadbc87ff404b09721fe7796222df188bdbef3f40f1a3f8eaea7b4de6b3e0f45
fetched_at: '2026-06-29T00:12:09.030277+00:00'
page_id: '938330155'
product: rm
source: tdn-rm
title: 03. Contratos 2.0 | Processos | Aditivo
type: documentation
url: https://tdn.totvs.com/display/LRM/03.+Contratos+2.0+%7C+Processos+%7C+Aditivo
version: 22
---

AditivotrueGerar Aditivo

O processo de **Aditivo** do item de contrato tem como objetivo aditivar **valor**, **quantidade** ou **prazo** ao item de contrato, atualizando as parcelas conforme o tipo de aditivo realizado.

* Permitir aditivo dos seguintes tipos: Valor, Quantidade ou Prazo.
* Permitir selecionar vários itens de contrato para aditivos simultâneos.
* Atualizar automaticamente as parcelas com status diferente de Faturada ao aditivar a quantidade ou o valor do item de contrato, incluindo a previsão financeira, se houver.
* Desconsiderar parcelas associadas a medições para itens com tipo de faturamento por medição (quantidade ou valor).
* Executar o aditivo várias vezes para o mesmo item de contrato:

  + Nos aditivos de Valor ou Quantidade, os valores serão somados.
  + A soma não pode ser menor (para evitar valor negativo) nem igual ao valor ou quantidade original do item (para não zerar o valor).

##### **Permissões**

O processo Gerar Aditivo no Item conta com controle de segurança.  
O acesso precisa ser liberado por meio de permissão de perfil associada ao usuário.

##### **Parâmetros do Processo**

Parâmetros comuns a todos os tipos de aditivo:

| Campo | Descrição |
| --- | --- |
| Número | Número do aditivo. |
| Data de Assinatura | Data em que o aditivo foi assinado. |
| Justificativa | Descrição sobre o motivo do aditivo. |

---

processos\_faturamentolefttrueAditivo Valor

O Aditivo de Valor permite aditivar um valor fixo ou percentual sobre o valor (preço) do item de contrato.

Importante

O valor aditivado ou percentual aditivado é aplicado por unidade.  
No cenário em que um contrato está recebendo um aditivo de valor de R$ 50,00, e o item está definido com 4 unidades, as regras aplicadas conforme o tipo de contrato serão:

* **Item com faturamento Periódico:**  
  Cada parcela será acrescida de R$ 200,00 (R$ 50,00 × 4 unidades).
* **Item com faturamento por Medição de Quantidade:**  
  O valor de R$ 200,00 será distribuído entre as parcelas.

  + Se o item não possui medições, o valor é distribuído igualmente.
  + Se o item já possui medições, será considerado o saldo de quantidades não medidas para aplicação do aditivo.  
    Exemplo: se o saldo de quantidade não faturada for 3 unidades, o valor total do aditivo será R$ 150,00, distribuído nas parcelas não medidas.
* **Item com faturamento por Medição de Valor:**  
  Nesse tipo de item, a quantidade é fixa em 1.  
  O valor do aditivo aplicado será R$ 50,00, distribuído entre as parcelas que ainda não foram medidas.

##### **Parâmetros do Aditivo de Valor**

| Campo | Descrição |
| --- | --- |
| Data Início Vigência (somente para itens do tipo Periódico) | Data em que o aditivo passa a vigorar, utilizada como data de corte para definir quais parcelas serão aditivadas. Não se aplica para itens com faturamento por medição. |
| Efeito Aditivo | Indicar se o aditivo Diminui (subtrai) ou Aumenta (soma) o valor. |
| Valor | Valor a ser aditivado ao item de contrato. Ao preencher o campo "Valor", o campo "Percentual" será bloqueado. |
| Taxa Juros | Define a taxa de juros das parcelas que serão aditivadas  (válido somente para contratos de arrendamento mercantil) |
| Percentual | Percentual a ser aplicado ao item de contrato. Ao preencher o campo "Percentual", o campo "Valor" será bloqueado. Não disponível para contratos de natureza: Arrendamento Mercantil. |

##### **Observações**

* Ao realizar o aditivo de valor (por Valor ou Percentual), o campo Aditivo Valor (localizado no grupo "Valores do Item", aba "Identificação" do item de contrato) será preenchido com o valor utilizado no processo.

  + Em caso de percentual, o valor será calculado a partir do valor do item.
* O aditivo é acumulativo: a cada aditivo realizado, o campo Aditivo Valor acumula o somatório de todos os aditivos anteriores.
* É permitido aplicar quantos aditivos forem necessários, desde que o somatório dos reajustes não seja menor que o valor do item.
* Se houver parcelas com status Previsionado, a previsão financeira será atualizada com os novos valores das parcelas.
* Os campos do contrato Valor Contrato e Saldo Contrato serão atualizados com base no valor atual das parcelas.
* O campo do item do contrato Valor Parcela será atualizado conforme o valor da primeira parcela aditivada.
* O campo **Taxa de Juros** é opcional. Se preenchido, o valor deve ser maior que 0 e menor ou igual a 100. (Aplica-se apenas a contratos de arrendamento mercantil.)

##### **Fórmulas de Cálculo do Valor Total Aditivo**

→ **Quando o aditivo for em valor:**

* + **Item do tipo Periódico:**

    - O valor do aditivo será acrescido ou subtraído do valor da parcela, a partir da Data de Início de Vigência.
    - O valor total do aditivo será o valor informado na parametrização, multiplicado pela quantidade do item em cada parcela (quantidade original + aditivada).
  + **Item do tipo Medição:**

    - O valor do aditivo será acrescido ou subtraído do valor do item e distribuído entre as parcelas, a partir da primeira parcela não medida.
    - O valor total corresponderá ao saldo do item multiplicado pelo valor informado na parametrização.
    - Para contratos do tipo Medição Valor, o valor informado será aplicado diretamente, sem cálculos adicionais.

**→ Quando o aditivo for em percentual:**

* + **Item do tipo Periódico:**

    - O sistema obtém o valor do item na data de início de vigência do aditivo e aplica o percentual sobre esse valor.
    - Caso existam aditivos ou reajustes anteriores, o percentual será calculado sobre o valor vigente na data.
    - O valor original atualizado será calculado dividindo o valor da parcela pela quantidade do item.
    - O percentual será aplicado sobre esse valor unitário e, após o cálculo, somado ao valor da parcela.
  + **Item do tipo Medição:**

    - O percentual é aplicado sobre o valor do saldo do item (valor disponível).
    - Se houver aditivos anteriores, eles serão considerados no cálculo.

    Fórmula:

    ```
    Valor do Aditivo = Soma das parcelas disponíveis (saldo do item) × Percentual do aditivo
    ```

---

Aditivo Quantidade

O Aditivo de Quantidade permite aditivar uma quantidade ao campo "Quantidade" do item de contrato.  
Este tipo de aditivo só pode ser realizado em itens que tenham o tipo de faturamento Periódico ou Medição de Quantidade. 

Não disponível para contratos de Natureza: Arrendamento Mercantil e Medição Valor

##### **Parâmetros do Aditivo de Quantidade**

* Data Início Vigência:  
  Data em que o aditivo passa a vigorar, sendo utilizada nos itens de faturamento periódico como data de corte para definir quais parcelas serão ou não aditivadas.  
  *→ Observação:* Para itens que utilizam faturamento por medição, esta informação não é utilizada para determinar quais parcelas serão aditivadas.
* Efeito Aditivo:
  + Aumenta: O aditivo será somado à quantidade existente.
  + Diminui: O aditivo será subtraído da quantidade existente.
* Quantidade:  
  Quantidade que será aditivada ao campo "Quantidade", do grupo Valores do Item, na aba Identificação do item de contrato.  
  O campo Aditivo Quantidade será preenchido automaticamente.

##### **Funcionamento do Processo**

Ao realizar o aditivo de quantidade:

* O campo Aditivo Quantidade será atualizado com o valor utilizado na execução do processo.
* O aditivo é acumulativo, ou seja, a cada novo aditivo, o campo refletirá o somatório de todos os aditivos já realizados.
* É possível aplicar quantos aditivos forem necessários, desde que o somatório não reduza a quantidade total do item abaixo de zero.

##### **Atualizações no Contrato**

* Se existirem parcelas com status "Previsionado", a Previsão Financeira será atualizada com os novos valores das parcelas.
* Os campos Valor do Contrato e Saldo do Contrato serão atualizados com base no valor atual das parcelas.

##### **Atualizações no Item**

* O Valor Parcela será atualizado conforme o valor da primeira parcela aditivada.

##### Fórmula de Cálculo do Aditivo

O valor atualizado será obtido conforme os seguintes passos:

1. Obter o valor do item na data de início da vigência do aditivo.
2. Calcular o valor unitário:

   > Valor da Parcela ÷ Quantidade do Item.
3. Multiplicar o valor unitário pela quantidade aditivada.
4. Aplicar o efeito selecionado:

   * Aumenta: somar o valor calculado à parcela.
   * Diminui: subtrair o valor calculado da parcela.

> *Importante:* As quantidades aditivadas anteriormente não serão utilizadas no cálculo atual.

Importante

Caso o item tenha faturamento por medição de quantidade, ao invés do valor calculado para o aditivo ser somado em cada parcela, ele será distribuído entre as parcelas que ainda não foram medidas, uma vez que diferentemente do item com faturamento periódico onde é previsto a disponibilização daquela quantidade periodicamente, no de medição a quantidade contratada é a definida para a duração de todo o contrato.

Aditivo Prazo

O Aditivo de Prazo permite adicionar uma quantidade de parcelas ao item de contrato, aumentando o período de abrangência do contrato.

#### Parâmetros do Aditivo de Prazo:

Quantidade de Parcelas → Define a quantidade de parcelas que serão aditivadas nos itens selecionados.

Taxa Juros → Define a taxa de juros das parcelas que serão aditivadas. O preenchimento é opcional, mas, se informado, o valor deve ser maior que 0 e menor ou igual a 100. (Válido apenas para contratos de arrendamento mercantil.)

Novo Valor Parcela →  Campo que permite alterar o valor das novas parcelas que serão geradas no aditivo de prazo. Este campo fica disponível após marcar a opção "Definir valor para novas parcelas em itens periódicos?". **É importante ressaltar que esta opção só afeta parcelas de itens periódicos, então caso algum dos itens selecionados no contrato para gerar este aditivo seja de medição, este parâmetro será ignorado.**

#### Processo de Aditivo de Prazo

Ao realizar o processo de aditivo de prazo, novas parcelas são geradas e adicionadas ao item do contrato, respeitando as informações preenchidas na aba de Faturamento do item, como:

* Dia do Vencimento
* Periodicidade (desconsiderando o vencimento imediato)

Além disso, os detalhes das parcelas geradas seguem as seguintes regras:

* Item Periódico: O valor das parcelas geradas será equivalente ao valor da parcela atual (informação disponível na aba de identificação do item), com exceção as situações onde é informado o campo Novo Valor Parcela.
* Item de Medição: O valor será equivalente ao valor restante a ser medido, dividido entre as parcelas existentes e as novas parcelas adicionadas pelo aditivo de prazo.

#### Edição dos Vencimentos das Novas Parcelas

Os vencimentos das novas parcelas poderão ser editados, exceto nos seguintes casos:

* Item Periódico: Quando as parcelas já estiverem faturadas.
* Item de Medição: Quando as parcelas já tiverem sido medidas ou faturadas.

#### Atualizações ao Finalizar o Processo

Ao finalizar o processo, os seguintes campos serão atualizados:

**Visão do Item**:

* + Data Fim Vigência (Aditivo): Aparece na visão de identificação do item, com a data de vencimento da última parcela aditivada.
  + Aditivo de Parcelas: Aparece na visão de faturamento do item, com a informação do total de parcelas aditivadas.

**Valor Total**:

* + Item Periódico: O valor total será atualizado para incluir os valores das parcelas aditivadas.
  + Item de Medição: O valor permanece inalterado, já que o valor/quantidade não medido será rateado entre as parcelas livres e as novas parcelas proveniente do aditivo.

**Visão do Contrato**:

* + Data Fim Vigência (Aditivo): Aparece na visão de identificação do contrato, com a data de vencimento da última parcela aditivada em seus itens.
  + Valor do Contrato e Saldo do Contrato:

    - Item Periódico: O valor será atualizado para incluir as parcelas aditivadas.
    - Item de Medição: O valor e saldo do contrato permanecem inalterados.

#### Previsionamento Financeiro

O previsionamento financeiro (lançamento no módulo Gestão Financeira) não será realizado de forma automática para as parcelas aditivadas. Caso a empresa trabalhe com previsões financeiras para os contratos, será necessário executar o processo de Gerar Previsão Financeira no contrato para que os valores sejam atualizados.

### **Memória de Cálculo**

A memória de cálculo fornece detalhes sobre o processo de aditivo, incluindo os dados utilizados e os valores considerados. Seu objetivo é facilitar o entendimento sobre o que foi aplicado em cada aditivo.

Exemplo de Memória de Cálculo Registrada no Histórico:

| **Campo** | **Valor** |
| --- | --- |
| Contrato | 126 |
| Número Sequencial | 1 |
| Produto | 01.01 - Produto teste Um |

---

Datas do Processo

| **Campo** | **Valor** |
| --- | --- |
| Data/Hora do Processo | 09/08/2024 17:10 |
| Data de Assinatura | 09/08/2024 |

---

Parâmetros do Aditivo

| **Campo** | **Valor** |
| --- | --- |
| Número | 004 |
| Tipo de Aditivo | Prazo |
| Quantidade de Parcelas | [Informar quantidade] |
| Taxa de juros informada no processo | É informada ao executar o processo (Válido somente para contratos de arrendamento mercantil) |
| Taxa de juros obtida do item | Taxa de juros do item do contrato (Válido somente para contratos de arrendamento mercantil) |
| Justificativa | teste |
| Novo valor Parcela | Utilizado no aditivo de prazo para definir o valor das novas parcelas geradas. (Válido apenas para itens periódicos). |

---

Cálculo Detalhado do Aditivo

| **Campo** | **Valor** |
| --- | --- |
| Periodicidade | Mensal |
| Dia do Vencimento | 17 |
| Data de Vencimento da Última Parcela Existente | 17/05/2025 |
| Valor da Última Parcela Existente | R$ 8.631,39 |

---

Parcelas

| **Número da Parcela** | **Vencimento** | **Valor** |
| --- | --- | --- |
| 11 | 17/06/2025 | R$ 8.631,39 |
| 12 | 17/07/2025 | R$ 8.631,39 |
| 13 | 17/08/2025 | R$ 8.631,39 |
| 14 | 17/09/2025 | R$ 8.631,39 |
| 15 | 17/10/2025 | R$ 8.631,39 |

---

Item

| **Campo** | **Valor** |
| --- | --- |
| Aditivo de Parcelas Atualizado | de 5 para 10 |

Cancelar aditivo

Processo que possibilita o cancelamento do último aditivo realizado nos itens de contrato selecionados.

**Regras para Cancelamento de Aditivo**

* **Cancelamento de Aditivo de Quantidade e Valor**

Restrições por tipo de faturamento do item selecionado:

* + Faturamento Periódico: O cancelamento só será possível se nenhuma parcela, a partir da data de vigência do aditivo, tiver sido faturada.
  + Aditivo de Valor em Medição (Quantidade e Valor): O cancelamento retirará o valor calculado para o aditivo das parcelas que ainda não foram medidas. Se não houver saldo suficiente para isso, o cancelamento não será possível.
  + Aditivo de Quantidade em Medição de Quantidade: O cancelamento só será possível se houver saldo disponível para efetuar o cancelamento. Caso a quantidade aditiva tenha sido comprometida por alguma medição, o cancelamento não poderá ser realizado.
  + Parcelas com status Previsionado: Se o status da parcela for Previsionado, os valores da previsão serão ajustados conforme necessário.

---

* **Cancelamento de Aditivo de Prazo**

Restrições por tipo de faturamento do item selecionado:

* + Faturamento Periódico: O cancelamento só será possível se nenhuma parcela gerada pelo aditivo tiver sido faturada.
  + Faturamento por Medição (Quantidade e Valor): O cancelamento só será possível se nenhuma parcela gerada pelo aditivo tiver sido medida.
  + Parcelas Normais do Contrato: Se as parcelas normais do contrato estiverem medidas e, ao cancelar o aditivo de prazo, houver saldo a ser medido, mas não houver mais parcelas, uma nova parcela será adicionada. Esta nova parcela receberá como valor o que falta ser medido no item do contrato.

### **Efeitos do Cancelamento**

Atualização de Valores → Ao executar o cancelamento, os valores das parcelas, dos itens e do contrato selecionado serão atualizados conforme necessário.

Histórico de Aditivos → O registro do aditivo cancelado será removido do histórico de aditivo do item.

Histórico de Processos → O processo de cancelamento será gravado no histórico de processos.
