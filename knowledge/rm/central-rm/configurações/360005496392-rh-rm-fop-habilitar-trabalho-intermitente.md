---
article_id: 360005496392
category: Configurações
content_hash: fe8dc5d192dc3bd6269be56e3d1c90931b3409a1a086056ddcc06d37d32635a4
fetched_at: '2026-06-28T22:46:49.673073+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Habilitar trabalho intermitente
type: support-article
updated_at: '2025-03-06T19:34:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005496392-RH-RM-FOP-Habilitar-trabalho-intermitente
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:20 min****Dúvida**Como devo preparar o meu sistema para utilização do Regime de Contrato Intermitente?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Siga os passos abaixo para preparar seu sistema para trabalhar com o regime de Contrato Intermitente:

1. O sistema deverá estar em uma das versões de mercado;
2. Execute o RM.Atualizador.exe (C:\TOTVS\CorporeRM\RM.Net);
3. Caso ainda não esteja habilitado, habilitar o parâmetro da reforma trabalhista em **Configurações | Parâmetros | Parametrizador | Folha Normal | Geral** e marcar o parâmetro **Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017**;
4. Habilitar o uso do regime intermitente no Parametrizador do TOTVS Folha de Pagamento em **Configurações | Parametrizador | Funcionário | Trabalho Intermitente** e marcar o parâmetro **Usa Trabalho Intermitente**;
5. É Necessário que seja informada a quantidade de caracteres para a parametrização da **Máscara para Código de Convocação**, conforme print abaixo.  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10591085149079)

Além dos procedimentos descritos acima, é necessário conceder permissão aos usuários responsáveis por cadastrar as convocações. Esta permissão deve ser concedida no cadastro de funcionários, pois o cadastro de convocação é encontrado em seus anexos.  
  
**Importante**Para mais informações sobre os cadastros do Regime de Contrato Intermitente e como parametrizar suas funções, veja o link: [Convocação para trabalho intermitente](http://tdn.totvs.com/pages/releaseview.action?pageId=364924305)
