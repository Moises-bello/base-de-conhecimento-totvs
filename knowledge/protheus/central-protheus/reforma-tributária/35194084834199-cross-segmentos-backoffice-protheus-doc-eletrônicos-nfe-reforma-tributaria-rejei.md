---
article_id: 35194084834199
category: Reforma Tributária
content_hash: d6ea4c1e0dca9c58ddea19020f6b1096ae3eb8adbf9f3172b6a7cd4ad7efda05
fetched_at: '2026-06-28T22:39:53.768352+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria
  - Rejeição 1061: CST do IBS/CBS informado obriga informação de diferimento da CBS
  [nItem: 999]'
type: support-article
updated_at: '2025-09-25T15:14:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35194084834199-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1061-CST-do-IBS-CBS-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-da-CBS-nItem-999
---

**[Remover as instruções entre colchetes e altere o tempo aproximado para leitura]**  
  
![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35194084811927) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
Ao transmitir uma nota fiscal eletrônica (NF-e) ou outro documento fiscal com cálculo de **CBS**utilizando a classificação tributária cClassTrib = 510001/510002, é apresentada a seguinte rejeição:

*Rejeição 1061: CST do IBS/CBS informado obriga informação de diferimento da CBS [nItem: 999]*

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - A partir da 12.1.2310  
  
**Causa**  
Essa rejeição ocorre quando a **Regra de Escrituração** vinculada ao cClassTrib 510001/510002 informado **não possui o percentual de diferimento** adequadamente configurado no campo **"Percentual de Diferimento"** para um código de cClassTrib que exige para o **CBS**.  
  
**Solução**  
Para resolver a rejeição, é necessário ajustar a **Regra de Escrituração** vinculada a Regra de Calculo do CBS com o cClassTrib 510001/510002, informando corretamente o percentual de redução no campo correspondente.

### 1. Acessar o Módulo Fiscal

* SIGAFIS → Configurador de Tributos → Regra de Cálculo Documentos Fiscais → **Regras de Escrituração** vinculada a Regra de Calculo do CBS.
* No campo **Percentual de Diferimento**, informe o percentual de redução aplicável, conforme a legislação vigente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35194084812695)

Obs: Verifique com o Fiscal responsável da sua empresa o percentual de diferimento correto para a sua operação.

### 

### 2. Salvar Alterações

* Confirme a alteração e salve o registro.

### 

### 3. Geração da nova nota

* Após as alterações na Regra de Escrituração, gerar um novo documento.
* A rejeição não deve mais ocorrer.

## Observações

* O campo **Percentual de Diferimento** é obrigatório para determinadas classificações tributárias quando se trata do **CBS**, principalmente no CST 510001/510002.
* A configuração incorreta pode impactar o cálculo do imposto e a validação da nota na Sefaz.

## Referências Técnicas

* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)
* [Nota Técnica 2025.002.v.1.20 - Publicada em 30/07/2025](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YFz9is%20R6tw=)
* [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria - Rejeição 1044: CST do IBS Municipal informado obriga informação de diferimento Municipal [nItem: 999]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35193716836503-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1044-CST-do-IBS-Municipal-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-Municipal-nItem-999)
* [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria - Rejeição 1030: CST do IBS Estadual informado obriga informação de diferimento Estadual [nItem: 999]](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35193578228631-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1030-CST-do-IBS-Estadual-informado-obriga-informa%C3%A7%C3%A3o-de-diferimento-Estadual-nItem-999)
