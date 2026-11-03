---
content_hash: 8a68a554da258f95563679dc88b4f6d5d6420a674d856ed90e3e10a41d86e5f9
fetched_at: '2026-06-29T00:08:58.613964+00:00'
page_id: '360451176'
product: rm
source: tdn-rm
title: Como limpar a Fila de Eventos ?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=360451176
version: 8
---

|  |  |
| --- | --- |
| **Produto:** | TOTVS Folha de Pagamento |
| **Dúvida:** | Como limpar a Fila de Eventos ? |
| **Resposta:** | Para limpar a fila de eventos,  deverá utilizar o processo "Limpa Fila de eventos" no menu eSocial / Outros Processos/ Limpar Fila de Eventos.    **Esse processo apaga todos registros existentes na fila de eventos independente do seu status. Pode ser usado quando a empresa necessitar alterar o tipo de ambiente de testes para produção, ou seja, quando precisar apagar todos os registros resultantes de testes, passando então a ter seu ambiente como produção.**     **Atenção:**   1. Deverá ser selecionado quais os tipos de eventos que serão considerados na execução do processo. 2. Antes de "Limpar Fila Eventos " é  imprescindível ter executado o processo 'Atualizar Status Integração TAF' . 3. Esse processo é **IRREVERSÍVEL**. Sendo assim é importante ter certeza da necessidade da sua execução. 4. Caso o tipo de ambiente seja igual a "1-Produção" e existir eventos na fila com status igual a 10-Aceito RET, não será possível concluir o processo “Limpar fila de Eventos”  e será exibida a seguinte mensagem para o usuário:   Foram encontrados eventos do eSocial já transmitidos para o RET (governo) nas coligadas:"XXX".  Os eventos dessas coligadas não foram excluídos.        Caso esteja em ambiente diferente do tipo "1-Produção", será possível concluir o processo “Limpar a fila de Eventos” .     Para ambos os casos será exibida a mensagem para o usuário:     ATENÇÃO!     Foram encontrados eventos do eSocial já integrados com o TAF nas coligadas: “XXX”                          Para manter a integridade das informações, após excluir os eventos no RM será necessário excluir                           também os eventos no TAF Confirma a exclusão?. |
