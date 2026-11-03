---
article_id: 360010161372
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: dea848a507eac4fcb7b24cd0a404a46916a0a241f08b2e7bdc0be3302455dd78
fetched_at: '2026-06-28T22:42:02.409021+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro C115: Local da Coleta e/ou entrega'
type: support-article
updated_at: '2025-02-11T21:27:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010161372-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-C115-Local-da-Coleta-e-ou-entrega
---

**Dúvida**  
Como gerar o registro C115: Local da Coleta e/ou entrega (Código 01, 1B e 04).  
  
**Ambiente**  
Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Configure o parâmetro **MV\_CONV115 = .F.** ;  
  
2. Efetue o lançamento da nota fiscal de saída com espécie NFE ou NF (modelo 01) com conteúdo do campo Cliente (**C5\_CLIENTE**) = 001 e campo Cli.Entrega (**C5\_CLIENT**) = 002;

No exemplo abaixo o cliente de coleta deve ser diferente do cliente de entrega.

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-55-55.png?version=1&modificationDate=1525460156000&api=v2)

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-56-55.png?version=1&modificationDate=1525460215000&api=v2)

3. Após faturar documento de saída, realize o complemento do Documento fiscal;  
**Caminho:**Módulo de Livros Fiscais > Atualizações > Movimentos> Nf. Entrada Manual ou Nf. Manual de Saída;  
  
4. Selecione a Nota Fiscal;   
  
5. Acesse o botão Ações Relacionadas > Complemento> Locais de Coleta e Entrega (**Tabela CDF)**;

**![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_15-59-27.png?version=1&modificationDate=1525460368000&api=v2)**

**![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_16-0-23.png?version=1&modificationDate=1525460424000&api=v2)**

Obs.: Para gerar o registro C115 é preciso gerar o C110 (**INFORMAÇÃO COMPLEMENTAR DA NOTA FISCAL**):

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_16-1-18.png?version=1&modificationDate=1525460479000&api=v2)

6. Na **geração do Arquivo** SPED FISCAL, marque como ‘SIM’ a opção “**GERAR REGISTRO COMPLEMENTARES DE FRETE”**.

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_16-2-9.png?version=1&modificationDate=1525460529000&api=v2)  
  
Registro gerado:

![](http://tdn.totvs.com/download/attachments/238035285/image2018-5-4_16-3-26.png?version=1&modificationDate=1525460606000&api=v2)

**Importante: Complemento de Nota Fiscal Automático**   
Ponto de Entrada MATUCOMP: Utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais. Para informações sobre o Ponto de entrada MATUCOMP, acesse: [MATUCOMP - Alterações automáticas.](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107)O parâmetro **MV\_ATUCOMP** deve ser configurado para que seja possível utilizar o **Ponto de Entrada MATUCOMP (MV\_ATUCOMP = T)**.
