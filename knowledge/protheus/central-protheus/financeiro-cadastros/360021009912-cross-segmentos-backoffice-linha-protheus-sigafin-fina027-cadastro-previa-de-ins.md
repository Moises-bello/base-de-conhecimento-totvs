---
article_id: 360021009912
category: Financeiro - Cadastros
content_hash: 3fedd33a9d9330df6dfde88bba2fd4ce4490c807bdc93b279d94cdcc177e5154
fetched_at: '2026-06-28T22:37:53.185644+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA027 - Cadastro
  Previa de INSS
type: support-article
updated_at: '2022-06-21T01:22:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021009912-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA027-Cadastro-Previa-de-INSS
---

*****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*****Tempo aproximado para leitura: ****00:03:00 min**  
  
Dúvida**Qual Informações temos sobre a rotina de cadastro previa de INSS?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA027 - Todas as versões  
  
****Solução****Nesta rotina é possível cadastrar as retenções prévias de **INSS** dos prestadores de serviços, e considerá-los na cumulatividade de **INSS** e na validação do limite de retenção caso o fornecedor seja pessoa física.

**Procedimento**1.    Na tela de cadastro das retenções de **INSS prévias**. Clique em **Incluir**.  
2.    Informe o código de fornecedor e loja relacionados ao prestador de serviços.  
3.    Preencha os dados da retenção por meio dos campos **Item, Dt. Inicial**, **Dt Final, a Entidade**, o **tipo** **de pessoa em TP pessoa**, **CNPJ**, o **Valor Base e o INSS**.  
4.    Confirme os dados e clique em **Confirmar**.  
   
É possível verificar o valor de retenção na rotina de **Contas a Pagar**.  
  
**Tabelas**

•    **FJW** - Cabeçalho de Prévias de INSS.  
•    **FLX** - Itens de Prévias de INSS.  
•    **SA2** - Cadastro de Fornecedores.  
•    **SE2** - Títulos a Pagar.  
•    **SED** - Cadastros de Naturezas.  
•    **BBC** - RDA Fixos Créditos e Débitos.  
•    **BMR** - Composições de Pagamentos.  
•    **BGQ** - Débitos e Créditos RDA.  
•    **BAU** - Redes de Atendimento.

**Parâmetro**

Nome  
**MV\_LIMINSS**  
  
Descrição  
Indica o valor limite de retenção para o INSS de pessoa física  
  
Conteúdo Padrão  
0  
  
**Importante**•    O limite de retenção é definido pelo parâmetro **MV\_LIMINSS**.  
•    É permitido realizar mais de uma retenção para o prestador, num mesmo período, para  empresas diferentes.  
•    É possível importar os arquivos de retenções de **INSS** prévias para o módulo do **Plano de Saúde** por meio da rotina **Importação de dados PLS**.
