---
article_id: 6571581773847
category: Gestão organizacional
content_hash: e991f98b20650dc11c95aa14cf62babf9a365c0ede67d976873d37bfd1186d9e
fetched_at: '2026-06-28T22:47:22.297333+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Hierarquia por Posição: Criar posições da hierarquia'
type: support-article
updated_at: '2025-11-19T19:39:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6571581773847-RH-RM-RHU-Hierarquia-por-Posi%C3%A7%C3%A3o-Criar-posi%C3%A7%C3%B5es-da-hierarquia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15864365484951) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como é feito o cadastro de posições da hierarquia?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.34** e **superiores**  
  
**Solução**

Para criação, acesse no Módulo de **Gestão de Pessoas** | **Gestão Organizacional** | **Posição.**

Nesta rotina será criado as posições de cada funcionário, isto é, cada funcionário ocupará uma posição dentro da hierarquia e para a associação à hierarquia, será validada a posição, não o funcionário.

O cadastro de posição deverá ser criado para todos os funcionários e o mesmo pode ser realizado manualmente na visão ou automaticamente no processo de **Criar Posição por Funcionário**quando o sistema estiver parametrizado para **'Permite Informar dados no Cadastro de Funcionário e na Posição'.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26790217762199)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26790217767831)**

Sobre o tipo de posição, atualmente possuímos dois tipos de posições que podem ser ocupadas, a posição **Oficial**, isto é, a posição a qual a pessoa está lotada permanentemente e a posição **Réplica**,esta posição é um cadastro temporário o qual pode servir como um substituto para um chefe temporário.

Os cadastros feitos manualmente serão do tipo oficial, para gerarmos uma posição de replica, será necessário selecionar a posição que deseja substituir e executar o processo **Réplica de Posição**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26790217772311)

Sobre o parâmetro **Marca Ponto**, poderá ser informado Marca Ponto na posição, ou seja, o funcionário que assumir a posição passará a Marcar Ponto. Caso ao inserir o funcionário na posição, seja informado que os dados do funcionário serão mantidos, o campo será atualizado com o dado original do cadastro do funcionário.

O cadastro de Posição, buscará os dados de Sálario, Seção e função do funcionário e dependendo do parâmetro marcado em **Configuração | Parametrizador | Gerenciamento de Hierarquia | Parâmetros Referente à Funcionário**pode ou não ser liberado a edição e cadastro das informações deste funcionário pela posição.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6571189213079)

Após o cadastro da hierarquia, será possível dentro do cadastro de **Posição | Anexo | Hierarquias da Posição**determinar à qual hierarquia será vinculada esta posição. É possível também controlar através deste anexo os históricos das hierarquias anteriores, onde se é possível marcar e desmarcar a opção **Status** de acordo com a necessidade de vocês.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6571430445591)

**Saiba mais**Para maiores informações sobre as informações, acesse:

- [Posição](https://tdn.totvs.com/pages/releaseview.action?pageId=655455281)
