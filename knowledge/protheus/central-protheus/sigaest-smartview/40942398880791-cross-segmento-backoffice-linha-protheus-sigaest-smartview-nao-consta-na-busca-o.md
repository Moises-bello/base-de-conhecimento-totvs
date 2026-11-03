---
article_id: 40942398880791
category: SIGAEST - SMARTVIEW
content_hash: 93c2cddb17076c57e9389baa2625a1365bd289b268929dca37c2d3a4bd39a282
fetched_at: '2026-06-28T22:38:47.109780+00:00'
product: protheus
section_id: 16108365627287
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Smartview nao consta
  na busca ou menu do modulo
type: support-article
updated_at: '2026-06-17T18:35:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40942398880791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Smartview-nao-consta-na-busca-ou-menu-do-modulo
---

Para adicionar um relatório Smart View no Protheus, primeiro verifique se o fonte está compilado no repositório RPO. Se não, atualize o pacote Backoffice. Com o fonte compilado, inclua o relatório manualmente via Configurador (SIGACFG) ou atualize o menu padrão do módulo para adicionar automaticamente os relatórios disponíveis.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40942415617047) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Como adicionar um relatório do Smart View ao menu do módulo desejado no Protheus?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.2310

**Solução**

Para disponibilizar um relatório do Smart View no Protheus, é necessário garantir que o fonte correspondente esteja presente no repositório RPO. Com o fonte devidamente compilado, a disponibilização da rotina pode ser feita manualmente via Configurador (SIGACFG) ou por meio da atualização do menu padrão do módulo.

**Passos**

1. Acesse o Inspetor de Objetos e valide se o fonte do relatório Smart View desejado já está compilado no seu repositório.
2. Caso não possua o fonte, realize o download e a atualização do pacote Backoffice mais recente disponível no Portal do Cliente. [Acumulado BackOffice](https://tdn.totvs.com/x/2hgdHw)
3. Com o fonte compilado no repositório, escolha uma das formas abaixo para inclusão no menu:

   * **Inclusão Manual:** Acesse o módulo Configurador (SIGACFG) e adicione o recurso manualmente ao menu.

     [Framework - Cross - Smart View - Incluir recurso no menu do Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27279374595095-Framework-Cross-Smart-View-Incluir-recurso-no-menu-do-Protheus)
   * **Atualização do Menu Padrão:** Caso o seu menu seja 100% padrão, baixe o arquivo de menu atualizado do módulo correspondente à sua release e efetue a atualização no banco de dados. Isso adicionará automaticamente todos os relatórios disponíveis.

     [Framework - Linha Protheus - Atualização de menus que estão no Banco de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026178872-Framework-Linha-Protheus-Atualiza%C3%A7%C3%A3o-de-menus-que-est%C3%A3o-no-Banco-de-Dados)

**Saiba Mais**

[Como configurar o SmartView](https://tdn.totvs.com/x/8WTCMQ)

[Clique aqui e veja mais artigos sobre Relatórios SmartView do Estoque Custos](https://tdn.totvs.com/x/pwKQLg)
