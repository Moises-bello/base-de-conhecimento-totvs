---
article_id: 1500000831201
category: Escrita Fiscal - Impostos - ICMS - Apuração e Livros Fiscais - Livro - Regime
  de Apuração
content_hash: bb3eeb37197a6b3e274636488c9d2a6799d5fff7dd10852134a68a86074de540
fetched_at: '2026-06-28T22:39:22.218995+00:00'
product: protheus
section_id: 1500001538681
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Refazer apuração de
  ICMS após baixar o título no Financeiro
type: support-article
updated_at: '2021-07-15T18:05:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000831201-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Refazer-apura%C3%A7%C3%A3o-de-ICMS-ap%C3%B3s-baixar-o-t%C3%ADtulo-no-Financeiro
---

**Dúvida**

É possível refazer a apuração de ICMS mesmo após ter o título baixado no financeiro?

**Ambiente**

Microsiga Protheus- Livros Fiscais – A partir da versão 11.80  
  
**Solução**

Através da configuração do parâmetro MV\_REFAPUR = .T. é possível refazer a apuração de ICMS (MATA953), mesmo após ter baixado o título do imposto na rotina de Contas a Pagar.

Detalhes do parâmetro:  
Nome: MV\_REFAPUR  
Tipo: Lógico  
Conteúdo: T ou F

Para realizar este procedimento, é necessário que a pergunta “Gera Título” nos parâmetros da apuração esteja igual a NÃO.

Após isso, o sistema permitirá refazer e gravar novas informações na apuração, porém o sistema não gerará um novo título, visto que foi colocado não nessa pergunta, mantendo o título já baixado no financeiro (ele não será excluído). Com relação à pergunta Gera Guia, se informado SIM, esta será gerada normalmente, podendo causar duplicidade na tabela SF6 (Guias de Recolhimento).

A configuração deste parâmetro é de total responsabilidade do cliente, visto que seu padrão é .F. (False) para impedir que seja refeita a apuração após baixa do título, uma vez que após alterados as informações no MATA953 (Apuração de ICMS) isto refletirá diretamente nos livros e demais arquivos magnéticos que leiam estes dados (SPED, GIA, etc).

Informações adicionais:

<https://tdn.totvs.com/pages/releaseview.action?pageId=165283478>
