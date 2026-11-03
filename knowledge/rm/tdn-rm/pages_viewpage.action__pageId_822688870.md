---
content_hash: 82bac53cdd8bcd110f08d5a1a16b7f43de77ff6d97b0460d2be8fa5f7bcac84a
fetched_at: '2026-06-29T00:11:46.541584+00:00'
page_id: '822688870'
product: rm
source: tdn-rm
title: tribMun/BM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822688870
version: 16
---

## Grupo de informações sobre o tipo do Benefício Municipal

Grupo específico para indicar os dados do Benefício Fiscal Municipal que afetam a NFS-e. Conforme definido no , informações de Benefícios Fiscais são tratados de forma especifica pela TOTVS.

Este grupo só será gerado se o parâmetro "Gerar Benefício Municipal" estiver marcado nos dados fiscais do município da filial.

**IMPORTANTE**: Caso o campo complementar no **movimento** esteja preenchido e o parâmetro desmarcado, será apresentado inconsistencia para marcar o parâmetro ou limpar o campo complementar.

| Nome | Pai | Obrigatório | Origem | Descrição |
| --- | --- | --- | --- | --- |
| **BM** |  | **Não** | Grupo | **Grupo de informações sobre o tipo do Benefício Municipal** |
| nBM | BM | Sim | Criar campo complementar no movimento.  Incluir o campo complementar na parametrização do tipo de movimento e preenchê-lo no movimento.  O mesmo campo complementar pode ser também adicionado ao produto.  Se os campos do produto e do movimento estiverem preenchidos é dada prioridade ao campo do movimento. | Identificador do benefício parametrizado pelo município.  Trata-se de um identificador único que foi gerado pelo Sistema Nacional no momento em que o município de incidência do ISSQN incluiu o benefício no sistema. |
| vRedBCBM | BM | Não | (Valor líquido do movimento - Base de cálculo do ISS) | Valor monetário (R$) informado pelo emitente para redução da base de cálculo (BC) do ISSQN devido a um Benefício Municipal (BM). |
| pRedBCBM | BM | Não | Campo complementar do produto PERCBENEFICIOMUN. | Valor percentual (%) informado pelo emitente para redução da base de cálculo (BC) do ISSQN devido a um Benefício Municipal (BM). |

## Configuração de Campos Complementares

Para a geração do grupo é necessária a criação de três campos específicos nos cadastros de **Movimento** e **Produto**.

| **Campo (Coluna)** | **Localização** | **Descrição** | **Tipo / Tamanho** |
| --- | --- | --- | --- |
| **NUMBENEFICIOMUN** | Movimento e/ou Produto | Número do Benefício Municipal | Alfanumérico (14) |
| **PERCBENEFICIOMUN** | Produto | Percentual de redução da base de cálculo | Alfanumérico (4) |
| **TIPOBENEFICIOMUN** | Produto | Define qual tag de redução será gerada (veja regras abaixo) | Inteiro |

## Regras de Geração das Tags (vRedBCBM e pRedBCBM)

* Se **TIPOBENEFICIOMUN** = 2: O sistema gera a tag vRedBCBM.
  + Cálculo: Corresponde ao valor monetário (R$) da redução (Valor líquido - Base de cálculo do ISS).
* Se **TIPOBENEFICIOMUN** = 3: O sistema gera a tag pRedBCBM.
  + Cálculo: Corresponde ao valor percentual (%) informado.
