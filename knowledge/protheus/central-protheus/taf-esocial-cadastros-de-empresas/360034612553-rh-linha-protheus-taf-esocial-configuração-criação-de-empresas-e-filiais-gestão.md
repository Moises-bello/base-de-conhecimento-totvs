---
article_id: 360034612553
category: TAF - eSocial - Cadastros de empresas
content_hash: 966a31301201228452d1746a1e402444668b843c363e5bbddeee73f0e7423f71
fetched_at: '2026-06-28T22:45:16.483223+00:00'
product: protheus
section_id: 1500001547962
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - Criação de Empresas e
  Filiais (Gestão de Empresas)
type: support-article
updated_at: '2026-06-24T12:20:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034612553-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-Cria%C3%A7%C3%A3o-de-Empresas-e-Filiais-Gest%C3%A3o-de-Empresas
---

**Dúvida**Como criar empresas e filiais no TAF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões  
  
**Solução**

1. Para criar grupos de empresas, empresas e filiais no TAF, siga os passos abaixo no Configurador (SIGACFG).
2. Caso você tenha dúvidas sobre como acessar o configurador do TAF, consulte o artigo de auxílio: "[Como acessar o configurador?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036108413)"  
     
   **CRIANDO GRUPOS DE EMPRESAS:**
3. Acesse o Configurador (SIGACFG) > Ambiente > Empresas > Grupo de Empresas.  
   ![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044127294)
4. Clique em "Incluir".  
   ![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044126794)
5. Na tela de criação do grupo de empresas, preencha os campos da seguinte maneira:

   * No campo "Código", selecione um número que identificará esse grupo de empresas (exemplo: 12).
   * No campo "Descrição", defina o nome do grupo de empresas.
   * No campo "Tamanho", defina a quantidade de caracteres que o campo "Filial" das tabelas irá aceitar (exemplo: 6).
   * No campo "Leiaute", defina como os caracteres serão compostos para formar o código da filial.

     + **Exemplo:** O campo "Leiaute" define a estrutura utilizada para o Grupo de Empresas, por exemplo: **EEUUFFFF**

       - As informações gravadas nos campos e filiais são identificadas da seguinte maneira: EE - Dois dígitos para Empresa UU - Dois dígitos para a Unidade de Negócio FFFF - Quatro dígitos para a Filial
       - Para cada identificador, é possível definir uma máscara de restrição para preenchimento, conforme o exemplo a seguir:

         * E - 0-9 (somente números entre 0 e 9)
         * E - 5-9 (somente números entre 5 e 9)
         * U - A-Z (somente caracteres entre A e Z)
         * U - X-Z (somente caracteres entre X e Z)
         * F - !-! (qualquer dígito numérico ou alfanumérico)
         * F - A,B,5,9 (somente caracteres A, B, 5 e 9)
         * F - 0-9 (somente números entre 0 e 9)
         * F - A-Z (somente caracteres entre A e Z)
6. Após a inclusão do grupo de empresas, o administrador deverá incluir e relacionar os cadastros de Empresas, Unidades de Negócios e Filiais de acordo com o layout aplicado nos exemplos a seguir:  
     
   * Para o layout EEUUFF, o administrador deverá relacionar os seguintes cadastros:

     + Empresas X Grupo de Empresas
     + Unidades de Negócio X Empresas
     + Filiais X Unidades de Negócios
   * Para o layout EEFF, o administrador deverá informar:

     + Empresas X Grupo de Empresas
     + Filiais X Empresas
   * Para o layout FF, o administrador deverá informar:

     + Filiais X Grupo de Empresas
7. Após configurar a empresa, clique em "Confirmar". Uma janela será exibida perguntando se deseja criar o dicionário de dados agora.  
   * + - Se clicar em "Não", o dicionário será criado ao acessar algum módulo por essa empresa.
       - Se clicar em "Sim", será feita uma nova pergunta.

   ![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044988353)
8. Criar Dicionário (Caso tenha clicado em sim):
   * [RECOMENDADO] "A partir de uma base existente". Será aberta uma janela para selecionar a empresa base e, em seguida, uma janela para informar o diretório dos arquivos de dados. Selecione a pasta "data".
   * "Com registros padrão:" Será exibida uma janela solicitando que você informe o país. Certifique-se de selecionar o país correto antes de prosseguir. Em seguida, será exibida uma janela para informar o diretório dos arquivos de dados. Selecione a pasta "data".
   * "Não criar agora:" O dicionário será criado ao acessar algum módulo por essa empresa.

     ![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044988373)  
      **CRIANDO EMPRESAS:**
9. Saia do menu Grupo de Empresas e acesse o menu Empresas.  
   **![7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044127654)**
10. Clique em "Incluir".
11. Preencha os campos da tela de criação de empresas da seguinte forma:

    * Em "Grupo", digite o código do Grupo de Empresas que você criou.
    * Em "Código", insira o código que essa Empresa terá (exemplo: 01).
    * Em "Descrição", defina o nome da Empresa.
    * Clique em "Confirmar".![8.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044989793)  
        
      **CRIANDO FILIAIS:**
12. Saia do menu **Empresas**, e acesse o menu **Filial:**![9.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044128654)
13. Clique em Incluir;
14. Selecione o código do Grupo e da Empresa à qual essa Filial pertence. Em seguida, defina um código para esta Filial (exemplo: 01).

    * Em "Descrição", defina o nome da Filial.
    * Os demais campos, que não possuem asterisco, são opcionais, mas recomendamos preenchê-los, pois são importantes para o envio das obrigações fiscais (eSocial e REINF).
    * Após preencher os campos, clique em "Confirmar".  
      ![10.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044128794)
15. Após criar os grupos, as filiais e as empresas, ao acessar o TAF, você verá as seguintes telas:  
    ![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045067853)
16. Deixe a opção "SERVIDOR" selecionada e clique em "Abrir".![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360044206874)
17. Serão criados novos grupos de empresas.  
    ![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045067873)
18. Aguarde a conclusão do processo de criação dos grupos de empresas.
19. Acesse o módulo SIGATAF e realize a amarração de empresas conforme material abaixo:  
    [Automação Fiscal - Configuração - Como efetuar amarração de empresas no Complemento Cadastral no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034976434)
