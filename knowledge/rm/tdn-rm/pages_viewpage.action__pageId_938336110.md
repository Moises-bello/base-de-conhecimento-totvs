---
content_hash: 28edf2c5e58848d36af7fa240577f7cb0fa6c4a067d878e987dc77a49d43f6c8
fetched_at: '2026-06-29T00:12:09.051643+00:00'
page_id: '938336110'
product: rm
source: tdn-rm
title: Cálculo do POEB na Geração de Movimento - NÃO PUBLICAR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=938336110
version: 2
---

O cálculo do POEB na geração de movimento por caixa, **somente para o ensino superior,** é o benefício aplicado no item do movimento, de forma a realizarmos uma separação entre valores tributáveis e não tributáveis para a emissão da Nota Fiscal conforme a sua  no TOTVS Gestão Fiscal.

ATENÇÃO

O recurso de utilização do benefício do POEB na geração de movimento por caixa é liberada por script especifico previamente alinhado com o produto TOTVS Educacional  
E na versão 12.1.2402 a partir do patch **12.1.2402.167 ou superior** com a necessidade de execução do **Atualizador de Base de Dados TOTVS RM,** além da liberação do script especifico previamente alinhado com o produto TOTVS Educacional

No TOTVS Educacional para a habilitação da utilização do benefício na geração do movimento por caixa o usuário deverá marcar o parâmetro "**Habilitada a utilização do benefício POEB na geração de movimento**". Esse parâmetro está disponível no menu Configuração → Parâmetros → Integração → Fiscal → Fiscal 1/2 no assistente de parametrização do sistema.

.

Desta forma, quando o parâmetro estiver marcado o processo de geração de movimento por caixa irá buscar no TOTVS Gestão Fiscal o valor do **percentual não tributável** a ser calculado no valor do item de movimento presente no movimento gerado pelo processo. E irá gerar separadamente um item do movimento com valor não tributável e outro item de movimento com valor tributável no movimento.

Com a marcação do parâmetro "**Habilitada a utilização do benefício POEB na geração de movimento**" no cadastro de serviços educacionais ficará disponível o campo "**Considerar utilização do benefício do POEB na geração de movimento**". Desta forma, no processo de geração de movimento por caixa o sistema irá verificar se no serviço vinculado à parcela do contrato esse campo está marcado. Se no serviço estiver com essa configuração, o sistema irá realizar a separação entre valores tributáveis e não tributáveis para a emissão da Nota Fiscal para aquele serviço.

Exemplo 1: Geração do movimento por caixa sem a utilização do benefício POEB

Contrato A do aluno ES-0001 tem uma parcela sem desconto e sem bolsa para o serviço de mensalidade

Parcela 1 no valor: R$ 1000,00.

A parcela 1 tem o lançamento 10 gerado no valor: R$ 1000,00.

O lançamento 10 tem o boleto 101 gerado no valor: R$ 1000,00

Na geração do movimento por caixa para o boleto 101, o processo gerar um movimento com os seguintes valores:

Movimento 201 no valor: R$ 1000,00

Item do movimento com preço unitário de: R$ 1000,00

Exemplo 2: Geração do movimento por caixa com a utilização do benefício POEB

Contrato A do aluno ES-0001 tem uma parcela sem desconto e sem bolsa para o serviço de mensalidade

Parcela 1 no valor: R$ 1000,00.

A parcela 1 tem o lançamento 10 gerado no valor: R$ 1000,00.

O lançamento 10 tem o boleto 101 gerado no valor: R$ 1000,00

Na geração do movimento por caixa para o boleto 101, o processo gerar um movimento com os seguintes valores:

Valor do percentual do POEB não tributável: 80%

Movimento 201 no valor: R$ 1000,00

Item do movimento com preço unitário não tributável de: R$ 800,00

Item do movimento com preço unitário tributável de: R$ 200,00

**Observa que a diferença entre os movimentos dos exemplos 1 e 2, é que no exemplo 2 são criados dois item de movimentos iguais ontem a diferença é o valor de cada um. Isso porque, é criado um item de movimento para o valor não tributável e outro item de movimento para o valor tributável.**

