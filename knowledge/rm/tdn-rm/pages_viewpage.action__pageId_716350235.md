---
content_hash: 0d65dda240cfcab035205b9ef2fe221473ca0ac698c61ec33dec192799d1f641
fetched_at: '2026-06-29T00:11:26.363971+00:00'
page_id: '716350235'
product: rm
source: tdn-rm
title: Afeta Base de Cálculo do Desconto por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=716350235
version: 6
---

---

A fim de afetar a base de cálculo para as próximas bolsas a serem processadas bem como a base para o cálculo do desconto por antecipação se o mesmo for calculado depois do cálculo da bolsa, foi criado o campo “Afeta base de cálculo” no cadastro de bolsas, no cadastro de bolsas de contratos dos alunos e no cadastro de concessão de bolsas futuras.

CadastroBolsasCadastro de BolsasCadastro de Bolsas

Acréscimo do campo "Afeta base de cálculo". O preenchimento do campo "Afeta base de cálculo" conterá o valor default para o cadastro de bolsas nos contratos, ou seja, a cada vez que uma bolsa for inserida no contrato do aluno, a mesma será inserida com o valor informado no cadastro da bolsa.

Para que esse campo esteja visível para o usuário, o sistema deverá ter o parâmetro de aplicação de bolsa setado com o valor "Contrato" e o campo "Aplicar desconto por antecipação" tem que estar setado com o valor "Depois do cálculo da bolsa". Seguem telas abaixo:

(Tela de bolsa)

(Parâmetros de sistema)

BolsasContratosAfetaBolsas de ContratosBolsas de Contratos

Acréscimo do campo "Afeta base de cálculo". Ao selecionar uma bolsa, o valor default para o campo "Afeta base de cálculo" setado no cadastro da bolsa será preenchido no respectivo campo da bolsa do contrato, mas o mesmo poderá ser alterado normalmente. A geração de lançamentos / simulação de valores de parcelas considerará esse valor do campo na bolsa do contrato.

Para que esse campo esteja visível para o usuário, o sistema deverá ter o parâmetro de aplicação de bolsa setado com o valor "Contrato", o campo "Aplicar desconto por antecipação" tem que estar setado com o valor "Depois do cálculo da bolsa" e o campo "Tipo da Bolsa" do contrato tem que ser diferente de "Aplicar bolsas em cascata" pois o comportamento de aplicar bolsas em cascata sempre afeta a base de cálculo das entidades que serão calculadas posteriormente ao cálculo de uma determinada bolsa. Seguem telas abaixo:

(Tela de bolsa do contrato)

(Parâmetros de sistema)

(Tela de contrato)

ConcessaoBolFutAfetaConcessão de Bolsas FuturasConcessão de Bolsas Futuras

No cadastro de concessão de bolsas futuras teve a criação do campo “Afeta base de cálculo”. Esse campo tem o objetivo indicar quando marcado, que o sistema afetará base de cálculo para as próximas bolsas a serem processadas bem como a base para o cálculo do desconto por antecipação se o mesmo for calculado depois desta bolsa.

O campo fica disponível quando o campo “Aplicar desconto por antecipação” estiver configurado para depois do cálculo da bolsa.

No assistente de concessão de bolsas futuras também teve a criação do campo “Afeta base de cálculo”.

O valor desse campo será preenchido automaticamente pelo mesmo valor do campo “Afeta base de cálculo” presente no cadastro de bolsa.

Na inclusão de parcela para o contrato do aluno, caso o aluno tenha uma concessão de bolsas futuras que contempla nos dados informados na parcela. A bolsa será incluída no contrato do aluno onde o campo “Afeta base de cálculo” da bolsa do aluno terá o mesmo valor do campo “Afeta base de cálculo” presente na concessão de bolsas futuras.

ConcessaoBolFutAfetaConcessão de Bolsas FuturasGeração de lançamentos / Simulação de valores de parcelas

A geração de lançamentos priorizará as bolsas que afetam a base de cálculo e, posteriormente, processará as outras bolsas sendo que, se duas bolsas no contrato possuem comportamentos distintos na aplicação do desconto por antecipação, a geração de lançamentos ou simulação de valores de parcelas, considerará, primeiramente, as bolsas que afetam a base de cálculo e logo em seguida, as bolsas cujo desconto seja calculado “Depois do cálculo da bolsa”.

**Exemplos**:

Somar Bolsas

Exemplos com o tipo de bolsa definido como "Somar Bolsas" no contrato

Exemplo 1:

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa A: **Marcado**  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Antes do cálculo da bolsa”  
- Afeta base de cálculo: **Desmarcado (Não visível)**  
  
=> Após geração da parcela 1, teremos os seguintes valores:  
- Valor do desconto por antecipação: 450,00  
- Bolsa A: R$ 100,00  
- Bolsa B: R$ 180,00  
- Total de Bolsas aplicado: R$ 280,00  
- Valor líquido: R$ 270,00

Exemplo 2:   
- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 7%  
- Bolsa A: 30% (Código da bolsa: 3)  
- Ordem Bolsa A:  sem preenchimento ou com mesma ordem da bolsa B  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa A: **Marcado**  
- Bolsa B: 30% (Código da bolsa: 5)  
- Ordem Bolsa B: sem preenchimento ou com mesma ordem da bolsa A  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa B: **Marcado**  
  
=> Após geração da parcela 1, teremos os seguintes valores:  
- Bolsa A: R$ 300,00 (Quando existirem bolsas com mesma "Ordem", o sistema aplicará primeiro a bolsa de menor código)  
- Bolsa B: R$ 210,00 (valor calculado sobre o valor de base com o desconto da Bolsa A)  
- Total de Bolsas aplicado: R$ 510,00  
- Valor do desconto por antecipação: R$ 34,30  
- Valor líquido: R$ 455,70

Exemplo 3:   
- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 7%  
- Bolsa A: 30%   
- Ordem Bolsa A:  2  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa A: **Marcado**  
- Bolsa B: 30%   
- Ordem Bolsa B: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa B: **Marcado**  
  
=> Após geração da parcela 1, teremos os seguintes valores:  
- Bolsa B: R$ 300,00 (é considerada a ordem da bolsa)  
- Bolsa A: R$ 210,00 (é considerada a ordem da bolsa)  
- Total de Bolsas aplicado: R$ 510,00  
- Valor do desconto por antecipação: R$ 34,30  
- Valor líquido: R$ 455,70

Somente a Maior Bolsa

Exemplo com o tipo de bolsa definido como "Somente a Maior Bolsa" no contrato

Exemplo 4:

- Parcela 1: R$ 1000,00  
- Desconto por antecipação no 1º vencimento: 50%  
- Bolsa A: 10%   
- Ordem Bolsa A: 1  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa A: **Marcado**  
- Bolsa B: 20%   
- Ordem Bolsa B: 2  
- Aplicar desconto por antecipação: “Depois do cálculo da bolsa”  
- Afeta base de cálculo Bolsa B: **Desmarcado**

=> Após geração da parcela 1, teremos os seguintes valores:  
- Valor do desconto por antecipação: 500,00  
- Bolsa A: R$ 0,00  
- Bolsa B: R$ 200,00  
- Total de Bolsas aplicado: R$ 200,00  
- Valor líquido: R$ 300,00
