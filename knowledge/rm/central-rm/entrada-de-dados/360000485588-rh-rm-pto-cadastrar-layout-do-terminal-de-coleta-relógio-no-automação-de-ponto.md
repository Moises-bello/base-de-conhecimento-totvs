---
article_id: 360000485588
category: Entrada de dados
content_hash: a97dfafbb1569ad96c70d39c8f14247b2082c962a3a8bd6249488f14145ab316
fetched_at: '2026-06-28T22:46:30.597385+00:00'
product: rm
section_id: 1500000835061
source: central-rm
title: RH - RM - PTO - Cadastrar layout do terminal de coleta (relógio) no Automação
  de Ponto
type: support-article
updated_at: '2024-05-15T19:51:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000485588-RH-RM-PTO-Cadastrar-layout-do-terminal-de-coleta-rel%C3%B3gio-no-Automa%C3%A7%C3%A3o-de-Ponto
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16814808411287) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Como cadastrar layout do relógio onde realizar a marcações no Automação de Ponto?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80

**Solução**Para efetuar o registro de layouts no **Automação de Ponto**, siga as instruções abaixo:

1. Acesse o menu **Entrada de Dados | Layout**:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21855649280791)
2. Escolha a opção de inclusão e preencha o **Código do Relógio** e a **Descrição do Relógio** na guia de identificação. Se estiver utilizando o layout **AFD** (Arquivo de Fonte de Dados), selecione o tipo de layout de acordo com a Portaria desejada.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21855649317527)  
     
   Aqui está a distinção entre cada tipo de layout:  
   **Utiliza layout AFD para importação da Portaria 1510/2009**: Se deseja importar batidas conforme o layout AFD da Portaria 1510/2009, selecione este parâmetro. A validação é feita por PIS para a importação.  
   **Utiliza layout AFD da Portaria 671/2021:** Se deseja importar batidas conforme o layout da Portaria nº 671/2021, selecione este parâmetro. De acordo com a portaria, Registro do tipo "3", posição 035-046, será reconhecido o PIS, CPF ou sua composição, sendo a leitura iniciada da esquerda para direita, contendo os 12 dígitos iniciando com o 0, 8 e 9 ou contendo apenas o CPF nas 11 primeiras posições e na 12ª posição com espaço.  
   **Utiliza layout AFD Portaria 671/2021, contém somente CPF:** Se deseja importar batidas conforme o layout da Portaria nº 671/2021, selecione este parâmetro. Esta opção deverá ser utilizada quando os registradores de pontos que gerem o AFD apenas com o CPF do funcionário no Registro do tipo "3", posição 035-046. Nesta posição o CPF poderá ser preenchido com o zero na 1ª posição ou com espaço na 12ª posição.  
     
   Nota: Ao selecionar uma das opções acima, a guia "Layout" será desativada, seguindo o layout conforme as portarias 1510 ou 671 determinadas pelo MTE (Ministério do Trabalho e Emprego) para a importação de batidas.
3. Se deseja cadastrar um layout personalizado, não escolha nenhuma das opções disponíveis de tipo de layout para habilitar a guia Layout.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21855672210199)
4. Na guia **Layout**, defina as posições das informações.  
     
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21855649350935)
5. Para testar o layout, clique no botão **Abrir**, selecione o caminho onde o arquivo está salvo e clique em **Testar**. Os campos da seção **Teste do Layout** serão preenchidos com as informações do arquivo selecionado. A seção **Estrutura do Layout** demonstra uma previsão da estrutura.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/21855672241303)
6. Após as alterações, clique em **Salvar**.

**Saiba Mais**

Para maiores informações acesse os documentos abaixo:  
[TDN - Layout de Relógio](https://tdn.totvs.com/pages/viewpage.action?pageId=452718923)  
[TDN - Portaria 671 - Leitura do Novo Layout AFD](https://tdn.totvs.com/display/public/ConSeg/Portaria+671+-+Leitura+do+Novo+Layout+AFD)  
[RH - RM - PTO - Como importar as marcações para o Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000486068)  
[RH - RM - PTO - Tipos de REPs (Registros Eletrônicos de Ponto) de acordo com a Portaria 671](RH%20-%20RM%20-%20PTO%20-%20Tipos%20de%20REPs%20(Registros%20Eletr%C3%B4nicos%20de%20Ponto)%20de%20acordo%20com%20a%20Portaria%20671)  
[AFD - ARQUIVO FONTE DE DADOS](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/fiscalizacao-do-trabalho/leiaute-do-arquivo-fonte-de-dados-afd.pdf)   
[PORTARIA/ Nº 1.510](https://www.normaslegais.com.br/legislacao/portaria1510_2009.htm)  
[PORTARIA/MTP Nº 671](https://in.gov.br/en/web/dou/-/portaria-359094139)  
[Perguntas e Respostas - Portaria n° 671/2021](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/fiscalizacao-do-trabalho/Perguntas%20e%20Respostas%20REP)