Exemplo 3: Geração do movimento por caixa com a utilização do benefício POEB com desconto

Contrato A do aluno ES-0001 tem uma parcela com desconto para o serviço de mensalidade

Parcela 1 no valor: R$ 1000,00.

A parcela 1 tem o lançamento 10 gerado no valor: R$ 1000,00.

O desconto de 15% da parcela:  R$ 150,00 

O lançamento 10 tem o boleto 101 gerado no valor: R$ 1000,00

Na geração do movimento por caixa para o boleto 101, o processo gerar um movimento com os seguintes valores:

Valor do percentual do POEB não tributável: 80%

Movimento 201 no valor: R$ 1000,00

Item do movimento com preço unitário não tributável de: R$ 800,00

Valor do desconto: R$ 120,00

Item do movimento com preço unitário tributável de: R$ 200,00

Valor do desconto: R$ 30,00

**Caso o contrato tenha bolsa, o valor da bolsa configurada para sair na nota fiscal também terá o seu valor proporcionado conforme o desconto baseado no valor percentual do POEB.**

Exemplo 4: Geração do movimento por caixa com a utilização de 0% do benefício POEB

Contrato A do aluno ES-0001 tem uma parcela sem desconto para o serviço de mensalidade

Parcela 1 no valor: R$ 1000,00.

A parcela 1 tem o lançamento 10 gerado no valor: R$ 1000,00.

O lançamento 10 tem o boleto 101 gerado no valor: R$ 1000,00

Na geração do movimento por caixa para o boleto 101, o processo gerar um movimento com os seguintes valores:

Valor do percentual do POEB não tributável: 0%

Movimento 201 no valor: R$ 1000,00

Item do movimento com preço unitário de: R$ 1000,00

**Como o percentual do benefício do POEB é zero porcento não será necessário informar no item de movimento se o seu valor é tributável ou não tributável.**

Exemplo 5: Geração do movimento por caixa com a utilização de 100% do benefício POEB

Contrato A do aluno ES-0001 tem uma parcela sem desconto para o serviço de mensalidade

Parcela 1 no valor: R$ 1000,00.

A parcela 1 tem o lançamento 10 gerado no valor: R$ 1000,00.

O lançamento 10 tem o boleto 101 gerado no valor: R$ 1000,00

Na geração do movimento por caixa para o boleto 101, o processo gerar um movimento com os seguintes valores:

Valor do percentual do POEB não tributável: 100%

Movimento 201 no valor: R$ 1000,00

Item do movimento com preço unitário não tributável de: R$ 1000,00

**Como o percentual do benefício do POEB é cem porcento é necessário informar no item de movimento se o seu valor é não tributável.**

Exemplo 6: Geração do movimento por caixa com e/ou sem serviço considerando a utilização do benefício POEB

Contrato A do aluno ES-0001 tem duas parcelas sem desconto 

Parcela 1 para o serviço de mensalidade no valor: R$ 1000,00.

A parcela 1 tem o lançamento 10 gerado no valor: R$ 1000,00.

O lançamento 10 tem o boleto 101 gerado no valor: R$ 1000,00

Parcela 2 para o serviço de natação no valor: R$ 100,00.

A parcela 2 tem o lançamento 20 gerado no valor: R$ 100,00.

O lançamento 20 tem o boleto 201 gerado no valor: R$ 100,00.

Serviço mensalidade tem o campo "Considerar utilização do benefício do POEB na geração de movimento" **marcado**.

Serviço natação tem o campo "Considerar utilização do benefício do POEB na geração de movimento" **desmarcado**

Na geração do movimento por caixa para o boleto 101, o processo gerar um movimento com os seguintes valores:

Valor do percentual do POEB não tributável: 80%

Movimento 201 no valor: R$ 1000,00

Item do movimento com preço unitário não tributável de: R$ 800,00

Item do movimento com preço unitário tributável de: R$ 200,00

Na geração do movimento por caixa para o boleto 201, o processo gerar um movimento com os seguintes valores:

Valor do percentual do POEB não tributável: 80%

Movimento 301 no valor: R$ 100,00

Item do movimento com preço unitário não tributável de: R$ 100,00
