---
article_id: 360034522854
category: TAF - eSocial - DBAccess
content_hash: c0e9f695cffc7040988db9fcda43a984f7a00cdc4e8d6fdf42c7d9936e641f40
fetched_at: '2026-06-28T22:45:12.410187+00:00'
product: protheus
section_id: 1500001536981
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - ATUALIZAÇÃO - Como atualizar o DBAccess
  para o TAF
type: support-article
updated_at: '2026-06-26T11:17:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034522854-RH-Linha-Protheus-TAF-eSocial-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-DBAccess-para-o-TAF
---

**Dúvida:**   
Como proceder à atualização do DBAccess?

**Ambiente:**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Todas as versões.

**Solução:**

1. Realize o download do DBAccess clicando no link correspondente à sua arquitetura:  
WINDOWS X64: <https://suporte.totvs.com/portal/p/10098/download#detail/1168438>

LINUX X64: <https://suporte.totvs.com/portal/p/10098/download#detail/1168439>

2. Descompacte o arquivo baixado em uma pasta temporária.

3. Interrompa a execução do serviço do DBAccess:  
![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045971253)

4. Verifique em qual diretório o DBAccess está instalado para realizar a atualização:  
![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045972493)  
  
- Faça uma cópia da pasta do DBAccess como medida de segurança.

5. Copie todos os arquivos descompactados para a pasta do DBAccess, substituindo seu conteúdo:  
![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360045973053)

6. Após a atualização, acesse o diretório do DBAccess e vá para a pasta CLIENT.  
- Copie o arquivo DBAPI.DLL.

7. Acesse as pastas do TAF em BIN/APP e BIN/APPSERVER.  
- Localize outro arquivo DBAPI.DLL e faça backup do mesmo.  
- Cole o arquivo DBAPI.DLL copiado da pasta CLIENT do DBAccess.

Para mais informações sobre o procedimento de substituição da DLL clique no link abaixo:  
[DBAccess - Como atualizar a biblioteca DBAPI](https://tdn.totvs.com.br/display/tec/DBAccess+-+Como+atualizar+a+biblioteca+DBAPI)

8. Após substituir os arquivos nos binários, reinicie os serviços do TAF.

9. Realize o teste de conexão com o DBAccess seguindo os passos:   
[TAF - CONFIGURAÇÃO - Criando e testando conexões com o DBAccess](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034395574)
