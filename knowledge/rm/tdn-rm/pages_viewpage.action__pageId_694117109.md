---
content_hash: f97e2411585005b9790f1ea608c9c9742172ca9ea84bf5fc59380be0cfb26f60
fetched_at: '2026-06-29T00:11:21.382806+00:00'
page_id: '694117109'
product: rm
source: tdn-rm
title: DT - Nome Social - Relatórios RM Reports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=694117109
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | Plataforma RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Gerador de Relatórios - RM Reports |
| País: | Brasil |
| Ticket: | S/N |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-2585](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2585)  [DRHCALCRM-2586](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2586)  [DRHCALCRM-2587](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2587) |

## **02. SITUAÇÃO/REQUISITO**

Atendendo a Portaria 1.036/2015 ([https://mpt.mp.br/pgt/publicacoes/cartilhas/atendimento-do-mpt-a-populacao-lgbqi/@@display-file/arquivo\_pdf)](https://mpt.mp.br/pgt/publicacoes/cartilhas/atendimento-do-mpt-a-populacao-lgbqi/@@display-file/arquivo_pdf) "Follow link") será implementado nos relatórios do RM Reports de  Demonstrativo de Pagamento, Aviso e Recibo de Férias a opção de exibir o Nome Social ao invés do Nome do cadastro de funcionário.

## **03. SOLUÇÃO**

Os relatórios (RM Reports) foram ajustados para obter o nome social caso tenha sido informado no cadastro do funcionário e marcado o parâmetro "Exibir Nome Social do Funcionário", disponível em RM | RH | Gestão de Pessoas | Configurações | Parametrizador | Configurações | Portal Meu RH | Controle de Dados Pessoais. Com ele desmarcado continua sendo exibido o "nome" do cadastro de funcionário.

**Exemplo:**

**1) Em RM | RH | Folha de Pagamento | Administração de Pessoal | Cadastros | Funcionários, cadastrar o Nome Social para o funcionário:**

**2) Acessar RM | RH | Gestão de Pessoas | Configurações | Parametrizador | Configurações | Portal Meu RH | Controle de Dados Pessoais e marcar 'Exibir nome social do funcionário':**

**3) Em RM | RH | Ferramentas de Análise | RM Reports, importar os relatórios alterados:**

**4) Em RM | RH | Ferramentas de Análise | RM Reports, gerar o relatórios:**

**Os relatórios que sofreram alteração são:**

**1) Demonstrativo de Pagamento**

FOPREL00015 - Envelope pgto Modelo Extrato (frenteverso).TotvsReport

FOPREL00016 - Envelope pgto Modelo Extrato (frenteverso).TotvsReport

FOPREL00176 - Envelope Pgto Portal Padrão.TotvsReport

FOPREL00177 - Envelope Pgto Portal Personalizado ORACLE.TotvsReport

FOPREL00178 - Envelope Pgto Portal Personalizado SQL.TotvsReport

FOPREL00192 - Envelope pgto Model Extrato (frenteverso).TotvsReport

FOPREL25.0025 - 2.004.101 - Envelope de pagamento - Labo 05.0.TotvsReport

**2) Aviso de Férias**

FOPREL00200 - Aviso de Férias (Modelo 3).TotvsReport

FOPREL00193 - Aviso de Férias - Modelo 2.TotvsReport

FOPREL00180 - Aviso de Férias - ORACLE.TotvsReport

FOPREL00030 - Aviso de Férias.TotvsReport

**2) Recibo de Férias**

FOPREL00112 - Recibo de Férias.TotvsReport

FOPREL00190 - Recibo de Férias RM Portal.TotvsReport

FOPREL00194 - Recibo de Férias(Modelo 2).TotvsReport

Caso utilize algum relatório listado acima do book padrão do Módulo TOTVS Folha de Pagamento, é necessário importar novamente os relatórios que estão na pasta Objetos Gerenciais após a atualização do Patch. A adequação não é aplicável a relatórios customizados. Neste caso é necessário que o cliente avalie a necessidade de adequação dos mesmos.
