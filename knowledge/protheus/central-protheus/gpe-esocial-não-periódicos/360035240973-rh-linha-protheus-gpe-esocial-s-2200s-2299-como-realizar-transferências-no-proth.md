---
article_id: 360035240973
category: GPE - eSocial - Não Periódicos
content_hash: 1d04391cf3fbfb31a81c063f97a468dc13beba8bdf5378beb0f62bedfc884963
fetched_at: '2026-06-28T22:45:04.622002+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200/S-2299 - Como realizar Transferências
  no Protheus com SIGAMAT/Bases/Ambientes diferentes e Empresas de CNPJ raiz diferente
type: support-article
updated_at: '2026-06-16T13:34:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035240973-RH-Linha-Protheus-GPE-eSocial-S-2200-S-2299-Como-realizar-Transfer%C3%AAncias-no-Protheus-com-SIGAMAT-Bases-Ambientes-diferentes-e-Empresas-de-CNPJ-raiz-diferente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41262125747863) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como realizar Transferências no **Protheus** com SIGAMAT/Bases/Ambientes diferentes e Empresas de CNPJ raiz diferente?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**  
O procedimento abaixo é utilizado quando a empresa **Origem** é Protheus e a empresa **Destino** será outro sistema, ou um sistema Protheus que não está na mesma base de dados. O caminho correto é realizar uma **Transferência Externa** para gerar o S-2299 na Empresa origem e realizar uma Admissão preenchendo a rotina de Sucessão de Vínculo para gerar um Evento S-2200 na Empresa destino.  
  
Para gerar o evento S-2299 na Empresa origem, acesse o artigo abaixo:  
[MP - GPE - eSocial - S-2299 - Preciso fazer a Transferência de trabalhadores do Protheus para uma empresa que não utiliza o Protheus, como fazer isso no sistema](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023167651)  
  
Para gerar o evento S-2200 na Empresa destino,  basta realizar uma admissão normal, preenchendo as informações originais do Trabalhador, porém, é obrigatório o complemento de preenchimento da rotina de Sucessão de Vínculos com as informações da Empresa origem para que o Sistema gere um Evento S-2200 com as informações previstas pelo leiaute do eSocial.  
  
No menu padrão a rotina de Sucessão de Vínculos fica em Atualizações > Funcionários > Sucessão de Vínculos.  
  
**![](https://totvssuporte.zendesk.com/attachments/token/TCIhe2hjhKYKGF9reMmk7Z9aD/?name=inline1333118276.png)​**  
  
Obs: Essas orientações são para os casos onde existe bases separadas sendo todas **Protheus**.  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)  
  
Para conhecimento dos eventos futuros, acessa a nossa página [*TOTVS Informa*](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos".
