---
content_hash: dceb76c84223854e2abd13f983a46a3c5e91429b8bff17631edc58f72f0c2866
fetched_at: '2026-06-29T00:10:42.220460+00:00'
page_id: '546698343'
product: rm
source: tdn-rm
title: Fiscal - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546698343
version: 73
---

parametrosFiscal 1/2Parâmetros do sistema Ambiente | Parâmetros | TOTVS Educacional | Integração | Fiscal 1/2:

1
complete
**Utiliza Movimento por Competência:** indique se a geração de movimento será por competência marcando esse parâmetro

**- Data competência****:**deve ser indicado o local onde o sistema deverá verificar o período de competência contábil para a inclusão de movimento do contrato educacional.   
Este local pode ser no cadastro do 'Período Letivo', na 'Parametrização por Curso' ou no 'Contrato e Plano de Pagamento'. Dentro do cadastro do respectivo local aqui escolhido, será habilitada uma aba chamada "Movimento", onde deve ser informado o período de competência contábil, preenchendo-se o mês/ano da competência inicial e o mês/ano da competência final.

* **Período Letivo:**Dentro do cadastro do Período Letivo será habilitada uma aba chamada 'Contabilização', onde devemos informar o período de competência contábil, ou seja, o período em que os serviços serão prestados neste período letivo, preenchendo o mês/ano da competência inicial e o mês/ano da competência final.
* **Parametrização por Curso:**Dentro do cadastro da Parametrização por Curso será habilitada uma aba chamada 'Contabilização', onde devemos informar o período de competência contábil, ou seja, o período em que os serviços serão prestados para esta parametrização, preenchendo o mês/ano da competência inicial e o mês/ano da competência final.
* **Contrato e Plano de Pagamento:**Dentro dos cadastros do *Contrato* e do *Plano de Pagamento* será habilitada uma aba chamada 'Contabilização', sendo que escolhendo esta opção devemos informar o período de competência contábil em pelo menos um destes dois cadastros e o sistema irá proceder da seguinte forma:   
  - Quando selecionado a opção do Contrato e se o período de competência contábil for informado dentro do Plano de Pagamento, todo novo Contrato vinculado a este plano de pagamento receberá este mesmo período de competência como default  
  - No processo de matricula e inclusão de contrato, será possível alterar ou definir o período de competência contábil do movimento no contrato do aluno.

* Quando estiver parametrizado para buscar o período de competência do movimento no "Período letivo" ou "Parametrização por curso", caso seja informado na turma as duas datas(Inicial e Final) o sistema irá considerar o ***período de competência do movimento***  ***da turma,***sobrepondo qualquer outro período.
* Quando a parametrização estiver definida para buscar do "Contrato" o período de competência do movimento prevalecerá o informado no contrato, caso esse não seja informado que será considerado o *período de competência do movimento*  *da turma*

11
incomplete
**Utiliza data de competência do movimento com base na data de emissão:**

Ao marcar este parâmetro durante a geração do movimento, a **data de competência** será automaticamente definida com o mesmo valor da **data de emissão do movimento**. Nesse caso, a data considerada será a **data atual (data do sistema)** no momento da geração do movimento,

**Histórico:** Defina por meio de variáveis e também descrições o histórico para cada movimento gerado, informações que podem ser parametrizadas e inseridas para que sejam visualizadas após a geração do Movimento, para informações sobre as variáveis do movimento por competência [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=616234472), movimentos gerados por caixa [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=425458681)

3
incomplete
**Gerar um movimento para cada lançamento do boleto:**Marque essa opção para gerar movimentos para cada lançamento de boleto agrupado. 

4
incomplete
**Gerar movimento de parcela do tipo Adicional**: Marque essa opção para gerar movimento de parcelas do tipo Adicional.

5
incomplete
**Gerar movimento de****parcela do tipo Extra**: Marque essa opção para gerar movimento de parcelas do tipo Extra

