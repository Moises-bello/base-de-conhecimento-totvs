---
content_hash: 453fe90ea19a0cd81474d3e522f3a49ef9a30c82e79b5adf3a876b3161f07b1c
fetched_at: '2026-06-29T00:09:32.534624+00:00'
page_id: '425458868'
product: rm
source: tdn-rm
title: Layout do Arquivo de Notas
type: documentation
url: https://tdn.totvs.com/display/LRM/Layout+do+Arquivo+de+Notas
version: 7
---

Essa forma de obtenção de notas exigirá que os candidatos já estejam vinculados às provas do TOTVS Avaliação e Pesquisa. A instituição tem a opção de utilizar meios de correção de provas extra-sistema. Dessa forma, a obtenção de notas não passará pela execução do processo "Importar Gabaritos".  Ou seja, os gabaritos não serão lidos para o sistema e a funcionalidade de correção do TOTVS Avaliação e Pesquisa não será utilizada.

Neste caso será necessário gerar, de alguma forma, um arquivo txt no layout "Arquivo de Notas".  Conforme o layout, nesse arquivo não constará as respostas e sim as notas totais já computadas para cada uma das provas. O layout limita a nove o número de notas possíveis de serem informadas para cada candidato.

Registro de presença

A partir da versão 12.1.2510, prevista para outubro de 2025, será possível registrar a presença dos candidatos no fluxo de classificação por meio da importação do "Arquivo de Notas", que agora conta com um novo campo opcional, no layout, chamado **Ausente**.

O preenchimento desse campo deve ser realizado da seguinte forma:

* **"S"** – Para candidato ausente.
* **"N"** ou **""** (vazio) – Para candidato presente.

Caso não deseje utilizar o registro de presença por meio desse novo campo, é possível remover a coluna **Ausente** do arquivo e continuar utilizando o layout adotado anteriormente.

Caso alguma informação do candidato esteja incorreta e ele não seja encontrado no documento de importação de notas, e a opção **"Consultar o registro de presença de candidatos"** esteja marcada, o candidato será considerado ausente no dia da prova.

|  |  |  |
| --- | --- | --- |
| **Coluna** | **Descrição** | **Obrigatório?** |
| CODCOLIGADA | Código da coligada | Sim |
| IDPS | Código do processo seletivo | Sim |
| CODPESSOA | Código de pessoa do candidato | Não |
| NUMEROINSCRICAO | Número da inscrição | Sim |
| IDETAPA | Código da etapa | Sim |
| NOTAPROVA1 | Nota total da prova 1 (se não houver nota colocar o valor zero) | Sim |
| NOTAPROVA2 | Nota total da prova 2 (se não houver nota colocar o valor zero) | Sim |
| NOTAPROVA3 | Nota total da prova 3 (se não houver nota colocar o valor zero) | Sim |
| NOTAPROVA4 | Nota total da prova 4 (se não houver nota colocar o valor zero) | Sim |
| NOTAPROVA5 | Nota total da prova 5 (se não houver nota colocar o valor zero) | Sim |
| NOTAPROVA6 | Nota total da prova 6 (se não houver nota colocar o valor zero) | Sim |
| NOTAPROVA7 | Nota total da prova 7 (se não houver nota colocar o valor zero) | Sim |
| NOTAPROVA8 | Nota total da prova 8 (se não houver nota colocar o valor zero) | Sim |
| NOTAPROVA9 | Nota total da prova 9 (se não houver nota colocar o valor zero) | Sim |
| AUSENTE | Registro de ausência (colocar "S" para candidato ausente e "N" ou "" (vazio) para candidato presente) | Não |

 

**EX de uma linha do arquivo**:  
1;11;;7;19;10;0;0;0;0;0;0;0;0

Veja também

Clique em [Associando a prova na área ofertada do processo seletivo](https://tdn.totvs.com/pages/viewpage.action?pageId=896383314) para saber mais sobre os critérios de desempate.
