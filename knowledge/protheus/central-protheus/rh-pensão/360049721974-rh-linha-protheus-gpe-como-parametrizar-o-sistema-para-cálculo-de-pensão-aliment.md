---
article_id: 360049721974
category: RH - Pensão
content_hash: f2a2d754a42b0cd1f47318a7ace9beb6e396345873c161f51617704e144b7200
fetched_at: '2026-06-28T22:43:35.172332+00:00'
product: protheus
section_id: 360004995674
source: central-protheus
title: RH - Linha Protheus - GPE - Como parametrizar o sistema para Cálculo de Pensão
  Alimentícia
type: support-article
updated_at: '2025-08-19T18:42:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049721974-RH-Linha-Protheus-GPE-Como-parametrizar-o-sistema-para-C%C3%A1lculo-de-Pens%C3%A3o-Aliment%C3%ADcia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16302203278615) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como parametrizar o sistema para Cálculo de **Pensão Alimentícia**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Estas informações serão utilizadas nos cálculos de Adiantamento, Folha de Pagamento, Férias, Rescisão e 13º Salário, bem como na Impressão de Cheque, Geração e Impressão de Líquidos.  
  
**1.** Na rotina de **Verbas (GPEA040)**, localizada no menu **Atualizações > Definições Cálculos > Verbas**, crie os cadastros para o desconto de Pensão que posteriormente serão relacionadas ao cadastro de Beneficiário.  
**OBS:** A verbas **não devem possuir ID de cálculo** e o campo **Pensão Alim**. da aba **Incidências** deve ficar com **Não**.  
  
**2.** Ainda na rotina de **Verbas**, parametrize as verbas que farão base de cálculo para a Pensão Alimentícia. Para isso, na aba **Incidências** altere o campo **Pensão Alim.** para **SIM,** dessa maneira o sistema passará a somar os valores dessa verba na base de Pensão:![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100710374)  
  
**3.** Acesse **Atualizações > Funcionários >** **Beneficiários (GPEA280),** selecione o Funcionário e clique em **Incluir/Alterar**:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27305989577495)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27305989580055)

Segue abaixo um detalhamento sobre os campos do **Cadastro de Beneficiários**:  
  
**- Beneficiário\*:** Nome do beneficiário(a) - filhos - para  qual deve ser efetuado o pagamento do benefício, por exemplo pensão.  
**- CPF\*:** Número do CPF do beneficiário - filhos  
**- Percentual:** Percentual a ser aplicado sobre a base de cálculo do benefício.  
**- Nro Sal Minimos:** Se informado, o número vezes o valor do salário mínimo (de acordo com a tabela), deve ser a base de cálculo sobre a qual será aplicado o percentual.  
**- Valor fixo:** Se informado, este será o valor do benefício.  
**- Verbas para base:** Neste campo, pode selecionar as verbas que irão compor a base de cálculo do benefício. No entanto, ele deve ser usado apenas quando o cálculo da pensão envolve verbas específicas. Não é necessário considerar todas as verbas marcadas como "SIM" para pensão. Ou seja, quando o cálculo exige incluir todas as verbas configuradas como "SIM" para pensão, este campo **pode ser deixado em branco.****- Verba para o Adto:** Código da verba a ser utilizado para o desconto da pensão no Adto (Verba sem id e com Não para pensão).  
**- Verba para Folha :** Código da verba a ser utilizado para o desconto da pensão na Folha (Verba sem id e com Não para pensão).  
**- Verba para Férias:** Código da verba a ser utilizado para o desconto da pensão nas Férias (Verba sem id e com Não para pensão).  
**- Verba para 13ª 1ª** **:** Código da verba a ser utilizado para o desconto da pensão na 1ª parcela do 13º salário (Verba sem id e com Não para pensão).  
**- Verba para 13ª 2ª :** Código da verba a ser utilizado para o desconto da pensão na 2ª parcela do 13º salário (Verba sem id e com Não para pensão).  
**- Verba p/ PLR:** Código da verba a ser utilizado para o desconto da pensão quando ocorrer o pagamento de PLR (Verba sem id e com Não para pensão).  
**- Calc. s/ liquido:** Se **Sim**, o valor da pensão após ser calculado será utilizado como dedução do IR e o IR como dedução na pensão, até que a diferença entre dois cálculos de pensão resulte menos que R$ 1,00.   
Se **Não**, será calculado o valor do benefício uma única vez e este será o valor a ser descontado.  
**- Banco/Agencia:** Código do banco e agência para geração de líquido em disquete ou emissão do relatório dos valores de líquido a receber - geralmente informada conta da mãe.  
**- Conta Corrente:** Número da conta corrente para geração de líquido em disquete ou emissão do relatório dos valores de líquido a receber.  
**- CPF Resp:** CPF do responsável pelo recebimento da pensão, caso seja diferente do beneficiário já cadastrado.  
**- Nome Resp:** Nome do responsável pelo recebimento da pensão, caso seja diferente do beneficiário já cadastrado.

**\*OBS:** Conforme [orientação da Consultoria de Segmentos](https://tdn.totvs.com/pages/releaseview.action?pageId=418683597), os dados como Nome e CPF sempre deverão ser do alimentado que recebe a Pensão, ou seja, os dados serão do filho independente de sua idade.

**Saiba Mais**[RH - Pensão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004995674-RH-Pens%C3%A3o)[Consultoria de Segmentos - Pensão Alimentícia](https://tdn.totvs.com/pages/releaseview.action?pageId=418683597)  
[RH - Linha Protheus - GPE - Verba desconto de pensão não aparece na rotina de Beneficiários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/21076040133015-RH-Linha-Protheus-GPE-Verba-desconto-de-pens%C3%A3o-n%C3%A3o-aparece-na-rotina-de-Benefici%C3%A1rios)  
[RH - Linha Protheus - GPE - Como cadastrar dois tipos de pagamento de pensão para o mesmo beneficiário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10263341187735-RH-Linha-Protheus-GPE-Como-cadastrar-dois-tipos-de-pagamento-de-pens%C3%A3o-para-o-mesmo-benefici%C3%A1rio)
