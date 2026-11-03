---
article_id: 360016791951
category: RH - Folha de Pagamento
content_hash: 26f44c34c704a9166c02ef93d83b83ed91a7f16a02ba34088e6d29332b900612
fetched_at: '2026-06-28T22:44:14.820433+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como valorizar as verbas as horas utilizando a
  função FGERAVERBA
type: support-article
updated_at: '2024-09-05T18:47:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016791951-RH-Linha-Protheus-GPE-Como-valorizar-as-verbas-as-horas-utilizando-a-fun%C3%A7%C3%A3o-FGERAVERBA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26166785562647) Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**No módulo **Gestão de Pessoal**, como devemos valorizar as verbas em horas utilizando a função FGERAVERBA?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as Versões.  
  
**Causa**Na versão 12, é necessário informar nos parâmetros da **função FGERAVERBA**, **0** para o valor da hora, e**"I"**(informado) para a origem da verba. **Diferente da versão 11** onde não era necessário estas 2 informações. Caso não sejam informados nos parâmetros estes conteúdos, ao informar a quantidade de horas da verba, não ocorrerá a valorização.

**Solução**O suporte não auxilia no desenvolvimento de fórmulas, porém, disponibilizamos um exemplo de como a função pode ser parametrizada:  
  
FGERAVERBA("138",**0**,3.00,,,"H",**"I"**,,,,,,,,,,,,,,,.T.)     
  
Variável de cada parâmetro da função montada acima:  
cCod = Codigo da Verba   
**nValor = Valor da Verba**   
nHoras = Horas da Verba  
cSem = Semana da Verba  
cCct = Centro de Custo  
cTip1 = Tipo da Verba   
**cTip2 = Origem da Verba**  
nPar = Parcela da Verba  
cDel = se Deletada "D"   
cMes = Data de Pagto da Verba  
lAltera = se permite alterar caso exista o código

Abaixo segue todas as variáveis usadas na função atualmente:

|  |  |
| --- | --- |
| cCod | Código da Verba a ser gerada |
| nValor | Valor da Verba |
| nHoras | Horas ou quantidade da verba |
| cSem | Número da Semana, pode ser utilizada a variável **cSemana** que é a semana indicada nas perguntas dos roteiros de cálculo. |
| cCct | Código do Centro de Custo do funcionário |
| cTip1 | Tipo da Verba. Pode ser **V** para Valor, **H** para Horas ou **D** para Dias. Se não for informado será assumido **V** |
| cTip2 | Origem da verba. Deve ser colocado "I", de "Informado". |
| nPar | Número de Parcelas da Verba. Deve estar entre 0 e 99 |
| cDel | Indica se a verba esta deletada. Deve ser informado "D" para deletada, caso contrário passar NIL ou uma string com espaço (" ") |
| cMes | Data do efetivo pagamento da Verba. Pode-se utilizar a Variável **dData\_Pgto** que é a data informada nas perguntas do cálculo |
| lAltera | Variável lógica para indicar se a verba pode ser alterada, caso já exista no movimento do funcionário e não for informada. Pode ser **.T.** ou **.F.**. |
| nValInfo | Compatibilidade. Deve ser passado NIL neste parâmetro. |
| nHorInfo | Compatibilidade. Deve ser passado NIL neste parâmetro |
| cSeq | Sequência a ser gerada no lançamento. Esta parâmetro é opcional, mas caso seja informado (diferente de NIL), deve ser passado uma string com o número da sequência ou com um espaço (" "). Não deve ser passado uma string vazia ("") pois desta forma não serão encontradas eventuais verbas que já existam no aPd, podendo ocasionar erro de chave duplicada. |
| cNumId | Compatibilidade. Deve ser passado NIL neste parâmetro. |
| lPropDia | Se a verba deve ser proporcionalizada de acordo com os dias trabalhados. DEFAULT **.F.** |
| cItCt | Código do Item contábil. Opcional |
| cClVl | Código da Classe de valor. Opcional |
| dDataRef | Data de referência do lançamento. Opcional |
| lNewValor | Compatibilidade. Deve ser passado NIL neste parâmetro. |
| cConvoc | Código da convocação. Deve ser passado apenas para funcionários com contrato intermitente. |

É **importante** também que no roteiro, a chamada ocorra antes da sequência de valorização das verbas. Caso contrário, não será calculado o valor das horas informadas.  
  
**Saiba mais**  
[Função fGeraVerba()](https://tdn.totvs.com/pages/viewpage.action?pageId=454830364)

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
