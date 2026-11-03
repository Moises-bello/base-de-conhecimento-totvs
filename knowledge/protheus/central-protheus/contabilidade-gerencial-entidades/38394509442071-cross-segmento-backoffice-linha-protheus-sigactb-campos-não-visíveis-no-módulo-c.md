---
article_id: 38394509442071
category: Contabilidade Gerencial - Entidades
content_hash: 7ffd2aabdb9b36824c0b2ab4b875da47b0b6adc424b3c932feca2daee2864f52
fetched_at: '2026-06-28T22:40:49.744713+00:00'
product: protheus
section_id: 1500001537661
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - Campos não visíveis
  no Módulo Contábil
type: support-article
updated_at: '2026-02-19T20:24:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38394509442071-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Campos-n%C3%A3o-vis%C3%ADveis-no-M%C3%B3dulo-Cont%C3%A1bil
---

Alguns campos das tabelas CT1, CT2, CT5, CTK e CV3 do TOTVS Protheus não aparecem por padrão para otimizar a performance e interface, mantendo visíveis apenas campos essenciais. É possível habilitá-los via Dicionário de Dados ou Otimizador de Telas, conforme a necessidade do usuário e configuração do ambiente.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38394509436311) Tempo aproximado para leitura: 00:05:00 min**  
  
**Dúvida**  
Por que alguns campos das tabelas **CT1**, **CT2**, **CT5**, **CTK** e **CV3** não são exibidos nas rotinas contábeis ou como habilitar campos que não aparecem por padrão?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - A partir da versão 12.1.2210

**Solução**  
Como parte da evolução do produto e melhoria da usabilidade, campos não obrigatórios das tabelas **CT1 (Plano de Contas)**, **CT2 (Lançamentos Contábeis)**, **CT5 (Lançamentos Padronizados)**, **CTK (Arquivo de Contra-Prova)** e **CV3 (Rastreabilidade de Lançamentos)** passaram por uma reavaliação técnica.

O objetivo desta alteração foi otimizar a performance das rotinas, reduzindo o custo de processamento e simplificando a interface, mantendo visíveis apenas os campos essenciais.

Existem duas formas de gerenciar essa visibilidade:

1. **Via Dicionário de Dados (SIGACFG):** Indicado para bases novas onde o campo consta como "**Não Usado**".
2. **Via Otimizador de Telas:** Indicado para bases onde o campo já consta como "**Usado**" ou para criar *templates* dinâmicos de exibição, desde que a propriedade **"Altera Uso"** do campo esteja definida como **"Sim"**.

As principais rotinas impactadas são:

* Plano de Contas (CTBA020);
* Lançamentos Contábeis (CTBA101 / CTBA102);
* Lançamentos Padronizados (CTBA080).

  ---

**Opção 1: Gerenciamento via Otimizador de Telas**  
Utilize este método para criar *templates* ou gerenciar campos que já estão como "**Usado**", mas ocultos por regra de interface:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Usuário/Senha > Otimizador de Tela**;
3. Crie ou edite um *template* para a rotina desejada;
4. Certifique-se de que o campo desejado possui a propriedade **"Altera Uso" = Sim** no dicionário de dados;
5. No Otimizador, configure a visibilidade do campo conforme a necessidade da regra de negócio;
6. Salve e aplique o *template* aos grupos ou usuários correspondentes.

**Passos**  
**Opção 2: Habilitar via Configurador (SIGACFG)**

Utilize este método se o campo não estiver marcado como "**Usado**" no dicionário:

1. Acesse o módulo **Configurador (SIGACFG)**;
2. Vá em **Base de Dados > Dicionário > Base de Dados**;
3. Pesquise pela tabela desejada (ex: **CT2**) e clique no ícone de **Edição (Lápis)**;
4. Localize o campo desejado na aba **Campos** e clique em **Alterar**;
5. Na aba **Uso**, marque a *checkbox* **Usado**;
6. Confirme a alteração e clique no ícone do **Disquete** para atualizar o dicionário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38394707763479)

---

**Saiba Mais**  
[Campos não usados CTB a partir da release 12.1.2210](https://tdn.totvs.com/pages/releaseview.action?pageId=842697736)  
[Campos Não Usados - CTB](https://tdn.totvs.com/pages/releaseview.action?pageId=842300955)
