---
article_id: 21023071404823
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 25ef0f70c9647765f75795006fca449b006e271af38dd157ba7ec51e8a8d33c1
fetched_at: '2026-06-28T22:42:02.676003+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Geração do Registro
  0221.
type: support-article
updated_at: '2024-02-01T19:04:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21023071404823-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Gera%C3%A7%C3%A3o-do-Registro-0221
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21023058182935) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida:**

Como gerar o registro 0221, no arquivo do Sped Fiscal ano 2024.

**Ambiente:**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12.1.33

**Solução:**

Para geração do registro 0221 do EFD ICMS/IPI, será necessário aplicar o pacote da expedição contínua do módulo de estoque para criação da tabela D4C e adicionar a rotina MATA039 no menu para cadastro da especificação de produtos e o pacote da expedição do fiscal para atualização das fontes SPEDFISCAL e SPEDXFUN.

Pacote da expedição contínua do estoque e fiscal, para realizar da atualização e execução do **UPDDISTR**.

**12.1.33 (Garantia contínua):**  
Estoque:  <https://suporte.totvs.com/portal/p/10098/download?e=1039086>  
Fiscal:  <https://suporte.totvs.com/portal/p/10098/download?e=1039088>  
**12.1.2210:**  
Estoque:  <https://suporte.totvs.com/portal/p/10098/download?e=1080339>  
Fiscal:  <https://suporte.totvs.com/portal/p/10098/download?e=1080345>

**12.1.2310:**  
Estoque:  <https://suporte.totvs.com/portal/p/10098/download?e=1123875>  
Fiscal:  <https://suporte.totvs.com/portal/p/10098/download?e=1123881>

**Atenção:**  
Após o pacote da expedição contínua já gerada, a equipe de produtos identificou que houve um defeito em relação à geração do **registro 0221** quando o tamanho do **código do produto** (B1\_COD) é menor que o tamanho do **campo B1\_COD**.  
   
Exemplo: **B1\_COD tamanho 15** e conteúdo do código do produto = 00239. Quando isso acontecer, poderá ocorrer duplicidade na geração do **registro 0221**.  
   
Como não houve tempo hábil para inclusão desta correção no pacote da expedição contínua, caso este incidente ocorra, será necessário aplicar o pacote pontual do **SPEDFISCAL e SPEDXFUN** após aplicar os pacotes da expedição contínua:

Pacote de atualização **SPEDFISCAL e SPEDXFUN.**

12.1.2210: <https://suporte.totvs.com/portal/p/10098/download?e=1134737>  ;  
12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1134738>  ;  
12.1.33 (Garantia Estendida): <https://suporte.totvs.com/portal/p/10098/download?e=1134742>  ;

**Documentação:**

[https://tdn.totvs.com/pages/releaseview.action?pageId=816317717](https://tdn.totvs.com/display/public/PROT/SPDFIS+-+Sped+Fiscal#SPDFISSpedFiscal-Bloco0-Abertura,Identifica%C3%A7%C3%A3oeRefer%C3%AAncias)

<https://tdn.totvs.com/display/public/PROT/SPDFIS+-+Sped+Fiscal#SPDFISSpedFiscal-Bloco0-Abertura,Identifica%C3%A7%C3%A3oeRefer%C3%AAncias>
