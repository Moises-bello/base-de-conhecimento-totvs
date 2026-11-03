---
content_hash: 18434530c5fb046a46856542acc98183e46507018d2c69b6780da8281bae53cd
fetched_at: '2026-06-29T00:09:35.924163+00:00'
page_id: '425459434'
product: rm
source: tdn-rm
title: Cancelar Empréstimos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459434
version: 7
---

**Cancelar Empréstimos**

---

O processo de Cancelar Empréstimos faz parte da solução de integração TOTVS Folha de Pagamento x Gestor AVB (TOOLS) para a Averbação (empréstimo consignado em folha). Algumas ações poderam ser tomadas diretamente no Gestor de Averbação (Tools), como por exemplo a quitação antecipada de contratos, que irá efetuar o cancelamento imediato do empréstimo no TOTVS Folha. No TOTVS Folha estará disponível um serviço que deverá efetuar a quitação antecipada de empréstimos do tipo AVBTOTVS, levando em consideração as informações descritar abaixo que serão enviadas pelo TOOLS.

|  |  |
| --- | --- |
| **CAMPO** | **OBRIGATÓRIO** |
| CNPJ (coligada) | SIM |
| CPF | SIM |
| Matrícula (chapa) | SIM |
| Código Empréstimo | SIM |
| Usuário | SIM |
| Senha | SIM |

Este processo irá atualizar o campo Saldo Devedor, do empréstimo consignado, para '0,00' e igualar o Número de Parcelas Pagas ao Número de Parcelas. Os empréstimos que estiverem cancelados estarão gravados em um histórico disponível no TOTVS Folha, na tabela PFDESCEMPRT. Quando todo o processo é concluído o TOTVS Folha disponibiliza para o Business Conector um retorno da execução que será enviado para o Gestor de Averbação (TOOLS), como sucesso (1) ou erro (0).
