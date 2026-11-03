---
content_hash: 19dad4c1559b47826030323bbb4231e293ad5a2fbd835642e4833da9f6253d31
fetched_at: '2026-06-29T00:09:15.396406+00:00'
page_id: '421385369'
product: rm
source: tdn-rm
title: Custo Horário Campos Livres
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385369
version: 2
---

---

Esta pasta se divide em duas subpastas: "1 a 10" e "11 a 20". Ambas possuem 10 dos seguintes campos:

Descrição do Campo / Valor: Estes 20 campos livres globais irão aparecer na planilha de custo horário, clicando com o botão direito do mouse em uma célula da planilha, como "Variáveis Custo Horário / Globais". Estes campos aparecerão nas células com a descrição CLP1...CLP20 e a descrição do campo atribuída por você. Os valores destes campos são cadastrados aqui mesmo neste parâmetro no campo Valor.

Insumos (Descrição): Estes 20 campos livres do insumo irão aparecer na planilha de custo horário, clicando com o botão direito do mouse em uma célula da planilha, como "Variáveis Custo Horário / Insumos". Estes campos aparecerão nas células com a descrição CLI1...CLI20 e a descrição do campo atribuída por você. Desta maneira (botão direito do mouse) será possível incluir também, nas células, os campos código, descrição e quantidade total utilizada dos insumos. Os valores destes campos são cadastrados na Janela de Edição de Insumo, na pasta Custo Horário.

**Passos para Cálculo e Impressão do Custo Horário de Equipamentos:**

1. Inclusão das variáveis globais e das variáveis do insumo através do parâmetro (Menu Opções | Parâmetros | RM Solum | Projetos | Custo Horário).

2. Criação da planilha com estas variáveis e fórmulas para o cálculo dos valores produtivo e improdutivo do equipamento.

3. Indicação da planilha e das células dos valores produtivo e improdutivo do equipamento (Janela de Edição do Insumo).

4. Cálculo dos valores produtivo e improdutivo na Janela de Edição de Insumo (pasta custo horário) ou pela opção "Calcular Custo Horário" (Menu Opções).

5. Impressão das planilhas pela própria janela da planilha ou pela opção "Composição de Custo Horário" (Menu Relatórios).  
    
  **Passos para Cálculo e Impressão do Custo Horário de Mão-de-obra:**

1. Inclusão das variáveis globais e das variáveis do insumo através do parâmetro (Menu Opções | Parâmetros | RM Solum | Projetos | Custo Horário).

2. Criação da planilha com estas variáveis e fórmulas para o cálculo do valor unitário da mão-de-obra.

3. Indicação da planilha e da célula do valor unitário da mão-de-obra (Janela de Edição do Insumo).

4. Cálculo do valor unitário do insumo na Janela de Edição de Insumo (pasta custo horário) ou pela opção "Calcular Custo Horário" (Menu Opções).

5. Impressão das planilhas pela própria janela da planilha ou pela opção "Composição de Custo Horário" (Menu Relatórios).

**Cálculo e Impressão do Custo Horário de Equipamentos:** Indicação da planilha e das células dos valores produtivo e improdutivo do equipamento (Janela de Edição do Insumo). **A partir da versão 12.1.7**, com a migração da arquitetura Delphi para .Net tornou-se necessário modificar a chamada das planilhas dependendo da arquitetura utilizada. **Na nova MDI, só será possível selecionar as planilhas migradas.** **Já no DELPHI, será possível escolher tanto as planilhas migradas quanto as não migradas.**

**Cálculo e Impressão do Custo Horário de Mão-de-obra:** Indicação da planilha e da célula do valor unitário da mão-de-obra (Janela de Edição do Insumo). **A partir da versão 12.1.7**, com a migração da arquitetura Delphi para .Net tornou-se necessário modificar a chamada das planilhas dependendo da arquitetura utilizada. **Na nova MDI, só será possível selecionar as planilhas migradas. Já no DELPHI, será possível escolher tanto as planilhas migradas quanto as não migradas.** OBs.: O Cálculo de custo também poderá ser feito através de um processo definido no menu Insumo, este processo encarrega de calcular o custo de todos os insumos de equipamento e mão de obra que possuem planilha RM vinculada.

---
