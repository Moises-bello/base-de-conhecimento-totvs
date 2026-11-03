---
article_id: 360051490153
category: RH - Funcionários
content_hash: 04116ce56378f03ba694251a84bcfb39da76eef1dd7ccad5cdc4b3b76cba6226
fetched_at: '2026-06-28T22:43:28.740696+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como utilizar o parâmetro MV_MATUNIC
type: support-article
updated_at: '2025-09-30T01:43:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051490153-RH-Linha-Protheus-GPE-Como-utilizar-o-par%C3%A2metro-MV-MATUNIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33056288669719) Tempo aproximado para leitura: **00:01:30 min****Dúvida**Como utilizar o parâmetro MV\_MATUNIC?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Quem utiliza o sequencial automático para o campo matrícula do funcionário pode, em algum momento, desejar que esse sequencial determine uma nova matrícula preenchendo as lacunas existentes entre as matrículas já cadastradas.  
Por exemplo, quem utilizava o parâmetro **MV\_MATAUT** para definir a partir de qual matrícula os autônomos seriam cadastrados acabava ficando com uma lacuna entre matrículas de funcionários e o início das matrículas de autônomos.  
  
O objetivo do novo parâmetro **MV\_MATUNIC** é fazer uma **varredura na tabela SRA**, identificar um código que não foi utilizado e sugeri-lo na inclusão, cópia e transferência de funcionários e autônomos.  
Nesse novo cenário o sistema iniciará a varredura a partir do código preenchido no parâmetro MV\_MATUNIC e retornará a primeira matrícula disponível.  
Após a primeira varredura, o parâmetro MV\_MATUNIC será **atualizado com a última matrícula** cadastrada para que não seja feita uma nova busca no intervalo que já sabemos que não há lacunas.

**O uso da funcionalidade é opcional.**O parâmetro MV\_MATRICU permanece como critério para definição da nova matrícula, por outro lado o MV\_MATAUT **não será mais considerado.**

O parâmetro MV\_MATUNIC pode ser preenchido de acordo com a **última matrícula cadastrada**, ou se deseja fazer uma verificação completa, **basta preencher com zeros,** respeitando o tamanho utilizado no campo RA\_MAT.   
Por exemplo, se a matrícula possuir 6 caracteres, preencher com 6 zeros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32861587392407)

**Importante:** Se utilizar numeração única por filial deverá ter um parâmetro para cada filial.

**Tabelas Utilizadas:**

* **SX6** -  Parâmetros
* **SRA** -  Funcionários

**Rotinas Envolvidas:**

* **GPEA010 :** Cadastro de Funcionários
* **GPEA265:** Cadastro de Autônomos
* **GPEA180:** Transferências

**Observação**

-Importante ressaltar que este parâmetro, além do cadastro de autônomos(GPEA265), afetará o cadastro de funcionários(GPEA010) e a rotina de transferências(GPEA180).

-Na configuração inicial, o parâmetro pode ser inicializado com "zeros" para que seja feita a verificação completa. Se o campo RA\_MAT, por exemplo, usar 6 caracteres, deve-se preencher o parâmetro com 6 zeros: 000000.

-A cada inclusão, cópia ou transferência de funcionários/autônomos, o parâmetro será atualizado com a última matrícula gravada para que não seja feita uma nova verificação de um intervalo que já sabemos que não há gaps.
