---
article_id: 7052945414167
category: 'Aplicativo MNTNG '
content_hash: 0efc9115967aff749c6b361aa1dd6c61093cfb18e9020e0f27759d16eb3a5e30
fetched_at: '2026-06-28T22:42:37.669147+00:00'
product: protheus
section_id: 360010992174
source: central-protheus
title: Manufatura - Linha Protheus - APP MNT - Consumo de Licença do MNT NG via Mingle
type: support-article
updated_at: '2024-02-05T20:49:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7052945414167-Manufatura-Linha-Protheus-APP-MNT-Consumo-de-Licen%C3%A7a-do-MNT-NG-via-Mingle
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)* Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como funciona o consumo de licença do aplicativo **MNT NG** via **Mingle**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Aplicativo MNTNG - Todas as versões  
  
**Solução**A implementação tem como objetivo adequar os padrões de autenticação e consumo de licenças do **Aplicativo - APP MNT NG**, através da utilização do **Mingle**. Dessa forma, o **APP MNT NG** passará a consumir uma **licença própria** com código igual a **3033**, ao invés das licenças do módulo de **Manutenção de Ativos - 19** que pode utilizar as licenças **3260, 4160, 4159 e 4161**.**Como é realizada a autenticação via licença MNT - Descontinuada a partir de 30 de Março de 2023**: A autenticação e as validações de usuário/licença são feitas manualmente pelo módulo e responsabilidade da equipe de **Manutenção de Ativos**. Devido as validações de usuário serem feitas pelo módulo, a abertura de ambiente é realizado via função **RPCSETENV**.  
  
**Como é realizada a autenticação via Mingle - Liberada a partir de julho/2022:** A autenticação passa a ser realizada pelo **Framework Protheus** e utilizará o **Mingle** para intermediar o processo entre **APP** e **WebService - WS** conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7052847976087/mceclip0.png)

Para ambientes que já possuem as configurações para utilizar o aplicativo, e será realizada a migração para nova licença, é necessário seguir o passos a seguir:

1. Adquirir novas licenças do **Mingle** para **MNT NG** - Entrar em contato com o **Executivo de Contas** e verificar a **aquisição** de licenças **3033**.
2. Realizar o cadastro do *alias* para o ambiente em [https://mingle.totvs.com.br](https://mingle.totvs.com.br/landpage/);
3. Realizar as configurações no **Protheus** pelo arquivo **appserver.ini**- Veja a documentação [Consumo de Licença por demanda no REST do Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=527852596);
4. Realizar a configuração do novo alias **Mingle** no **Portal Mobile**, conforme imagem abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7052880247447/mceclip2.png)

**Saiba mais**Ao solicitar o *alias* **Mingle**, não é necessário informar **Empresa** / **Filial**, o *alias* **Mingle** deve ser **ÚNICO** para o seu ambiente, para mais informações acesse a documentação [Consumo de licença do MNT NG via Mingle](https://tdn.totvs.com/pages/viewpage.action?pageId=691451743).  
Para ambientes que não possuem as configurações necessárias para a funcionalidade do **MNT NG** acesse a documentação em [Implementando o Mobile - MNT NG - Protheus](https://tdn.totvs.com/display/PROT/Implementando+o+Mobile+%28MNT+NG%29+-+Protheus)
