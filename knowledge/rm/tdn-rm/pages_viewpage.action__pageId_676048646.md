---
content_hash: 96a2c039ed6f69f6f33821aed13a372a9939d574023afb90879c5de8d8098017
fetched_at: '2026-06-29T00:11:17.052228+00:00'
page_id: '676048646'
product: rm
source: tdn-rm
title: Fundo Promocional - Anexos - Cobrança em Dobro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676048646
version: 7
---

### **Introdução**

---

O anexo de cobrança em dobro permite criar cadastros que irão definir as cobranças em dobro de determinado fundo promocional.

### **Procedimentos para utilização**

---

Este cadastro pode ser associado a um template de fundo e suas configurações irão afetar todos os contratos associados neste template.

Os campos deste cadastro são:

* **Competência**: Esse campo determina qual a competência inicial que será aplicado o Aluguel em Dobro no Contrato de Locação.
* **Percentual:** Esse campo determina qual o percentual de cobrança em cima do valor de locação. Não é permitido inserir valor igual ou menor que 0 porém, podemos inserir valores que ultrapassem os 100% ao critério do usuário.
* **Parcelas**: Em quantas parcelas a cobrança o fundo promocional em dobro será dividido;
* **Data Inicial:** Determina qual o mês/ano, será o inicio de vigência do parâmetro cadastrado. Pode ser editado para qualquer data desejada. Campo obrigatório;
* **Data Final:** Determina qual o mês/ano, será o final de vigência do parâmetro cadastrado. Pode ser editado para qualquer data desejada.

**Observação:**

* Neste cadastro é possível cadastrar mais de uma competência por Contrato de Locação, entretanto, a mesma competência só pode ser definida quando houverem períodos diferentes de data inicial e data final. O sistema não permitirá duas competências iguais onde as datas iniciais ou finais coincidam.
* O valor do fundo em dobro será gerado através de um valor de integração. Este valor de integração deverá ser cadastrado obrigatoriamente no tipo de evento de fundo promocional do Template de fundo, no "Campo Integração". O Campo integração (Subtrai) não será utilizado para este cálculo caso também seja cadastrado.

#### **Geração não agregada (Disponível a partir da versão 12.1.2502)**

---

Com a opção de geração não agregada, o sistema gerará lançamentos separados de fundo em dobro, durante o processo de geração de lançamentos.

Esta separação além de permitir um controle mais detalhado de cada parcela gerada em dobro, permite que sejam utilizados parâmetros financeiros distintos, possibilitando então realizar rateios de centro de custo / naturezas orçamentárias financeiras diferentes do lançamento original.

Todos os lançamentos em dobro gerados dessa forma, passam a compor um novo evento financeiro que abriga todos os registros gerados pelo processo.

* É importante notar que apesar do cadastro ser flexível, não deve ser utilizado gerações hibridas, ou seja, em determinada competência não agregada e em outra competência, agregada. Recomendamos que siga o mesmo padrão para todas as competências onde deve incidir cobrança em dobro.
* No processo de cancelamento de lançamento financeiros, além da exclusão das parcelas do fundo promocional, o sistema irá automaticamente também excluir as parcelas do evento financeiro gerado para o processo de fundo em dobro, desde que estejam dentro do período escolhido para cancelamento.
* Não será possível cancelar através do processo quando um dos lançamentos (Origem ou Em Dobro) esteja com o status igual a "Baixado" ou "Baixado Parcialmente". O cancelamento é sempre feito para as duas parcelas. Caso uma destas esteja, por algum motivo, bloqueada o sistema não prosseguirá com o cancelamento.

### **Gerando lançamentos com fundo em dobro**

---

Vamos utilizar um exemplo, onde cadastramos uma cobrança em dobro para um Template de fundo promocional, com os seguintes parâmetros:

* Competência: **Março**
* Percentual: **80%**
* Parcelas: **5**
* Data inicial **01/01/21 até 31/12/22**

Diante deste cenário, teremos cobrança em dobro, calculada por um percentual de 80% sobre o valor do fundo promocional.  
O valor de fundo promocional para este contrato é de R$ 1000,00. Logo, teremos uma cobrança de R$ 800,00 relacionada ao fundo em dobro.  
Esta cobrança em dobro será em 5 parcelas.   
Então, teremos este valor distribuído nos lançamentos de fundo, a partir da competência de 03/21 e nos quatro meses subsequentes em 2021.  
Da mesma forma, teremos também a cobrança em dobro a partir da competência de 03/22 e nos quatro meses subsequentes em 2022.

