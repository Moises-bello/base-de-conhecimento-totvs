---
article_id: 360053795633
category: PMS - Projetos
content_hash: 5341616c137760cbc20311cf1f584b5cef03a46a78f20a376334d4de656cc7de
fetched_at: '2026-06-28T22:37:14.935997+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAPMS - Help PMSUSRNFE '
type: support-article
updated_at: '2024-02-23T11:55:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053795633-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Help-PMSUSRNFE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21563171682711) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**Help **PMSUSRNFE**, ocorre quando o usuário tenta alterar a Estrutura do Projeto ou ao classificar uma Nota de Entrada.   
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 11.80.  
  
**Solução**

Para que não ocorra o help **PMSUSRNFE**, é necessário que o projeto esteja configurado com o campo **AF8\_CTRUSR**= 2 (Sem controle de usuário), ou caso o mesmo esteja =1 (com controle de usuário), o usuário logado deve estar configurado com acesso ao projeto (Para verificar o acesso, selecione o projeto desejado, vá em outras ações - usuários - Irão aparecer os usuários que possuem acesso ao projeto).

Então, ao tentar relacionar um documento de entrada a um projeto PMS, se estiver configurado conforme mencionado acima, não exibirá o help **PMSUSRNFE**.

Caso o usuário seja o Administrador, o mesmo terá todas as permissões no projeto, sem precisar se preocupar com o conteúdo do campo **AF8\_CTRUSR**.  
  
**Solução quando utiliza integração via EAI :**

Para integração via EAI entre as marcas, se na seção do Job do Web Service, a chave secutity estiver 1, todo o serviço de Web Service do Protheus vai pedir autenticação, e nesse caso, a marca da integração tem que enviar no cabeçalho da mensagem (HEADER da requisição), o usuário e senha válidos do Protheus com autenticação do tipo Basic.

Caso a a **chave security** estiver =0, não será necessário o envio da autenticação.  
  
Procure deixar o campo **AF8\_CTRUSR** com inicializar padrão **"2"** para que não haja o controle do usuário 

**Saiba Mais**  
Para maiores detalhes segue a documentação deste processo: **[Configurar Portais e Webservices](https://tdn.totvs.com/x/apk4E)**Alteração de permissão de usuário no projeto: **[Acesso para Alterar projeto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061165434-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Gest%C3%A3o-de-Projetos-SIGAPMS-Acesso-para-Alterar-projeto)**
