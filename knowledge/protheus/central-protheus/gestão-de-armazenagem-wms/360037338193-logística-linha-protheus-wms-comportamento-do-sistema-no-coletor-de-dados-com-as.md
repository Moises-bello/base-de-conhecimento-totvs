---
article_id: 360037338193
category: Gestão de Armazenagem (WMS)
content_hash: fbfd4b79a43dbbbac2022698c4500b06230f9ba140a55277bd447bc9f7910777
fetched_at: '2026-06-28T22:45:47.994407+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Comportamento do Sistema, no Coletor de
  Dados, com as unidades de medida do movimento, da Sequência de Abastecimento - WMSA030
type: support-article
updated_at: '2025-10-31T22:27:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037338193-Log%C3%ADstica-Linha-Protheus-WMS-Comportamento-do-Sistema-no-Coletor-de-Dados-com-as-unidades-de-medida-do-movimento-da-Sequ%C3%AAncia-de-Abastecimento-WMSA030
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26998257222679)***Tempo aproximado para leitura: **00:05:20 min****Dúvida**Qual é o comportamento do Sistema, no **Coletor de Dados**, com as **unidades de medida do movimento**, da **Sequência de Abastecimento - WMSA030**?  
  
**Ambiente****TOTVS Distribuição** - **TOTVS WMS** (Linha Protheus) - Gestão de Armazenagem (**WMS**) - Todas as versões  
  
**Solução**O campo **UM Movimento - DC3\_UMMOV**, presente no cadastro **Sequência de Abastecimento**  - **WMSA030** - possui três opções:

1. Primeira Unidade de Medida;
2. Segunda Unidade de Medida;
3. Solicita Unidade de Medida.

**1 - Primeira Unidade de Medida**Ao executar um **endereçamento ou separação no coletor**, na convocação dos itens será apresentada a quantidade inteira na primeira unidade de medida.   
 **Endereçamento:**Para exemplificar foi gerada uma nota fiscal de entrada para um produto, em que a primeira unidade de medida é **PC - Peça**, a segunda unidade de medida é **CX - Caixa**, o fator de conversão é 10, o tipo de conversão é divisor e a norma é de 10 x 10, isto é, 100 peças.   
A quantidade de entrada para a nota fiscal foi de 25. Desta forma, ao executar o **endereçamento**, foi apresentada a quantidade total em peças, ou seja, 25.

![Unid_1_enderecamento.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360048995253)

**Separação:**Para exemplificar foi gerada uma nota fiscal de entrada para um produto, em que a primeira unidade de medida é **PC - Peça**, a segunda unidade de medida é **CX - Caixa**, o fator de conversão é 10, o tipo de conversão é divisor e a norma é de 10 x 10, isto é, 100 peças.  
A quantidade de saída para o pedido de venda foi de 25. Desta forma, ao executar a **separação**, foi apresentada a quantidade total em peças, ou seja, 25.

**![Unid_1_separacao.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360048995653)**

**2 - Segunda Unidade de Medida**Ao executar um **endereçamento** ou **separação** **no coletor**, na convocação dos itens será apresentada a quantidade inteira na segunda unidade de medida.  
 **Endereçamento:**Para exemplificar foi gerada uma nota fiscal de entrada para um produto, em que a primeira unidade de medida é **PC - Peça**, a segunda unidade de medida é **CX - Caixa**, o fator de conversão é 10, o tipo de conversão é divisor e a norma é de 10 x 10, isto é, 100 peças.  
A quantidade de entrada para a nota fiscal foi de 25. Desta forma, ao executar o **endereçamento**, foi apresentada a quantidade total em caixas, ou seja, 2.5.

![Unid_2_enderecamento.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360048133274)

**Separação:**Para exemplificar foi gerada uma nota fiscal de entrada para um produto, em que a primeira unidade de medida é **PC - Peça**, a segunda unidade de medida é **CX - Caixa**, o fator de conversão é 10, o tipo de conversão é divisor e a norma é de 10 x 10, isto é, 100 peças.  
A quantidade para o pedido de venda foi de 25. Desta forma, ao executar a **separação**, foi apresentada a quantidade total em caixa, ou seja, 2.5.

**![Unid_2_separacao.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360048997173)**

**3 - Solicita Unidade de Medida**Ao executar um **endereçamento** ou **separação** **no coletor** é possível selecionar qual das duas unidades de medida será endereçada primeiro.  
 **Endereçamento**:  
Para exemplificar foi gerada uma nota fiscal de entrada para um produto, em que a primeira unidade de medida é **PC - Peça**, a segunda unidade de medida é **CX - Caixa**, o fator de conversão é 10, o tipo de conversão é divisor e a norma é de 10 x 10, isto é, 100 peças.  
A quantidade de entrada para a nota fiscal foi de 25. Desta forma, ao executar o **endereçamento**, foi apresentada a quantidade inteira na segunda unidade de medida, ou seja, 2 caixas e a quantidade restante na primeira unidade de medida, ou seja, 5 peças. Neste momento, é possível selecionar qual das duas unidades de medida será endereçada primeiro.

![Unid_3_enderecamento.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360048997333)

**Separação**:  
Para exemplificar foi gerada uma nota fiscal de entrada para um produto, em que a primeira unidade de medida é **PC - Peça**, a segunda unidade de medida é **CX - Caixa**, o fator de conversão é 10, o tipo de conversão é divisor e a norma é de 10 x 10, isto é, 100 peças.  
A quantidade para o pedido de venda foi de 25. Desta forma, ao executar a **separação**, foi apresentada a quantidade inteira na segunda unidade de medida, ou seja, 2 caixas e a quantidade restante na primeira unidade de medida, ou seja, 5 peças. Neste momento, é possível selecionar qual das duas unidades de medida será separada primeiro.

![Unid_3_enderecamento.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360048136334)

**Importante**

1. A norma definida na **Sequência de Abastecimento - WMSA030** determina a quantidade de embalagem que comporta 1 palete. Neste exemplo: a norma de 10 x 10 resulta em 100 peças que correspondem a 10 caixas em cima de 1 palete.

2. Quando usada a opção **Solicita Unidade de Medida**, na primeira linha do coletor é trazido o palete fechado isto é, a norma! Logo, se temos uma norma de 100 e a separação também for de 100, será levado 1 palete para separação e as unidade de medida CX e PC ficarão com valor zerado.

3. Ainda para a opção **Solicita Unidade de Medida**, na segunda linha do coletor de dados é carregada a maior unidade de medida do produto, que no nosso exemplo é CX. Já na terceira linha do coletor, é movimentada a menor unidade de medida, isto é, PC.

4. Em resumo, o comportamento do Sistema na alternativa **Solicita Unidade de Medida**, será levar para a primeira linha a norma completa, para a segunda linha a maior unidade de medida e para a terceira linha a menor unidade de medida do produto. O valor que chegará nessas linhas do coletor dependerá da quantidade a ser separada, ou seja, o que não inteirar ficará com o valor zerado.

**Saiba mais**Veja no *link* da documentação a seguir, sobre a utilização da unidade de medida nas tarefas de conferência: [Porque as Conferências Convocadas Não Consideram a Unidade de Medida da Sequência de Abastecimento](https://tdn.totvs.com/pages/viewpage.action?pageId=566460859)  
Também assista ao *Webinar* sobre o cadastro **Sequência de Abastecimento**: [Webinar TOTVS | Desvendando a Sequência de Abastecimento](https://www.youtube.com/watch?v=LggYlJy-GEc)
