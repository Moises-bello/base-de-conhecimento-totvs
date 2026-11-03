---
content_hash: f3c3dd717610d8152a505dcca21c0032e3bbe74f42e807b02d5d63f922afd412
fetched_at: '2026-06-29T00:09:21.767962+00:00'
page_id: '422545901'
product: rm
source: tdn-rm
title: Automatismo de Lançamentos (Lalur Parte B)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545901
version: 3
---

Automatismos na **constituição de saldo** na conta da Parte B do Lalur e na **utilização de saldo** da conta da Parte B do Lalur na apuração do lucro real.  
A constituição de saldo em conta da Parte B do Lalur para posterior adição ou exclusão, seja em conta existente ou em nova conta, pode ser proveniente de lançamentos de adição e/ou exclusão realizados na Parte A do Lalur.

**Regras**  
Se o valor a ser controlado na Parte B for proveniente de uma Adição na Parte A  - A conta da Parte B terá natureza de "**Exclusão**".

* Se o valor a ser controlado na Parte B for proveniente de uma Exclusão na Parte A - A conta da parte B terá Natureza de "**Adição**".
* Se for referente à Prejuízo apurado no período - A conta da parte B terá Natureza de "**Prejuízo Fiscal**".

***Nota!*** Neste caso, é preciso identificar o Código do lançamento (tabela dinâmica do Registro M300/M350 da ECF) que originou a conta da Parte B.

**Conta da Parte B do Lalur**

Menu: RM\Gestão Fiscal\Obrigações Principais\Lalur Parte B\Contas\Anexos\Informações Fiscais  
 Foi criado o anexo Informações Fiscais e incluído neste anexo o campo "CNPJ da pessoa jurídica relacionada

**CNPJ da pessoa jurídica relacionada**: Neste campo deve ser informado o CNPJ da outra pessoa jurídica envolvida no evento que originou a conta, por exemplo, CNPJ da investida, da antecessora, etc.Esse campo será utilizado para gerar o campo 11 do Registro M010: "CNPJ\_SIT\_ESP - CNPJ da outra pessoa jurídica relacionada com evento originário da conta".

Menu: RM\Gestão Fiscal\Obrigações Principais\Lalur Parte B\Contas\Pasta Tributos\  
 Inclusão de novo campo no cadastro:  
  
**Código da Tabela Dinâmica da ECF**(pasta Tributos): Este campo terá lookup para o Cadastro da Tabela Dinâmica da ECF. Deve ser informado nesse campo o código do lançamento na parte A do e-Lalur e/ou do e-Lacs que deu origem à conta.  
 Essa informação será utilizada para gerar os campos 5 (Código do Lançamento de origem) e 6 (Descrição do lançamento de origem) do Registro M010 - IDENTIFICAÇÃO DA CONTA NA PARTE B DO e-LALUR E DO e-LACS na rotina da ECF.

**Lançamentos da Parte B do Lalur**

Menu: RM\Gestão Fiscal\Obrigações Principais\Lalur Parte B\Lançamentos\Pasta Processos Judiciais e Administrativos\  
 Criar **Anexo** no Lançamento da Parte B do Lalur com lookup para o **Cadastro de Processo Judicial e Administrativo** onde o usuário deverá informar todos os processos judiciais ou administrativos que embasaram movimentações na parte B do e-Lalur ou do e-Lacs com tratamento diverso das regras fiscais. Cada processo associado ao Lançamento deve gerar um Registro M415 na ECF.  
***Importante!***Esse Anexo deve ser utilizado apenas para os valores que **NÃO** afetam a Parte A, ou seja, somente para deduções\compensações do tributo. Nos demais casos, adições, exclusões e compensação de prejuízo, o Processo Judicial/Administrativo deve ser informado no Item Tributário, dentro do Evento Tributário.

**Recurso "Replicar lançamento para a CSLL"**  
 Ao salvar o lançamento na conta da Parte B para o tributo do Tipo "IRPJ", perguntar ao usuário se ele deseja replicar o lançamento para o tributo do Tipo "CSLL".   
 O usuário respondendo "Sim" o sistema deve criar outro lançamento com os mesmos dados alterando apenas o **Tributo**.   
***Importante!***Esse recurso só existi inclusão. Na edição não deve ser apresentado para evitar duplicidade de lançamentos.
