---
content_hash: c3e5c4b3168170bc1f4ea79d376f1bfa44e8278eddfde1756bb7d779673e6408
fetched_at: '2026-06-29T00:11:49.752260+00:00'
page_id: '837872620'
product: rm
source: tdn-rm
title: Nota Técnica V.S-1.2 01/2023-Itens 3.3 e 3.4
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=837872620
version: 2
---

false

**A partir das Versões:**

# Objetivo:

---

Adequamos o produto TOTVS Folha de Pagamento para atender ao leiaute S-1.2, conforme as alterações descritas na [Nota Técnica 01/2023](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-01-2023.pdf)[,](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-1-01-2023.pdf)  do eSocial, publicada em 07/12/2023, referentes aos itens 3.1 e 3.2.

11AtualizadorAtualizador

Após a liberação da versão será necessário executar os script's de adequação das tabelas e campos do sistema através do sistema **RM.Atualizador.exe.**

true3Alterações com entrada em produção 04/01/2024 Alterações com entrada em produção 04/01/2024 

1) **Tabela 01 - Categorias de Trabalhadores**

Alteração a descrição do código 902 para Contemplar o médico em curso de formação, conforme Lei 13.958/2019.

| DE | PARA |
| --- | --- |
| Médico residente ou residente em área profissional de saúde | Médico residente, residente em área profissional de saúde ou médico em curso de formação |

Ajustado na Tabela Dinâmica **PESOCIALCATTRAB**  conforme demonstrado abaixo:

2) **Tabela 03 – Natureza das Rubricas da Folha de Pagamento**

Incluído o código [1012] relativo a DSR e feriado.

Incluído na Tabela Dinâmica **PCODNATRUBRICA** o código "1012 - Descanso semanal remunerado - DSR e feriado" conforme demonstrado abaixo:

3) **Tabela 10 de Tipos de Lotação Tributária** 

Incluído o código 92 para possibilitar a informação de bolsista contribuinte individual sem contribuição patronal (médico em curso de formação).

Incluído na Tabela Dinâmica **PTIPOSLOTACAO** o tipo "92 Bolsista contribuinte individual sem contribuição patronal", conforme demonstrado abaixo:

4) **S-1020 - Tabela de Lotações Tributárias** - **campo  {dadosLotacao/tpInsc}**

Incluída a possibilitar a informação de bolsista contribuinte individual sem contribuição patronal (médico em curso de formação).

Tratamento na geração do XML do evento S-1020, incluindo a opção "92-Bolsista contribuinte individual sem contribuição patronal" nos campos "20-nrInsc e tpInsc".

5) **S-1000 - Informações do Empregador/Contribuinte/Órgão Público**

Correção de descrição do campo {vlrDedPC}

Ajuste na descrição do campo "Indicador de tributação sobre a folha de pagamento - PIS e COFINS" para "Indicador de tributação sobre a folha de pagamento - PIS e PASEP", existente em eSocial | Informações do Empregador | Aba Informações Complementares.

Alterada a Tabela **PESOCIALEMPREGADOR.INDTRIBFOLHAPISCOFINS**.
