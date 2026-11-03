---
content_hash: c3370d60b694c07912d47961e5b9ecab7f78f26ac6c1e110e7a143829df08839
fetched_at: '2026-06-29T00:06:22.461142+00:00'
page_id: '223919110'
product: rm
source: tdn-rm
title: Transformar Campo Complementar em Lookup
type: documentation
url: https://tdn.totvs.com/display/LRM/Transformar+Campo+Complementar+em+Lookup
version: 22
---

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.9 |
| **Ocorrência:** | Transformação de um campo complementar em lookup. |
| **Ambiente:** |  |
| **Passo a passo:** | ``` Este documento tem por finalidade exemplificar como transformar um campo complementar em lookup. Como exemplo iremos utilizar o módulo do RM Officina (Totvs Manutenção) ```    ATENÇÃO:  ``` Somente campos complementares podem ser transformados em LookUp.  ```  ``` Caso o campo não seja um campo complementar somente o Label será alterado. ```     Acesse o módulo "RM Officina" e clique em "Cadastros | Campos Complementares".   ``` Em seguida adicione as colunas chaves desse lookup: CODCOLIGADA e CODFILIAL. ```    ATENÇÃO:  ``` Caso a tabela do formulário contenha a chave do lookup, o campo complementar deverá ter um nome diferente da chave. ```          ``` Após a criação dos campos complementares, crie uma fórmula visual para alterar o campo Textbox para Lookup. ```  ``` Na criação da formula, utilize a atividade “Alterar Propriedades da Coluna”. A atividade é configurada de acordo com a imagem abaixo: ```    ATENÇÃO: Separe as chaves Local e Lookup com "ponto e virgula" sem espaços.     ```  ```   Em seguida adicione outra atividade *"Alterar Propriedades da Coluna",* e a configure conforme imagem abaixo:        Depois de configurar a fórmula visual, adicione o gatilho "Após a leitura da visão" no objeto.  Pesquise pelo nome "Objeto de Manutenção", e adicione a action "MntObjOficinaData".        Feito isso acesse "Manutenção | Objeto de Manutenção | Objeto de Manutenção" e edite um objeto qualquer. Clique na aba "Campos Complementares", e observe que o campo "Filial" está configurado como Lookup. |
| **Observações:** | Essa funcionalidade é válida somente para aplicação windows forms( nova MDI ). |
