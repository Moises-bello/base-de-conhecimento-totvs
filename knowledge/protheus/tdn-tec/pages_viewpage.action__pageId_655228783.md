---
content_hash: d5b8154051857dc54efbee6bbf6b0e788575d676a367d8fdf163a56d96e6f645
fetched_at: '2026-07-02T19:24:27.005329+00:00'
page_id: '655228783'
product: protheus
source: tdn-tec
title: e-2 - Execução em thread
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=655228783
version: 4
---

O **PROBAT** por default abre uma thread apartada da execução principal para melhor controle de erros, pois dessa forma, ao ocorrer um error.log na execução do teste o **PROBAT** tem a capacidade de capturar esse erro e continuar com a execução dos demais testes sem interrupção do motor de testes.

Porém, pode ser que um recurso ou outro não possa ser executado com o uso de StartJob() do appserver, então nesse caso o desenvolvedor tem a possibilidade de informar ao **PROBAT** de que deseja que o teste seja executado na mesma Thread do motor de testes.

Contudo há um risco envolvido nesse processo, pois se houver um error.log no teste e não for possível a captura do erro, todo a execução do **PROBAT** será interrompida pois a Thread principal será derrubada.

Por isso demos esse controle nas mãos do desenvolvedor, pois ele determina através de uma propriedade da annotation *[TestFixture]* conforme necessidade e tem controle dos riscos.

Veja os exemplos abaixo.

##### \* Abre a Thread:

cpp

##### \* NÃO abre a Thread:

cpp

```

```

Todos os testes marcados com [thread="no"] serão somente executados ao final de todos os demais testes, justamente para diminuir os riscos já citados acima.

## Todos os testes como Thread = 'no'

Caso seja necessário desabilitar a funcionalidade de abertura de thread para todos os teste, ou seja, nenhum teste será executado em thread destacada, existe uma forma simples sem precisar refatorar todos os testes.

No INI de sua aplicação na seção [PROBAT], adicione a seguinte chave:

```
Dessa forma o PROBAT irá ignorar todas as instruções no metadados 'thread=' dos testes e irá desabilitar a abertura de thread para todos os testes a serem executados.
```
