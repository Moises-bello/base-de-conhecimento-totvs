---
content_hash: e7079958333e6cd110b50b5b314c1e5595354d9d3975c46474c223bd1ad19e9b
fetched_at: '2026-06-29T00:09:19.442051+00:00'
page_id: '421390951'
product: rm
source: tdn-rm
title: Como o RM/TAF irá consolidar o pagamento de um "Autônomo Fluxus/Externo" e
  "Funcionário com vinculo" na mesma competência?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421390951
version: 4
---

---

---

Atualmente no RM, para situações em que existem pagamentos na mesma competência para um funcionário com vinculo e outra para algum autônomo externo ou oriundo do RM Fluxus, o evento S-1200 será gerado em registros (XML) distintos, sendo um referente ao seu registro com vinculo e outro associado ao cadastro do autônomo.

* Como isso será entendido pelo governo, já que é possível enviar apenas uma ordem de pagamento para um CPF em um determinado período (Competência)?

Ao transmitir ambos os XMLs para o TAF, o mesmo irá consolidar as duas ordens de pagamento em apenas um XML e então transmiti-lo para o governo. Mas para que isso ocorra com sucesso, deverá se atentar a seguinte restrição:

Não poderá ser transmitido ao TAF pagamentos para o mesmo ideDmDev, ou seja, para o mesmo **período** de pagamento do labore.

**Observação:** Isso ocorre pelo fato de que os pagamentos serão agrupados por CPF e por período, caso seja enviado o mesmo período, o TAF irá prevalecer com os valores associados ao ultimo período processado, substituindo assim o existente.

* ### Já que não podemos transmitir períodos iguais para a mesma período de pagamento, como vou fazer para não cair nessa exceção?

Devemos fazer com que o Labore diferencie os períodos de pagamentos, evitando assim que ocorra pagamento em períodos iguais, para isso faça:

1true11º PassoAssociando prefixo ao funcionário.

1. Acesse o cadastro do funcionário que possui vinculo e vá na pasta "Parâmetros";
2. Preencha o campo "Prefixo Período (eSocial)" de acordo com sua necessidade;  
   Obs.: O valor preenchido neste campo será concatenado ao campo ideDmDev, impedindo assim que ocorra duplicidade de períodos.
3. Salve as alterações.
22º PassoGeração do XML e Validação

1. Acesse a fila de eventos dos periódicos;
2. Faça a geração do registro referente ao funcionário com vinculo;
3. Verifique no XML se a tag "ideDmDev" será calculado contendo o valor do prefixo, exemplo:

**Observação**: Para o XML referente a folha de pagamento do autônomo fluxus/externo, o período (ideDmDev) será calculado com o valor fixo 1.

* ### Como o TAF irá consolidar os XMLs?

2

Ao fazer o processo de transmissão e integração das ordens de pagamento com o TAF, os períodos (ideDmDev) serão agrupados em apenas um cadastro.

1S-1200S-12003true11º PassoCadastro de pagamento.

No TAF acesse o menu referente ao cadastro da folha de pagamento.

**Caminho**: Atualizações | Eventos Esocial | Periódicos | Folha de Pagamento.

22º PassoValores e Períodos

Na aba "Demonstrativos de Valores" é onde veremos como as informações foram consolidadas.

Note que foi criado dois períodos referente ao funcionário com vinculo, possuindo prefixo P (1P e 2P), além também do período referente ao autônomo fluxus/externo, onde se encontra com período 1.

33º PassoXML consolidado

Ao verificar o XML que será transmitido para o governo, podemos notar que será levado 3 grupos "ideDmDev", conforme existente na aba demonstrativo de valores.

2S-1210S-12103true11º PassoCadastro de pagamento.

No TAF acesse o menu referente ao cadastro do rendimento referente a folha de pagamento.

**Caminho**: Atualizações | Eventos Esocial | Periódicos | Pagto Rend Trab.

22º PassoPagamentos Realizados

No agrupamento "informações dos Pagamentos Efetuados" será onde veremos como as informações foram consolidadas.

Note que foi criado dois registros com data de pagamento, um referente ao funcionário com vinculo e outro referente ao autônomo fluxus/externo.

33º PassoXML consolidado

Ao verificar o XML que será transmitido para o governo, podemos notar que será levado 3 grupos "ideDmDev".

falsefalse

**Produto:** Folha de Pagamento

false

**Rotina:** eSocial

false

**Versões:**

|  |
| --- |
| 12.1.22 |
| 12.1.21 |
| 12.1.20 |
| 12.1.19 |

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autor:**
