---
article_id: 360037420754
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 96598b7a4052ebc4e5556db4b8773b5fffcf4a1a576b98b3b242df355f31990e
fetched_at: '2026-06-28T22:42:02.280188+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar os registros G110, G125, G130 e G140 via rotina de Manutenção CIAP
type: support-article
updated_at: '2025-02-11T21:13:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037420754-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-os-registros-G110-G125-G130-e-G140-via-rotina-de-Manuten%C3%A7%C3%A3o-CIAP
---

**Dúvida**Como gerar os registros G110, G125, G130 e G140 via rotina de Manutenção CIAP (**MATA905**)?  
   
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 11.80  
   
**Solução**  
 Para solucionar essa dúvida, realize os seguintes passos:  
  
 1. Para o correto preenchimento dos campos dos registros do bloco G, realize a criação dos campos abaixo no Protheus:

Exemplo para criação dos campos na rotina Manutenção CIAP.  
  
Para inclusão do código do item é necessário criar um novo campo (F9\_ITEMNF2) na tabela SF9 para que a informação seja gerada corretamente no Sped Fiscal.  
Campo: F9\_ITEMNF2  
Tipo: Caracter  
Tamanho: 3  
Decimal: 0  
Formato: @!  
Contexto: Real  
Titulo: Num Item SPD  
Texto: Incluir item nf entrada   
Help: Incluir numero do item da nota fiscal de entrada para alimentar o campo 02\_NUM\_ITEM do registro G140 SPED FISCAL.

Campo: F9\_CODPROD  
Tipo: Caracter  
Tamanho: 30  
Decimal: 0  
Formato: @!  
Contexto: Real  
Titulo: Cod Prod SPD  
Texto: Informa codigo do produto  
Help: Informa codigo do correspondente ao bem no documento fiscal, preenchimento do campo 03\_COD\_ITEM G140 SPED FISCAL.

Campo: F9\_CC  
Tipo: Caracter  
Tamanho: 9  
Decimal: 0  
Formato: @!  
Contexto: Real  
Titulo: C. Custo     
Texto: Informa centro de custo  
Help: Informação do centro de custo para preenchimento do campo 02 COD\_CCUS registro 0305 SPED FISCAL.

Campo: F9\_PL  
Tipo: Caracter  
Tamanho: 20  
Decimal: 0  
Formato: @!  
Contexto: Real  
Titulo: C. Contábil      
Texto: Informa conta contábil    
Help: Informa contata contábil da tabela CT1 plano de contas para preenchimento do campo 06 COD\_CTA registro 0300  SPEDFISCAL.  

    
2.Realize a amarração dos campos nos parâmetros:

MV\_F9ITEM = F9\_ITEMNF2  
MV\_F9PROD = F9\_CODPROD  
MV\_F9CC = F9\_CC  
MV\_F9PL = F9\_PL

3. Inclua o ativo no sistema através da rotina Manutenção CIAP (**MATA905**).

![BLOCO_G_-_inclusao_bem_sf9.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049944813/BLOCO_G_-_inclusao_bem_sf9.gif)

Obs.: O número do item deverá ser informado no campo criado (F9\_ITEMNF2). Caso o campo F9\_ITEMNFE seja preenchido, o sistema tentará validar a nota fiscal de entrada que nesta caso não foi lançada no sistema.

4. Após a inclusão do bem realize a apropriação através da rotina Estorno CIAP (**MATA906**).

**Importante:**  
Deve ser informado sempre o último dia do mês para geração da apropriação do crédito CIAP para gravação das informações na tabela SFA. Após a apropriação, verifique se as informações foram gravadas corretamente na tabela mencionada.

![BLOCO_G_-_apropriacao_sf9.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049946633/BLOCO_G_-_apropriacao_sf9.gif)

Com a correta apropriação a legenda do bem ficará VERDE.  
Caso existam dúvidas ou problemas com relação a este procedimento, por favor, consulte nossa equipe de suporte Escrita Fiscal e Relatórios.

![sf9_bem_apropriado.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360049059574/sf9_bem_apropriado.JPG)

5. Acesse a rotina Sped Fiscal e gere o arquivo.

![BLOCO_G_-_sped_sf9.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360049946953/BLOCO_G_-_sped_sf9.gif)
