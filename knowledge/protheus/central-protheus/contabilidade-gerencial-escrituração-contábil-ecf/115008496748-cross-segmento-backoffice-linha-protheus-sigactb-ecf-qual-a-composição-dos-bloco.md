---
article_id: 115008496748
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: ff03d2c24ec548978c07d5117e8a3b22e952ecb58741b78b864bfe64d68ba5b0
fetched_at: '2026-06-28T22:40:47.415302+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - qual a composição
  dos blocos para a geração do arquivo da ECF
type: support-article
updated_at: '2022-06-07T12:59:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115008496748-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-qual-a-composi%C3%A7%C3%A3o-dos-blocos-para-a-gera%C3%A7%C3%A3o-do-arquivo-da-ECF
---

**Ocorrência**

Qual a composição dos Blocos para a Geração do Arquivo da ECF?

**Ambiente**

Microsiga Protheus  – Contabilidade Gerencial – A partir da versão 11.80

**Solução**

A empresa poderá gerar um arquivo em formato texto, através do software utilizado para sua escrituração, ou poderá preencher as informações diretamente no programa gerador da ECF.

O arquivo possui uma organização hierárquica, com definições de  regras  para  cada  registro  gerado,  que  serão  submetidos  à  validação do Programa Validador da ECF.

A recuperação de dados da ECD é obrigatória para empresas que são obrigadas a entregar a ECD.

Composição dos Blocos do arquivo:

**Bloco 0 - Abertura e Identificação**

Abre  o  arquivo,  identifica  a  pessoa  jurídica  e  referencia  o  período da ECF.

**Bloco C - Informações Recuperadas das ECD (Bloco recuperado pelo sistema – Não é importado e não é editado no programa)**

Armazena  as  informações  do  plano  de  contas  e  dos  saldos mensais  das  ECD  recuperadas.  As  ECD  recuperadas  devem  corresponder  ao  período  da  ECF.  Os  seguintes  registros  da  ECD são recuperados na ECF: - I050 – Plano de Contas - I051 –  Mapeamento  para  o  Plano  de  Contas  Referencial  -  I053  –  Subcontas Correlatas - I100 – Centro de Custos - I150 – Data dos Saldos Periódicos - I155 – Saldos Periódicos - I350 – Data da Apuração do Resultado - I355 – Saldos das Contas de Resultado Antes do Encerramento Estão obrigadas a efetuar a recuperação da ECD todas as pessoas jurídicas obrigadas a entregar a ECD, conforme Instrução Normativa RFB no 1.420/2013 e alterações.

**Bloco E - Informações Recuperadas da ECF Anterior e Cálculo Fiscal  dos  Dados  Recuperados  da  ECD (Bloco  recuperado pelo sistema – Não é importado e não é editado no programa)**

Armazena,  da  ECF  recuperada  do  período  imediatamente anterior,  os  saldos  finais  das  contas  referenciais  e  da  parte  B (do e-LALUR e e-LACS). Calcula os saldos contábeis de acordo com o período de apuração do tributo.

**Bloco J - Plano de Contas e Mapeamento**

Apresenta  o  mapeamento  do  plano  de  contas  contábil  para o  plano  de  contas  referencial.  Caso  a  ECD  recuperada  possua o  mapeamento  para  o  plano  de  contas  referencial  válido na  ECF,  o  bloco  J  pode  ser  construído  automaticamente e é permitida a sua edição. O bloco J também pode ser importado, independentemente da recuperação da ECD.

**Bloco K – Saldos das Contas Contábeis e Referenciais**

Apresenta os saldos das contas contábeis patrimoniais  e de resultado por período de apuração e o seu mapeamento para as contas referenciais. Caso haja recuperação da ECD, o bloco K pode ser construído automaticamente e é permitida a sua edição.

O bloco K também pode ser importado, independentemente da recuperação da ECD.

**Bloco L - Lucro Líquido – Lucro Real**

Apresenta o balanço patrimonial, a demonstração do resultado do exercício e apura o lucro líquido da pessoa jurídica tributada pelo lucro real.

**Bloco M - e-LALUR e e-LACS – Lucro Real**

Apresenta os livros eletrônicos de escrituração e apuração do IRPJ (e-LALUR) e da CSLL (e-LACS) da pessoa jurídica tributada pelo lucro real - partes A e B.

**Bloco N - Cálculo do IRPJ e da CSLL – Lucro Real**

Calcula o IRPJ e a CSLL com base no lucro real (estimativas mensais e ajuste anual ou valores trimestrais).

**Bloco P - Lucro Presumido**

Apresenta o balanço patrimonial, a demonstração do resultado do exercício e apura o IRPJ e a CSLL com base no lucro presumido.

**Bloco Q - Livro Caixa**

Apresenta o balanço patrimonial, a demonstração do resultado do exercício e apura o IRPJ e a CSLL com base no lucro presumido.

**Bloco T - Lucro Arbitrado**

Apura o IRPJ e a CSLL com base no lucro arbitrado.

**Bloco U - Imunes ou Isentas**

Apresenta o balanço patrimonial e a demonstração do resultado das  imunes  ou  isentas.  Apura  o  IRPJ  e  a  CSLL  quando  forem  obrigadas.

**Bloco W - Declaração País-a-País (Country-by-Country Report)**

Esse bloco informa a Declaração País-a-País (DPP) que consiste em um relatório anual por meio do qual grupos multinacionais deverão fornecer à administração tributária da jurisdição de residência para fins tributários de seu controlador final diversas informações  e  indicadores  relacionados  à  localização  de  suas atividades, à alocação global de renda e aos impostos pagos e devidos.  Também deverão ser identificadas todas as jurisdições nas  quais  os  grupos  multinacionais  operam,  bem  como  todas as entidades integrantes do grupo (incluindo estabelecimentos permanentes)  localizadas  nessas  jurisdições  e  as  atividades econômicas que desempenham.

**Bloco X - Informações Econômicas**

Apresenta informações econômicas da pessoa jurídica.

**Bloco Y - Informações Gerais**

Apresenta informações gerais da pessoa jurídica.

**Bloco 9 - Encerramento do Arquivo Digital**

Encerra o arquivo digital.
