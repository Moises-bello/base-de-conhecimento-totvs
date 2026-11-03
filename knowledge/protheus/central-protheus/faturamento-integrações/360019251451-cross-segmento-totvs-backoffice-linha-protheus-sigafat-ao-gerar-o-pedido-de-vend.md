---
article_id: 360019251451
category: Faturamento - Integrações
content_hash: e9bb94cc22097209cf219c36511c63bbe2daadadcbbde89652432761a75a5982
fetched_at: '2026-06-28T22:38:26.392577+00:00'
product: protheus
section_id: 1500001539261
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Ao gerar o pedido
  de vendas com integração com GFE a tabela GWB não é criada
type: support-article
updated_at: '2021-11-24T17:59:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019251451-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Ao-gerar-o-pedido-de-vendas-com-integra%C3%A7%C3%A3o-com-GFE-a-tabela-GWB-n%C3%A3o-%C3%A9-criada
---

**Duvida**  
Ao gerar o pedido de vendas com integração com **GFE** a tabela **GWB** não é criada.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Essa tabela e alimentada no momento da geração da nota de saída quando só campos (**C5\_VOLUME1** e **C5\_ESPECIE1**) e subsequentes (**VOLUME2**, **ESPECIE2**) estão preenchidos corretamente.  
Se apenas um deles estiver preenchido ou nenhum dos dois a informação não e gravada na **GWB**.

Para que o campo **"GWB\_CDUNIT"** seja gravado, é necessário que a espécie informada no **Pedido de Venda** esteja cadastrada na rotina de **"Cadastro de Unitizadores de Carga (GFEA043)"** do módulo do **SIGAGFE**.

Os Unitizadores do **SIGAGFE** correspondem ao campos de **Espécie** que estão na nota de saída/entrada do ERP Protheus. Cada Espécie é um Unitizador no Documento de Carga. Se a Espécie não estiver cadastrada como Unitizador no GFE, não vai ocorrer nenhuma mensagem de validação no momento da integração, mas também não será gravado o Unitizador no Documento de Carga, fazendo com que o sistema considere a soma das quantidades dos itens para gravação da Quantidade de Volumes.

**Observação** O sistema sempre busca os dados da tabela **SC5**, ele não olha a **SF2** mesmo se nos campos da **SF2** estiver preenchido corretamente.

Para mais detalhes da Integração, conheça nossa FAQ Faturamento X GFE no Link abaixo:

**[Principais ocorrências da Integração Protheus Faturamento X GFE](https://tdn.totvs.com/x/RbMbF)**
