---
article_id: 4403608828567
category: SIGAEST - LEGAIS
content_hash: c294e51fe2f38c965a5bd14204184ac7d802ddb6369912f221c3189af2a92ed9
fetched_at: '2026-06-28T22:38:51.795909+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Movimento Interno
  e Inventário não gera nenhum registro no Bloco K
type: support-article
updated_at: '2021-07-02T18:14:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403608828567-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Movimento-Interno-e-Invent%C3%A1rio-n%C3%A3o-gera-nenhum-registro-no-Bloco-K
---

**Dúvida**

Tenho cenários em que faço movimentos internos de requisição e devolução mas não gera dados nos registros K220 e K280 do Sped Fiscal. O que fazer para que gere?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

## **Movimento Interno e Inventário no Protheus**

## **Gera ou Não registro K220/K280 no SPED.**

Para o bloco K do SPED Fiscal, somente são enviados os lançamentos de forma automática quando o movimento está vinculado em ordem de produção (podendo eventualmente gerar registros **[K230](https://tdn.totvs.com/display/public/PROT/Registro+K230%3A+Itens+Produzidos)**/**[K235](https://tdn.totvs.com/pages/releaseview.action?pageId=259560161)**). Em caso de apontamentos de ganho ou perda de saldo for informado no sistema via inventário ou movimentação interna, então não é levado para nenhum registro do bloco K. Conforme perguntas e respostas do bloco K:

*"**As perdas de mercadorias ou insumos em decorrência de obsolescência ou, ainda, em decorrência de caso fortuito, deverão ser registradas no registro K220?** Não. Estes tipos de perdas deverão ser registrados no bloco C, por meio de documento fiscal."*

*"**Como registrar perdas de estoque para Bloco K?** Os Estados determinam em suas legislações internas os procedimentos para regularizar a situação de perdas. Como por exemplo, temos o Estado de São Paulo, que através do Decreto nº 61.720/2015 exige a emissão da nota fiscal de perda que deverá: a) indicar, no campo "Código Fiscal de Operações e Prestações - CFOP", o CFOP 5.927; b) ser emitida sem destaque do valor do imposto."*

Atualmente, se a movimentação interna não estiver com o campo OP preenchido, a movimentação não será registrada em nenhum registro do Bloco K. Em caso de ajuste, validar com o fisco responsável da empresa, pois apenas ajustes registrados por meio de documento fiscal são enviados no arquivo fiscal SPED. Em caso de maiores dúvidas, basta realizar uma consulta ao "fale conosco" da Fazenda responsável pela Unidade de Federação para que possa repassar maiores informações para esta situação.

**Saiba mais:**

*[Condições e Exemplo Prático da geração do registro K220 no Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=259560142)*

*[Condições e Exemplo Prático da geração do registro K270 no Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=259560564)*

*[Condições e Exemplo Prático da geração do registro K280 no Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=259560569)*

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
