---
content_hash: 26e4f506f23ef209919151a61f07e7113c98af69b61fe9fcfac89890d82a9309
fetched_at: '2026-06-29T00:09:58.952342+00:00'
page_id: '452718261'
product: rm
source: tdn-rm
title: Representante de Empregado
type: documentation
url: https://tdn.totvs.com/display/LRM/Representante+de+Empregado
version: 4
---

**Representante de Empregado**

Este cadastro tem como objetivo realizar o registro dos Representantes dos Empregados.

**Observações:**

* Todos os funcionários podem ser representantes, exceto demitidos e afastados.
* Início e Fim da Candidatura deve ser inferior a data de início do mandato na Comissão.

**Atenção:**

Após o cadastro do Representante é realizada uma integração com o sistema Folha de Pagamento, registrando a sua estabilidade.

Para verificar a estabilidade acesse Acompanhamento| Funcionários, Anexo Folha de Pagamento| Estabilidade.

* Se o Representante foi cadastrado com o tipo 14 (Candidato Representante dos Funcionários) ele gera a estabilidade com as datas de início e fim da candidatura.
* Se o Representante foi cadastrado com o tipo 15 (Eleito Titular Representante dos Funcionários) ele gera a estabilidade com a data de início da candidatura e data fim do mandato, este acrescido de mais 1 ano.
* Se o Representante foi cadastrado com o tipo 16 (Eleito Suplente Representante dos Funcionários) ele gera a estabilidade com a data de início da candidatura e data fim do mandato, este acrescido de mais 1 ano. Quando incluir a Data de exoneração do Representante, ele finaliza a estabilidade com esta data.
* Se o Representante for excluído da Comissão, os registros da estabilidade também são excluídos.
