---
article_id: 38006107103639
category: Escrita Fiscal - Impostos - ICMS
content_hash: 51f6f84c4b5b641c4b009787a90871922a34a5c1ed8e993d3d2a212ec2416035
fetched_at: '2026-06-28T22:39:24.408884+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar os
  Códigos de Valores Declaratórios de São Paulo no Protheus?
type: support-article
updated_at: '2026-04-10T20:18:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38006107103639-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-os-C%C3%B3digos-de-Valores-Declarat%C3%B3rios-de-S%C3%A3o-Paulo-no-Protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38006075898519) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como configurar os Códigos de Valores Declaratórios de São Paulo?  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da versão 12.1.2410  
  
**Solução**  
Para configurar realize os seguintes passos:

**Pontos principais da obrigatoriedade do cBenef em SP:**

* **Prazo Final:** A partir de 6 de abril de 2026, notas sem o código correto ou com código genérico, quando houver um específico, serão rejeitadas.
* **Ambiente de Testes:** A validação começa em ambiente de homologação em 12 de janeiro de 2026.

### Cadastrar os Códigos de Benefícios Fiscais - cBenef

No site <https://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=SpedFiscal> ainda não foi disponibilizado para o estado de SP a tabela 5.2.

Com isso, nesse momento ainda não é possível importar a tabela via compatibilizador U\_IMPSPED, pois o próprio Fisco ainda não disponibilizou o arquivo para download.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38006107084951)

 Porém, é possível cadastrar os códigos manualmente na rotina FISA156 - Códigos de Valores Declaratórios.

Primeiro deverá acessar o portal da fazenda de SP e baixar a Tabela CST x cBenef - Excel.  
<https://portal.fazenda.sp.gov.br/servicos/nfe/Paginas/cBenef.aspx>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38006107088919)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38006107089815)

Acesse a rotina FISA156 - - Códigos de Valores Declaratórios e realize a configuração manualmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38006107090071)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38006107090967)
