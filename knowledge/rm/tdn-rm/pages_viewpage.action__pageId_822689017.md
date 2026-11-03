---
content_hash: 0ff221d4e1badc51450bdc150b6114dda97955dbe3eb2914be55d8ed1b1e845a
fetched_at: '2026-06-29T00:11:46.573108+00:00'
page_id: '822689017'
product: rm
source: tdn-rm
title: totTrib/vTotTrib
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822689017
version: 8
---

Grupo de informações destinado a informar os valores monetários (R$) totais aproximados dos tributos. Este grupo é gerado a partir do cálculo realizado nos itens do movimento.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Nome** | **Pai** | **Obrigatório** | **Origem** | **Máscara** | **Descrição** |
| **vTotTrib** | **NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/** | **Sim**  **(Condicional)** | **Grupo** | **--** | **Grupo de valores monetários totais aproximados dos tributos (R$).** |
| vTotTribFed | NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/vTotTrib/ | Sim | TITMMOVFISCAL.VALORIBPTFEDERAL  *(Soma dos valores dos Tributos Federais do Movimento)* | 1-15v2 | Valor monetário total aproximado dos tributos federais (R$). |
| vTotTribEst | NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/vTotTrib/ | Sim | TITMMOVFISCAL.VALORIBPTESTADUAL  *(Soma dos valores dos Tributos Estaduais do Movimento)* | 1-15v2 | Valor monetário total aproximado dos tributos estaduais (R$). |
| vTotTribMun | NFSe/infNFSe/DPS/infDPS/valores/trib/totTrib/vTotTrib/ | Sim | TITMMOVFISCAL.VALORIBPTMUNICIPAL  *(Soma dos valores dos Tributos Municipais do Movimento)* | 1-15v2 | Valor monetário total aproximado dos tributos municipais (R$). |

Regras de Negócio (Lógica de Geração)

Este grupo possui prioridade de geração para empresas do **Regime Normal** (Não Optantes pelo Simples Nacional). O sistema gera este grupo quando o cálculo detalhado está ativo.

**Condições Obrigatórias:**

1. **Regime:** A Filial **não** é optante pelo Simples Nacional.
2. **Parametrização:** O parâmetro **"Calcula Lei da Transparência"** está habilitado no cadastro do Tipo de Movimento.

> **Nota de Cálculo:** O sistema realiza a soma do campo `VALORIBPT...` da tabela `TITMMOVFISCAL` de **todos** os itens presentes no movimento para compor o totalizador da nota.
>
> Localização dos Valores IBPT no Item do Movimento
>
> Para o cálculo do Valor IBPT é necessário realizar o cadastro das alíquotas no Produto para a UF da filial.
>
> * *Caminho no sistema:* Cadastro do Produto | Anexo Dados Fiscais por UF | Aba Lei da Transparência.

### Detalhes Técnicos

* **Visualização na Interface:** Os valores somados aqui correspondem aos campos visíveis na tela de *Movimento > Item > Sub Pasta Valores* (quando o parâmetro está ativo).
* **Tipo de Dado:** Numérico Monetário (Decimal).
* **Precisão:** Suporta até 15 dígitos, sendo 2 decimais (Ex: `150.55`).
* **Exclusividade:** A geração deste grupo impede a geração dos grupos `pTotTrib` (Alíquotas) e do indicador `indTotTrib`.
