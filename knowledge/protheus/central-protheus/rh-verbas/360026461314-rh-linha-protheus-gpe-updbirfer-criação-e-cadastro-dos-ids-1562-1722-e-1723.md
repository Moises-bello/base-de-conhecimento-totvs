---
article_id: 360026461314
category: 'RH - Verbas '
content_hash: 40fe0f7817ef20896005512db3102971e74e39e80c7c2a32120f0ca84a53af4e
fetched_at: '2026-06-28T22:43:20.156387+00:00'
product: protheus
section_id: 360010838314
source: central-protheus
title: RH - Linha Protheus - GPE - UPDBIRFER - Criação e cadastro dos Ids 1562, 1722
  e 1723
type: support-article
updated_at: '2026-06-24T14:11:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026461314-RH-Linha-Protheus-GPE-UPDBIRFER-Cria%C3%A7%C3%A3o-e-cadastro-dos-Ids-1562-1722-e-1723
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26567593614103) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Criação e cadastros dos Ids 1562, 1722 e 1723  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Quando o funcionário possui férias no mês, o cálculo de férias é gerado no evento S-1210 como tipo de pagamento 7 e também é gerado as verbas de férias no evento S-1200. Isso está correto, pois é necessário para a apuração correta do INSS.

Porém, a base de IRRF de férias, o abono pecuniário e a dedução da previdência oficial acabam ficando duplicadas no retorno do evento S-5002 pois o sistema do eSocial também considerou as verbas de férias enviadas no evento S-1200, além da enviada no evento S-1210, na apuração da base de IRRF.  
  
Efetuado a criação do Id de cálculo que serão **gerados no cálculo da folha.**  
**1562** - Base de IRRF Férias s/ dedução   
**1722** - Informativa Dedutora do Abono Férias   
**1723** - Informativa da Dedução INSS Base IR Férias  
  
**Após as substituições das verbas de férias em 2026 somente o ID 1722 continuará sendo gerado no S-1200 FOL. Os identificadores 1562 e 1723 devem ter incidencia IRRF 9 para 2026.**

A verba de Id **1562** tem o objetivo de deduzir os valores de provento de férias da base de IRRF de férias quando for efetuado o envio do evento S-1200. Essa verba será **composta pela somatória das verbas de provento de férias com incidência 13 para IR eSocial** e não irá alterar o líquido de folha do funcionário por se tratar de base e por não ter incidências para folha. Dessa forma, tanto a base de INSS quanto a base de IRRF apurados pelo eSocial ficarão corretos.

* Para a geração do ID 1562, o sistema vai considerar apenas as verbas que são do tipo provento e com SIM para IR.  
  O fonte fará uma validação para pegar as mesmas verbas que estão na SRD e SRR e após isso validará as verbas que são do tipo provento e com SIM para IR, então a soma do valor leva no ID 1562

A verba deverá ser cadastrada com natureza informativa **9989**, de tipo **base (desconto)** para ser utilizada como Informativa Dedutora no eSocial e com incidência **13** para IR, para ser deduzida da base de IRRF de férias quando efetuado o envio do evento S-1200.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26567605128727)

A verba de Id **1722** tem o objetivo de deduzir os valores de abono pecuniário quando for efetuado o envio do evento S-1200. Essa verba será composta pela somatória das verbas de provento de abono pecuniário (Ids de cálculo 0074, 0079, 0094, 0095, 0205, 0206, 0207, 0208, 0622, 0623, 0632, 0633, 0634, 0635, 1312, 1313, 1314, 1315, 1316, 1317, 1318, 1319, 1320, 1321, 1322, 1323, 1324, 1325, 1326, 1327, 1330, 1331, 1407, 1408, 1409, 1410, 1416, 1417, 1418, 1419, 1450 e 1451 ou campo RV\_REFABON, se existir, configurado com 1) sem incidência para IR e não irá alterar o líquido de folha do funcionário por se tratar de base e por não ter incidências para folha. 

A verba deverá ser cadastrada com natureza informativa **9989**, de tipo **base (desconto)** para ser utilizada como Informativa Dedutora no eSocial e com incidência **75** para IR, para ser deduzida da base de abono pecuniário quando efetuado o envio do evento S-1200.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26567605138455)

A verba de Id **1723** tem o objetivo de deduzir o valor da dedução de INSS da base de IR de Férias quando for efetuado o envio do evento S-1200. Caso seja a verba do Id de cálculo **0168** que possua incidência **43** para IR, o valor dessa verba será considerado para a geração da verba de ID 1723; caso seja a verba de Id de cálculo **0065** que possua incidência **43** para IR, é o valor dessa verba (e não o valor da verba do Id 0168) que será considerado para a geração da verba de Id 1723. Além disso, a verba do Id 1723 não irá alterar o líquido de folha do funcionário por se tratar de base e por não ter incidências para folha. 

