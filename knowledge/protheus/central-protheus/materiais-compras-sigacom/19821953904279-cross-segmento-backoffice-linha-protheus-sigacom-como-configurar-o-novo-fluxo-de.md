---
article_id: 19821953904279
category: Materiais - Compras (SIGACOM)
content_hash: 147683966cd58b2f25b459fcdc5268c053363b6c6eec1c0bed575a48cef82435
fetched_at: '2026-06-28T22:41:10.541936+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Como configurar o
  Novo Fluxo de Compras - NFC (PGCA010)?
type: support-article
updated_at: '2025-03-17T20:23:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19821953904279-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Como-configurar-o-Novo-Fluxo-de-Compras-NFC-PGCA010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19821910150295) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como configurar o novo fluxo de compras - NFC (PGCA010)?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras/GCT - Protheus Release 12.1.2210.

**Solução:**

Para iniciar a implantação do NFC devemos atender alguns **Requisitos**:

- Release superior a versão 12.1.2210 **(Obrigatório);**

- LIB do Framework Protheus® igual ou superior a data de 27/02/2023 que pode ser baixada no endereço: [LIB-download](https://suporte.totvs.com/portal/p/10098/download#detail/1050526) **(Obrigatório);**

- Último pacote da **[Expedição Contínua](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)**do Compras **(Obrigatório);**

**-** Atualização do dicionario de dados disponivel na última **[Expedição Contínua](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)** **(Obrigatório);**

**Configurações:**

Após atender todos requisitos listados acima, é necessario executar algumas configurações no ambiente:

**-** Na seção GENERAL do appserver.ini, deve-se incluir a chave **“App\_Environment”**, cujo valor deve ser o nome do ambiente onde os serviços serão executados, exemplo:

*[General]*  
*App\_Environment=Nome\_Do\_Ambiente*

- Na seção DRIVERS,  deve-se habilitar a porta **multiprotocolo** na chave “**MultiProtocolPort”** com o valor = **1,** exemplo:

*[Drivers]*  
*Active=TCP*  
*MultiProtocolPortSecure=0*  
*MultiProtocolPort=1*

**Observação**: Por padrão a conexão **SSL** está ativa na porta **multiprotocolo**, os detalhes das configurações estão disponíveis na documentação Application Server - Porta Multiprotocolo. Para desabilitar a conexão por SSL é necessário informar a chave “**MultiProtocolPortSecure = 0”,** para maiores informações sobre essa configuração, [clique aqui.](https://tdn.totvs.com/display/tec/Application+Server+-+Porta+Multiprotocolo)

- Adicione ao menu do Compras a rotina PGCA010 através do SIGACFG para acesso ao NFC via menu do Protheus.

![Untitled design.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19859014135959)

- Parabéns! Seu novo NFC está pronto para uso. Para aprender a configurar o Workflow e aproveitar ao máximo essa nova ferramenta, [clique aqui!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19823527070871)**Importante**, essa é uma configuração tradicional do workflow centralizando todas cotações em uma unica caixa de e-mail!

Sabia que é possivel realizar uma **configuração especial no workflow** para que cada comprador tenha sua propria caixa de e-mail? Tornando o processo de cotação totalmente exclusivo do comprador, [clique aqui e aprenda como realizar essa configuração!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19837259521559)

Para maiores informações sobre o NFC acesse: [Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

**SAIBA MAIS EM :**

**[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)**

**[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)**
