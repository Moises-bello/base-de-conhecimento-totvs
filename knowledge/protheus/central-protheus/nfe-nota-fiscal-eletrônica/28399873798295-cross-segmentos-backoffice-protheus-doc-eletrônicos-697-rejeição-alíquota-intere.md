---
article_id: 28399873798295
category: NFe - Nota Fiscal Eletrônica
content_hash: acadfa915d30e0e0a12bcfc9e66ff33fd812b17b89df240050e445bbc5b28fb2
fetched_at: '2026-06-28T22:40:00.034297+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 697 Rejeição  –
  Alíquota interestadual do ICMS com origem diferente do previsto
type: support-article
updated_at: '2025-01-09T13:04:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28399873798295-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-697-Rejei%C3%A7%C3%A3o-Al%C3%ADquota-interestadual-do-ICMS-com-origem-diferente-do-previsto
---

**Dúvida**Como corrigir a Rejeição 697 – Alíquota interestadual do ICMS com origem diferente do previsto ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Há duas validações para a Rejeição “697 – Alíquota interestadual do ICMS com origem diferente do previsto”. Veja a seguir a descrição das duas situações onde haverá rejeição:

Primeira situação:

Quando for emitida uma NFe com Alíquota Interestadual (pICMSInter) igual 4.00% (quatro por cento) e a Origem da Mercadoria for IGUAL a:

0 – Nacional, exceto as indicadas nos códigos 3, 4, 5 e 8;  
4 – Nacional, cuja produção tenha sido feita em conformidade com os processos produtivos básicos de que tratam as legislações citadas nos Ajustes;  
5 – Nacional, mercadoria ou bem com Conteúdo de Importação inferior ou igual a 40%;  
6 – Estrangeira – Importação direta, sem similar nacional, constante em lista da CAMEX e gás natural;  
7 – Estrangeira – Adquirida no mercado interno, sem similar nacional, constante lista CAMEX e gás natural.

Será retornado a rejeição “697 – Alíquota interestadual do ICMS com origem diferente do previsto”.

<ICMS>  
<ICMS00>  
**<orig>4</orig>**  
<CST>00</CST>  
<modBC>3</modBC>  
<vBC>1000.00</vBC>  
<pICMS>7.00</pICMS>  
<vICMS>70.00</vICMS>  
</ICMS00>  
</ICMS>

<ICMSUFDest>  
<vBCUFDest>1000.00</vBCUFDest>  
<pFCPUFDest>2.00</pFCPUFDest>  
<pICMSUFDest>17.00</pICMSUFDest>  
**<pICMSInter>4.00</pICMSInter>**  
<pICMSInterPart>40.00</pICMSInterPart>  
<vFCPUFDest>20.00</vFCPUFDest>  
<vICMSUFDest>52.00</vICMSUFDest>  
<vICMSUFRemet>78.00</vICMSUFRemet>  
</ICMSUFDest>

Para a correção será considerado que a Alíquota Interestaduais (pICMSInter) foi informada corretamente, logo será necessário alterar a origem da mercadoria, alterando o conteúdo do campo **B1\_ORIGEM**.

**Correção da primeira situação**

Para a alíquota informada de 4.00% (quatro por cento), a origem da mercadoria deve ser sempre: 1, 2, 3 ou 8. No exemplo, foi informado a origem “3 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%”. Outra correção necessária nesse exemplo, por se tratar de uma operação interestadual com mercadoria de origem estrangeira, o Grupo de ICMS (Normal) deve ter Alíquota (pICMS) de 4.00% (quatro por cento). Veja a seguir o exemplo corrigido:

<ICMS>  
<ICMS00>  
**<orig>3</orig>**  
<CST>00</CST>  
<modBC>3</modBC>  
<vBC>1000.00</vBC>  
**<pICMS>4.00</pICMS>**  
<vICMS>40.00</vICMS>  
</ICMS00>  
</ICMS

<ICMSUFDest>  
<vBCUFDest>1000.00</vBCUFDest>  
<pFCPUFDest>2.00</pFCPUFDest>  
<pICMSUFDest>17.00</pICMSUFDest>  
**<pICMSInter>4.00</pICMSInter>**  
<pICMSInterPart>40.00</pICMSInterPart>  
<vFCPUFDest>20.00</vFCPUFDest>  
<vICMSUFDest>52.00</vICMSUFDest>  
<vICMSUFRemet>78.00</vICMSUFRemet>  
</ICMSUFDest>

