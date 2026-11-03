---
article_id: 4411045503511
category: Materiais - Compras (SIGACOM)
content_hash: 51b08e98bf860ef32184c271d42c4367e41fe067e7af0b5742b7ce8ac8c6be05
fetched_at: '2026-06-28T22:41:25.492968+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos Totvs Backoffice Protheus - SIGACOM - HELP SN3DETAIL VLDDATA_LINEPOST
  SN3DETAIL ATFVALORUF
type: support-article
updated_at: '2024-06-20T13:32:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411045503511-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-HELP-SN3DETAIL-VLDDATA-LINEPOST-SN3DETAIL-ATFVALORUF
---

**Ocorrência**Ao realizar a entrada de um documento via MATA103 que atualiza Ativo, ocorre o HELP SN3DETAIL VLDDATA\_LINEPOST SN3DETAIL ATFVALORUF

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411048911895)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - A partir da versão 11.80  
  
**Causa**O Help pode estar ocorrendo devido alguma alteração/customização incorreta na regra do parâmetro "MV\_VLRATF".  
  
**Solução**Corrigir a expressão para o padrão do sistema, ou verificar se a expressão criada está correta.  
Por padrão o conteúdo da validação do parâmetro deve ser:

Conteúdo do Dicionário SX6:

**MV\_VLRATF** = (SD1->D1\_TOTAL-SD1->D1\_VALDESC)+If(SF4->F4\_CREDIPI=="S",0,SD1->D1\_VALIPI)-IIf(SF4->F4\_CREDICM=="S",SD1->D1\_VALICM,0)

Verificar além disso o conteúdo do parâmetro **MV\_ATFMOED**:

* Se o parâmetro MV\_ATFMOED estiver igual = 1, o compras não irá disparar mensagem e deverá alimentar o campo N3\_VORIG1, visto que é a moeda 1 é o Real, por padrão.
* Se o parâmetro MV\_ATFMOED estiver igual = 3, o compras deverá alimentar o campo N3\_VORIG3. Mas para que o sistema consiga preencher e gravar esse campo, será necessário que haja, cadastrado no cadastro de moedas do sistema, uma taxa de conversão para a moeda 3. Caso contrário, o sistema não consegue gravar o campo N3\_VORIG3 com o devido valor, por conta da ausência de taxa no cadastro de moedas.

**Importante :** A Taxa de conversão para a moeda precisa estar cadastrada no mesmo dia de emissão da nota de entrada.

***Saiba Mais :***

[MV\_VLRATF - INTEGRAÇÃO DOCUMENTO DE ENTRADA COM ATIVO FIXO](https://tdn.totvs.com/pages/releaseview.action?pageId=235596102)

[MP - SIGAATF - INCONSISTÊNCIA REFERENTE A MOEDA NA VERIFICAÇÃO DE INTEGRIDADE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017523572-MP-SIGAATF-INCONSIST%C3%8ANCIA-REFERENTE-A-MOEDA-NA-VERIFICA%C3%87%C3%83O-DE-INTEGRIDADE-)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
