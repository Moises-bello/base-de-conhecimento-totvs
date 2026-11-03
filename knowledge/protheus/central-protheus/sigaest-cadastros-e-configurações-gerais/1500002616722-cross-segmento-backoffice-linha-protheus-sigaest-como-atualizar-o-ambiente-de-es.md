---
article_id: 1500002616722
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 6be81f98ef0aed7244c1400a70d34cdeb208751a086f0e3bae95348a44a267ef
fetched_at: '2026-06-28T22:39:08.084505+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como atualizar o ambiente
  de Estoque/Custos/ACD?
type: support-article
updated_at: '2025-03-31T16:50:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002616722-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-atualizar-o-ambiente-de-Estoque-Custos-ACD
---

**Dúvida**Onde obter o pacote (patch) acumulado de fontes do módulo SIGAEST - Estoque/Custos/ACD no *Protheus*?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Para atualizar o seu ambiente de Estoque/Custos com fontes e Stored Procedures, basta aplicar nosso pacote acumulado, antes o pacote continha os fontes apenas do módulo de estoque, porém agora ele possui a atualização do Backoffice, incluindo os demais módulos.

Com isso, você evita a atualização parcial do ambiente gerando erros devido a dependdencia de fontes de outros módulos.

***Pacotes acumulados Backoffice:***

[ATUALIZACAO DE ARQUIVOS FONTES - BACKOFFICE (EXPEDICAO CONTINUA)](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/backoffice_expedicao_continua)

Acima o pacote correspondente a sua release, basta efetuar a aplicação do arquivo correspondente em seu ambiente, e caso utilize Procedures, abaixo um breve tutorial para correta atualização das procedures, bem como uma orientação para aplicação de pacotes via VSCODE.

[TOTVS Developer Studio for VSCode (AdvPL, TLPP e 4GL)](https://marketplace.visualstudio.com/items?itemName=totvs.tds-vscode)

[MP - SIGAEST - Instalação corretas dos Procedures de Estoque-Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018446312-MP-SIGAEST-Instala%C3%A7%C3%A3o-corretas-dos-Procedures-de-Estoque-Custos?source=search)

Observação: Sempre atualizar primeiramente em ambiente de homologação (cópia da produção).

Em caso de sucesso, aplicar a atualização em ambiente de produção.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
