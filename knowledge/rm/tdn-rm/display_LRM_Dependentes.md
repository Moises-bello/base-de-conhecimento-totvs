---
content_hash: 778aa41f83dd1b58a53ebbcae3a28e25f11fbbb4dd2d6be9c026855089318442
fetched_at: '2026-06-29T00:10:07.303064+00:00'
page_id: '452719396'
product: rm
source: tdn-rm
title: Dependentes
type: documentation
url: https://tdn.totvs.com/display/LRM/Dependentes
version: 12
---

No cadastro dos dependentes do empregado são informados os dados documentais e incidências para cálculos de salário família, IRRF, pensão alimentícia dentre outros.   
   
**IRRF**  
Será considerado como dependente de IRRF, sempre que a incidência 'IRRF' estiver marcada.  
Porém para Grau de Parentesco '**1-Filho(a) Válido' ou 'D-Enteado(a)**' será verificada também a data de nascimento e o parâmetro '**Universitário/Escola Técnica 2º Grau**'.  
   
A informação se o dependente é '**Universitário/Escola Técnica 2º Grau**' será considerada somente para o Grau de Parentesco '**1-Filho(a) Válido' ou 'D-Enteado(a)**', até completar 25 (vinte e quatro) anos de idade, conforme legislação.

**ATENÇÃO:**

1. Se esta informação estiver confirmada, o dependente em questão deverá também incidir em IRRF.
2. O sistema desmarca automaticamente o campo incidência '**IRRF**' na Liberação de Competência, para o Grau de Parentesco '**1-Filho(a) Válido' ou 'D-Enteado(a)**', desde que o parâmetro "**Considera a dedução de dependente somente até o mês de aniversário**" esteja marcado em Parametrizador | Folha Normal | Cálculo 2/2. Veja informação do parâmetro no [Link](https://tdn.totvs.com.br/pages/viewpage.action?pageId=561848185)

**SALÁRIO FAMÍLIA**

O salário família é concedido quando o dependente é:

a) filho(a) inválido(a);

b) filho(a) válido(a) com até 12 meses de idade;

c) filho(a) válido(a) maior de 4 anos e menor de 7 anos de idade que tenha entregue o cartão vacina e frequencia escolar;

d) filho(a) válido(a) com idade entre 7 e 14 anos que tenha comprovado a frequência escolar;

e) Irmã(o) válido com até 12 meses de idade;

f) Irmã(o) válido maior de 4 anos e menor de 7 anos de idade que tenha entregue o cartão vacina e frequencia escolar;

g) Irmã(o) válido com idade entre 7 e 14 anos que tenha comprovado a frequência escolar;

h) Irmã(o) Inválido;

i) Neto(a) com até 12 meses de idade;

j) Neto(a) válido maior de 4 anos e menor de 7 anos de idade que tenha entregue o cartão vacina e frequencia escolar;

k) Neto(a) válido com idade entre 7 e 14 anos que tenha comprovado a frequência escolar;

**ATENÇÃO:**

1. Caso o parâmetro “**Dependente menor de 1 anos s/cartão vacina**” no Parametrizador | Folha Normal | Salário Família estiver marcado será considerado para pagamento de salário família, o dependente menor de 1 ano e com o parâmetro '**Entregou Cartão Vacina**' desmarcado.
2. Ao informar um dependente, com idade superior a um ano, o campo '**Entregou cartão vacina**' deverá ser obrigatoriamente marcado para que o funcionário receba o salário família.
3. A informação de **'Data de entrega da certidão**' é utilizada para impressão no documento legal da Ficha de Salário Família.
4. Ao informar um dependente com idade superior a 7(sete) anos, o campo '**Entregou comprov. de frequência escolar**' deverá ser obrigatoriamente marcado para que o funcionário receba o salário família.
5. Na liberação de competência será atualizado o número de dependentes para salário família e a respectiva incidência no cadastro de dependentes.
6. Quando a incidência 'Forçar incidência de Salário Família' estiver marcada, o sistema irá considerar o dependente para o cálculo do Salário Família independente se atende ou não aos requisitos legais (idade, cartão vacina, grau de parentesco, etc).
7. Ao informar um dependente válido, com idade entre 4 e 7 anos, é necessário que os campos '**Entregou cartão vacina**' e '**Entregou comprov. de frequência escolar**' estejam em uso

**INCIDÊNCIAS**  
Caso o usuário necessite criar outras incidências para ser utilizada em fórmulas ou relatórios, poderá criar através da tabela INT37.  
   
Quando a incidência 'Pensão' estiver marcada, será habilitada a aba 'Dados da Pensão' e os anexos 'Eventos da Pensão de Dependente' e 'Movimentação da Pensão de Dependente' para preenchimento das informações para desconto de pensão alimentícia.

**ASSISTÊNCIA MÉDICA**   
Informar se é dependente em plano privado de saúde. Sendo: S-Sim; N-Não. Valores Válidos: S, N.

**ASSISTÊNCIA ODONTOLÓGICA**   
Informar se é dependente em plano privado odontológico. Sendo: S-Sim; N-Não. Valores Válidos: S, N.

**ANEXO MOVIMENTO DA PENSÃO**   
Informações do movimento de pensão alimentícia do funcionário.

 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários

Incidências

Dados da Pensão

Campos complementares

[Anexo Eventos Não Considerados](https://tdn.totvs.com/pages/viewpage.action?pageId=452719789)

[Valor Dedução do Rendimento Tributável](https://tdn.totvs.com/pages/viewpage.action?pageId=784779468)
