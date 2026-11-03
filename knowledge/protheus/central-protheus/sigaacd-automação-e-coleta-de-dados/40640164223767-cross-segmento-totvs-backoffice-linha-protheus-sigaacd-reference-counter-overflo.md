---
article_id: 40640164223767
category: SIGAACD - Automação e Coleta de Dados
content_hash: db79960bf27b57ad1a2bcbacdc2168d75b719bc3ebcfa4d20370e94d67811934
fetched_at: '2026-06-28T22:39:13.922880+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD - Reference counter
  overflow (over 32700) no Monitor ACDA030
type: support-article
updated_at: '2026-05-21T18:52:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40640164223767-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAACD-Reference-counter-overflow-over-32700-no-Monitor-ACDA030
---

O erro "Reference counter overflow" no monitor da rotina ACDA030 ocorre ao carregar mais de 32 mil itens simultaneamente. A solução envolve aplicar um patch que permite filtrar por "Produto De" e "Produto Até", evitando sobrecarga. Após o patch, é necessário executar o compatibilizador para atualizar o dicionário de dados e configurar manualmente os parâmetros no módulo SIGACFG.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40640153013655) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**

Ao acessar o monitor da rotina ACDA030 em cenários onde existam mais de 32 mil itens, o sistema apresenta a seguinte inconsistência: Reference counter overflow (over 32700) on tClassInstance::addRef(). Como resolver?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD - Versões 12.1.2410 e 12.1.2510.

**Solução** 

O erro ocorre devido ao excesso de registros carregados simultaneamente. Foi realizado um ajuste na rotina para permitir a utilização dos filtros de "Produto De" e "Produto Até", o que evita a sobrecarga no monitor e a respectiva inconsistência. Como esta implementação envolve ajustes no dicionário de dados, é necessário aplicar o patch de correção e executar o compatibilizador.

**Passos**

1. Baixe e aplique o patch de correção correspondente à sua versão atual:

* 12.1.2410: <https://r.totvs.io/p/1235206>
* 12.1.2510: <https://r.totvs.io/p/1235209>

  **OBS:** Sempre realizar o backup, ou testar antes em ambiente de homologação.

2. Após a aplicação do patch, execute o compatibilizador UPDDISTR com o pacote diferencial (SDF) para atualizar o dicionário.
3. Para criar os parâmetros manualmente (caso opte por não aguardar o processamento via pacote), acesse o módulo SIGACFG: Base de Dados > Dicionário > Base de Dados.
4. Localize o grupo de perguntas ACD032.
5. Insira duas novas perguntas referentes a "Produto De" e "Produto Até".
6. Na configuração do tamanho destas perguntas, utilize a referência de tamanho do campo B1\_COD.
7. Confirme a alteração para que os ajustes sejam salvos na tabela SX1.
8. Acesse novamente a rotina (módulo SIGAEST: Atualizações > ACD > Inventário > Mestre > Outras Ações > Monitor).
9. O pergunte será exibido em tela; ao informar o intervalo de produtos, os dados serão carregados conforme o filtro aplicado.

**Saiba Mais**

Documentação Técnica TDN - Lentidão no Monitor ACDA030:

<https://tdn.totvs.com/pages/releaseview.action?pageId=1034804007> 

[*Clique aqui e veja artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
