---
article_id: 38941468760343
category: Financeiro - Movimentos Bancários
content_hash: 7921eb51dd84bbf62da687c91e3c7d23147817c1138a6a8b0c6c931d6c45791d
fetched_at: '2026-06-28T22:37:31.850988+00:00'
product: protheus
section_id: 35057601824535
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA100 - Como demonstrar
  o valor em Dólar na movimentação bancária ?
type: support-article
updated_at: '2026-03-19T11:23:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38941468760343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Como-demonstrar-o-valor-em-D%C3%B3lar-na-movimenta%C3%A7%C3%A3o-banc%C3%A1ria
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38941489773207) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como visualizar o valor do movimento bancário em Dólar (Moeda 2) na rotina FINA100 (Movimentação Bancária)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**  
Por padrão, a rotina **FINA100** exibe o valor do movimento através do campo **E5\_VALOR** (Moeda 1 - Real). Para visualizar o valor correspondente em **Dólar**, é necessário que o campo **E5\_VLMOED2** esteja configurado como "Browse" no Dicionário de Dados.

Desta forma, o sistema passará a exibir a coluna com o valor convertido no *browser* da rotina, permitindo a conferência direta entre as moedas.

### **Passos**

1. Acesse o módulo **SIGACFG** (Configurador);
2. Vá em **Base de Dados > Dicionário > Bases de Dados**;
3. No menu à esquerda, selecione **Dicionário de Dados** e pesquise pela tabela **SE5** (Movimentação Bancária);
4. Clique no ícone de edição (Lápis) e localize o campo **E5\_VLMOED2**;
5. Na aba **Visualização**, certifique-se de que o campo esteja marcado para exibição no **Browser**;
6. Confirme as alterações e clique em **Atualizar Base de Dados**;
7. Após o processo, acesse o **SIGAFIN** > Atualizações > Movimentos Bancários > **Movimentos (FINA100)** e verifique a nova coluna disponível.  
     
   Print de exemplo dos valores em Real e em Dolar demonstrado na rotina  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38941489773847)

**Saiba mais:**  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Incluir um campo da mesma tabela no browser da rotina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024437412-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Incluir-um-campo-da-mesma-tabela-no-browser-da-rotina)
