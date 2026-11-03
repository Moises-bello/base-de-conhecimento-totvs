---
content_hash: 4e3de5724570a550b0aa3a89fda585daec056ebb1aa61d6b26875180b4b5ed4a
fetched_at: '2026-06-29T00:10:03.097670+00:00'
page_id: '452719003'
product: rm
source: tdn-rm
title: Importação Horário Professor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719003
version: 2
---

**Importação Horário Professor**   
Ao executar a importação do horário do professor, será considerado o período vigente do usuário que estará realizando a importação, e a seleção de funcionário.  
Será importado como horário planejado os intervalos conforme o plano de aula gerado no Totvs Educacional.  
**Grupo de Funcionários:** Seleção de funcionários para importar o horário do TOTVS Educacional para o TOTVS Automação de Ponto.  
**Período:** Sempre irá informar o período atual do usuário no TOTVS Automação de Ponto.   
Esta data será calculada conforme o DSR de cada funcionário. Podendo variar alguns dias antes da data início do período e alguns dias depois a data fim do período.  
   
Para os professores que não realizam batidas/marcações no relógio (REP), ou seja, assinam o livro de ponto, será possível efetuar a tratativa do espelho ponto desses Professores/Funcionários através do processo de "Apontamento de falta" pelo sistema Educacional.  
Observação: Para maior detalhamento do processo, acesse o link "Como Fazer" abaixo.

**Informações importantes sobre o cálculo do Automação de Ponto para o parâmetro Desconsidera** **Ponto do RM Educacional**

 O Automação de Ponto não calculará faltas/atrasos para jornadas que tiverem o parâmetro **marcado** no Educacional. Para que as faltas e atrasos sejam calculados, é necessário que tenha uma batida dentro do intervalo, indicando que o funcionário de fato teve atrasos/faltas, não sendo necessário neste caso apontar as faltas no Educacional.

Exemplos:

O intervalo de 16:45 às 17:30 das quartas está com o parâmetro **Desconsidera Ponto** **marcado**. Os demais horários estão com o parâmetro **desmarcado**.

No exemplo abaixo, podemos verificar que a batida foi realizada dentro do limite do intervalo, e o trabalho foi calculado corretamente para o intervalo que desconsidera o ponto do professor.

O mesmo ocorre para dias que o professor não tem jornada ou realiza a batida antes do horário.

Agora, para casos onde o funcionário teve batidas dentro do intervalo de desconsidera ponto, os atrasos serão calculados de acordo com a batida inserida, não sendo necessário o apontamento de faltas no Educacional.

|  |  |
| --- | --- |
|  | Como Fazer |

---

[Integração Ponto x Educacional](http://tdn.totvs.com/x/B4AnBQ)  
[Apontamento de Falta no Educacional integrado com o Chronus](http://tdn.totvs.com/display/LRM/DT+Apontamento+de+faltas+no+Educacional+integrado+com+o+Chronus)

|  |  |
| --- | --- |
|  |  |
