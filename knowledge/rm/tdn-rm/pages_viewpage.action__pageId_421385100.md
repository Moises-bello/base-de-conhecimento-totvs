---
content_hash: 9dd1ac36e5fb282583a26d0dcb665818c5675b1b6d612259780fbdfc3dfa27c3
fetched_at: '2026-06-29T00:09:13.743549+00:00'
page_id: '421385100'
product: rm
source: tdn-rm
title: Apropriação de Apontamentos de Equipamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385100
version: 4
---

---

Os apontamentos de equipamentos, recebidos dos coletores, quando não existe integração com o SIGA-MNT (Protheus) podem ser apropriados através da execução manual do processo de apropriação.  
 Para a apropriação das horas improdutivas, poderá ser definida nos parâmetros do projeto uma tarefa para a apropriação das mesmas. Caso a tarefa não seja definida, as horas improdutivas serão apropriadas nas tarefas produtivas que foram apontadas para este equipamento, nesta mesma data e centro de custo.  
 No caso de existir mais de um insumo vinculado à família do bem que está no apontamento, a apropriação vai ser realizada para o primeiro insumo encontrado. Caso não encontre nenhum insumo a partir do bem, não será realizada a apropriação e será informado no log de erros.  
 No caso de erros durante o processo de apropriação poderá ser enviado um e-mail para o usuário/grupo parametrizado informando que existem apontamentos que não foram apropriados e que devem ser apropriados de forma manual.

**Importante:**

* O cálculo do valor para apropriação é o seguinte: Valor para apropriação = Quantidade apontada \* Preço do insumo;
* Nos casos onde for necessário informar a tarefa, deve-se selecionar tarefas pertencentes ao mesmo centro de custos do apontamento, para que a apropriação seja realizada com sucesso.

**Passos para executar Apropriação Manual de Apontamentos de Equipamentos:**

1. Acessar o TOP
2. Selecionar o projeto
3. Acessar o menu Cadastros|Mobilidade|Equipamentos|Apontamentos de equipamentos
4. Selecionar apontamentos que possuam status = "Pendente"
5. Acessar o menu Processos|Apropriação de apontamentos de equipamentos
6. Informar obra/etapa/tarefa para apropriação dos apontamentos (caso o apontamento não possua tarefa preenchida)
7. Sistema apropria os apontamentos baseado no preço do insumo
8. Sistema altera o status dos registros para "Apropriado".
