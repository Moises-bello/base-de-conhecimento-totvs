---
article_id: 13163882240791
category: Controle de Documentos (SIGAQDO)
content_hash: 82b954a6eed70168bd9b9c8cb9db57bfc313d4f70b57c5b2fc3f823d11c4b712
fetched_at: '2026-06-28T22:42:29.027925+00:00'
product: protheus
section_id: 360005906113
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQDO - Documento Sigiloso
type: support-article
updated_at: '2023-03-17T14:04:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13163882240791-Manufatura-Linha-Protheus-SIGAQDO-Documento-Sigiloso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:03 min****Dúvida**Na rotina **QDOA050 - Cadastro de Documentos** qual a funcionalidade do campo **QDH\_SIGILO - Doc. Sigiloso**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Documentos (SIGAQDO) - Todas as versões]  
  
**Solução**O campo **Doc. Sigiloso** tem a funcionalidade para que quando o parâmetro **MV\_QLIBLEI - Define que qualquer usuário pode ler o documento** estiver configurado igual a **Sim**, alguns documentos continuem inacessíveis para usuários que não são responsáveis pelo documento. Para isto, o campo **Doc. Sigiloso** deve ser configurado com o conteúdo igual a **1-Sim**.

Estando o campo **Doc. Sigiloso** com o conteúdo igual **1-Sim** o comportamento será:  
1. Somente usuário responsável pelo documento poderá acessá-lo (**Digitador**, **Elaborador**, **Revisor**, **Aprovador** e **Homologador**);  
2. Somente será possível **alterar** o conteúdo do campo **Doc. Sigiloso** na geração de **revisão do documento**.

Se o campo **Doc. Sigiloso** estiver com o conteúdo igual **2-Não** os usuários responsáveis e não responsáveis terão acesso ao documento.