6
incomplete
**Gerar um movimento para cada serviço do contrato**: Marque essa opção para gerar movimentos separados quando o contrato possui mais de um serviço.
Fiscal 2/2Parâmetros do sistema Ambiente | Parâmetros | TOTVS Educacional | Integração | Fiscal 2/2

**Valor do item de movimento:**Para a emissão da Nota Fiscal, a forma como o sistema irá calcular o valor do item de movimento deve ser indicado. Assim, o valor do Serviço, indicado no Item de movimento poderá ser calculado das seguintes maneiras:

* **Valor original**: Opção disponível para geração de movimentos por regime de caixa ou por regime de competência.   
  Neste caso, no item de movimento serão apresentados o 'Preço Unitário' com o valor correspondente ao valor original do serviço e o 'Valor do Item' com o valor deduzido dos descontos (descontos das parcelas + valor de bolsas incondicionais) e, neste acaso, o valor dos descontos serão destacados na aba Tributos e Valores, conforme parametrização do tipo de movimento utilizado.
* **Valor líquido educacional**: Opção disponível para geração de movimentos por regime de caixa ou por regime de competência.  
  Neste caso, no item de movimento tanto o 'Preço Unitário' como o 'Valor do Item' serão apresentados com o valor líquido (valor original – descontos das parcelas - valor de bolsas incondicionais) e, neste acaso, os descontos NÃO serão destacados na aba Tributos e Valores pois o valor do item já está abatido dos descontos.
* **Valor líquido (calculado por fórmula):** Opção disponível *somente* para geração de movimentos por regime de caixa.

Neste caso, o valor do item de movimento será calculado por fórmulas que deverão ser criadas para contemplar regras específicas de cada empresa. Estas fórmulas deverão ser criadas no *TOTVS Gestão Financeira* e associadas posteriormente aqui nos parâmetros do *TOTVS Educacional | Integração | Fiscal 2/2*.

O valor processado pela fórmula irá compor o valor do item do movimento representado como valor líquido, portanto o valor de desconto no item de movimento NÃO será preenchido.  
O valor processado pela fórmula para a composição do valor do item de movimento será de responsabilidade de cada empresa. Haverá, no entanto, a seguinte validação: *o valor líquido calculado pela fórmula não poderá ser maior que o valor líquido calculado pelo Educacional*. O valor líquido calculado pelo educacional é igual ao Valor da parcela - Descontos de bolsa incondicional - Descontos concedidos na parcela. Como o sistema sempre fará esta validação entre o valor calculado pela fórmula com o valor calculado pelo educacional, todas as parametrizações referentes a descontos de bolsa que impactam ou não na geração do movimento devem ser mantidas para que esta regra possa ser corretamente aplicada.   
Se na tela do processo de geração de movimento a opção *"Gerar movimentos para boletos de valor líquido igual a zero"* estiver marcada, o sistema permitirá a geração de movimentos em que a fórmula executada retorne valor igual a zero.

Ao selecionar a opção *'Valor líquido (calculado por fórmula)',* serão habilitados dois campos à seguir para associação das fórmulas criadas que serão utilizadas para calcular o valor líquido que irá compor o valor do item de movimento:

10
incomplete
**Aplicar sobre lançamentos**: O preenchimento da fórmula neste primeiro campo é obrigatório e será executada sempre que os boletos indicados para a geração de movimentos estiverem **em aberto** ou **baixados parcialmente**. Esta formula será executada sobre o contexto do lançamento financeiro (FLAN).  
  

8
incomplete
**Aplicar sobre lançamentos baixados:** A fórmula indicada neste segundo campo será utilizada sempre que os boletos indicados para a geração de movimentos estiverem **baixados**. Esta formula será executada sobre o contexto dos itens de baixa do lançamento (FLANBAIXA). Este segundo campo não é de preenchimento obrigatório e, caso não esteja preenchido, o sistema irá utilizar a fórmula associada no primeiro campo para calcular também o valor líquido de boletos baixados.   
  

