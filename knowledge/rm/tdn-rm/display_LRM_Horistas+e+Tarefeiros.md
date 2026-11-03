---
content_hash: 411e184d0c99ba5804da912df424660329b9e2531cc8e371e7e2692086a1fc7c
fetched_at: '2026-06-29T00:10:10.594013+00:00'
page_id: '452719887'
product: rm
source: tdn-rm
title: Horistas e Tarefeiros
type: documentation
url: https://tdn.totvs.com/display/LRM/Horistas+e+Tarefeiros
version: 4
---

Nesta etapa são definidas como será tratado o salário de funcionários com o tipo de recebimento Horista ou Tarefeiros  
   
**Parâmetros**  
Limita horas normais para horista/tarefeiros  
Selecione esta opção para que seja limitado o lançamento de horas normais para o funcionário horista/tarefeiro. Somente será permitido um lançamento de até 220 horas (para meses de até 30 dias) e 227,33 horas (para meses de 31 dias). Se o campo não for marcado, não será feita nenhuma consistência no lançamento de horas para os funcionários horistas.  
   
Edita salário mensal para horista/tarefeiros  
Com este parâmetro marcado, o campo Salário Mensal é habilitado. após ser informado o salário mês do funcionário, o sistema calculará o Salário Hora (salário mês / jornada) e, em seguida, arredondará esse valor considerando somente duas casas decimais.

**Observação**  
Mesmo com o arredondamento do salário hora, não é feito um recalculo do salário mensal. Desta forma, se fizer o cálculo do salário hora arredondado x Jornada, poderá encontrar um valor diferente do salário mensal informado para o campo mensal. Internamente o sistema faz o calculo dos eventos considerando o salário hora sem o arredondamento.  
Com este parâmetro desmarcado, o campo Salário Hora é habilitado e o campo Salário Mês é desabilitado. Após a informação do salário hora do funcionário, o sistema calculará o salário mensal (Salário Hora \* jornada).  
   
Permite salário hora com mais de duas casas decimais  
Com este parâmetro marcado, o usuário poderá informar e visualizar mais de duas casas decimais no campo 'Hora' do salário do funcionário.

**Observação**  
Para editar o campo hora é necessário que o parâmetro 'Edita salário mensal para horista/tarefeiros' esteja desmarcado, caso contrário, com esse parâmetro marcado, só será possível visualizar com mais de duas casas decimais.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Voltar para tela anterior **Folha de Pagamento**
