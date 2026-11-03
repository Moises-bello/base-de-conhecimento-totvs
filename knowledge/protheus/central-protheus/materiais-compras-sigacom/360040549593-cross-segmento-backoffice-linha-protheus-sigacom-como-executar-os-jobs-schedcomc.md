---
article_id: 360040549593
category: Materiais - Compras (SIGACOM)
content_hash: 40a5582bc3d4f7045dbd008a73c1cd0479ae2ed479ad0133f7438d5b897080cf
fetched_at: '2026-06-28T22:41:10.576149+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como executar os Jobs
  Schedcomcol e Colautoread manualmente?
type: support-article
updated_at: '2024-10-07T18:47:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040549593-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-executar-os-Jobs-Schedcomcol-e-Colautoread-manualmente
---

**Dúvida**

Como executar os Jobs Schedcomcol e Colautoread manualmente?

Confira nosso tutorial no YouTube para configurar a integração do XML.

[How To | MP - SIGACOM -Configuração Menus COLAUTOREAD e SCHEDCOMCOL](https://www.youtube.com/watch?v=k2_lw7KYSpI)

**Ambiente**Protheus – Compras – A partir da versão 12

**Solução**

Por padrão, os jobs **COLAUTOREAD** e **SCHEDCOMCOL**  são executados automaticamente pelos agendamentos do Schedule, porém, caso esses agendamentos não estejam funcionando corretamente (Exemplo, o xml não é movido da pasta INN para LIDOS) é possivel executa-los de forma manual para tentar identificar possiveis erros:

**Siga os procedimentos conforme o passo a passo abaixo :**

 No Configurador, acesse **Ambiente > Cadastros > Menus**.

  3.1 No rodapé, clique em **Todos os menus** para desmarcar todas as caixas e marque apenas o **Módulo de Compras**. Clique em **OK**.

  3.2 Na coluna do meio, clique em **Adicionar**.

  3.3 No lado direito, selecione a pasta e a subpasta onde deseja adicionar o item de menu, e clique em **Novo item** para adicionar o menu **COLAUTOREAD**.

  3.4 Repita os mesmos passos para incluir o **SCHEDCOMCOL**.

  3.5 Após adicionar os itens Insira o nome do módulo e clique em "Gerar"

Detalhes sobre a Configuração do Menu [Clique Aqui!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035446693-Framework-Linha-Protheus-Como-incluir-e-utilizar-menus-customizados-com-o-dicion%C3%A1rio-no-banco-de-dados)

4. Pause ambos os serviços no Schedule, em seguida execute manualmente as rotinas **COLAUTOREAD** e **SCHEDCOMCOL**e verifique se o arquivo é atualizado da pasta **IN** para **LIDOS:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360053976133)**

OBSERVAÇÃO : Ao realizar o processo manual das funções lembre-se de primeiramente executar**a COLAUTOREAD e depois a SCHEDCOMCOL.** Sendo que a rotina **SCHEDCOMCOL** deverá ser executada logado na filial onde o XML deverá ser integrado/importado.

Se mesmo dessa forma o arquivo não for atualizado para a pasta LIDOS, execute teste com o pacote acumulado conforme a versão que consta em seu ambiente:

[Pacotes de Atualização - Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

***Saiba Mais :***

[Integração Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7557934491159-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-Importador-XML-x-TOTVS-Transmite)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
