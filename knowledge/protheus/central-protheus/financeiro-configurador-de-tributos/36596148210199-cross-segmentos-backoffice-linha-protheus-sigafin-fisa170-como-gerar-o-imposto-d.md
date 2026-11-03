---
article_id: 36596148210199
category: Financeiro - Configurador de Tributos
content_hash: 07f290968d7722064a3cf6065c1452ec75d4360d44fb296f5599fccd25d310f5
fetched_at: '2026-06-28T22:37:46.104331+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar
  o imposto de IRRF referente às comissões de vendedores usando a regra financeira
  pelo documento de saída
type: support-article
updated_at: '2025-11-26T17:45:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36596148210199-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-de-IRRF-referente-%C3%A0s-comiss%C3%B5es-de-vendedores-usando-a-regra-financeira-pelo-documento-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36596148198935) Tempo aproximado para leitura: **00:15 min**  
  
**Dúvida**  
Como gerar o imposto de IRRF referente às comissões de vendedor no contas a pagar?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2210.  
  
**Solução**  
Para definir a regra financeira do **IRRF** no **Contas a Receber** por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Cliente, Fornecedor e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **Cliente, Fornecedor e Natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

**1.  FISA710 – Configuração de Regras Fiscais por Perfil>** **Perfil de Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596148199447)

Para esse cenário, crie a **regra de perfil do produto** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código Perfil**
* **Descrição**
* **Código do Produto**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596164795415)

**2. FISA710 – Configuração de Regras Fiscais por Perfil>** **Perfil de Participante**

Para esse cenário, crie a **regra de perfil do participante** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código Perfil**
* **Descrição**
* **Tipo (Cliente)**
* **Participante (selecionar o cliente cadastrado)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596148200855)

**3. FISA710 – Configuração de Regras de Cálculo de Documento Fiscal > Regra de Base de Cálculo**

Para esta regra, é necessário preencher as configurações correspondentes à **Regra de Base de Cálculo**, Regra de **Alíquota** e **Regra de Cálculo do Documento Fiscal**.

**3.1** O processo inicia-se pela definição da **Regra de Base de Cálculo**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596164797335)

Para esse cenário, crie a **regra de base de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código Regra**
* **Descrição**
* **Valor Origem**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596164797847)

**3.2 Regra de alíquota**

Para esse cenário, crie a **regra de alíquota** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código Regra**
* **Descrição**
* **Valor Origem**
* **Tipo Alíquota (1 - Percentual)**
* **Alíquota (conforme a necessidade)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596148201495)

**3.3** **Regra de Cálculo do Documento Fiscal**

Para esse cenário, crie a **regra de cálculo do documento fiscal** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código Regra**
* **Descrição**
* **Tributo** (IRF)
* **Data de início**
* **Data Final** (opcional)
* **Status** utilizar o status **2 - Aprovada**
* **Base de cálculo** (vínculo da regra de cálculo)
* **Alíquota** (vínculo da regra de alíquota)
* **Regra Financeira** (vínculo da regra financeira) **Poderá ser cadastrada posteriormente.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596164798999)

* **Origem/Destino** (000002 - Para todas as UFS)
* **Participante** (cadastrado na regra de perfil do participante)
* **Operação** (000051 - Todos os CFOPS)
* **Produto** (cadastrado na regra de perfil do produto)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596296683543)

**4.  FISA710 - Regras Financeiras > Regra do Título**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596148202135)

Para esse cenário, crie a **regra de título** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* O **Tipo de Movimento (Tp. Movto)**, selecionando a opção impostos**.**
* ****Participante** (1 - Fornecedor)**
* O**código do participante** (informar o código do fornecedor)
* A **carteira**, que neste caso deve ser definida como **Pagar**;
* A **natureza** previamente criada para vinculação do tributo;
* O **tipo de título** (TX)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596495401367)

**5.  FISA710 - Regras Financeiras > Regra de Cálculo**

Para esse cenário, crie a **regra de cálculo** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* **Alíquota**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596579619607)

**6.  FISA710 - Regras Financeiras > Regra de Vencimento**

Para esse cenário, crie a **regra de vencimento** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* **Dia de Vencimento** (conforme a necessidade)
* **Tipo de vencimento** (conforme a necessidade)
* **Data base p/ vencimento dos impostos** (conforme a necessidade)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596579620503)

**7.  FISA710 - Regras Financeiras > Regra de Retenção**

Para esse cenário, crie a **regra de retenção** considerando os campos indicados a seguir:

**Preenchimento dos campos**:

* **Código**
* **Descrição**
* **Valor mínimo de retenção** (conforme a necessidade)
* **Valor máximo de retenção** (conforme a imagem)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596654383127)

**8.  FISA710 - Regras Financeiras > Regra Financeira**