**Segunda situação:**

Quando for emitida uma NFe com Alíquota Interestadual (pICMSInter) igual a 7.00% (sete por cento) ou 12.00% (doze por cento) e a Origem da Mercadoria for IGUAL a:

1 – Estrangeira – Importação direta, exceto a indicada no código 6; ou  
2 – Estrangeira – Adquirida no mercado interno, exceto a indicada no código 7; ou  
3 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 40% e inferior ou igual a 70%; ou  
8 – Nacional, mercadoria ou bem com Conteúdo de Importação superior a 70%.

Será retornado a rejeição “697 – Alíquota interestadual do ICMS com origem diferente do previsto”.

<ICMS00>  
**<orig>3</orig>**  
<CST>00</CST>  
<modBC>3</modBC>  
<vBC>1000.00</vBC>  
<pICMS>4.00</pICMS>  
<vICMS>40.00</vICMS>  
</ICMS00>

<ICMSUFDest>  
<vBCUFDest>1000.00</vBCUFDest>  
<pFCPUFDest>2.00</pFCPUFDest>  
<pICMSUFDest>17.00</pICMSUFDest>  
**<pICMSInter>7.00</pICMSInter>**  
<pICMSInterPart>40.00</pICMSInterPart>  
<vFCPUFDest>20.00</vFCPUFDest>  
<vICMSUFDest>40.00</vICMSUFDest>  
<vICMSUFRemet>60.00</vICMSUFRemet>  
</ICMSUFDest>

Para a alíquota **pICMSInter** informada de 7.00% (sete por cento) ou 12.00% (doze por cento), a origem da mercadoria deve ser sempre **0, 4, 5, 6 ou 7**. Para corrigir o exemplo, foi informado a origem “4 – Nacional, altere o campo **B1\_ORIGEM.**  Veja a seguir o exemplo corrigido:

ICMS00>  
**<orig>4</orig>**  
<CST>00</CST>  
<modBC>3</modBC>  
<vBC>1000.00</vBC>  
<pICMS>4.00</pICMS>  
<vICMS>40.00</vICMS>  
</ICMS00>

<ICMSUFDest>  
<vBCUFDest>1000.00</vBCUFDest>  
<pFCPUFDest>2.00</pFCPUFDest>  
<pICMSUFDest>17.00</pICMSUFDest>  
**<pICMSInter>7.00</pICMSInter>**  
<pICMSInterPart>40.00</pICMSInterPart>  
<vFCPUFDest>20.00</vFCPUFDest>  
<vICMSUFDest>40.00</vICMSUFDest>  
<vICMSUFRemet>60.00</vICMSUFRemet>  
</ICMSUFDest>

Caso haja necessidade de alterar a alíquota **pICMSInter** será necessário entrar em contato com suporte fiscal.

## [Exceções e observações](https://oobj.com.br/bc/rejeicao-697-como-resolver/#excecoes-e-observacoes)

A regra de validação 697 não se aplica, em produção, para NFe com data de emissão anterior a 01/07/2016.

## [Regras de validação da Sefaz](https://oobj.com.br/bc/rejeicao-697-como-resolver/#regras-de-validacao-da-sefaz)

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Campo-Seq | Modelo | Regra de Validação | Aplic. | Msg | Efeito | Descrição Erro |
| NA09-10 | 55 | Se informada alíquota interestadual (tag:pICMSInter) de 4% e Origem da mercadoria difere de produto importado (tag:orig<>1,2,3,8) Exceção: A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. (NT 2015.003) | Obrig. | 697 | Rej. | Rejeição: Alíquota interestadual do ICMS com origem diferente do previsto [nItem:999] |
| NA09-20 | 55 | Se informada alíquota interestadual (tag:pICMSInter) de 7% ou 12% e Origem da mercadoria de produto importado (tag:orig=1,2,3,8) Exceção: A regra de validação não se aplica, em produção, para Nota Fiscal com data de emissão anterior a 01/07/2016. (NT 2015.003) | Obrig. | 697 | Rej. | Rejeição: Alíquota interestadual do ICMS com origem diferente do previsto [nItem:999] |
MOC 7.0 – Anexo I – Leiaute e Regras de Validação da NFe e da NFCe – NA. Item / ICMS para a UF de Destino
