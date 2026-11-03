---
content_hash: b59ef5a2ae3b4679d4cb243e1a8668aeda77623b4e25f5dce4284ce891a0ff8a
fetched_at: '2026-06-29T00:09:47.053531+00:00'
page_id: '435104895'
product: rm
source: tdn-rm
title: Condomínio - Básicos - Cobrança por Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104895
version: 17
---

Este cadastro permite mapear as cobranças do condomínio baseadas no orçamento elaborado para a empresa.  
As informações desse cadastro serão utilizadas na apuração dos valores do condomínio durante o fechamento.

Na tela de cadastro da Cobrança por Orçamento possui os seguintes campos:

* **Código:** Campo de controle interno do sistema, preenchido automaticamente;
* **Descrição:** Campo de texto livre, com função de descrever o cadastro;
* **Cód. Item Cobrança:** Campo que associa um Item de Cobrança ao cadastro;
* **Tipo de Valor:** Campo que determina o tipo de Valor do Cadastro, podendo ser "Valor Orçado" ou "Valor realizado"
* **Modelo de cálculo de Rateio**: Para saber mais sobre os tipos de rateio, verifique o link abaixo.

### **Modelos de Rateio**

---

* [Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio Linear por Total de Subunidade da Unidade](https://tdn.totvs.com/pages/viewpage.action?pageId=435105215)
* [Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio Linear por Total de Subunidade por Empreendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105092)
* [Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio Linear por Total de Subunidades](https://tdn.totvs.com/pages/viewpage.action?pageId=435105093)
* [Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio por CRD](https://tdn.totvs.com/pages/viewpage.action?pageId=435105196)
* [Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio por Fração Ideal](https://tdn.totvs.com/pages/viewpage.action?pageId=435105183)
* [Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio por M² Construído](https://tdn.totvs.com/pages/viewpage.action?pageId=435105299)
* [Cobrança por Orçamento - Modelo de Cálculo de Rateio - Rateio por M² Locado](https://tdn.totvs.com/pages/viewpage.action?pageId=435105202)
* [Cobrança por Orçamento - Modelo de Cálculo de Rateio - Valor Fixo](https://tdn.totvs.com/pages/viewpage.action?pageId=435105104)

### **Cobrança por valor fixo da subunidade**

---

Quando a associação de cobrança por orçamento, além do seu cálculo principal definido através do modelo de rateio mostrado acima, possui tbm um anexo de valor fixo por subunidade, teremos um comportamento diferente na realização do cálculo do rateio do orçamento

Seguindo o exemplo abaixo, vamos cadastrar uma associação de cobrança por orçamento, cujo valor é fixo e replicado por subunidades.

Porém neste cadastro também temos no seu anexo um valor fixo para duas subunidades existentes.

Na aba cobrança fixa por subunidade, cadastrei as duas cobranças:

Agora ao fazer o meu fechamento de condomínio e selecionar o processo de orçamento o sistema irá deduzir o valor das subunidades e fará o rateio para as unidades restantes de acordo com o cálculo cadastrado.

No histórico de cálculo do fechamento, na memória de cálculo, temos o log deste nosso exemplo que exemplifica esta dedução:

*Cobrança por Orçamento: 1/Por Subunidade*  
*Associação: BH MALLS*  
*Período: 01/12/2000 - (sem data final)*  
*Tipo de Valor: Valor orçado*  
*Valor: R$5.000,00*  
*Item de Cobrança: 7/Por Subunidade*  
*Modelo de Rateio: Valor Fixo*

*Cobrança fixa:*  
*Quadra/Lote: FIXO/000001*  
*R$500,00*

*Cobrança fixa:*  
*Quadra/Lote: FIXO/000002*  
*R$1.000,00*

*Valor total das cobranças fixas: R$1.500,00*  
*Novo valor do orçamento a ser rateado:*  
*Orçamento - Valor total: R$5.000,00 - R$1.500,00 = R$3.500,00*

### **Anexos - Natureza Orçamentária/Financeira**

---

O orçamento classificado como "Despesa" no TOTVS Gestão de Estoques, Compras e Faturamento só pode ser associado à uma natureza orçamentária financeira do tipo "A Pagar" ou "Ambas".

Desta forma, para que o processo de Cobrança por Orçamento no módulo de Condomínio realize os cálculos para este Orçamento durante uma apuração, devemos consultar e cadastrar essa mesma Natureza "A Pagar" ou "Ambas" no anexo de Natureza Orçamentária Financeira presente em *Condomínio / Cobrança por Orçamento / Anexos / Natureza Orçamentária Financeira.*Não é possível associar Naturezas do tipo "A Receber" neste cadastro, visto que os Orçamentos de Condomínio devem ser sempre do tipo "Despesa".

Ao associar no cadastro de Cobrança por Orçamento a mesma Natureza cadastrada no Orçamento de Despesa do TOTVS Gestão de Estoques, Compras e Faturamento o sistema estará pronto para realizar este cálculo.

É importante também que, o Empreendimento que fará parte do cálculo do Orçamento possua o mesmo Centro de Custo cadastrado no Orçamento.

A Natureza Orçamentária "A Receber" deve ser associada ao Item de Cobrança associado a Cobrança por Orçamento. Neste Item de Cobrança só serão permitidas Naturezas do tipo "A Receber" visto que utilizamos esta Natureza para realizar os devidos rateios nos lançamentos a receber do Condomínio.

### **Cobrança por valor fixo da subunidade - Reajuste do contrato no fechamento do condomínio**

---

Quando existe uma ou várias subunidades com valores de cobrança fixa, associadas ao cadastro da cobrança por orçamento, o sistema passa a atualizar os valores desta cobrança fixa a partir do reajuste do condomínio.   
Desta forma, ao gerar o fechamento do orçamento, através do condomínio, estes valores reajustados irão incidir nestes cálculos, automaticamente.

Para entender como realizar este procedimento, primeiro, respeite as premissas abaixo

* **Contrato de Aluguel com reajuste de condomínio cadastrado**. Para saber como cadastrar um reajuste para o condomínio
* **Efetivar o reajuste do condomínio** através do processo **Aplicar Reajuste em Condomínio.** O link acima também possui um passo a passo de como efetivar este reajuste.
* **Para que o fechamento do condomínio reflita os valores reajustados, o mesmo precisa ser calculado na mesma competência do reajuste ou em competência superior.**

Exemplo básico de um cálculo de fechamento de condomínio onde o orçamento possui valores fixos por subunidade e estes valores reajustados irão refletir no cálculo.

**Condomínio reajustado na data 01/01/2019**

**Perceba o valor reajustado de R$ 995,60, resultado do reajuste na data 01/01/2019. Uma pequena deflação no valor.**

Agora, faremos o fechamento da competência do condomínio **02/2019**

Neste cenário, todas as cobranças fixas a partir desta data terão seus valores reajustados refletidos no cálculo (**R$ 995,60),**como mostra o log abaixo:

*Cobrança por Orçamento: 2/ORÇAMENTO COM REAJUSTE*  
*Associação: BH MALLS*  
*Período: 01/01/2000 - (sem data final)*  
*Tipo de Valor: Valor orçado*  
*Valor: R$5.000,00*  
*Item de Cobrança: 19/Orçamento com Reajuste*  
*Modelo de Rateio: Valor Fixo*

*Cobrança fixa:*  
*Bloco/Apto: FIXO/000010*  
*R$995,60*

*Valor total das cobranças fixas: R$995,60*  
*Novo valor do orçamento a ser rateado:*  
*Orçamento - Valor total: R$5.000,00 - R$995,60 = R$4.004,40*
