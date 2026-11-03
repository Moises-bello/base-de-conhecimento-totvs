---
article_id: 360016520192
category: GPE - eSocial - Periódicos
content_hash: ff0a84dc7265e2416942d7237a7d494776e7da69a88e04bbf13c5e22fecbd7a6
fetched_at: '2026-06-28T22:45:07.433982+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1299 - Inconsistência do RET - 163
  - O Trabalhador sem vinculo com Nome : X, CPF : X, NIS : X e Categoria : X consta
  na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração'
type: support-article
updated_at: '2025-07-25T20:51:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016520192-RH-Linha-Protheus-GPE-eSocial-S-1299-Inconsist%C3%AAncia-do-RET-163-O-Trabalhador-sem-vinculo-com-Nome-X-CPF-X-NIS-X-e-Categoria-X-consta-na-base-de-dados-do-Ambiente-Nacional-do-eSocial-mas-n%C3%A3o-foi-informada-sua-remunera%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31644816867991) Tempo aproximado para leitura: 00:03:00 min  
  
Ocorrência**Inconsistência do RET - 163 - O Trabalhador sem vinculo com Nome : X, CPF : X, NIS : X e Categoria : X consta na base de dados do Ambiente Nacional do eSocial, mas não foi informada sua remuneração  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O Retorno de Inconsistência do RET é devido haver o registro de um Trabalhador na base do Governo informado através de um evento S-2190 ou S-2300, porém não há um evento de remuneração (exemplo: S-1200) para ele no período a que se referente o evento S-1299.  
Muitos casos relatados estão relacionados a Trabalhadores Sem Vínculo (Autônomos) que prestam serviços esporadicamente e consequentemente não recebem contraprestação de seus serviços em todos os meses.  
Essa mensagem de Inconsistência também pode ser gerada quando tem a situação acima e tenta integrar o evento S-1299 de uma Filial, porém o evento já havia sido retornado consistente quando enviado através da empresa Matriz.  
  
**Solução**Para solucionar essa ocorrência, efetue as seguintes validações:  
**1.** Conforme descrito na tabela de regras do **eSocial** "**REGRA\_VALIDA\_FECHAMENTO\_FOPAG**" existindo um ou mais trabalhadores **TSV** **ativos** no período de apuração da folha de pagamento e para os quais não tenha sido enviado o respectivo evento de remuneração, o evento de fechamento é aceito como válido, no entanto, são gerados **ALERTAS** contendo o **Nome**, **CPF** e **NIS** dos trabalhadores para os quais **não foi prestada a informação de remuneração**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14806213401623)  
  
**2.** Para casos em que há obrigação do envio do evento **S-2200 ou S-2300** é obrigatório o envio de um evento de remuneração (exemplo: S-1200), com exceção dos Trabalhadores em determinadas situação de afastamento preestabelecidas no leiaute do **eSocial** (exemplo: auxílio doença).  
  
**3.** Verifique se o evento S-1299 foi gerado através da empresa Matriz, o **eSocial** só aceita um evento por raiz de CNPJ e quando é enviado um segundo evento por uma Filial o RET apresenta a mensagem mencionada, porém ela não é a origem da inconsistência  
  
**Observação**  
Vale ressaltar que esta é uma mensagem de inconsistência retornada pelo RET (Governo) e não necessariamente relacionada a uma inconsistência na base do Sistema, sendo assim, para outras orientações e soluções formule um questionamento diretamente ao RET (Governo) através do Fale Conosco no portal do e-Social.   
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
