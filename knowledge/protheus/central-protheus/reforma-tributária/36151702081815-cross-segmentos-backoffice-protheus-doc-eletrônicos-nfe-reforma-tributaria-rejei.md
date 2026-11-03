---
article_id: 36151702081815
category: Reforma Tributária
content_hash: 37bd3c6552a279ed2711b4c74f7218ef26730ab6c29b48eb3b9453d0970ca60d
fetched_at: '2026-06-28T22:39:53.735695+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributaria
  - Rejeição 1026: Alíquota do IBS da UF inválida [nItem:1]'
type: support-article
updated_at: '2026-05-15T20:20:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36151702081815-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tributaria-Rejei%C3%A7%C3%A3o-1026-Al%C3%ADquota-do-IBS-da-UF-inv%C3%A1lida-nItem-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36151702059287) Tempo aproximado para leitura: **00:10 min**  
  
**Ocorrência**  
Ao transmitir uma nota fiscal eletrônica (NF-e) ou outro documento fiscal com cálculo de **CBS Federal,** **IBS Estadual e IBS Municipal** utilizando a classificação tributária cClassTrib que exigem redução de alíquota (CST = 200), é apresentada a seguinte rejeição:

***Rejeição 1026: Alíquota do IBS da UF inválida [nItem:1]***  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - A partir da 12.1.2310  
  
**Causa**  
Essa rejeição ocorre quando a **regra de alíquota** vinculada ao CST informado **não possui o percentual de redução como 100%** adequadamente configurado no campo **"% Redução de Alíquota"**para um código de cClassTrib que exige para o **IBS Estadual.**  
  
**Solução**  
Para resolver a rejeição, é necessário ajustar a **Regra de Alíquota** vinculada a Regra de Calculo do IBS Estadual com o cClassTrib 200003, informando corretamente o percentual de redução no campo correspondente e informar a alíquota 0% para as respectivas regras.

### 1. Acessar o Módulo Fiscal

* SIGAFIS → Configurador de Tributos → Regra de Cálculo Documentos Fiscais → **Regras de Alíquota** vinculada a Regra de Calculo do IBS Estadual, IBS Municipal e CBS Federal.
* No campo **Alíquota**, informe 0.1% para o IBS e 0.9% para CBS.
* No campo **% Redução de Alíquota**, informe o percentual de redução aplicável, conforme a legislação vigente.

CBS Federal:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37883125202071)

IBS Estadual:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37883125206423)

IBS Municipal:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36151702062871)

Obs: Deve ser utilizado o Tributo conforme abaixo:

CBS Federal: CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36151715744407)

IBS Estadual: IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36151702065175)

IBS Municipal: IBSMUN

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36151702066071)

### 2. Salvar Alterações

* Confirme a alteração e salve o registro.

### 

### 3. Geração da nova nota

* Após as alterações na Regra de Alíquota, gerar um novo documento.
* A rejeição não deve mais ocorrer.

## Observações

* O campo **% Redução de Alíquota** é obrigatório para determinadas classificações tributárias quando se trata do **IBS Estadual**, principalmente no CST 200003.
* A configuração incorreta pode impactar o cálculo do imposto e a validação da nota na Sefaz.
* Consultar a tabela do SEFAZ para verificar qual o percentual de redução para cada cClassTrib:

  [Tabela cClassTrib SEFAZ](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=dRTFFnw8z08=)
* Caso o campo CJ3\_ALIQOR não esteja com a alíquota informada, favor entrar em contato com o suporte Protheus Escrita Fiscal.

## Referências Técnicas

* [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)
* [Nota Técnica 2025.002.v.1.20 - Publicada em 30/07/2025](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YFz9is%20R6tw=)
