---
content_hash: da20dd130b04c0a97f7a153133150f339aa9e4b28778efc57f94b29ca3295877
fetched_at: '2026-06-29T00:09:21.052818+00:00'
page_id: '422545781'
product: rm
source: tdn-rm
title: Particularidades da NFC-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Particularidades+da+NFC-e
version: 5
---

Para o envio da NFC-e é obrigatório o preenchimento do Horário de Emissão do movimento. A opção "Exibir data e hora de criação do movimento" pode ser habilitada nos parâmetros do [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835) através da etapa Esta 4 - Movimento - Datas do tipo de movimento.  
Em relação a modalidade em contingência apenas estarão disponíveis os tipos **Contingência Offline FS-DA** e **Contingência Offline (NFC-e)**.  
***Observação:***Foi implementado uma maneira de enviar uma NFC-e após o tempo limite de 5 minutos.  
Os dados de envio da NFC-e será preenchida com a data de criação do movimento e a hora do momento do envio.  
É obrigatório a marcação da opção "Consumidor Final" disponível na aba Integrações | Fiscal do movimento do [TOTVS Gestão de Estoque, Compras e Faturamento](http://tdn.totvs.com/pages/viewpage.action?pageId=198948835). Este campo será preenchido na criação do movimento ou quando integrado com o [TOTVS Gestão Educacional](http://tdn.totvs.com/pages/viewpage.action?pageId=198948849). O preenchimento automático se aplicará apenas se tratando do Tipo de Documento 65-Nota Fiscal Eletrônica para Consumidor Final.

O indicador de presença do comprador no estabelecimento comercial no momento da operação, será preenchido em função do campo Operação Presencial da aba Fiscal do Movimento. Nos testes SEFAZ aceitou somente os valores abaixo para NFC-e. O sistema envia o valor que for informado no movimento, deixando a cargo da SEFAZ a validação.  
**"1" - Operação presencial**;  
**"4" - NFC-e em operação com entrega em domicílio**. 

Uma vez que a identificação do consumidor não é obrigatória e ainda pode ser identificado com CPF, CNPJ ou Identificação do Estrangeiro, foram criados os campos na aba Dados da NFC-e nas Integrações do movimento.  
Os novos campos servirão para o preenchimento dos Grupos de identificação do Destinatário e endereço do Destinatário, respeitando as seguintes regras:

* Os dois grupos serão **totalmente omitidos** na NFC-e quando o Cliente/Fornecedor selecionado no movimento for igual ao que estiver parametrizado como default no Tipo de Movimento e os novos campos criados (CPF/CNPJ/Id Estrangeiro e Nome estiverem vazios;
* Quando os novos campos criados (CPF/CNPJ/Doc. Estrangeiro Adquirente) estiverem preenchidos, gerarão, somente, as respectivas tags (CNPJ, CPF, Identificador do Estrangeiro e Nome). Neste caso deve ser criado um Cliente/Fornecedor "fictício" (CLIENTE BALCÃO) ´para ser informado no movimento uma vez que o campo é de preenchimento obrigatório;
* Se o Cliente/Fornecedor do movimento for diferente daquele informado como default no Tipo de Movimento, considera-se que o consumidor foi identificado no momento da operação e os dois grupos devem ser gerados por completo.

**Observações importantes:**

* O consumidor pode ser identificado apenas pelo CPF, CNPJ ou Identificador do Estrangeiro omitindo-se nome e endereço.
* O valor máximo para consumidor não identificado é de **R$ 10.000,00** (Dez Mil Reais), ao contrário, acima desse valor o consumidor deve ser identificado obrigatoriamente.
* No caso de emissão de NFC-e com Operação Presencial igual à "NFC-e em Operação com entrega em domicílio", independentemente do valor da operação, é obrigatória a identificação do destinatário, do endereço de entrega e do Transportador.
* O Grupo de **Formas de Pagamento** será gerado de forma fixa **"99 – Outros"** e o valor do pagamento será o valor líquido do movimento. Já o **Grupo de Cartões** será omitido.
* Para a NFC-e, é vedada a informação do grupo das Formas de Pagamento e, para a NFC-e a obrigatoriedade é definida a critério da UF.

**Integração com TOTVS Gestão Educacional**

Pelo TOTVS Gestão Educacional, a NFC-e pode ser gerada tanto pelo Regime de Caixa quanto pelo Regime de Competência.

* **Regime de Caixa:**A geração do movimento NFC-e é realizada a partir do [Boleto](http://tdn.totvs.com/display/LRM/Boletos) criado através das parcelas de dentro do Contrato do Aluno, onde são gerados os lançamentos e boletos financeiros.

* **Regime de Competência:**No modelo de competência, o movimento é gerado a partir do [Contrato do aluno](http://tdn.totvs.com/pages/viewpage.action?pageId=425458693). O valor total do contrato é dividido pelo total de meses compreendidos pela competência definida no contrato.

Na geração do movimento o campo Operação Presencial será gravado com valor default "Operação Presencial".

**ICMS60 TAG pST:**Foi modificado o envio da NFC-e para permitir a geração da TAG pST quando o produto não incidir FECP

* **Se o valor** ICMSST > 0  **Então gera** vBCSTRet, pST, vICMSSTRet
* **Se**alíquota do FECP > 0   **Então gera**  vBCFCPSTRet, pFCPSTRet, vFCPSTRet

Caso a regra esteja parametrizada com  **"Tipo ICMS outros"**, **"Regra de ICMS com ST"**, **"Não soma no valor contábil"** e **"Movimento de saída"** as tags vão ser geradas da seguinte forma:  
>Na 4.00 não deve gerar nada, somente o CST e a origem. >Na 3.10 deverá gerar as tags de base e valores zerados.
