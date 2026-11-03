---
content_hash: a54ca707111ca2acbceea1206e11abd0d17c0293783c5460ffb6af09b59955e0
fetched_at: '2026-06-29T00:10:26.739988+00:00'
page_id: '514729702'
product: rm
source: tdn-rm
title: ICMS Desonerado
type: documentation
url: https://tdn.totvs.com/display/LRM/ICMS+Desonerado
version: 43
---

O ICMS (Imposto Sobre Circulação de Mercadorias e Serviços) desonerado consiste em um beneficio fiscal que concede um desconto tributário no valor do imposto dispensado nas operações não tributadas, isentas ou suspensas. Este documento visa dar orientações sobre as parametrizações necessárias e o funcionamento do ICMS Desonerado no módulo TOTVS Gestão Fiscal.

# Cadastros

No Cadastro da Regra de ICMS devem ser parametrizados os campos **ICMS Desonerado**, **Motivo da Desoneração e Fórmula Base de Cálculo do ICMS Desonerado.** Vide documentação especifica .

# Movimento

Ao criar um movimento utilizando um CFOP que esteja com ICMS Desonerado marcado na Regra de ICMS, na linha do **tributo do ICMS** os campos serão preenchidos com as seguintes regras:

* **Base de Cálculo:** será preenchida com o resultado da Fórmula de Base de Cálculo defina nos Parâmetros do Tipo de Movimento;
* **Alíquota:** no caso do ICMS Desonerado este campo será preenchido com a Alíquota informada na Regra de ICMS somente se o Tipo de Tributação for Tributado e marcado a opção ICMS Desonerado (Considerando que a parametrização está configurada para buscar a alíquota na Natureza). Caso contrário o campo não será preenchido.
* **Valor:** Será preenchido com o resultado da Multiplicação dos campos **Base de Cálculo** **X** **Alíquota**, se a alíquota tiver sido preenchida.
* **Motivo Desoneração ICMS:** Será preenchido automaticamente com o Valor preenchido na Regra de ICMS associada ao CFOP;
* **Base de Cálculo ICMS Desonerado:** Será preenchido com o resultado da **Fórmula de Base de Cálculo do ICMS Desonerado** preenchida na Regra de ICMS. No caso de não ter nenhuma fórmula preenchida será considerado o valor do campo **Base de Cálculo** do próprio tributo ICMS.
* **Valor do ICMS Desonerado:** Será preenchido com o resultado da Multiplicação dos campos **Base de Cálculo ICMS Desonerado X Alíquota do ICMS.**

  Alíquota

  Se o parâmetro "Busca Alíquota da Operação Própria no Estado" estiver marcado a alíquota será preenchida com a Alíquota do Estado desconsiderando a Alíquota da Regra de ICMS.

  Valor Líquido

  Em algumas situações o ICMS Desonerado poderá afetar o valor líquido do documento. Em caso de dúvidas consulte a legislação vigente.

# NF-e

No xml da NF-e (Nota Fiscal Eletrônica) os campos abaixo referente ao ICMS Desonerado serão preenchidos.

Na tributação do Item

* **vICMSDeson;**
* **motDesICMS.**

Vide documentação especifica

No total da NF-e

* **vICMSDeson.**

Vide documentação especifica

# Escrituração

Ao realizar a escrituração de um movimento com o ICMS Desonerado o Lançamento será criado conforme abaixo.

Lançamentos com mais de uma Situação Tributária

* **Valor do ICMS Desonerado:** será preenchido com o mesmo cálculo que foi realizado no movimento desconsiderando qualquer edição realizada diretamente na linha do tributo no movimento;
* **Motivo da Desoneração do ICMS:** será preenchido com o motivo da desoneração informado no movimento;
* **Alíquota do ICMS Desonerado:** será preenchido com a alíquota do ICMS conforme a parametrização de alíquotas;
* **Isentos ICMS:** será preenchido com o valor calculado para a  Base do ICMS Desonerado subtraído o valor do ICMS Desonerado. Exemplo: BC ICMS Desonerado = 1.000,00 e Valor do ICMS Desonerado = 180,00 este campo receberá 820,00 (1.000,00 - 180,00);
* **Valor Total da Situação Tributária:** será preenchido com o total calculado para a Situação tributárias subtraído o valor do ICMS Desonerado.

Lançamentos apenas uma situação Tributária

