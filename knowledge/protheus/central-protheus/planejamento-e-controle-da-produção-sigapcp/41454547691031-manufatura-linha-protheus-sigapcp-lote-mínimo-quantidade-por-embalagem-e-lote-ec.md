---
article_id: 41454547691031
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 99c940b759b042a7951ca7ddd6ea2364343ba00cbf152652da7634063f3756c6
fetched_at: '2026-06-28T22:42:43.544106+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Lote mínimo, quantidade por embalagem
  e lote econômico
type: support-article
updated_at: '2026-06-26T17:50:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41454547691031-Manufatura-Linha-Protheus-SIGAPCP-Lote-m%C3%ADnimo-quantidade-por-embalagem-e-lote-econ%C3%B4mico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41454535951383) Tempo aproximado para leitura: **00:02:04 min**  
  
**Dúvida**  
Ao gerar uma solicitação de compra ou ordem de produção pelo **MRP** ou **MATA650** quais informações do **MATA010**, **MATA018** ou **MATA019** são levadas em consideração para determinar quanto será comprado ou produzido?  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Para produtos comprados e com o parâmetro **MV\_ARQPROD** com o conteúdo **SBZ**, as informações registradas nos campos **BZ\_QE** e **BZ\_LE** são levadas em consideração. Já quando o parâmetro **MV\_ARQPROD** tem o conteúdo **SB1** ou não existe informação para o produto na tabela **SBZ,** as informações consideradas são as dos campos **B1\_QE e B1\_LE**  
Já para produtos produzidos e com o parâmetro **MV\_ARQPROD** com o conteúdo **SBZ**, as informações consideradas são as dos campos **BZ\_LM e BZ\_LE.** Já quando o parâmetro **MV\_ARQPROD** tem o conteúdo **SB1** ou não existe informação para o produto na tabela **SBZ**, as informações consideradas são as dos campos **B1\_QE** e **B1\_LE.**  
  
**Saiba mais**  
**Para mais informações do cálculo realizado acesse a documentação** [**Cálculo das necessidades de produção/compras**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058709693-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-das-necessidades-de-Produ%C3%A7%C3%A3o-Compras)  
  
**Glossário**  
**MRP** - Material Requiriments Planning  
**MATA650** - Cadastro de ordem de produção   
**MATA010** - Cadastro de produtos  
**MATA018** - Indicadores de produtos  
**MATA019** - Indicadores de produtos modelo 2  
**MV\_ARQPROD** - Indica se os dados de indicadores de produto serão considerados pela tabela SB1 ou se serão considerados pela tabela SBZ  
**BZ\_QE** - Quantidade por embalagem  
**BZ\_LM** - Lote mínimo  
**BZ\_LE** - Lote econômico  
**B1\_QE** - Quantidade por embalagem  
**B1\_LE** - Lote econômico  
**B1\_LM** - Lote mínimo
