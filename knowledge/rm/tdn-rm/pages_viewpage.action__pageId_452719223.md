---
content_hash: 6e5e1ea5b088f84bb9f88954ba1c568a83c9136babe11f1853ae64dfc281fb1a
fetched_at: '2026-06-29T00:10:04.589424+00:00'
page_id: '452719223'
product: rm
source: tdn-rm
title: Empréstimo - Folha de pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719223
version: 13
---

Nesta etapa será configurado como será feito o empréstimo de férias.  
   
**Campos e Parâmetros**  
Utiliza lançamento automático de empréstimo de férias  
Com este parâmetro marcado será habilitado o recurso de empréstimo na marcação de férias. Quando marcado, deverá preencher os campos abaixo para o correto funcionamento do recurso.  
Ao solicitar um empréstimo nas férias, quando é lançada as férias, é inserido no cadastro de empréstimo do funcionário um registro conforme as informações configuradas nos abaixo.   
Também quando marcado este parâmetro, é habilitado o campo 'Número de vezes' e 'Início do desconto' no cadastro de férias.  
   
Tipo de empréstimo  
Refere-se ao tipo do empréstimo que será lançado no envelope do funcionário. O preenchimento deste campo é necessário para o lançamento automático dos empréstimos.

**Observação**  
Os tipos de empréstimos devem ser criados na tabela dinâmica INT30 em Administração de Pessoal | Cadastros | Cadastros Globais | Tabelas Dinâmicas  
Evento de desconto do empréstimo  
É o evento que irá para o cadastro de empréstimo do funcionário ao efetuar o lançamento de férias no Mês. Quando é feito o lançamento da folha ou rescisão do funcionário, com a opção de lançar empréstimos e selecionado o tipo de empréstimo cadastrado, este evento que será lançado com o valor do desconto.   
   
Evento de provento do empréstimo  
É o evento que será lançado no envelope do funcionário ao efetuar o lançamento de férias no mês. Este evento deverá ser criado sem código de cálculo.   
**Observação**  
Se o evento informado neste campo for calculado por fórmula, o sistema retornará no envelope do funcionário o valor da fórmula e criará um empréstimo no cadastro do funcionário com este mesmo valor.  
Caso o evento informado neste campo não tenha fórmula, o sistema retornará o líquido do recibo de férias do funcionário e criará um empréstimo no cadastro do funcionário com este mesmo valor.  
   
**Atenção**  
Sem utilizar o campo acima, o usuário calcula as férias do funcionário, lança as verbas das férias em seu envelope de pagamento para demonstrar os valores que foram adiantados no recibo de férias e é lançado também um desconto do líquido antecipado (adiantamento conforme recibo).  
Utilizando o campo acima, no lançamento das férias para o envelope de pagamento será lançado também um evento do tipo provento, conforme parametrizado e também será gravado na pasta Empréstimos um evento que será descontado conforme o número de parcelas informadas.

Min. parcelas  
Número mínimo de parcelas a serem descontadas. O sistema faz a consistência desse número mínimo de parcelas e não aceita informar um valor menor que o informado. Quando não informado este campo, retorna uma mensagem de erro para o usuário, não permitindo concluir o cadastro do empréstimo.   
   
Máx. parcelas  
Número máximo de parcelas a serem descontadas. O sistema faz a consistência desse número máximo de parcelas e não aceita informar um valor maior que o informado. Quando não informado este campo, retorna uma mensagem de erro para o usuário, não permitindo concluir o cadastro do empréstimo.   
   
Periodicidade do evento  
Neste campo é informado de quantos em quantos meses será descontado o empréstimo de férias.

**Exemplo**  
periodicidade = 1, será descontado mensalmente  
periodicidade = 2, será descontado de dois em dois meses  
*Descontos referentes a empréstimo*  
   
   
Desconta empréstimo de folha nas férias  
Com este parâmetro marcado, ao fazer o cálculo de férias será lançado no recibo de férias o desconto de empréstimo cadastrado.   
Este parâmetro só funciona para funcionário que tiver férias no mês, mesmo que não seja o mês todo.

**Exemplo**  
Funcionário com Férias do dia 01/09 a 20/09  
Será descontado o empréstimo de férias  
Funcionário com Férias do dia 15/09 a 04/10  
Não será descontado o empréstimo de férias  
   
**Observação**  
Quando é feito o desconto de empréstimo no recibo de férias, o mesmo não é feito na folha no Mês do desconto, caso o funcionário tenha dias de trabalhados conforme o exemplo acima.

Desconta empréstimo em férias partidas  
Com este parâmetro marcado, ao fazer o cálculo de férias será lançado no recibo de férias o desconto de empréstimo cadastrado, independente se é férias partidas ou não.

**Exemplo**  
Funcionário com Férias do dia 15/09 a 04/10  
Será descontado o empréstimo de férias  
   
**Observação**  
Quando é feito o desconto de empréstimo no recibo de férias, o mesmo não é feito na folha no Mês do desconto, caso o funcionário tenha dias de trabalhados conforme o exemplo acima.   
   
**Atenção**  
Este parâmetro só fica habilitado se o parâmetro 'Desconta empréstimo de folha nas férias' estiver marcado.

Lança provisionamento do empréstimo Crédito do Trabalhador nas férias

Com esse parâmetro marcado será lançado o provisionamento nas férias.

IMPORTANTE:

O evento só deve ser lançado se não existir o  provisionamento no adiantamento e/ou não existir algum empréstimo dessa modalidade "Crédito do Trabalhador eSocial" lançado em algum período da competência.

Veja mais informações sobre o parâmetro e exemplos de utilização em [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com.br/pages/viewpage.action?pageId=925361639) .

Período para lançar o provisionamento do empréstimo crédito do trabalhador nas férias

Quando informado este período, os processos de Lançar e Finalizar as férias irão inserir os eventos de[CC 487 - Provisão Crédito Trab. Férias 1º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707675) e [488 - Provisão Crédito Trab. Férias 2º Mês Envelope](https://tdn.totvs.com.br/pages/viewpage.action?pageId=944707680) no período selecionado pelo usuário. Caso não tenha nenhum conteúdo neste campo, os eventos de CC's 487 e 488 serão inseridos no mesmo envelope dos eventos de férias.

IMPORTANTE:

O parâmetro "**Período para lançar o provisionamento do empréstimo crédito do trabalhador nas férias**" ficará habilitado se o parâmetro "**Lança provisionamento do empréstimo Crédito do Trabalhador nas férias**" estiver marcado.

Quando houver mais de um período de concessão de férias no mesmo mês e houver um período informado no parametrizador será somado o valor no período informado.

**Disponibilizado nos patches descritos em** [DT - Crédito do Trabalhador - CC 487 e 488 lançados em período diferente da folha - Provisionamento Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=1039033071)

Veja exemplo de utilização em [Cálculo de Férias - Provisionamento nas Férias utilizando período específico para lançamento da provisão na folha de pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=1039869246)

Lança provisionamento no adiantamento e no recibo de férias da mesma competência

Com esse parâmetro marcado será lançado o provisionamento nas férias e também no adiantamento quando solicitado.

IMPORTANTE:

O parâmetro "**Lança provisionamento no adiantamento e no recibo de férias da mesma competência**" ficará habilitado se o parâmetro "**Lança provisionamento do empréstimo Crédito do Trabalhador nas férias**" estiver marcado.

Veja exemplo de utilização em [Cálculo de Férias - Lançar provisionamento simultâneo para Férias e Adiantamento](https://tdn.totvs.com.br/pages/viewpage.action?pageId=1042933004)

---

<< Retornar para **Férias**
