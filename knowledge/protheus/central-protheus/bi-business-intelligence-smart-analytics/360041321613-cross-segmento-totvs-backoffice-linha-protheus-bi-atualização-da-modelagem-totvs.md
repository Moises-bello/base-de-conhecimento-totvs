---
article_id: 360041321613
category: BI - Business Intelligence - Smart analytics
content_hash: eaa0e7d08ae0c621d4c096a8fe6ad029e839d29ca709aa5c30ea80d22fa5cd72
fetched_at: '2026-06-28T22:37:04.099799+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Atualização da modelagem
  TOTVS Smart Analytics
type: support-article
updated_at: '2022-07-27T17:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041321613-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Atualiza%C3%A7%C3%A3o-da-modelagem-TOTVS-Smart-Analytics
---

**Dúvida**Como Realizar a atualização da modelagem **TOTVS Smart Analytics?****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - BI - A partir da versão 12.1.17  
  
**Solução**Após salvar o *backup*, siga os passos a seguir para atualizar a modelagem.   
A princípio, abra o projeto padrão atualizado no **Cloud Connect**, seguindo os passos abaixo:

1. À esquerda, clique na **View Navigator / Import**.  
   ![Analytcs1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053977714/Analytcs1.png)
2. Na janela de diálogo, selecione **General / Existing Projects into Workspace**.  
   ![Analytcs2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053977694/Analytcs2.png)
3. Mantenha a opção **Select root directory**, e clique em **Browse**.  
     
   ![Analytcs3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053977674/Analytcs3.png)
4. Selecione o caminho e clique no projeto desejado. A pasta do projeto a ser selecionada, deve ter a seguinte estrutura:  
     
   ![Analytcs4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053977654/Analytcs4.png)
5. Clique em **OK**.
6. De volta à caixa de diálogo, clique em **Finish**.
7. O projeto será aberto na ferramenta.

1. 1. Dê duplo clique na pasta **Model**.
   2. Dê duplo clique no arquivo: **TOTVSSA.mdl**.
   3. Clique em **Publish model to server**. Neste momento, é realizada uma comparação com o que está na nuvem do **GoodData** e o que está no disco local.  
        
      ![Analytcs5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053977634/Analytcs5.png)
   4. Analise as alterações que serão realizadas.  
      ![Analytcs6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360054824953/Analytcs6.png)

      Se deseja visualizar o ***script*****MAQL**, antes de publicar a modelagem, clique em **Advanced**, e em seguida, em **View MAQL**:

      ![Analytcs7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053977614/Analytcs7.png)

      A tela com o **script MAQL** será exibida, onde é possível copiar o script:

      ![Analytcs8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053977594/Analytcs8.png)

      Para saber mais sobre **MAQL**, acesse: <https://help.gooddata.com/display/doc/Getting+Started+with+MAQL>
   5. Clique em **Publish**, para continuar.
   6. Aguarde a mensagem informando que as alterações foram realizadas com sucesso e clique em **OK**.

**Saiba Mais:  
[Fluxo de atualização Smart Analytics](https://tdn.totvs.com/pages/releaseview.action?pageId=196805227)**
