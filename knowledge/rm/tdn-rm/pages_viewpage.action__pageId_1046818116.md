---
content_hash: cc323f448cd41e08d7e88fd941e0973156952dd1a45ee84ee0c5ba96699d51ff
fetched_at: '2026-06-29T00:05:51.021658+00:00'
page_id: '1046818116'
product: rm
source: tdn-rm
title: Leiaute S-1.3 - Nota Técnica 06/2026
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1046818116
version: 20
---

false

**A partir das Versões:**

* [DT - eSocial - Leiaute S-1.3 - Nota Técnica 06/2026 - Processo Trabalhista](https://tdn.totvs.com/pages/viewpage.action?pageId=1062372952)

# Objetivo:

Adequamos o produto TOTVS Folha de Pagamento para atender ao leiaute S-1.3, conforme as alterações descritas na [Nota Técnica 06/2026](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-3-06-2026.pdf).

11ParametrizaçãoParametrização

1) Criado o parâmetro da Nota Técnica (**S-1.3 NT 06/2026**) em Configurações | Parametrizador | Folha de Pagamento | eSocial | Configurações Gerais conforme demonstrado abaixo:

2 Nota Técnica 06/2026 - Folha de Pagamento Nota Técnica 06/2026 - Folha de Pagamento

1) **Grupo {infoRegCTPS} – alterada condição.**

Ao gerar o xml o sistema apresenta erro caso não tenha os campos preenchidos

3 Nota Técnica 06/2026 - Processos Trabalhistas Nota Técnica 06/2026 - Processos Trabalhistas

### S-2500 - Processo Trabalhista

| CAMPOS E GRUPOS ALTERADOS | DESCRIÇÃO DA ALTERAÇÃO |
| --- | --- |
| Campo {compFim} – alterada validação. | Possibilitar a recepção do evento caso a competência seja posterior ao mês/ano de {dtSent} ou {dtCCP}. |
| Grupo {infoProcJud} – alterada condição. | Ajuste realizado em virtude da possibilidade de transmissão do evento quando se tratar de precatórios da Justiça Comum (situação aplicável a órgãos públicos). |
| Grupo {infoInterm} – alterada condição. | Correção de condição do grupo, para que o grupo seja preenchido (ou não) nos casos de mudança de categoria. |
| Campo {origem} – alterada descrição do valor [1] e incluído valor [3]. | Possibilitar o preenchimento do evento quando se tratar de precatórios da Justiça Comum (situação aplicável a órgãos públicos). |
| Campo {nrProcTrab} – alterada validação. | Ajuste para validar o 14º (décimo quarto) algarismo do número do processo. |
| Campo {infoPatPrec} – criado. | Ajuste realizado em virtude da possibilidade de transmissão do evento quando se tratar de precatórios da Justiça Comum (situação aplicável a órgãos públicos). |
| Campo {infoContr/tpContr} – alterada validação. | Ajuste realizado em virtude da possibilidade de transmissão do evento quando se tratar de precatórios da Justiça Comum (situação aplicável a órgãos públicos). |
| Campo {mudCategAtiv/codCateg} – alterada validação. | Correção de validação, de acordo com o conteúdo do campo {indCateg} |
| Campo {mudCategAtiv/natAtividade} – alterada validação. | Correção de validação, de acordo com o conteúdo do campo {indNatAtiv} |

S-2501 - Informações dos Tributos Decorrentes de Processo Trabalhista)

| CAMPOS E GRUPOS ALTERADOS | DESCRIÇÃO DA ALTERAÇÃO |
| --- | --- |
| Campo {perRef} – alterada validação. | Não permitir que o campo seja posterior a {perApurPgto} |
| Campo {nrProcTrab} – alterada validação. | O evento S-2501 não é aplicável a processos da Justiça Comum. |
