---
content_hash: 9781e136cbc1cfda6ca3b8f5f5a5e4c287784d8a789e607f361020a57dfa0349
fetched_at: '2026-06-29T00:12:08.470531+00:00'
page_id: '934636669'
product: rm
source: tdn-rm
title: DT - Informações do Local de Trabalho nos eventos S-2200, 2206, 2300 e 2306
  - Parâmetro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=934636669
version: 16
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Informações do Local de Trabalho nos eventos S-2200, 2206, 2300 e 2306 - Parâmetro |
| País: | Brasil |
| Issue: | [DRHROTRM-13573](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13573) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.133
* 12.1.2410.216
* 12.1.2502.265 e superiores

## **03. SITUAÇÃO/REQUISITO**

Permitir definir, na geração dos eventos S-2200, 2206, 2300 e 2306, a opção de registrar no grupo **"Informações do local de trabalho"** (tag `<localTrabalho>`) com as informações do **CEI da obra própria** ou as informações da **seção do funcionário** quando o funcionário estiver alocado em um único tomador de serviço.

Essa melhoria visa oferecer maior flexibilidade no preenchimento do evento, atendendo diferentes cenários de alocação dos trabalhadores conforme as exigências do eSocial.

## **04. SOLUÇÃO**

Foi implementado, no menuConfigurações | Parametrizador | eSocial | Configurações Gerais 3/7, o parâmetro **"Considera CNO nas tags localTrabGeral do S-1005 para funcionários alocados em um único tomador obra própria"**.

Com essa configuração habilitada, passa a ser possível registrar no grupo "Informações do local de trabalho" (tag `<localTrabalho>`) dos eventos S-2200, 2206, 2300 e 2306 as informações do CEI da obra própria quando o funcionário estiver alocado em um único tomador de serviço.

Ao marcar esse parâmetro o sistema irá buscar os dados conforme tomador de serviço informado no menu Administração de Pessoal | Funcionário | Anexos | Históricos | Histórico de Rateio por Tomador, conforme demonstrado abaixo:

XML:

 

Importante

1. **Não será gerado gatilho** na troca do tomador, ou seja, a alteração do tomador não dispara automaticamente o envio do evento S-2206 – Alteração de Contrato de Trabalho.
2. Somente com o parâmetro **"Considera CNO nas tags localTrabGeral do S-1005 para funcionários alocados em um único tomador obra própria"** marcado, o XML será gerado com as **informações do CEI da obra própria** no grupo **"Informações do local de trabalho"** (tag `<localTrabalho>`).

## **05.****ASSUNTOS RELACIONADOS**

[Mapeamento S-2200](https://tdn.totvs.com/display/LRM/Evento+S-2200)

[Mapeamento S-2206](https://tdn.totvs.com/display/LRM/Evento+S-2206)

[Mapeamento S-2300](https://tdn.totvs.com/display/LRM/Evento+S-2300)

[Mapeamento S-2306](https://tdn.totvs.com/display/LRM/Evento+S-2306)
