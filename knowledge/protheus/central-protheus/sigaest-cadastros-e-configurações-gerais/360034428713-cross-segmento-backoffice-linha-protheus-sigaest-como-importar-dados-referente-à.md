---
article_id: 360034428713
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 453fd65fd9366d3fdb9a0c6315396c87584fe27e3d31b7f2604b32b4f33f9bc8
fetched_at: '2026-06-28T22:39:08.150210+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como importar dados
  referente à Movimentação de Estoque no Protheus?
type: support-article
updated_at: '2024-04-01T18:31:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034428713-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-importar-dados-referente-%C3%A0-Movimenta%C3%A7%C3%A3o-de-Estoque-no-Protheus
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22148724608663) Tempo aproximado para leitura: 00:04:00 min**

**Dúvida**

Como importar dados referentes a Saldos de Estoque no Protheus?  
  
**Ambiente**

Microsiga Protheus – Estoque – A partir da versão 11.80

**Solução**

Existem momentos em que o usuário necessita alterar uma grande quantidade de informações e preferem informar esses dados importando os registros ao invés de editar um a um, por exemplo registros da tabela **SD3** (Movimentos Internos). Desta forma, o Protheus disponibiliza a rotina de **Importação de Dados** localizado em **Miscelânea > Arquivos > Importação de Dados**. Caso não tenha no menu, abaixo um passo a passo para inclusão da rotina no Menu, **é necessário que o RDMAKE esteja compilado no ambiente para acessar a rotina Importação de Dados**.

Para que a importação de dados ocorra, é necessário compilar o RDMAKE - MATAIMP e assim esse fonte poderá adequar a necessidade da empresa, para que somente os dados necessários da tabela sejam importados.   
  
Para saber mais sobre o MATAIMP, **[clique aqui.](http://tdn.totvs.com/pages/releaseview.action?pageId=6087653)**

**Observações**: Faça o download dos includes que estão anexo abaixo.

**Abaixo o passo a passo para incluir a rotina MATAIMP no Menu do Módulo Estoque Custos.**

![MATAIMP.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/22483432538775)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22483199095191)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*

*[SIGAEST - MATA241 - Como configurar a rotina movimentação multipla via Mile?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20687093055639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA241-Como-configurar-a-rotina-movimenta%C3%A7%C3%A3o-multipla-via-Mile?source=search)*
