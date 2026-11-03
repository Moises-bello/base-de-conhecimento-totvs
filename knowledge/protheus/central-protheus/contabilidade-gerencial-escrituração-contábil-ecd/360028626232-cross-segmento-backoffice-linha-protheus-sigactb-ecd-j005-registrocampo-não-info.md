---
article_id: 360028626232
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 4b5e47072915bbef45b3921d57866b1e4e373a7c99293794c87225e087de5c3b
fetched_at: '2026-06-28T22:40:44.779525+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB :ECD : J005 - Registro/Campo
  não informado ou invalido (No Balanço Patrimonial, o somatório do saldo final...)'
type: support-article
updated_at: '2025-05-20T19:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028626232-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J005-Registro-Campo-n%C3%A3o-informado-ou-invalido-No-Balan%C3%A7o-Patrimonial-o-somat%C3%B3rio-do-saldo-final
---

**Ocorrência**

J005 - Registro/Campo não informado ou invalido:  
No Balanço Patrimonial, o somatório do saldo final (J100.VL\_CTA\_FIN) das linhas de detalhe (J100.IND\_COD\_AGL = "D") do Ativo (J100.IND\_GRP\_BAL = "A") está diferente do somatório do saldo final (J100.VL\_CTA\_FIN) das linhas de detalhe (J100.IND\_COD\_AGL = "D") do Passivo (J100.IND\_GRP\_BAL = "P").

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029717932)

**Ambiente**Microsiga Protheus – Contabilidade Gerencial  – A partir da versão 11.80

**Requisitos**

* Caso tenha gerado a ECD com [Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046818313-MP-SIGACTB-ECD-I100-Centro-de-Custo?source=search)verifique se o centro de custo esta devidamente conciliado
* Veja se o procedure da ECD [MV\_CTBSPRC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007132632-MP-SIGACTB-Habilitar-procedures-din%C3%A2mica-na-gera%C3%A7%C3%A3o-da-ECD?source=search) esta configurado
* Seguir as instruções [Aqui descritas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025142372-MP-SIGACTB-Como-atualizar-o-ECD-?source=search)
* Aplique**o Pacote Acumulado Contábil + [Instalação de Procedure nele existente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011410951-MP-SIGACTB-SIGAATF-Instala%C3%A7%C3%A3o-de-Procedure-?source=search):**

  **12.1.27**: <https://suporte.totvs.com/portal/p/10098/download?e=955975>

  **12.1.33**: <https://suporte.totvs.com/portal/p/10098/download?e=1065188>

* Obs : necessário aplicação deste pacote para que os fonte CTBXATU , CTBA190 e os demais fontes de atualização de saldo estejam atualizados
* Um vez que os pacotes foram aplicador e as procedures atualizadas Realize um reprocessamento de saldo, pois os registro são gerado com base na tabelas de saldo
* realize a conciliação do bloco J100 e veja se o saldo Anterior e movimento no período estão  correto em comparação com o relatório de balanço gerado no Protheus :  [J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)

**Causa**O erro informa que o balanço registro J100 não está correto. (Pode ocorrer devido a algumas contas novas serem criadas e não ajustada no Balanço Patrimonial verifique esse ponto).  
  
**Solução**  
Reveja a documentação sobre como gerar o registro J100, observe o campo Coluna, no cadastro da visão gerencial, está relacionado ao ativo e passivo.  
[MP- SIGACTB : ECD : J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)  
   
É importante rever as informações do link a baixo, explica como conferir as informações, inclusive do balanço patrimonial.  
Se necessário estornar a apuração e refazer.

**Saiba mais**  
[MP - SIGACTB : PRÉ-REQUISITOS PARA GERAR A ECD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028834291-MP-SIGACTB-PR%C3%89-REQUISITOS-PARA-GERAR-A-ECD?source=search)
