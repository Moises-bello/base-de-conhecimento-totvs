---
article_id: 360026398811
category: Controle de Documentos (SIGAQDO)
content_hash: cc444971f8bdf6cabc37b04db5a2cb717cc221e3f9082e29502034652f162895
fetched_at: '2026-06-28T22:42:29.013008+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Documento não liberado
type: support-article
updated_at: '2023-08-04T21:28:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026398811-Manufatura-Linha-Protheus-SIGAQDO-Documento-n%C3%A3o-liberado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:02:20 min****Ocorrência**Ao tentar visualizar, alterar ou excluir um documento na rotina **QDOA050 - Cadastro de Documentos** é apresentada a mensagem **Documento não liberado**.  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões  
  
**Causa**A mensagem **Documento não liberado** é apresentada nas seguintes situações:  
1. Quando o usuário em questão não é responsável pelo documento ou não está configurado para ser leitor do documento.  
2. Na exclusão do documento, quando a situação do documento for diferente de **D - Digitação**, **DC - Digitação com Crítica**, **E - Elaboração**, **EC - Elaboração com Crítica** ou **A - Aprovação**.  
3. Quando o nível de responsabilidade do usuário que está realizando a ação, de alteração ou exclusão, não está parametrizado para alterar o documento.  
  
**Solução**  
Para solucionar cada situação, realize os seguintes passos:  
  
1. Na rotina **QDOA050**, selecione o documento em questão, clique no botão **Outras Ações > Detalhes** e verifique se o usuário em questão recebeu a pendência de leitura anteriormente. Caso sim, está confirmado que o usuário deveria conseguir visualizar o documento. Neste caso, verifique se o usuário trocou de departamento. Verifique também se a **Matrícula**, **Departamento** e **Cargo** que constam na tabela **QD1 - Distribuição por Usuário** são os mesmos que constam na tabela **QAA - Usuários**. Esta verificação pode ser realizada pela da ferramenta **APSDU**, filtrando pelo **código do documento** e **revisão**; Caso as informações do passo 1 já estiverem corretas ou o usuário não recebeu a pendência de leitura deste documento anteriormente, verifique o conteúdo do parâmetro **MV\_QLIBLEI - Define se a Leitura do Documento poderá ser feita por todos os usuários**. Se o conteúdo do parâmetro for igual **S - Sim**, indica que qualquer usuário, independente de ser responsável pelo documento ou ter recebido a pendência de leitura, poderá visualizar o documento.  
2. Somente é possível excluir documento que estejam com situação **D**, **DC**, **E**, **EC** ou **A**.  
3. Neste caso, deve-se verificar qual é responsabilidade do usuário logado para então, verificar na rotina **QDOA020 - Tipos de Documentos** em **Outras Ações/Niv Respon** se para o nível em questão, o campo **Altera Doc** está preenchido como **Sim**.