Como as fórmulas são criadas pelo próprio usuário é importante que na sua codificação sejam observados os seguintes pontos:  
- O lançamento financeiro pode contemplar valores eventualmente aproveitados da conta corrente do aluno;  
- O lançamento financeiro pode estar baixado parcialmente;   
- Na geração dos movimentos, os descontos nos lançamentos que estiverem em aberto e que forem calculados pela função de fórmula "VALORLIQUIDO" levarão em consideração para o cálculo, a data de execução da geração do movimento e acreditamos que isso possa impactar no cálculo do valor liquido, cabendo ao cliente avaliar o cenário e adequar as fórmulas para cálculo do valor líquido.  
- O processo de geração de movimento sempre gera um único movimento para cada lançamento, então, mesmo que o lançamento tenha sido baixado parcialmente ou que possua vários itens de baixa, somente um movimento será gerado para este lançamento, ou seja, ao ser solicitada a geração de movimento para um boleto que faz parte de um lançamento que já possui movimento gerado anteriormente para algum dos seus boletos, o sistema vai **'regerar'** o movimento já criado considerando as informações do lançamento. O sistema não incluirá um novo movimento para cada boleto.

9
incomplete


**Usar campo dedução para informar valor de desconto no item de movimento**   
Com essa opção *marcada*, os valores de bolsas incondicionais e descontos de parcelas passarão a preencher o campo *"Percentual deduzido"* ao invés de preencherem o campo de Desconto incondicional do item de movimento. Essa opção é válida tanto para  quanto para . Caso o parâmetro esteja *desmarcado*, o sistema continuará gravando os valores de bolsas e descontos incondicionais no respectivo campo de desconto incondicional do item de movimento. (Campo: TITMMOV.VALORDESC)  
  
Caso o parâmetro esteja *marcado*, na tela de geração de movimentos o campo "Tipo de Movimento" listará os tipos de movimentos onde o parâmetro "Dedução" no tipo de movimento tiver o valor *"Usa Percentual", "Usa Valor" ou "Ambos".* Esse parâmetro fica disponível em "*TOTVS Gestão de Estoque, Compras e Faturamento -> Ambiente -> Parâmetros -> Gestão de Estoque, Compras e Faturamento -> Vendas -> Tipo de Movimento XXXX -> Item – Valores Financeiros 2/2*".  
No item de movimento do movimento gerado, o campo *será* exibido como **"Percentual de Dedução"** ou em **"Valor de Dedução"** com os valores de bolsas incondicionais e descontos em relação ao preço unitário. Esse campo fica na aba *"Tributos e Valores"* do item de movimento. No movimento gerado, o campo *"Dedução de ISS"* estará preenchido pelo somatório dos valores deduzidos dos tipos de movimentos. Esse campo fica na aba *Integrações |* *"Fiscal"* do movimento.  
Caso o parâmetro esteja *desmarcado*, o sistema continuará gravando os valores de bolsas e descontos incondicionais no respectivo campo de desconto incondicional do item de movimento. (Campo: TITMMOV.VALORDESC) 

ATENÇÃO

Esse parâmetro na integração  não estará disponível. Já que no SigaFat do Protheus o valor de dedução é utilizado no pedido de compra.  E não no pedido de venda pela mensagem Order. Lembramos que o TOTVS Educacional envia pedido de venda para o SigaFat.

**Forma de Pagamento Padrão (Lançamentos Não Baixados)**

Define um meio de pagamento padrão (ex: Boleto) para preencher a tag obrigatória da NFS-e quando a nota é gerada a partir de lançamentos **em aberto**. Garante a autorização da nota antes da liquidação financeira; para lançamentos já baixados, o sistema ignora este campo e utiliza a baixa real.

**Regra Tributária para Geração de Movimento**

Parâmetro mandatório para adequação à **Reforma Tributária**. Vincula o movimento gerado às configurações de cálculo do **IBS** e **CBS**, assegurando a correta tributação e a rastreabilidade necessária para o futuro processamento.
