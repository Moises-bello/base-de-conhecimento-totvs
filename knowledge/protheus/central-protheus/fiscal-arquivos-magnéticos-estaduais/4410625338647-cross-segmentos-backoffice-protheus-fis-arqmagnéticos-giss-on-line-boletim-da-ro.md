---
article_id: 4410625338647
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 01ac3d14d0d8cf616431811346c1e8a3d6108ec9e55f012e0f036fba7a96a81b
fetched_at: '2026-06-28T22:42:11.661482+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GISS ON LINE
  - Boletim da rotina Giss Online
type: support-article
updated_at: '2024-05-24T18:40:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410625338647-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GISS-ON-LINE-Boletim-da-rotina-Giss-Online
---

**Dúvida**

**GISS On Line -** Como configurar a rotina para geração do arquivo **GISS ON LINE?**  
  
**Ambiente**TOTVS Backoffice (Linha Protheus) – Livros Fiscais –  A partir da versão **12.1.25.**  
  
**Solução**

Está disponível na rotina Instruções Normativas (**MATA950**), a geração do arquivo para importação da **GISS online** – Guia de Informação de ISSQN.  
No dia 01/09/2021 a plataforma **GISS Online** mudou a forma de validação dos arquivos de remessa, deixando o *Layout* único com 38 posições obsoleto e passando a validar o *layout* através dos campos obrigatórios de acordo com a modalidade de entrega.

Abaixo a imagem extraída do Manual da **GISS ONLINE** , que esta disponível <https://portal.gissonline.com.br/> no quadro de "Acesso Fácil - Dicas de Acesso / Manual de Operação"

![](https://tdn.totvs.com/download/attachments/643306559/image2021-10-4_17-37-17.png?version=1&modificationDate=1633379837783&api=v2)

Cada modalidade acima, tem um *layout* de campos obrigatórios para serem atendidos na geração do arquivo, para maiores detalhes verifique o link: [*Layout* da Interface](https://portal.gissonline.com.br/help_portal/manuais/layouts.zip)

**\*\*** Com isso, na rotina **MATA950** é preciso utilizar o **arquivo INI** conforme a modalidade **.**

**PROCEDIMENTO COMPLETO PARA CONFIGURAÇÃO:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=643306559>

Arquivos INIs em anexo.

##
