---
content_hash: a29d00888135442f0e93fa0bfd3b3399f22eb462e08f313b2ac30438fffff586
fetched_at: '2026-06-29T00:09:28.075248+00:00'
page_id: '423938652'
product: rm
source: tdn-rm
title: Atualização da Data de Inclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938652
version: 3
---

Ao incluir uma ***conta contábil***, ***conta gerencial*** ou um ***centro de custo*** é obrigatório informar a Data de Inclusão. A data do dia será sugerida como data de inclusão, podendo neste momento, antes de salvar a inclusão dos registros, ser modificada. A data de inclusão é um dado obrigatório na geração do SPED Contábil.

Para as *contas contábeis*, *contas gerenciais* e *centros de custos* já incluídos na base e cuja data de inclusão ainda esteja em branco, o preenchimento da data poderá ser feito editando-se os registros dos respectivos cadastros e preenchendo o campo Data de Inclusão com a data desejada ou através da execução do Processo **Atualização da Data de Inclusão**.

Este processo permitirá ao usuário atualizar a Data de Inclusão de várias *contas contábeis*, *contas gerenciais* ou *centros de custos* ao mesmo tempo. Os procedimentos para a execução deste processo serão os mesmos para os três cadastros: Basta marcarem os registros desejados, acionar o processo e informar a data de inclusão. A data informada será incluída simultaneamente em todos os registros marcados.

**Atenção:**

* Somente será permita a execução deste processo para registros cuja data de inclusão ainda esteja em branco.
* Uma vez preenchida a data de inclusão das *contas contábeis*, *contas gerenciais* e *centros de custos*, ela não poderá mais ser alterada.
* Não será possível gerar o SPED Contábil caso haja no cadastro de *contas contábeis* ou *contas gerenciais/centros de custos*, algum registro em que a 'Data de Inclusão' esteja em branco.
* As contas contábeis que tiverem datas de inclusão maiores que a data final da escrituração gerada para o SPED Contábil não serão enviadas para o registro I050 do arquivo digital, porém,  se para estas mesmas contas existirem movimentações no período da escrituração, estas contas serão enviadas normalmente para o registro I050 com suas respectivas datas de inclusão assim como suas movimentações e, neste caso, como as datas de inclusão destas contas são maiores que a data final da escrituração, serão apresentadas *Advertências* ao validar o arquivo digital no PVA (Programa Validador do SPED Contábil).
