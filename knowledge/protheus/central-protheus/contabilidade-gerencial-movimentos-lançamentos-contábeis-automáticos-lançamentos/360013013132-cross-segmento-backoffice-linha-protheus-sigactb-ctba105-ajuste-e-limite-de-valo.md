---
article_id: 360013013132
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 8685288065c17fa8f9b3ba9dbef0481163393417cdbd4db0abf4e815eb7801a0
fetched_at: '2026-06-28T22:40:32.489974+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA105 - Ajuste e
  limite de valores em centavos '
type: support-article
updated_at: '2022-07-18T19:46:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013013132-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Ajuste-e-limite-de-valores-em-centavos
---

**Dúvida**

* Permitir o sistema efetuar um lançamento automático referente a diferença de centavos entre os valores de debito e credito no mesmo documento
* Arredondamento de valores

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus – Contabilidade – A partir da versão 11.80 **Solução**

Uma nota fiscal inclusa em dólar onde o credito é feito pelo total da nota e os débitos pelos itens (produtos/impostos), lançamento contábil:

Credito: 242,08 (total da Nota)

Debito: 100,03

Debito: 100,03

Debito: 21,01

Debito: 21,02

Total a Crédito: 242,08

Total a Debito: 242,09

 A diferença 0,01 centavos irá para a entidades contábeis padrões, definidas pelo usuário nos parâmetros **MV\_CTBCENC**, conforme regra abaixo:

* Caso a diferença saldo seja credor, irá fazer um lançamento de ajuste a debito.
* Caso a diferença de saldo seja devedora, irá fazer um lançamento de ajuste a crédito.

No mesmo lote, sub-lote e documento.

O limite de valores em centavos para ajuste, será definido no parâmetro **MV\_CTBLIMC** o valor tolerante referente a cada moeda configurada, exemplo:

**MV\_CTBLIMC** = 0.20;0.20;0.20;0.20;0.20; (a diferença para todas as 5 moedas é de 0.20)     

* Caso o a diferença do lançamento seja menor ou igual à listada neste parâmetro será feito um lançamento de ajuste, caso contrário o lançamento será impedido, apresentando os helps conforme padrão configurado no sistema.

No parâmetro **MV\_CTBCENC** serão listadas todas as entidades contábeis usadas nos lançamentos separadas por ponto e vírgula (;), na seguinte Ordem: Conta Contábil, Centro de Custo, Item Conta, Classe de Valor, Entidade 05, Entidade 06, Entidade 07, Entidade 08, Entidade 09.

Na Inicialização do módulo Contabilidade Gerencial, se o parâmetro **MV\_CTBLIMC** o valor tolerante for maior zero, deverá validar se o parâmetro **MV\_CTBCENC** está preenchido e se as entidades informadas são validas.

Os parâmetros acima são utilizados para o contexto de criação automática dos lançamentos de ajuste, mas para ativar essa funcionalidade será necessário configurar também os parâmetros conforme abaixo:  
**MV\_CONTBAT = S**  
**MV\_CONTSB = N  
 MV\_CTBVLDM = 11111** .Esse parâmetro indica em quais moedas o Sistema fará a validação das moedas. Ex. 11222 o Sistema validará a moeda 1 e 2 ignorando as outras moedas.

Documentações relacionadas

<https://tdn.totvs.com/pages/viewpage.action?pageId=538480494>

<http://tdn.totvs.com/pages/viewpage.action?pageId=311066592>

<http://tdn.totvs.com/display/MIG/Dicas-ctba102_dicas.htm>

Saiba mais

[CTBA105 - Contabilização Off-Line não valida a linha do lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-MP-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento?source=search)
