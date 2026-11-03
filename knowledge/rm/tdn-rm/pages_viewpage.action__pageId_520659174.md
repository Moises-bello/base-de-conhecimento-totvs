---
content_hash: 511deb94dda8e0020ee8a2d5b51066a3bb0fa4d7eb7626fab5bf9cfc2e4cf20c
fetched_at: '2026-06-29T00:10:30.971868+00:00'
page_id: '520659174'
product: rm
source: tdn-rm
title: Contrato de Locação - Dados Gerais - Identificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520659174
version: 25
---

---

false

🔹 **Contrato Locação (código)**

Campo de preenchimento automático do sistema. Este campo não pode ser editado.

🔹 **Número Contrato Locação**

Permite inserir o número do Contrato de Locação registrado pelo cliente. Este campo pode ser editado em Contratos de Locação que estejam na situação **“Elaboração”** e **“Efetivado”**.

🔹 **Data Contrato**

Campo informativo, onde o usuário pode inserir a data de assinatura do contrato.

🔹 **Modelo de Contrato**

O código do modelo de contrato é responsável por trazer alguns padrões para o cadastro do aluguel.

🔹 **Identificação**

Possibilita configurar **Regras de Vencimento**, **Parâmetros de Integração Financeira**, **Eventos Financeiros** e **Tipo de Locação**.

🔹 **Dados Reajuste**

São configuradas as regras de reajuste que podem ser aplicadas a este contrato.

🔹 **Dados de Rescisão**

São os dados que poderão ser parametrizados ao realizar a rescisão de um contrato.  
Importante destacar que nesta tela é possível configurar informações para **cálculos rescisórios por parte do locador**, como **Taxa Rescisória** e **Fórmula Rescisória**.

🔹 **Relatórios / DIMOB**

