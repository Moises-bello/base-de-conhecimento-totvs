---
content_hash: c2612f547c76262167ddf5150e72f80f5123cda23973ac41660a5766faae1293
fetched_at: '2026-06-29T00:12:03.159808+00:00'
page_id: '904065817'
product: rm
source: tdn-rm
title: MIT (Módulo de Inclusão de Tributos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=904065817
version: 76
---

# Conteúdo

**Conteúdonone**

# 1. Visão Geral

A Receita Federal do Brasil (RFB) está promovendo a evolução da DCTFWeb para simplificar e otimizar o cumprimento das obrigações tributárias acessórias. Um dos principais avanços desse processo é a criação do **Módulo de Inclusão de Tributos (MIT)**, que terá um papel fundamental na nova sistemática de declaração fiscal.

O **MIT** substituirá o PGD DCTF e permitirá a inclusão de tributos que ainda não são transmitidos automaticamente via escrituração fiscal digital, como ocorre com o eSocial e o EFD-Reinf. Esse novo módulo abrangerá tributos como IRPJ, CSLL, PIS/PASEP, IPI, COFINS, CIDE, IOF, CONDECINE, CPSS e RET/Pagamento Unificado, centralizando e padronizando a forma de declaração.

A partir de janeiro de 2025, todas as obrigações tributárias atualmente divididas entre DCTF e DCTFWeb serão unificadas na DCTFWeb, eliminando redundâncias e simplificando os processos. Essa mudança segue a Instrução Normativa RFB nº 2.237/2024, que regulamenta a nova sistemática de confissão de débitos tributários.

# 2. Seleção de dados

A geração da rotina do MIT recupera os dados das [Guias](https://tdn.totvs.com/pages/viewpage.action?pageId=431677671) geradas de tributos como IRPJ, CSLL, PIS/PASEP, IPI, COFINS, CIDE, IOF, e RET/Pagamento Unificado, que foram geradas no [Período de Apuração](https://tdn.totvs.com/pages/viewpage.action?pageId=422545773).

Os Tributos CONDECINE, CPSS, IRRF não são considerados na geração do arquivo.

Pessoas jurídicas optantes pelo Simples Nacional que apurarem PIS/PASEP e COFINS sobre importação de bens e serviços também serão considerado na geração do arquivo.

# 3. Como Gerar Rotina do MIT

Para gerar o arquivo da rotina MIT, acesse o menu: **Obrigações Acessórias | Federais | MIT - Módulo de Inclusão de Tributos**. Em seguida, preencha os campos conforme o enquadramento da empresa e execute o processo.

Tela de Geração

# 5. Como realizar a Apuração e gerar a guia DARF

Com a introdução da **EFD-Reinf** (Escrituração Fiscal Digital de Retenções e Informações da Contribuição Previdenciária Substituída), a apuração de tributos federais passou a ser realizada automaticamente pelo governo por meio do portal **DCTFWeb**.

No entanto, desenvolvemos um mecanismo na linha RM que permite às empresas espelharem os valores apurados pelo governo em seus **Lançamentos Financeiros**.

Para mais informações detalhadas, consulte a nossa documentação: [DCTFWeb - Como chegar no valor da DARF a recolher? Será possível unificar as DARF de INSS e IRRF?](https://tdn.totvs.com/pages/viewpage.action?pageId=808478015)

# 4. Layout do JSON Gerado

A rotina do MIT vai gerar um arquivo JSON conforme estrutura abaixo. Ao clicar em cada ponto da estrutura, pode-se verificar os detalhes e regras de geração de cada campo dentro dos grupos.

falseDeclaração Módulo de Inclusão de Tributos (MIT)false500autohiddentrue26231
