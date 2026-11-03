---
article_id: 33208366723607
category: Reforma Tributária
content_hash: f9494ebfc1912ee7e61666db65dadf035951d67356907d850bc6059ce8f08ff3
fetched_at: '2026-06-28T22:39:53.796012+00:00'
product: protheus
section_id: 34900856700439
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFE - Reforma Tributária
  – Nota Técnica 2025.002 v.1.10, v1.20 e V1.30. IBS - CBS
type: support-article
updated_at: '2026-06-17T17:34:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33208366723607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFE-Reforma-Tribut%C3%A1ria-Nota-T%C3%A9cnica-2025-002-v-1-10-v1-20-e-V1-30-IBS-CBS
---

**Dúvida**  
O que deverá ser realizado e quais atualizações são necessárias para contemplar a Reforma Tributária – Nota Técnica 2025.002 v.1.10 e v.1.20 IBS e CBS?  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Todas as versões  
  
**Solução**  
Para contemplar a NT 2025.002 v.1.10, v.1.20 e v.1.30, deverão ser providenciadas as seguintes atualizações:

Criar os parâmetros abaixo no Protheus via Sigacfg,

[Documentação do parâmetro MV\_CSTGXML](https://tdn.totvs.com/pages/viewpage.action?pageId=1011566715)

[Documentação do parâmetro MV\_RTC55](https://tdn.totvs.com/pages/viewpage.action?pageId=1013641031)

**Protheus**  
**1. Aplicação do Pacote**

12.1.2310 <https://suporte.totvs.com/portal/p/10098/download#detail/1124963> [Somente para cliente com garantia estendida]

12.1.2410 <https://suporte.totvs.com/portal/p/10098/download#detail/1171486>

12.1.2510: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1224039>

**2. Aplicar o  patch e o nfesefaz do pacote liberado dia 17/06/2026.**

12.1.2310:<https://r.totvs.io/p/1255089> ; [Somente para cliente com garantia estendida]

12.1.2410:<https://r.totvs.io/p/1255090> ;

12.1.2510:<https://r.totvs.io/p/1255088> ;

**3. Aplicação do patch fiscal expedição continua**

12.1.2310: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1123867> [Somente para clientes com garantia estendida]

12.1.2410:  <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1182881> 

12.1.2510: <https://suporte.totvs.com/portal/p/10098/customer-portal-dashboard/services/downloads?e=1223280>  

**TSS**  
**1.** **Arquivos de Schema:** [Download dos schemas](https://suporte.totvs.com/portal/p/10098/download?e=761857)  
Apoio caso necessário: [Procedimento: Substituir na pasta schemas do TSS.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)  
  
**2.** **Atualizar RPO do TSS:** [Clique aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS)   
Documentação: [maiores detalhes.](https://tdn.totvs.com/pages/releaseview.action?pageId=956646956)

**Caso esteja na release 12.1.2310 sem garantia estendida, será necessário a migração para a release 12.1.2410:**  
- Veja como **migrar o TSS** [**aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038065954-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Migra%C3%A7%C3%A3o-para-12-1-2410-Instala%C3%A7%C3%A3o)!  
  
**📅** **Cronograma de Implementação (Previsão)**

* **Homologação**: a partir de 8 de setembro de 2025
* **Produção (****facultativo** **com regras de validação)**: a partir de 10 de novembro de 2025
* **Produção (****obrigatório** **com regras de validação)**: a partir de 5 de janeiro de 2026

**Para montar a tag vItem em produção facultativa antes de 05/01/2026, precisa criar o parâmetro** **MV\_NT25002** **= 10/11/2025 na tabela** **SPED000** **do** **TSS** **para a entidade que deseja mandar IBS e CBS um produção****.**

**Precisa criar o parâmetro** **MV\_RTC130** **= 01/01/2025 na tabela** **SPED000** **do** **TSS** **para a entidade que deseja mandar IBS e CBS um produção.**

**Observações:**  
**As orientações para CRT=1-Simples Nacional, CRT=2-Simples Nacional-Excesso de Sublimite, CRT=4-MEI e Tributação Monofásica serão publicadas em NT futura, tendo em vista que a tributação do IBS, CBS e IS para estes contribuintes ocorre somente a partir de 2027, conforme disposto no Art. 348 da LC 214/25.**  
  
[Notas Técnicas aqui!](https://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=04BIflQt1aY=)  
  
Precisa configurar a **Carga Automática (cClassTrib**) ou Configurar o cálculo de IBS e CBS? Acesse os links abaixo:  
1**.**[CFGTRIB - Adequação do Configurador de Tributos aos Códigos de Classificação Tributária do IBS, CBS e IS](https://tdn.totvs.com/pages/releaseview.action?pageId=962623217)  
**2.** [CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como importar a tabela cClassTrib-IBS/CBS no Configurador de Tributos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34662420522391-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-importar-a-tabela-cClassTrib-IBS-CBS-no-Configurador-de-Tributos)

Para maiores informações consulte a documentação abaixo:  
[Como configurar o calculo do IBS e CBS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33661274329367-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-calculo-do-IBS-e-CBS)

De acordo com a Nota Técnica 2025.002, versão 1.30, página 73.  
<https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=YFz9is%20R6tw=>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35067880339351)  
   
Alterações no DANFE para exibir informações relativas aos novos tributos estão em estudo, e serão publicadas em uma nova versão desta Nota Técnica.  
   
Se ainda tiver duvidas, entre em contato com a SEFAZ do seu estado.

**Observação:**

Para validar o xml com as novas regras do IBS e CBS a sefaz disponibilizou o link abaixo:

<https://dfe-portal.svrs.rs.gov.br/Cff/ValidadorNfe>

O suporte não tem controle sobre os validadores disponibilizados pela SEFAZ . Caso o validador acuse falha de schema mesmo após a autorização da nota, é recomendável entrar em contato com a SEFAZ do seu estado para esclarecimentos.

**Importante**

Assuntos relacionados a gravação  do IBS, CBS e IBSMUN, parâmetros, configurações e atualizações.

<https://tdn.totvs.com/pages/releaseview.action?pageId=995199956>

<https://tdn.totvs.com/pages/releaseview.action?pageId=1012517982>
