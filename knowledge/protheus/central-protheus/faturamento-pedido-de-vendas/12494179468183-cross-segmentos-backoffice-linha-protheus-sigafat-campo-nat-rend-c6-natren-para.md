---
article_id: 12494179468183
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 289f10dac96115284952b37b11afde615f285cbde4d229e4dd16e427df3d17ed
fetched_at: '2026-06-28T22:38:42.464780+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Campo "Nat. Rend."
  (C6_NATREN) para REINF 2.1.2
type: support-article
updated_at: '2024-02-02T19:55:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12494179468183-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Campo-Nat-Rend-C6-NATREN-para-REINF-2-1-2
---

**Dúvida**Campo "Nat. Rend." (**C6\_NATREN**) da rotina Pedidos de Venda, utilizado para informar o código de Natureza de Rendimento.  
  
**Ambiente**Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Veja o Evento que realizamos sobre o tema através do link: [Webinar | MP - SIGATAF - Evento: Processo EFD REINF](https://youtu.be/Miy-B10g_CM?si=DD4TQiITQFByJwsi)

* O campo "Nat.Rend." (C6\_NATREN) está disponível oficialmente a partir do Pacotes de Atualização do Faturamento, disponível no link: **[Pacotes de Atualização - Faturamento](https://tdn.totvs.com/x/Iw4dHw)**
* Assista nosso **vídeo** demonstrando o processo de configuração e uso: **[Configuração do REINF (SIGAFAT)](https://youtu.be/4fpGg7xealI)**
* Para que o campo seja preenchido automaticamente, siga as orientações da documentação: [**Preenchimento automático da Natureza de Rendimento**](https://tdn.totvs.com/x/WhuLL)
* Caso alguma das informações solicitadas nos eventos da serie R-4000 tenham sido inseridas no Backoffice Protheus antes da atualização do ambiente para a EFD-Reinf 2.1.1, será necessário atender a uma das opções abaixo:

  + Incluir a informação novamente no sistema atendendo as pré-condições necessárias para o envio dos eventos R-4000;
  + [Executar a funcionalidade "FIXREINF"](https://tdn.totvs.com/x/4t7rL);
  + [Lançar os dados diretamente no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14823862934807-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-integrar-o-evento-R-4080-manualmente-no-TAF-);
* Para saber qual registro da tabela "Impostos x Natureza Rendimento" (FKW) foi gerado pela nota fiscal, é possível validar a amarração entre nota e FKW na "Tabela Auxiliar" (FK7)
* Help: NATREN:
  + [Funcionamento do parâmetro MV\_FATNATR](https://totvssuporte.zendesk.com/knowledge/editor/01HNMV5HVB9N8QNPY0P0Y08X6W/pt-br?brand_id=1509248&return_to=%2Fhc%2Fpt-br%2Farticles%2F21067226242199)
  + [Help: NATREN na inclusão do Pedido de Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17687168113047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-NATREN-na-inclus%C3%A3o-da-Natureza-de-Rendimento-no-Pedido-de-Venda)

**Observação**: Para criação das tabelas e o campo é necessário executar o UPDDISTR com a aplicação do Dicionário Diferencial (SDF), disponibilizado no pacote de **BACKOFFICE**;

**Saiba mais**:

* [EFD - REINF](https://tdn.totvs.com/x/epkPEw)
* [DT - NF x Naturezas de Rendimento - Gravação da tabela FKW](https://tdn.totvs.com/x/CdarKw)
