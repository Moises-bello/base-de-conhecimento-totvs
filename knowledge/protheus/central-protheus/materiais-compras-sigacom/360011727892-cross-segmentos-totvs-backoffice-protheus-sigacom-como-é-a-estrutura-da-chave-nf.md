---
article_id: 360011727892
category: Materiais - Compras (SIGACOM)
content_hash: d92e5859528b50633dc3df9dc617293b6d13b4d2523ccbc6652d452155ff4dfa
fetched_at: '2026-06-28T22:41:07.613739+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é a estrutura
  da Chave NFE para verificação do parâmetro MV_VCHVNFE ?
type: support-article
updated_at: '2022-05-16T22:18:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011727892-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-a-estrutura-da-Chave-NFE-para-verifica%C3%A7%C3%A3o-do-par%C3%A2metro-MV-VCHVNFE
---

**Dúvida**Como é a estrutura da Chave NFE para verificação do parâmetro MV\_VCHVNFE ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

- MV\_VCHVNFE - Este parâmetro valida se a chave confere com a nota que está sendo digitada para as espécies CTE e SPED com formulário próprio = Não.

Ele não confere se a chave é completamente válida junto à SEFAZ.

Apenas verifica se o CNPJ constante na chave bate com o CNPJ do fornecedor informado na nota e se o número e a série constante na chave batem com o número e série digitados na nota.

Caso as informações não baterem será informada a mensagem "Chave NFE informada não confere com a nota que está sendo digitada."

O sistema confere a chave NFE com anota que está sendo digitada e para verificação do usuário segue abaixo o esquema da estrutura da chave de acesso da nota fiscal eletrônica e o conceito de cada bloco de numeração:

![estrutura_chave_nfe.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360008593731/estrutura_chave_nfe.JPG)

O primeiro campo UF, possui a lista no menu superior da página na aba GUIA nas tabelas Globais.

O campo MOD. Se refere ao modelo do documento que a planilha também está disponível na mesma aba do site. O modelo 55 se refere a NF-e.

O campo Código Numérico é de livre utilização pelas empresas. Existem empresas que optam por utilizar uma sequência numérica aleatória e randômica. Já algumas empresas optam por utilizar o número da fatura ou um número sequencial.

O campo DV é o dígito verificador da chave de acesso onde é possível validar a sequência logarítmica da chave.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
