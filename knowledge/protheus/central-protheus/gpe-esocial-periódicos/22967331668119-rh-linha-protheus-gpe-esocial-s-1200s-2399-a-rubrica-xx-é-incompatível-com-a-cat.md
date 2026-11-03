---
article_id: 22967331668119
category: GPE - eSocial - Periódicos
content_hash: 5e5da38b07d63d1ddd0a21b16faac7fc6fadd6b916d849378512406f0f36c500
fetched_at: '2026-06-28T22:45:07.366812+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200/S-2399: A Rubrica xx é incompatível
  com a categoria xxx do trabalhador. Rubricas de incidência de IRRF iguais a [14,
  34, 54, 94, 9024, 9034, 9054, 9834] só são aceitas para categoria do grupo empregado
  [1xx]'
type: support-article
updated_at: '2024-04-22T12:10:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22967331668119-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2399-A-Rubrica-xx-%C3%A9-incompat%C3%ADvel-com-a-categoria-xxx-do-trabalhador-Rubricas-de-incid%C3%AAncia-de-IRRF-iguais-a-14-34-54-94-9024-9034-9054-9834-s%C3%B3-s%C3%A3o-aceitas-para-categoria-do-grupo-empregado-1xx
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22967318838935)** Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Ao transmitir o evento S-1200 ou S-2399 para funcionários sem vinculo (TSV) ocorre erro: A Rubrica xxx é incompatível com a categoria xxx do Trabalhador. Rubricas de incidência de IRRF iguais a [14, 34, 54, 94, 9024, 9034, 9054, 9834] só são aceitas para categoria do grupo empregado [1xx].  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**

Para que seja realizado o ajuste desta mensagem, é necessário **verificar se a categoria do contribuinte** está correta, estando certa, será necessário que **verifique se o código de incidência da rubrica** é **compatível com a categoria** do contribuinte.

Se for o caso contribuinte individual, não podem ser utilizadas rubricas com incidências que sejam específicas de segurados empregados. Portanto, não são aceitas rubricas cujo:

* Código de Incidência de Contribuição Previdenciária igual a 12, 21, 22, 32, 51, 92, 93 e 94, exceto se categoria de trabalhador for igual à 771;
* Código de Incidência de IRRF igual a 12, 13, 14, 32, 33 e 34;
* Código de Incidência de Contribuição Previdenciária igual a 34 se a categoria do contribuinte individual for diferente de 711, 712 e 734;
* Código de Incidência de Contribuição Previdenciária igual a 31 se a classificação tributária do contribuinte for igual a 21 ou 22 - Pessoa Física e Categoria igual à 7XX, pois não existe previsão legal de desconto de contribuição do contribuinte individual que é contratado por outro contribuinte individual, exceto se o tipo de Lotação da respectiva lotação igual à 22 - obra de pessoa física.  
    
  **Importante**: O eSocial prevê o pagamento de PLR - Participação de Lucros e Resultados para funcionários celetistas, não sendo válido para estagiários e funcionários sem vinculo.  
    
  Regra de validação eSocial - [REGRA\_RUBRICA\_COMPATIVEL\_CATEGORIA](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/regras.html)  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/22967318839191)  
    
    
  **Saiba Mais**Para saber mais consulte os *links* abaixo:   
  [eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
  [MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
  [Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  [ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
