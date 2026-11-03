---
article_id: 4470748266775
category: RH – DIRF
content_hash: 17469910aa612b4236f31b036951b935f8dfafdc4833af10279811c9d3f5b620
fetched_at: '2026-06-28T22:44:07.896290+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - De onde o Sistema busca as informações do bloco
  DECPJ
type: support-article
updated_at: '2025-08-19T20:46:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4470748266775-RH-Linha-Protheus-GPE-De-onde-o-Sistema-busca-as-informa%C3%A7%C3%B5es-do-bloco-DECPJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34269972324119) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**De onde o Sistema busca as informações do bloco DECPJ?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**O sistema busca os dados do bloco DECPJ ou de acordo com os parâmetros da rotina Arquivo Magnético ou quando há determinados valores/blocos no arquivo magnético, conforme abaixo:

- Efetuou pagamentos a plano privado de assistência à saúde - coletivo empresarial  
Sim quando existe o bloco PSE no arquivo magnético

- Administrados ou intermediário de fundo de clube de investimentos  
No sistema, sempre Não

- instituição Financeira que na condição de depositária de crédito efetuou pagamento de rendimentos decorrentes de decisão judicial do trabalho  
Será de acordo com a pergunta do arquivo magnético  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4470630210327)  
- Efetuou pagamentos a residentes no exterior  
Sim se no arquivo magnético existir o bloco VRPDE

- Sócio ostensivo  de sociedade em consta de participação  
Será de acordo com o preenchimento da pergunta ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4470661575575)  
- União detém maioria do capital social sujeito a voto, recebe recursos  do tesouro nacional e esta obrigada a registrar a execução  orçamentaria Siafi. Sim caso exista o bloco VPEIM no arquivo magnético e Natureza declarante seja 0, 1 ou 3

- Declaração Situação especial  
Será preenchido de acordo com o preenchimento das perguntas ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4470724026391)

**Saiba mais**  
[RH - Linha Protheus - GPE - Passo a Passo para geração do Arquivo magnético da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022076092)

[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
