---
content_hash: d8dfecd2d9cfb6ba5a7b2242ff39a78bc547f6d88e96177cacbd9e13f1754160
fetched_at: '2026-06-29T00:05:48.049065+00:00'
page_id: '1022368035'
product: rm
source: tdn-rm
title: Considerações sobre a Base de Cálculo para o IVA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1022368035
version: 5
---

## **01. Visão Geral**

Com a chegada e transição da Reforma Tributária, temos para 2026 e anos conseguintes a [tributação gradual](https://www12.senado.leg.br/noticias/materias/2024/12/16/novos-tributos-comecam-a-ser-testados-em-2026-e-transicao-vai-ate-2033) do IVA Dual, que é composto por IBS (Imposto sobre Bens e Serviços), CBS (Contribuição sobre Bens e Serviços) e IS (Imposto Seletivo). Dentro do IVA Dual, é de caráter **obrigatório** a declaração do IBS e da CBS à partir de primeiro de Janeiro de 2026, conforme [Lei Complementar 214 de 2025](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214.htm). Entretanto, visando minimizar a possibilidade de não faturamento das empresas – caso haja algum erro de ambiente no envio de documentos eletrônicos com os novos tributos – foi disponibilizada a [Nota Técnica 2025.002 v1.33](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=AklZnck3o6I=), que descreve em sua seção de Detalhamento do Cronograma:

Preenchimento dos campos IBS/CBS é facultativo. Se preenchidos, as RV serão aplicadas.

Preenchimento dos campos IBS/CBS não será exigido por regra de validação, porém permanece obrigatório conforme a legislação vigente. Para as NF-e e NFC-e com IBS/CBS as RV serão aplicadas. Com valor jurídico para os novos tributos a partir de 01/01/2026.

Ou seja, no cenário específico em que envio dos novos tributos seja impossibilitado por algum problema de ambiente do órgão autorizador da NF-e/NFC-e, existe a possibilidade de não demonstração dos novos tributos. **Essa escolha é de responsabilidade do emitente da nota fiscal**.

## **02. Objetivo**

Este documento visa explicar e exemplificar a possibilidade de não geração do IBS e da CBS ao zerar a base de cálculo dos seus tributos no TOTVS Gestão de Estoque, Compras e Faturamento, através do cadastro global de [Fórmulas](https://tdn.totvs.com/pages/viewpage.action?pageId=403746924).

## **03. Composição da Base de Cálculo e como zerar**

Conforme Notas Técnicas da RTC disponibilizadas no [Portal da NF-e](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=), a Base de Cálculo (BC) do IBS e da CBS é composta pela totalização das tags:

| Soma | Subtrai |
| --- | --- |
| (+) vProd | (-) vDesc |
| (+) vServ | (-) vPIS |
| (+) vFrete | (-) vCOFINS |
| (+) vSeg | (-) vICMS |
| (+) vOutro | (-) vICMSUFDest |
| (+) vII | (-) vFCP |
|  | (-) vFCPUFDest |
|  | (-) vICMSMono |
|  | (-) vISSQN |

Considerando a tabela acima, podemos pegar o valor dos campos do item do movimento que irão preencher essas tags para realizar o cálculo da BC do IBS/CBS no movimento, conforme o seguinte **exemplo** de fórmula:

false

```
KQT*KPU + TABITM ('RATEIOFRETE' , 'V') +  
TABITM ('RATEIODESP' , 'V') - KDE - TABITM ('RATEIODESC' , 'V')
```

> ```
> Importante considerar que a tributação para o IBS e a CBS são realizadas no item do movimento, e não no movimento em si.
> ```

Existe tanto a possibilidade de criar uma nova fórmula para a BC do IBS/CBS quanto editar uma fórmula já existente, caso essa edição não gere impacto em outros cálculos da nota.   
Para zerar a BC do IBS/CBS, podemos utilizar do exemplo acima e fazer uma condição simples:

false

SE TABMOV('CODFILIAL','I') = 2 E TABMOV('CODTMV','S')= '2.2.02' ENTAO  
0  
SENAO   
KQT\*KPU + TABITM ('RATEIOFRETE' , 'V') +  
TABITM ('RATEIODESP' , 'V') - KDE - TABITM ('RATEIODESC' , 'V')  
FIMSE

Vamos considerar que temos uma filial de SP, cujo código seja 2, e que ela utilize o código de movimento 2.2.02 para envio de NF-e. A condição "SE TABMOV('CODFILIAL','I') = 2 E TABMOV('CODTMV','S')= '2.2.02'" irá se aplicar para essa filial e movimento específicos, assim, zerando sua base de cálculo. Caso qualquer outra filial e/ou outros movimentos sejam utilizados, a BC será calculada normalmente.  
Mas, caso o cenário se aplique a mais de uma filial e a mais de um tipo de movimento, basta incluí-los na condição da fórmula. Outro exemplo:

false

SE (TABMOV('CODFILIAL','I') = 2 OU TABMOV('CODFILIAL','I') = 3 OU TABMOV('CODFILIAL','I') = 4) E (TABMOV('CODTMV','S')= '2.2.02' OU TABMOV('CODTMV','S')= '2.2.01') ENTAO  
0  
SENAO   
KQT\*KPU + TABITM ('RATEIOFRETE' , 'V') +  
TABITM ('RATEIODESP' , 'V') - KDE - TABITM ('RATEIODESC' , 'V')  
FIMSE

No cenário acima, a BC será zerada para as filiais 2, 3 e 4, cujos tipos de movimento sejam 2.2.02 ou 2.2.01.

Também é possível utilizar outras funções de fórmula conforme seu cenário e necessidade. O importante, nesse caso, é que aplique as condições conforme desejado para que a BC do IBS/CBS seja zerada.

**04. Gatilhos e impactos de zerar a Base de Cálculo**

Ao zerar a BC do IBS/CBS, por mais que o tributo fique salvo no movimento com seu valor e BC zerados, as tags referentes ao IBS e à CBS automaticamente não serão geradas na NF-e/NFC-e. Logicamente, ao escriturar a nota/movimento, seus valores também não serão escriturados no lançamento fiscal, tampouco apurados no período de apuração.  
Remover o valor da BC dos tributos pela fórmula evita a necessidade de mudar a parametrização do movimento - não sendo necessário remover os tributos para não gerar as tags da RTC. Além disso, também permite a rastreabilidade das informações pelo movimento, pois sempre será possível verificar quando os tributos estiverem no movimento e, assim, fazer o comparativo com as notas enviadas e autorizadas.

## **05. Outras Informações**

A criação de fórmulas é de responsabilidade do usuário. As fórmulas descritas neste documento são apenas exemplos, devendo ser personalizadas conforme a necessidade e cenário de cada empresa.  
Importante ressaltar que a não declaração do IBS e da CBS não é a regra, e sim a exceção, para casos muito específicos. Conforme mencionado anteriormente, a demonstração desses tributos é obrigatória à partir de Janeiro/2026.