Após esta definição, deveremos gerar os lançamentos de aluguel através de *processos / gerar lançamentos* do contrato de aluguel.

Veja o efeito desta geração nas imagens abaixo:

Após a geração de lançamentos na competência 01/21 até 12/22, vamos verificar o evento de fundo promocional gerado, no menu *Aluguel / Evento Financeiro:*

Este evento é o evento do fundo promocional, que está atrelado ao contrato de locação 75. Este contrato está associado ao fundo promocional que fizemos a parametrização do aluguel em dobro.

Após isso, iremos consultar a aba *Parcelamento* e selecionar a parcela da competência onde parametrizamos o fundo em dobro, neste caso a competência do mês 3

Dentro desta parcela, vamos editar o lançamento financeiro correspondente, na aba *"Lançamentos financeiros da parcela"*

E neste lançamento, vamos clicar em *Valores, Valores de Integração*

Então neste caso a nossa primeira parcela de fundo promocional foi gerada no valor de R$ 160, devido ao seu parcelamento em 5 parcelas.

false160\*5 = 800,00  
800,00 = 80% de 1000,00 que é o valor cadastrado do fundo promocional para este contrato.

O restante das parcelas será incluída nas competências seguintes.

ImportanteQuando o Contrato de Locação associado ao template possui a opção "Considerar somente no faturamento" o fundo em dobro será gerado juntamente a cobrança complementar. Neste caso, todo o procedimento acima será refletido no lançamento de fundo promocional gerado no aluguel complementar.

### Cancelamento do fundo em dobro

---

* O cancelamento dos lançamentos de fundo promocional, inclusive seus valores de integração quando houver cobrança em dobro, será feito através do processo de *Cancelar Lançamentos* do contrato de aluguel
* Todos os lançamentos do fundo serão cancelados na mesma competência em que são cancelados os lançamentos do contrato de aluguel.
* Quando o Contrato de Locação associado ao template possui a opção "Considerar somente no faturamento" o fundo em dobro será cancelado  juntamente no processo de cancelamento de cobrança complementar.

### **Ajuste no Período de Cobrança em Dobro (Fundo Promocional)**

---

Esta atualização permite maior flexibilidade na alteração do período de vigência do anexo **Cobrança em Dobro**, mantendo a integridade dos dados financeiros já gerados.

#### **O que mudou?**

Agora é possível alterar as datas de início e fim da cobrança em dobro, desde que o novo período **englobe todas as parcelas já geradas** para aquele fundo. O sistema bloqueia alterações que deixariam parcelas "órfãs" fora do intervalo definido.

#### **Regras para Alteração de Datas**

Para garantir a consistência, o sistema valida o novo período com base nas parcelas existentes:

| **Ação** | **Condição para Sucesso** | **Mensagem de Bloqueio** |
| --- | --- | --- |
| **Alterar Data Inicial** | Deve ser **igual ou anterior** à data da primeira parcela gerada. | "Não é possível alterar o fundo em dobro, pois há parcelas geradas anteriores à data inicial informada." |
| **Alterar Data Final** | Deve ser **igual ou posterior** à data da última parcela gerada. | "Não é possível alterar o fundo em dobro, pois há parcelas geradas após a data final informada." |
| **Outros Campos / Exclusão** | Bloqueado se houver **qualquer** parcela já gerada. | "Não é possível alterar o fundo em dobro, pois existem parcelas geradas." |

### Exemplo Prático

Imagine um fundo que já possui parcelas geradas entre **01/03/2025** e **01/07/2025**:

* **Permitido:** Alterar a data inicial para 01/02/2025 (amplia o período).
* **Bloqueado:** Alterar a data inicial para 01/04/2025 (deixaria a parcela de março de fora).
* **Permitido:** Alterar a data final para 31/12/2025 (extende a cobrança).
* **Bloqueado:** Alterar a data final para 01/06/2025 (deixaria a parcela de julho de fora).

**Nota:** Se você precisar realizar uma alteração estrutural ou excluir um anexo que já possua parcelas, será necessário estornar/excluir as parcelas geradas antes de prosseguir.
