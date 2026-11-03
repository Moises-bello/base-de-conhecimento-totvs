---
article_id: 360027265791
category: RH - Integração de Titulo
content_hash: 9352f56c967828688eefe49e61c935bd0fb01603c8c7106da3d49ab5303a5b71
fetched_at: '2026-06-28T22:43:36.189117+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar e conferir um título de adiantamento
  quinzenal
type: support-article
updated_at: '2025-07-15T18:03:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027265791-RH-Linha-Protheus-GPE-Como-configurar-e-conferir-um-t%C3%ADtulo-de-adiantamento-quinzenal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33487081607575)**Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como configurar e conferir um título de adiantamento quinzenal  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1) Acesse Miscelânea -> Títulos -> Definição:  
  
![10.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026784411)

2) Preencher os campos da definição de título:  
**Atenção:** os campos preenchidos no exemplo abaixo são meramente ilustrativos.   
  
![11.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360026791051)  
  
3) No canto inferior direito, clicar em "Definir Título" para selecionar a verba e a tabela que buscará a informação:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16760626968855)  
  
4)  Na definição de título, especificar a verba para geração (verba líquido de adiantamento = ID 0546) e a tabela para busca dos valores.   
No exemplo abaixo, apresentamos a verba de ID 0546 e a busca na tabela SRC - Movimento do período, uma vez que o movimento de adiantamento ainda não foi fechado:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16760532857239)

**RC\_DATA - Sistema efetuará a busca de dados do roteiro ADI da tabela SRC, campo Dt. Pgto, de acordo com os parâmetros de geração, nas perguntas Dt. Busca Pagto De e em Dt Pagto Até**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16775843133207)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16759595688727)   
  
**RC\_DTREF -Sistema efetuará a busca de dados do roteiro ADI da tabela SRC, campo Dt. Ref, de acordo com os parâmetros de geração, nas perguntas Dt. Busca Pagto De e em Dt Pagto Até**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16760425493655)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16775856839831)  
  
6) Após a criação do título, verificar no resumo de folha de pagamento , os valores calculados referentes à verba indicada na definição de título:   
Acesse: Relatórios -> Periódicos -> Folha de Pagamento  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16760498336791)

A mesma configuração é validada se utilizada a tabela SRD - Movimento Fechado  
  
6) Acessar Miscelânea -> Títulos -> Geração, configurando os campos de acordo com a definição de título e datas de geração.  
  
7) Verificar na manutenção de títulos, o título gerado com o valor de acordo com o resumo de folha:  
Acessar: Miscelânea ->títulos -> Manutenção  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16760588273559)  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