* **Valor do ICMS Desonerado:** será preenchido com o valor informado na linha do tributo do movimento
* **Motivo da Desoneração do ICMS:** será preenchido com o motivo da desoneração informado no movimento;
* **Alíquota do ICMS Desonerado:** será preenchido com a alíquota do ICMS conforme a parametrização de alíquotas;
* **Isentos ICMS:** será preenchido com o valor calculado para a  Base do ICMS Desonerado subtraído o valor do ICMS Desonerado. Exemplo: BC ICMS Desonerado = 1.000,00 e Valor do ICMS Desonerado = 180,00 este campo receberá 820,00 (1.000,00 - 180,00);
* **Valor Total da Situação Tributária:** será preenchido com o valor líquido do Movimento.

Para outros detalhes da escrituração consulte a documentação do processo 

# Lançamento Fiscal

Ao incluir um Lançamento Fiscal o comportamento será:

* **Base de Cálculo ICMS Desonerado:** será o valor não tributado da base do ICMS;
* **Valor do ICMS Desonerado:** será preenchido com o resultado da Multiplicação da **Base de Cálculo ICMS Desonerado X Alíquota do ICMS**;
* **Motivo da Desoneração do ICMS:** será preenchido com o motivo da desoneração informado na Regra de ICMS;
* **Alíquota do ICMS Desonerado:** será preenchido com a alíquota do ICMS conforme a parametrização de alíquotas;
* **Isentos ICMS:**- Caso na Regra de ICMS | Aba Dados ICMS, o **parâmetro ICMS Deson. NÃO afeta o Valor Contábil estiver desmarcado:** será preenchido com o valor calculado para a  Base do ICMS Desonerado subtraído o valor do ICMS Desonerado. Exemplo: BC ICMS Desonerado = 1.000,00 e Valor do ICMS Desonerado = 180,00 este campo receberá 820,00 (1.000,00 - 180,00);  
  - Caso na Regra de ICMS | Aba Dados ICMS, o **parâmetro ICMS Deson. NÃO afeta o Valor Contábil estiver marcado:** será preenchido com o valor da redução da Base do ICMS. Exemplo: BC ICMS = 1.000,00 e 30% de Red. ICMS este campo receberá 300,00 (1.000,00 \* 30%);
* **Valor Total da Situação Tributária:**   
  - Caso na Regra de ICMS | Aba Dados ICMS, o **parâmetro ICMS Deson. NÃO afeta o Valor Contábil estiver desmarcado:**será preenchido com o total calculado para a Situação tributárias subtraído o valor do ICMS Desonerado.

  Atenção

   A  fórmula a ser utilizada na Base de Cálculo do ICMS do Movimento deve levar em consideração do ICMS Desonerado.

  - Caso na Regra de ICMS | Aba Dados ICMS, o **parâmetro ICMS Deson. NÃO afeta o Valor Contábil estiver marcado:** será preenchido o valor da Base do ICMS.

  Atenção

   A  fórmula a ser utilizada na Base de Cálculo do ICMS do Movimento NÃO deve levar em consideração do ICMS Desonerado.

Para outros detalhes do Lançamento consulte a documentação do Lançamento Fiscal 

Base de Cálculo ICMS Desonerado:

No Lançamento Fiscal o valor da **Base de Cálculo ICMS Desonerado** não é apresentando em tela nem fica gravado na base de dados.

# SPED EFD ICMS IPI

No arquivo do SPED Fiscal (ICMS IPI) o ICMS Desonerado afetará os campo abaixo conforme o manual do SPED.

* C100:
  + Campo 12 (Valor Total do Documento Fiscal): será gerado com a soma do valor contábil de todas as situações tributárias do Lançamento Fiscal;
  + Campo 15 (Valor do Abatimento): será preenchido com o valor do ICMS Desonerado conforme documentação ;

* C190:
  + Campo 5 (Valor da Operação): será gerado com a soma do valor contábil de todas as situações tributárias do Lançamento Fiscal, subtotalizadas por CST.

Para outros detalhes do SPED consulte a documentação 

## Base Legal

* AJUSTE SINIEF 10, DE 28 DE SETEMBRO DE 2012;
* AJUSTE SINIEF 25, DE 17 DE DEZEMBRO DE 2012;
* AJUSTE SINIEF 1, DE 30 DE MARÇO DE 2015;
* Nota Técnica 2016.002 - v 1.60.

true

|  |  |
| --- | --- |
| Ocorrências relacionadas |  |
