---
article_id: 35192540469015
category: Reforma Tributária
content_hash: b40a8370f86e8061ae15987271c79ef01656b4c39ee7d9a7b96291b5a55b3e59
fetched_at: '2026-06-28T22:39:53.781654+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria
  - Rejeição 1079: Não informado o grupo de redução de alíquota da CBS [nItem: 999]'
type: support-article
updated_at: '2025-10-21T22:16:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35192540469015-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1079-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-da-CBS-nItem-999
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35192566929943) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
Ao transmitir uma nota fiscal eletrônica (NF-e) ou outro documento fiscal com cálculo de **CBS Federal** utilizando a classificação tributária cClassTrib que exige redução de aliquota, é apresentada a seguinte rejeição:

*Rejeição 1079: Não informado o grupo de redução de alíquota da CBS [nItem: 999]*

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - A partir da 12.1.2310  
  
**Causa**  
Essa rejeição ocorre quando a **R****egra de Alíquota** vinculada ao CST informado **não possui o percentual de redução** adequadamente configurado no campo **"% Redução de Alíquota"** para um código de cClassTrib que exige para o **CBS Federal**.  
  
**Solução**  
Para resolver a rejeição, é necessário ajustar a **Regra de Alíquota** vinculada a Regra de Calculo do IBS Estadual com o cClassTrib 200003, informando corretamente o percentual de redução no campo correspondente.

### 1. Acessar o Módulo Fiscal

* SIGAFIS → Configurador de Tributos → Regra de Cálculo Documentos Fiscais → **Regras de Alíquota** vinculada a Regra de Calculo do **CBS Federal**.
* No campo **% Redução de Alíquota**, informe o percentual de redução aplicável, conforme a legislação vigente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35192540435223)

Obs: Verifique com o Fiscal responsável da sua empresa o percentual de redução correto para a sua operação.

### 2. Salvar Alterações

* Confirme a alteração e salve o registro.

### 3. Geração da nova nota

* Após as alterações na Regra de Alíquota, gerar um novo documento.
* A rejeição não deve mais ocorrer.

## Observações

* O campo **% Redução de Alíquota** é obrigatório para determinadas classificações tributárias quando se trata do **CBS Federal**, principalmente no CST 200003.
* A configuração incorreta pode impactar o cálculo do imposto e a validação da nota na Sefaz.

## Referências Técnicas

* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)
* [Nota Técnica 2025.002.v.1.20 - Publicada em 30/07/2025](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YFz9is%20R6tw=)
* [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária - Rejeição 1035, 1041, 1064 e 1069](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35178711212055-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Rejei%C3%A7%C3%A3o-1035-1041-1064-e-1069)
* [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria - Rejeição 1033: Não informado o grupo de redução de alíquota Estadual [nItem: 999]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35191834941207-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1033-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-Estadual-nItem-999)
* [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria - Rejeição 1074: Não informado o grupo de redução de alíquota IBS Municipal [nItem: 999]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35192179404951-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1074-N%C3%A3o-informado-o-grupo-de-redu%C3%A7%C3%A3o-de-al%C3%ADquota-IBS-Municipal-nItem-999)
