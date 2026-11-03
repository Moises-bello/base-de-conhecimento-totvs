---
content_hash: 0e9f16d6ca06bfe4cbdbffd9a0b3bd86c6ee97ad8bb89c33c54baebc70937be6
fetched_at: '2026-06-29T00:10:58.786965+00:00'
page_id: '606843193'
product: rm
source: tdn-rm
title: Alterações S-1210
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=606843193
version: 5
---

false

**A partir das Versões:**

* 12.1.29.282
* 12.1.31.197
* 12.1.32.135
* e Superiores.

# Objetivo:

---

Apresentar as alterações realizadas no evento S-1210 para o leiaute do eSocial Versão S-1.0.

---

| GRUPO/CAMPO/ITEM | DE | PARA |
| --- | --- | --- |
| Grupos {**ideEvento**}: Campo {**nrRecibo**}  Alterado tamanho | De: 40 | Para: 23 |
| Grupos {**ideEvento**}: Campo      **{evPagtos}**           Alterado Chave |  | Para: {indApuracao} , {perApur} e {indguia} |
| Grupos {**ideEvento**}: Campo      **{ideBenef}**  Alterado Chave |  | Para: {tpPgto} , {perRef} e {ideDmDev} |
| Grupos {**ideEvento**}: Campo      **{indApuracao}** |  | Campo excluido |
| Grupos{**ideEvento**}: Campo     **{IndGuia}**          Incluído campo |  | Indicativo do tipo de guia. **Valores válidos:** **1** - Documento de Arrecadação do eSocial - DAE |
| Grupo {**ideEvento**}: Campo     **{tpAmb}**         Incluído Valores | DE: 1 - Produção;        2 - Produção restrita. | Identificação do ambiente. Valores válidos: 1 - Produção 2 - Produção restrita 7 - Validação (uso interno) 8 - Teste (uso interno) 9 - Desenvolvimento (uso interno) |
| Grupo {**ideEvento**}: Campo     **{procEmi}**      Incluído Valores , Alterado        descrição e excluído campo | 1- Aplicativo do empregador;  2 - Aplicativo governamental - Empregador Doméstico;  3 - Aplicativo governamental - Web Geral;  4 - Aplicativo governamental - Simplificado Pessoa Jurídica;  5 - Aplicativo governamental - Segurado Especial. | 1 - Aplicativo do empregador 2 - Aplicativo governamental - Simplificado Pessoa Física 3 - Aplicativo governamental - Web Geral 4 - Aplicativo governamental - Simplificado Pessoa Jurídica 22 - Aplicativo governamental para dispositivos móveis - Empregador Doméstico 81 - Aplicativo governamental para envio de eventos pelo Judiciário 91 - Aplicativo governamental - Integração com a Junta Comercial |
| Grupo {**ideBenef**}:Campo**{deps}**      Campo Excluido |  | Campo Excluido |
| Grupo {**infoPagto**}:Campo**{dtpPgto}**    Aterada a Validação | Informar a data de pagamento. Validação: A data informada deve estar compreendida no período de apuração ({perApur}), exceto se {procEmi} = [2, 4]. | Informar a data de pagamento.  Validação: A data informada deve estar compreendida no período de apuração (perApur), exceto se procEmi = [2, 4, 22]. |
| Grupo {**infoPagto**}:Campo**{tpPgto}**      Aterada a Validação |  | Valores válidos:  1 - Pagamento de remuneração, conforme apurado em ideDmDev do S-1200  2 - Pagamento de verbas rescisórias conforme apurado em ideDmDev do S-2299 3 - Pagamento de verbas rescisórias conforme apurado em ideDmDev do S-2399 4 - Pagamento de remuneração conforme apurado em ideDmDev do S-1202 5 - Pagamento de benefícios previdenciários, conforme apurado em ideDmDev do S-1207 |
| Grupo{**infoPagto**}:Campo**{indResBr}**      Campo excluido |  | Campo Excluido |
| Grupo{**infoPagto**}:Campo**{perRef}**      Campo incluido |  | Informar a competência declarada no campo {perApur} do evento remuneratório a que se refere o pagamento, no formato AAAA-MM (ou AAAA, se for relativa à folha de 13° salário). Se tpPgto = [2, 3], informar o mês/ano da data de desligamento (ou de término), no formato AAAAMM. Validação: Deve corresponder ao conteúdo indicado na relação a seguir:  Se tpPgto = [1], perApur do S-1200;  Se tpPgto = [2], mês/ano de dtDeslig do S-2299 (formato) |
| Grupo{**infoPagto**}:Campo**{ideDmDev}**      Campo incluido |  | Identificador atribuído pela fonte pagadora para o demonstrativo de valores devidos ao trabalhador conforme definido em S-1200, S-1202, S-1207, S-2299 ou S-2399. Validação: Deve ser um valor atribuído pela fonte pagadora em S-1200, S-1202, S-1207, S-2299 ou S-2399 no campo {ideDmDev}, obedecendo à relação:  Se tpPgto = [1], em S-1200;  Se tpPgto = [2], em S-2299;  Se tpPgto = [3], em S-2399;  Se tpPgto = [4], em S-1202;  Se tpPgto = [5], em S-1207. |
| Grupo{**infoPagto**}:Campo**{vrLiq}**      Campo incluido |  | Valor líquido recebido pelo trabalhador, composto pelos vencimentos e descontos, inclusive os descontos de IRRF e de pensão alimentícia (se houver). Validação: Não pode ser um valor negativo. |
