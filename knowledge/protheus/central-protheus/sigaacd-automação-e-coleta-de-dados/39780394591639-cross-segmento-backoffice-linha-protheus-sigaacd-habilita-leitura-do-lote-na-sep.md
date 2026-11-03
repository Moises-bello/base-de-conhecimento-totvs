---
article_id: 39780394591639
category: SIGAACD - Automação e Coleta de Dados
content_hash: 9588a92fbb359776a690f58d129467095fc61c84fbb3ed8e97af590455c1c041
fetched_at: '2026-06-28T22:39:12.736094+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Habilita leitura do
  lote na separação no aplicativo Meu Coletor de Dados
type: support-article
updated_at: '2026-04-16T11:38:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39780394591639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Habilita-leitura-do-lote-na-separa%C3%A7%C3%A3o-no-aplicativo-Meu-Coletor-de-Dados
---

O parâmetro MV\_MCDCLTE controla a habilitação da leitura do lote na separação no aplicativo Meu coletor de dados. Se não configurado, a leitura é habilitada por padrão. Para ajustar, crie o parâmetro como lógico, com descrição adequada, e defina seu valor como .T. para ativar ou .F. para desativar a leitura do lote.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39780386058519) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Como habilitar ou desabilitar a leitura do lote na separação utilizando o aplicativo Meu coletor de dados?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Para controlar a leitura do lote na separação através do aplicativo Meu coletor de dados, é necessária a utilização do parâmetro MV\_MCDCLTE. Quando o usuário realiza o sincronismo no aplicativo, o sistema efetua a leitura deste parâmetro para habilitar ou desabilitar o recurso. Se o ambiente não possuir o parâmetro MV\_MCDCLTE configurado, a leitura do lote será habilitada por padrão.

**Passos**

1. Acesse as configurações do seu ambiente e verifique a existência do parâmetro MV\_MCDCLTE.
2. Caso o parâmetro não exista, realize a criação seguindo as especificações abaixo:

* Parâmetro: MV\_MCDCLTE.
* Tipo: Lógico.
* Descrição: Habilita leitura do lote na separação.
* Descrição 1: Meu coletor de dados.

3. Preencha o conteúdo do parâmetro com o valor booleano adequado à sua operação:

* Informe .T. para habilitar a leitura do lote.
* Informe .F. para desabilitar a leitura do lote.

**Saiba Mais**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
