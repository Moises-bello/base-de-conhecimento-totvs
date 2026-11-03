---
article_id: 29912740330391
category: Integrações - Feedz
content_hash: 3ab34b03085370c1e1d603be672f575429e2532fffddc53290f474115087baf6
fetched_at: '2026-06-28T22:46:41.440762+00:00'
product: rm
section_id: 28212337440791
source: central-rm
title: RH - RM - FOP - Integração RM Folha de Pagamento x Feedz - Como parametrizar
  a integração do RM com a FEEDZ
type: support-article
updated_at: '2025-02-12T13:55:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29912740330391-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-parametrizar-a-integra%C3%A7%C3%A3o-do-RM-com-a-FEEDZ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29912755453079) Tempo aproximado para leitura: **00:05:45min****Dúvida**Como parametrizar a integração do RM com a FEEDZ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2310  
  
**Solução**Para realizar a parametrização da integração RM x Feedz, realize os seguintes passos:  
  
1**.** Acesse o portal da Feedz e vá para **Configurações** > **Integrações**. No campo **Chave de Integração (API 2.0)**, você encontrará o valor do token que deve ser inserido no RM.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29912755455127)

2. Logo abaixo, em **Integrações TOTVS**, marque a opção **Ativar Integração ERP** e no campo **Sistema** preencha com "**RM**". No campo "**Domínio padrão de e-mail fake",** informe o domínio interno da empresa.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29912755457431)

**Observação 1**: A opção **Feedz Recrutamento & Seleção (ATS)** não faz parte desta integração, os campos **Client ID e Client Secret** não precisam ser preenchidos.

**Observação 2**: Caso não apareça as configurações **Integração de ERP TOTVS**, é necessário acionar o time de CS da Feedz para solicitar a liberação da integração.

3. No RM, acesse o módulo **Serviços Globais** | **Segurança** | **Perfis.** Selecione o sistema **Folha de pagamento** e edite o perfil do usuário utilizado. Na aba **Acesso a menus,** permita o acesso ao item **[01.05.01] - Integração Performance e Metas / Feedz.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29913716670743)

4. Após conceder a permissão, acesse o módulo **Folha de pagamento** > **Configurações** > **Parametrizador**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29913716673687)

4.1. Expanda a opção "**Integrações**" e selecione "**TOTVS RH Performance e Metas / Feedz**":  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29913735401111)

4.2. Na tela de parametrização, em "Ativar integração com" selecione **Feedz**. Em "Tipo de Ambiente" escolha **Produção** ou **DEV** homologação. Abaixo em Informações do Ambiente, cole o token da **Chave de Integração (API 2.0)** gerado na Feedz.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29913716678551)

**Configurações opcionais:**

* **Utiliza token por filial:** Com esse parâmetro será possível fazer com que o RM transmita as informações de funcionário conforme sua filial cadastrada para o ambiente vinculado da feedz correspondente (conforme Token indicado), marcando o parâmetro, o sistema irá habilitar a Aba **Token X Filiais** para possibilitar as vinculações.  
  ![](https://tdn.totvs.com/download/attachments/868233301/image-2024-9-30_15-46-40.png?version=1&modificationDate=1727722019712&api=v2)
* **Concatenar Descrição do Cargo (Descrição + Código):** Ao selecionar esse parâmetro, o sistema irá combinar a descrição da função com o seu código correspondente.

  Por exemplo, se o código da função for "**0001**" e a descrição for "**Gerente**", após ativar esse parâmetro, o sistema enviará para a Feedz a informação "**Gerente 0001**".

  Importante ressaltar que, caso o parâmetro não esteja marcado e houver Cargos com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.
* **Concatenar Descrição do Departamento (Descrição + Código):** Ao selecionar esse parâmetro, o sistema incluirá tanto a descrição da seção quanto o seu código correspondente.

  Por exemplo, se o código da seção for "**01.01**" e a descrição for "**Administrativa**", ao ativar esse parâmetro, o sistema enviará para a Feedz a informação "**Administrativa 01.01**".

  Importante ressaltar que, caso o parâmetro não esteja marcado e houver Departamentos com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.
* **Concatenar Descrição da Unidade (Descrição + Código):** Ao selecionar esse parâmetro, o sistema incluirá tanto a descrição (GFILIAL.NOME) da filial quanto o seu código correspondente.

  Por exemplo, se o código da filial "**1**" e a descrição for "**TOTVS** **- Filial Belo Horizonte**", ao ativar esse parâmetro, o sistema enviará para a Feedz a informação "**TOTVS - Filial Belo Horizonte1**".

  Importante ressaltar que, caso o parâmetro não esteja marcado e houver Filiais com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.
* **Concatenação de Coligada:** Ao selecionar esse parâmetro, o sistema incluirá o código da Coligada (GCOLIGADA.CODCOLIGADA) no envio da filial.

  Por exemplo 1: Concatenar Descrição da Unidade (Descrição + Código) marcado, se o código da coligada "**8**", código da filial "**1**" e a descrição for **"TOTVS - Filial Belo Horizonte"**, ao ativar esse parâmetro, o sistema enviará para a Feedz a informação **"TOTVS - Filial Belo Horizonte18"**.

  Por exemplo 2: Concatenar Descrição da Unidade (Descrição + Código) desmarcado, se o código da coligada "**8**" e a descrição for "**TOTVS - Filial Belo Horizonte**", ao ativar esse parâmetro, o sistema enviará para a Feedz a informação "**TOTVS - Filial Belo Horizonte8**".

  Importante ressaltar que, caso o parâmetro não esteja marcado e houver Filiais com a mesma descrição, sistema irá sobrescrever as informações a cada coligada enviada. Isso acontece devido à descrição ser um elemento-chave na Feedz.
* **Considerar Nome Fantasia para a Unidade:** Ao selecionar esse parâmetro, o sistema incluirá a descrição (GFILIAL.NOMEFANTASIA) no envio da filial.

  Importante ressaltar que, caso o parâmetro não esteja marcado e houver Filiais com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.

Após realizar esta parametrização da integração, para saber como realizar o envio de funcionários do RM para a Feedz, [clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29903246172695-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-realizar-o-envio-de-colaboradores-e-associa%C3%A7%C3%A3o-de-l%C3%ADderes)

**Saiba Mais:**

**[TDN - Integração RM x FEEDZ](https://tdn.totvs.com.br/pages/releaseview.action?pageId=785614408)**

**[Integração RM Folha de Pagamento x Feedz - Como realizar o envio de colaboradores e associação de líderes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29903246172695-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Como-realizar-o-envio-de-colaboradores-e-associa%C3%A7%C3%A3o-de-l%C3%ADderes)**

**[Integração RM Folha de Pagamento x Feedz - Erro na integração com a Feedz código XXXX](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29909362246039-RH-RM-FOP-Integra%C3%A7%C3%A3o-RM-Folha-de-Pagamento-x-Feedz-Erro-na-integra%C3%A7%C3%A3o-com-a-Feedz-c%C3%B3digo-XXXX)**