A verba deverá ser cadastrada com natureza informativa **9989**, de tipo **base (provento)** para ser utilizada como Informativa no eSocial e com incidência **43** para IR, para ser somada (já que a dedução é um desconto) à base de dedução da base de cálculo do IR de Férias quando efetuado o envio do evento S-1200.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26567605143831)  
  
Por exemplo, segue abaixo como ficaria o cálculo de folha do funcionário com férias partidas:

| Id de Cálculo | Descrição | Valor |
| --- | --- | --- |
| 0072 | Férias | R$ 2.000,00 |
| 0073 | Férias Mês Seguinte | R$ 2.000,00 |
| 0077 | 1/3 Férias | R$ 700,00 |
| 0078 | 1/3 Férias Mês Seguinte | R$ 700,00 |
| 0082 | Média de Horas | R$ 100,00 |
| 0083 | Média de Horas Mês Seguinte | R$ 100,00 |
| 0065 | INSS Férias | R$ 252,00 |
| 0168 | Dedução INSS Base IR Férias | R$ 504,00 |
| 0205 | Abono Mês Seguinte | R$ 2.000,00 |
| 0206 | 1/3 Abono Mês Seguinte | R$ 700,00 |
| 0232 | INSS Férias Mês Seguinte | R$ 252,00 |
| 0633 | Média de Horas Abono Mês Seguinte | R$ 100,00 |
| 1562 | Base de IRRF Férias s/ Dedução | R$ 5.600,00 |
| 1722 | Informativa Dedutora do Abono Férias | R$ 2.800,00 |
| 1723 | Informativa da Dedução INSS Base IR Férias | R$ 504,00 |

Por exemplo, segue abaixo como ficaria o cálculo de folha do funcionário no segundo mês das férias:

| Id de Cálculo | Descrição | Valor |
| --- | --- | --- |
| 0065 | INSS Férias | R$ 252,00 |
| 0072 | Férias | R$ 2.000,00 |
| 0074 | Abono | R$ 2.000,00 |
| 0077 | 1/3 Férias | R$ 700,00 |
| 0079 | 1/3 Abono | R$ 700,00 |
| 0082 | Média de Horas | R$ 100,00 |
| 0164 | Fer. Pag. Mês Ant. | R$ 2.548,00 |
| 0622 | Média de Horas Abono | R$ 100,00 |
| 1449 | Abo. Pag. Mês Ant. | R$ 2.800,00 |
| 1562 | Base de IRRF Férias s/ Dedução | R$ 2.800,00 |
| 1722 | Informativa Dedutora do Abono Férias | R$ 2.800,00 |

**Atenção****: Dedução INSS Base IR Férias**

A verba de ID 0168 **NÃO** transita no segundo mês de férias, como ocorre com as verbas de férias e abono, pois não existe verba de dedução de INSS da base de IR de férias de mês seguinte.

Dessa forma, no segundo mês de férias **NÃO** haverá a geração da **verba de ID 1723** pois não haverá necessidade de efetuar dedução desse valor na declaração para o eSocial.  
  
**Importante**  
Também foi disponibilizado o rdmake **UPDBIRFER**que irá efetuar o processamento de todos os funcionários que tiveram férias, conforme filtro definido na geração (filial, matrícula e período de/até), para gerar as verbas de ID 1562, 1722 e/ou 1723 no movimento acumulado (tabela SRD) do funcionário.

Para a utilização da rotina, deverá ser efetuado a inclusão manual no menu do módulo SIGAGPE, cadastrando o item como função de **usuário**.

Ao término do processamento, o log de ocorrências irá listar as verbas que foram geradas para cada funcionário, separados por Filial, Matrícula e Período.

**IRRF Férias**

A verba de IRRF de férias deixou de ser gerada no recibo de pagamento da folha ao efetuar a geração do evento S-1210, conforme documentação disponível na atualização do link: [3453497 DRHESOCP-6830 S1210: Ajuste para não levar valores de IR de férias no demonstrativo de pagamento da folha.](http://tdn.totvs.com/pages/viewpage.action?pageId=389546727)

**Saiba Mais**  
[Boletim técnico: DT Criação Ids 1562, 1722 e 1723](http://tdn.totvs.com/pages/viewpage.action?pageId=394210801)  
[RH - Verbas](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010838314-RH-Verbas)
