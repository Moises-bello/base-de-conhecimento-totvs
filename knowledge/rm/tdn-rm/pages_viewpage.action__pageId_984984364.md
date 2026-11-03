---
content_hash: 186dc0ab884f132d368b5a74913aa04072a2d3c4d735f9de14133054aca1290a
fetched_at: '2026-06-29T00:12:16.283859+00:00'
page_id: '984984364'
product: rm
source: tdn-rm
title: Validação da Licença de Funcionário – Folha de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=984984364
version: 3
---

No produto TOTVS Folha de Pagamento, existe uma validação que verifica se a quantidade de funcionários na base de dados está dentro do limite contratado na licença.

O sistema realiza essa validação de duas formas:

---

**1 – Processo de Liberação de Competência**

**1-1 -** Durante a liberação da competência, o sistema compara a quantidade de funcionários ativos no produto com o limite da licença. Para isso, considera:

* + Funcionários que possuem evento na ficha financeira no mês da liberação, excluindo os demitidos.

**1-2 -** Se o limite for excedido, o sistema emitirá um alerta por duas liberações consecutivas e, na terceira, bloqueará a liberação, exigindo contato com o departamento Comercial da TOTVS para regularização.

**1-3 -** Exemplo de consulta SQL para contagem de funcionários ativos:

`SELECT COUNT(*) FROM PFUNC (NOLOCK)
WHERE ((CODSITUACAO <> 'D' AND CODTIPO <> 'A') OR
(CODTIPO = 'A' AND CODSITUACAO <> 'D' AND
EXISTS (SELECT 1 FROM PFFINANC (NOLOCK)
WHERE PFFINANC.CODCOLIGADA = PFUNC.CODCOLIGADA
AND PFFINANC.CHAPA = PFUNC.CHAPA
AND PFFINANC.ANOCOMP = :ANOCOMP
AND PFFINANC.MESCOMP = :MESCOMP)))`

**1-4**- A verificação da quantidade de funcionários permitidos na licença é feita através do License Server do cliente.

**Mensagens Apresentadas**

**Aviso**

**Atenção!** Usuário excedeu o limite de funcionários permitidos de acordo com a sua licença de uso que é de xxx funcionários, atualmente você possui xxx funcionários cadastrados. Até a regularização da situação você terá direito à 3 liberações de competência, sendo essa a {2}ª. Favor entrar em contato com o Departamento do Comercial da TOTVS no intuito de regularizar essa situação o mais rápido possível.

**Após 3 liberações de competência ele bloqueia**

**Atenção!** Usuário excedeu o limite de funcionários permitidos de acordo com a sua licença de uso que é de XXX funcionários, atualmente você possui XXX funcionários cadastrados, e já foram esgotadas as 3 liberações de competência permitidas durante situação irregular. Informamos que a liberação de competência não será permitida. Favor entrar em contato com o Departamento Comercial da TOTVS no intuito de regularizar essa situação o mais rápido possível.

---

**2 – Inclusão de Funcionário**

Ao incluir um novo funcionário e clicar em <Salvar>, o sistema verifica se a quantidade de funcionários ativos cadastrados no produto ultrapassa o limite da licença, conforme descrito no **item 1** acima, com **exceção** do descrito no **item 1.2**, ao incluir um funcionário, o sistema aplica um cálculo que impede a inclusão caso o limite seja excedido, considerando uma margem de tolerância que varia entre 10 e 30 funcionários, dependendo da base.

### Exemplo:

* A empresa possui uma licença para até **500 funcionários**.
* O sistema considera uma margem de até **10%**:  
  `500 x 10% = 50`

Quando começa a avisar sobre a aproximação do limite?

O que depende da base para ser diferente?
