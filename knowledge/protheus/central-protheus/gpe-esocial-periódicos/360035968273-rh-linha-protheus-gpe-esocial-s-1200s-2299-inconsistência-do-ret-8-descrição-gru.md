---
article_id: 360035968273
category: GPE - eSocial - Periódicos
content_hash: 7f70a1296e88a4b701374a86da8df59daade12b9d6779c02471b9fd7bc66b20d
fetched_at: '2026-06-28T22:45:08.828137+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Inconsistência do RET
  - 8 - Descrição: Grupo Remuneração no período de apuração ou períodos anteriores
  deve ser preenchido.'
type: support-article
updated_at: '2026-03-14T11:48:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035968273-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Inconsist%C3%AAncia-do-RET-8-Descri%C3%A7%C3%A3o-Grupo-Remunera%C3%A7%C3%A3o-no-per%C3%ADodo-de-apura%C3%A7%C3%A3o-ou-per%C3%ADodos-anteriores-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27445504228503) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
S-1200/S-2299 - Inconsistência do RET - 8 - Descrição: Grupo Remuneração no período de apuração ou períodos anteriores deve ser preenchido.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**  
Esta mensagem de erro é apresentada quando não são geradas Verbas/Rubricas e/ou Valores no evento S-1200/S-2299 na aba de demonstrativo de Valores.  
  
Em muitos casos a mensagem é apresentada quando o evento S-1200 de trabalhadores desligados em períodos anteriores tem "Diferença de Pagamento / Diferença de Dissidio" calculado no Protheus para esse período com erro.   
  
**Solução**  
Acesse o evento S-1200 no TAF (módulo 84), no caminho: *Atualizações > Eventos eSocial > Eventos Periódicos > Folha de Pagamento.*  
  
Na rotina de Folha de Pagamento filtre o Trabalhador com inconsistência e pressione a opção Visualizar ou Alterar e verifique se há informações na aba Demonstrativo de Valores.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046204374)  
  
Caso hajam informações, verifique se todos os campos estão preenchidos de acordo com o leiaute do eSocial para a esse Trabalhador.  
  
Caso contrário, na maioria dos casos analisados o erro ocorre porque esse Trabalhador tem direito a "Diferença de Pagamento / Diferença de Dissidio" e não foi utilizada a rotina de Dissidio Retroativo do SIGAGPE ou não observado os demais parâmetros para sua integração com o TAF.  
  
Neste cenário você deve refazer as validações dos artigos relacionados abaixo e retransmitir o evento do GPE ao TAF:

* [RH - Linha Protheus - GPE - eSocial - Parâmetros 3ª Fase esocial (Periódicos)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004981112)
* [RH - Linha Protheus - GPE - eSocial - Como o eSocial vai apurar os encargos nos casos de Reajuste/Dissidio Retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342453)
* [RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar informações de dissidio e rescisão complementar por dissidio no esocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013552271)

Caso mesmo assim a inconsistência persista, verifique:

* Foi utilizada a rotina de Dissidio Retroativo?
* A Data Acordo, Tipo de Aumento, Sindicato das tabelas S126 e S050 são os mesmos informados na rotina de Dissidio Retroativo?
* No caso de rescisão complementar, quando ocorreu a rescisão e quando ocorreu a rescisão complementar?

**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://informa.totvs.com/)   
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Para conhecimento dos eventos futuros, acessa a nossa página [***TOTVS Informa***](https://informa.totvs.com/) selecione em categorias a área e pesquise por "**Eventos**".
