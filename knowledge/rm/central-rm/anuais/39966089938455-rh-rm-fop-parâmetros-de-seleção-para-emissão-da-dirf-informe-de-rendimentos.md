---
article_id: 39966089938455
category: Anuais
content_hash: 797f76b335153c09991567df16d02157b6da146bdd3de4c6c0ecd10d1be8a8dc
fetched_at: '2026-06-28T22:46:50.962621+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: RH - RM - FOP -  Parâmetros de Seleção para Emissão da DIRF / Informe de Rendimentos
type: support-article
updated_at: '2026-04-24T17:50:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39966089938455-RH-RM-FOP-Par%C3%A2metros-de-Sele%C3%A7%C3%A3o-para-Emiss%C3%A3o-da-DIRF-Informe-de-Rendimentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39966089880087) Tempo aproximado para leitura: **00:03:06 min**  
  
**Dúvida**  
Como parametrizar a primeira tela da geração do Informe de Rendimento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**  
Para emissão dos relatórios de Informe de Rendimento, acesse: **Anuais | DIRF/Informe de Rendimentos | DIRF/Informe de Rendimentos**

![primeira tela.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39966089883799)

Ao acessar o menu DIRF/Informe de Rendimentos, será apresentada a primeira tela de parametrização para geração dos relatórios.

Nesta parametrização é possível emitir 3 (três) relatórios:

* **Informe de Rendimentos** (padrão, detalhado ou em arquivo .TXT);
* **DIRF em Arquivo** (para importação no programa da Receita);
* **DIRF para Conferência** (relatório para validação visual dos dados).

![segunda tela.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39966089885207)

**Quebra de Seção:**

É importante que a DIRF seja gerada uma coligada por vez, com apenas uma seção.

Não pode haver quebra de seção no arquivo da DIRF, pois isso poderá ocasionar diversos erros durante a validação ou importação no programa da Receita Federal.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39966073280919)

**Código do Relatório - DIRF para Conferência:**

Informe o código do relatório que será utilizado quando, ao final do processo, for selecionada a opção: **“**DIRF para Conferência”. Este relatório será utilizado para validação visual das informações e não poderá ser importado no programa da DIRF.

![Código do Relatório - DIRF para Conferência.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39966089891351)

**Código do Relatório - Informe de Rendimentos:**

Informe o código do relatório que será utilizado quando for selecionada a opção: "Informe de Rendimentos"

O próprio sistema já disponibiliza três modelos padrão de Informe de Rendimento, :

* **FOPREL0008** – Informe de Rendimentos (modelo padrão)
* **FOPREL0011** – Informe de Rendimentos Detalhado
* **FOPREL0012** – Informe de Rendimentos em Arquivo TXT

![Código do Relatório - Informe de rendimento.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39966073285015)

Para gerar o Informe de Rendimentos em formato **.TXT**, será necessário:

1. Informar o relatório **FOPREL0012**;
2. Marcar o parâmetro **“Gerar Informe de Rendimentos em TXT”** em opções.

**Localização do(s) Arquivo(s):**

Informe o caminho onde os arquivos da DIRF serão salvos. O usuário responsável pela geração deverá possuir permissão de gravação na pasta informada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39966089898007)

**Observação - Buscar relatório no sistema:**

Caso nenhum relatório seja apresentado na tela de seleção, será necessário realizar previamente a importação dos relatórios pelo caminho: **Gestão | TOTVS Compartilhamento** e pesquisar o nome do relatório.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39966073289239)

Selecionar o relatório que deseja, apertar em Download e fazer a importação para o sistema.

![Totvs compartilhamento 2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39966073291287)

Após este procedimento o relatório será apresentado na tela de seleção.

**Saiba mais**

[Parametrização do menu de emissão da rotina DIRF / Informe de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=208347682)

[Opções para geração do menu de emissão da rotina DIRF / Informe de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=208347682#Op%C3%A7%C3%B5esparaGera%C3%A7%C3%A3o-2-3)
