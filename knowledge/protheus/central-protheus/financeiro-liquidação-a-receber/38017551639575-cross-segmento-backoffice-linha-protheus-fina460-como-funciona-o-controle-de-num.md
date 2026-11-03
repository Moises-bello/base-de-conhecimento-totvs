---
article_id: 38017551639575
category: Financeiro - Liquidação a Receber
content_hash: 15cda75fd282261c1560e2e1fe9053a97318d738d8c578addc30fc8c8dfa4e5b
fetched_at: '2026-06-28T22:37:42.239993+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA460 - Como funciona o controle
  de numeração dos títulos gerados na rotina de liquidação
type: support-article
updated_at: '2026-02-04T19:27:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38017551639575-Cross-Segmento-Backoffice-Linha-Protheus-FINA460-Como-funciona-o-controle-de-numera%C3%A7%C3%A3o-dos-t%C3%ADtulos-gerados-na-rotina-de-liquida%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38017551624855) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como funciona o controle de numeração dos títulos gerados na rotina de Liquidação (FINA460) do Protheus?  
  
**Solução**  
O sistema controla o sequencial de numeração da liquidação utilizando o parâmetro **MV\_NUMLIQ**. O valor definido nesse parâmetro será gravado no campo **E1\_NUMLIQ** (Título a Receber) ou **E2\_NUMLIQ** (Título a Pagar) do título correspondente.

![mv_numliq.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38022863464727)

Quanto à numeração do **novo título** gerado pela liquidação (campo Número), o Protheus segue a lógica do maior número já cadastrado na base de dados (Tabelas SE1 ou SE2), considerando o **prefixo** e o **tipo** informados.

**Lógica de Numeração:**

1. **Validação por Prefixo:** O sistema busca o maior número existente no campo **E1\_NUM** ou **E2\_NUM** que possua exatamente o mesmo prefixo informado rotina.

   * *Exemplo:* Se o prefixo for "FAT" e o maior número encontrado for "000000001", o próximo sugerido será "000000002".
2. **Alteração de Prefixo/Tipo:** Caso o usuário altere o prefixo ou o tipo durante o processo de liquidação, o sistema refaz a busca no banco de dados para encontrar o maior sequencial correspondente à nova combinação informada. Por esse motivo, ao trocar o tipo, o número anteriormente preenchido pode ser alterado automaticamente para o próximo número livre daquela nova sequência.
3. **Inexistência de Registro:** Se não houver nenhum título cadastrado com o prefixo e tipo informados, o sistema iniciará a numeração a partir de "1", completando com zeros à esquerda de acordo com o tamanho do campo ex: "000000001".

Exemplo do comportamento do sistema, considerando a existência prévia de uma liquidação do tipo FA e prefixo FAT, com numeração 000000001:

![Adobe Express - FUNCIONAMENTO-NUMERO-FINA460.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/38022857381271)

**Saiba Mais**

[FINA460 - Liquidação a receber - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=545236275)
