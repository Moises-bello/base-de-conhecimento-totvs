---
content_hash: c2cb8c0c1bf1d1e2375afb20905036a93771282b366568af8dd095d5a28f0ee5
fetched_at: '2026-06-29T00:11:44.983664+00:00'
page_id: '818454991'
product: rm
source: tdn-rm
title: Desalocar demanda
type: documentation
url: https://tdn.totvs.com/display/LRM/Desalocar+demanda
version: 19
---

Para turmas criadas através do processo de Realocar demanda, foi criado o processo de Desalocar demanda.

Somente é possível desalocar demanda de turmas de Demanda realocada, não sendo possível executar essa operação em turmas de Demanda original ou outro tipo de turma gerado por outros processos.

Caso selecione alguma turma de Demanda original ou outro tipo de turma diferente de turma de Demanda realocada e tente executar ação de Desalocar demanda, o sistema emitirá uma mensagem informando que não é possível desalocar turmas desses tipos.

Caso a turma de Demanda realocada selecionada seja também um desses outros tipos: agrupada, agrupadora, gerencial, gerenciada, é necessário desfazer essas operações antes de executar a operação de Desalocar demanda, caso contrário o sistema emitirá uma mensagem informando que não é possível desalocar a demanda de turma desses tipos.

Ao desalocar a demanda de uma turma de Demanda realocada, esta turma deixa de existir e a demanda dela volta a ser somada na demanda existente da turma de Demanda original desta que foi desalocada.

A turma de Demanda original continua com esse status enquanto houver pelo menos 1(uma) turma de Demanda realocada gerada a partir dela.

* **Selecione as turmas de demanda realocada que deseja desalocar demandas**

Elas são identificadas pelo ícone na coluna de "Ações":

* **Em seguida, clique sobre a caixa de seleção "Selecione uma ação" e clique em "Desalocar demanda".**

***Nota-se também que, como foram selecionadas todas as turmas de "Demanda realocada", a turma da demanda original perdeu seu status de Demanda original.***

```

```
