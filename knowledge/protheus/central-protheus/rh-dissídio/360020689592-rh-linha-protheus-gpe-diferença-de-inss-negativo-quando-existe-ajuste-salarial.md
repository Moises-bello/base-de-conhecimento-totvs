---
article_id: 360020689592
category: RH - Dissídio
content_hash: 0a44617e4002b7d979029e6739ec6e1f197f4471f51191141fbd02cb9d7f7073
fetched_at: '2026-06-28T22:43:43.560845+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Diferença de INSS negativo quando existe ajuste
  salarial
type: support-article
updated_at: '2025-08-20T13:03:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020689592-RH-Linha-Protheus-GPE-Diferen%C3%A7a-de-INSS-negativo-quando-existe-ajuste-salarial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34314751767959) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Quando funcionário possui férias partidas calculadas com o parâmetro [MV\_DINSSFM](http://tdn.totvs.com/x/JCaLFQ) preenchido com "S" ou "R" e existe ajuste salarial antes do cálculo do dissídio, no dissídio a verba de INSS Folha pode ficar negativa.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12  
  
**Solução**A utilização do parâmetro MV\_DINSSFM com "S" ou "R" indica que os valores de INSS apurados no cálculo de férias não serão alterados na folha, logo, qualquer diferença de INSS ocasionada pela soma das verbas de férias e folha será paga exclusivamente na verba de INSS Folha.

No exemplo abaixo foi feito um cálculo de férias partidas com início em setembro:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314751774103)

Quando existe um aumento salarial, no mês seguinte ao início das férias, as diferenças de férias serão calculadas e pagas na folha. Entretanto, devido o parâmetro MV\_DINSSFM indicar que o INSS não deve ser alterado, é mantido o valor calculado no roteiro de férias no mês anterior, e todo o excedente é lançado na verba de INSS da Folha.

Abaixo a folha de outubro do mesmo funcionário com aumento salarial, repare que o valor da verba de INSS Férias é mantido, apesar da diferença nas demais verbas:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314725292183)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314751776279)

Repare que toda a diferença de INSS que deveria ter sido lançada na verba de INSS Férias foi gerada na verba de INSS Folha:

Base INSS = Salário + Verbas de Férias => 2728,61

INSS Total => 2728,61 \* 9% = 245,57

INSS Férias => 83,55

INSS Folha => INSS TOTAL - INSS Férias = 162,02

Posteriormente, ao efetuar o cálculo do dissídio, o roteiro de férias será inteiramente recalculado com o novo salário, e uma nova base e valores de INSS serão encontrados. Estes valores serão gerados na folha de dissidio juntamente com o novo valor de INSS folha, que será obtido da soma de todas as verbas de férias e folha com incidência para INSS, subtraindo o novo INSS de férias apurado, podendo neste momento o total de INSS de Folha apurado ser menor que o total de INSS de Folha pago no cálculo original, que foi aumentado por conta da verba de INSS não poder ser alterada.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314751779095)

No cálculo do dissídio as férias serão recalculadas, portanto o valor do INSS Férias será maior, enquanto o valor do INSS Folha será diminuído, já que ele teve um acréscimo no mês de outubro devido a não alteração da verba de férias.

O cálculo com o novo salário será o seguinte:

Base INSS Férias => (Férias + 1/3 Férias) =>  859,51 + 286,50 = 1146,01

INSS Férias => 1146,01 \* 8% = 91,68

Base INSS Folha => Base INSS Férias + Salário => 1146,01 + 1645,00 = 2791,01

INSS Total => 2791,01 \* 9% = 251,19

INSS Folha => INSS Total - INSS Férias => 251,19 - 91,68 = 159,51

Embora a diferença seja negativa, o valor que será descontado do funcionário será a soma das verbas de INSS Férias e INSS Folha, que no caso estão corretas, conforme cálculo abaixo:

INSS Total Anterior = 2728,61 \* 9% = 245,57 (162,02 + 83,55)

INSS Total Dissídio = 2791,01 \* 9% = 251,19 (159,51 + 91,68)

Diferença de INSS = 251,19 - 245,57 = 5,62 ou 8,13 - 2,51 = 5,62  
  
**Saiba Mais**O conteúdo também está disponível no *link* a seguir: [GPEM690 - Diferença de INSS negativo](http://tdn.totvs.com/pages/viewpage.action?pageId=444611368)
