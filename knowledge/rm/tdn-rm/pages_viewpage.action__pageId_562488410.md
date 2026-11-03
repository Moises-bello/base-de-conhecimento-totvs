---
content_hash: 010a743d1b7a05b8a1ed5a012e2416c35728ae13f214b0a4126f4f09aaa19d68
fetched_at: '2026-06-29T00:10:50.671040+00:00'
page_id: '562488410'
product: rm
source: tdn-rm
title: Parametrização para o Ressarcimento/Complemento de ICMS ST - Paraná (ADRC-ST)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=562488410
version: 7
---

Fique atento as parametrizações para a correta geração do arquivo referente ao Ressarcimento/Complemento de ICMS ST - Paraná (ADRC-ST).

#### **Cadastro do Produto**

Revise o Cadastro de Produtos para que todas as mercadorias tributadas pelo ICMS ST estejam com o Anexo “**Dados Fiscais por UF**” corretamente preenchido.

Anexo Dados Fiscais

#### **Natureza de Operação**

No Cadastro de CFOP marque corretamente as operações que devem ser consideradas nos cálculos na pasta “Outros Dados”.

**IMPORTANTE:** Para ser considerado na rotina ADRC-ST a opção "Operação com Ressarcimento/Complemento de ST" deve estar marcada.

CFOP

#### **Associação Lançamentos de Saída**

Para os contribuintes não varejistas o Processo de associar os lançamentos de entrada aos lançamentos de saída deve ocorrer todo mês, antes do encerramento da Sub-apuração.Para saber mais sobre este processo, consulte este link: [Associação Lançamentos de Saída](https://tdn.totvs.com/pages/viewpage.action?pageId=438273534).

Processo de Associação

#### **Definindo os registros que não devem ser gerados na rotina**

Na tela de geração da rotina ADRC-ST, o parâmetro de tela "Desconsiderar Registros", quando informado, permite que o arquivo final gerado pela rotina desconsidere determinado registro. Este parâmetro pode aceitar os seguintes valores:

| Valores válidos |
| --- |
| 1200 |
| 1300 |
| 1400 |
| 1500 |

Mais de um valor pode ser informado na geração da rotina, para isso basta utilizar o delimitador ponto-vírgula (;) ou  vírgula (,), por exemplo:

* 1200;1300
* 1400,1500

Processo de AssociaçãoInformação

Os registros filhos como 1000, 1100,1110, 1120, 1210, 1220, 1310,1320, 1410, 1420, 1510 e1520 não serão desconsiderados da geração da rotina, caso sejam informados no parâmetro da geração da rotina.
