---
article_id: 4415054346519
category: Configurações
content_hash: 9f2cb6fdf3f70549d48ef038abee4c372c1c2a6875baa54d1b90116836fc8cf5
fetched_at: '2026-06-28T22:46:49.554855+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - Erro  String was not recognized as a valid DateTime na importação
  de histórico de seção
type: support-article
updated_at: '2025-03-05T18:51:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415054346519-RH-RM-FOP-Erro-String-was-not-recognized-as-a-valid-DateTime-na-importa%C3%A7%C3%A3o-de-hist%C3%B3rico-de-se%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:15 min****Ocorrência**Ao realizar a importação de dados do histórico de seção, ocorre o erro **String was not recognized as a valid DateTime**.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro ocorre devido à digitação incorreta do DateTime, formato usado pelo layout. Veja abaixo um exemplo **incorreto**:  
  
Layout:  
**70347;01022021 000000;3;07.01.04**  
Erro:  
**Linha <1> - Erro ao realizar importação de Histórico de Seção:**  
**String was not recognized as a valid DateTime.**No exemplo acima, o layout desrespeita a estrutura proposta pelo layout, ficando com 15 caracteres ao invés de 17, pois não foram inseridos os dois pontos que separam as horas dos minutos e os minutos dos segundos.   
  
**Solução**Para solucionar esse problema, será necessário ajustar o Layout com o formato correto de DateTime. Exemplo de layout **correto**:  
  
**00001;01031990 00:00:00;01;01.03**  
Feita a correção do seu layout, Importe no caminho **Configurações | Importação de Dados da Folha de Pagamento**:

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10960656939799)  
  
Saiba mais**Para acessar a estrutura do layout de Histórico de Seção, [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=452719255).
