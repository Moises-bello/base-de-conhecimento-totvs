---
article_id: 360020990791
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 42620076793b61cd7bfeb1ee2cfd35cfcdd8512a6bc8e8cd80386dedcaeb0e18
fetched_at: '2026-06-28T22:42:07.840772+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Layout T007
  Código de Origem C30_ORIGEM Inexistente
type: support-article
updated_at: '2022-08-18T17:35:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020990791-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Layout-T007-C%C3%B3digo-de-Origem-C30-ORIGEM-Inexistente
---

**Ocorrência**Erro 1 - Linha: 8 - O valor '9' informado na coluna 28 para o campo Cod. Identific. Origem (C30\_ORIGEM ) não existe na base.

**Ambiente**Protheus – Livros Fiscais – A partir da versão 12.1.17  
  
**Causa**O erro mencionado se trata de um código que não existe na base de dados e na receita.  
![](https://totvssuporte.zendesk.com/attachments/token/Qbs3G1VJ62ohRAGwLdtMBnY93/?name=inline1562414293.png)  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Acesse a tabela SFT e valide se o conteúdo do campo FT\_CLASFIS foi gravado com a origem + CST (090), pois é o primeiro digito do campo FT\_CLASFIS que o extrator fiscal busca a informação.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360024665332/mceclip0.png)

Se o conteúdo do campo FT\_CLASFIS não estiver correto, siga as instruções abaixo:

1. Acesse o **cadastro de produtos(SB1);**  
2. Localize o produto e clique em **alterar;**  
3. Informe um valor valido no campo **B1\_ORIGEM**e clique em **confirmar;**

4.Reprocesse o documento fiscal;  
5. Execute o extrator fiscal, selecionando o *layout* **T013** novamente e execute a rotina de processamento;  
6. Efetue novamente a extração e processamento do***Layout* T007**.

Caso o erro "Código de Origem C30\_ORIGEM Inexistente" for apresentando na integração com o módulo TAF referente documentos de serviços, será necessário verificar se para o documento em questão foi gravado o campo FT\_CLASFIS com algum CST, caso tenha conteúdo, será preciso verificar no cadastro de TES, aba Impostos, através do campo Sit Trib ICM (F4\_SITTRIB) se foi cadastrado algum CST de ICMS.   
  
O campo Sit Trib ICM (F4\_SITTRIB) é configurado para documentos fiscais referente mercadoria. Caso tenha configurado o campo Sit Trib ICM em operações de serviço, para que possa corrigir o erro de integração, será necessário retirar o conteúdo do campo Sit Trib ICM e informar o conteúdo correto de acordo com a regra fiscal no campo Sit Trib ISS (F4\_CSTISS).

Em seguida, efetue o reprocessamento do documento para que possa atualizar a tabela SFT, execute o Extrator Fiscal e, por fim, execute o Processamento do TAF para que possa concluir a integração do documento fiscal.

Para documentos fiscais de serviço é configurado o CST através do campo Sit Trib ISS (F4\_CSTISS) na aba Outros do cadastro de TES.
