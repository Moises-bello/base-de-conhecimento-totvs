---
content_hash: a3ca944a8b004039e60cd629ace1b019ec8117a8aa5de6a56631c67ad81a7885
fetched_at: '2026-06-29T00:12:15.455521+00:00'
page_id: '979796252'
product: rm
source: tdn-rm
title: Leiaute S-1.3 - Nota Técnica 04/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=979796252
version: 22
---

false

**A partir das Versões:**

# Objetivo:

Adequamos o produto TOTVS Folha de Pagamento para atender ao leiaute S-1.3, conforme as alterações descritas na [Nota Técnica 04/2025](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-04-2025.pdf) e na [Nota Técnica 04/2025 Revisada](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-04-2025-rev.pdf) do eSocial.

---

11ParametrizaçãoParametrização

1) Criado o parâmetro da Nota Técnica (**S-1.3 NT 04/2025**) em Configurações | Parametrizador | Folha de Pagamento | eSocial | Configurações Gerais conforme demonstrado abaixo:

2) Após a liberação da versão será necessário executar os scripts de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

2 Nota Técnica 04/2025 Nota Técnica 04/2025

**1) Tabela 03 - Natureza das Rubricas**

Foi incluído o código [9912], e alterada o nome da natureza da rubrica dos códigos [6129 e 9219], conforme abaixo:

| Código | De | Para |
| --- | --- | --- |
| 6129 | Outras multas ou indenizações | Outras verbas não remuneratórias (indenizatórias ou multas) |
| 9219 | Desconto de assistência médica ou odontológica | Desconto de assistência médica ou odontológica - Plano coletivo empresarial |
| 9912 | N/A | Desconto de assistência médica ou odontológica - Plano diferente de coletivo empresarial |

Realizamos a adequação na tabela dinâmica **NATRUBRICA - Natureza das rubricas da folha de pagamento**, conforme demonstrado abaixo:

**2) Tabela 25 - Tipos de Benefícios**

Foi incluído o código [0606], conforme descrito abaixo:

| Código | DESCRIÇÃO DO BENEFÍCIO |
| --- | --- |
| 0606 | Pensão por morte - EC 103/2019 |

Realizamos a adequação no menu Administração de Pessoal |Funcionários | Anexos | Folha de Pagamento | Dados do Benefício, conforme demonstrado abaixo:

**3) Tabela 18 - Motivos de Afastamento**

Foi incluído os códigos [44, 45] e alterado a descrição do código [21], conforme descrito abaixo:

| Código | De | Para |
| --- | --- | --- |
| 21 | Licença não remunerada ou sem vencimento | Licença não remunerada ou suspensão contratual decorrente de obrigação legal incompatível com a continuação do serviço |
| 44 | N/A | Suspensão contratual decorrente de ajuizamento de reclamação trabalhista pleiteando rescisão indireta do contrato |
| 45 | N/A | Suspensão contratual para ajuizamento de inquérito para apuração de falta grave |

Realizamos a adequação na tabela dinâmica **PESMOTAFAS - Mot de afast do ESocial**, conforme demonstrado abaixo:

**4) Natureza de Rubrica X Incidência INSS eSocial**

Nova regra de validação para os eventos remuneratórios do eSocial (S-2299, S-2399 e S-1200).

false🔔 ATENÇÃO:

Preparamos uma documentação com o passo a passo para conferência [saiba mais.](https://tdn.totvs.com/pages/viewpage.action?pageId=979033796)

2 Nota Técnica 04/2025 Revisada Nota Técnica 04/2025 Revisada

**1) Tabela 03 - Natureza das Rubricas**

Foi incluído os códigos abaixo:

| Código | Descrição |
| --- | --- |
| 1015 | Adiantamento de férias |
| 1799 | Alimentação concedida em pecúnia com caráter indenizatório |
| 1811 | Auxílio-transporte ou auxílio-combustível com caráter salarial |

Realizamos a adequação na tabela dinâmica **NATRUBRICA - Natureza das rubricas da folha de pagamento**, conforme demonstrado abaixo:

**2) Tabela 03 - Natureza das Rubricas**

Foram alteradas as descrições dos códigos descritos abaixo:

| Código | De | Para |
| --- | --- | --- |
| 1800 | Alimentação concedida em pecúnia | Alimentação concedida em pecúnia com caráter salarial |
| 1810 | Transporte | Vale-transporte ou auxílio-transporte com caráter indenizatório |

Realizamos a adequação na tabela dinâmica **NATRUBRICA - Natureza das rubricas da folha de pagamento**, conforme demonstrado abaixo:

2 Nota Técnica 04/2025 Tag notAFT Nota Técnica 04/2025 Tag notAFT

**1) Tag notAFT**

A geração do XML dos eventos **S-1200**, **S-2299** e **S-2399** passou a considerar a nova tag **notAFT**, disponível na tabela **PFPERFF**.

Sempre que o campo **“Notificação da Auditoria Fiscal do Trabalho”** estiver preenchido, a tag **`<notAFT>`** será automaticamente incluída no XML, com o respectivo valor informado, garantindo o envio conforme o layout definido pelo eSocial.

Para o preenchimento desse campo, acesse o menu Administração de Pessoal | Funcionários | Anexos | Movimento | Ficha Financeira, em seguida, edite o período desejado e informe corretamente o valor no campo **“Notificação da Auditoria Fiscal do Trabalho”**, conforme demonstrado abaixo:

Geração do XML:
