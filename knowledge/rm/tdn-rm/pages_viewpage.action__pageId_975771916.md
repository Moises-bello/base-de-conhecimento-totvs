---
content_hash: 37ac9caf0b74851bf0e6df6b2926904a8591aecb49ee4fbedea66b44d0a1b6d9
fetched_at: '2026-06-29T00:12:15.295148+00:00'
page_id: '975771916'
product: rm
source: tdn-rm
title: Item de Cobrança - Anexo - Tabela Opcional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=975771916
version: 5
---

## **Contexto**

---

Atualmente, o sistema utiliza exclusivamente o parâmetro de integração financeira definido no empreendimento para gerar os lançamentos do fechamento de condomínio. Com o anexo das tabelas opcionais, será possível incorporar tabelas opcionais específicas, proporcionando uma granularidade maior no controle e na apuração dos lançamentos, atendendo a necessidades contábeis mais detalhadas por itens de cobrança.

## **Introdução**

---

Esse recurso permitirá que, no momento do fechamento de condomínio, os lançamentos sejam gerados considerando as tabelas opcionais definidas para cada **coligada**, garantindo maior aderência às regras e necessidades contábeis de cada operação.

## **Procedimento de Utilização**

---

1. **Cadastro**

   * No anexo de tabelas opcionais dos itens de cobrança, o usuário seleciona a coligada e anexa as tabelas opcionais desejadas.
   * É Importante dar a permissão correta ao anexo *Tabelas Opcionais* no Perfil de Segurança do Usuário, nas permissões do módulo de Condomínio.
   * O cadastro das tabelas opcionais segue as permissões do financeiro. Se serão obrigatórias ou não, as permissões são as mesmas do módulo.

## **Restrições Importantes**

---

1. **Escopo Global do Item de Cobrança**

   * O item de cobrança é multi-coligada, sendo assim, a tabela opcional utilizada deve estar corretamente vinculada à coligada que gerencia o fechamento do condomínio, ou seja, a coligada do empreendimento.
   * Não será permitido cadastrar mais de um conjunto de tabelas opcionais para a mesma coligada.
2. **Restrições por Agrupamento**
   * Só serão consideradas as tabelas opcionais dos itens de cobrança, quando a geração de lançamentos for agrupada por Item de Cobrança. Para todos os outros agrupamentos, o sistema continuará se valendo das tabelas opcionais dos parâmetros de integração financeira do empreendimento.
