---
article_id: 360038006853
category: GPE - eSocial - Não Periódicos
content_hash: 2d678174a09cae82e25c47a242773dcd5ed34f4649cdf3a8ed96a9f0fb0bfcd5
fetched_at: '2026-06-28T22:45:04.471578+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2200 - Como deve ser gerado o S-2200
  no Protheus nos casos de transferências com RAIZ de CNPJ diferentes onde a empresa
  Origem não é Protheus ou não pertence a mesma base de dados/SIGAMAT
type: support-article
updated_at: '2026-06-16T13:33:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038006853-RH-Linha-Protheus-GPE-eSocial-S-2200-Como-deve-ser-gerado-o-S-2200-no-Protheus-nos-casos-de-transfer%C3%AAncias-com-RAIZ-de-CNPJ-diferentes-onde-a-empresa-Origem-n%C3%A3o-%C3%A9-Protheus-ou-n%C3%A3o-pertence-a-mesma-base-de-dados-SIGAMAT
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30373351541911) Tempo aproximado para leitura: 00:05:00 min  
  
Dúvida**Como deve ser gerado o S-2200 no **Protheus** nos casos de transferências com RAIZ de CNPJ diferentes onde a empresa Origem não é **Protheus** ou não pertence a mesma base de dados/SIGAMAT?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Não é possível fazer a transferência de forma automática quando ocorre de uma empresa que não utiliza o Protheus ou não está dentro da mesma base de dados.   
  
Nesse caso na empresa Origem deve existir o **S-2299** como motivo de desligamento para o **eSocial** 11, 12 ou 13. E na empresa Destino deve ser gerado o **S-2200** com dados da Sucessão de Vínculo.  
  
Abaixo demonstro com prints as principais informações do S-2200 na empresa Destino.

1. **Cadastro de Funcionários:**  
*Caminho: atualizações >Funcionários > Funcionários*

* O tipo de admissão deve ser preenchido com a informação de Transferência;
* A data de admissão é a mesma data que o trabalhador tinha na empresa origem.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049182634)  
  
2. **Cadastro de Sucessão de Vínculos:**  
*Caminho: atualizações >Funcionários > Sucessão de**Vínculos*

* Nesse cadastro deve ser preenchida as informações de sucessão de vinculo, ao aperta a tecla **F1** dentro de cada campo é possível ver o descritivo do que deve ser preenchido;
* Obs: O campo Matricula deve ser preenchido com a Matricula utilizada para o **eSocial** na empresa anterior.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050073353)

3. **Trabalhador no TAF:***Caminho: atualizações > eventos eSocial > Trabalhador > Cadastro Trabalhador*

* No TAF é gerado o evento S-2200 para esse trabalhador com as informações da Sucessão de Vínculo.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049182954)  
  
Consulte Também: [Como realizar Transferências no Protheus com SIGAMAT/Bases/Ambientes diferentes e Empresas de CNPJ raiz diferente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035240973)   
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Artigos S-2200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052505613)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw) [MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
