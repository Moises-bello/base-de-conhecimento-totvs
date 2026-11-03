---
content_hash: 1ed0d5cc6b6bb7c9e5e18286143ca8b748d7d5dd82f5eebbc3a7dec630a38db1
fetched_at: '2026-06-29T00:10:18.430970+00:00'
page_id: '4811194'
product: rm
source: tdn-rm
title: Redução Por Perdas Recuperação de Perdas - Impairment
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4811194
version: 4
---

BLOCK

Redução Por Perdas Recuperação de Perdas - Impairment

FAQ: **Redução Por Perdas /Recuperação de Perdas - Impairment**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.20 |

Solução

* **Introdução**

***Redução ao Valor Recuperável de Ativos - IMPAIRMENT***

Impairment é uma palavra em inglês que significa deterioração em sua tradução literal. Tecnicamente trata-se da redução do valor recuperável de um bem ativo. O impairment na prática é a mensuração dos ativos que geram benefícios presentes e futuros. Impairment é o instrumento utilizado para adequar o ativo a sua real capacidade de retorno econômico.

O pronunciamento técnico CPC 01 - , **REDUÇÃO AO VALOR RECUPERÁVEL DE ATIVOS** tem como objetivo definir procedimentos visando a assegurar que os ativos não estejam registrados contabilmente por um valor superior àquele passível de ser recuperado por uso ou por venda. Caso existam evidências claras de que ativos estão avaliados por valor não recuperável no futuro, a entidade deverá imediatamente reconhecer a desvalorização por meio da constituição de provisão para perdas. O Pronunciamento também define quando a entidade deve reverter referidas perdas e quais divulgações são necessárias.

Os seguintes termos são utilizados neste documento com os significados abaixo.

***UGC – Unidade Geradora de Caixa*** *– é o menor grupo identificável de ativos que gera as entradas de caixa, que são em grande parte independentes das entradas de caixas de outros ativos ou de grupo de ativos:*

*Ex: Linha de produção, frota de veículos.*

***VC – Valor Contábil -*** *é o custo de aquisição do ativo menos a depreciação acumulada até o momento do teste de recuperabilidade do ativo.*

***Valor recuperável -*** *é o maior valor entre o valor líquido de venda de um ativo ou UCG e seu valor em uso.*

**Valor líquido de venda -** é o valor de venda de um ativo ou de uma UGC menos as despesas de venda.

**Valor em uso** - é o valor presente de fluxos de caixa futuros estimados, que devem resultar do uso de um ativo ou de uma UGC.