Permite informar relatórios para impressão das informações do contrato de locação e o campo **Informação para DIMOB**, onde poderá ser utilizada uma fórmula para compor o **Valor Bruto** do arquivo.  
Para mais informações, acesse: [Relatórios - DIMOB](https://tdn.totvs.com.br/pages/viewpage.action?pageId=435105161)

⚠️ **Observação**

É possível copiar modelos de contratos para uma nova coligada utilizando a funcionalidade **“Cópia de Dados”**.  
(Disponível a partir da versão **12.1.2506**)

---

📆 **Regra de Vencimento**

Define a regra utilizada na geração das parcelas do Contrato de Locação.  
A data de vencimento da **primeira parcela** não utiliza esta regra, pois é definida pelo usuário.  
Em cada regra de vencimento é possível configurar o **dia do vencimento**, se é **dia fixo ou dia útil**, entre outras opções.  
Para mais informações sobre este cadastro, acesse aqui.

💳 **Tipo Pagamento**

Pode ser: **Vincendo**, **Vencido** ou **Personalizado**.

📅 **1º Vencimento Em**

Campo habilitado apenas quando o **Tipo Pagamento** estiver definido como **Personalizado**.  
Permite definir a data de vencimento da primeira parcela do contrato.  
Essa data impacta diretamente nas demais parcelas, que serão geradas de forma subsequente conforme a regra de vencimento.

false

📌 **Início Vigência**

Determina o início de vigência do Contrato de Locação.  
Este campo é utilizado para validações de processos como **Reajuste, Aditivos e Escalonamento**, que devem estar entre a data de início e fim da vigência.

📌 **Final Vigência**

Campo obrigatório por padrão.  
Porém, ao marcar o parâmetro **“Permite o Contrato de Locação ter prazo indeterminado”**  
(Caminho: *Parâmetros TOTVS Incorporação >> Aluguel >> Contrato de Locação*), este campo deixa de ser obrigatório.

Quando não preenchido, o contrato passa a ter **Prazo Indeterminado**, não sendo permitido:  
• Contabilizar por período do contrato  
• Contabilizar por linearização  
• Efetivar aditivo de prorrogação

📌 **Início da Locação**

Define o início da locação, a partir do qual serão geradas as parcelas e, consequentemente, os lançamentos financeiros do contrato.

📌 **Prorrogação Vigência**

Caso exista um aditivo de prorrogação efetivado, este campo será preenchido com a data correspondente.

📌 **Fim do Primeiro Período**

Define o fim da primeira competência de locação, impactando diretamente os demais períodos.

🔎 **Exemplos**

• Início da locação: **16/05** | Fim do 1º período: **31/05**  
→ 1ª competência: 16/05 a 31/05  
→ 2ª competência: 01/06 a 30/06  
→ 3ª competência: 01/07 a 31/07

• Início da locação: **16/05** | Fim do 1º período: **10/06**  
→ 1ª competência: 16/05 a 10/06  
→ 2ª competência: 11/06 a 10/07  
→ 3ª competência: 11/07 a 10/08

📌 **Dias de Carência**

Define a quantidade de dias em que o primeiro período de locação será deslocado.

🔎 **Exemplos**

• Início da locação: 10/01/2018 | Carência: 31 dias  
→ Início da primeira locação: 10/02/2018

• Início da locação: 10/01/2018 | Carência: 75 dias  
→ Início da primeira locação: 26/03/2018

⚠️ Os campos **Fim do Primeiro Período**, **Dias de Carência** e **Início da Locação (Período)** possuem influência direta entre si.

📌 **Data da Próxima Revisão**

Data em que pode ser solicitada a revisão do contrato.  
Este campo pode ser editado mesmo em contratos efetivados.

false

💰 **Parâmetro de Integração Financeira**

Define qual parâmetro financeiro será associado ao contrato de locação.

💳 **Tipo de Evento Financeiro**

Define o evento financeiro que será associado ao contrato.

🏠 **Tipo de Locação**

Permite definir **Tipo de Locação**, **Tipo de Destinação**, **Tipo de Pagamento** e **Defaults Contábeis**.  
Para mais informações, clique aqui. [Cadastros - Tipo de Contrato de Locação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=435105420)

📁 **Número da Pasta**

Campo livre para informar a localização física do contrato.

📐 **Utiliza Cálculo Pro Rata**

Define se escalonamentos e aditivos serão calculados com **Pro Rata Dia**. [Contrato de Locação - Aditivos - Exemplos da aplicação do cálculo pro rata para aditivos](https://tdn.totvs.com.br/pages/viewpage.action?pageId=435105116)

false

🎯 **Tipo de Desconto**  
Este campo permite definir qual o tipo de desconto do Contrato de Locação. Possui as seguintes opções:

     🔹 **Desconto no valor final do Contrato:** Ao escolher essa opção, o valor inserido pelo usuário será descontado do valor final do Contrato de Locação;

     🔹 **Percentual:** Ao escolher essa opção, o valor inserido pelo usuário será descontado em percentual ao valor final do Contrato de Locação;

      🔹 **Desconto no valor do m²:** Ao escolher essa opção, o valor inserido pelo usuário será descontado no valor médio do m².   
            O valor final do contrato será impactado, pois é resultado do (Valor médio do m² \* Área Locada).

⚠️ **Observação**

Esse tipo de desconto só pode ser aplicado em Contrato de Locação que possua imóveis do tipo **"Áreas Fracionadas"** ou **"Áreas Unificadas"**. Dessa forma, se escolhido esse tipo de desconto, não será possível incluir imóvel do tipo **"Imóvel"**.

💲 **Valor desconto**

Permite o usuário inserir o valor de desconto desejado. Esse campo somente é habilitado quando é selecionado no **"Tipo de Desconto"** as opções **"Desconto no valor final do Contrato"** ou **"Desconto no valor do m²"**;

📊 **% desconto**

Permite o usuário inserir o valor em percentual do desconto no valor final do contrato. Esse campo somente é habilitado quando é selecionado no **"Tipo de Desconto"** a opção **"Percentual"**;

🔁 **Aplica reajuste no desconto**

Define se o valor do desconto será reajustado conforme a variação do reajuste do Contrato de Locação. Este campo só é habilitado quando é selecionado no **"Tipo de Desconto"** as opções **"Desconto no valor final do Contrato"** ou **"Desconto no valor do m²"**.

false

💰 **Valor do Contrato**

Este campo exibe o resultado do somatório dos valores dos imóveis associados ao Contrato de Locação;

💵 **Valor Final**

Este campo, por padrão, exibe o resultado do **Valor do Contrato - Valor do Desconto**. Pode exibir o resultado do cálculo da Fórmula inserida nos Parâmetros Gerais, que fica no seguinte caminho:  
**Parâmetros >> TOTVS Incorporação >> Aluguel >> Contrato de Locação >> Fórmula para cálculo do valor final do contrato de locação**.

false

🔄 **Situação do Contrato de Locação**

Exibe a situação do Contrato de Locação que ele se encontra, possuindo as seguintes situações:

📝 **Elaboração**;  
✅ **Efetivado**;  
❌ **Rescindido**;  
⏸️ **Suspenso**;  
🏁 **Encerrado**;  
🔐 **Em Aprovação**: Esta situação do contrato de locação será utilizada em workflows do **Fluig**. Toda edição no contrato estará barrada quando o contrato estiver nesta situação. Entretanto, o processo de efetivar o contrato de locação continuará disponível.

false

💼 **Taxas aplicadas ao contrato**  
As taxas são as mesmas informadas no Contrato de Administração, vinculado ao Contrato de Locação através da atribuição do mesmo Imóvel:

📌 **% Taxa de Administração**;  
📌 **Carência**;  
📌 **% Taxa de Intermediação**;  
📌 **Recorrência**.

💸 **Taxas de Repasse dos Encargos Financeiros**

As taxas são as mesmas informadas no Contrato de Administração, vinculado ao Contrato de Locação através da atribuição do mesmo Imóvel.

📈 **% de Juros**

Define que o valor de Juros calculado na parcela do aluguel terá o percentual informado direcionado ao lançamento financeiro de repasse (não o percentual do valor do lançamento financeiro de repasse);

📉 **% de Multa**

Define que o valor de Multa calculado na parcela do aluguel terá o percentual informado direcionado ao lançamento financeiro de repasse (não o percentual do valor do lançamento financeiro de repasse);

📊 **% de Desconto**

Define que o valor de Desconto calculado na parcela do aluguel terá o percentual informado direcionado ao lançamento financeiro de repasse (não o percentual do valor do lançamento financeiro de repasse).

falseMulta de atraso e Juros de mora

⏰ **Juros ao dia**

Pode ser informado em **Taxa (%)** ou **Valor**. Define o juros que será cobrado;

⚠️ **% Multa ao dia**

Define o percentual da multa que será cobrado por dia.

❗ **Observação**

Os valores de juros e multa definidos no Contrato de Locação têm prioridade em relação aos definidos no parâmetro do financeiro associado ao contrato.

falseChecklist de conclusão para efetivação

✅ **Checklist de Conclusão para Efetivação**

O checklist fornece um retorno visual das informações obrigatórias para efetivação do contrato, indicando o que já foi preenchido e o que ainda falta.

📌 Itens mínimos obrigatórios:  
• Identificação  
• Locatário  
• Garantia  
• Dados Reajuste  
• Imóveis  
• Fiador
