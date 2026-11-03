---
content_hash: 324e4cbd1e79dfbfbff930a7a2e06820a7a338233ff062f5ab4ed2631edee4ad
fetched_at: '2026-06-29T00:12:01.668619+00:00'
page_id: '898437596'
product: rm
source: tdn-rm
title: Classificador de Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Classificador+de+Documentos
version: 9
---

* + **O que é o Classificador de Documentos?**
  + O Classificador de Documentos é uma funcionalidade desenvolvida para facilitar a gestão e validação automática de documentos enviados por fornecedores no Portal de Medição de Contratos.

    Com essa ferramenta, o usuário poderá:

    - Cadastrar documentos conhecidos ou personalizados.
    - Treinar documentos personalizados, permitindo que a IA os reconheça e valide.
    - Classificar os documentos em grupos vinculados a contratos específicos.
    - Definir parâmetros de confiabilidade para a validação de documentos:
      * Aprovação automática, reprovação automática ou envio para avaliação manual.**Benefícios do Classificador de Documentos**
    - Automação do processo de validação e categorização de documentos.
    - Flexibilidade ao permitir o cadastro de documentos personalizados.
    - Integração com o fluxo de medição e aprovação de contratos.
    - Redução de erros manuais e otimização de tempo.**Perfil de acesso**

    Para habilitar o Classificador de Documento e o Grupo de Classes de Documento o usuário precisar ter permissão de acesso nas respectivas tags de perfil, de acordo com a necessidade:

    **Cadastro de Documentos:**
  + 1. Acesse Controle> Contrato > Inteligência Artificial - Anexos de Documentos> Classificador de Documento> Adicionar documento.
  + 1. 1. Escolha entre:
       - Documentos Conhecidos: padrões pré-treinados pela IA (ex.: conta de luz Cemig, Carteira de Identidade).
       - Documentos Personalizados: crie e treine documentos novos, conforme a necessidade.2. Treinamento de Documentos Personalizados

    Para criar um documento personalizado:

    1. Defina o nome do documento.
    2. Envie até 3 arquivos para treinamento.
    3. Utilize a opção Visualizar para revisar os arquivos enviados. Caso necessário, remova ou substitua os arquivos.
    4. Clique em Treinar Tipo de Documento.
    5. Clique em Avançar
  + 3.1 Definir Parâmetros de Confiabilidade
  + Após o treinamento, defina os valores de confiabilidade e clique em salvar:
* + No exemplo acima ficou definido da seguinte forma:
  + | Parâmetro | Valor | Ação |
    | --- | --- | --- |
    | % Confiabilidade para Reprovação | Menor que 30% | Reprovação automática. |
    | % Confiabilidade para Aprovação | Maior que 90% | Aprovação automática. |
    | Em Revisão Manual | Entre 30% e 90% | Necessária validação manual. |
* + Na visão de Documentos Cadastrados é possível a edição do treinamento, confiabilidade e até a remoção do documento.
  + Obs.: Documentos conhecidos não permitem alteração no treinamento, apenas nos parâmetros de confiabilidade.
* + Ao clicar em 'Testar Documento', será possível selecionar um arquivo, observando os pré-requisitos estabelecidos:
* + Formatos adotados: .PNG, .JPEG, .JPG, .GIF, .BMP, .WEBP e .TIFF.

    Limite de tamanho por arquivo: até 2 MB

    Obs: a primeira página do arquivo .pdf será convertida em imagem
  + Ao clicar em Classificar Imagem irá retornar a validação do documento:

* + 3.2 Vinculação de Documentos a Grupos de Contratos
    1. Acesse Grupo de Classes de Documentos.
    2. Defina um nome para o grupo.
    3. Adicione os documentos personalizados ou conhecidos ao grupo.

Importante:  Documentos da classe marcados como obrigatórios, com anexos associados ao período, só seguirão o fluxo de aprovação se todos os itens anexados forem **aprovados** pelo *DTA Vision* Document.

* + **Pré-requisito**: No menu Parâmetros do Projeto (F6), em Contratos > Portal de Medição, deve ser definida a fórmula de validação de medição.
  + **Descrição da fórmula:**

    fórmulas novas: QUANTIDADEDOCUMENTOSPDOPRINCIPAL e QUANTIDADEDOCUMENTOSPDOCOMPLEMENTAR

     Retorna o total de classes de documentos com determinado status do período principal.

    Se o status for "reprovado" e documento obrigatório:  
     - Retorna o total de classes de documentos obrigatórios pendentes (reprovados ou não preenchidos) do período   
    Se o status for "aprovado" e documento obrigatório:  
     - Retorna o total de classes de documentos obrigatórios sem documentos "aprovados" e "análise manual" do período  
    Senão  
     - Retorna o total de classes de documentos com o status do período

    **Parâmetros disponíveis na função de fórmula:**

    - **Parâmetro 1 (Obrigatório):** Indica uma escolha binária, onde **1** representa "Sim" e **0** representa "Não".
    - **Parâmetro 2 (Status):** Define o status do processo, podendo assumir os seguintes valores:
    - **0** - Em Análise
    - **1** - Aprovado
    - **2** - Reprovado
    - **3** - Análise Manual
    - **4** - Sem Análise
  + Seguindo esses passos :
    - Edite algum Contrato e, na aba Parâmetros, selecione o grupo de documentos criado.
* + 4. Portal de Medições - Inserção e Validação de Documentos

    No Portal de Medições, ao anexar um documento nos cards de medição:

    1. O documento é enviado para validação da IA.
    2. A IA retorna com o status:
       - Aprovado: validação automática.
       - Reprovado: documento rejeitado.
       - Em Avaliação Manual: aguarda revisão pelo usuário.

    Se existir um fluxo de aprovação, o documento validado pela IA será enviado para esse fluxo após a aprovação dos documentos obrigatórios. Caso contrário, se o documento for validado pela IA e estiver marcado como obrigatório, ele será movido para a coluna **Em Liberação**.
* + Como não foi aprovado os documentos, a seguinte mensagem irá aparecer e o card não será movido para o fluxo de aprovação:
  + Cenário de aprovação:
  + 5. Observações Importantes
    - Somente documentos cadastrados no Classificador (personalizados ou conhecidos) poderão ser adicionados a grupos.
    - Documentos conhecidos são pré-configurados e não podem ser re-treinados.
