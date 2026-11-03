---
article_id: 30711438211479
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: f1fd95ac87d4af42265769735692a234707ac346f30e5110c2e64836b0f7f9bb
fetched_at: '2026-06-28T22:39:09.551500+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 Como limitar
  campos para uso restrito por usuarios na SB1?
type: support-article
updated_at: '2025-03-17T21:20:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30711438211479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Como-limitar-campos-para-uso-restrito-por-usuarios-na-SB1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30711484128023) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Preciso autorizar aos usuario de um setor especifico, a possibilidade de alteração de campos especificos no cadastro de produto, como eu posso configurar isso?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Essa configuração pode ser efetuada via Nivel de acesso dos usuarios, mas uma vez definido o nivel de acesso, o usuario que não tem o nivel, não tera a visualização dos campos nem mesmo em relatórios.

**1- SIGACFG> Acesse Usuários > Senhas > Usuários**. Defina primeiramente o nível de acesso do usuário para o módulo **SIGAEST**, clique na aba "**Restrições de Acesso**" e depois em "**Ambientes**", posicione no módulo **04 SIGAEST** e no final da linha, informe o campo **Nível**, neste exemplo, parametrizado com **5**.

![Screenshot_1A.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30712117384471)

**2- Configure o nível** de acesso do campo, acesse **Base de Dados -> Dicionário -> Base de Dados**. Ao entrar na rotina de Base de Dados, clique em **Dicionário de Dados** e depois na lupa para pesquisar a tabela de **cadastro de produto - SB1**, e posicione no campo desejado, clicando no caderno de edição, usaremos como exemplo o campo **B1\_GRUPO**.

![Screenshot_5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30712146282647)

**3- Aqui iremos usar como exemplo** o campo **B1\_GRUPO** "Grupo", clique em **Campos**, selecione o campo B1\_DESC e clique em **editar**. Ao entrar na configuração do campo **B1\_GRUPO**, clique na aba **Validações**, informe no campo nível o conteúdo **6**, salve as alterações **e atualize a base de dados.**

**![Screenshot_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30712117388951)**

**![Screenshot_7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30712117388951)**

![Screenshot_8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30712117391383)

Para a atualizar, deve estar com ambiente exclusiva para alteração dos dados.

Após estas configurações, apenas usuários com **nível 6 ou maior**, conseguirão ver o campo **B1\_GRUPO**, bem como gerar relatorio com a apresentação do campo.

Duvidas sobre a restrição de niveis de acesso, podera ser tratada juntamente o nosso time Protheus Framework.

***Caso com a configuração de Nivel não seja viavel, devido aos campos não serem acessiveis nem via relatorios***, nesse caso você conseguira contorno apenas com a customização via ponto de entrada conforme sua necessidade especifica, como por exemplo os seguintes:  
<https://tdn.totvs.com/display/public/PROT/PE+MA010FIL+Adiciona+filtro+para+o+registro+do+cadastro+de+produtos>  
<https://tdn.totvs.com/pages/releaseview.action?pageId=894395414>  
  
**Segue demais pontos de entrada disponiveis para a rotina MATA010.**  
<https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010+-+Estoque+-+P12>

**Saiba mais:**

*[Clique aqui para mais informações sobre a MATA010](https://tdn.totvs.com/display/public/PROT/Produtos+-+MATA010#ProdutosMATA010-PastaCadastrais)*

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de envio Messenger para ID de eventos do Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque)*
