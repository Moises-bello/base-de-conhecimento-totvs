---
article_id: 33778269624471
category: Escrita Fiscal - Configurador de Tributos
content_hash: 37f1c55effbec41fe6ecb3c6fe861578fc852b2e9a0f881d7dbd536b605ebb56
fetched_at: '2026-06-28T22:39:18.394290+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 – Como altera
  a consulta padrão do código de serviço da tabela 60 para a CCQ.
type: support-article
updated_at: '2025-11-28T14:41:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33778269624471-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-Como-altera-a-consulta-padr%C3%A3o-do-c%C3%B3digo-de-servi%C3%A7o-da-tabela-60-para-a-CCQ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33778269603607) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como alterar a consulta padrão do código de serviço no Configurador de Tributos da tabela 60 para a CCQ no Perfil de Operação e Regra de Códigos de Prestação de Serviço?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões

**Solução**  
Para a alteração da consulta padrão no Configurador de Tributos na Regra de Código de Prestação de Serviço e Perfil de Operação aba Código de Serviço para a tabela CCQ que é preenchida via a rotina Cod. Serviço (MATA943), é preciso realizar o seguinte procedimento:

**1)** Acesse o Configurador, Base de dados > Dicionário > Base de dados.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33778302837655)

**2)** Filtre pela tabela CIX (Regra de Códigos de Prestação de Serviço):

Cabeçalho da Regra de ISS (CIX):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33778302839063)

Ajuste a consulta padrão na aba Opções para a tabela CCQ:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/33778269606551)**

Na Aba Validações, ajuste o campo Val. Usuário = Vazio() .Or. ExistCpo('CCQ') informando manualmente, sem realizar o procedimento de copiar e colar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36640441636119)

**3)** Filtre a tabela CIO (Perfil de Operação aba Código de Serviço)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33778302840087)

Ajuste a consulta padrão na aba Opções para a tabela CCQ:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33778269607703)

Na Aba Validações, ajuste o campo Val. Usuário = Vazio() .Or. ExistCpo('CCQ') informando manualmente, sem realizar o procedimento de copiar e colar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36640441637911)

4) Atualize a Base de Dados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33778269608215)

Após o ajuste nas tabelas CIO e CIX e atualização da base de dados, o código de serviço no Perfil de Operação e Regra de Código de Prestação de Serviço irão buscar os códigos da tabela CCQ.

**Documentações relacionadas:**

[DSERFISE-12074 DT Não permite utilizar a tabela CCQ como consulta padrão no campo CIO\_CODISS](https://tdn.totvs.com/pages/releaseview.action?pageId=946409240)

[Cadastro de Código de Serviço do ISS - Fiscal - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=642630535)

[CFGTRIB - Configurador de Tributos](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos+-+12.1.22.10)

[CFGTRIB - Cálculos no Configurador de Tributos](https://tdn.totvs.com/pages/viewpage.action?pageId=676039354)
