---
article_id: 41297339022359
category: SIGAEST - CUSTOS
content_hash: 9727285c7c9e56d3d50502d9fa575fcd028d2aa570d147d7ece282f44fac8770
fetched_at: '2026-06-28T22:39:02.353316+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Sem licença ao modulo
  SIGACTB como fechar o estoque?
type: support-article
updated_at: '2026-06-17T18:06:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41297339022359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Sem-licen%C3%A7a-ao-modulo-SIGACTB-como-fechar-o-estoque
---

Ao fechar o estoque sem licença do módulo contábil no TOTVS Protheus, deve-se configurar o parâmetro "Gerar lançamento contábil" na opção 3, evitando a contabilização e as validações do calendário contábil durante o processo de fechamento.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41297327992087) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**

Ao efetuar o fechamento de estoque, são apresentadas validações do calendário contábil, porém o ambiente não possui licença para o módulo contábil. Como realizar o fechamento de estoque neste cenário?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Se não há licenças para o uso do processo de amarração com o módulo Contábil, a contabilização não poderá ser exercida durante a jornada de fechamento ou custo médio, com a "contabilização ativa". Para contornar a validação e prosseguir com o processo, é necessário ajustar a parametrização da rotina para não gerar lançamentos contabeis, assim sera permitido o processo de custeio e virada de saldos.

1. Acesse a rotina de "Acompanha Custos."
2. Clique no menu "Configurar Parâmetros".
3. Localize o pergunte "Gerar lançamento contábil" e configure com a opção "3" (Não e mantém lançamentos existentes).
4. Confirme os parâmetros e prossiga com o fechamento do estoque.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41297339008919)

**Saiba mais**:

[*Clique aqui e veja mais artigos sobre a Nova Jornada de Fechamento no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/5367899706647-ACOMPANHA-CUSTOS-JORNADA-DE-FECHAMENTO-NOVO-)
