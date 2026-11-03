---
content_hash: fe849351878d911f8dd3e96fe0ee44e4776a1ffc2a4f0f55c3d01dcdb906d848
fetched_at: '2026-06-29T00:12:08.064771+00:00'
page_id: '928946396'
product: rm
source: tdn-rm
title: Leiaute S-1.3 - Nota Técnica 03/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=928946396
version: 10
---

false

**A partir das Versões:**

# Objetivo:

Adequamos o produto TOTVS Folha de Pagamento para atender ao leiaute S-1.3, conforme as alterações descritas nas notas técnicas do eSocial nº [03/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-03-2025.pdf) do eSocial.

---

11ParametrizaçãoParametrização

1) Criado o parâmetro da Nota Técnica (**S-1.3 NT 03/2025**) em Configurações | Parametrizador | Folha de Pagamento | eSocial | Configurações Gerais conforme demonstrado abaixo:

2) Após a liberação da versão será necessário executar os scripts de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

2 Nota Técnica 03/2025 Nota Técnica 03/2025

1) **S-1000** - Criado o parâmetro "Indicador de pertencimento do IRRF" em eSocial | Informações do Empregador | Pasta Identificação conforme demonstrado abaixo:

2) **S-1200, S-1202, S-1207, S-2299 e S-2399** - Alterado o tamanho do campo "**Número do contrato de empréstimo consignado CEF"** de 8 para 15. Esse campo é preenchido em Administração de Pessoal | Funcionários | Anexos Folha de Pagamentos | Empréstimos. E a validação que exigia exatamente 8 caracteres foi removida.

3) **S-2500, S-2501 e S-3500** - Os eventos Processo Trabalhista foram adequados conforme links abaixo:
