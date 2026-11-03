---
article_id: 5570613598615
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 1b7d21a95d0bbb33483214ff77efa9ab0404132703a580cb472d67a4655093e6
fetched_at: '2026-06-28T22:39:08.042301+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Aumento de tamanho
  do campo Descrição do Produto B1_DESC
type: support-article
updated_at: '2026-03-03T11:58:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5570613598615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Aumento-de-tamanho-do-campo-Descri%C3%A7%C3%A3o-do-Produto-B1-DESC
---

É possível aumentar o campo B1\_DESC (Descrição do Produto) no Protheus para até 254 caracteres, porém, valores acima de 60 podem causar erros na transmissão à SEFAZ e truncamento de relatórios. Recomenda-se avaliar impactos com a equipe fiscal e realizar alterações com acompanhamento técnico especializado.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34321458404119)** **Tempo aproximado para leitura:****00:02:00 min**

**Dúvida**

Eu posso aumentar o tamanho do campo **Descrição do Produto (B1\_DESC)**? Quais impactos causam?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Estoque/Custos- todas as versões  
  
**Solução**

Os campos de descrição/nome (nome do cliente, nome do contato, etc.) no Protheus são, geralmente, do tipo “**Caracter**”, esses campos tem a possibilidade de aumento para **até 254 caracteres,**então sim, ele pode ter seu tamanho alterado.

**O que ocorre quando realizamos o aumento de um campo descrição?**

A partir do release 12.1.2410 o campo B1\_DESC **passa a fazer parte de um grupo de Campos,** que é o de **Código 171 - Descrição do Produto**.

![grupo b1_desc .jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/34321487988887)

**Como saber quais as tabelas relacionadas de maneira geral?**

**1.** Verifique se a informação que deseja alterar possui um Grupo de Campos no configurador, ao alterar o Grupo de Campos, todos os campos que fazem parte do grupo serão alterados,

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34321487992087)

**2.** Você pode acessar a **tabela SX9** do sistema, nela constam os relacionamentos entre as tabelas do sistema:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5574317215639)

**3**. Após atualizar o tamanho do Grupo de Campos 171 - Descrição do Produto, desinstale e instale todos os Procedures do ambiente:

[**Backoffice (Linha Protheus) - SIGAEST - Como instalar a nova gestão de procedures e as procedures?**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8388802894615-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-instalar-a-nova-gest%C3%A3o-de-procedures-e-as-procedures)

[**Backoffice (Linha Protheus) - SIGAEST - Desinstalando pacotes de Stored Procedures**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28150699874071-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Desinstalando-pacotes-de-Stored-Procedures)

**Impactos mapeados oriundos do aumento da Descrição do Produto:**

Segundo o Manual de Orientação Contribuinte v 6.00 - Minuta a tag <cProd> deve ter o tamanho entre 1-60  
  
Portanto, se for alterado o campo B1\_DESC acima de 60 poderá gerar erro na transmissão a SEFAZ ou a descrição pode sair cortada, e truncamento de relatórios que validam a descrição do produto. É recomendável avaliar com a equipe Fiscal da empresa ou mesmo com a equipe Fiscal do Protheus para duvidas quanto às tags <cProd> do Manual de Orientação Contribuinte v 6.00

**Importante:** O Protheus já vem com o tamanho de campos padrões, caso necessite alteração, é aconselhável a manutenção, com um analista consultor in loco, para avaliação dos possíveis impactos no campo em questão.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
