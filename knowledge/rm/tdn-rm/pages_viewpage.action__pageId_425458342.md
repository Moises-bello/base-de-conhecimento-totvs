---
content_hash: f8e0b74ea24eacf626b2cab22c90302977b7154cdc093793d202a7abc6b0e83f
fetched_at: '2026-06-29T00:09:29.906490+00:00'
page_id: '425458342'
product: rm
source: tdn-rm
title: Tipos de Ocorrência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458342
version: 7
---

Esta funcionalidade permite cadastrar os tipos de  previstos na Instituição de Ensino.

Se o aluno possuir registro de ocorrências, o sistema verificará a configuração do tipo da ocorrência.   
Possibilidades de verificação:

* **Não verificar**: o sistema ignora a ocorrência do aluno;
* **Alertar**: o sistema alerta o usuário sobre as ocorrências do aluno, mas não impede a matrícula;
* **Bloquear**: o sistema alerta o usuário sobre as ocorrências do aluno e impede a continuação da matrícula.

**Exemplo:**  
Uma ocorrência de secretaria para o aluno, pode ser devido a falta de documentos. Neste caso é este tipo é parametrizado o tipo de ocorrência para ser: Não verificada, Alerta, Bloquear qualquer mudança de status do aluno. Nesta tela é possível incluir, editar e excluir cadastros caso haja necessidades de manutenção.

A partir da versão **12.1.29** foram incluídos dois parâmetros de Status:

* **Permite Cadastro:** o sistema levará este parâmetro em consideração no momento de inclusão de alguma ocorrência, seja ela para aluno ou professor tanto no Portal, EducaMobile e RM.exe.
* **Visível no Portal/App:** o portal e mobile utilizarão este parâmetro para validar se o tipo de ocorrência poderá ser exibido no Portal e no EducaMobile. Este parâmetro não influência no RM.exe.

No Portal ao lançar uma ocorrência, todos os grupos serão exibidos para o professor, caso o mesmo tenho permissão em seu perfil conforme mencionado no cadastro de , mas os tipos de ocorrências que ficarão disponíveis para o professor lançar a ocorrência serão os que tiverem os parâmetros **Permite cadastro**e **Visível no Portal/App**marcados. Caso um deles não estiver marcado, o tipo de ocorrência não será exibido. Vale ressaltar que, se o professor já lançou uma ocorrência e o tipo não mais permite cadastro, o professor poderá ver a ocorrência e até editada, mas não irá conseguir cadastrar um nova ocorrência.

No EducaMobile, ao lançar uma ocorrência, somente ficarão disponíveis os  que possuem pelo menos um tipo de ocorrência com os dois parâmetros (**Permite cadastro e Visível no** **Portal/App**) marcados. O restante seja a mesma regra do portal descrita acima.

Para o aluno tanto nos portais (antigo e novo), quanto no EducaMobile, ele somente irá ver as ocorrências que possuem o parâmetro **Visível no Portal/App** marcado.
