---
article_id: 360020948072
category: RH - 13º salário
content_hash: b24622b1e29ee078007940be23187f2bc05dfd9520b7a47c205b928936088f79
fetched_at: '2026-06-28T22:44:00.548915+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular a 2° parcela do 13° salário
type: support-article
updated_at: '2025-07-23T12:31:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020948072-RH-Linha-Protheus-GPE-Como-calcular-a-2-parcela-do-13-sal%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18898356786839) Tempo aproximado para leitura: **00:04:00 min  
  
Dúvida**  
Como calcular a segunda parcela do décimo terceiro salário?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
 **Solução**Para efetuar o cálculo da segunda parcela do décimo terceiro salário na P12, siga o procedimento abaixo:  
  
- **Atualizações > Definições de cálculo > Períodos GPEA400**: Crie o período e informe o roteiro 132  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409829148567)  
  
As informações desta rotina serão armazenadas nas tabelas **RFQ/RCH.**  
  
Para que o sistema gere o cálculo da segunda parcela, é necessário ter o **identificador de cálculo 0024** devidamente cadastrado, assim como os demais identificadores para encargos como INSS, IR, FGTS.

Abaixo segue a lista dos **principais Identificadores de Cálculo para 2º parcela do 13º**.

Id 0024 2a Parc. 13o Salário  
Id 0070 INSS 13° salario  
Id 0071 IR 13° Salário  
Id 0183 Desconto Antec. 2° Parcela 13o  
Id 0019 Base INSS Até o limite 13o Salário  
Id 0020 Base INSS Acima do Limite 13o Salário  
Id 0027 Base IR 13o Salário  
Id 0108 Base FGTS 13o Salário  
Id 0109 Valor FGTS 13o Sal.  
Id 0169 Dedução INSS 13° Salario  
Id 0670 Ded. Sal. Maternidade 13o GPS - Tipo Base  
Id 0021 Líquido Segunda Parcela 13  
  
Para cadastrar as verbas acesse **Atualizações > Definições de Cálculo > Verbas GPEA040**.

Para realizar o cálculo, acesse **Miscelânea> Cálculos > Por Roteiro GPEM020**: Preencha os parâmetros conforme necessidade, lembrando que a Referência, orientamos a deixar com 31/12/ANO VIGENTE, visto que serve para o sistema se basear nos avos, nesse caso 12/12 avos. Colocando por exemplo 30/11/ANO VIGENTE, será calculado em cima de 11/12 avos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18943733862423)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18943691280023)

As informações desta rotina serão armazenadas na tabela **SRC**.  
  
**Para consulta do cálculo acesse Consulta > Cálculo > Por Funcionário GPEA090:**  
  
![](http://tdn.totvs.com/download/attachments/322152210/image2017-12-19_21-34-8.png?version=1&modificationDate=1513727680000&api=v2)

Resumo do Cálculo:**Verba 010:** 2.006,49 pois o empregado não teve adiantamento da primeira parcela do décimo.  
 **Verba 521:** 2.006,49 verba 010 X 9% alíquota INSS de acordo com a tabela **S001**= 180,58.  
  
![](http://tdn.totvs.com/download/attachments/322152210/image2017-12-19_21-40-57.png?version=1&modificationDate=1513727680000&api=v2)

**Verba A10:** Refere-se a base de cálculo para o INSS que neste caso é apenas o valor da verba 010= 2.006,49, porém, se existissem mais verbas com **SIM** para INSS no cadastro de verbas, o sistema consideraria as mesmas na verbas A10.  
  
**Verba A12:** Refere-se ao total de proventos 2.006,49 verba 010 - total de descontos 180,58 verba 521= 1.825,91.  
  
**Verba A13:** Refere-se as verbas que estão com S para IR no cadastro de verba, ou seja, 2.006,49 verba 010 - 180,58 verba 521= 1.825,91 de acordo com a tabela **S002** o empregado está isento do recolhimento de imposto de renda.  
  
![](http://tdn.totvs.com/download/attachments/322152210/image2017-12-19_21-42-24.png?version=1&modificationDate=1513727680000&api=v2)  
  
![](http://tdn.totvs.com/download/attachments/322152210/image2017-12-19_21-42-45.png?version=1&modificationDate=1513727680000&api=v2)  
  
**Verba A24:** Refere-se a verba de base de **FGTS** para décimo terceiro salário, ou seja, o sistema validará o cadastro de verbas e verificará quais verbas estão com **SIM** para FGTS, ao identificá-las representará a mesma através da verba A24 que corresponde a 2.006,49 verba 010.  
  
**Verba A25:** Refere-se a verba 2.006,49 verba 010 X 8% alíquota FGTS conforme tabela **S037**= 160,51  
  
![](http://tdn.totvs.com/download/attachments/322152210/image2017-12-19_21-46-49.png?version=1&modificationDate=1513727680000&api=v2)

Fechamento:  
- **Miscelânea/Fechamento/Período:**![](http://tdn.totvs.com/download/attachments/322152210/image2017-12-19_21-59-47.png?version=1&modificationDate=1513727987000&api=v2)  
  
Observe a transição dos valores de cálculo do décimo segunda parcela entre as tabelas do sistema:  
- Inicialmente quando o cálculo da segunda parcela do décimo é realizada, os valores são lançados na tabela **SRC.**Após efetuarmos o fechamento do**Roteiro 132**o sistema move as verbas da tabela**SRC**para a**SRD:****![](http://tdn.totvs.com/download/attachments/322152210/image2017-12-19_22-2-52.png?version=1&modificationDate=1513728172000&api=v2)**

**Importante**- No cálculo do décimo não será necessário realizar a integração do processo 132 apenas o fechamento mensal.  
- No cálculo do décimo terceiro salário segunda parcela, após o fechamento mensal do roteiro 132 o sistema gravará valores de cálculo do décimo na tabela SRD.  
  
**Saiba Mais**  
Verifique alguns cenários possíveis no cálculo da segunda parcela:  
[RH - Linha Protheus - GPE - Cálculo de 13º não efetuado - Calculo Finalizado Pela FinalCalc() ou Pela EndCalc() - S\_CAINSAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050186973-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-13%C2%BA-n%C3%A3o-efetuado-Calculo-Finalizado-Pela-FinalCalc-ou-Pela-EndCalc-S-CAINSAL)  
[RH - Linha Protheus - GPE - Como gerar relatório memória de calculo para conferencia de medias da segunda parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414505421207)

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)
