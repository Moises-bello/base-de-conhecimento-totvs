---
article_id: 14635481028759
category: Financeiro - Contas a Receber
content_hash: 9fe4e9429d1c92493e1af6384ef50f1c3711ef8619a7cbc96f39f3115094ab5e
fetched_at: '2026-06-28T22:38:12.453972+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGAFIN -  Como calcular multa
  e juros
type: support-article
updated_at: '2026-05-07T17:46:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14635481028759-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-calcular-multa-e-juros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17803178260119) Tempo aproximado para leitura: **12:00 min**  
  
**Dúvida**  
Como calcular multa e juros?

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus  - Financeiro - Todas as versões. **Solução** Para ser calculada, a multa depende do conteúdo informado nos parâmetros abaixo:

```
MV_JURTIPO: L (CONSIDERA CALCULO DE MULTA)

MV_LJMULTA: Percentual de multa que será aplicada

MV_FINJRTP = 3 - Ambos (calcula juros e taxa de permanência)
```

Cálculo de juros e taxa de permanência, no financeiro, os juros são gerados por meio dos parâmetros:

```
MV_LJJUROS = Igual ao parâmetro MV_TXPER e maior que zero
MV_TXPER = Igual ao parâmetro MV_LJJUROS e maior que zero
MV_LJJUFIN = .F.
MV_FINJRTP = 3 - Ambos (calcula juros e taxa de permanência)
MV_TOLER = Tolerância de dias de atraso 
MV_LJFSEMA = 0 - Não calcula no sábado e domingo
MV_LJCALJM = .F. - Define se calcula juros e multa dos títulos a receber independente da data 
de vencimento do título
```

Para o parâmetro **MV\_JURTIPO** existem 3 tipos de cálculo de juros; abaixo o cálculo gerado pelo sistema:  
**Juros Simples** (parâmetro **MV\_JURTIPO = S**)

```
Juros = Saldo do Título * (dias de atraso *(taxa de juros/100))
```

**Juros Compostos** (parâmetro **MV\_JURTIPO = C**)

```
Juros = Saldo do Título *((1+(taxa de juros/100))**dias de atraso)
```

**Juros Mistos** (parâmetro **MV\_JURTIPO = M**)  
Este tipo de juro é a combinação do simples com o composto:

Até 30 dias, é calculado o **juro simples**:

```
Juros = Saldo do Título * (dias de atraso*(taxa de juros/100))
```

Acima de 30 dias, calcula-se o **juro compostos**:

```
Juros Simples = Saldo do título *(1+(30*(taxa de juros/100)))

Juros = Juros Simples* ((1+(taxa de juros/100)) **dias de atraso-30)
```

**Observação**  
Selecionando qualquer uma das opções acima, não será calculada a multa. Para cálculo da multa, deve ter o conteúdo igual a 'L' no parâmetro **MV\_JURTIPO**.  
  
**Importante**  
Quando não houver percentual de juros indicado no título, o juro será calculado pela taxa de permanência da seguinte forma:

```
Juros = Valor da Taxa de Permanência * dias de atraso
```

Será validada a data de vencimento para cálculo de juros e multa e o parâmetro **MV\_TOLER.**  
  
O conceito do sistema, quanto ao tratamento de juros e permanência:   
- Taxa de Permanência é um valor fixo cobrado por dia de atraso no pagamento do título.  
- Juros são um percentual calculado sobre o valor baixado por dia de atraso.  
   
Quando da baixa do título, a taxa de permanência, por ser um valor fixo, será multiplicada pelo número de dias de atraso, obtendo-se assim o valor total da taxa de permanência a ser cobrada, independente do valor baixado.  
Quanto aos juros, é aplicado o percentual, multiplicado pelo número de dias em atraso (se juros simples) sobre o valor baixado.  
  
No Financeiro, para calcular **taxa de permanência e juros,** utilize o parâmetro **MV\_TXPER**

```
MV_LJJUROS = Igual ao parâmetro MV_TXPER e maior que zero
MV_TXPER = Igual ao parâmetro MV_LJJUROS e maior que zero
MV_LJMULTA = Maior que zero
MV_JURTIPO = L (CONSIDERA CALCULO DE MULTA DA LOJA)
MV_LJJUFIN = .F.
MV_FINJRTP = 3 - Ambos (calcula juros e taxa de permanência)
MV_TOLER = 0
MV_LJFSEMA = 0 - não calcula no sábado e domingo
```

**Importante**  
Por padrão, o sistema calcula somente a permanência diária. O parâmetro **MV\_TXPER** é a taxa de permanência diária, ou seja, o valor aplicado no parâmetro será utilizado para o cálculo diário dos juros, caso possua uma taxa mensal, terá que realizar a divisão pela quantidade de dias daquele mês em específico e colocar no parâmetro o valor diário.   
Segue o esclarecimento no uso do parâmetro MV\_TXPER:   
"Para que o parâmetro MV\_TXPER possa acatar os valores de juros diários, será necessário que haja o cálculo da TAXA / (dividido) por 30 ou a quantidade de dias no mês, que será igual ao percentual que deseja, como, por exemplo:  
Para uma taxa de 6%, o cálculo ficaria = 6 / 30 = 0,2%. O preenchimento correto no parâmetro MV\_TXPER tem que conter o ponto no lugar da vírgula, ficando 0.20.  
   
**Observação**: O parâmetro MV\_TXPER não calcula de forma automática a divisão pelos dias do mês, sendo necessário executar de forma manual, obtendo o resultado que deseja para só após, acrescentar no parâmetro MV\_TXPER".

**Importante**

O sistema irá utilizar o conteúdo do parâmetro **MV\_TXPER**, quando o registro vier de integração de outros módulos (exemplo: módulo Lojas para o financeiro, módulo Faturamento para o financeiro).

Caso esteja incluindo um título diretamente no módulo financeiro, será necessário inserir o percentual de juros no campo **E1\_PORCJUR** chamado "**Porc Juros**", para que o sistema calcule os juros.  
  
  
**Saiba Mais**  
[Cálculo de juros - MV\_JURTIPO](https://tdn.totvs.com/pages/releaseview.action?pageId=39682457)

[Ponto de entrada - FJURCST - Cálculo de juros](https://tdn.totvs.com/pages/releaseview.action?pageId=6071298)

[Ponto de entrada - FJURREC - Ponto de Entrada recalculo de juros a receber](https://tdn.totvs.com/display/public/PROT/FJURREC+-+Ponto+de+Entrada+recalculo+de+juros+a+recebe)
