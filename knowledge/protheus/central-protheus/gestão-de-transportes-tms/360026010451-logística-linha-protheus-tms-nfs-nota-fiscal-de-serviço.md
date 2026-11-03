---
article_id: 360026010451
category: Gestão de Transportes (TMS)
content_hash: e0d7ab52c093c972a02c153559f3ef9fc21d0023ed707433a94726f2edf6b958
fetched_at: '2026-06-28T22:45:29.459673+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - NFS Nota fiscal de Serviço
type: support-article
updated_at: '2026-04-06T11:15:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026010451-Log%C3%ADstica-Linha-Protheus-TMS-NFS-Nota-fiscal-de-Servi%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20880761053079) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como emitir **NFS - Nota Fiscal de Serviço de Transporte** por meio do **SIGATMS**?  
  
**Ambiente**  
TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**  
Para emissão de Nota Fiscal de Serviço pelo **SIGATMS - Gestão de Transportes**, temos os seguintes cadastros:  
  
**MATA010** **- Produto:**Cadastrar um produto de Cálculo de **ISS - Imposto Sobre Serviços**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026096891)

**TMSA150** **- Configuração de Documentos:**Criar um tipo de documento igual a **5 - NOTA FISCAL**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026096931)

Por meio do Configurador **- SIGACFG/Base de dados/Dicionário/Base de dados/Tabelas Genéricas/L4**, que pertence a tabela SX5, cadastrar o **tipo de serviço**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026097071)

Ainda no Configurador - **Ambiente/Cadastros/Parâmetros/** Informar a serie cadastrada anteriormente no parâmetro **MV\_ESPECIE** igual a **RPS**. Neste exemplo, 099=**RPS.** Caso seja informado uma espécie diferente de **RPS**, então, ao realizar o estorno do calculo do frete, os registros nas tabelas **SFT** e **SF3** serão deletados.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28211573136151)**

**DLGA070 - Serviços x Tarefas:**Cadastrar um Serviços x Tarefas com esse tipo de documento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026098892)

**MATA080 - Tipos de Entrada e Saída**: Cadastrar uma TES - Tipo de entrada e saída para calcular ISS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026109791)

**TMSA410 - Regras de Tributação:** Criar uma Regra de tributação para TES criada anteriormente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026097191)

**TMSA600 - Regras de Tributação por Cliente:** Criar uma Regra por cliente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026097171)

**TMSA115 - Grupo de região:** Definir as alíquotas internas de ISS para cada região no cadastro de estrutura.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360026097411)

**TECA250 - Contrato de Prestação de Serviços:** Informar o serviço cadastrado acima.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027709771)

A geração da Nota Fiscal de Serviço de transporte é realizada no **SIGATMS**, porém, para casos quando houver a necessidade de transmissão à prefeitura, então, a transmissão será realizada pela rotina **FISA022** **- NFS-e.**  
  
Será necessário verificar se o município da filial que fará as transmissões está homologado no **TSS - TOTVS Sped Service**. Maiores informações acessar link abaixo:  
[Cross Segmentos - Linha Datasul - NFSE - IMPLANTAÇÃO DE NFSE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006652632-MP-NFSE-IMPLANTA%C3%87%C3%83O-DE-NFSE)  
  
Com relação à dúvidas na transmissão da **NFS-e** para a prefeitura, entrar em contato com equipe  **Protheus SPED**.