Este cadastro tem como função definir a regra de retenção do tributo aplicado a títulos gerados diretamente no módulo Financeiro, consolidando outras regras como vencimento, cumulatividade, retenção, cálculo, etc.

Outra função deste cadastro é definir a qual tributo a regra se refere, ou seja, relacionar a regra financeira a um tributo definido por legislações federais, estaduais ou municipais.

Para este cenário, é necessário criar a regra financeira correspondente ao imposto na aba Dados Gerais, preenchendo os campos indicados a seguir:

Preenchimento dos campos:

* **Código**
* **Descrição**
* **Início de vigência:** data inicial.
* **Fim da vigência:** data final.
* **Fato Gerador:** 1 – Competência (emissão) | 2 – Caixa (baixa). Conforme necessidade, mas para este cenário será utilizada a competência.
* **Aplica-se à Carteira:** (1 – Pagar ou 2 – Receber; neste caso, selecionar a opção Pagar)
* **Valor do Título:** (1 – Subtrair, 2 – Somar ou 3 – Sem ação. Neste caso, selecionar a opção Subtrair)
* Código de retenção (conforme a necessidade)
* **Parcelamento: opcional** (conforme a necessidade)
* **Tributo:** imposto a ser cadastrado.
* **Classificação do tipo de imposto** (principal)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36596740750999)

Na aba **Regras Gerais**, vincule todas as regras criadas anteriormente nas **regras financeiras**, considerando os campos indicados a seguir:

**Preenchimento dos campos:**

* **Regra de Vencimento**
* **Regra de Título**
* **Regra de Cálculo**
* **Regra de Retenção**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36597057793687)

Após a conclusão do cadastro da regra financeira, é necessário retornar ao módulo **Regra Fiscal** e acessar o caminho:  
**Configuração de Regras de Cálculo de Documento Fiscal > Regra de Base de Cálculo – Documentos Fiscais**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36597037799959)

Nesta regra, deve ser realizado o **vínculo da regra financeira** previamente configurada, garantindo que sejam gerados os impostos no financeiro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36597037802007)

**Importante**

Os cadastros mencionados acima permitirão a geração do **IRRF** do documento de saída destinado ao **Contas a Pagar** referente à Nota Fiscal.

No entanto, para que o sistema realize também a **retenção de IRRF referente à comissão do vendedor**, é necessário criar uma **regra financeira específica de IRRF para o Contas a Pagar**, a qual deverá ser vinculada ao **cadastro do fornecedor e natureza.**

**Para orientar essa etapa, consulte a documentação indicada abaixo.**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar o imposto de IRF pessoa jurídica para o configurador de tributos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32263850401943-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-de-IRF-pessoa-jur%C3%ADdica-para-o-configurador-de-tributos)

Após a criação da regra financeira para o contas a pagar referente à comissão, será necessário vinculá-la ao **cadastro da natureza e fornecedor** correspondente.

**9.** **Cadastro de Fornecedor**  
No **cadastro do fornecedor**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36597411945879)

Vincule o código da **Regra Financeira**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36597365068183)

**10. Cadastro da Natureza**  
Nocadastro de natureza**,** criado sem parametrização de impostos, vincule a regra financeira em **"**Tipo de retenção x natureza**"**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36597729626263)

**11.** **Cadastro de Vendedores**

No cadastro do vendedor, acesse a aba **Pagamento de Comissão** e preencha os seguintes campos:

* **Fornecedor**
* **Forma de Pagamento**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36597729629335)

Na aba **Outros**, é necessário preencher o campo **Base c/ IRF** selecionando a opção **1 – Não**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36597899703447)

É imprescindível vincular o fornecedor que vinculou a **regra financeira** responsável pela geração do **IRRF** no **Contas a Pagar**, assegurando o correto processamento da retenção sobre a comissão.

**Importante**

Para que o **IRRF referente à comissão do vendedor** seja devidamente gerado no módulo de **Contas a Pagar**, o parâmetro **MV\_COMISIR** deve estar configurado com o valor **“S”**.

Comportamento do sistema

Após o envio do **Pedido de Venda**, será gerada a **NF** no **Contas a Receber.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36598168974359)

E o **título de IRRF (TX)** correspondente a NF no **Contas a Pagar**, conforme evidenciado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36598189809047)

Quando a baixa do título for realizada, a **comissão** será registrada na rotina **Manutenção de Comissões (MATA490)**, desde que o processo seja **online**.  
Caso o ambiente esteja configurado como **offline**, será necessário executar o **Recálculo de Comissão (FINA440)** para que os valores sejam atualizados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36598324123287)

Para que o **IRRF sobre a comissão** seja devidamente gerado, é obrigatório efetuar o **pagamento da comissão** por meio da rotina **Atualização de pagamento de Comissão (MATA530) realizando a baixa do título de comissão.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36598609389719)

E consequentemente gerada a comissão no contas a pagar e o TX do IRRF.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36604015837847)

**Saiba mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
