---
article_id: 25917625974551
category: Materiais - Compras (SIGACOM)
content_hash: 843fdab7cdf740e945c6362cd4531c4f04f9501c52b59d6fec2507706e1c4b1b
fetched_at: '2026-06-28T22:41:17.389092+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de entrada
  help N3_VORIG1 AF012TPNEG Valor deste Item não pode ser negativo
type: support-article
updated_at: '2024-08-26T18:07:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25917625974551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-entrada-help-N3-VORIG1-AF012TPNEG-Valor-deste-Item-n%C3%A3o-pode-ser-negativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25917617160855) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao tentar incluir um documento de entrada, cujo produto gerará um ativo, o sistema exibe o help :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25917617162135)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – A partir da versão 12

**Solução**Por padrão o campo calcula os campos de valor da tabela SN3, quando o ativo é integrado pelo documento de entrada, verificando a moeda preenchida no parâmetro **[MV\_ATFMOED](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017523572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-INCONSIST%C3%8ANCIA-REFERENTE-A-MOEDA-NA-VERIFICA%C3%87%C3%83O-DE-INTEGRIDADE)**.

No momento de incluir o ativo  o sistema estaá tentando calcular o valor do ativo, porém este está sendo calculado e esteja ficando negativo, a tela de mensagem exibirá o campo N3\_VORIG1, ou seja, o sistema está calculando o valor do valor do ativo através do conteúdo do parâmetro **MV\_VLRATF** e no **MV\_ATFMOED o conteúdo será 1**.

**<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025906972-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-valor-original-do-bem-na-classifica%C3%A7%C3%A3o-do-ativo-quando-a-nota-%C3%A9-lan%C3%A7ada-pelo-compras?source=search>**

**<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016120672-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-Ativo-Fixo-x-Frete-IPTU-Seguros-Licen%C3%A7a-de-Uso?source=search>**

O conteúdo padrão do parâmetro **MV\_VLRATF** é : **(SD1->D1\_TOTAL-SD1->D1\_VALDESC)+If(SF4->F4\_CREDIPI=="S",SD1->D1\_VALIPI,0)-IIf(SF4->F4\_CREDICM=="S",SD1->D1\_VALICM,0), porém o cliente pode alterá-lo de acordo com a sua necessidade de cálculo do valor do ativo.**

Abaixo um exemplo do sistema estar calculando o valor do ativo negativo e exibindo o help :

Temos uma nota de entrada cujo D1\_TOTAL ( total do item ) = R$ 250,00.

Nessa nota não há desconto, mas há uma despesa de R$ 700,00 e um valor de frete de R$150,00  ( reparem que a configuração padrão do MV\_VLRTAF não considera por padrão o frete e nem a despesa ). O TES usado está com o campo F4\_CREDIPI=N, então se na nota tiver IPI, ele não será somado, pois o conteúdo padrão do parâmetro diz que só somará o valor do IPI, se o F4\_CREDIPI=S.

Porém o TES usado está com o campo F4\_CREDICM = S, então pela configuração do parâmetro o valor do ICM calculado na nota, será subtraído do D1\_TOTAL ( Total do item ). Nesse exemplo o valor do ICMS calculado pelo sistema foi de R$ 330,00.

Quando o sistema executa a configuração do MV\_VLRATF :

(SD1->D1\_TOTAL-SD1->D1\_VALDESC)+If(SF4->F4\_CREDIPI=="S",SD1->D1\_VALIPI,0)-IIf(SF4->F4\_CREDICM=="S",SD1->D1\_VALICM,0)

250,00 -0,00(não há desconto)+0,00(F4\_CREDIPI=N)-330,00(F4\_CREDICM=S) = R$ -80,00.

Um ativo não pode ser integrado com valor negativo no sistema. Nesse cenário, o cliente precisará rever a configuração do parâmetro para que o sistema não calcule um valor negativo para o ativo integrado pela rotina de documento de entrsada.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
