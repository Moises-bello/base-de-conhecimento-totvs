---
content_hash: 7b26c9aca39609cff6c9ab6a89df4c371dba44efaa69e8a5c59d2138f7df3712
fetched_at: '2026-06-29T00:09:35.915005+00:00'
page_id: '425459429'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Configuração dos campos Edt/Tarefa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459429
version: 8
---

**Backoffice RM x Protheus SigaMNT - Configuração dos campos Edt/Tarefa**

---

**Edt / Tarefa**  
    
 O campo de código da tarefa, que identifica a obra , etapa e tarefa, aceita por padrão do Protheus SigaMNT 12 caracteres de código. O Backoffice RM está preparado para enviar um número maior de caracteres através da mensagem única. Para que haja a integração entre os dois sistemas é necessário a configuração do campo Edt/Tarefa.

1. A tabela Edt / Tarefa deve ser configurada para aceitar até 50 caracteres.
2. Acesse o Protheus Smart Client.
3. Conectar ao Protheus SigaCFG :
4. Acessar : Base de Dados / Dicionário / Bases de dados.
5. Acessar : Empresa / Dicionario de Dados / Grupo de Campos.
6. Selecione EDT /Tarefa e clique no ícone Editar.
7. Informe 50 no campo Tamanho e clique no ícone Confirmar.
8. Confirmar as 2 mensagens para alterar o grupo.
9. Clique no ícone Atualizar Base de Dados.
10. ```
    Selecione : Grupo de Campos | Edt / Tarefa \[ALTERADO\]
    ```
11. Clique em Avançar
12. Aguarde o final do processamento e clique em Finalizar.