[![image](http://lh3.ggpht.com/_G7KXZLoZDsY/TK8AJRhWolI/AAAAAAAAB2k/7xGn2WZuYR4/image_thumb%5B1%5D.png?imgmax=800 "image")](http://lh5.ggpht.com/_G7KXZLoZDsY/TK8AIkCXLWI/AAAAAAAAB2g/yPrI12AOIXg/s1600-h/image%5B3%5D.png)

No quadro acima simulamos duas situações (A e B). Na primeira situação o valor contábil do bem era de R$ 10.000,00 e o valor recuperável era de R$ 10.500,00. Como o valor recuperável é maior que o valor contábil do bem não haverá Impairment na primeira situação.

No segunda situação, o valor contábil do bem é R$ 10.000,00 e o valor recuperável é R$ 8.000,00. Neste caso deverá ser feito uma redução de R$ 2.000,00 no valor contábil do bem.

***Procedimento/Desenvolvimento***

Com base na situação “B” do exemplo acima vamos citar os procedimentos que devem ser feitos no sistema para realização do processo de Impairment.

Na situação B o bem possui o valor contábil de **R$ 10.000,00** , então vamos acessar o cadastro de bens pelo menu **CADASTROS/BENS/COMPLETO** e simular este exemplo para o bem **01.01.002.**

O bem **01.01.002** foi cadastrado em **01/01/2007**, ao editar o bem acessaremos a pasta cálculos para visualizar os cálculos em **01/01/2010**.

*[![clip_image002](http://lh4.ggpht.com/_G7KXZLoZDsY/TK8AKsS2sII/AAAAAAAAB2s/59OxYWSuVcg/clip_image002_thumb%5B1%5D.jpg?imgmax=800 "clip_image002")](http://lh4.ggpht.com/_G7KXZLoZDsY/TK8AKISUH9I/AAAAAAAAB2o/NaH4qUo3zN0/s1600-h/clip_image002%5B4%5D.jpg)*

Repare que no data **01/01/2010** o valor contábil do bem **(coluna Vr. Residual)** é **R$ 10.000,00** , a coluna **‘Vr. Dep. R$’** representa a depreciação acumulada até **01/01/2010** que é de **R$ 12.000,00.**

De acordo com nosso exemplo, **na situação B** a perda foi de **R$ 2.000,00**, então vamos realizar o teste de Impairment no valor de **R$ 2.000,00**.

***1 -*** ***Para realizar o teste de Impairment devemos realizar os seguintes procedimentos:***

*Acessar o menu **Movimentações/Assistentes/Ajuste a valor de mercado/Redução por perdas (Impairment).***

[![clip_image004](http://lh5.ggpht.com/_G7KXZLoZDsY/TK8AMN_13BI/AAAAAAAAB20/bEW8uvcF0l4/clip_image004_thumb%5B2%5D.jpg?imgmax=800 "clip_image004")](http://lh5.ggpht.com/_G7KXZLoZDsY/TK8ALMAhcLI/AAAAAAAAB2w/YVQgZCgHuHU/s1600-h/clip_image004%5B5%5D.jpg)

**2 -** *Selecionar os bens que após avaliação a preços de mercado, identificou-se a necessidade de ajuste por desvalorização. No nosso exemplo vamos informar o bem **01.01.002**. O Tipo de ajuste a ser informado é **‘Baixa Parcial’** e a data em nosso exemplo será **01/01/2010, o valor da ocorrência será de R$ 2.000,00**. Para contabilizar o Impairment a opção **‘Contabilizar ocorrência’** deve estar marcada conforme demonstrado abaixo.*

[![clip_image006](http://lh3.ggpht.com/_G7KXZLoZDsY/TK8ANcCKDsI/AAAAAAAAB28/YGw1nzXaA2A/clip_image006_thumb%5B2%5D.jpg?imgmax=800 "clip_image006")](http://lh6.ggpht.com/_G7KXZLoZDsY/TK8AMmlImGI/AAAAAAAAB24/JTw5pOrcanA/s1600-h/clip_image006%5B5%5D.jpg)

***3 -******Após informar os dados deve-se clicar em ‘Avançar’****.*

*Será apresentada a tela com os campos **‘Documento’**, **‘Histórico Padrão’** e **‘Complemento’**. Estes dados serão utilizados no lançamento contábil que será gerado no processo**.***

***[![clip_image008](http://lh4.ggpht.com/_G7KXZLoZDsY/TK8AOgzm6NI/AAAAAAAAB3E/8FoDBe9HkLE/clip_image008_thumb%5B1%5D.jpg?imgmax=800 "clip_image008")](http://lh6.ggpht.com/_G7KXZLoZDsY/TK8AN0zvRgI/AAAAAAAAB3A/DU98CNojnAE/s1600-h/clip_image008%5B4%5D.jpg)***

***4*** *- Após informar os dados deve-se clicar em **‘Avançar’** novamente, será apresentada a tela para informar o rateio, será necessário o rateio somente se as contas contábeis utilizadas nacontabilização exigem distribuição gerencial**.***

***[![clip_image010](http://lh4.ggpht.com/_G7KXZLoZDsY/TK8APgdG8hI/AAAAAAAAB3M/2kKKNSgFhZM/clip_image010_thumb%5B1%5D.jpg?imgmax=800 "clip_image010")](http://lh4.ggpht.com/_G7KXZLoZDsY/TK8AO7dppBI/AAAAAAAAB3I/Q502KrMwWgc/s1600-h/clip_image010%5B4%5D.jpg)***

***5*** *- Ao clicar em avançar será apresentada a tela com os campos **‘N******º Laudo’*** *, **‘Responsável pelo laudo/Avaliação’**, **‘Data Laudo/avaliação’** e **‘Observações’**. No nosso exemplo a data da avaliação será **01/01/2010** conforme demonstrado abaixo**.***

***[![clip_image012](http://lh5.ggpht.com/_G7KXZLoZDsY/TK8ARZYcvGI/AAAAAAAAB3U/A29nNUCMae8/clip_image012_thumb%5B1%5D.jpg?imgmax=800 "clip_image012")](http://lh3.ggpht.com/_G7KXZLoZDsY/TK8AQPyneHI/AAAAAAAAB3Q/KTTihTlZBEY/s1600-h/clip_image012%5B4%5D.jpg)***

***6 -*** *Ao clicar no botão **‘Avançar’** será apresentada a mensagem para confirmação do processo**.*

*Após a execução do processo, para conferência dos cálculos que foram feitos vamos acessar o menu **‘Cadastro/Bens/Completo’**, filtrar o bem **’01.01.002’** e editar o mesmo. A aba **cálculos** na edição do bemserá apresentada conforme abaixo;*

[![clip_image014](http://lh3.ggpht.com/_G7KXZLoZDsY/TK8ASQ7-OTI/AAAAAAAAB3c/MpB7ACXF5hY/clip_image014_thumb%5B1%5D.jpg?imgmax=800 "clip_image014")](http://lh3.ggpht.com/_G7KXZLoZDsY/TK8AR5qA80I/AAAAAAAAB3Y/lpT-EG7fxWs/s1600-h/clip_image014%5B4%5D.jpg)

*Repare que no dia **31/01/2010** o **Vr. residual** do bem é **R$ 7.545,50**. Este valor já está considerando a depreciação do mês de Janeiro que é **R$ 454,50.***

**Se retirarmos a depreciação mensal do bem em Janeiro teremos:**

**R$ 12.454,50** **(Depreciação acumulada em 31/01)** menos **R$ 454,50 (Depreciação mensal de Janeiro) = R$ 12.000,00**

Então;

**R$ 20.000,00 – R$ 12.000 = R$ 8.000,00**

 Ou seja, o valor contábil do bem em **01/01/2010** após o processo de Impairment é de **R$ 8.000,00**, conforme nosso exemplo que foi demonstrado no quadro acima na situação **B** .

***OBS: O valor da perda informado no processo de Impairment foi de 2.000,00 e deve reduzir apenas o valor corrigido do bem, o valor de depreciação acumulada não é afetado, pois a contabilização feita no processo deve ser:***

**DÉBITO – Despesas com Provisão Para Perdas (conta de resultado).**

**CRÉDITO - Provisão para Perda (ATIVO).**

* ##### **Reversão da Perda**

“O valor contábil de um ativo, exceto o ágio pago por expectativa de resultado futuro, que foi elevado devido à reversão de perda com desvalorização, não deve exceder o valor contábil que teria sido determinado, líquido de depreciação, amortização ou exaustão, se não tivesse sido reconhecida, em anos anteriores, a desvalorização para o ativo”.

O texto acima retirado da **CPC 01** (Comitê de Pronunciamentos Técnicos) diz que o valor da baixa por Impairment pode ser revertido até o limite do seu valor no caso de uma revisão do valor do bem em função de alterações nas estimativas anteriores.

##### 

* ##### Desenvolvimento/Procedimento

***1 -*** *Para efetuar a Reversão da Perda deve-se acessar o menu **Movimentações/Assistentes/Ajustes a valor de mercado/Recuperação de perdas(reversão Impairment):***

[![clip_image015](http://lh6.ggpht.com/_G7KXZLoZDsY/TK8ATX69pGI/AAAAAAAAB3k/jt781W98zes/clip_image015_thumb%5B1%5D.jpg?imgmax=800 "clip_image015")](http://lh5.ggpht.com/_G7KXZLoZDsY/TK8AS-rWU3I/AAAAAAAAB3g/xv_SnaI6fWA/s1600-h/clip_image015%5B4%5D.jpg)

**2 -** Após clicar no processo **‘Recuperação de perdas (reversão Impairment)** deverá ser filtrado o bem desejado para recuperação da perda. Após selecionado o bem clicando em **‘Avançar’** será apresentada a tela para informação do **tipo de acréscimo**. Nesta tela não há necessidade de marcar nenhuma opção, deve-se clicar em ‘**Avançar’.**

[![clip_image017](http://lh3.ggpht.com/_G7KXZLoZDsY/TK8AVGtPGFI/AAAAAAAAB3s/rlRHyDjnXQU/clip_image017_thumb%5B1%5D.jpg?imgmax=800 "clip_image017")](http://lh3.ggpht.com/_G7KXZLoZDsY/TK8AUB7T98I/AAAAAAAAB3o/i6e61g4W6JQ/s1600-h/clip_image017%5B4%5D.jpg)

 No próximo passo deve ser informado a data e valor da recuperação. Ao marcar a opção ‘**Contabilizar**’ deverá ser informado a conta de **Reversão de Perdas** e a conta de **Provisão de Perdas.**

##### [clip_image019](http://lh4.ggpht.com/_G7KXZLoZDsY/TK8AVxLBkEI/AAAAAAAAB3w/Lwa_4hTuCL8/s1600-h/clip_image019%5B4%5D.jpg)

##### 

##### **Contabilização da Reversão da Perda**

**DÉBITO – Provisão Para Perdas (Ativo).**

**CRÉDITO - Reversão de Perdas por Impairment (Resultado)**

- No cadastro de ocorrências que pode ser acessado pelo menu **Cadastro/Ocorrências**, as ocorrências geradas por ajustes, poderão ser acompanhadas:

[![clip_image021](http://lh6.ggpht.com/_G7KXZLoZDsY/TK8AYeV1bpI/AAAAAAAAB38/M4S8us_cVcE/clip_image021_thumb%5B1%5D.jpg?imgmax=800 "clip_image021")](http://lh6.ggpht.com/_G7KXZLoZDsY/TK8AXkRAouI/AAAAAAAAB34/odMeHoGVe8o/s1600-h/clip_image021%5B4%5D.jpg)

 Ao editar a ocorrência referente ao Impairment é apresentada a aba **‘Contabilidade’** com as contas que foram utilizadas no processo e também a aba ‘**Observações’** que permite visualizar os dados informados sobre o laudo.

**OBS: Após integrar o lote contábil no RM Saldus que possui a contabilização deste processo não é mais possível visualizar as contas contábeis na aba ‘Contabilidade’.**

* **Informações Adicionais**

As informações gravadas na base permitem aos nossos clientes, desenvolver relatórios com os laudos, os ajustes a valor de mercado, etc, através do gerador de relatórios.

**Importante:** No exemplo citado acima a data de realização do Impairment foi feita no **primeiro dia do mês.** Sugerimos que após avaliação dos valores, o processo seja executado sempre no primeiro dia do mês, pois no sistema atual se o bem sofrer uma redução do valor corrigido no final do mês a depreciação mensal é afetada. Desta forma, realizando a redução no primeiro dia do mês a depreciação mensal será calculada com base no novo valor.

**Exemplo**: Se foi feito um laudo de avaliação com data em **31/12/2009**, sugerimos que os processos no sistema sejam feitos em **01/01/2010**.
