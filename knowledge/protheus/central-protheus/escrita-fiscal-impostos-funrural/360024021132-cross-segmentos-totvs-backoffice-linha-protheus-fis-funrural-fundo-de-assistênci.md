---
article_id: 360024021132
category: Escrita Fiscal - Impostos - Funrural
content_hash: cf2534735a7fa71cb6e5a850740282c04cbd98f3058976a01819e4a16c1988a2
fetched_at: '2026-06-28T22:39:28.156627+00:00'
product: protheus
section_id: 1500001549822
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - FUNRURAL - Fundo
  de Assistência ao Trabalhador Rural
type: support-article
updated_at: '2023-07-19T20:35:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024021132-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FUNRURAL-Fundo-de-Assist%C3%AAncia-ao-Trabalhador-Rural
---

**Dúvida**

Como parametrizar FUNRURAL - Fundo de Assistência ao Trabalhador Rural

**Ambiente**

Protheus – Livros Fiscais – a partir da versão 11

**Solução**

Devido as exigências de informações do **e-Social** e **REINF**, onde as contribuições**GILRAT**, **INSS** e **SENAR**são separadas, se faz necessário apresentar no sistema estas contribuições calculadas separadamente, conforme configurações abaixo.

Portanto deve-se utilizar as configurações descritas para ser utilizado o **FUNRURAL** para cálculo da contribuição do **GILRAT** e efetuar os cálculos segregados do **INSS** e **SENAR**.

Para solucionar essa dúvida, realize os seguintes passos:

**1. Configurador do sistema**

Acesse o configurador > empresa > filial  
No Cadastro de Filiais deve ser definido o campo **Produtor Rural** em **Dados Cadastrais**, pasta **Complementos.**

Neste campo você devera informar o cenário da sua empresa perante a operação Funrural.

 J - Pessoa Jurídica

 F - Pessoa Física,

 L - Segurado Especial (trabalha com o grupo familiar conforme Bol. IOB Legislação Trabalhista Previdenciária 48/94).

**2. Cadastro Fornecedor   
  
Pessoa Física**

Tipo (A2\_TIPO) = F - Fisico

CNPJ/CPF = Informe o CPF do produtor Rural

Tp.Contr.Soc (A2\_TIPORUR)  = F-Pessoa Fisica

Tipo de Pessoa (A2\_TPESSOA) = PF - Pessoa Fisica

Calc. INSS (A2\_RECINSS) = SIM  
  
**Pessoa Jurídica**

Nos casos em que o produtor rural tenha CNPJ poderá efetuar as configurações no cadastro do Fornecedor seguindo a sequencia abaixo:   
  
**1**-Acessar o cadastro do Fornecedor.

**2**-Acessar a aba Outros e configurar o campo Ind Prod Rur (A2\_INDRUR).  
**3**- Acessar a aba Cadastrais e configurar o campo Tipo (A2\_TIPO) igual a Físico. 

Seguindo a sequencia acima, após alterar o campo CNPJ/CPF (A2\_CGC) de Jurídico para Físico será mantido o CNPJ informado sem mudar a máscara para CPF.

Caso tenha a necessidade de informar o CPF do produtor Rural, poderá informar na aba Outros no campo CPF Rural (A2\_CP\_RUR) que será habilitado após efetuar as configurações conforme sequencia descrita acima referente Fornecedor Pessoa Jurídica.

**3. Cadastro Produto**

Cont.Seg.Soc (B1\_CONTSOC) = Sim

Calcula INSS = SIM

**4. TES**

Cont.Seg.Soc (F4\_CONTSOC) = Sim Calcula o GILRAT (Para não calcular o GILRAT deixe como NÃO)

Aliq. SENAR (F4\_ALSENAR) = Informe alíquota do SENAR

Informar campo **Bas.FUNRURAL** (F4\_BSRURAL) conforme a necessidade e/ou interpretação da Instrução Normativa SRP nº 03/2005 artigos 246 e 247.

**5. Natureza**

Calcula INSS = SIM para calcular INSS, para não calcular o INSS deixe como NÃO

Porc. INSS = Informe alíquota necessária

Ded.INSS (ED\_DEDINSS): Informe "1" (Sim)para que o valor do INSS seja deduzido do valor do título quando houver retenção desta contribuição. Informe "2" (Não) em caso contrário.

Documentação completa disponível em:

<https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=336407064>

<https://tdn.totvs.com/display/public/PROT/FIS0111+-+SENAR+%2C+INSS+E+GILRAT>
