---
article_id: 4407512054295
category: esocial - Processos
content_hash: 9a2caaa86807e51b4e1d7ca88fd5ca60285ed82614805683b9eaee4d4d99cd16
fetched_at: '2026-06-28T22:47:08.345867+00:00'
product: rm
section_id: 1500000834441
source: central-rm
title: RH - RM - FOP - eSocial - Erro 400 na ativação do Middleware - Código do Município
  não informado
type: support-article
updated_at: '2024-06-27T19:01:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407512054295-RH-RM-FOP-eSocial-Erro-400-na-ativa%C3%A7%C3%A3o-do-Middleware-C%C3%B3digo-do-Munic%C3%ADpio-n%C3%A3o-informado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao realizar a ativação do Middleware, é apresentado o erro: **Ocorreu erro que impediu a execução do processo. The remote server returned an error: (400) Bad Request.{"code":400,"message":"Código do Município não informado no parâmetro 'countyCode'.","detailedMessage":""}**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro geralmente ocorre quando o município informado no cadastro da coligada não possui correspondência no cadastro de municípios do sistema.  
  
**Solução**Para solução do erro apresentado, siga os passos a abaixo:

1. Acesse o menu **Administração de Pessoal I Cadastros Globais I Coligadas** e verifique se o município informado no campo **Cidade** consta corretamente escrito (sem espaço ao final do texto);

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407517431191/mceclip1.png)

2. No menu **eSocial | Endereços | Municípios** deve existir um município escrito exatamente igual ao supracitado;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407511552535/mceclip2.png)

3. Após garantir que exista um município cadastrado conforme o registro da coligada, acesse o menu **Configurações | Parametrizador | eSocial** e na etapa **De/Para de Endereço** verifique se o campo **Conceito de Classificação para Códigos de Municípios** está preenchido;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407508833943/mceclip0.png)

4. No menu **eSocial | Endereços | Municípios** acessando **Anexos | Codificação de Município**, deve conter uma codificação cadastrada conforme o item utilizado na etapa anterior (etapa 3).

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407511616663/mceclip3.png)

**Saiba mais**  
Para mais informações sobre configuração de endereços e sobre o erro 400, acesse:  
     - [Ao ativar o Middleware ocorre erro sobre cadastro de municípios na coligada](https://tdn.totvs.com/pages/viewpage.action?pageId=546695939)  
     - [Como realizar configurações de endereços?](https://tdn.totvs.com/pages/releaseview.action?pageId=379290027)
